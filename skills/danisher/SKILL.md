---
name: danisher
description: Use when writing or editing Danish copy of any kind, including marketing text, kundemails, LinkedIn-opslag, reports, UI-tekst, nyhedsbreve and documentation, and especially when Danish text reads translated, stiff, over-polished or too enthusiastic, or when the user asks to "skrive på dansk", "rette min danske tekst", "gøre teksten mindre AI-agtig", or wants English source material rendered as natural Danish.
license: MIT
compatibility: claude-code opencode
---

# Danisher

## Overview

AI-written Danish often carries English syntax, idioms and rhythm even when the grammar is correct. This skill targets those observable traces without guessing how the text was produced.

Core principle: **fix the register and the rhythm, keep the terminology.** Danish business and IT writing legitimately uses English technical vocabulary. Stripping it out is the most common over-correction and it makes the text worse, not better.

## Hard rule: never invent facts

This skill tells you to prefer concrete numbers, names and dates over adjectives. That is a rule about *which of the available facts to use*, not a licence to produce new ones.

- **REDIGER:** every proposition and every relationship in your output must appear in the source. Preserve facts, claims, attribution, modality, tense, aspect, negation, quantifiers, actors, addressees, obligations, permissions and commitments. Preserve numbers, dates, names, causes and the objects of vague terms. If the source uses vague attribution or the text requires a citation, keep the claim and its original attribution, then mark the gap `[kilde?]` or `[hvilken kilde?]`.
- **Source-bound SKRIV:** English source plus "på dansk" uses SKRIV's composition method, but not its freedom to omit material. Preserve every source proposition and protected string. Restructure the prose; do not summarize, strengthen, weaken or reassign it unless the user explicitly names the permitted transformation, such as a summary with a stated length.
- **SKRIV:** use every fact the brief supplies, including statistics. Preserve each value and identity while applying Danish notation from D8. For missing facts, write `[X kunder]`, `[antal]`, `[produktnavn]` and list the placeholders at the end. A bracketed gap is correct output. Replacing a supplied figure with a placeholder or inventing a plausible number are both failures.
- Rewriting `omfattende beskyttelse` into `beskyttelse af 400 endpoints` is fabrication even though it reads better. If the source did not say 400, you may not either.
- Three classes slip past the obvious check, because they feel like clarification rather than addition:
  - **Årsag.** The brief says `planlagt nedetid`. Writing `Vi opdaterer systemet` invents a reason. Write `[årsag]` or leave it out.
  - **Objektet for et vagt ord.** The source says `problemfri integration` without saying with what. Writing `integrerer med jeres Microsoft 365` invents the object. Write `[hvilke systemer?]`.
  - **Den udledte beroligelse.** The brief says `ingen data går tabt`. Writing `I skal ikke foretage jer noget` adds a commitment about the reader's obligations that nobody made.
- **Do not change modality, tense or aspect.** `kan bidrage til` may not become `bidrager`. `vil transformere` may not become `transformerer`. `udrulles i næste uge` may not become `er udrullet`. `hjælper med at identificere` may not become `finder`. `fungerer som databehandler` may not become `er databehandler`. Remove a stacked hedge only when the removed words are genuinely synonymous in context; if uncertain, leave it. Never remove the last qualification. In legal, contractual, SLA and driftstekst this is the most damaging edit in the file.
- **Do not add or remove stance or focus.** In REDIGER, preserve existing modal particles, focus adverbs and stance phrases. Do not insert `jo`, `da`, `vel`, `nok`, `dog`, `netop` or `i øvrigt` merely to meet a style target; they can add shared knowledge, reservation, certainty, focus or presupposition.
- **Do not reassign who asserts a claim or who must act.** `Det understreges, at opdatering bør prioriteres` is agentless. Turning it into `Vi anbefaler, at I opdaterer` invents both a sender and an obligation. In REDIGER, activate a passive only when the source already names every role used by the active sentence.
- **Do not widen quantifiers or flip negation scope.** `nogle kunder` may not become `kunderne`. `visse regioner` may not become `alle`. `ingen kendte sårbarheder` may not become `sikker`. Replacing `en række` with a specific number is only allowed when the source states the number.
- **Preserve attributed quotes and mandated wording.** In REDIGER, leave them verbatim. In source-bound translation, translate an attributed quote faithfully when the user asks for the whole source in Danish; preserve its attribution, modality, scope and quotation status, and do not polish or paraphrase it. For statutory, contractual or regulator-supplied wording, ask whether the user wants the original retained or a clearly labelled non-authoritative translation. A scare-quoted idiom like `"sæt op og glem"` is not an attributed quote and is fair game.
- **Preserve functional strings exactly.** Code spans, variables, localization placeholders, commands, flags, URLs, IDs and product identifiers are mandated wording unless the user explicitly asks to change them. Preserve their characters and surrounding delimiters; do not add or remove quotes, backticks or code fences around paste-ready strings.
- **Non-assertive metadata may expose a gap.** Bracketed questions and audit notes may describe the input or edit, but they may not supply an answer or assert an external fact.
- **Deletion follows the same rule.** Never assume repeated wording is accidental; repetition can carry emphasis or rhythm. Delete it only when the user authorizes shortening and the requested emphasis still survives. Labels such as `positionering`, `fyld`, `reklamesprog` and `generisk` are not permission to delete source meaning. Only explicit permission to shorten or remove content authorizes deleting a proposition. A tone request may change only the named stance, never facts, claims, promises, recommendations or commitments.

