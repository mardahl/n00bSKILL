---
name: danish-report-writer
description: Use when planning, drafting, revising, or reviewing Danish reports, including requests like "lav en rapport", "skriv en rapport", "write me a report in Danish", problemformulering, synopsis, kilder, kildehenvisninger, rapportsprog, serviceafsnit, or educational and workplace formalia.
license: MIT
compatibility: claude-code opencode
---

# Danish report writer

## Overview

Use this skill when an agent helps with a Danish report: planning it, drafting it, revising it, or checking whether it is ready to hand in.

A Danish `rapport` is a `faglig`, `saglig` answer to a real question. It should help a specific reader use the material. Do not draft the report before the audience, purpose, local rules, `problemformulering`, and source basis are clear.

Primary source: Per Salling's 12-part Omatskrive.dk series `Skriv bedre rapporter!`. See `report-writing-source-notes.md` for article-by-article source notes.

## When to use

Use it for Danish work involving:

- User prompts such as `lav en rapport`, `skriv en rapport`, `skriv en dansk rapport`, `write me a report in Danish`, `help me with a Danish report`, `ret min rapport`, `lav en problemformulering`, or `hjælp med synopsis`.
- Report planning, `synopsis`, `problemformulering`, `hypotese`, `afgrænsning`, or method.
- Drafting or revising Danish report sections.
- Source selection, `kildekritik`, `kildehenvisninger`, `kildefortegnelse`, or appendices.
- Report language: `rapportsprog`, `fagsprog`, active/passive phrasing, or academic Danish.
- Reviewing `indledning`, `analyseafsnit`, `konklusion`, `resumé`, `forord`, or `serviceafsnit`.
- Danish school, university, public-sector, or workplace report conventions.

Do not use for ordinary emails, blog posts, essays, fiction, or non-Danish report conventions unless the user explicitly asks to adapt this Danish model.

## Start by choosing mode

When the user asks for a Danish report without specifying the work mode, ask them to choose before doing report work:

1. `Guided intake`: best when the user only has a subject. Ask required elements one at a time.
2. `Fast assumptions`: best when the user needs speed. Draft visible assumptions for all required elements and ask the user to approve or correct them.
3. `Existing report audit`: best when the user already has text. Audit gaps before rewriting.

If the prompt clearly includes an existing report or asks to fix one, use `Existing report audit` and ask for the report text if it is missing. If the user explicitly asks for speed, use `Fast assumptions`. Otherwise, ask mode first.

## Help the blank user choose

When a required element is missing, do not ask a blank open question. Give exactly three context-aware suggestions plus a custom option.

Use this format:

```text
Målgruppe:
A. [suggestion based on what is already known]
B. [different plausible suggestion]
C. [different plausible suggestion]
D. Skriv selv
```

Base suggestions on the subject, user wording, education/work context, existing notes, uploaded report text, or likely reader. Do not invent source facts. If you lack context, make the suggestions broad but useful.

Use three suggestions plus `Skriv selv` for these elements when they are missing or weak:

- `Afsender`
- `Målgruppe`
- `Formål`
- Context or institution
- `Formalia`
- Report type
- `Problemformulering`
- `Hypotese` when relevant
- `Afgrænsning`
- Source basis
- Citation style
- Required `serviceafsnit`

In `Guided intake`, ask about one element at a time. In `Fast assumptions`, show a compact assumption sheet with three alternatives for the uncertain elements and ask for approval. In `Existing report audit`, first show what is missing or weak, then offer three fixes for each important gap.

## Before you draft

Before writing full report prose, establish:

- `Afsender`: who is writing or speaking?
- `Målgruppe`: who must use the report?
- `Formål`: what should the reader know, decide, or do afterward?
- Context: education, workplace, public sector, or other institution?
- `Formalia`: assignment brief, rubric, template, page count, citation style, layout rules, submission requirements.
- Report type: descriptive, explanatory, or investigative/problem-solving.
- `Problemformulering`: the exact question the report answers.
- Source basis: what data, sources, observations, interviews, or empirical material can support the report?

If one of these is missing and matters for the job, ask one focused question before drafting. If the user insists on speed, state your assumptions visibly.

## Stop and fix first

Stop and repair the plan if you notice:

- The task is only `noget om ...` and has no `problemformulering`.
- You are about to draft a standard academic-looking report without local `formalia`.
- The bibliography is being treated as cleanup instead of evidence infrastructure.
- Google, image search, or ChatGPT is listed as a factual source.
- The analysis follows source order instead of an argument or knowledge progression.
- The conclusion summarizes the topic but does not answer the question.
- A repaired conclusion invents causes, findings, or recommendations not supported by the report's actual sources, data, or analysis.
- Appendices are included to show effort rather than help the reader.

## Quick reference

| Need | Use |
| --- | --- |
| Start a report | Pre-draft checks, then 9-part `synopsis` |
| Narrow a broad topic | `emne` -> problem -> affected audience -> `problemformulering` -> `afgrænsning` |
| Build main body | `indledning`, `analyseafsnit`, `konklusion` |
| Structure analysis | `redegørelse` -> `undersøgelse` -> `diskussion` |
| Fix weak conclusion | Compare `problemformulering` and `konklusion` side by side |
| Fix weak sources | Classify material, run `kildekritik`, add claim-level references |
| Finish a report | Audit citations, `kildefortegnelse`, and `serviceafsnit` |

