# n00bSKILL

Skills for AI agents. Most of them are about writing, in Danish and in English. Each skill has its own folder with a README that explains what it does and how to install it.

## Skills

| Skill | What it does |
| --- | --- |
| [`englisher`](skills/englisher/) | Writes and edits English copy that doesn't read like AI wrote it. It catches inflated claims, sales language, vague sources, formulaic rhythm, chatbot artifacts, and over-hedging. It's the English counterpart to `danisher`. |
| [`danisher`](skills/danisher/) | Writes and edits Danish copy that doesn't read like translated English. It catches word-for-word English idioms, missing modal particles (*jo*, *da*, *vel*), compounds split into separate words (*særskrivning*), English number and date formats, and flat AI enthusiasm. |
| [`danish-report-writer`](skills/danish-report-writer/) | Helps plan, draft, revise, and review reports that follow Danish conventions: the *problemformulering* (research question), the *synopsis*, sources and citations, report language, and front and back matter such as the title page, table of contents, and appendices. |
| [`presentation-design`](skills/presentation-design/) | Helps with slide structure, storytelling, and visual hierarchy. It has extra guidance for Microsoft technical decks and a script that fetches official Microsoft and Azure icons. |
| [`self-contained-output`](skills/self-contained-output/) | Removes leftover chat references from files that have to stand on their own, so scripts, READMEs, configs, and UI copy make sense to someone who never saw the conversation. |
| [`pnp-powershell-expert`](skills/pnp-powershell-expert/) | Helps write and debug PnP.PowerShell scripts for SharePoint Online. It covers the traps that fail silently or give misleading errors: `ReadOnlyEnforced` fields, video thumbnails, playlist lists, `Invoke-PnPSPRestMethod`, subweb scope, SPFx deploys, and link rewriting. |

## Repo layout

- `skills/<skill-name>/README.md`: what the skill is for and how to install it
- `skills/<skill-name>/SKILL.md`: the source skill
- `skills/<skill-name>/package/`: upload-ready `.skill` files, where a skill has one

## Versioning

Each skill has its own version number and follows semantic versioning. The version is in the `metadata.version` field of the skill's `SKILL.md`, and the skill's README has a changelog. Each release is tagged `<skill-name>-v<version>`, for example `danisher-v1.2.0`.

## License

MIT