When rhythm and accuracy conflict, accuracy wins.

## Modes

Route on what the user gives you.

| Input | Mode | What to do |
| --- | --- | --- |
| Existing Danish text | REDIGER | Draft rewrite, then self-audit, then final version |
| A brief, topic or bullet points | SKRIV | Write Danish copy that never had the tells |
| English text plus "på dansk" | SKRIV, source-bound | Write from the meaning while preserving every source claim and protected string |

The last row is the important one. Sentence-by-sentence translation is what produces nearly every problem documented below. Read the English, understand the point, then write it in Danish from scratch without dropping or changing any source meaning. If the user requests a transformation, only its explicit dimensions may change.

## SKRIV mode: writing new Danish copy

### Intake

Ask before writing, not after. These three answers change every sentence, and guessing them is the most common reason a first draft has to be thrown away. Ask them in brief-based SKRIV for what the brief does not answer. In source-bound rendering, ask one short clarification only when an ambiguity prevents faithful preservation. A brief that says "kundemail til Morten om at leveringen er forsinket, ny dato 14. marts" has answered all three: én person, kundemail, informér.

Present them as a multiple-choice list. If the host application has an interactive question tool, use it. Otherwise number them in chat and wait for one reply.

1. **Hvem skriver I til?**
   - én person → `du`
   - en virksomhed eller et team → `I/jer`
   - offentligheden med direkte tiltale → `du`
   - offentligheden uden direkte tiltale → upersonlig

2. **Hvilken slags tekst?**
   - marketing eller social
   - kundemail eller tilbud
   - fagpresse eller analyse
   - intern note
   - drift, status eller release notes
   - myndighed, jura eller sikkerhed

3. **Hvad skal teksten udrette?**
   - informere
   - sælge eller overbevise
   - bede læseren om at gøre noget
   - berolige
   - dokumentere

Answer 2 selects a row in the register table below. Answer 3 decides where the point goes and how the text ends: a `bed om handling`-text ends on the ask, a `berolig`-text ends on what happens next, and a `dokumentér`-text does not end on anything.

Do not ask about facts here. Missing facts become bracketed placeholders, per the hard rule. Asking the user to supply a statistic mid-draft is the same mistake as inventing one, just slower.

### Pre-flight

Settle these before the first sentence in brief-based SKRIV. Intake answers 1 and 2 cover pre-flight 1 and 2; answer 3 informs pre-flight 4. Pre-flight 3 comes only from an explicitly named sender in the brief. In source-bound SKRIV, derive audience, register, sender, stance and commitments from the source instead of applying these defaults.

1. **Tiltaleform.** An explicit brief always wins. When unspecified: `du` for one person or a directly addressed public audience, `I/jer/jeres` for a company or team, upersonlig for notices without direct address. Never `De` unless asked. For an otherwise ambiguous B2B social post, use `I/jer` for operational content and `du` for personal content. Pick one and hold it.
2. **Register.** Pick one row and stay in it.

   | Register | Sætninger | Fragmenter | Underspil (D4) |
   | --- | --- | --- | --- |
   | Marketing / social | korte, varierede | ja | ja, ét sted |
   | Kundemail / tilbud | mellemlange | sparsomt | ja, sparsomt |
   | Fagpresse / analyse | varierede, lange tåles | nej | ja |
   | Intern note | korte, telegramagtige | ja | ja |
   | Drift, status, release notes | korte, fulde sætninger | nej | **nej** |
   | Myndighed, jura, sikkerhed | fulde sætninger | nej | **nej** |

   Modalpartikler are not in this table. D6 explains when they sound natural in SKRIV and why REDIGER must preserve the source's stance instead of meeting a quota.

