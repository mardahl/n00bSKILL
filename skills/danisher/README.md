# Danisher

`danisher` writes and edits Danish copy that does not read like translated English.

Use it for marketing text, kundemails, LinkedIn-opslag, nyhedsbreve, UI-tekst, rapporter and documentation, in either direction: paste Danish text and it cleans it up, or give it a brief and it writes the Danish from scratch. Give it English source material and it writes Danish from the meaning instead of translating sentence by sentence.

It is for anyone producing Danish text with an AI agent: marketers, consultants, IT folks writing customer-facing documentation, and students. It is Danish only. For English, use [`englisher`](../englisher/).

## Kort på dansk

AI-skrevet dansk bærer ofte spor af engelsk syntaks, engelske vendinger og engelsk rytme. Resultatet kan være grammatisk korrekt dansk, som stadig lyder oversat.

`danisher` retter registret og rytmen, ikke fagsproget. Den fanger direkte oversatte vendinger, manglende modalpartikler, særskrivning, forkerte bindestreger, engelsk talformat og den lidt for pæne ChatGPT-begejstring. Den lader være med at "danskgøre" almindelige engelske IT-termer, for det er dér, de fleste sprogrettelser gør teksten værre.

Den kan både rette en tekst, du har, og skrive en ny fra en prompt.

## What to install

For Claude Team or Enterprise, upload this file under organization skills:

[`package/danisher.skill`](package/danisher.skill)

Then enable the skill for the relevant workspace or users.

For opencode and Claude Code, install this folder as a source skill. See install locations below.

## Files

- `SKILL.md`: the source skill for opencode and Claude Code
- `references/registers.md`: intake questions, pre-flight checks, register table and channel defaults. Loaded when writing new Danish from a brief.
- `references/danish-tells.md`: the Danish-specific patterns D1–D10, with worked examples. Loaded when auditing or editing Danish text.
- `references/typography.md`: typography and number formats (D8). Loaded when the scanner flags dashes, numbers, dates, currency or commas.
- `references/lokalisering.md`: locale mode for a reader in Denmark. Loaded when the input or draft has American or other non-Danish conventions.
- `LICENSE.txt`: licence terms, a ready-made credit line and any third-party notices
- `README.md`: this landing page
- `package/danisher.skill`: upload-ready Claude artifact

Source versus artifact: `SKILL.md` plus `references/` is the source. The `.skill` file is a zip archive renamed with the `.skill` extension, containing `SKILL.md`, `references/`, `README.md` and `LICENSE.txt`. It is not a separate skill.

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
| A brief or bullet points | Asks up to three intake questions, then writes Danish copy that reads as if a Dane wrote it |
| English text and "på dansk" | Writes Danish from the meaning, not sentence by sentence |
| Anything with American or other non-Danish conventions (dollars, `11/28`, EST, ZIP codes, HIPAA, Thanksgiving, "thrilled to announce") | Localises for a reader in Denmark (`da-DK`) and lists every adaptation it made |

Locale mode lives in `references/lokalisering.md` and is read only when the input or draft needs it. It converts formats and time zones, swaps in Danish equivalents and tones down American sales register. It never invents an exchange rate, a Danish price, Danish availability or a compliance claim; those become bracketed gaps.

Before writing from a brief it asks who you are writing to, what kind of text it is, and what the text should achieve. Each comes with a fixed set of options, so it takes one reply. It skips any question the brief already answers. With pasted Danish or English source, it normally infers context from the text and asks one short clarification only when an ambiguity such as register or `du` versus `I` prevents a faithful rewrite.

Before delivering, it runs a scanner on its own draft. The mechanical checks cover dashes and ranges, decimal commas, thousands separators, consistent `%` spacing, lowercase weekdays and months, the comma system and hyphens in compounds. Then it checks that every fact traces to the input and that modality and register haven't changed. The final version is revised against the scanner, because a first draft always keeps patterns the model can't see while writing it.

It will not invent facts to make the copy better. When a needed fact is missing, it leaves a bracketed gap and lists what you need to supply. That is deliberate: a thin honest draft beats a polished one with plausible invented details.

If you want new copy to sound like you, paste a sample of your own Danish writing and say so. The skill matches sentence length, register, tiltaleform and punctuation habits without importing unsupported claims. Source-bound rewrites keep the source's meaning and address form.

## Relationship to other skills in this repo

`danisher` replaces the `humanizer-danish-addendum` skill, which has been removed from this repo. The addendum was a bolt-on that required the `humanizer` skill to be installed alongside it. Danisher is standalone and adds a writing mode, Danish typography rules and Danish address-form guidance. If you still have the addendum installed, remove it.

For longer Danish academic and workplace reports, use [`danish-report-writer`](../danish-report-writer/) to get the structure and argument right first, then run Danisher as the final language pass.

## Changelog

- **1.3.1:** Licence changed from MIT to CC BY-SA 4.0 for the skill text. Adds `LICENSE.txt` with the terms and a credit line; it is also inside the package. Versions released before this one stay MIT.
- **1.3.0:** Stops the skill from flattening your text. It no longer splits correct long sentences or swaps long words for short ones just to make a text easier to read. When you supply a writing sample, it checks the draft's sentence length and share of long words against the sample, and builds longer sentences from your facts plus bracketed gaps instead of invented claims. Reading effort now follows the text's purpose: plain for instructions and driftstekst, not smoothed out for persuasive text.
- **1.2.0:** First numbered release. Earlier changes were not versioned. This release adds:
  - hyphen rules from Retskrivningsreglerne § 57: a hyphen for a left-out shared part (`drifts- og supportaftaler`), hyphens between equal-ranking parts (`dansk-tysk`, `kunde-leverandør-forholdet`), compounds with digits, symbols and spoken letters (`1990-tallet`, `A-kunder`), a hyphen only at the boundary (`e-mailadresse`, `ph.d.-studerende`), and proper names in group compounds (`New York-kontoret`)
  - ranges (`mandag-fredag kl. 9-16`, `1. januar – 30. juni`), a spaced hyphen used as a dash, and ISO dates in running text
  - LOKALISÉR mode (`references/lokalisering.md`) for a reader in Denmark

## Attribution

- Danish rules and worked examples are rebuilt and honed against [Dansk Sprognævn](https://dsn.dk) and other official Danish language sources
- The anti-flattening rules (1.3.0) draw on Ilyas, Tashk, Beier and Bækgaard, ["Reading the Readers Mind through Eye Tracking: Can AI Generated Texts Match Human Authors?"](https://dl.acm.org/doi/10.1145/3715669.3726846), ETRA 2025. In that study, Copilot imitations of Danish authors were simpler than the originals and were read more like skimming. The study had 12 readers, one model and literary texts, so the skill uses it as a reason for caution, not as a detection rule

Licence: skill text CC BY-SA 4.0. See [`LICENSE.txt`](LICENSE.txt) for the terms and how to credit this skill.
