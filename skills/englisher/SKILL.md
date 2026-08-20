---
name: englisher
description: Use when composing or editing any deliverable containing English prose for an external reader — marketing copy, customer emails, proposals, reports, presentation text, UI text, newsletters, documentation — including when English is only one part of a larger technical artifact (an English appendix, quote, or email body inside other work). Trigger on "write in English", "humanize this text", "make it sound less AI", "fix my English text", or any request whose output is English prose a customer, partner, reviewer or colleague will read. Do NOT trigger on English variable names, English tenant/domain strings, quoted legal clauses used as data, or English words discussed inside a technical discussion.
license: MIT
compatibility: claude-code opencode
---

# Englisher

## Overview

AI-written English carries stock AI patterns even when grammar is correct: inflated claims, sales language, vague sources, formulaic rhythm, chatbot artifacts. Fix the patterns, keep the writer's voice. Rewriting every dry or formal sentence as a tell is the most common over-correction and makes text worse.

Load reference files on demand:
- `references/english-tells.md` — E1–E37 with worked examples, false positives, human details to keep. Load when auditing or editing English text, or when a scanner check needs a worked example.
- `references/voice.md` — writer's-voice matching, register table, personality guidance, WRITE-mode intake. Load when composing new English from a brief or matching a writing sample.
- `references/typography.md` — typography and number-format table. Load when the scanner flags dashes, quotes, numbers, dates, currency or punctuation consistency.

## Hard rule: never invent facts

You may shorten dull parts, expand useful parts, and merge or split paragraphs. That is a rule about *how to present the available facts*, not a licence to produce new ones.

- **EDIT:** every proposition and every relationship in output must appear in the source. Preserve facts, claims, attribution, modality, tense, negation, quantifiers, actors, addressees, obligations, permissions, commitments, numbers, dates, names, causes and objects of vague terms. Vague attribution stays vague; mark the gap `[source?]`.
- **Source-bound WRITE:** material in another language plus "in English" uses WRITE's composition method, not its freedom to omit. Preserve every source proposition and protected string. Restructure prose; do not summarize, strengthen, weaken or reassign unless the user names the permitted transformation.
- **WRITE:** use every fact the brief supplies. For missing facts, write `[X customers]`, `[date]`, `[product name]` and list placeholders at the end. A bracketed gap is correct output. Replacing a supplied figure with a placeholder or inventing a plausible number are both failures.
- Three classes slip past the obvious check:
  - **Cause.** Brief says `scheduled downtime`. Writing `we are upgrading our systems` invents a reason. Write `[reason]` or leave it out.
  - **Object of a vague term.** Source says `seamless integration` without saying with what. Writing `integrates with your Microsoft 365` invents the object. Write `[which systems?]`.
  - **The derived reassurance.** Brief says `no data is lost`. Writing `you don't need to do anything` adds a commitment nobody made.
- **Do not change modality, tense or aspect.** `may contribute to` may not become `contributes`. `will transform` may not become `transforms`. `rolls out next week` may not become `is live`. Remove a stacked hedge only when removed words are genuinely synonymous; if uncertain, leave it. Never remove the last qualification. In legal, contractual, SLA and operational text this is the most damaging edit in the file.
- **Do not reassign who asserts a claim or who must act.** `It is recommended that the update be prioritized` is agentless. `We recommend you update` invents sender and obligation. In EDIT, activate a passive only when the source already names every role.
- **Do not widen quantifiers or flip negation scope.** `some customers` may not become `customers`. `no known vulnerabilities` may not become `secure`. `a number of` → specific number only when source states it.
- **Preserve attributed quotes and mandated wording.** In EDIT, verbatim. In source-bound translation, translate faithfully; preserve attribution, modality, scope and quotation status. For statutory, contractual or regulator-supplied wording, ask whether original is retained or a clearly labelled non-authoritative translation.
- **Preserve functional strings exactly.** Code spans, variables, localization placeholders, commands, flags, URLs, IDs and product identifiers are mandated wording. Preserve characters and surrounding delimiters.
- **Deletion follows the same rule.** Never assume repeated wording is accidental. Delete only when user authorizes shortening and requested emphasis survives. Labels like `positioning`, `filler`, `sales language` and `generic` are not permission to delete source meaning. A tone request changes only the named stance, never facts, claims, promises, recommendations or commitments.

When rhythm and accuracy conflict, accuracy wins.

## Modes

Route on input.

| Input | Mode | What to do |
| --- | --- | --- |
| Existing English text | EDIT | Draft rewrite, run scanner, final version |
| A brief, topic or bullet points | WRITE | Write English copy that never had the tells |
| Text in another language plus "in English" | WRITE, source-bound | Write from meaning while preserving every source claim and protected string |