3. **Afsender.** An explicit brief always wins. Use `vi` only when the brief identifies the writing organization as claimant; use `jeg` only when it identifies an individual. Otherwise stay impersonal or use `[afsender]`. Never invent `vi`, `jeg` or an addressee to activate a passive.
4. **Point first.** Say the thing in the first or second sentence. Do not warm up for three sentences of context.
5. **Rhythm.** Vary sentence length on purpose, and let some sentences be very short. Do not apply a quota: long-long-short in every single paragraph is itself uniform, which is the tell you are trying to kill. Diagnostic: if you can predict the shape of the next sentence from the last three, rewrite.
6. **Modalpartikler.** Use them only when they express a stance the brief supports. They are a diagnostic, not a quota: short text may need none, and overdosing sounds like a transcript. See D6.
7. **Konkrete tal og navne slår adjektiver, når du har dem.** `fire regioner` beats `en række regioner`. `9,8 i CVSS` beats `kritisk`, if someone gave you the 9,8. If the brief gave you no number, write `[antal]`, not a number you made up. See the hard rule above.

### Kanal

Only the constraints that actually change the copy.

These are brief-based SKRIV defaults only. In source-bound modes, a channel name does not authorize reordering qualifiers, removing greetings or asks, changing statements into imperatives, or changing scope, obligation, addressee, modality or stance.

- **LinkedIn:** put the point in the first sentence. Use short paragraphs. Put up to three hashtags at the end, or use none.
- **Kundemail:** subject line carries the point. No greeting theatre. Prefer one ask at the end unless the brief explicitly requires more.
- **UI-tekst:** use imperative in action buttons: `Gem`, not `Gemme` or `Gem dine ændringer nu`. Infinitive can fit navigation labels only when the product's established pattern uses it.
- **Rapport:** see the `danish-report-writer` skill for structure. This skill is the language pass.

### SKRIV example

Brief: *"LinkedIn-opslag om at vi lancerer en backup-løsning til mindre virksomheder. Max 150 ord."*

Intake: the brief says LinkedIn, so question 2 is answered. `Til mindre virksomheder` describes the market, not necessarily the addressee, so questions 1 and 3 remain open. Answers here: `en virksomhed eller et team` and `bed læseren om at gøre noget`.

Pre-flight: register marketing/social, afsender `vi`, no product name, scope or requested action in the brief, so those facts stay bracketed.

**Endelig version:**
> Vi lancerer [produktnavn]: backup til mindre virksomheder. [Hvad dækker den?]
>
> [Hvad skal læseren gøre?]

Mangler før publicering: `[produktnavn]`, `[Hvad dækker den?]` og `[Hvad skal læseren gøre?]`.

That post is well under the 150-word budget, and it is thin. The brief plus intake answers support the launch, product category, audience and purpose; everything else remains visible as a gap. At this length, deliver only that final version and its three-item placeholder list.

## REDIGER mode: editing existing Danish text

Before rewriting, work out four things from the source. Getting these wrong is worse than leaving a tell in. Infer only what the text makes unambiguous; if register or communicative situation materially changes the edit and the source does not reveal it, ask one short clarification.

1. **Register.** Et tilbud på 1,5 mio. kr. and a LinkedIn-opslag get different treatment. Infer register from the genre and communicative situation, not merely from a price, deliverable or deadline.
2. **Tiltaleform already in use.** Keep it. Do not switch the reader from `du` to `I` mid-edit.
3. **Meaning-bearing material.** Mark facts, claims, attribution, modality, tense, aspect, negation, quantifiers, actors, obligations and protected strings. Rewrite them only if all meaning survives.
4. **Positioning and stance.** Treat these as source content too. Tighten wording, but delete a claim, promise or recommendation only when the user explicitly authorizes content reduction. A tone request may change the named emotion or stance, not other propositions or commitments. If authorized deletions occur, list them unless the user requests text only.

Then rewrite, self-audit and deliver.

### REDIGER example

**Opgave:** *Stram teksten op ved at fjerne den ordrette gentagelse.*

**Før:**
> Vi lancerer Backup Lite den 14. marts. Backup Lite er vores nye løsning. Backup Lite er vores nye løsning. Den kan sikkerhedskopiere op til 2 TB. Microsoft oplyser, at den understøtter Windows 11. Det understreges, at installation bør prioriteres.

