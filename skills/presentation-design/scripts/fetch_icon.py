#!/usr/bin/env python3
"""
fetch_icon.py — fetch official Microsoft / Azure product & architecture icons
for use in technical presentations and diagrams.

Primary human/browser source is msicons.com (https://msicons.com), a community
library of ~2,400 official Microsoft architecture icons by Daniel Bradley (MVP).
msicons.com is a client-rendered web app with no documented public API, so this
script provides a NON-INTERACTIVE fallback via the GitHub API:
  - PRIMARY: loryanstrant/MicrosoftCloudLogos — Microsoft cloud product/brand
    logos grouped by family (Entra, Intune, Defender, Purview, M365, Power
    Platform, Fabric...). Best for IT-Pro product marks.
  - COMPLEMENT: benc-uk/icon-collection — Azure architecture service icons
    (VMs, networking, Key Vault...), derived from Microsoft's official set.

Usage:
    # List matching icons (no download)
    python3 fetch_icon.py --list entra
    python3 fetch_icon.py --list ""          # list everything

    # Download the best match as SVG into a folder
    python3 fetch_icon.py "Microsoft Entra ID" --out ./public/images/icons/
    python3 fetch_icon.py "Intune" --out ./assets/icons/

    # Download every match for a term
    python3 fetch_icon.py "defender" --out ./icons/ --all

Notes:
    - Pure standard library (urllib). Python 3.8+.
    - GitHub API is rate-limited to 60 req/hr unauthenticated; the icon index is
      cached locally (default 7 days) so repeated runs are cheap.
    - If a product isn't found here, use msicons.com directly (see --help epilog).
"""

import argparse
import json
import os
import re
import sys
import tempfile
import time
import urllib.request
import urllib.error
from difflib import SequenceMatcher

# --- Sources -----------------------------------------------------------------
# Each source = a directory of .svg files in a public GitHub repo. The GitHub
# "contents" API returns name + download_url (raw) for every file.
SOURCES = [
    {
        "name": "loryanstrant/MicrosoftCloudLogos",
        "type": "tree",  # whole repo tree in one API call
        "api": "https://api.github.com/repos/loryanstrant/MicrosoftCloudLogos/git/trees/main?recursive=1",
        "raw_base": "https://raw.githubusercontent.com/loryanstrant/MicrosoftCloudLogos/main/",
        "prefix": "logos/",
        "note": "PRIMARY. Microsoft cloud PRODUCT logos grouped by family (Entra, Intune, Defender, "
                "Purview, Microsoft 365, Power Platform, Fabric...). AAD lives under the Entra folder.",
    },
    {
        "name": "benc-uk/azure-icons",
        "type": "contents",  # flat directory
        "api": "https://api.github.com/repos/benc-uk/icon-collection/contents/azure-icons?ref=master",
        "note": "Azure ARCHITECTURE service icons (VMs, networking, Key Vault...). Complements product logos.",
    },
    {
        "name": "benc-uk/azure-docs",
        "type": "contents",
        "api": "https://api.github.com/repos/benc-uk/icon-collection/contents/azure-docs?ref=master",
        "note": "Azure docs icons (broader service coverage).",
    },
]

# Synonyms bridge current product names to historical icon filenames.
# (Azure architecture icons still use older names like "Azure-Active-Directory".)
SYNONYMS = {
    "entra": ["entra", "active-directory", "azure-active-directory", "aad", "identity"],
    "entra id": ["entra", "active-directory", "azure-active-directory", "aad"],
    "azure ad": ["active-directory", "azure-active-directory", "aad", "entra"],
    "conditional access": ["conditional-access", "active-directory", "entra"],
    "intune": ["intune", "endpoint-manager", "managed-device", "device"],
    "endpoint manager": ["intune", "endpoint-manager"],
    "defender": ["defender", "security-center", "sentinel", "shield"],
    "defender for endpoint": ["defender", "security-center"],
    "purview": ["purview", "compliance", "information-protection"],
    "sentinel": ["sentinel", "security"],
    "m365": ["microsoft-365", "office", "office-365"],
    "microsoft 365": ["microsoft-365", "office", "office-365"],
    "autopilot": ["autopilot", "intune", "device"],
    "key vault": ["key-vault", "keyvault"],
    "log analytics": ["log-analytics", "monitor"],
}

CACHE_TTL_SECONDS = 7 * 24 * 3600
CACHE_FILE = os.path.join(tempfile.gettempdir(), "ms_presentation_icon_index.json")
USER_AGENT = "presentation-design-skill/0.3 (+https://msicons.com)"

MSICONS_HELP = """
If an icon isn't found here, use the primary library msicons.com directly:
  1. Open https://msicons.com  (or https://msicons.com/download for the full set)
  2. Search the product name (e.g. "Intune", "Entra", "Conditional Access")
  3. Download SVG (preferred — scales cleanly) or PNG at your chosen size
  4. Save into your deck's icon folder (public/images/icons or assets/icons)
Official Microsoft sources:
  - Azure architecture icons: https://learn.microsoft.com/azure/architecture/icons/
  - Microsoft 365 / Fabric / Power Platform icon sets on Microsoft Learn
"""