Sentence-by-sentence translation produces nearly every tell in `references/english-tells.md`. Read the source, understand the point, write English from scratch without dropping or changing any source meaning. If user requests a transformation, only its explicit dimensions may change.

## Pre-emit scanner

Run before delivering, in every mode. Each item passes or fails; fix every failure before emitting. Pattern references (E1–E37) point to worked examples in `references/english-tells.md`.

1. No em dashes, en dashes or ` -- ` (E14), unless the writer's sample uses them — then match the sample's rate. See `references/typography.md`.
2. Quote style consistent (straight vs curly), apostrophe style matching, serial comma held, list punctuation consistent, number/unit notation held. See `references/typography.md`.
3. No chatbot artifacts: greetings, closings, offers, knowledge-limit disclaimers, gap-fill guesses (E20–E22).
4. No overused AI word clusters (E7) or metaphor overload (E36). One instance passes; clusters fail.
5. No verb inflation: avoiding simple is/are via `serves as` / `boasts` / `features` where `is` / `has` works (E8).
6. No forced groups of three / mechanical triads (E10) and no other formulaic rhythm: negative parallelism (`not X but Y`, E9), repeated sentence openings or synonym roulette (E11).
7. No bold mini-heading lists or gratuitous bold (E15–E16); sentence-case headings (E17); no decorative emoji (E18).
8. No filler phrases or stacked qualifiers (E23–E24). Never remove the last qualification.
9. No generic positive ending or over-explaining abstract gloss (E25, E37).
10. No answered-but-unraised objections and no rejected fake alternatives (E34–E35). Keep options that are real or attributed.
11. Every number, name, date, quote and commitment traceable to input. Untraceable → replace with bracketed placeholder or delete.
12. Modality, tense, quantifiers, negation scope unchanged from source or brief.
13. Vague attribution still vague or marked `[source?]` — never replaced with an invented citation.
14. Calibration and false positives checked: density and co-occurrence are the target, not zero occurrences. Flag clusters and repetition, not isolated instances. Polish, mixed register, single transition words, auto-curled quotes, lone em dashes, deliberate repetition are not tells by themselves. Preserve the author's voice. See the false-positives list in `references/english-tells.md`.

## EDIT mode: editing existing English text

Before rewriting, work out four things from the source. Infer only what the text makes unambiguous; if register or audience materially changes the edit and the source does not reveal it, ask one short clarification.

1. **Register and audience.** A proposal for a £1m contract and a LinkedIn post get different treatment. Infer from genre and communicative situation. See `references/voice.md`.
2. **Formality already in use.** Keep it. Do not switch a casual piece to formal mid-edit.
3. **Meaning-bearing material.** Mark facts, claims, attribution, modality, tense, negation, quantifiers, actors, obligations and protected strings. Rewrite only if all meaning survives.
4. **Positioning and stance.** Tighten wording; delete a claim, promise or recommendation only when user explicitly authorizes content reduction. A tone request changes the named stance, not other propositions or commitments. List authorized deletions unless user requests text only.

If the user provides a sample of their own writing, it takes priority over the style rules — match its habits. See `references/voice.md`.

Then rewrite, run the scanner, deliver.

## WRITE mode: writing new English copy

Load `references/voice.md`. It contains intake questions (reader, text type, goal), the register table, personality guidance and a pre-delivery checklist.

## Process

Both modes end the same way. The scanner above is not optional; the first draft always keeps tells you cannot see while generating. Draft the best version, run every scanner check, fix every failure, then ask *"What still sounds AI-generated?"* and *"Did the rewrite add or remove any fact, name, number, date, quote, citation, or other claim?"* Treat any unsupported addition or lost claim as an error. Write the final version by stating each point naturally, not by patching one flagged phrase at a time.

## Output format

Default by length, not mode.

| Situation | Deliver |
| --- | --- |
| Under roughly 200 words | Final text, placeholder list, any authorized deletion list, plus at most three other change bullets |
| Over roughly 200 words | Final text, any actual audit findings, placeholder list and any authorized deletion list |
| User says `just the text`, `text only`, `no commentary` | Final text only. Keep unresolved placeholders visible inline; do not add separate lists. |

Generate the draft and run the complete scanner internally. Do not expose a draft already known to contain unsupported or altered meaning. Always surface bracketed placeholders, in every format, including the short one. A placeholder the user does not see is the same failure as an invented number.

**File mode.** When the user names a file, run the full rewrite process but write only the final text to the file. Change prose only. Keep code blocks, YAML metadata, data and link targets unchanged. Then give a short summary.

**Embedded mode.** When another task uses this skill for a pull request, commit message or document, return only the final text.
