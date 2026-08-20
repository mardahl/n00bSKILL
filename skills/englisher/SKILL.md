---
name: englisher
description: Use when composing or editing any deliverable containing English prose for an external reader — marketing copy, customer emails, proposals, reports, presentation text, UI text, newsletters, documentation — including when English is only one part of a larger technical artifact (an English appendix, quote, or email body inside other work). Trigger on "write in English", "humanize this text", "make it sound less AI", "fix my English text", or any request whose output is English prose a customer, partner, reviewer or colleague will read. Do NOT trigger on English variable names, English tenant/domain strings, quoted legal clauses used as data, or English words discussed inside a technical discussion.
license: MIT
compatibility: claude-code opencode
---

# Englisher

## Overview

AI-written English carries stock AI patterns even when grammar is correct: inflated claims, sales language, vague sources, formulaic rhythm, chatbot artifacts. Fix the patterns, keep the writer's voice. Rewriting every dry or formal sentence as a tell is the most common over-correction and makes text worse. Detection rules and worked examples come from the [Humanizer skill by blader](https://github.com/blader/humanizer), itself based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject AI Cleanup. For detection detail, consult those sources; the scanner below is the working checklist.

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

Sentence-by-sentence translation produces nearly every AI tell. Read the source, understand the point, write English from scratch without dropping or changing any source meaning. If user requests a transformation, only its explicit dimensions may change.

## The patterns the scanner enforces

Full list with before/after examples lives in the sources linked above. Working set, in check order:

**Content**
1. **Inflated importance.** `stands as`, `a testament to`, `pivotal moment`, `marks a shift`, `underscores its significance`. State the fact; drop the legacy claim.
2. **Name-dropping.** Publication lists and follower counts used to prove a person matters. Keep citations that carry context; cut the proof-by-association.
3. **Shallow `-ing` analysis.** `symbolizing...`, `reflecting...`, `contributing to...` bolted onto a simple fact to make it sound deep. State the fact.
4. **Sales language.** `boasts`, `vibrant`, `nestled`, `in the heart of`, `breathtaking`, `renowned`, `showcasing`. Especially in descriptions of places, products, organizations.
5. **Vague sources.** `Industry reports`, `Experts argue`, `Observers have cited`. Name a real source or remove the claim. Never invent one.
6. **Formulaic challenges-and-outlook sections.** Stock `Despite these challenges... continues to thrive` paragraphs. Keep the concrete fact; cut the boilerplate.

**Language**
7. **Overused AI words.** `delve`, `crucial`, `pivotal`, `vibrant`, `showcase`, `underscore`, `highlight`, `intricate`, `foster`, `garner`, `tapestry`, `landscape` (abstract), `testament`, `Additionally` piling up. One instance is not a tell; clusters are.
8. **Avoiding `is`/`are`/`has`.** `serves as`, `features`, `boasts` where a simple verb works. `The gallery is...` beats `The gallery serves as...`.
9. **`Not X but Y` and clipped negative endings.** `It's not just X, it's Y`; tailing negations like `no guessing`. Write the clear clause.
10. **Forced groups of three.** `innovation, inspiration, and industry insights`. Two items or four are fine when that is what the content has.
11. **Synonym cycling and repeated sentence openings.** Renaming the same subject each sentence, or opening five sentences with `She`. Fix the pattern, not the word.
12. **False `from X to Y` ranges.** `from the Big Bang to dark matter` where X and Y are not a range. List the actual items.
13. **Passive voice and missing subjects.** Activate when it makes actor and action clearer; `No configuration file needed.` → `You do not need a configuration file.`

