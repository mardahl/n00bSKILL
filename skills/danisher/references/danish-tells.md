# Danish-specific tells

Load when auditing or editing Danish text, or when a scanner check in SKILL.md needs a worked example. These are the ones English word lists cannot see.

Every `Efter` below is derivable from its own visible `Før`: no new content and no change to attribution, modality, tense, aspect, agent, negation or quantifier scope. If extra source material is needed, the example displays it.

## D1. Calqued English idioms

The flagship Danish tell. The model translates an English saying word for word and produces a phrase no Dane would write.

A native writer has two legitimate moves with an English saying: use a real Danish equivalent, or keep the English verbatim. Danish also *semi-ingests* English, keeping the English spelling but reading it as Danish. The clumsy literal translation is the giveaway that a machine sat in between.

**Opgave:** *Erstat den bogstavelige vending. Den forklarende gentagelse må forkortes, hvis hele forklaringen bevares i den valgte formulering.*

**Før:**
> Det er en "sæt op og glem"-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb.

**Efter, tre gyldige muligheder:**
> Det er en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(dansk omskrivning)*
> Det er en "set and forget"-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(engelsk ækvivalent, i citationstegn)*
> Det er en set-and-forget-løsning, altså en løsning, som sættes op én gang og derefter ikke kræver løbende indgreb. *(indoptaget: engelsk stavning, læst som dansk)*

Watch for: `ved slutningen af dagen` (→ `i sidste ende` when that is the meaning), `på samme side` (→ `enige` only when source asserts agreement), `tænke uden for boksen` (keep English or rewrite without adding a claim), `tager skridtet` only when used as a literal calque rather than established Danish, `lavthængende frugter` (borderline: some Danes use it, many cringe), `med det sagt` / `når det er sagt` as filler when they carry no contrast.

## D2. Over-explanation and example stacking

AI often repeats the same point in three forms after it has already landed. In REDIGER, repetition, reformulation and summary all require authorization to shorten; examples that add a property or implication must stay.

**Opgave:** *Forkort teksten uden at miste dens påstand.*

**Før:**
> En tyv stjæler. Det vil sige, at en tyv stjæler. Kort sagt: En tyv stjæler.

**Efter:**
> En tyv stjæler.

Both removed sentences repeat `En tyv stjæler` without another property, actor or qualification. The example assumes the user requested a shorter version; without that authorization, preserve even reformulation and summary relationships.

## D3. English syntax bleeding through

Grammatically correct, but the sentences do not sit the way a Dane would build them.

Signs: grammatically valid but heavy fronting that buries the main point; over-explicit connectors (`Derudover,` `Ydermere,` `I takt med at`) opening sentence after sentence when Danish links more by juxtaposition; `Det handler ikke om X, men om Y` imported wholesale.

**Før:**
> Ved at implementere denne løsning, og ved at sikre at alle processer er optimerede, kan organisationen opnå betydelige fordele.

**Efter:**
> Organisationen kan opnå betydelige fordele ved at implementere denne løsning og ved at sikre, at alle processer er optimerede.

The original clause order already obeys V2; this edit changes information structure and corrects comma placement. The main clause moved to the front, the comma after the opening phrase disappeared, and a clause comma was added after `sikre`. `kan opnå`, `alle`, both `ved at`-phrases, stative `er optimerede` and agent `Organisationen` stayed.

## D4. Flat earnestness

AI copy often reads uniformly sincere and over-positive. Danish commercial and editorial writing can use dry understatement: `det er jo ikke verdens undergang`, `det kan godt være, vi skal kigge en ekstra gang`.

In brief-based SKRIV, dry understatement can suit marketing, kundemail, fagpresse and internal notes. Do not use it in myndighedstekst, legal text, safety instructions, incident notifications, driftsmeddelelser, planlagt nedetid, statusopdateringer, release notes or SLA-varsler. In source-bound modes, do not add dryness or remove enthusiasm unless the user requested that tone change. `Og ja, den kommer op igen` in a maintenance notice is a defect, not voice.

