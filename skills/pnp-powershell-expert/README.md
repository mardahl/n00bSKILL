# PnP.PowerShell Expert

`pnp-powershell-expert` is an agent skill for writing, debugging, and reviewing PnP.PowerShell automation against SharePoint Online.

Use it when an agent is uploading files, reading or writing list items, migrating content, touching modern pages or web parts, dealing with video thumbnails, calling Graph via `Invoke-PnPGraphMethod`, or calling SharePoint REST via `Invoke-PnPSPRestMethod`.

It is for anyone running an AI agent against real SharePoint Online tenants, where the recurring failure mode is a cmdlet that returns no error while silently doing nothing.

## What it covers

- Silent write failures — cmdlets that bump the item version but drop the field write
- `ReadOnlyEnforced` fields (distinct from `ReadOnlyField`) — settable only at item creation
- Video thumbnails — why `Add-PnPFile` (CSOM) never triggers frame-grab generation, and the Graph fix
- Playlist (video) lists — the `AdditionalUXProperties` template marker the `Lists` handler drops
- `Invoke-PnPSPRestMethod` gotchas — the `Members`/`BaseObject` serialization trap and when to bypass the cmdlet
- Subweb scope — `Get-PnPList`/`Get-PnPListItem`/`Set-PnPListItem` have no `-Web` parameter
- SPFx `.sppkg` deploys — the tenant-admin permission trap and the browser-upload workaround
- Embedded-reference rewriting — `/s/` vs `/r/` sharing links, `Doc.aspx` redirects, stock images
- Localized list names, stale variables, idempotent migrations
- Entra app registration — the retired PnP Management Shell client ID trap, Graph PATCH PSObject serialization, app re-keying without a proof JWT
- Sharing-link metadata — creation dates via CSOM `ObjectSharingInformation` (Graph/PnP cmdlets don't expose them), synthetic `SharingLinks.*` role assignments
- Locked/deprovisioned site detection (the 403-with-empty-content-type signature)

## What to install

For Claude Team or Enterprise, upload this file under organization skills:

[`package/pnp-powershell-expert.skill`](package/pnp-powershell-expert.skill)

Then enable the skill for the relevant workspace or users.

For opencode and Claude Code, install this folder as a source skill. See install locations below.

## Files

- `SKILL.md`: the source skill — overview, core principle, quick-reference symptom table, routing to reference files
- `reference/silent-failures.md`: re-fetch verification pattern + the `ReadOnlyEnforced` trap
- `reference/uploads-thumbnails.md`: CSOM vs Graph uploads and video thumbnails
- `reference/playlist-lists.md`: playlist list marker, `VideoIdentifiers`, diagnosis playbook
- `reference/invoke-pnpsprestmethod.md`: SPRestMethod gotchas + Graph identifier resolution
- `reference/pages-webparts.md`: modern pages and web parts
- `reference/connections-scope.md`: connection pitfalls, subweb enumeration, web-scoped file checks
- `reference/spfx-appcatalog.md`: `.sppkg` deploys and the tenant-admin permission model
- `reference/link-rewriting.md`: post-migration embedded-reference rewriting
- `reference/entra-app-registration.md`: retired PnP Management Shell client ID, Graph PATCH traps, app re-keying
- `reference/sharing-links.md`: sharing-link creation dates via CSOM, `SharingLinks.*` filtering
- `README.md`: this landing page
- `package/pnp-powershell-expert.skill`: upload-ready Claude artifact

Source versus artifact: `SKILL.md` plus `reference/` is the source. The `.skill` file is a zip archive renamed with the `.skill` extension, containing `SKILL.md`, `reference/` and `README.md`. It is not a separate skill.

## Install locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/pnp-powershell-expert/
.opencode/skills/pnp-powershell-expert/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/pnp-powershell-expert/
```

Restart the agent application after installing.

## Attribution

Content distilled from real-world PnP.PowerShell migration and automation work against SharePoint Online tenants, contributed by the repository maintainer. Cmdlet behaviour references ground in the [PnP.PowerShell dev-branch docs and source](https://github.com/pnp/powershell).
