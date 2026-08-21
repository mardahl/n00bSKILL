# n00bSKILL

Reusable AI agent skills.

## Skills

| Skill | What it does | Start here |
| --- | --- | --- |
| [`englisher`](skills/englisher/) | Writes and edits English copy that does not read like AI wrote it. Catches inflated claims, sales language, vague sources, formulaic rhythm, chatbot artifacts, and over-hedging. English counterpart to `danisher`. | Open the skill folder. |
| [`danisher`](skills/danisher/) | Writes and edits Danish copy that does not read like translated English. Catches idiom calques, missing modalpartikler, særskrivning, English number and date format, and flat AI enthusiasm. | Open the skill folder. |
| [`danish-report-writer`](skills/danish-report-writer/) | Danish report-writing workflow for `problemformulering`, `synopsis`, sources, citations, report language, and service sections. | Open the skill folder. |
| [`presentation-design`](skills/presentation-design/) | Presentation design workflow for slide structure, storytelling, visual hierarchy, Microsoft technical decks, and official icon sourcing. | Open the skill folder. |
| [`self-contained-output`](skills/self-contained-output/) | Strips conversational bleed from standalone file deliverables, so scripts, READMEs, configs, and UI copy read as written for a stranger with zero chat context. | Open the skill folder. |
| [`pnp-powershell-expert`](skills/pnp-powershell-expert/) | PnP.PowerShell against SharePoint Online: silent write failures, `ReadOnlyEnforced` fields, video thumbnails, playlist lists, `Invoke-PnPSPRestMethod` traps, subweb scope, SPFx deploys, link rewriting. | Open the skill folder. |

## Repo layout

- `skills/<skill-name>/README.md`: install notes for that skill
- `skills/<skill-name>/SKILL.md`: source skill file
- `skills/<skill-name>/package/`: upload-ready files, when needed

## License

MIT