def _http_get(url, as_json=False):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/vnd.github+json" if as_json else "*/*"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    return json.loads(data) if as_json else data


def build_index(force=False):
    """Return list of {name, slug, download_url, source}. Cached locally."""
    if not force and os.path.exists(CACHE_FILE):
        age = time.time() - os.path.getmtime(CACHE_FILE)
        if age < CACHE_TTL_SECONDS:
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as fh:
                    return json.load(fh)
            except (json.JSONDecodeError, OSError):
                pass

    index = []
    errors = []
    for src in SOURCES:
        try:
            payload = _http_get(src["api"], as_json=True)
        except urllib.error.HTTPError as e:
            errors.append(f"{src['name']}: HTTP {e.code} ({e.reason})")
            continue
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            errors.append(f"{src['name']}: {e}")
            continue

        if src.get("type") == "tree":
            # Recursive git tree: one call returns every blob path in the repo.
            prefix = src.get("prefix", "")
            raw_base = src.get("raw_base", "")
            for node in payload.get("tree", []):
                if node.get("type") != "blob":
                    continue
                path = node.get("path", "")
                if not path.lower().endswith(".svg"):
                    continue
                if prefix and not path.startswith(prefix):
                    continue
                rel = path[len(prefix):] if prefix else path
                index.append({
                    "name": os.path.basename(path),
                    "slug": _slug(rel),          # includes product-family folder name
                    "download_url": raw_base + path,
                    "path": path,
                    "source": src["name"],
                })
        else:
            # Contents API: flat directory listing.
            for it in payload:
                if it.get("type") != "file":
                    continue
                name = it.get("name", "")
                if not name.lower().endswith(".svg"):
                    continue
                index.append({
                    "name": name,
                    "slug": _slug(name),
                    "download_url": it.get("download_url"),
                    "path": it.get("path", name),
                    "source": src["name"],
                })

    if not index and errors:
        sys.stderr.write("Could not build icon index:\n  " + "\n  ".join(errors) + "\n")
        sys.stderr.write(MSICONS_HELP)
        return []

    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as fh:
            json.dump(index, fh)
    except OSError:
        pass
    return index


def _norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# Generic tokens that should not, on their own, match an icon.
STOPWORDS = {"microsoft", "ms", "azure", "the", "for", "and", "of", "id", "a", "an"}


def _slug(s):
    return _norm(os.path.splitext(s)[0])


def _expand(query):
    """Return a set of normalized match terms (full phrase + words + synonyms)."""
    q = _norm(query)
    terms = set()
    if q:
        terms.add(q)  # full phrase
    for key, syns in SYNONYMS.items():
        nk = _norm(key)
        if nk and (nk in q or q in nk):
            terms.update(_norm(s) for s in syns)
    for w in q.split():  # individual words, minus generic stopwords
        if len(w) > 1 and w not in STOPWORDS:
            terms.add(w)
    return {t for t in terms if t and t not in STOPWORDS}


def score(query, entry):
    slug = entry["slug"]
    terms = _expand(query)
    if not terms:
        return 0.0
    best = 0.0
    for t in terms:
        if t == slug:
            best = max(best, 1.0)
        elif re.search(rf"\b{re.escape(t)}\b", slug):
            best = max(best, 0.9)
        elif t in slug or slug in t:
            best = max(best, 0.7)
        else:
            best = max(best, 0.5 * SequenceMatcher(None, t, slug).ratio())
    # De-prioritise retired/legacy variants so current marks win by default.
    path = entry.get("path", "").lower()
    if "zzformer" in path or "former" in path:
        best *= 0.55
    if re.search(r"/(?:19|20)\d\d", path):  # year-prefixed legacy subfolders
        best *= 0.7
    return best


def search(index, query, limit=15):
    if query.strip():
        scored = [(score(query, e), e) for e in index]
        scored = [x for x in scored if x[0] > 0.45]
    else:
        scored = [(0.0, e) for e in index]

    def sort_key(item):
        sc, e = item
        name = e["name"].lower()
        prefer_scalable = 0 if "scalable" in name else 1  # prefer vector "scalable" variant
        return (-sc, prefer_scalable, len(e.get("path", name)), name)

    scored.sort(key=sort_key)
    return scored[:limit] if limit else scored


def download(entry, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, entry["name"])
    data = _http_get(entry["download_url"])
    with open(dest, "wb") as fh:
        fh.write(data)
    return dest


def main():
    p = argparse.ArgumentParser(
        description="Fetch official Microsoft/Azure icons for presentations (msicons.com fallback).",
        epilog=MSICONS_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("query", nargs="?", default="", help='Product/icon name, e.g. "Microsoft Entra ID", "Intune".')
    p.add_argument("--out", default=".", help="Output directory for downloaded SVG(s). Default: current dir.")
    p.add_argument("--list", action="store_true", help="List matches only; do not download.")
    p.add_argument("--all", action="store_true", help="Download all matches, not just the best one.")
    p.add_argument("--limit", type=int, default=15, help="Max results to show/consider (0 = no limit).")
    p.add_argument("--refresh", action="store_true", help="Force-refresh the cached icon index.")
    args = p.parse_args()

    index = build_index(force=args.refresh)
    if not index:
        return 2  # build_index already printed guidance

    results = search(index, args.query, limit=args.limit)
    if not results:
        print(f'No icons matched "{args.query}".')
        print(MSICONS_HELP)
        return 1

    if args.list or not args.query.strip():
        print(f'{len(results)} match(es) for "{args.query}":')
        for sc, e in results:
            tag = f"{sc:.2f}" if args.query.strip() else "   -"
            print(f"  [{tag}] {e['name']}  ({e['source']})")
        if not args.query.strip():
            print("\nTip: pass a product name to download, e.g.  fetch_icon.py \"Intune\" --out ./icons/")
        return 0

    to_get = [e for _, e in results] if args.all else [results[0][1]]
    print(f'Downloading {len(to_get)} icon(s) for "{args.query}" → {args.out}')
    for e in to_get:
        try:
            dest = download(e, args.out)
            print(f"  ✓ {dest}")
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as ex:
            print(f"  ✗ {e['name']}: {ex}")
    print('\nVerify the icon is the current product mark. If not, grab it from msicons.com (see below).')
    return 0


if __name__ == "__main__":
    sys.exit(main())