**Style**
14. **Em dashes and spaced dashes.** Default: replace `—`, `–`, ` -- ` with a period, comma, colon or parentheses — *unless the writer's own sample uses them*, in which case match the sample's rate.
15. **Gratuitous bold.** Bolding phrases with no reason.
16. **Lists with bold mini-headings.** `- **User Experience:** ...` items that should be a sentence.
17. **Title Case headings.** AI capitalizes every main word; most house styles use sentence case.
18. **Decorative emoji.** 🚀 in headings and list items.
19. **Curly quotes.** `“...”` where writer or target format uses straight quotes. Note: many editors auto-curl; this counts only when stacked with other tells.

**Chatbot artifacts**
20. **Chatbot text left in the answer.** `I hope this helps!`, `Certainly!`, `Let me know if you'd like...`.
21. **Knowledge-limit disclaimers and gap-fill guesses.** `as of my last update`, `details are scarce`, followed by a plausible guess. State what the source does not show, or cut. Never present a guess as fact.
22. **Overly agreeable openings.** `Great question!`, `You're absolutely right`.

**Filler and hedging**
23. **Filler phrases.** `In order to` → `To`. `Due to the fact that` → `Because`. `At this point in time` → `Now`. `has the ability to` → `can`.
24. **Stacked qualifiers.** `could potentially possibly be argued that... might`. Keep one qualifier, only when meaning needs it.
25. **Generic positive endings.** `The future looks bright. Exciting times lie ahead.` End on the last concrete fact.
26. **Over-hyphenated pairs.** `data-driven`, `cross-functional`, `end-to-end` hyphenated everywhere. Keep the hyphen before a noun (`a high-quality report`); drop it after (`the report is high quality`).
27. **Pretending to reveal a deeper truth.** `The real question is`, `at its core`, `what really matters`. State the point.
28. **Announcing the next point.** `Let's dive in`, `Here's what you need to know`, `One thing that bit me, so pay attention:`. Remove the announcement.
29. **Heading repeated in the first sentence.** A heading followed by a one-line paragraph that restates it. Delete the restatement.
30. **Writing about the previous version.** Prose describing what the old approach did, outside changelogs and migration guides. Describe current behavior.
31. **Forced punchlines and dramatic fragments.** A row of short fragments for drama. One short sentence for emphasis is fine.
32. **Formulaic sayings.** `X is the Y of Z`, `X is not a tool but a mirror`, `the language of trust`. Replace with the specific claim.
33. **Fake-candid openings.** `Honestly?`, `Look,`, `Here's the thing,` as staged pauses before an ordinary point.
34. **Answering objections no one raised.** `This isn't really about...`, `I'm not saying...`, `You could argue this differently but...` where no objection exists in the text. Remove only the unsupported defense; keep the real claim.
35. **Rejecting fake alternatives.** `A tempting approach would be... but...` for an option no reader would consider. Remove the fake option; state the real constraint.

## Check for false positives

A person may use some of these patterns. Do not treat any item below as proof by itself:

- **Perfect grammar and consistent style.** Polish does not equal AI.
- **Mixed casual and formal styles.** Can reflect field, age or habits.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic words.** Pattern 7 lists specific overused words. Do not simplify every formal word.
- **Common transition words in isolation.** `Additionally`, `moreover` are AI-coded only when piled up. One `however` is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs and most CMSes auto-curl by default.
- **Em dashes alone.** Many editors and journalists use them. Evidence only when paired with formulaic rhythm.
- **One short sentence for emphasis.** Flag dramatic fragments only when several appear in a row.
- **Deliberate repeated openings.** `She came. She saw. She conquered.` builds rhythm on purpose. Change it only when the repetition adds nothing.
- **"Honestly" or "look" mid-sentence.** Ordinary in casual writing. The tell is the standalone theatrical opener.
- **Useful limits and disclaimers.** Keep scope statements, legal and safety notices, real corrections, named objections, replies, FAQ answers.
- **Real alternatives.** Keep options a reader may genuinely consider in a design document, tutorial or argument.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations proves nothing.
- **Correct, complex formatting.** Templates and visual editors produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.

When unsure, look for several patterns together. One em dash proves nothing. Several stock patterns in the same passage are stronger evidence.

