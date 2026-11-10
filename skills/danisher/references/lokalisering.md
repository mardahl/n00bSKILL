# LOKALISÉR: da-DK locale mode

Load this file from `SKILL.md` when it routes here. Everything in `SKILL.md` still applies, including the hard rule. This file adds one thing: **permission to adapt locale-bound content for a reader in Denmark, on the condition that every adaptation is reported.**

Target locale is always `da-DK`. Not Greenland, the Faroe Islands or Sydslesvig.

## Why this mode exists

Models write Danish on top of American defaults: dollars, `11/28`, EST, Thanksgiving, ZIP codes, HIPAA, "all 50 states", "reach out", "thrilled to announce". Translating those faithfully gives correct Danish words in an American world. A Danish reader notices in the first line.

The fix is not better translation. It is asking, for every locale-bound element: *what would a Danish writer, writing for a Danish reader, have put here?* Then do that, or flag why you could not.

## When this mode is active

- The user asks for it: `lokalisér`, `tilpas til det danske marked`, `gør den dansk`, `transcreate`, `til danske kunder`.
- Any SKRIV, source-bound SKRIV or REDIGER input contains a locale marker from the scan below. In that case run this mode for the marked elements only; the rest of the text follows its original mode.
- Your own SKRIV draft contains one. Models introduce American defaults unprompted, so scan your draft too.

## Locale scan

Look for these before writing. Each hit is an element to convert, adapt, flag or remove.

| Category | Markers |
| --- | --- |
| Format | `$`, `USD`, `11/28`, `2 PM`, `EST`/`PST`/`ET`, `(555) 123-4567`, `1,000.50`, `°F`, miles, feet, pounds, inches, gallons, Letter size |
| Institutions and law | SSN, ZIP code, state/states, county, IRS, 401(k), Medicare, HIPAA, CCPA, ADA, FedRAMP, COPPA, CAN-SPAM, FDA, "federal" |
| Calendar | Thanksgiving, Labor Day, Memorial Day, Fourth of July, Super Bowl, Presidents' Day, "back to school" in late August as a US season, fiscal year that is not the calendar year, "spring break" |
| Commerce | price without moms, "free shipping" US-wide, "call toll-free", "500 stores nationwide", comparative claims (`50% faster than the competition`), discount announcements |
| Pragmatics | `thrilled/excited to announce`, `game-changer`, `world-class`, `best-in-class`, `hits it out of the park`, `touch base`, `circle back`, `reach out`, `Dear valued customer`, `Don't miss out!`, stacked exclamation marks, sports metaphors |

## Four actions

Every hit gets exactly one action. Every action except a pure format conversion goes on the Lokaliseringer list.

| Action | When | Example |
| --- | --- | --- |
| **Konvertér** | The value is preserved; only notation changes, or a deterministic conversion with no outside data | `11/28` → `28. november`; `2 PM` → `kl. 14`; `68 °F` → `20 °C`; `5 miles` → `ca. 8 km`; `EST` midnight → `kl. 06.00 dansk tid` |
| **Tilpas** | A genuine Danish equivalent exists and the substitution does not change a factual claim | `ZIP code` → `postnummer`; `SSN` → `CPR-nummer`; `reach out` → `skriv til os`; `Happy holidays` → `god jul` when the text is clearly about December |
| **Markér** | Adapting would need a fact you do not have, or would change a factual, legal or commercial claim | `$49` → `49 $ [pris i kr.?]`; `HIPAA compliant` → keep verbatim and flag; `rolling out to all 50 states` → `[udrulles i Danmark? hvornår?]` |
| **Fjern** | The reference only makes sense to an American reader and carries no claim the Danish reader needs | `Happy Thanksgiving from the team!` → removed |

**Fjern only decoration.** If a foreign reference carries a claim, such as the reason for a closure (`lukket pga. Thanksgiving`), a date or a scope, keep it. You may add a short gloss a Danish reader needs, `den amerikanske helligdag Thanksgiving`, and list it as Tilpas.

Format conversions alone (`typography.md`) need no list entry. Time zone and unit conversions do, because the reader may need to check them.

## What adaptation may never do

The hard rule still governs. Locale permission covers notation, equivalents and pragmatics. It does not cover facts.

