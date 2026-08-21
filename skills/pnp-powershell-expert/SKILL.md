---
name: pnp-powershell-expert
description: Use when writing, debugging, or reviewing PnP.PowerShell automation against SharePoint Online — uploading files, reading/writing list items, migrating content, working with modern pages/web parts, video thumbnails, Graph calls via Invoke-PnPGraphMethod, or REST via Invoke-PnPSPRestMethod. Covers silent write failures, read-only-enforced fields, localized list names, connection/variable pitfalls, and cmdlet gotchas that produce misleading errors.
---

# PnP.PowerShell (SharePoint Online)

## Overview

PnP.PowerShell wraps three different SharePoint APIs (CSOM, SharePoint REST, Microsoft Graph) behind PowerShell cmdlets. Most hard-to-diagnose bugs come from the wrapper hiding *which* API ran and *whether it actually succeeded*. The recurring failure mode is a cmdlet that returns no error while silently doing nothing.

**Core principle:** Never trust a no-error return. Re-fetch and assert the value actually changed. Version numbers incrementing is NOT proof a field write persisted.

**Ground cmdlet usage in current docs**, not memory: `https://github.com/pnp/powershell/tree/dev/documentation`. When behavior is ambiguous, reading the cmdlet's C# source under `https://github.com/pnp/powershell/tree/dev/src/Commands` resolves it fast — the source reveals which API the cmdlet calls and how it serializes input.

## Quick reference

