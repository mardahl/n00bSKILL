# Humanizer Danish Addendum

`humanizer-danish-addendum` is the single landing folder for this repo's Danish Humanizer guidance.

It contains the source Danish addendum for people who already run a Humanizer-style skill, and it also includes a ready-made `.skill` package for Claude Teams or anyone who wants a complete upload file.

The parent Humanizer skill catches structural patterns such as significance inflation, rule-of-three rhythm, generic positive conclusions, and promotional phrasing. This addendum covers Danish-specific tells: English idiom calques, translated syntax, Danish business filler, flat earnestness, low burstiness, and the risk of over-correcting legitimate Danish IT fagsprog.

## Ready-Made Claude Package

If you run Claude Team/Enterprise or just want one ready-made combined skill file, upload this package:

[`package/humanizer-danish.skill`](package/humanizer-danish.skill)

This package contains the complete combined `humanizer-danish` skill: the original Humanizer guidance plus this Danish addendum in one `.skill` upload file.

The package is an install artifact, not a separate repo skill folder. This folder remains the source and explanation for the Danish addendum.

Credit: this addendum is designed to complement the original [Humanizer skill by blader](https://github.com/blader/humanizer). The original Humanizer skill is based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide maintained by WikiProject AI Cleanup.

## Files

- `SKILL.md`: standalone discoverable skill for opencode and Claude Code.
- `README.md`: install, merge, and agent instructions.
- `package/humanizer-danish.skill`: ready-made combined Claude upload package.

## Use as a Companion Skill

This is the recommended setup. Keep your existing `humanizer` skill unchanged and install this skill next to it.

### opencode

Copy or symlink this folder into one of opencode's skill locations:

```text
~/.config/opencode/skills/humanizer-danish-addendum/
.opencode/skills/humanizer-danish-addendum/
```

Then restart opencode. opencode loads skills at startup.

When Danish text is involved, the agent should load both skills:

1. `humanizer` for general AI-writing patterns.
2. `humanizer-danish-addendum` for Danish-specific patterns.

### Claude Code

Copy or symlink this folder into Claude Code's skill location:

```text
~/.claude/skills/humanizer-danish-addendum/
```

Restart Claude Code or start a new session so the skill index refreshes.

When Danish text is involved, the agent should load both skills:

1. `humanizer` for general AI-writing patterns.
2. `humanizer-danish-addendum` for Danish-specific patterns.

## Merge into an Existing Humanizer Skill

Use this only if you want one combined Humanizer skill instead of two skills.

For opencode or Claude Code agents doing the merge:

1. Locate the existing `humanizer/SKILL.md`.
2. Keep the existing Humanizer frontmatter, name, and trigger description unless the user explicitly asks to change them.
3. Copy the body content from this skill starting at `# Humanizer Danish Addendum`.
4. Paste it into the existing Humanizer skill before the parent skill's final process/output section or near its language-specific guidance section.
5. Do not duplicate YAML frontmatter from this skill inside the parent skill.
6. Preserve the caveat about not over-correcting Danish IT fagsprog.
7. Restart the agent application after saving.

## Agent Instructions

When asked to humanize Danish text:

1. Apply the general Humanizer patterns first.
2. Run a Danish pass using D1-D5 from this addendum.
3. Treat the watch-list as judgment prompts, not mechanical rules.
4. Keep normal Danish IT terms and English technical vocabulary when they are standard practice.
5. Report briefly which Danish tells were removed.

## Why There Is One Folder

The Danish guidance lives in one repo folder to keep the install story simple. Local agent users can install only the addendum, while Claude Team/Enterprise users can upload the ready-made combined `.skill` file from `package/`.

## Attribution

- Original Humanizer skill: [github.com/blader/humanizer](https://github.com/blader/humanizer)
- Original Humanizer creator: [blader](https://github.com/blader)
- Primary reference used by Humanizer: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
