---
name: danisher
description: Use when composing or editing any deliverable containing Danish prose for an external reader — kundemails, tilbud, fakturanotater, aftaletekst, rapportafsnit, præsentationstekst, UI-tekst, nyhedsbreve — including when Danish is only one part of a larger technical artifact (a Danish appendix, quote, or email body inside English work). Trigger on "skriv på dansk", "skriv en mail til kunden", "skriv et tilbud", "ret min danske tekst", or any request whose output is Danish prose a customer, partner, myndighed or colleague will read. Do NOT trigger on Danish variable names, Danish tenant/domain strings, Danish legal clauses quoted verbatim as data, or Danish words quoted inside an English technical discussion.
license: MIT
compatibility: claude-code opencode
---

# Danisher

## Overview

AI-written Danish carries English syntax, idioms and rhythm even when grammar is correct. Fix register and rhythm, keep terminology. Stripping English technical vocabulary is the most common over-correction and makes text worse.

Load reference files on demand:
- `references/registers.md` — register table, intake, pre-flight, kanal. Load when composing new Danish from a brief or choosing a register row.
- `references/danish-tells.md` — D1–D10 with worked examples. Load when auditing or editing Danish text, or when a scanner check needs a worked example.
- `references/typography.md` — D8 typography and number table. Load when the scanner flags typography, numbers, dates, currency or comma system.

## Hard rule: never invent facts

Prefer concrete numbers, names and dates over adjectives. That is a rule about *which of the available facts to use*, not a licence to produce new ones.

- **REDIGER:** every proposition and every relationship in output must appear in the source. Preserve facts, claims, attribution, modality, tense, aspect, negation, quantifiers, actors, addressees, obligations, permissions, commitments, numbers, dates, names, causes and objects of vague terms. Vague attribution stays vague; mark the gap `[kilde?]`.
- **Source-bound SKRIV:** English source plus "på dansk" uses SKRIV's composition method, not its freedom to omit. Preserve every source proposition and protected string. Restructure prose; do not summarize, strengthen, weaken or reassign unless the user names the permitted transformation.
- **SKRIV:** use every fact the brief supplies. Preserve each value and identity while applying Danish notation from `references/typography.md`. For missing facts, write `[X kunder]`, `[antal]`, `[produktnavn]` and list placeholders at the end. A bracketed gap is correct output. Replacing a supplied figure with a placeholder or inventing a plausible number are both failures.
- Three classes slip past the obvious check:
  - **Årsag.** Brief says `planlagt nedetid`. Writing `Vi opdaterer systemet` invents a reason. Write `[årsag]` or leave it out.
  - **Objektet for et vagt ord.** Source says `problemfri integration` without saying with what. Writing `integrerer med jeres Microsoft 365` invents the object. Write `[hvilke systemer?]`.
  - **Den udledte beroligelse.** Brief says `ingen data går tabt`. Writing `I skal ikke foretage jer noget` adds a commitment nobody made.
- **Do not change modality, tense or aspect.** `kan bidrage til` may not become `bidrager`. `vil transformere` may not become `transformerer`. `udrulles i næste uge` may not become `er udrullet`. Remove a stacked hedge only when removed words are genuinely synonymous; if uncertain, leave it. Never remove the last qualification. In legal, contractual, SLA and driftstekst this is the most damaging edit in the file.
- **Do not add or remove stance or focus.** In REDIGER, preserve existing modal particles, focus adverbs and stance phrases. Do not insert `jo`, `da`, `vel`, `nok`, `dog`, `netop` or `i øvrigt` merely to meet a style target.
- **Do not reassign who asserts a claim or who must act.** `Det understreges, at opdatering bør prioriteres` is agentless. `Vi anbefaler, at I opdaterer` invents sender and obligation. In REDIGER, activate a passive only when the source already names every role.
- **Do not widen quantifiers or flip negation scope.** `nogle kunder` may not become `kunderne`. `visse regioner` may not become `alle`. `ingen kendte sårbarheder` may not become `sikker`. `en række` → specific number only when source states it.
- **Preserve attributed quotes and mandated wording.** In REDIGER, verbatim. In source-bound translation, translate faithfully; preserve attribution, modality, scope and quotation status. For statutory, contractual or regulator-supplied wording, ask whether original is retained or a clearly labelled non-authoritative translation. A scare-quoted idiom like `"sæt op og glem"` is not an attributed quote.
- **Preserve functional strings exactly.** Code spans, variables, localization placeholders, commands, flags, URLs, IDs and product identifiers are mandated wording. Preserve characters and surrounding delimiters.
- **Non-assertive metadata may expose a gap.** Bracketed questions and audit notes may describe input or edit; they may not supply an answer or assert an external fact.
- **Deletion follows the same rule.** Never assume repeated wording is accidental. Delete only when user authorizes shortening and requested emphasis survives. Labels like `positionering`, `fyld`, `reklamesprog` and `generisk` are not permission to delete source meaning. A tone request changes only the named stance, never facts, claims, promises, recommendations or commitments.

When rhythm and accuracy conflict, accuracy wins.

## Modes

Route on input.

| Input | Mode | What to do |
| --- | --- | --- |
| Existing Danish text | REDIGER | Draft rewrite, run scanner, final version |
| A brief, topic or bullet points | SKRIV | Write Danish copy that never had the tells |
| English text plus "på dansk" | SKRIV, source-bound | Write from meaning while preserving every source claim and protected string |

