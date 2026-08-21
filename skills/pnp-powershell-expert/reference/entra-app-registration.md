# Entra app registration for PnP.PowerShell

## Never use the retired PnP Management Shell client ID

The multi-tenant **PnP Management Shell** app (`31359c7f-bd7e-475c-86db-fdb8c937548e`) is **retired since September 2024**. Any code that hardcodes it for interactive/delegated sign-in:

```powershell
# DO NOT DO THIS — retired app, fails on any tenant that never consented it
Connect-PnPOnline -Url $url -Interactive -ClientId '31359c7f-bd7e-475c-86db-fdb8c937548e'
```

fails with `AADSTS700016` (app not found in tenant) on every tenant that doesn't already have its service principal. PnP.PowerShell has required callers to bring their own app registration since 2.x.

**Hung-session signature:** the failure mode is not a clean exception. The browser pops `AADSTS700016`, the MSAL localhost redirect listener never fires, and the PowerShell console hangs until Ctrl+C. If `Connect-PnPOnline -Interactive` hangs with a browser error, check the client ID first.

**Replacement for bootstrap/operator sign-ins** (app deletion, cert renewal, re-key, initial `Register-PnPAzureADApp`): use Microsoft's own multi-tenant **Microsoft Graph PowerShell** bootstrap client — the same one PnP.PowerShell's own `Register-PnPEntraIDApp*` cmdlets use:

```powershell
$bootstrapClientId = '1950a258-227b-4e31-a9cf-717495945fc2'  # Microsoft Graph PowerShell
Connect-PnPOnline -Url $url -Interactive -ClientId $bootstrapClientId -Tenant $tenant
```

It is pre-consented in any tenant that ever registered an app, so no per-tenant adminconsent dance is needed. For production scripts, register your own app with `Register-PnPAzureADApp` / `Register-PnPEntraIDAppForInteractiveLogin` and use its client ID instead.

## `Get-PnPAzureADApp` property-name trap

The cmdlet returns `AppId`, **not** `AzureAppId`. Reading `$app.AzureAppId` returns `$null` silently. Check property names with `Get-Member` before consuming.

## Graph `PATCH` with PSObject-wrapped bodies (phantom `Members`/`Properties`)

Objects returned by `Invoke-PnPGraphMethod` or PnP cmdlets are `PSObject`-wrapped. Serializing them straight back into a Graph `PATCH` body via `ConvertTo-Json` produces phantom `Members`/`Properties` keys, and Graph rejects with `"Invalid property 'Members'"`. Fix: round-trip through JSON to strip the wrapper before re-serializing:

```powershell
$clean = $obj | ConvertTo-Json -Depth 10 | ConvertFrom-Json
$body  = $clean | ConvertTo-Json -Depth 10 -Compress
```

## Re-keying an app registration: avoid `addKey`

Graph's `addKey` action requires the new key as **base64-encoded DER**, not the PEM string `New-PnPAzureCertificate` emits — and it requires a proof-of-possession JWT signed by an existing key on the app, which is useless for re-keying after key loss.

Use `PATCH keyCredentials` with the full existing-plus-new key set instead: it needs only Application Administrator and no proof JWT.

Working recipe — `New-PnPAzureCertificate`'s `.KeyCredentials` JSON already carries the base64 DER under `.value`, so extract from there rather than converting PEM yourself:

```powershell
$cert   = New-PnPAzureCertificate # ... usual args
$newKey = ($cert.KeyCredentials | ConvertFrom-Json).value   # base64 DER, ready for Graph

$app    = Get-PnPAzureADApp -Identity 'My-App-Name'
$appId  = $app.AppId   # NOT .AzureAppId — that property does not exist

$token  = Get-PnPAccessToken -ResourceTypeName Graph
$body   = @{ keyCredentials = @( <existing keys> + @{ usage='Verify'; type='AsymmetricX509Cert'; key=$newKey } ) } | ConvertTo-Json -Depth 10
Invoke-RestMethod -Method Patch -Uri "https://graph.microsoft.com/v1.0/applications(appId='$appId')" `
  -Headers @{ Authorization = "Bearer $token" } -Body $body -ContentType 'application/json'
```

## Parameter-binding bugs in PnP 3.3.0

`Get-PnPAccessToken -ResourceUrl` does not bind on PnP 3.3.0 — parameter-set resolution is broken. Use `-ResourceTypeName Graph` / `-ResourceTypeName SharePoint` instead.

Test parameter binding **in isolation** before debugging a full flow: run the single cmdlet with `-ErrorAction Stop` on an unauthenticated session — binding errors reproduce without needing a tenant, separating "parameter doesn't exist" from "auth failed."
