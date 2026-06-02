# Humanizer Danish

Looking for the Claude upload file? Use:

[`../../packages/humanizer-danish.skill`](../../packages/humanizer-danish.skill)

This folder is the source version of the skill. Claude's organization upload flow wants the packaged `.skill` file, not this folder and not `SKILL.md` by itself.

`humanizer-danish` is a combined Humanizer skill for Claude.ai Team and Enterprise organization skill upload. It includes the original Humanizer guidance plus the Danish-specific addendum in one uploadable package.

Use this when you want one skill that handles both general AI-writing tells and Danish-specific tells, rather than installing `humanizer` and `humanizer-danish-addendum` separately.

## Attribution

- Original Humanizer skill: [github.com/blader/humanizer](https://github.com/blader/humanizer)
- Original Humanizer creator: [blader](https://github.com/blader)
- Primary reference used by Humanizer: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Danish addendum: this repo's `humanizer-danish-addendum` skill

## Claude Team and Enterprise Organization Installation

Upload this file:

```text
packages/humanizer-danish.skill
```

The `.skill` file contains the complete skill folder and includes `SKILL.md`.

Organization owners can provision it for everyone:

1. Open `Organization settings > Skills` in Claude.
2. Enable `Code execution and file creation` and `Skills` if they are not already enabled.
3. In `Organization skills`, click `+ Add`.
4. Upload `packages/humanizer-danish.skill`.

Provisioned skills appear for members under `Customize > Skills`. Members can toggle the skill off, but only owners can add or remove organization-provisioned skills.

## Individual Claude.ai Installation

For personal use, upload the same package from `Customize > Skills`:

1. Click `+`.
2. Choose `Create skill`.
3. Select `Upload a skill`.
4. Upload `packages/humanizer-danish.skill`.
5. Toggle the skill on.

## Claude Code or opencode Installation

For local agent clients, copy the folder directly:

```text
skills/humanizer-danish/
```

Claude Code personal location:

```text
~/.claude/skills/humanizer-danish/
```

opencode global location:

```text
~/.config/opencode/skills/humanizer-danish/
```

Restart opencode after installing. Claude Code usually detects changes in existing skill directories, but restart if the directory did not exist when the session started.

## Package Structure

The upload artifact is a ZIP-format archive with this structure:

```text
humanizer-danish/
  SKILL.md
  README.md
```

Do not upload only `SKILL.md`; Claude organization upload expects an archive containing a skill folder with `SKILL.md` inside.