- **No invented exchange rates.** `$49` never becomes `ca. 340 kr.` unless the user supplied the rate or the DKK price. Keep `49 $` (or `49 dollar`) and add `[pris i kr.?]`.
- **No substituted compliance.** `HIPAA compliant` does not become `GDPR-compliant`, `overholder gældende databeskyttelsesregler` or anything else. Compliance and certification are factual claims about the product. Keep the original term and flag that it is a US standard. International standards Danes already use, such as `ISO 27001` and `SOC 2`, stay as they are without a flag.
- **No invented Danish availability.** A US rollout, store count, US phone line or US support hours says nothing about Denmark. Do not write `i hele Danmark`, a Danish phone number or Danish opening hours. Flag the gap.
- **No widened or narrowed scope.** `all 50 states` does not become `hele landet`. Removing it silently is also wrong; it is a scope claim, so flag it.
- **No silent equivalence.** `401(k)` → `pensionsordning` is an approximation. Use it only with a flag that says so.
- **No invented deadlines.** When converting time zones, convert the stated moment. If the source moment is ambiguous (`midnight Friday` can mean the start or end of Friday), pick the common reading, convert it, and flag the ambiguity.

## da-DK conventions beyond `typography.md`

| Element | da-DK |
| --- | --- |
| Tidszone | `dansk tid`. CET (UTC+1) in winter, CEST (UTC+2) in summer. US and EU change clocks on different dates in March and October/November; check before converting. |
| Frister | `til og med fredag` or `senest fredag kl. 23.59`. Bare `indtil fredag` is ambiguous in Danish. After a time zone conversion, state only the Danish moment: `Tilbuddet slutter lørdag den 29. november kl. 06.00 dansk tid.` Never put the source's day next to the converted one (`til og med fredag, det vil sige til lørdag`); the reader sees two deadlines. The original goes on the Lokaliseringer list. |
| Ugenumre | Danes plan in weeks: `uge 7`, `i uge 42`. Use when the source gives a week; do not invent one. Common periods: vinterferie uge 7 or 8, efterårsferie uge 42, industriferie/sommerferie omkring uge 28-30. |
| Telefon | `+45 12 34 56 78` or `12 34 56 78`. A foreign number keeps its country code: `+1 555 123 4567`. |
| Adresse | `Vesterbrogade 1, 1620 København V`. Street, then number; postnummer before by; no state. |
| Priser | B2C prices to Danish consumers are shown `inkl. moms`. B2B commonly states `ekskl. moms`. If the source does not say, flag `[inkl. eller ekskl. moms?]`. |
| Rabat | Danish rules require a før-pris in a discount to be the lowest price in the preceding 30 days. When a discount appears, flag `[tjek førpris]`; do not give legal advice. |
| Sammenlignende reklame | `50 % hurtigere end konkurrenterne` needs documentation under markedsføringsloven. Keep the claim and flag `[dokumentation?]`. |
| Enheder | Metric only. `A4`, not Letter. Round converted figures sensibly and mark them `ca.` |
| Regnskabsår | Many Danish companies use the calendar year. Keep `Q4` or `4. kvartal`; flag if the source's fiscal Q4 is not October–December. |
| Helligdage | Store Bededag is no longer a public holiday (from 2024). Grundlovsdag 5. juni is also Fars dag. Thanksgiving, Labor Day, Memorial Day and Fourth of July are not Danish. Black Friday and Cyber Monday are used in Denmark. Halloween is used, mostly for children. |
| Låneords køn | Follow Danish trade press: `en tenant`, `en server`, `en app`, `en licens`, `et dashboard`, `et API`, `et webinar` (`webinaret`, not `webinaren`). Not `et tenant`. |

## Pragmatics: the American register

A Danish reader distrusts enthusiasm that has not been earned. That is the largest locale gap and the one machine translation never closes, because every word is correctly translated.

| American default | Danish default |
| --- | --- |
| `We're thrilled to announce` | `Nu lancerer vi`, `Fra i dag kan du`, or just state the news |
| `game-changing`, `revolutionary`, `best-in-class` | Remove the adjective and keep the supplied fact. If no fact was supplied, the sentence may be empty; that is a REDIGER problem, not a reason to invent one. |
| `Reach out`, `touch base` | `Skriv til os`, `ring til os`, `kontakt [navn]` |
| `Don't miss out! Act now!` | `Tilbuddet gælder til og med [dato].` |
| `Dear valued customer` | `Hej [navn]` or `Kære [navn]`; no greeting in a notice |
| `Hi John!` | `Hej John` (no exclamation mark) |
| `Best regards, The Team` | `Venlig hilsen` / `Med venlig hilsen` + a named person when supplied |
| Sports metaphors (`hits it out of the park`, `slam dunk`, `MVP`) | Drop the metaphor and keep its claim. Do not replace it with a Danish football metaphor. |
| Three exclamation marks per post | Zero or one |

