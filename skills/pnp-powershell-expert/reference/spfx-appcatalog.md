# Deploying SPFx solutions (.sppkg) — app catalog permission model

`Add-PnPSiteCollectionAppCatalog` and `Add-PnPApp -Scope Tenant`/`-Scope Site` all inherit from `PnPSharePointOnlineAdminCmdlet` or otherwise call a SPO **Tenant Administration** API (`Tenant.GetSiteByUrl`, `Tenant.SetSiteProperties`) regardless of which site the connection is pointed at. That API checks SPO's own internal tenant-admin flag on the signed-in account — a flag separate from, and not reliably synced with, Microsoft Entra directory roles.

This produces a specific, misleading failure pattern: every permission check you can verify comes back clean, yet the call still fails.

- SharePoint delegated scope on the token includes `AllSites.FullControl` ✓
- Token's `wids` claim includes the Global Administrator role template ID (`62e90394-69f5-4237-9190-012177145e10`) ✓
- `(Get-PnPWeb -Includes CurrentUser).CurrentUser.IsSiteAdmin` on the target site returns `True` ✓
- Still: `Add-PnPSiteCollectionAppCatalog` / `Add-PnPApp -Scope Tenant` throws a permission error, or (worse) `Add-PnPApp` returns **no error, no output, and no app added** — a silent no-op, not an exception. Check `Get-PnPApp -Scope Tenant` afterward; don't trust a clean return.

Being Global Admin does not imply SPO's internal tenant-admin recognition. Confirm the actual role by decoding the token rather than trusting the Entra portal's role list:

```powershell
$token = Get-PnPAccessToken
$payload = ($token -split '\.')[1]
while ($payload.Length % 4) { $payload += '=' }
$claims = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($payload.Replace('-','+').Replace('_','/'))) | ConvertFrom-Json
$claims.wids   # look for f28a1f50-f6e7-4571-818b-6a12f2af6b6c (SharePoint Administrator) alongside Global Admin's id
```

Note that classic **SharePoint Add-Ins** (the ACS-based add-in model, distinct from SPFx) were retired for all tenants as of April 2, 2026. Per Microsoft's retirement doc, once that retirement takes effect, admins "cannot add new SharePoint Add-Ins to the tenant and site collection app catalogs" — the site-collection-app-catalog machinery shares plumbing with the retired add-in model. SPFx itself (`.sppkg` packages) remains fully supported; only the legacy tenant-admin-gated catalog-management cmdlets are affected.

## Working path when the above is blocked

Skip the site-collection-scoped app catalog and PnP-driven uploads entirely.

1. Be added as an explicit **Site Collection Administrator** on the tenant App Catalog site itself (Owner/Global Admin is not sufficient for uploads to that library — this is a distinct ACL from being SCA on the target site).
2. Upload the `.sppkg` via browser directly: app catalog site → **Site Contents** → **Apps for SharePoint** library → drag-and-drop or **Upload**.
3. When prompted "make this solution available to all sites," leave it **unchecked** to keep the app scoped to whichever site(s) you explicitly install it on.
4. On the target site: **Site Contents** → **Add an app** → find it under **From Your Organization** → install.

This bypasses `Add-PnPApp`'s tenant-admin-context code path (and its no-script auto-toggle-and-revert behavior, which itself needs the same tenant-admin permission and can fail silently mid-flow) entirely, since browser uploads to this system library run under normal delegated site permissions, not the CSOM tenant-administration API.