**Human details to keep** — these often carry the writer's voice:

- Specific, unusual details: a real address, an odd quote, a phrase like "the lawyer who used to work upstairs from my dentist."
- Mixed feelings and unresolved tension: "I think this is mostly good, but it bothers me, and I can't fully explain why."
- Dated, era-bound references: slang, memes, in-jokes tied to a specific year and subculture.
- Deliberate first-person choices the writer can explain.
- Variety in sentence length. Real writing alternates short and long; AI tends toward an even, mid-length cadence.
- Genuine asides, parentheticals, self-corrections: "(I keep wanting to say 'almost' here, but it really was certain.)"
- Edits made before November 30, 2022 — ChatGPT's public launch. Anything older is, with very rare exceptions, not AI-written.

## Match the writer's voice

If the user provides a sample of their own writing, analyze it before rewriting: sentence length, word choice, paragraph openings, punctuation, repeated phrases, transitions. Match those habits. Do not replace casual words with formal ones or remove deliberate quirks. A writing sample takes priority over the style rules above — if the sample uses em dashes, keep them at about the same rate.

Add personality in blog posts, essays, opinions and personal writing when it fits the writer. Keep reference, technical, legal and factual text neutral. Do not add opinions or first-person language where they do not belong. Never invent facts to make text feel personal.

## EDIT mode: editing existing English text

Before rewriting, work out four things from the source. Infer only what the text makes unambiguous; if register or audience materially changes the edit and the source does not reveal it, ask one short clarification.

1. **Register and audience.** A proposal for a £1m contract and a LinkedIn post get different treatment. Infer from genre and communicative situation.
2. **Formality already in use.** Keep it. Do not switch a casual piece to formal mid-edit.
3. **Meaning-bearing material.** Mark facts, claims, attribution, modality, tense, negation, quantifiers, actors, obligations and protected strings. Rewrite only if all meaning survives.
4. **Positioning and stance.** Tighten wording; delete a claim, promise or recommendation only when user explicitly authorizes content reduction. A tone request changes the named stance, not other propositions or commitments. List authorized deletions unless user requests text only.

Then rewrite, run the scanner, deliver.

## WRITE mode: writing new English copy

Before composing from a brief, establish: who the reader is, what kind of text this is (email, post, proposal, docs), and what the text should achieve. Skip any question the brief already answers. Then write English that never had the tells, using the scanner as a pre-emit check.

## Pre-emit scanner

Run before delivering, in every mode. Each item passes or fails; fix every failure before emitting.

1. No em dashes, en dashes or ` -- ` (pattern 14), unless the writer's sample uses them.
2. No chatbot artifacts: greetings, closings, offers, knowledge-limit disclaimers (patterns 20–22).
3. No overused AI word clusters (pattern 7). One instance passes; three in a paragraph fails.
4. No `serves as` / `boasts` / `features` where `is` / `has` works (pattern 8).
5. No forced groups of three (pattern 10).
6. No bold mini-heading lists or gratuitous bold (patterns 15–16).
7. Sentence-case headings (pattern 17), no decorative emoji (pattern 18).
8. No filler phrases or stacked qualifiers (patterns 23–24).
9. No generic positive ending (pattern 25).
10. Every number, name, date, quote and commitment traceable to input. Untraceable → replace with bracketed placeholder or delete.
11. Modality, tense, quantifiers, negation scope unchanged from source or brief.
12. Vague attribution still vague or marked `[source?]` — never replaced with an invented citation.

## Process

Both modes end the same way. The scanner is not optional; the first draft always keeps tells you cannot see while generating. Draft the best version, run every scanner check, fix every failure, then ask *"What still sounds AI-generated?"* and *"Did the rewrite add or remove any fact, name, number, date, quote, citation, or other claim?"* Treat any unsupported addition or lost claim as an error. Write the final version by stating each point naturally, not by patching one flagged phrase at a time.

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