Pre-flight: register does not affect this edit. The source supplies first-person plural, product, date, capacity, platform, named claimant and the recommendation's agentless form; it does not identify who `vi` denotes.

**Udkast:**
> Vi lancerer Backup Lite den 14. marts. Det er vores nye løsning. Den kan sikkerhedskopiere op til 2 TB.
>
> Microsoft oplyser, at den understøtter Windows 11.
>
> Det understreges, at installation bør prioriteres.

**Hvad afslører stadig AI?**
- The source repeats `Backup Lite er vores nye løsning` twice verbatim; the draft retains the proposition once.
- The first paragraph still has three equal declaratives; combine the two adjacent claims without changing them.
- Names, dates, numbers, modality and attribution must remain unchanged.

**Endelig version:**
> Vi lancerer Backup Lite den 14. marts. Det er vores nye løsning, og den kan sikkerhedskopiere op til 2 TB.
>
> Microsoft oplyser, at den understøtter Windows 11.
>
> Det understreges, at installation bør prioriteres.

The exact duplicate was removed; its proposition appears once. `Backup Lite`, `14. marts`, `2 TB`, `Microsoft`, `Windows 11`, `kan`, `oplyser` and the agentless `Det understreges` all stayed. The draft and audit are shown here to expose the process; at this length, deliver only the final version and a short change note if it helps.

## Danish-specific tells

These are the ones English word lists cannot see.

Every `Efter` below is derivable from its own visible `Før`: no new content and no change to attribution, modality, tense, aspect, agent, negation or quantifier scope. If extra source material is needed, the example displays it.

### D1. Calqued English idioms

The flagship Danish tell. The model translates an English saying word for word and produces a phrase no Dane would write.

A native writer has two legitimate moves with an English saying: use a real Danish equivalent, or keep the English verbatim. Danish also *semi-ingests* English, keeping the English spelling but reading it as Danish. The clumsy literal translation is the giveaway that a machine sat in between.

**Opgave:** *Erstat den bogstavelige vending. Den forklarende gentagelse må forkortes, hvis hele forklaringen bevares i den valgte formulering.*

**Før:**
> Det er en "sæt op og glem"-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb.

**Efter, tre gyldige muligheder:**
> Det er en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(dansk omskrivning)*
> Det er en "set and forget"-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(engelsk ækvivalent, i citationstegn)*
> Det er en set-and-forget-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(indoptaget: engelsk stavning, læst som dansk)*

Watch for: `ved slutningen af dagen` (→ `i sidste ende` when that is the meaning), `på samme side` (→ `enige` only when the source asserts agreement), `tænke uden for boksen` (keep English or rewrite without adding a claim), `tager skridtet` only when used as a literal calque rather than established Danish, `lavthængende frugter` (borderline: some Danes use it, many cringe), `med det sagt` / `når det er sagt` as filler when they carry no contrast.

### D2. Over-explanation and example stacking

AI often repeats the same point in three forms after it has already landed. In REDIGER, repetition, reformulation and summary all require authorization to shorten; examples that add a property or implication must stay.

**Opgave:** *Forkort teksten uden at miste dens påstand.*

**Før:**
> En tyv stjæler. Det vil sige, at en tyv stjæler. Kort sagt: En tyv stjæler.

**Efter:**
> En tyv stjæler.

Both removed sentences repeat `En tyv stjæler` without another property, actor or qualification. The example assumes the user requested a shorter version; without that authorization, preserve even reformulation and summary relationships.

### D3. English syntax bleeding through

Grammatically correct, but the sentences do not sit the way a Dane would build them.

Signs: grammatically valid but heavy fronting that buries the main point; over-explicit connectors (`Derudover,` `Ydermere,` `I takt med at`) opening sentence after sentence when Danish links more by juxtaposition; `Det handler ikke om X, men om Y` imported wholesale.

**Før:**
> Ved at implementere denne løsning, og ved at sikre at alle processer er optimerede, kan organisationen opnå betydelige fordele.

**Efter:**
> Organisationen kan opnå betydelige fordele ved at implementere denne løsning og ved at sikre, at alle processer er optimerede.

The original clause order already obeys V2; this edit changes information structure and corrects comma placement. The main clause moved to the front, the comma after the opening phrase disappeared, and a clause comma was added after `sikre`. `kan opnå`, `alle`, both `ved at`-phrases, stative `er optimerede` and agent `Organisationen` stayed.

### D4. Flat earnestness

