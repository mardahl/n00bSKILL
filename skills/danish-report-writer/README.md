# Danish Report Writer

`danish-report-writer` helps AI agents plan, draft, revise, and audit Danish reports using Danish report-writing conventions: `problemformulering`, `synopsis`, `kilder`, `kildehenvisninger`, `rapportsprog`, `serviceafsnit`, and local `formalia`.

It is for students, workplace writers, and agents helping with Danish reports where the output must be useful to a defined reader rather than just sound academic.

## Kort på dansk

Brug `danish-report-writer`, når en dansk rapport skal have styr på `problemformulering`, `synopsis`, kilder, analyse, konklusion og formalia, før sproget bliver pudset af.

Den hjælper agenten med at stoppe op, før den bare skriver en pæn rapport om "noget med ...". Først skal læser, formål, krav, kilder og det egentlige spørgsmål være på plads.

Når rapporten hænger sammen fagligt, så kør gerne en sidste sprogpassage med [`humanizer-danish-addendum`](../humanizer-danish-addendum/). Den er bedre til den danske finish: stiv ChatGPT-dansk, oversatte engelske vendinger, konsulentsprog og den lidt for polerede tone.

## What To Install

Install the source skill folder:

`skills/danish-report-writer/`

For Claude Team/Enterprise or anyone who wants one upload-ready file, use:

[`package/danish-report-writer.skill`](package/danish-report-writer.skill)

Upload it in Claude Team/Enterprise under organization skills, then enable the skill for the relevant workspace or users.

## Files

- `SKILL.md`: installable source skill for opencode and Claude Code.
- `report-writing-source-notes.md`: paraphrased source notes from Omatskrive.dk's 12-part report-writing series.
- `README.md`: this landing page.
- `package/danish-report-writer.skill`: upload-ready Claude artifact.

## Install Locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/danish-report-writer/
.opencode/skills/danish-report-writer/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/danish-report-writer/
```

Restart the agent application after installing.

## Source Versus Package

`SKILL.md` is the source skill file. `report-writing-source-notes.md` is supporting reference material. The `.skill` file in `package/` is a zip archive renamed with the `.skill` extension for upload, not a separate skill folder.

## Attribution

This skill is based primarily on Per Salling's `Skriv bedre rapporter!` article series on [Omatskrive.dk](https://www.omatskrive.dk/rapportteknik/skriv-bedre-rapporter-serie/). Source notes are paraphrased and linked in `report-writing-source-notes.md`.