**Før:**
> Vi præsenterer en ny løsning, der vil ændre jeres arbejdsgange.

**Efter:**
> Vi præsenterer en ny løsning. Den vil ændre jeres arbejdsgange.

The edit only splits the relative clause while preserving indefinite `en`, `ny`, future `vil`, actor `vi` and object `jeres arbejdsgange`. Deadpan confirmation is primarily SKRIV advice. In REDIGER, add claims such as `den virker`, habitual `plejer`, sufficiency `nok` or reassurance only when the source states that exact meaning with the same modality.

## D5. Low burstiness and empty scene-setting

Equal-length declaratives padded with `i den moderne digitale verden`, `i nutidens samfund`, `i en verden hvor X`.

In brief-based SKRIV, omit empty scene-setting. In source-bound modes, even broad context can narrow a claim, so preserve it unless the user authorizes its removal.

**Før:**
> AI-detektorer er vigtige værktøjer. De hjælper med at identificere maskinskrevet indhold. Mange organisationer bruger dem. Teknologien udvikler sig konstant.

**Efter:**
> AI-detektorer er vigtige værktøjer. De hjælper med at identificere maskinskrevet indhold, og mange organisationer bruger dem. Teknologien udvikler sig konstant.

The second sentence boundary became a comma plus `og`, and `Mange` became lowercase. Nothing else changed. `hjælper med at identificere` did not become `finder`, and `indhold` did not become `tekst`; that would change the claim.

If this still reads a little flat, that is because the source contains four flat facts. Burstiness you cannot source is decoration. Get the real variation in SKRIV mode, where you control the sentences.

## D6. Manglende modalpartikler

Danish prose, including formal prose, uses modal particles such as `jo`, `da`, `vel`, `nok`, `dog` and `altså` to signal shared knowledge, reservation and stance. Focus adverbs such as `netop` and adverbial phrases such as `i øvrigt` are also meaning-bearing and need the same care in REDIGER.

**Før:**
> Det er da ikke gået ubemærket hen, at Danmark stadig arbejder med NIS2.

**Efter:**
> At Danmark stadig arbejder med NIS2, er da ikke gået ubemærket hen.

The existing `da` and `arbejder` both stayed. Rewriting `arbejder` to `bakser med` would assert a difficulty the source never claimed.

In brief-based SKRIV, use any such marker only when the brief explicitly supports that exact stance or focus; there is no quota. In source-bound modes, preserve existing markers and do not insert one merely to make prose sound Danish. They are not interchangeable.

## D7. Kompositum og bindestreg

Keep five rules separate:

1. **Ordinary compounds:** Danish compounds, including established one-word loans, are written as one word: `sikkerheds opdateringer` → `sikkerhedsopdateringer`; `backupløsning`, `mailserver`, `cloudtjenester`, `weekendvagt`, `jobfunktion`, `computerudstyr`.
2. **Group compounds:** a multiword first element takes a boundary hyphen: `Conditional Access politikken` → `Conditional Access-politikken`; `Zero Trust arkitekturen` → `Zero Trust-arkitekturen`; `Microsoft 365-opsætning`.
3. **Initial abbreviations:** an abbreviation normally takes a hyphen in a compound: `AI-selskab`. A pronounceable abbreviation written in lowercase or with only an initial capital may optionally omit it: `aids-patient`/`aidspatient`, `Nato-land`/`Natoland`. All capitals keep the hyphen: `NATO-land`.
4. **One-word names and products:** an English proper name or product name does not require a hyphen merely because it is English. Ordinary compounding follows pronunciation; a clarity hyphen is optional when the join is hard to read. `Windows-enheder` and `Intune-policyen` use that clarity option.
5. **Inflected abbreviations:** abbreviations written without a full stop normally take an apostrophe before the ending: `SMV'er`, `API'er`, `KPI'erne`, `cd'en`. Ordinary loans do not: `policyen`, `policyer`, never `policy'en`.