AI copy often reads uniformly sincere and over-positive. Danish commercial and editorial writing can use dry understatement: `det er jo ikke verdens undergang`, `det kan godt være, vi skal kigge en ekstra gang`.

In brief-based SKRIV, dry understatement can suit marketing, kundemail, fagpresse and internal notes. Do not use it in myndighedstekst, legal text, safety instructions, incident notifications, driftsmeddelelser, planlagt nedetid, statusopdateringer, release notes or SLA-varsler. In source-bound modes, do not add dryness or remove enthusiasm unless the user requested that tone change. `Og ja, den kommer op igen` in a maintenance notice is a defect, not voice.

**Før:**
> Vi præsenterer en ny løsning, der vil ændre jeres arbejdsgange.

**Efter:**
> Vi præsenterer en ny løsning. Den vil ændre jeres arbejdsgange.

The edit only splits the relative clause while preserving indefinite `en`, `ny`, future `vil`, actor `vi` and object `jeres arbejdsgange`. Deadpan confirmation is primarily SKRIV advice. In REDIGER, add claims such as `den virker`, habitual `plejer`, sufficiency `nok` or reassurance only when the source states that exact meaning with the same modality.

### D5. Low burstiness and empty scene-setting

Equal-length declaratives padded with `i den moderne digitale verden`, `i nutidens samfund`, `i en verden hvor X`.

In brief-based SKRIV, omit empty scene-setting. In source-bound modes, even broad context can narrow a claim, so preserve it unless the user authorizes its removal.

**Før:**
> AI-detektorer er vigtige værktøjer. De hjælper med at identificere maskinskrevet indhold. Mange organisationer bruger dem. Teknologien udvikler sig konstant.

**Efter:**
> AI-detektorer er vigtige værktøjer. De hjælper med at identificere maskinskrevet indhold, og mange organisationer bruger dem. Teknologien udvikler sig konstant.

The second sentence boundary became a comma plus `og`, and `Mange` became lowercase. Nothing else changed. `hjælper med at identificere` did not become `finder`, and `indhold` did not become `tekst`; that would change the claim.

If this still reads a little flat, that is because the source contains four flat facts. Burstiness you cannot source is decoration. Get the real variation in SKRIV mode, where you control the sentences.

### D6. Manglende modalpartikler

Danish prose, including formal prose, uses modal particles such as `jo`, `da`, `vel`, `nok`, `dog` and `altså` to signal shared knowledge, reservation and stance. Focus adverbs such as `netop` and adverbial phrases such as `i øvrigt` are also meaning-bearing and need the same care in REDIGER.

**Før:**
> Det er da ikke gået ubemærket hen, at Danmark stadig arbejder med NIS2.

**Efter:**
> At Danmark stadig arbejder med NIS2, er da ikke gået ubemærket hen.

The existing `da` and `arbejder` both stayed. Rewriting `arbejder` to `bakser med` would assert a difficulty the source never claimed.

In brief-based SKRIV, use any such marker only when the brief explicitly supports that exact stance or focus; there is no quota. In source-bound modes, preserve existing markers and do not insert one merely to make prose sound Danish. They are not interchangeable.

### D7. Kompositum og bindestreg

Keep five rules separate:

1. **Ordinary compounds:** Danish compounds, including established one-word loans, are written as one word: `sikkerheds opdateringer` → `sikkerhedsopdateringer`; `backupløsning`, `mailserver`, `cloudtjenester`, `weekendvagt`, `jobfunktion`, `computerudstyr`.
2. **Group compounds:** a multiword first element takes a boundary hyphen: `Conditional Access politikken` → `Conditional Access-politikken`; `Zero Trust arkitekturen` → `Zero Trust-arkitekturen`; `Microsoft 365-opsætning`.
3. **Initial abbreviations:** an abbreviation normally takes a hyphen in a compound: `AI-selskab`. A pronounceable abbreviation written in lowercase or with only an initial capital may optionally omit it: `aids-patient`/`aidspatient`, `Nato-land`/`Natoland`. All capitals keep the hyphen: `NATO-land`.
4. **One-word names and products:** an English proper name or product name does not require a hyphen merely because it is English. Ordinary compounding follows pronunciation; a clarity hyphen is optional when the join is hard to read. `Windows-enheder` and `Intune-policyen` use that clarity option.
5. **Inflected abbreviations:** abbreviations written without a full stop normally take an apostrophe before the ending: `SMV'er`, `API'er`, `KPI'erne`, `cd'en`. Ordinary loans do not: `policyen`, `policyer`, never `policy'en`.

