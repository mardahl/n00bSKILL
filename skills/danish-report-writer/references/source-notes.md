# Danish Report Writer Source Notes

Primary source: Per Salling, Omatskrive.dk, `Skriv bedre rapporter!`, a 12-part report-writing series.

These notes are paraphrased implementation guidance for the `danish-report-writer` skill. They are not copied source articles.

## 1. Hvad er en god rapport?

URL: https://www.omatskrive.dk/rapportteknik/hvad-er-en-god-rapport/

Core use in skill: Begin with `afsender`, `målgruppe`, `formål`, and report type. A report is `faglig`, `saglig`, concrete, purposeful, and reader-usable.

Agent rules:

- Require sender, target audience, purpose, and intended use before drafting.
- Classify report type as descriptive, explanatory, or investigative/problem-solving.
- Organize for reader needs rather than writer interest.
- Make the report easy to read, understand, and use.

Anti-patterns:

- Treating the report as a school essay, article, or generic assignment.
- Accumulating information without selection or commentary.
- Forgetting the reader as a real person.

## 2. Rapportens struktur

URL: https://www.omatskrive.dk/rapportteknik/rapportens-struktur/

Core use in skill: Separate final report order from drafting order. Write `hovedafsnit` before `serviceafsnit`.

Agent rules:

- Use `serviceafsnit` and `hovedafsnit` as structural categories.
- Build `indledning`, `analyseafsnit`, and `konklusion` around the main question.
- Use the canonical report sections as a final checklist, not as the drafting sequence.

## 3. Rapportens formål

URL: https://www.omatskrive.dk/rapportteknik/rapportens-formal/

Core use in skill: Narrow the topic and define `problemformulering` early.

Agent rules:

- Clarify assignment source and local purpose.
- Narrow from broad `emne` to focused scope.
- Require `målgruppe`, optional `persona`, and an answerable `problemformulering`.
- Reject yes/no, vague, or unbounded questions.

## 4. Hypotesen - det, du vil undersøge

URL: https://www.omatskrive.dk/rapportteknik/hypotesen-det-du-vil-undersoge/

Core use in skill: Convert a topic into an interesting, testable `hypotese` or `arbejdshypotese`.

Agent rules:

- Distinguish `hypotese`, `antagelse`, and `teori`.
- Validate why the investigation matters to the `målgruppe`.
- Define what evidence could support, weaken, or reject the hypothesis.

## 5. En god model til en synopsis

URL: https://www.omatskrive.dk/rapportteknik/en-god-model-til-en-synopsis/

Core use in skill: Use the 9-part synopsis as the planning gate before drafting.

The nine prompts:

1. `Mit emne er ...`
2. `Det er et "problem", at ...`
3. `Det er et "problem" for ...`
4. `Jeg vil undersøge, om "problemet" skyldes ...`
5. `Jeg vil derfor finde svaret på dette spørgsmål ...`
6. `Rapporten skal kunne bruges af ... til at ...`
7. `Jeg vil kun beskæftige mig med ... fordi ...`
8. `Jeg vil bygge rapporten på ...`
9. `Jeg vil gøre sådan-og-sådan ...`

Agent rules:

- Require complete sentences, not keywords.
- Treat the synopsis as future-looking planning, not final report prose.
- Do not copy future-tense method text into the final method section.

## 6. Kilder og data

URL: https://www.omatskrive.dk/rapportteknik/kilder-og-data/

Core use in skill: Make source quality and `kildekritik` part of planning and drafting.

Agent rules:

- Classify material as `selve stoffet`, `nødvendig baggrundsviden`, or irrelevant.
- Reject Google and chatbots as sources.
- Explain why each source matters alone and in relation to other evidence.
- Cut interesting material outside the `afgrænsning`.

## 7. Rapportens hovedafsnit

URL: https://www.omatskrive.dk/rapportteknik/rapportens-hovedafsnit/

Core use in skill: Build `indledning`, `analyseafsnit`, and `konklusion` as a question-answer system.

Agent rules:

- Draft `indledning` from broad field to precise question, scope, method, audience, and purpose.
- Structure analysis as `redegørelse`, `undersøgelse`, `diskussion`.
- Make `konklusion` directly answer `problemformulering`.
- Add `metodekritik` and `perspektivering` only when useful.

## 8. Skriveprocessen

URL: https://www.omatskrive.dk/rapportteknik/skriveprocessen/

Core use in skill: Enforce phased writing.

Agent rules:

- Draft raw `indhold` first.
- Reorder before polishing language.
- Rewrite into coherent Danish only after content and order are stable.
- Correct spelling, punctuation, and commas near the end.

## 9. Godt rapportsprog

URL: https://www.omatskrive.dk/rapportteknik/godt-rapportsprog/

Core use in skill: Add a Danish report-language revision pass.

Agent rules:

- Use `fagsprog` only when the `målgruppe` can use it.
- Do not simplify the subject; simplify the language.
- Prefer active language when responsibility matters.
- Lower unnecessary abstraction and inflated academic phrasing.

## 10. Kildehenvisninger

URL: https://www.omatskrive.dk/rapportteknik/kildehenvisninger/

Core use in skill: Add citation and bibliography audit.

Agent rules:

- Require claim-level references plus full `kildefortegnelse`.
- Prefer `fodnoter` over `slutnoter` unless local rules say otherwise.
- Use precise digital source links.
- Do not list unused sources as used sources.

## 11. Serviceafsnittene

URL: https://www.omatskrive.dk/rapportteknik/serviceafsnittene/

Core use in skill: Treat service sections as the report's `brugsanvisning`.

Agent rules:

- Add or audit `forside`, optional `titelblad/kolofon`, `indholdsfortegnelse`, `resumé`, `forord`, `kildefortegnelse`, and `bilag` as needed.
- Keep table-of-contents depth proportional to report length.
- Remove unused or show-off appendices.
- Reference appendices from the main text.

## 12. Mere om rapportskrivning

URL: https://www.omatskrive.dk/rapportteknik/mere-om-rapportskrivning/

Core use in skill: Local requirements override generic guidance.

Agent rules:

- Ask whether the report is educational, workplace, public-sector, or another institutional context.
- Ask for `retningslinjer`, rubric, template, page count, citation style, and layout rules.
- Do not finalize structure or formatting without explicit rules or stated assumptions.

## Combined Skill Requirements

A Danish report-writing agent should:

- Start with reader, purpose, assignment context, and local requirements.
- Convert topic into a focused `problemformulering` and relevant hypothesis where needed.
- Use a 9-part `synopsis` before full drafting when planning is missing.
- Classify sources and data before writing paragraphs.
- Draft main sections before support sections.
- Audit citations and source list before final delivery.
- Use clear, direct Danish suited to the target audience.
- Treat service sections as the reader's practical guide to the report.
