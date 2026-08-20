# Registers, intake, pre-flight, kanal

Load this when composing new Danish from a brief (SKRIV mode), or when REDIGER requires choosing or confirming a register row.

## Intake

Ask before writing, not after. These three answers change every sentence; guessing them is the most common reason a first draft has to be thrown away. Ask them in brief-based SKRIV for what the brief does not answer. In source-bound rendering, ask one short clarification only when an ambiguity prevents faithful preservation. A brief that says "kundemail til Morten om at leveringen er forsinket, ny dato 14. marts" has answered all three: én person, kundemail, informér.

Present as a multiple-choice list. If the host application has an interactive question tool, use it. Otherwise number in chat and wait for one reply.

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

## Pre-flight

Settle before first sentence in brief-based SKRIV. Intake answers 1 and 2 cover pre-flight 1 and 2; answer 3 informs pre-flight 4. Pre-flight 3 comes only from an explicitly named sender in the brief. In source-bound SKRIV, derive audience, register, sender, stance and commitments from the source instead of applying these defaults.

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

3. **Afsender.** An explicit brief always wins. Use `vi` only when brief identifies the writing organization as claimant; use `jeg` only when it identifies an individual. Otherwise stay impersonal or use `[afsender]`. Never invent `vi`, `jeg` or an addressee to activate a passive.
4. **Point first.** Say the thing in first or second sentence. Do not warm up for three sentences of context.
5. **Rhythm.** Vary sentence length on purpose, and let some sentences be very short. Do not apply a quota: long-long-short in every paragraph is itself uniform, which is the tell you are trying to kill. Diagnostic: if you can predict the shape of the next sentence from the last three, rewrite.
6. **Modalpartikler.** Use only when they express a stance the brief supports. Diagnostic, not quota: short text may need none, and overdosing sounds like a transcript. See `danish-tells.md` D6.
7. **Konkrete tal og navne slår adjektiver, når du har dem.** `fire regioner` beats `en række regioner`. `9,8 i CVSS` beats `kritisk`, if someone gave you the 9,8. If brief gave no number, write `[antal]`, not a number you made up. See the hard rule in SKILL.md.

## Kanal

Only constraints that actually change the copy.

These are brief-based SKRIV defaults only. In source-bound modes, a channel name does not authorize reordering qualifiers, removing greetings or asks, changing statements into imperatives, or changing scope, obligation, addressee, modality or stance.

- **LinkedIn:** point in first sentence. Short paragraphs. Up to three hashtags at the end, or none.
- **Kundemail:** subject line carries the point. No greeting theatre. Prefer one ask at the end unless brief explicitly requires more.
- **UI-tekst:** imperative in action buttons: `Gem`, not `Gemme` or `Gem dine ændringer nu`. Infinitive fits navigation labels only when the product's established pattern uses it.
- **Rapport:** see the `danish-report-writer` skill for structure. This skill is the language pass.

## SKRIV example

Brief: *"LinkedIn-opslag om at vi lancerer en backup-løsning til mindre virksomheder. Max 150 ord."*

Intake: brief says LinkedIn, so question 2 is answered. `Til mindre virksomheder` describes the market, not necessarily the addressee, so questions 1 and 3 remain open. Answers here: `en virksomhed eller et team` and `bed læseren om at gøre noget`.

Pre-flight: register marketing/social, afsender `vi`, no product name, scope or requested action in brief, so those facts stay bracketed.

**Endelig version:**
> Vi lancerer [produktnavn]: backup til mindre virksomheder. [Hvad dækker den?]
>
> [Hvad skal læseren gøre?]

Mangler før publicering: `[produktnavn]`, `[Hvad dækker den?]` og `[Hvad skal læseren gøre?]`.

That post is well under the 150-word budget, and it is thin. The brief plus intake answers support the launch, product category, audience and purpose; everything else remains visible as a gap. At this length, deliver only that final version and its three-item placeholder list.
