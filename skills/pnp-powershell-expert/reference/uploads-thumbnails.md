# Uploads and video thumbnails (CSOM vs Graph)

`Add-PnPFile` uploads through the classic CSOM `Files.Add` path (chunked CSOM above ~10 MB). This path does **not** trigger SharePoint's backend video-thumbnail (frame-grab) generation — only files that pass through the Microsoft Graph driveItem ingestion pipeline (browser upload, sync client, or a direct Graph `PUT`) get a real thumbnail. CSOM-uploaded videos keep the generic file-type icon indefinitely.

Diagnose (empty array = no server-side thumbnail exists yet):

```powershell
$thumbs = Invoke-PnPGraphMethod -Url "drives/$driveId/items/$itemId/thumbnails" -Connection $c
```

Remediate by re-submitting the same bytes through Graph. Small files (≤4 MB) a single `PUT` to `/content`; larger files a chunked upload session (chunk size must be a multiple of 320 KiB). Get a bearer token with `Get-PnPAccessToken -Connection $c` for raw `Invoke-WebRequest` calls to a Graph URL, or for a pre-authenticated upload-session URL send chunks with a `Content-Range` header and NO `Authorization` header.