Danish trade press writes `tredjepartsopdatering`, `krypteringsnøgle`, `Windows-enheder`, `AI-selskab`, `backupløsning`.

### D8. Typografi og talformat

MT Danish keeps English conventions. These are mechanical and the model gets them wrong constantly.

| Element | Forkert | Rigtigt |
| --- | --- | --- |
| Tankestreg | `15. maj—og derefter` | `15. maj – og derefter` (halvlang streg, mellemrum om) |
| Decimaltal | `1.1 mia.`, `9.8` | `1,1 mia.`, `9,8` |
| Tusindtal | `1,000,000` | `1.000.000` |
| Dato i brødtekst | `May 15` | `15. maj`. Numeric `15/5/2026` is also correct Danish; `15. maj 2026` is often clearer in running text. For ambiguous dates such as `03/04/2026`, preserve the form and ask which source locale applies. |
| Store tal | `$100 billion` | `100 milliarder $`. Engelsk *billion* = dansk *milliard*. Bevar valutabetegnelsen. |
| Valuta i brødtekst | `DKK 100`; `$5` | `100 DKK`; `5 $` eller `5 dollar`. Brug kun `kr.` når konteksten allerede fastslår danske kroner. I tabeller kan valutaen stå foran beløbet. |
| Procent | `20 %` og senere `30%` i samme tekst | `20 %` og `30 %`, eller `20%` og `30%`. Mellemrum er Dansk Sprognævns anbefaling; formen uden er også udbredt. Vælg én form og hold den. |
| Procent i sammensætninger | `20 %-rabat`, `43 %-tallet` | `20-%-rabat`, `43-%-tallet` |
| Klokkeslæt | `3:00 PM` | `kl. 15` eller `kl. 15.00` |
| Forkortelser | `e.g.`, `i.e.` | `fx`, `dvs.`. Både `etc.` og `osv.` er korrekte på dansk. |
| Komma ved ledsætninger | `Vi anbefaler, at I patcher når fejlen er rettet` (blandede systemer) | `Vi anbefaler, at I patcher, når fejlen er rettet` eller `Vi anbefaler at I patcher når fejlen er rettet`. Slutkomma sættes normalt i begge systemer; der findes snævre undtagelser. Startkomma ved almindelige ledsætninger er valgfrit, men selvstændige og parentetiske ledsætninger har fast komma. Vælg ét system og hold det. |
| Ugedage og måneder | `Mandag`, `Maj` | `mandag`, `maj` (småt på dansk) |
| Nationalitetsadjektiver | `Dansk lovgivning` | `dansk lovgivning` (`Danmark` stort, `dansk` småt) |
| Overskrifter | `Strategiske Partnerskaber Og Vækst` | `Strategiske partnerskaber og vækst` |
| Anførselstegn i ubeskyttet prosa | blanding af `"..."`, `“...”` og `»...«` | Alle tre former kan bruges. Vælg én og hold den. Do not normalize attributed quotes, mandated wording, code or paste-ready strings. |

### D9. Kildeangivelse og citatverber

AI writes `Ifølge kilder` and `Eksperter påpeger, at`. Danish trade writing credits short and concrete when the source is available: `Det skriver Ars Technica`, `lyder det fra Microsoft`, `fremgår af en rapport fra Rigsrevisionen`, `oplyser leverandøren`. Preserve who makes the claim and how the source presents it. `skriver`, `lyder`, `fremgår`, `oplyser` and `vurderer` are not stylistic synonyms; vary only when the source supports the new evidential relation. Repetition is safer than reassignment.

If a SKRIV brief supplies an unsourced claim, keep it and mark `[kilde?]` when publication needs a citation. If the brief asks for evidence but supplies no claim, use a placeholder instead of inventing one. In source-bound SKRIV and REDIGER, source claims may not be dropped because a citation is missing.

**Før:**
> Eksperter påpeger, at sårbarheden er kritisk. Det understreges desuden, at opdatering bør prioriteres.

**Efter, når du kun har kildeteksten:**
> Eksperter påpeger, at sårbarheden er kritisk. `[Hvilke eksperter?]` Det understreges desuden, at opdatering bør prioriteres.

The claim, vague claimant, reporting verb, modality and agentless recommendation all stayed. The placeholder exposes the missing source without turning the prose voice into the claimant.

