# Self-Contained Output

`self-contained-output` strips assistant-to-user conversational bleed from standalone deliverables, so each file reads as if written for a stranger with zero chat context.

It is for anyone using an AI agent to produce files that outlive the conversation: scripts, source code, READMEs, configs, IaC, CI/CD YAML, UI copy, documentation, sample data. If the output is a file another person will read without seeing the chat, this skill applies. It does not apply to in-chat conversational answers.

The defect it catches: artifact text that addresses the requester or references the conversation - "as we discussed", "the file you sent", "one trade-off you already signed off on", "here's the updated version". The reader of the file does not know who "you" is or what was discussed.

## What to install

For Claude Team or Enterprise, upload this file under organization skills:

[`package/self-contained-output.skill`](package/self-contained-output.skill)

Then enable the skill for the relevant workspace or users.

For opencode and Claude Code, install this folder as a source skill. See install locations below.

## Files

- `SKILL.md`: the source skill for opencode and Claude Code
- `README.md`: this landing page
- `package/self-contained-output.skill`: upload-ready Claude artifact

Source versus artifact: `SKILL.md` is the source. The `.skill` file is a zip archive renamed with the `.skill` extension, containing `SKILL.md` and `README.md`. It is not a separate skill.

## Install locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/self-contained-output/
.opencode/skills/self-contained-output/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/self-contained-output/
```

Restart the agent application after installing.

## What the skill enforces

- No requester references or assumed chat history inside the artifact ("as we discussed", "as requested", "the file you sent").
- No assistant voice or meta-commentary ("I", "we", "here's the updated version", apologies). Real CHANGELOG sections written neutrally are exempt.
- Caveats and trade-offs live in a neutral "Known issues" or "Limitations" section, stated as facts.
- Every sentence must make sense to a reader who never saw the chat.
- Placeholders are generic (`<tenant>`, `user@example.com`) unless a concrete value is genuinely part of the deliverable.
- Instructional "you" for any future reader is allowed ("Run this once per tenant"); "you" presuming this specific requester is not.
- Technical terminology is not bleed - domain terms, cmdlet names and product jargon stay.

The skill ends with a pre-finalize self-check the agent runs on the artifact before emitting it.

## Attribution

- Authored and maintained as part of `n00bSKILL`.
