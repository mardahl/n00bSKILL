# Modern pages and web parts

- Parse a page's controls with the Pages API instead of regex over `CanvasContent1` (which is HTML-entity-encoded and painful):
  ```powershell
  $page = Get-PnPPage -Identity "MyPage.aspx" -Connection $c
  $page.Controls | ForEach-Object { $_.Type; $_.Title; $_.PropertiesJson }
  ```
- Web parts that show list-backed content (news, Stream/Playlist grids, highlighted content) usually render thumbnails from **per-item list columns**, not from anything baked into the page JSON. Fix the list item's column, not the page.
- The pages library is found by template, not title: `Get-PnPList -Includes BaseTemplate | Where-Object { $_.BaseTemplate -eq 119 }`.
