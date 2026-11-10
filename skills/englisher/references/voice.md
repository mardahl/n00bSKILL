# Voice, register and composition

Load when composing new English from a brief, matching a writer's voice, or deciding how much personality a text should carry.

## Match the writer's voice

If the user provides a sample of their own writing, analyze it before rewriting:

1. Read the sample first. Note sentence length, word choice, paragraph openings, punctuation, repeated phrases, and transitions.
2. Match those habits. Do not replace casual words with formal ones or remove deliberate quirks.
3. If there is no sample, use the guidance below.

A writing sample takes priority over the style rules in `references/english-tells.md`. If the sample uses em dashes, keep them at about the same rate. If the sample opens sentences with "And" or fragments for rhythm, keep that too. The tells list describes what AI produces by default; a real writer's deliberate habits are not tells.

### Dimmer check

Models imitating a writer keep the writer's level of difficulty in relative terms but lower it in absolute terms: shorter sentences, fewer long words, more generic phrasing. Reusing the sample's openers and matching its total word count does not count as matching its voice. After drafting, compare the draft with the sample on two numbers:

- average words per sentence
- share of words with seven or more letters

If either is clearly lower in the draft (roughly under three-quarters of the sample's value), the draft has been flattened. Rebuild sentences the way the sample builds them, for example subordinate clauses, a qualification inside the sentence, a causal `because` chain. Fill them only with facts and stances the brief supplies. Never pad length with invented claims, reasons or observations; a shorter draft with bracketed gaps beats a long one with invented content. Invented content includes expert generalisations (`the biggest pitfall is usually…`, `most councils…`), advice or diagnoses the brief does not give, and scene details (`on the train home`). Writing them in the writer's voice does not make them supplied. When the brief has too few facts, build the long sentences from the facts you have plus bracketed gaps. The sample's sentence length overrides the register defaults below.

## Personality: when it fits

Removing AI patterns is only half the job. The result should still sound like a person.

| Text type | Personality |
| --- | --- |
| Blog posts, essays, opinions, personal writing | Yes, when it fits the writer |
| Reference, technical, legal, compliance, factual text | No — keep neutral |

When personality fits, keep the writer's opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm. Do not add opinions or first-person language where they do not belong. Never invent facts to make the text feel personal.

## Register and formality

Infer from genre and communicative situation, not merely from the deliverable's price or deadline:

- **Formal:** proposals, contracts, regulator-facing text, academic work. Full sentences, no contractions unless the house style allows them, no humor.
- **Professional-neutral:** customer emails, documentation, internal reports, status updates. Contractions fine, direct address fine, no slang.
- **Casual:** LinkedIn posts, personal blogs, community posts, chat-adjacent writing. Contractions, fragments, humor and asides all fine when the writer's sample supports them.

Keep the register already in use when editing. Do not switch a casual piece to formal mid-edit, and do not loosen a formal piece unless asked.

## WRITE mode intake

Before composing from a brief, establish up to three things. Ask only what the brief does not already answer, and ask them in one short message:

1. **Reader.** Who reads this — customer, colleague, reviewer, public audience?
2. **Text type.** Email, post, proposal, docs section, report section, UI text?
3. **Goal.** What should the reader know, feel or do after reading?

If the brief already makes all three unambiguous, ask nothing and write.

The goal also sets how much effort the text may ask of the reader:

- **Inform, document, or get the reader to act** in instructions, notices, status updates or UI text: low reading effort is the goal. Short, predictable sentences are correct here. Do not add variation or rarer words to sound less like AI.
- **Persuade**, and any text meant to hold attention (proposals, cover letters, opinion pieces, LinkedIn posts): the flat, even-length draft with the most obvious word in every slot is the weakness. Choose the more precise word, not the fancier one (fancier is E7 and E11), and let sentence length follow the argument. Readers skim AI-smoothed text more and engage less with it.

## Checklist before delivering new copy

- Reader, text type and goal settled (asked or inferred).
- Register chosen and held throughout.
- Every fact from the brief used; every missing fact a visible bracketed placeholder.
- No invented facts, names, numbers, dates, quotes or citations.
- Writer's sample (if given) drives sentence length, punctuation and word choice, and the draft passes the dimmer check.
- Reading effort matches the goal: plain for instructions and notices, not flattened for persuasion.
- Personality level matches the text type table.