## Working order

1. Intake `formalia` and reader context.
2. Narrow the topic from broad `emne` to focused `afgrænsning`.
3. Draft or refine the `problemformulering`.
4. Add a `hypotese` or `arbejdshypotese` when the report investigates causes, explanations, or solutions.
5. Build a 9-part `synopsis` in complete sentences.
6. Plan `kilder og data`; classify material as `selve stoffet`, `nødvendig baggrundsviden`, or irrelevant.
7. Draft `hovedafsnit`: `indledning`, `analyseafsnit`, `konklusion`.
8. Revise `rapportsprog`: clear Danish, useful `fagsprog`, named responsibility, and no unnecessary abstraction.
9. Audit `kildehenvisninger` and `kildefortegnelse`.
10. Add and audit `serviceafsnit`.
11. Compare `problemformulering` and `konklusion` side by side. If the conclusion does not answer the question, the report is not done.

## 9-part synopsis template

Use this before drafting. Each point should be 1-3 complete sentences, not keywords.

1. `Mit emne er ...`
2. `Det er et "problem", at ...`
3. `Det er et "problem" for ...`
4. `Jeg vil undersøge, om "problemet" skyldes ...`
5. `Jeg vil derfor finde svaret på dette spørgsmål ...`
6. `Rapporten skal kunne bruges af ... til at ...`
7. `Jeg vil kun beskæftige mig med ... fordi ...`
8. `Jeg vil bygge rapporten på ...`
9. `Jeg vil gøre sådan-og-sådan ...`

Do not copy this future-looking method text directly into the final report. The final `metodeafsnit` says what was actually done.

## Main sections

`Indledning` should move from broad `emneområde` to concrete problem field, focused scope, `problemformulering`, `afgrænsning`, method, audience, and purpose.

`Analyseafsnit` should usually move from `redegørelse` to `undersøgelse` to `diskussion`. Do not structure it as a source dump.

`Konklusion` must directly answer the `problemformulering`. Echo the question before answering if that helps clarity. When repairing a conclusion, do not invent findings; use only the report's existing analysis, sources, data, and interview material. If those are missing, give a conclusion scaffold with placeholders and ask for the evidence.

Add `metodekritik` or `perspektivering` only when it genuinely helps the reader understand limits, use, or further implications.

## Skriveproces

Keep drafting and polishing apart:

1. Write raw `indhold`: facts, data, observations, arguments, and source points.
2. Reorder the material before polishing sentences.
3. Cut irrelevant material and add missing support while the prose is still rough.
4. Rewrite into coherent Danish only after content and order are stable.
5. Correct spelling, commas, punctuation, formatting, and references at the end.

Do not make the first draft sound finished. A shiny but unfocused report is harder to repair than a rough, well-structured one.

## Source rules

- Google, image search, and chatbots are discovery tools, not sources.
- Every external factual claim, quote, graph, figure, dataset, interview, web page, PDF, broadcast, or observation needs a traceable source.
- Use claim-level references plus a complete `kildefortegnelse`.
- Prefer `fodnoter` over `slutnoter` unless local rules say otherwise.
- Use exact digital source locations, not vague homepage links, whenever possible.
- Cut interesting material outside the `afgrænsning`.
- Explain what each source contributes alone and in relation to the other material.

## Rapportsprog pass

- Write for the defined `målgruppe`, not for everyone.
- Use `fagsprog` only when the reader can use it.
- Do not simplify the subject; simplify the language.
- Prefer active wording where responsibility matters.
- Replace inflated academic phrasing with direct Danish.
- Save spelling, commas, and punctuation cleanup for the final correction pass.

Useful test: imagine explaining the point by phone to a `fagfælle` you do not personally know. The report prose should preserve that clear professional voice.

## Serviceafsnit audit

Check which support sections are required by local rules and report length:

- `Forside`
- Optional `titelblad` or `kolofon`
- `Indholdsfortegnelse`
- `Resumé`
- `Forord`
- `Kildefortegnelse`
- `Bilag`
- `Bilagsfortegnelse` when appendices are numerous

`Serviceafsnit` are the report's `brugsanvisning`, not decoration. Remove unreferenced `bilag`. Match table-of-contents depth to report length.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Drafting before local `formalia` are known | Ask for rules or state assumptions visibly |
| Writing about `noget om ...` | Convert topic to `problemformulering` |
| Weak audience definition | Name `målgruppe` or create a concrete `persona` |
| Source dump | Classify material, then synthesize around the question |
| Google or ChatGPT in source list | Replace with actual sources or disclose as tools only |
| Conclusion only summarizes | Rewrite as a direct answer to `problemformulering` |
| Conclusion repair invents evidence | Use placeholders and request the missing analysis, source, or interview support |
| Inflated academic Danish | Use clear, active, audience-aware Danish |

## What to return

When helping with a report, give the requested artifact and briefly state:

- Which assumptions were made because user information was missing.
- Which report stage was handled: planning, synopsis, drafting, revision, citation audit, or service-section audit.
- Any blocking `formalia`, source, or problem-formulation issues that must be resolved before final delivery.

If the user asks what they missed, check for: local rules, audience, purpose, report type, `problemformulering`, `hypotese`, scope, source metadata, citation style, required service sections, and whether the conclusion actually answers the question.
