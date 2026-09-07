# CSOM raw calls, tenant admin API, and OneDrive admin audit/repair

## `ExecuteQueryRetry()` is an extension method — invisible from script scope

`$ctx.ExecuteQueryRetry()` works inside PnP.Framework-based modules because the
extension class is imported there. In a plain `.ps1` (or a scriptblock running
outside the module's session state) the method does not exist on the raw
`ClientContext`, and the call dies with a **RuntimeException**:

```
Method invocation failed because [PnP.Framework.PnPClientContext] does not
contain a method named 'ExecuteQueryRetry'.
```

From scripts, use the cmdlet instead — it wraps the same retry logic and runs
inside the module's session state where the extension is visible:

```powershell
$ctx = Get-PnPContext
$ctx.Load($props)
Invoke-PnPQuery -ErrorAction Stop     # not $ctx.ExecuteQueryRetry()
```

Same applies to `$ctx.ExecuteQuery()` — it exists, but you lose PnP's throttling
retry. Prefer `Invoke-PnPQuery` everywhere in `.ps1` code.

## Tenant admin API: what each cmdlet actually does

The tenant-side cmdlets wrap `Microsoft.Online.SharePoint.TenantAdministration.Tenant`
(CSOM). Knowing the mapping matters because the friendly names hide real gaps:

| Task | Correct call | Trap |
|---|---|---|
| Enumerate sites | `Get-PnPTenantSite -IncludeOneDriveSites -Detailed` | No `-Url` param — single-site fetch is `-Identity <url>` (alias `Url` exists on the parameter, but the **parameter name** is `Identity`). |
| Read primary site collection admin | `SPOSite.Owner` from the tenant record | This IS the primary admin — there is no separate "primary" field. May come back as a bare UPN **or** a claims login (`i:0#.f|membership|upn`) depending on API version — normalize before comparing. |
| Read the SCA ACL (all admins) | `Get-PnPSiteCollectionAdmin` **on a per-site connection** | Not exposed by the tenant model at all. Returns CSOM `User` objects (`Email`, `LoginName`, `IsSiteAdmin`). `Email` can be empty for system/guest entries — fall back to the `LoginName` claim. |
| Add an SCA | `Set-PnPTenantSite -Identity <url> -Owners <upn[]>` → `Tenant.SetSiteAdmin(url, login, $true)` | **Only adds.** Sets the account as *a* SCA; it becomes primary ONLY if no primary exists. It never replaces a wrong existing primary and never removes other admins. |
| Remove an SCA | `Tenant.SetSiteAdmin(url, login, $false)` via CSOM, or `Remove-PnPSiteCollectionAdmin` on a site connection | `Remove-PnPSiteCollectionAdmin` is **site-scoped** (sets `user.IsSiteAdmin = false` on the connected web) — needs a per-site connection. `SetSiteAdmin(...,$false)` works from the admin connection, no reconnect needed. |
| Set the PRIMARY admin explicitly | CSOM: `$tenant.GetSitePropertiesByUrl($url,$false)` → `$props.Owner = $upn` → `$props.Update()` → `Invoke-PnPQuery` | No PnP cmdlet exposes this. `Set-PnPTenantSite` has no parameter that replaces an existing primary. |

To drive CSOM `Tenant` from a script connected to the admin URL:

```powershell
Connect-PnPOnline -Url "https://<tenant>-admin.sharepoint.com" ...
$ctx    = Get-PnPContext
$tenant = New-Object Microsoft.Online.SharePoint.TenantAdministration.Tenant($ctx)
$tenant.SetSiteAdmin($siteUrl, $loginName, $false)   # remove SCA
Invoke-PnPQuery -ErrorAction Stop
```

## Auditing "is the user admin of their own OneDrive" at scale

The personal-site slug is a **lossy** encoding of the UPN: at provision time
`.` and `@` both flatten to `_`, and existing `_` in the local part also stays
`_`. So `abdulrahman_nur_dk_gt_com` could be `abdulrahman.nur@dk.gt.com` OR
`abdulrahman@nur.dk.gt.com` — the boundary is unrecoverable from the URL alone.

**Do not reverse the slug blindly.** A first-underscore split silently produces
a wrong UPN for every user in tenants whose UPN domain isn't derivable from the
tenant name (e.g. tenant `gtdk.onmicrosoft.com`, UPNs `@dk.gt.com`).

Reliable approaches, in order:

1. **Learn the UPN domains from the enumeration itself** — collect the domain of
   every tenant-record `Owner`, seed with the tenant domain, then match the slug
   against the `_`-flattened suffix (longest first, so `dk_gt_com` beats
   `gt_com`). Split at the suffix; `_`→`.` in the local part; append `@domain`.
2. **Forward-compare** — flatten each candidate identity (owner, SCA entries,
   site users) with `(upn -replace '[.@]','_').ToLower()` and check equality
   with the slug. Whichever identity flattens to the slug IS the user; no
   reversal needed. Use this as the fallback for unknown domains.
3. For repair when neither resolves: `Get-PnPUser` on the site — the user
   normally still exists in the site's user list even after losing SCA rights.

Secondary OneDrives for the same user get a numeric suffix on the whole slug
(`jane_doe_contoso_com1`) — strip `\d+$` before matching.

Filter noise out of the enumeration before scanning: `Template -like 'SPSPERS*'`
for personal sites, skip `ArchiveStatus -ne 'NotArchived'` (M365 Archive —
deleted/inactive users) and `LockState -ne 'Unlock'` (locked/deprovisioned).
A site archived between enumeration and connect still 403s with the empty
content-type signature — treat as skipped, not failed (see
`connections-scope.md`).

A healthy OneDrive has the user as primary admin (`Owner` matches) AND on the
SCA ACL. Both can be broken independently after bad migrations; flag both, and
also flag `Owner` empty (no primary admin set) and an empty SCA ACL.