Danish trade press writes `tredjepartsopdatering`, `krypteringsnøgle`, `Windows-enheder`, `AI-selskab`, `backupløsning`.

## D8. Typografi og talformat

See `typography.md`.

## D9. Kildeangivelse og citatverber

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

## D10. Modality in contractual and invoice text

The Myndighed, jura, sikkerhed register row covers commercial contract and invoice wording, but that row's failure modes differ from notices and safety instructions. Here the scanner's modality check earns its keep.

**Opgave:** *Ret kommafejlene i klausulen. Ændr ikke andet.*

**Før:**
> Kunden kan opsige aftalen med 30 dages varsel, såfremt der ikke foreligger ubetalte fakturaer og beløbet kan refunderes hvis opsigelsen sker inden bindingsperiodens udløb.

**Efter:**
> Kunden kan opsige aftalen med 30 dages varsel, såfremt der ikke foreligger ubetalte fakturaer, og beløbet kan refunderes, hvis opsigelsen sker inden bindingsperiodens udløb.

Only two commas were added: one before `og` to close the `såfremt`-clause, one before `hvis` to open the conditional. Nothing else changed.

**Defekt omskrivning:**
> Kunden kan opsige aftalen med 30 dages varsel, såfremt der ikke foreligger ubetalte fakturaer, og beløbet refunderes, hvis opsigelsen sker inden bindingsperiodens udløb.

`kan refunderes` → `refunderes` removes the modal. The source grants a possibility subject to conditions; the rewrite asserts an unconditional refund. In a contract this changes what the parties have agreed to. The scanner's modality check exists to catch exactly this edit.

## Dansk ordliste under mistanke

Candidates, not automatic replacements. They trip the ear. In REDIGER, neither deletion nor substitution is allowed when it removes or changes source meaning. Preserve tone and stance unless the user explicitly asks to change them.

- `Det er værd at bemærke, at ...`
- `Derudover` / `Ydermere` opening consecutive sentences
- `I takt med at ...`
- `spiller en central / afgørende / vigtig rolle`
- `i en verden hvor ...` / `i nutidens samfund` / `i den moderne digitale verden`
- Nominalstil: `foretage en vurdering af` → `vurdere` only when no process meaning changes; `gennemføre en implementering af` → `implementere` only when completion aspect remains unchanged
- `er designet til at`: expresses purpose, not capability. In REDIGER, leave unchanged unless an exact purpose construction preserves the same actor, object and aspect.
- `giver mulighed for at`: in REDIGER, leave unchanged. In brief-based SKRIV, prefer a direct capability only when the brief explicitly supplies it.
- `sikre at` three or more times per page
- `en række`: preserve in REDIGER unless context proves an exact equivalent. Write a number only when source states it.
- `robust`, `omfattende`, `problemfri` (calques of robust/comprehensive/seamless)
- `Bemærk venligst at`: preserve in source-bound modes because `venligst` carries politeness stance. In brief-based SKRIV, prefer `Bemærk:` when that tone fits the brief.
- `fremadrettet` as sentence filler
- Passive cascades: in brief-based SKRIV, prefer a sender and actor only when the brief names them. In source-bound modes, activate only when the source names every role: `Vi anbefaler, at opdateringen implementeres af jer` may become `Vi anbefaler, at I implementerer opdateringen`. Otherwise preserve the passive.

## Universelle AI-mønstre, i dansk form

The structural patterns transfer from English. These are the ones whose Danish surface form differs enough to need naming.

**Read the fix column as brief-based SKRIV defaults.** In source-bound SKRIV and REDIGER, the hard rule is the entire Fix column: preserve every source proposition, relationship and protected string; do not apply a row's brief-based rewrite unless its cell explicitly says it is safe in source-bound modes. Where a fix asks for a concrete fact or named source, use it only when input supplies it; otherwise preserve source and bracket the gap.

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