| Symptom | Cause | Fix |
|---|---|---|
| `Set-PnPListItem` returns OK, version bumps, value unchanged | Field has `ReadOnlyEnforced="TRUE"` in SchemaXml | Set at item **creation** (`Add-PnPListItem`), not update. See `reference/silent-failures.md`. |
| `Get-PnPField` says `ReadOnlyField=False` but writes still fail | `ReadOnlyField` ≠ `ReadOnlyEnforced` (distinct attributes) | Inspect raw `$field.SchemaXml` — `reference/silent-failures.md` |
| Video files show generic icon, not a real frame thumbnail | Uploaded via `Add-PnPFile` (CSOM), which never triggers thumbnail generation | Re-submit bytes through Microsoft Graph driveItem `/content` — `reference/uploads-thumbnails.md` |
| `Invoke-PnPSPRestMethod`: "invalid request URI ... BaseAddress must be set" | URL missing leading `/` and not absolute | Use `/_api/...` (leading slash) or a full absolute URL |
| `Invoke-PnPSPRestMethod` POST body: "unexpected 'StartObject' node ... 'PrimitiveValue' expected" | Cmdlet's auto object→JSON serialization mishandles nested Hashtables | Pre-serialize: `$body \| ConvertTo-Json -Depth 10`, pass the **string** |
| Server error names a property you never sent (`Members`/`BaseObject`) | PowerShell object wrapper failed the cmdlet's `is string` check and got serialized as the wrapper | Stop using the cmdlet for that call — CSOM or raw `Invoke-WebRequest`. `reference/invoke-pnpsprestmethod.md` |
| `RenderListDataAsStream`: "Parameter viewXml does not exist" | Wrong param shape | Wrap in `parameters` object, PascalCase `ViewXml` |
| List not found by English title (e.g. "Site Pages") | Titles are localized per site language | Find by template: pages library is `BaseTemplate -eq 119` |
| A lookup that failed silently reuses an old value | Stale PowerShell variable across command blocks | Re-declare/reconnect per block, or `Remove-Variable` first |
| `Get-PnPListItem \| Where FileLeafRef -eq (Get-PnPHomePage)` finds nothing | `Get-PnPHomePage` returns a site-relative path; `FileLeafRef` is the bare filename | `Split-Path $homePage -Leaf` |
| "-SystemUpdate is not a parameter" | Removed in PnP 3.x | Use `-UpdateType SystemUpdate` |
| Subsite pages/items never scanned or written; report omits them | List/item/page cmdlets operate ONLY on the connected web — none has a `-Web` override | Enumerate `Get-PnPSubWeb -Recurse`, one connection per web — `reference/connections-scope.md` |
| File-existence check 404s for a file that provably exists in a subsite | `GetFileByServerRelativePath`/CSOM file lookup is web-scoped | Route to the deepest target web whose path prefixes the file |
| Graph `driveItem.webUrl` for `.docx/.xlsx/.pptx` is `.../Doc.aspx?sourcedoc={GUID}` | Office types return the web-editor redirect, not a path | Extract `sourcedoc` GUID, resolve via SP REST `GetFileById` — `reference/link-rewriting.md` |
| A `/r/` "copy link" resolves dead when pushed through Graph `/shares` | `/r/` links carry the literal path; only `/s/` links are opaque tokens | Route `/s/` to Graph, `/r/` to direct-path resolution |
| `Add-PnPSiteCollectionAppCatalog` / `Add-PnPApp -Scope Tenant` fails for a confirmed Global Admin | Cmdlets force a tenant-admin API context; SPO's internal tenant-admin flag doesn't reliably sync from Entra roles | Upload `.sppkg` via browser to app catalog — `reference/spfx-appcatalog.md` |
| Migrated video-playlist list renders as plain table; row click opens item details | `AdditionalUXProperties` template marker not reproduced by `Lists` handler | Copy whole `AdditionalUXProperties` string from source — `reference/playlist-lists.md` |
| A field you know exists never appears in your field dump | Dump filters `$_.Hidden`; playlist video-reference column is hidden by design | Never filter hidden fields in a diagnostic |
| `$select=SomeProperty` errors and you conclude the property "isn't exposed" | One unknown name fails the WHOLE request | Fetch default projection with no `$select`, probe uncertain names one request each |
| `Connect-PnPOnline ... -ClientId 31359c7f-...` fails with `AADSTS700016` | PnP Management Shell app retired Sept 2024 | Use `1950a258-227b-4e31-a9cf-717495945fc2` (Graph PowerShell bootstrap) or your own app — `reference/entra-app-registration.md` |
| `$app.AzureAppId` returns `$null` from `Get-PnPAzureADApp` | Property is named `AppId`, not `AzureAppId` | `$app.AppId` |
| Graph `PATCH` rejected with `"Invalid property 'Members'"` | PSObject-wrapped object serialized into the body | Round-trip `ConvertTo-Json \| ConvertFrom-Json` to strip wrapper — `reference/entra-app-registration.md` |
| Need sharing-link creation date; `Get-PnPSharingLink` has no such property | Graph `permission` object never exposes it; REST `GetSharingInformation` unreliable | CSOM `ObjectSharingInformation.GetListItemSharingInformation` — `reference/sharing-links.md` |
| Role-assignment dump includes `SharingLinks.*` entries | Synthetic system entries, not real grantees | Filter `Title -like 'SharingLinks.*'` out — `reference/sharing-links.md` |
| `Connect-PnPOnline` succeeds but every call 403s on a OneDrive site | Site is locked/deprovisioned (`LockState=NoAccess`); connect only acquires a token | Match 403 + `content type of the response is ""` — `reference/connections-scope.md` |

## Routing to reference files

- Silent writes, `ReadOnlyEnforced`, recreate-to-fix → **`reference/silent-failures.md`**
- Video thumbnails, CSOM-vs-Graph uploads → **`reference/uploads-thumbnails.md`**
- Playlist lists, `AdditionalUXProperties`, `VideoIdentifiers`, "identical config, different rendering" → **`reference/playlist-lists.md`**
- `Invoke-PnPSPRestMethod` body/URL/header gotchas, `RenderListDataAsStream`, Graph ID resolution → **`reference/invoke-pnpsprestmethod.md`**
- Modern pages, `CanvasContent1`, web parts → **`reference/pages-webparts.md`**
- Stale variables, subweb enumeration, web-scoped file checks → **`reference/connections-scope.md`**
- `.sppkg` deploys, tenant-admin permission trap → **`reference/spfx-appcatalog.md`**
- `/s/` vs `/r/` sharing links, `Doc.aspx` redirects, stock images, bare web URLs → **`reference/link-rewriting.md`**
- Retired PnP Management Shell client ID, `AppId` vs `AzureAppId`, Graph PATCH PSObject trap, app re-keying → **`reference/entra-app-registration.md`**
- Sharing-link creation dates via CSOM, synthetic `SharingLinks.*` role assignments → **`reference/sharing-links.md`**

