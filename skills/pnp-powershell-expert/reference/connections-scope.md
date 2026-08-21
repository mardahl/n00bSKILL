# Connection pitfalls and subweb scope

## Connection and variable pitfalls

- A single delegated interactive connection *authenticates* against every site collection the signed-in user has rights to; you do not need a new app registration per site. **But authentication reach is not operating scope** — see below.
- **Stale variables bite hard.** When pasting sequential command blocks (or across sessions), a failed lookup leaves the previous run's value in the variable, and a later `$x["field"]` silently reads the wrong item. Re-declare and reconnect at the top of each self-contained block, or `Remove-Variable` the working set first. Verify a lookup succeeded (`if (-not $item) { throw }`) before using it.
- `Get-PnPHomePage` returns a **site-relative path** (`SitePages/Home.aspx`); list-item `FileLeafRef` holds only the **leaf filename**. Compare with `Split-Path $homePage -Leaf`.

## Subwebs (subsites) are out of scope by default

The most silent scope bug: `Get-PnPList`, `Get-PnPListItem`, `Set-PnPListItem`, and `Set-PnPPage` have **no `-Web` parameter**. They operate only on whichever web the `-Connection` was opened against (the docs say "the current web"). A connection to `/sites/intranet` therefore never sees or touches anything in `/sites/intranet/SubsiteA` — its lists, pages, and items are simply invisible. A script scanning only the root web silently skips all subsite content and reports nothing about it (no error, no "unresolved" — just absence).

There is no "one connection spans the whole tree" mode. To cover root + subwebs, enumerate and open one connection per web. Passing the existing root connection as `-Connection` on each reconnect reuses the cached MSAL auth for same-host reconnects, so this does **not** re-prompt for interactive login per subsite:

```powershell
$root = Connect-PnPOnline -Url $SiteUrl -Interactive -ClientId $appId -ReturnConnection
$webs = @($root) + @(
    Get-PnPSubWeb -Recurse -Connection $root |
    ForEach-Object { Connect-PnPOnline -Url $_.Url -Interactive -ClientId $appId -Connection $root -ReturnConnection }
)
foreach ($conn in $webs) {
    $pages = Get-PnPList -Connection $conn -Includes BaseTemplate | Where-Object { $_.BaseTemplate -eq 119 }
    foreach ($p in $pages) { Get-PnPListItem -List $p.Id -Connection $conn -PageSize 500 } # ...
}
```

Corollary — **file-existence checks are web-scoped too.** `GetFileByServerRelativePath` (or CSOM file lookup) run against the root web returns 404 for a file that exists in a subsite. Route the check to the deepest known web whose server-relative URL prefixes the file path (sort the web list longest-first), else you falsely conclude the file wasn't migrated.

## Detecting a locked / deprovisioned site

`Connect-PnPOnline` only acquires a token — it **succeeds even against a locked or deprovisioned site** (e.g. a OneDrive pending deletion after user removal, `LockState=NoAccess`). The lock only surfaces on the first real CSOM call (`Get-PnPWeb`, etc.).

Detect it by the specific error signature: HTTP **403 Forbidden** with an **empty response content-type**:

```powershell
if ($m -match 'content type of the response is\s*""' -and $m -match 'Forbidden') { # site is locked/deprovisioned
```

A genuine app-permission 403 always carries a non-empty JSON/XML body, so this pattern does not false-positive on real permission errors.
