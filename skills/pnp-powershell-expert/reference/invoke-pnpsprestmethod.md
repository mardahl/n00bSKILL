# Invoke-PnPSPRestMethod gotchas + Graph identifier resolution

## Invoke-PnPSPRestMethod gotchas

- **URL:** must start with `/` (server-relative, e.g. `/_api/web/...`) or be a full absolute URL. A bare `_api/...` throws "invalid request URI ... BaseAddress must be set".
- **POST/PATCH/MERGE body serialization:** the cmdlet forwards `-Content` unchanged **only** when the value's runtime type is recognised as a string (`Content is string ? Content.ToString() : JsonSerializer.Serialize(Content, ...)`), and otherwise serializes whatever object it received. Passing a `Hashtable` mishandles nesting (symptom: "unexpected 'StartObject' node ... 'PrimitiveValue' node was expected"). Pre-serializing first helps:
  ```powershell
  $bodyJson = $body | ConvertTo-Json -Depth 10
  Invoke-PnPSPRestMethod -Method Post -Url $url -Content $bodyJson -ContentType "application/json;odata=verbose" -Connection $c
  ```
  **But pre-serializing is not always sufficient.** A PowerShell object wrapper can still reach that check, fail `is string`, and get serialized as the wrapper — producing a body of `Members`/`BaseObject` and a server error naming a property you never sent:
  `The property 'Members' does not exist on type 'SP.List'`. The same symptom appears on `RenderListDataAsStream` POSTs (`The parameter Members does not exist in method RenderListDataAsStream`). It is not a permissions or read-only error, and no amount of body-encoding tweaking fixes it from the calling side. **When you see `Members` in a server error, stop using this cmdlet for that call** and use CSOM, or build the request yourself:
  ```powershell
  $token = Get-PnPAccessToken -ResourceTypeName SharePoint -Connection $c
  Invoke-WebRequest -Method Post -Uri $absoluteUrl -Body ([System.Text.Encoding]::UTF8.GetBytes($bodyJson)) `
    -Headers @{ Authorization = "Bearer $token"; "X-HTTP-Method" = "MERGE"; "IF-MATCH" = "*" } `
    -ContentType "application/json;odata=nometadata"
  ```
- **`-Method Merge` and `Patch` do exist** (the `HttpRequestMethod` enum has `Get, Head, Post, Put, Delete, Trace, Options, Merge, Patch`). `Merge` adds `X-HTTP-Method: MERGE` and `IF-MATCH: *` for you, and `Delete` adds `IF-MATCH: *`. There is no parameter for custom headers, so anything else must be built with `Invoke-WebRequest`.
- **Accept header:** defaults to `application/json;odata=nometadata` **independently** of `-ContentType`. Verbose endpoints want both set to `odata=verbose`; pass `-Accept "application/json;odata=verbose"` explicitly.
- **`RenderListDataAsStream`** needs the view wrapped: `-Content @{ parameters = @{ ViewXml = $camlXml } }` (PascalCase `ViewXml`). Do NOT add `__metadata` unless the request is genuinely `odata=verbose` — with the default content type it errors as an unknown property.
- **Reading computed render values** (what a web part actually receives — e.g. thumbnail/preview URLs a list view computes) is best done via `RenderListDataAsStream`, since those are not stored list columns and won't appear in `Get-PnPListItem` field values.

**The same wrapper bug exists in `Invoke-PnPGraphMethod`.** It also `JsonSerializer.Serialize()`s `-Content` unconditionally. Feeding a PSObject-wrapped value (e.g. a PnP cmdlet's own GET response) into a Graph PATCH leaks phantom `Members`/`Properties` keys → Graph rejects with `Invalid property 'Members'`. Round-trip through `ConvertTo-Json | ConvertFrom-Json` to strip the wrapper, or drop to raw REST with `Get-PnPAccessToken -ResourceTypeName Graph`. See `entra-app-registration.md`.

## Resolving Graph identifiers from what you already know

You rarely need to hunt GUIDs. Resolve a site's Graph id from its URL, then chain:

```powershell
$web  = Get-PnPWeb -Connection $c
$site = Invoke-PnPGraphMethod -Url "sites/$($host):$($web.ServerRelativeUrl)" -Connection $c  # host = xxx.sharepoint.com
# $site.id is "host,siteCollectionId,webId" — usable directly:
$di = Invoke-PnPGraphMethod -Url "sites/$($site.id)/lists/$listId/items/$itemId/driveItem" -Connection $c
$driveId = $di.parentReference.driveId; $itemId2 = $di.id
```
