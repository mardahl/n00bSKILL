---
name: humanizer-danish-addendum
description: Use when humanizing, editing, or reviewing Danish text for AI-generated writing tells, especially English idiom calques, translated syntax, Danish business filler, flat earnest tone, or Danish IT fagsprog that should not be over-corrected.
license: MIT
compatibility: claude-code opencode
---

# Humanizer Danish Addendum

## Overview

This is a bolt-on skill for the `humanizer` skill. Use the parent `humanizer` skill for structural AI patterns first, then apply this addendum for Danish-specific tells that English word lists miss.

Core principle: Danish AI writing often sounds like English translated underneath. Fix the translated register and rhythm without damaging legitimate Danish technical language.

## How to Use

When a user asks to humanize Danish text:

1. Load and apply `humanizer` if it is available.
2. Apply this skill as the Danish pass.
3. Treat every item below as a judgment aid, not a detector score.
4. Preserve correct Danish IT terms and English technical vocabulary where Danish practice normally keeps them.

## D1. Calqued English Idioms

**The single most reliable Danish tell:** the text translates an English saying word-for-word into Danish, producing a phrase no Dane would naturally write.

Native Danish usually does one of three things with English idioms:

- Uses a real Danish equivalent.
- Keeps the English verbatim, often in quotes.
- Semi-ingests the English: English spelling kept, read as Danish.

**Before:**
> Det er en "sæt op og glem"-løsning.

**After:**
> Det er en vedligeholdelsesfri løsning.
> Det er en "set and forget"-løsning.
> Den er set-and-forget.

**Watch for:** "ved slutningen af dagen" for "at the end of the day", "på samme side" for "on the same page", "tænke uden for boksen", "lavthængende frugter", and "i lang løb" or other literal versions of "in the long run".

## D2. Over-Explanation and Example-Stacking

AI often hammers one obvious point with three near-identical illustrations. Danish business writing usually trusts the reader and stops once the point lands.

**Watch for:** chains like "..., nogen der er ..., og ikke mindst ..." or three parallel clauses making one simple point.

**Before:**
> En tyv er en person der stjæler, nogen der er uærlig, og ikke mindst en forræder mod fællesskabet.

**After:**
> En tyv stjæler. Det undergraver tilliden i fællesskabet.

## D3. Anglicisme and English Syntax Bleed-Through

Danish LLM output often keeps English sentence rhythm after translation. The result may be grammatical but still feel `oversat`.

**Signs:**

- Heavy front-loaded subordinate clauses where Danish V2 word order would sound more natural.
- Consecutive sentence openings with "Derudover", "Ydermere", or "I takt med at".
- Imported negative parallelism: "Det handler ikke om X, men om Y".
- Filler connectors: "med det sagt" and "når det er sagt".

**Before:**
> Ved at implementere denne løsning, og ved at sikre at alle processer er optimerede, kan organisationen opnå betydelige fordele.

**After:**
> Med den her løsning får I styr på processerne, og det kan mærkes på bundlinjen.

## D4. Flat Earnestness

ChatGPT tends to remove Danish understatement, dry humor, and mild irony. It replaces them with sincere, over-positive corporate enthusiasm.

Real Danish business writing, even formal writing, often has dry understatement: "det er jo ikke verdens undergang" or "det kan godt være, vi skal kigge en ekstra gang".

**Before:**
> Vi er utroligt begejstrede for at præsentere denne banebrydende og innovative løsning, der vil transformere jeres arbejdsgange.

**After:**
> Her er løsningen. Den fjerner det manuelle bøvl, I har klaget over, og ja, den virker.

## D5. Low Burstiness and Empty Scene-Setting

Watch for equal-length declarative sentences padded with Danish scene-setting phrases.

**Watch for:** "i den moderne digitale verden", "i nutidens samfund", and "i en verden hvor X".

**Before:**
> AI-detektorer er vigtige værktøjer i den moderne digitale verden. De hjælper med at identificere maskinskrevet indhold. Mange organisationer bruger dem. Teknologien udvikler sig konstant.

**After:**
> AI-detektorer? De dukker op overalt nu. Skoler bruger dem, medier bruger dem, men ærligt talt rammer de ved siden af halvdelen af tiden. Især på dansk.

## Danish Lexical Watch-List

Treat these as candidates, not rules:

- "Det er værd at bemærke, at ..."
- "Derudover" or "Ydermere" opening consecutive sentences
- "I takt med at ..."
- "spiller en central / afgørende / vigtig rolle"
- "i en verden hvor ..."
- "i nutidens samfund"
- "i den moderne digitale verden"
- "Lad os dykke ned i ..."
- Stiff nominalstil: "foretage en vurdering af" instead of "vurdere"
- Stiff nominalstil: "gennemføre en implementering af" instead of "implementere"

Dropped on native review: "når alt kommer til alt" is not common enough in real Danish to be a useful tell.

## Caveat: Do Not Over-Correct Technical Danish

Legitimate fagsprog in M365, security, infrastructure, and software work is naturally precise, predictable, and low-perplexity. It can look flat without being AI-generated.

Before flagging technical Danish:

- A correct technical term is not a tell. `Conditional Access-politikken håndhæver MFA` is accurate, not robotic.
- English technical vocabulary kept verbatim is normal Danish IT practice, not D1 calquing.
- `Vi ruller en Intune-policy ud` is fine.
- `Vi ruller en politik om enhedsovervågning ud` reads worse if it is trying to avoid normal English terminology.
- The Danish tells are about register and rhythm, not terminology. Fix the flatness, keep the precision.

## Output Expectations

When rewriting Danish text, provide:

1. A revised Danish version.
2. A brief note naming the Danish-specific tells removed.
3. A caveat if technical terminology was intentionally preserved.