Changing register this way is a Tilpas action. List it once as a group (`Amerikansk salgstone dæmpet: ...`), not phrase by phrase, unless a change touched a claim.

## Writing new copy: think from Danish exemplars

When writing from a brief, do not draft in English in your head and then render it. Name the genre to yourself in Danish, as a Danish writer would, and write the text that genre would contain. The Danish genre name pulls the model toward Danish text; an English label pulls it toward English text.

| Genre (tænk i dette navn) | Kendetegn |
| --- | --- |
| `en nyhed i et dansk IT-fagmedie` | Rubrik with the news, not a teaser. Fact first, quote second. Dry, no exclamation marks. English technical terms kept. |
| `en dansk kundemail fra en bank eller et forsyningsselskab` | Emnelinjen carries the point. `Hej [navn]`. Short paragraphs. One ask. `Venlig hilsen` + name. |
| `en vejledning fra en dansk myndighed eller kommune` | Plain language, upersonlig or `du`. Exact dates, no tone. Steps in order. |
| `et LinkedIn-opslag fra en dansk konsulent` | First person, low-key, one observation, no hype words, at most one exclamation mark. |
| `et dansk nyhedsbrev fra en IT-partner` | `I/jer`, practical, what changes for the reader, a link to read more. |

These are genre descriptions, not imitation targets. Do not imitate a named publication or company, and do not borrow facts, phrases or claims from any real text.

Then run the locale scan on your draft. American defaults surface even when you are writing in Danish from the start.

## Output

Deliver, in this order:

1. The final text.
2. **Lokaliseringer:** one line per Tilpas, Markér and Fjern action, plus time zone and unit conversions. Say what changed and why: `Thanksgiving-hilsen fjernet: fejres ikke i Danmark.`
3. The placeholder list, as in `SKILL.md`.

The Lokaliseringer list is mandatory in every output format. If the user asks for `kun teksten`, compress it to one line after the text, for example `Lokaliseret: dollarpris bevaret, EST omregnet til dansk tid, Thanksgiving fjernet.` The user has to be able to see every adaptation, the same way they must see every placeholder.

## Example

**Brief:** *"Danish customer email: Black Friday sale, 30% off all plans, starting at $49/month. Sale ends Friday 11/28 at midnight EST. No Social Security Number needed at checkout, just your ZIP code. Happy Thanksgiving from the whole team! Questions? Call (555) 123-4567."*

**Endelig version:**
> **Emne:** Black Friday: 30 % rabat på alle abonnementer
>
> Hej [navn]
>
> Til Black Friday giver vi 30 % rabat på alle abonnementer. Priserne starter ved 49 $ om måneden [pris i kr.?] [inkl. eller ekskl. moms?].
>
> Tilbuddet slutter lørdag den 29. november kl. 06.00 dansk tid.
>
> Du skal ikke oplyse dit CPR-nummer, når du tilmelder dig. Du skal kun bruge dit postnummer.
>
> Har du spørgsmål, kan du ringe til os på +1 555 123 4567.
>
> Venlig hilsen
> Hele teamet

**Lokaliseringer:**
- Midnat EST omregnet til lørdag kl. 06.00 dansk tid. `Midnight Friday` er læst som slutningen af fredag; bekræft.
- `Social Security Number` → `CPR-nummer` og `ZIP code` → `postnummer` (danske pendanter).
- Thanksgiving-hilsen fjernet: fejres ikke i Danmark.
- Dollarpris bevaret. Ingen kurs eller dansk pris i briefet.
- Telefonnummeret er amerikansk; danske kunder ringer til udlandet.
- Rabatten skal overholde førprisreglen [tjek førpris].

**Mangler:** `[navn]`, `[pris i kr.?]`, `[inkl. eller ekskl. moms?]`, og om der findes et dansk telefonnummer.

Not done, on purpose: no `ca. 340 kr.`, no invented Danish phone number, no claim that the offer applies in Denmark beyond what the brief says.
