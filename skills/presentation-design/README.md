# Presentation Design

`presentation-design` helps AI agents design, structure, and improve presentations, especially technical and Microsoft-focused decks for Intune, Entra ID, Conditional Access, Autopilot, Azure, Microsoft 365, Defender, and Purview.

It is for presenters, IT pros, architects, consultants, and agents building slide outlines, presentation narratives, technical diagrams, presenter notes, or slide-level reviews where clarity matters more than dense information dumps.

## What To Install

Install the source skill folder:

`skills/presentation-design/`

For Claude Team/Enterprise or anyone who wants one upload-ready file, use:

[`package/presentation-design.skill`](package/presentation-design.skill)

Upload it in Claude Team/Enterprise under organization skills, then enable the skill for the relevant workspace or users.

## Files

- `SKILL.md`: installable source skill for opencode and Claude Code.
- `references/microsoft-presentations.md`: Microsoft technical presentation playbook.
- `references/presentation-best-practices.md`: research notes behind the presentation rules.
- `scripts/README.md`: usage notes for icon fetching.
- `scripts/fetch_icon.py`: standard-library helper for fetching Microsoft and Azure icons.
- `package/presentation-design.skill`: upload-ready Claude artifact.

## Install Locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/presentation-design/
.opencode/skills/presentation-design/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/presentation-design/
```

Restart the agent application after installing.

## Source Versus Package

`SKILL.md`, `references/`, and `scripts/` are the source skill files. The `.skill` file in `package/` is a zip archive renamed with the `.skill` extension for Claude upload, not a separate skill folder.

## Attribution

This skill is a Microsoft-enhanced version of the original MIT-licensed `Presentation Design` skill by Roland Huss from [`rhuss/cc-slidev`](https://github.com/rhuss/cc-slidev). The Microsoft presentation additions, icon helper, and packaging in this repository are maintained as part of `n00bSKILL`.
