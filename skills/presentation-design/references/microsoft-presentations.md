# Microsoft Technical Presentations — Playbook

Patterns for IT Pro and cloud/enterprise-architect decks (Intune, Entra ID, Azure, Microsoft 365, Defender, Purview). Use with the core rules in `SKILL.md`.

## Deck archetypes

### 1. Architecture review
**Goal:** get a design endorsed or improved.
**Flow:** Context/constraints → Current state → Proposed architecture (one diagram, built progressively) → Key trade-offs (options compared) → Risks & mitigations → Decision asked for.
**Tips:** One decision per slide. Use a decision-record style ("We chose hub-spoke over flat VNet because…"). Put full topology in a backup slide.

### 2. Migration / rollout plan
**Goal:** align stakeholders on phases, risk, and timeline.
**Flow:** Why now → Scope (in/out) → Phases (wave plan) → Pilot results → Rollback plan → Timeline → Owners.
**Tips:** Before/after contrast. Show the pilot's hard numbers. Keep runbooks in backup.

### 3. Security posture / Zero Trust
**Goal:** show risk reduction and get sign-off on controls.
**Flow:** Threat/incident hook → Current gaps → Control changes (identity → device → app → data) → Evidence (sign-in logs, Secure Score, Defender) → Residual risk → Asks.
**Tips:** Lead with risk in business terms. Pair each control with the threat it removes. Cite exact numbers in notes, show the delta on-slide.

### 4. Product deep-dive / enablement
**Goal:** teach admins/engineers how something works.
**Flow:** Prerequisites → Concept → How it works (diagram) → Config (cropped portal / PowerShell) → Gotchas → Try-it / resources.
**Tips:** One feature per slide. 1-2 code blocks max. Real gotchas earn trust.

### 5. Customer workshop / discovery
**Goal:** facilitate, not lecture.
**Flow:** Outcomes for today → Current state questions → Options → Whiteboard/diagram → Agreed next steps.
**Tips:** Fewer slides, more interaction. Capture decisions live.

### 6. RFP / proposal readout
**Goal:** win or get approval.
**Flow:** Their problem → Recommended approach → Why us/why this → Scope & timeline → Commercials → Risks → Ask.
**Tips:** Pyramid principle — recommendation first. Commercials honest and clear.

## Product naming quick-reference (use current names)

| Use this | Not this |
| --- | --- |
| Microsoft Entra ID | Azure AD, AAD |
| Microsoft Entra (family) | — |
| Microsoft Intune / Intune Suite | Endpoint Manager, MEM, MEMCM |
| Microsoft Defender XDR | Microsoft 365 Defender |
| Microsoft Defender for Endpoint | Defender ATP |
| Microsoft Purview | Compliance Center, Azure Purview (for the unified service) |
| Microsoft 365 | Office 365 (when you mean the broader suite) |
| Microsoft Entra Connect | Azure AD Connect |
| Conditional Access | "CA policies" is fine as shorthand after first use |
| Windows Autopilot / Autopatch | — |
| Microsoft Entra Private Access / Internet Access (Global Secure Access) | — |

Mention a legacy name **once** for older audiences ("Microsoft Entra ID, formerly Azure AD"), then use the current name.

## Licensing cues to pre-empt

State the SKU when a feature depends on it (on-slide or in notes):
- **Entra ID P1** — Conditional Access, group-based licensing, dynamic groups.
- **Entra ID P2** — Identity Protection (risk policies), PIM, access reviews.
- **Intune Plan 1** — core MDM/MAM; **Plan 2 / Intune Suite** — Remote Help, Endpoint Privilege Management, advanced app management.
- **Defender for Endpoint P1 vs P2** — P2 adds EDR, threat & vuln management, automated investigation.
- **E3 vs E5** — E5 unlocks most advanced security/compliance (Defender XDR, Purview advanced, Entra ID P2).

Architects and buyers will ask; answering first builds trust.

## Code and query conventions

- **PowerShell:** prefer Microsoft Graph PowerShell SDK and `az`; avoid deprecated `MSOnline` / `AzureAD` modules in examples (call out if showing legacy for migration context).
- **Graph:** show the endpoint + the one property that matters; full payloads go to backup.
- **KQL (Sentinel / Defender / Log Analytics):** show the query and the single insight it produced, not raw result dumps.
- **Bicep/Terraform:** show the resource of interest, replace boilerplate with `// ...`, highlight the changed line.

## Diagrams to keep on hand

- Conditional Access signal→control flow
- Zero Trust pillars with explicit-verify points
- Hub-spoke / Azure landing zone
- Device lifecycle: Autopilot enroll → Intune configure → Defender protect → retire
- Hybrid identity: on-prem AD ↔ Entra Connect ↔ Entra ID
- Tenant-to-tenant migration / B2B collaboration

Build them from official icons (see Icons section in `SKILL.md` and `scripts/fetch_icon.py`). Keep one idea per diagram; reveal layers with progressive disclosure.

## Screenshot hygiene

- Crop to the single relevant setting; never paste a whole blade.
- Annotate (arrow/box) and give the slide an assertion title.
- **Redact** tenant names, UPNs, email, object/device IDs, IP addresses, license counts — treat as PII.
- Portal UIs change often; prefer a diagram or icon for anything meant to stay accurate over time.
