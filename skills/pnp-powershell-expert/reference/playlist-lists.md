# Playlist (video) lists

A SharePoint/M365 **Playlist** is not a special list type. It is `BaseTemplate 100` with the generic `TemplateFeatureId`, ordinary columns, and an ordinary `Type="HTML"` view. Nothing about the base template, content types, or column formatting identifies it. Two playlists in the same site have unrelated content-type GUIDs, so content type is never the marker.

What actually makes it render as a playlist is a **list-template marker** stored in the list's `AdditionalUXProperties` string:

```
{"TypeId":"3a867b4a-7429-0e1a-b02e-bf4b240ff1ce","Color":"0","Icon":"12"}
```

`TypeId` identifies the Microsoft list template. **The `Lists` site-template handler does not reproduce it.** A migrated playlist therefore keeps every column, every view, and even the correct view type, yet the client renders it as a plain table and clicking a row opens item details instead of a player.

Diagnosis-critical facts, each of which sends you the wrong way if you assume otherwise:

- The view's `ViewType2` is `PLAYLISTPLAYBACK`, and it **does** migrate correctly. Seeing it set on the target proves nothing and is not the fix.
- The view's `CustomFormatter` and `VisualizationInfo` are **empty on both sides**. Playlist rendering is not view formatting.
- The content type's `ClientFormCustomFormatter` is **empty on both sides**. It is not a custom display form either.
- The video-reference column is **hidden**, so any field dump that filters `Hidden` silently omits the single most relevant column.

Read the marker (this property is absent from Microsoft's published REST reference):

```powershell
Invoke-PnPSPRestMethod -Method Get -Connection $c `
  -Url "$($web.Url)/_api/web/lists/getbytitle('MyPlaylist')?`$select=Title,AdditionalUXProperties,Color,Icon"
```

`Color` and `Icon` are ALSO exposed as separate scalar list properties and compose into the same JSON, so `Set-PnPList -Color DarkRed -Icon Playlist` produces `{"Color":"0","Icon":"12"}` — correct colour and icon, **still no `TypeId`, still a plain table**. (`ListIcon.Playlist = 12`, `ListColor.DarkRed = 0`.) `TypeId` has no separate property; the whole string must be written.

Write it with CSOM, whose value is committed by the object model rather than a hand-built body:

```powershell
$list = Get-PnPList -Identity "MyPlaylist" -Connection $c
$list.AdditionalUXProperties = $valueCopiedFromSource
$list.Update(); Invoke-PnPQuery -Connection $c
# Re-fetch and assert — a clean return proves nothing (see "Never trust a silent success").
```

If the loaded client assembly lacks the property, fall back to a direct MERGE — **not** `Invoke-PnPSPRestMethod`, for the `-Content` reason in `invoke-pnpsprestmethod.md`:

```powershell
$token = Get-PnPAccessToken -ResourceTypeName SharePoint -Connection $c
$body  = @{ AdditionalUXProperties = $valueCopiedFromSource } | ConvertTo-Json -Compress
Invoke-WebRequest -Method Post -Uri "$($web.Url)/_api/web/lists/getbytitle('MyPlaylist')" `
  -Headers @{ Authorization = "Bearer $token"; Accept = "application/json;odata=nometadata"
              "X-HTTP-Method" = "MERGE"; "IF-MATCH" = "*" } `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -ContentType "application/json;odata=nometadata"
```

The value is JSON held **as a string**, so it must be escaped as a string inside the body, not embedded as a nested object. `ConvertTo-Json` does that; hand-built strings get it wrong.

## Playlist items point at videos, they do not contain them

The hidden `VideoIdentifiers` column holds a pointer:

```json
{"UniqueId":"<file guid>","Id":"<item id>","WebAbsoluteUrl":"https://host/sites/X",
 "ListFullUrl":"https://host/sites/X/Delte dokumenter","WebDavUrl":"https://host/sites/X/.../video.mp4"}
```

The referenced video can live in **any site collection**, commonly one outside the migration scope. Migrating the playlist without its videos yields items that look right and play nothing. The `Thumbnail` column (`ReadOnlyEnforced`, so settable only at item creation — see `silent-failures.md`) holds a separate `_api/v2.0/drives/{driveId}/items/{itemId}/thumbnails/...` URL that must be rebuilt against the target drive.

## Diagnosing "identical config, different rendering"

When every property you thought to compare matches and behaviour still differs, the property you did not think to compare is the cause. Stop naming candidates and enumerate:

1. Fetch the list and the view with **no `$select`** — the default projection returns everything the tenant exposes.
2. Probe uncertain names **one request each**, so an unknown name fails only itself. A single bad name in a shared `$select` fails the whole request and looks exactly like "the tenant does not expose this".
3. Read the list's **root folder property bag** (`web/lists(guid'..')/RootFolder/Properties`) — not covered by the `Lists` handler.
4. Diff source against target and ignore identifiers, URLs, counts, timestamps and localized labels.