## Idempotency and re-runnable migrations

For scripts run repeatedly against an evolving source (until a cutover):

- Make every mutation skip-if-already-correct (check the target's current state, not just a local checkpoint of processed source IDs).
- Checkpoint files that record "source item X processed" make a script resumable but NOT a true sync — they won't re-copy an item that changed on the source after it was first processed. If ongoing source edits must reach the target, compare content, don't skip by ID.
- Guard destructive steps (delete/overwrite) behind a re-fetch verification of the replacement.

## Common mistakes

- Trusting a cmdlet's return object instead of re-fetching to confirm a write.
- Reading `ReadOnlyField` and concluding a field is writable (check `SchemaXml` for `ReadOnlyEnforced`).
- Assuming `TypeAsString`/`FieldTypeKind` reflects a column's semantic type.
- Hardcoding English list/library titles on non-English sites.
- Expecting `Add-PnPFile` to produce video thumbnails.
- Passing nested Hashtables as `-Content` to `Invoke-PnPSPRestMethod` and getting a cryptic JSON node error.
- Connecting only to the root web and assuming subsite lists/pages are in scope.
- Running a web-scoped file-existence check from the root web against a subsite file and concluding it wasn't migrated.
- Treating Graph's `driveItem.webUrl` for an Office file as a path (it's the `Doc.aspx` editor redirect).
- Routing a `/r/` copy-link through Graph `/shares`, or anchoring a URL-capture regex to `https://host` so host-relative sharing links are missed.
- Guessing cmdlet syntax from memory instead of the dev-branch docs.
- Trusting Global Admin / "I created the site" as proof of SPO tenant-admin recognition for `Add-PnPSiteCollectionAppCatalog`/`Add-PnPApp -Scope Tenant` — verify via the token's `wids` claim, or upload the `.sppkg` through the browser instead.
- Filtering `Hidden` fields out of a diagnostic dump, then concluding a column doesn't exist.
- Putting an uncertain property name in a shared `$select`, getting an error, and recording it as "not exposed by this tenant" — one bad name fails the whole request.
- Comparing only the properties you thought of, then concluding "the config is identical" when behaviour still differs. Enumerate every property and diff; the cause is the one you didn't think to compare.
- Reading a server error naming a property you never sent (`Members`) as a permissions or read-only problem, rather than a client-side serialization bug.
- Treating distinct error strings as one "permission error." `Edm.Binary` = type serialization, `Members` = object wrapper, `AADSTS700016` = app consent. Each names a different layer; read them separately.
- Hardcoding the retired PnP Management Shell client ID `31359c7f-bd7e-475c-86db-fdb8c937548e` for interactive sign-in — browser shows `AADSTS700016`, MSAL listener never fires, console hangs until Ctrl+C.
- Guessing a cmdlet parameter exists. Test binding in isolation with `-ErrorAction Stop` on an unauthenticated session — no tenant needed to reproduce a binding error.
- Expecting `Get-PnPSharingLink` or REST `GetSharingInformation` to expose a link's creation date — only CSOM `ObjectSharingInformation` does.
- Treating `SharingLinks.*` role-assignment entries as real principals.
- Assuming `Connect-PnPOnline` failing is how you detect a locked site — it succeeds; the first CSOM call fails.
- Fixing a bug in `src/` while the user re-tests a stale derived artifact (a `dist/` build, a copied script). After the fix, rebuild and tell the user exactly which file to launch.
