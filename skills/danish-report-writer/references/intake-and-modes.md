# Intake and modes

Use before any planning or drafting of a Danish report.

## Choose mode

When the user asks for a Danish report without specifying the work mode, ask them to choose:

1. `Guided intake`: best when the user only has a subject. Ask required elements one at a time.
2. `Fast assumptions`: best when the user needs speed. Draft visible assumptions for all required elements and ask the user to approve or correct them.
3. `Existing report audit`: best when the user already has text. Audit gaps before rewriting.

If the prompt clearly includes an existing report or asks to fix one, use `Existing report audit` and ask for the report text if it is missing. If the user explicitly asks for speed, use `Fast assumptions`. Otherwise, ask mode first.

## Required elements before drafting

- `Afsender`: who is writing or speaking?
- `Målgruppe`: who must use the report?
- `Formål`: what should the reader know, decide, or do afterward?
- Context: education, workplace, public sector, or other institution?
- `Formalia`: assignment brief, rubric, template, page count, citation style, layout rules, submission requirements.
- Report type: descriptive, explanatory, or investigative/problem-solving.
- `Problemformulering`: the exact question the report answers.
- Source basis: what data, sources, observations, interviews, or empirical material can support the report?

If one of these is missing and matters for the job, ask one focused question before drafting. If the user insists on speed, state the assumptions visibly.

## Help the blank user choose

When a required element is missing, do not ask a blank open question. Give exactly three context-aware suggestions plus a custom option:

```text
Målgruppe:
A. [suggestion based on what is already known]
B. [different plausible suggestion]
C. [different plausible suggestion]
D. Skriv selv
```

Base suggestions on the subject, user wording, education/work context, existing notes, uploaded report text, or likely reader. Do not invent source facts. If context is lacking, make suggestions broad but useful.

Use three suggestions plus `Skriv selv` for these elements when missing or weak: `afsender`, `målgruppe`, `formål`, context or institution, `formalia`, report type, `problemformulering`, `hypotese` when relevant, `afgrænsning`, source basis, citation style, required `serviceafsnit`.

In `Guided intake`, ask about one element at a time. In `Fast assumptions`, show a compact assumption sheet with three alternatives for the uncertain elements and ask for approval. In `Existing report audit`, first show what is missing or weak, then offer three fixes for each important gap.
