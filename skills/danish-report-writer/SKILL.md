---
name: danish-report-writer
description: Use when planning, drafting, revising, or reviewing Danish reports, including requests like "lav en rapport", "skriv en rapport", "write me a report in Danish", problemformulering, synopsis, kilder, kildehenvisninger, rapportsprog, serviceafsnit, or educational and workplace formalia.
license: MIT
compatibility: claude-code opencode
---

# Danish report writer

## Overview

A Danish `rapport` is a `faglig`, `saglig` answer to a real question, written so a specific reader can use it. Do not draft before audience, purpose, local rules (`formalia`), `problemformulering`, and source basis are clear.

This file is the routing hub. Load only the reference file matching the current task — do not read all references up front.

Do not use for ordinary emails, blog posts, essays, fiction, or non-Danish report conventions unless the user explicitly asks to adapt this Danish model.

## Routing to reference files

| Need | Load |
|---|---|
| Choose work mode, collect `afsender`/`målgruppe`/`formål`/`formalia`, offer 3-suggestion intake prompts | `references/intake-and-modes.md` |
| Narrow a broad `emne`, draft `problemformulering`/`hypotese`, build the 9-part `synopsis` | `references/synopsis-and-problemformulering.md` |
| Draft or repair `indledning`, `analyseafsnit` (`redegørelse` → `undersøgelse` → `diskussion`), or a `konklusion` that must answer the question | `references/main-sections.md` |
| Classify material, reject Google/chatbots as sources, audit `kildehenvisninger` and `kildefortegnelse` | `references/sources-and-citations.md` |
| Phased drafting (`skriveproces`), `rapportsprog`/`fagsprog` language pass | `references/rapportsprog-and-process.md` |
| Audit `forside`, `indholdsfortegnelse`, `resumé`, `bilag`, other support sections | `references/serviceafsnit-audit.md` |

## Working order

1. Intake `formalia` and reader context (`references/intake-and-modes.md`).
2. Narrow `emne` → `afgrænsning`; draft `problemformulering` and optional `hypotese`; build the 9-part `synopsis` (`references/synopsis-and-problemformulering.md`).
3. Classify `kilder og data` before writing paragraphs (`references/sources-and-citations.md`).
4. Draft `hovedafsnit` before `serviceafsnit` (`references/main-sections.md`).
5. Revise `rapportsprog`; keep drafting and polishing apart (`references/rapportsprog-and-process.md`).
6. Audit citations and `serviceafsnit` (`references/serviceafsnit-audit.md`).
7. Final gate: compare `problemformulering` and `konklusion` side by side. If the conclusion does not answer the question, the report is not done.

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

## Common mistakes

| Mistake | Fix |
|---|---|
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

## Attribution

Based primarily on Per Salling's 12-part `Skriv bedre rapporter!` series on Omatskrive.dk. Article-by-article source notes live in `references/source-notes.md` (maintainer reference — not needed for normal report work).