Sentence-by-sentence translation produces nearly every problem in `references/danish-tells.md`. Read English, understand the point, write Danish from scratch without dropping or changing any source meaning. If user requests a transformation, only its explicit dimensions may change.

## Pre-emit scanner

Run before delivering. Mechanical checks first, meaning-preservation checks second. Each item passes or fails; fix every failure before emitting.

**Mechanical**

1. Em-dash `—` present → must be `–` with surrounding spaces. See `references/typography.md`.
2. Decimal `.` in numbers (`1.100,00`, `9.8`) → must be `,` (`1.100,00`, `9,8`). See `references/typography.md`.
3. Thousands `,` (`1,000,000`) → must be `.` (`1.000.000`). See `references/typography.md`.
4. `%` spacing inconsistent within document (`20 %` then `30%`) → pick one form and hold it. See `references/typography.md`.
5. Weekday, month or nationality adjective capitalized (`Mandag`, `Maj`, `Dansk lovgivning`) → lowercase (`mandag`, `maj`, `dansk`). See `references/typography.md`.
6. Comma system: one chosen, held throughout; `såfremt`/`hvis`/`når`/`at` clauses consistent within the chosen system. See `references/typography.md`.
7. Group compound missing boundary hyphen (`Conditional Access politik`, `Zero Trust arkitektur`) → `Conditional Access-politik`, `Zero Trust-arkitektur`. See `references/danish-tells.md` D7.

**Meaning preservation**

8. Every number, name, date and commitment traceable to input. Untraceable → replace with bracketed placeholder or delete.
9. Modality unchanged: no `kan` → present tense, no `vil` → present tense, no `bør` → `skal`, no modal removed or strengthened. See worked example in `references/danish-tells.md` D10.
10. Register row selected and held; no understatement in myndigheds-, jura-, sikkerheds-, drift-, status- eller SLA-tekst. See `references/registers.md`.

## REDIGER mode: editing existing Danish text

Before rewriting, work out four things from source. Infer only what text makes unambiguous; if register or communicative situation materially changes the edit and source does not reveal it, ask one short clarification.

1. **Register.** Et tilbud på 1,5 mio. kr. and a LinkedIn-opslag get different treatment. Infer from genre and communicative situation, not merely price, deliverable or deadline. See `references/registers.md`.
2. **Tiltaleform already in use.** Keep it. Do not switch reader from `du` to `I` mid-edit.
3. **Meaning-bearing material.** Mark facts, claims, attribution, modality, tense, aspect, negation, quantifiers, actors, obligations and protected strings. Rewrite only if all meaning survives.
4. **Positioning and stance.** Tighten wording; delete a claim, promise or recommendation only when user explicitly authorizes content reduction. A tone request changes named emotion or stance, not other propositions or commitments. List authorized deletions unless user requests text only.

Then rewrite, run the scanner, deliver.

### REDIGER example

**Opgave:** *Stram teksten op ved at fjerne den ordrette gentagelse.*

**Før:**
> Vi lancerer Backup Lite den 14. marts. Backup Lite er vores nye løsning. Backup Lite er vores nye løsning. Den kan sikkerhedskopiere op til 2 TB. Microsoft oplyser, at den understøtter Windows 11. Det understreges, at installation bør prioriteres.

**Endelig version:**
> Vi lancerer Backup Lite den 14. marts. Det er vores nye løsning, og den kan sikkerhedskopiere op til 2 TB.
>
> Microsoft oplyser, at den understøtter Windows 11.
>
> Det understreges, at installation bør prioriteres.

Exact duplicate removed; its proposition appears once. `Backup Lite`, `14. marts`, `2 TB`, `Microsoft`, `Windows 11`, `kan`, `oplyser` and agentless `Det understreges` all stayed. Scanner: no typography failures; every number, name, date and commitment traces to input; modality `kan` preserved.

## SKRIV mode: writing new Danish copy

Load `references/registers.md`. It contains intake questions, pre-flight checklist, register table, kanal defaults and a worked example.

## Process

Both modes end the same way. The scanner above is not optional; the first draft always keeps tells you cannot see while generating. Draft the best version, run every scanner check, fix every failure, ask in Danish *"Hvad afslører stadig, at det her er AI-skrevet?"*, record zero to four findings for possible delivery (cap applies only to surfaced notes, never internal audit), revise against scanner and audit.

## Output format

Default by length, not mode. `ret lige den her` and `pudse lige` signal informality, not a request for commentary.

| Situation | Deliver |
| --- | --- |
| Under roughly 200 words | Final text, placeholder list, any authorized deletion list, plus at most three other change bullets |
| Over roughly 200 words | Final text, any actual audit findings, placeholder list and any authorized deletion list |
| User says `kun teksten`, `bare giv mig den`, `no commentary` | Final text only. Keep unresolved placeholders visible inline; do not add separate lists. |

Audit notes and change summaries are written in the same language as the deliverable. When surfacing the skill's internal English terminology in Danish-facing commentary, translate: ask → opfordring, tell → afslørende træk, hedge → forbehold, burstiness → sætningsvariation, signposting → vejvisning.

Generate draft and run complete scanner internally. Do not expose a draft already known to contain unsupported or altered meaning. Surface only concise findings that remain relevant. Always surface bracketed placeholders, in every format, including the short one. A placeholder the user does not see is the same failure as an invented number.