**Efter, når du faktisk har kilden foran dig:**
> Supplerende kilde: *Microsoft klassificerer i sin sikkerhedsbulletin fra 14. januar sårbarheden som kritisk og angiver CVSS 9,8.*
>
> Eksperter påpeger, at sårbarheden er kritisk. `[Hvilke eksperter?]` Microsoft klassificerer i sin sikkerhedsbulletin fra 14. januar sårbarheden som kritisk og angiver CVSS 9,8. Det understreges desuden, at opdatering bør prioriteres.

The original claim, claimant, reporting verb and recommendation remain. The supplementary source visibly supplies the separate Microsoft claim, `klassificerer`, `CVSS 9,8`, `sikkerhedsbulletin` and `14. januar`. Without that displayed input, the added source sentence would be fabrication.

## Dansk ordliste under mistanke

Candidates, not automatic replacements. They trip the ear. The table below covers *categories*; this list covers specific Danish phrases. In REDIGER, neither deletion nor substitution is allowed when it removes or changes source meaning. Preserve tone and stance unless the user explicitly asks to change them.

- `Det er værd at bemærke, at ...`
- `Derudover` / `Ydermere` opening consecutive sentences
- `I takt med at ...`
- `spiller en central / afgørende / vigtig rolle`
- `i en verden hvor ...` / `i nutidens samfund` / `i den moderne digitale verden`
- Nominalstil: `foretage en vurdering af` → `vurdere` only when no process meaning changes; `gennemføre en implementering af` → `implementere` only when completion aspect remains unchanged
- `er designet til at`: it expresses purpose, not capability. In REDIGER, leave it unchanged unless an exact purpose construction preserves the same actor, object and aspect.
- `giver mulighed for at`: in REDIGER, leave this construction unchanged. In brief-based SKRIV, prefer a direct capability only when the brief explicitly supplies it.
- `sikre at` three or more times per page
- `en række`: preserve it in REDIGER unless context proves an exact equivalent. Write a number only when the source states it.
- `robust`, `omfattende`, `problemfri` (calques of robust/comprehensive/seamless)
- `Bemærk venligst at`: preserve it in source-bound modes because `venligst` carries politeness stance. In brief-based SKRIV, prefer `Bemærk:` when that tone fits the brief.
- `fremadrettet` as sentence filler
- Passive cascades: in brief-based SKRIV, prefer a sender and actor only when the brief names them. In source-bound modes, activate only when the source names every role: `Vi anbefaler, at opdateringen implementeres af jer` may become `Vi anbefaler, at I implementerer opdateringen`. Otherwise preserve the passive.

## Universelle AI-mønstre, i dansk form

The structural patterns transfer from English. These are the ones whose Danish surface form differs enough to need naming.

**Read the fix column as brief-based SKRIV defaults.** In source-bound SKRIV and REDIGER, the hard rule is the entire Fix column: preserve every source proposition, relationship and protected string; do not apply a row's brief-based rewrite unless its cell explicitly says it is safe in source-bound modes. Where a fix asks for a concrete fact or named source, use it only when the input supplies it; otherwise preserve the source and bracket the gap.

| Mønster | Sådan ser det ud på dansk | Fix |
| --- | --- | --- |
| Betydningsoppustning | `markerer et vendepunkt i`, `vidner om`, `sætter scenen for` | Omit unsupported significance. |
| `-ende`-analyser | `..., hvilket understreger virksomhedens engagement` | Omit unsupported analysis. Use a concrete fact only when input supplies it. |
| Reklamesprog | `banebrydende`, `innovativ`, `unik`, `i hjertet af`, `smukt beliggende` | Prefer a supported concrete detail. |
| Vag autoritet | `Eksperter vurderer`, `Ifølge flere kilder` | Name a supplied source or use a placeholder. See D9. |
| Treklang | tre parallelle led every time | Vary list structure without dropping supplied items. |
| Negativ parallelisme | `Det handler ikke om X, men om Y` | State Y directly when X is not part of the brief. |
| Halehæng-negation | `Valgmulighederne kommer fra elementet, ingen gætteri.` | Make negation grammatical without inserting a subject, actor or modality absent from input. If that cannot be done safely, preserve wording and flag it. |
| Falske spænd | `fra strategi til eksekvering, fra idé til virkelighed` | Mention only endpoints supplied by input. |
| Synonymkarrusel | virksomheden / selskabet / koncernen / firmaet i fire sætninger i træk | Reuse one word when all terms have the same referent and legal scope. |
| Copula-flugt | `fungerer som`, `udgør`, `står som` i stedet for `er` | Use `er` or `har` only when identity, function and possession are equivalent. |
| Hedging-stak | `kan potentielt muligvis bidrage til` | Remove only a genuinely synonymous stacked hedge. If each word changes probability, possibility or scope, keep it. Never remove the last qualification. |
| Fyldfraser | `med henblik på at`, `i forbindelse med`, `på nuværende tidspunkt` | Shorten only when purpose, relation and time remain unchanged; these phrases are not always synonyms for `for at`, `ved`, `nu`. |
| Signposting | `Lad os dykke ned i`, `Her er hvad du skal vide` | Omit it. |
| Fed skrift i stribevis | `**Fordel:** ... **Ulempe:** ...` | Change formatting without deleting labels or changing which text each label governs. |
| Emoji i overskrifter | `🚀 **Lancering**` | Omit the emoji; preserve adjacent wording. |
| Servil tone | `Godt spørgsmål!`, `Selvfølgelig!`, `Håber det hjælper!` | Omit unsupported service phrases. |
| Videnscutoff-forbehold | `Selvom detaljerne er begrænsede ...` | Do not add it to cover missing information. |
| Generisk positiv slutning | `Fremtiden ser lys ud.` | Omit it unless the brief supports it. |
| Overskrift-ekko | overskrift, derefter én linje der gentager overskriften | Avoid writing the echo. |

