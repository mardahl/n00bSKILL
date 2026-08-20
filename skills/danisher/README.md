# Danisher

`danisher` writes and edits Danish copy that does not read like translated English.

Use it for marketing text, kundemails, LinkedIn-opslag, nyhedsbreve, UI-tekst, rapporter and documentation, in either direction: paste Danish text and it cleans it up, or give it a brief and it writes the Danish from scratch. Give it English source material and it writes Danish from the meaning instead of translating sentence by sentence.

It is for anyone producing Danish text with an AI agent: marketers, consultants, IT folks writing customer-facing documentation, and students. It is Danish only. There is no English mode.

## Kort på dansk

AI-skrevet dansk bærer ofte spor af engelsk syntaks, engelske vendinger og engelsk rytme. Resultatet kan være grammatisk korrekt dansk, som stadig lyder oversat.

`danisher` retter registret og rytmen, ikke fagsproget. Den fanger direkte oversatte vendinger, manglende modalpartikler, særskrivning, engelsk talformat og den lidt for pæne ChatGPT-begejstring. Den lader være med at "danskgøre" almindelige engelske IT-termer, for det er dér, de fleste sprogrettelser gør teksten værre.

Den kan både rette en tekst, du har, og skrive en ny fra et brief.

## What to install

For Claude Team or Enterprise, upload this file under organization skills:

[`package/danisher.skill`](package/danisher.skill)

Then enable the skill for the relevant workspace or users.

For opencode and Claude Code, install this folder as a source skill. See install locations below.

## Files

- `SKILL.md`: the source skill for opencode and Claude Code
- `references/registers.md`: intake, pre-flight, register table, kanal — loaded when composing new Danish from a brief
- `references/danish-tells.md`: D1–D10 with worked examples — loaded when auditing or editing Danish text
- `references/typography.md`: D8 typography and number table — loaded when the pre-emit scanner flags numbers, dates, currency or comma system
- `README.md`: this landing page
- `package/danisher.skill`: upload-ready Claude artifact

Source versus artifact: `SKILL.md` plus `references/` is the source. The `.skill` file is a zip archive renamed with the `.skill` extension, containing `SKILL.md`, `references/` and `README.md`. It is not a separate skill.

## Install locations

For opencode, copy or symlink this folder into:

```text
~/.config/opencode/skills/danisher/
.opencode/skills/danisher/
```

For Claude Code, copy or symlink this folder into:

```text
~/.claude/skills/danisher/
```

Restart the agent application after installing.

## How the agent uses it

The skill routes on what you give it:

| You give it | It does |
| --- | --- |
| Danish text | Rewrites it, audits its own draft, delivers a final version |
| A brief or bullet points | Asks up to three intake questions, then writes Danish copy that never had the tells |
| English text and "på dansk" | Writes Danish from the meaning, not sentence by sentence |

Before writing from a brief it asks who you are writing to, what kind of text it is, and what the text should achieve. Each comes with a fixed set of options, so it takes one reply. It skips any question the brief already answers. With pasted Danish or English source, it normally infers context from the text and asks one short clarification only when an ambiguity such as register or `du` versus `I` prevents a faithful rewrite.

Every run ends with a mechanical pre-emit scanner (em-dash, decimal comma, thousands separator, % consistency, weekday/month case, comma system, group-compound hyphens) followed by meaning-preservation checks (fact traceability, modality, register). The final version is revised against that scanner, because the first draft always keeps tells the model cannot see while generating.

It will not invent facts to make the copy better. When a needed fact is missing, it leaves a bracketed gap and lists what you need to supply. That is deliberate: a thin honest draft beats a polished one with plausible invented details.

If you want new copy to sound like you, paste a sample of your own Danish writing and say so. The skill matches sentence length, register, tiltaleform and punctuation habits without importing unsupported claims. Source-bound rewrites keep the source's meaning and address form.

## Relationship to other skills in this repo

`danisher` supersedes [`humanizer-danish-addendum`](../humanizer-danish-addendum/). The addendum was a bolt-on that required the `humanizer` skill to be installed alongside it. Danisher is standalone and adds a writing mode, Danish typography rules and Danish address-form guidance. Install one or the other, not both.

For longer Danish academic and workplace reports, use [`danish-report-writer`](../danish-report-writer/) to get the structure and argument right first, then run Danisher as the final language pass.

## Attribution

- Danish rules and worked examples originate in `humanizer-danish-addendum` in this repository
- That addendum was built as a Danish companion to the [Humanizer skill by blader](https://github.com/blader/humanizer)
- The universal-pattern table is condensed from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup
