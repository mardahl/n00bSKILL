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

## Credits

- The [Humanizer skill by blader](https://github.com/blader/humanizer) was the initial inspiration for the writing skills `danisher` and `englisher`.
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, is the source for the general AI-writing patterns both skills check for.

Each skill's README lists any other credits for that skill.

## License

The skills are © 2026 Michael Mardahl and use two licences:

- **Skill text** (`SKILL.md`, reference files, READMEs and worked examples) is licensed under [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). The full text is in [`LICENSE`](LICENSE).
- **Code** (script files such as `fetch_icon.py`, and code blocks inside the Markdown files) is licensed under MIT. The full text is in [`LICENSE-MIT`](LICENSE-MIT).

Each skill folder has a `LICENSE.txt` with that skill's terms and any third-party notices. The file is also inside the `.skill` package.

Releases tagged before this change were published under MIT and stay MIT for anyone who already has them.

### How to credit

You may use, change and republish the skills, including commercially, as long as you:

1. Credit the author and link to the source.
2. Say that you changed the skill, if you did.
3. Publish your version under CC BY-SA 4.0 as well.

A credit line that meets the first point:

> Based on `<skill-name>` by Michael Mardahl, https://github.com/mardahl/n00bSKILL, licensed under CC BY-SA 4.0. Changes: `<what you changed>`.

Republishing a skill, or an adapted version of one, as your own work without this credit breaks the licence.

GitHub's **Cite this repository** button uses [`CITATION.cff`](CITATION.cff).
