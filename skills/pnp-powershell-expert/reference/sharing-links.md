# Sharing-link metadata (creation date, etc.)

## Getting a sharing link's creation date

Neither Graph nor PnP.PowerShell sharing cmdlets expose when a link was created:

- `Get-PnPSharingLink` / `Get-PnPFileSharingLink` / `Get-PnPFolderSharingLink` return the Graph `permission` object shape — `Id`, `Roles`, `Link`, `LinkKind`, `SharingLinkStatus`, `Invitations`. **No `CreatedDateTime` exists.**
- SharePoint REST `_api/web/lists(...)/items(...)/GetSharingInformation` POST does not reliably return `sharingLinks` on current tenants — neither the light-JSON body (`maxLinksToReturn`, camelCase) nor the verbose-JSON typed body (`__metadata.type = 'SP.Sharing.SharingInformationRequest'`) works consistently.

**The only reliable source is CSOM `ObjectSharingInformation.GetListItemSharingInformation`:**

```powershell
$ctx = Get-PnPContext -Connection $conn
$osi = [Microsoft.SharePoint.Client.ObjectSharingInformation]::GetListItemSharingInformation(
    $ctx, [guid]$ListId, $ItemId, $false, $false, $false, $true, $true, $false)
$ctx.Load($osi)
$ctx.ExecuteQuery()

foreach ($sl in @($osi.SharingLinks)) {
    if ($sl.Url -and $sl.Created) {
        [pscustomobject]@{ Url = $sl.Url; Created = [string]$sl.Created }
    }
}
```

Traps:

- **`Created` is already a string** (e.g. `"2026-07-24T07:10:18.520Z"`), not a `DateTime`. Calling `.ToString('yyyy-MM-ddTHH:mm:ssZ')` on it crashes or mis-formats. Cast with `[string]$sl.Created` or pass through as-is.
- The boolean parameters to `GetListItemSharingInformation` are positional and easy to get wrong — signature is `(listId, itemId, excludeCurrentUser, excludeSiteAdmin, excludeSecurableObjects, retrieveAnonymousLinks, retrieveUserInfoDetails, checkForAccessRequests)`. For link enumeration you want `retrieveAnonymousLinks = $true` and `retrieveUserInfoDetails = $true`.
- Falls back to Unified Audit Log (`SharingSet` / `AnonymousLinkCreated` events) only when CSOM is not an option — audit requires logging to have been enabled at link-creation time, so it misses historical links.

## Filtering synthetic `SharingLinks.*` role assignments

When enumerating `roleassignments` via REST for a list item or folder, SharePoint injects synthetic entries whose `Title`/`LoginName` start with `SharingLinks.` — these are system scaffolding for sharing links, not real grantees:

```powershell
if ($Title -like 'SharingLinks.*' -or $Login -like '*SharingLinks.*') { return $null }  # not a principal
```

Exclude them from grant-classification logic or you'll misreport (or attempt to revoke) a non-principal.
