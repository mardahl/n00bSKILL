# Englisher

`englisher` writes and edits English copy that does not read like AI wrote it.

Use it for marketing text, customer emails, LinkedIn posts, newsletters, UI text, reports, proposals and documentation, in either direction: paste English text and it cleans it up, or give it a brief and it writes the English from scratch. Give it source material in another language and it writes English from the meaning instead of translating sentence by sentence.

It is for anyone producing English text with an AI agent: marketers, consultants, IT folks writing customer-facing documentation, and students. It is English only.

## What it catches

AI-written English is usually grammatically correct but carries stock patterns: inflated claims (`stands as a testament to`), sales language (`nestled`, `vibrant`, `boasts`), vague sources (`experts argue`), formulaic rhythm (groups of three, even mid-length sentences), chatbot artifacts (`I hope this helps!`), em dashes everywhere, and stacked qualifiers that make every claim sound uncertain.

`englisher` fixes the patterns, not the writer's voice. It checks its own draft against a scanner before delivering, and it will not invent facts to make the copy better: when a needed fact is missing, it leaves a bracketed gap and tells you what to supply.

## What to install

For Claude Team or Enterprise, upload this file under organization skills:

[`package/englisher.skill`](package/englisher.skill)

Then enable the skill for the relevant workspace or users.

For opencode and Claude Code, install this folder as a source skill. See install locations below.

## Files

- `SKILL.md`: the source skill for opencode and Claude Code
- `references/english-tells.md`: E1–E37 with worked examples, false positives, human details to keep — loaded when auditing or editing English text
- `references/voice.md`: writer's-voice matching, register table, personality guidance, WRITE-mode intake — loaded when composing new English from a brief
- `references/typography.md`: typography and number-format table — loaded when the pre-emit scanner flags dashes, quotes, numbers, dates, currency or punctuation consistency
- `README.md`: this landing page
- `package/englisher.skill`: upload-ready Claude artifact

Source versus artifact: `SKILL.md` plus `references/` is the source. The `.skill` file is a zip archive renamed with the `.skill` extension, containing `SKILL.md`, `references/` and `README.md`. It is not a separate skill.

## Install locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/englisher/
.opencode/skills/englisher/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/englisher/
```

Restart the agent application after installing.

## How the agent uses it

The skill routes on what you give it:

| You give it | It does |
| --- | --- |
| English text | Rewrites it, runs a pre-emit scanner over its own draft, delivers a final version |
| A brief or bullet points | Establishes reader, text type and goal, then writes English copy that never had the tells |
| Text in another language and "in English" | Writes English from the meaning, not sentence by sentence, preserving every source claim |

Before delivering, every run passes a pre-emit scanner: no em dashes (unless your own sample uses them), no chatbot artifacts, no AI-word clusters, simple verbs instead of `serves as`/`boasts`, no forced groups of three, no filler phrases, and every number, name, date and commitment traceable to your input. Modality, tense and quantifiers survive unchanged — `may contribute` does not become `contributes`.

If you want the output to sound like you, paste a sample of your own writing and say so. The skill matches sentence length, register, punctuation and word-choice habits instead of applying generic rules.

## Relationship to other skills in this repo

`englisher` is the English counterpart to [`danisher`](../danisher/). Same structure, same guarantees (mode routing, pre-emit scanner, no invented facts), with English AI-writing patterns instead of Danish ones. Use `danisher` for Danish output, `englisher` for English output.

## Attribution

- Detection rules and worked examples derive from the [Humanizer skill by blader](https://github.com/blader/humanizer) (MIT)
- Humanizer's patterns come from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup
- Skill structure mirrors [`danisher`](../danisher/) in this repository
