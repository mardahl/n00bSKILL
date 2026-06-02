# Humanizer Danish addendum

A Danish add-on for the Humanizer skill.

Use it when Danish AI text sounds translated, too polished, or weirdly corporate. It catches Danish-specific tells the English Humanizer rules miss: direct English idiom translations, English sentence rhythm, Danish business filler, flat ChatGPT enthusiasm, and over-correction of normal Danish IT language.

## Kort på dansk

Hvis dansk AI-tekst lyder som engelsk med danske ord, er det her addendum lavet til oprydningen.

Det fanger især direkte oversatte engelske vendinger, stiv syntaks, konsulentsprog og den der lidt for pæne ChatGPT-tone.

Brug det sammen med Humanizer, eller upload den færdige `.skill`-fil i Claude Teams.

## What to install

For Claude Team/Enterprise, upload this file in the organization skill upload screen:

[`package/humanizer-danish.skill`](package/humanizer-danish.skill)

That file is the combined `humanizer-danish` skill: the original Humanizer guidance plus this Danish addendum in one `.skill` upload.

For opencode or Claude Code, install this folder as a companion skill and keep your existing `humanizer` skill.

Source versus artifact: `SKILL.md` is the source addendum. `package/humanizer-danish.skill` is the upload-ready package.

## Files

- `SKILL.md`: source addendum for opencode and Claude Code
- `README.md`: install notes and usage guidance
- `package/humanizer-danish.skill`: combined Claude upload package

## Install as a companion skill

This is the cleanest setup for local agents. Leave `humanizer` alone and install this skill next to it.

### opencode

Copy or symlink this folder into one of opencode's skill locations:

```text
~/.config/opencode/skills/humanizer-danish-addendum/
.opencode/skills/humanizer-danish-addendum/
```

Restart opencode after copying the folder.

When Danish text is involved, the agent should load both skills:

1. `humanizer` for general AI-writing patterns
2. `humanizer-danish-addendum` for Danish-specific patterns

### Claude Code

Copy or symlink this folder into Claude Code's skill location:

```text
~/.claude/skills/humanizer-danish-addendum/
```

Restart Claude Code or start a new session.

When Danish text is involved, the agent should load both skills:

1. `humanizer` for general AI-writing patterns
2. `humanizer-danish-addendum` for Danish-specific patterns

## Merge into an existing Humanizer skill

Use this only if you want one local skill file instead of two companion skills.

For opencode or Claude Code agents doing the merge:

1. Locate the existing `humanizer/SKILL.md`
2. Keep the existing Humanizer frontmatter unless the user asks to change it
3. Copy this skill body starting at `# Humanizer Danish Addendum`
4. Paste it near the parent skill's language-specific guidance or before its final process section
5. Do not copy this skill's YAML frontmatter into the parent skill
6. Keep the caveat about not over-correcting Danish IT fagsprog
7. Restart the agent application after saving

## Agent instructions

When asked to humanize Danish text:

1. Apply the general Humanizer patterns first
2. Run a Danish pass using D1-D5 from this addendum
3. Treat the watch list as judgment prompts, not mechanical rules
4. Keep normal Danish IT terms and English technical vocabulary when they are standard practice
5. Report briefly which Danish tells were removed

## Attribution

- Original Humanizer skill: [github.com/blader/humanizer](https://github.com/blader/humanizer)
- Original Humanizer creator: [blader](https://github.com/blader)
- Primary reference used by Humanizer: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
