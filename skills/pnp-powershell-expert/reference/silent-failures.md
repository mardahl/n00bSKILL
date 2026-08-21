# Silent failures and read-only-enforced fields

## Never trust a silent success

The single most important PnP.PowerShell habit. Many cmdlets commit an item update (incrementing its version) even when an individual field write was rejected server-side. A clean return proves nothing.

```powershell
Set-PnPListItem -List $list -Identity $id -Values @{ MyField = $newValue } -Connection $c
# Re-fetch FRESH and assert — do not read back the object the cmdlet returned.
$after = Get-PnPListItem -List $list -Id $id -Connection $c
if ($after["MyField"] -ne $newValue) { throw "write silently discarded" }
```

Apply this to any script that mutates SharePoint, especially before a destructive follow-up step (e.g. deleting an old item after "successfully" recreating it).

## Read-only-enforced fields (the silent-write trap)

Some columns — notably system-provisioned ones on modern list templates (Stream/Playlist video lists, etc.) — carry `ReadOnlyEnforced="TRUE"` in their field SchemaXml. Microsoft's [Field element schema](https://learn.microsoft.com/en-us/sharepoint/dev/schema/field-element-field) defines it as: *"the user cannot change the field by any means and that it can only be changed by the system."*

Critical traps:

- This is **distinct** from the standard `ReadOnly` attribute. `Get-PnPField` surfaces `ReadOnlyField` (from `ReadOnly`), which reads **False** — misleadingly suggesting the field is writable.
- `TypeAsString`/`FieldTypeKind` may report `Note` (plain text) even when the column is semantically something else (an Image/Thumbnail column). Storage type ≠ semantic type.
- An update (`Set-PnPListItem`, REST `PATCH`, CSOM `ListItem.Update()`) is silently dropped. The value can only be set **at item creation**.

Detect it by reading the raw schema, not the friendly properties:

```powershell
$field = Get-PnPField -List $list -Identity "FieldInternalName" -Connection $c
$field.SchemaXml   # look for ReadOnlyEnforced="TRUE"
```

Set it at creation via `Add-PnPListItem`, whose CSOM implementation (`list.AddItem()` + `SetFieldValues()` + a single `Update()`/`ExecuteQueryRetry()`) commits values as part of the create — the one window the attribute allows:

```powershell
$new = Add-PnPListItem -List $list -Values @{
    Title = $title
    FieldInternalName = $valueAllowedOnlyAtCreation
} -Connection $c
# Then verify by re-fetch (see "Never trust a silent success").
```

To fix an **existing** item's enforced field, you must recreate it (create-verify-then-delete-old), because in-place update is impossible by design. Guard the delete behind a successful re-fetch verification so a partial failure never loses the only copy.