## Caveat: do not over-correct Danish fagsprog

Legitimate fagsprog in M365, security and infrastructure is naturally precise, predictable and low-perplexity. It can look flat to a detector and to the lists above. Before flagging:

- A correct technical term is not a tell. `Conditional Access-politikken håndhæver MFA` is accurate, not robotic.
- English technical vocabulary kept verbatim is correct Danish IT practice, not a D1 calque. `Vi ruller en Intune-policy ud` is fine. `Vi ruller en politik om enhedsovervågning ud`, written to avoid the English, is what reads wrong.
- The tells above are about register and rhythm, not terminology. Fix the flatness, keep the precision.
- In vendor-statement summaries, repeating `Microsoft oplyser, at ...` several times is correct practice, not an AI tell.

## Voice matching

If the user supplies a sample of their own Danish writing, read it first. In brief-based SKRIV, match sentence length, register, tiltaleform and punctuation habits. Reuse a recurring phrase only when the brief independently supports every claim, actor, modality and commitment in it; otherwise copy its structural pattern, not its content. In source-bound modes, borrow a pattern only when source meaning, stance and protected wording remain unchanged. Without a sample, use the varied default voice only in brief-based SKRIV.

## Process

Both modes end the same way. The self-audit is not optional; the first draft always keeps tells you cannot see while generating.

1. **Draft.** Write the best version you can. Do not hold back a known problem so the audit has something to find. If you notice a tell while drafting, fix it while drafting.
2. **Self-audit.** Ask yourself in Danish: *"Hvad afslører stadig, at det her er AI-skrevet?"* Run every check and fix every defect. Record zero to four findings for possible delivery; this cap applies only to surfaced notes, never to the internal audit. If none remain, do not invent a bullet.
   - **Unsupported additions.** Trace every noun phrase, number, name, date, cause, object, action and commitment to the input.
   - **Meaning preservation.** Compare every claim, attribution, modality, tense, aspect, agent, addressee, obligation, permission, commitment, quantifier, negation, stance and protected string with the input.
   - **Source-bound translation.** Confirm that every source proposition survived unless the user requested an omission.
   - **Language.** Check rhythm, idioms, word order, terminology, typography and numbers. In source-bound modes, do not insert a modal particle solely to meet a style target.
3. **Final.** Revise against your own audit.

## Output format

Default by length, not by mode. Danish phrasings like `ret lige den her` and `pudse lige` signal informality, not a request for commentary, so length decides.

| Situation | Deliver |
| --- | --- |
| Under roughly 200 words | Final text, placeholder list, any authorized deletion list, plus at most three other change bullets |
| Over roughly 200 words | Final text, any actual audit findings, placeholder list and any authorized deletion list |
| User says `kun teksten`, `bare giv mig den`, `no commentary` | Final text only. Keep unresolved placeholders visible inline; do not add separate lists. |

Generate the draft and run the complete audit internally. Do not expose a draft that you already know contains unsupported or altered meaning. When the table asks for audit findings, surface only concise findings that actually remain relevant to the user. Always surface bracketed placeholders, in every format, including the short one. A placeholder the user does not see is the same failure as an invented number.
