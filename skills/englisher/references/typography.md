# Typography and number format

Load when the pre-emit scanner in SKILL.md flags typography, numbers, dates, currency, or punctuation consistency. These conventions are mechanical and models get them wrong constantly, especially when translating from another locale.

| Element | Wrong | Right |
| --- | --- | --- |
| Dashes in prose | `the result—unexpected—changed plans`; `the result - unexpected - changed plans` | Rule and examples: `english-tells.md` E14. |
| Hyphen vs dash | `a 3–year project`, `the costs—$5m—rose` | Hyphen (`-`) joins words: `a 3-year project`. Never use a dash where a hyphen belongs. |
| Quotation marks | mixing `"..."` and `“...”` in one document | Straight quotes `"..."` in plain text and code-adjacent content. Curly quotes are acceptable when the writer's sample or target CMS uses them — pick one form and hold it. Do not normalize attributed quotes, mandated wording, code, or paste-ready strings. |
| Apostrophes | `it’s` in plain text with straight quotes elsewhere | `'`. Match the document's quote style. |
| Ellipsis | `wait... what`, `wait . . . what` in formal text | `wait…` single character, or three unspaced dots `...` — pick one and hold it. Avoid in formal text entirely. |
| Serial comma (Oxford) | `apples, oranges and pears` then later `apples, oranges, and pears` | Both forms are correct English. Pick one and hold it for the whole document. When editing, keep the form the source already uses. |
| List punctuation | bullet items ending with mixed periods and no periods | Full sentences in a list end with a period; fragments do not. Never mix the two in one list. |
| Number consistency | `8 GB` then later `8GB`; `version 2.0` then `v2.0` | One notation, held throughout. Match the source when editing. |
| Spell out vs digits | `five servers` then `5 servers` in one text | Convention: spell out one through nine, digits from 10 up, digits always with units and in technical text. Whatever the rule, apply it consistently. |
| Dates in prose | `May 15th`, `the 15 of May`, `15/5/2026` | `May 15` or `15 May` — pick one convention and hold it. Numeric dates are ambiguous across locales (`03/04/2026`): preserve the source form and ask which locale applies. |
| Large numbers | long-scale source words carried over: `1 milliard` (Danish/German), `1 billion` meaning 10¹² (older UK/French usage) | English `billion` = 10⁹, `trillion` = 10¹². Source-bound translation: Danish/German `Milliarde/milliard` → `billion`; French `billion` → `trillion`. When unsure, write the digits. |
| Currency in prose | `100 kr.`, `100DKK`, `100€`, `$ 5` | `DKK 100` or `100 DKK` (hold one form); `€100`, `$5` — no space after the symbol. ISO codes (`DKK`, `EUR`, `USD`) are unambiguous; prefer them in business text. |
| Percent | `20 %` then `30%` in the same document | `20%` is standard in English prose; `20 %` appears in some house styles. Pick one and hold it. |
| Time | `3:00 PM` in a document that otherwise uses `15:00` | Pick 12-hour or 24-hour and hold it. `3 PM` needs no `:00`. |
| Headings | `Strategic Negotiations And Global Partnerships` | `Strategic negotiations and global partnerships` (sentence case) unless the house style demands title case. See `english-tells.md` E17. |
| Capitalization after colon | mid-sentence `: The system...` when the following text is a fragment | Capitalize after a colon only when a full sentence follows — and even then, lowercase is common in US style. Fragments stay lowercase. |
| Abbreviations | source-language abbreviations leaking into English (`fx`, `dvs.`, `osv.`, `z.B.`, `ca.`, `p.ex.`) | `e.g.`, `i.e.`, `etc.` — or better, plain English: `for example`, `that is`, `and so on`. |
