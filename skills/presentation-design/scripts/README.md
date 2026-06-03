# Icon fetching for Microsoft presentations

The `fetch_icon.py` helper retrieves official Microsoft / Azure product and
architecture icons for slides and diagrams.

## Sources & order of preference

1. **[msicons.com](https://msicons.com) — primary library.** ~2,400 official
   Microsoft architecture icons, SVG/PNG at any size, by Daniel Bradley (MVP).
   It's a client-rendered web app with **no documented public API**, so fetch
   from it interactively:
   - With a browser tool (e.g. Claude in Chrome): navigate, search the product,
     download the SVG.
   - Bulk: `https://msicons.com/download` for the full library (grab once, reuse).
   - Manual: search the product name on the site and save into your deck.
2. **`fetch_icon.py` — scriptable fallback (no browser).** Pulls via the GitHub API from:
   - **`loryanstrant/MicrosoftCloudLogos`** (primary) — Microsoft cloud product
     logos grouped by family (Entra, Intune, Defender, Purview, Microsoft 365,
     Power Platform, Fabric...). Legacy Azure AD logos live under the Entra folder.
   - **`benc-uk/icon-collection`** (complement) — Azure architecture *service*
     icons (VMs, networking, Key Vault...), derived from Microsoft's official set.
   Good for non-interactive runs. The author of MicrosoftCloudLogos notes the marks
   are Microsoft's (no ownership/copyright claimed) — use per Microsoft's terms.
3. **Microsoft official downloads** — when you need the canonical pack:
   - Azure architecture icons: <https://learn.microsoft.com/azure/architecture/icons/>
   - Microsoft 365, Fabric, Power Platform icon sets on Microsoft Learn.

## Examples

```bash
# What's available for a term?
python3 fetch_icon.py --list entra
python3 fetch_icon.py --list defender

# Download best match (SVG) into a deck folder
python3 fetch_icon.py "Microsoft Entra ID" --out ./public/images/icons/
python3 fetch_icon.py "Intune" --out ./assets/icons/

# Grab every match for a term
python3 fetch_icon.py "defender" --out ./icons/ --all

# Refresh the cached index (after ~7 days, or to pick up new icons)
python3 fetch_icon.py --list "" --refresh
```

## Behaviour & limits

- Pure Python standard library; Python 3.8+. No `pip install` needed.
- The icon index is cached in your temp dir for 7 days (GitHub's anonymous API
  allows ~60 requests/hour).
- Synonyms map current names to legacy icon filenames — e.g. searching
  **"Entra"** also matches **Azure-Active-Directory** icons.
- Always sanity-check that the downloaded mark is the **current** product logo
  (Microsoft rebrands often). If it's stale or missing, use msicons.com.

## Usage rules (also in SKILL.md)

- Official icons only; one icon family per deck; never alter the marks.
- Pair every icon with a text label (color-blind + distracted-viewer safe).
- On dark slides, place blue/teal icons on a light chip for contrast.
- Microsoft icons are for architecture/diagram use under Microsoft's terms — do
  not imply partnership or endorsement.
