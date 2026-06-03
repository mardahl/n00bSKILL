# Presentation Best Practices — Research Basis

Background and citations for the rules enforced in `SKILL.md`. The hard limits are not stylistic preferences; they come from cognitive science and communication research.

> Note: This reference was authored for the Microsoft-enhanced version of the skill. The upstream `rhuss/cc-slidev` repository ships its own `presentation-best-practices.md`; consult it for the original author's full bibliography.

## Cognitive load and working memory

- **Miller's Law (1956)** — Working memory holds roughly **7 ± 2** items. Once a slide presents more discrete elements than this, the audience must either drop information or stop listening to process the slide. This is the basis for the **≤6 elements per slide** limit (kept below the upper bound for safety margin).
- **Cognitive Load Theory (Sweller)** — Extraneous load (decoration, redundant text, chart junk) competes with the load available for actually understanding the content. Remove anything that does not carry meaning.
- **Dual-channel / split-attention (Mayer's multimedia principles)** — The verbal channel processes spoken words; the visual channel processes images and on-screen text. Dense on-screen prose forces the audience to *read*, which blocks *listening*. Hence **keyword phrases, not sentences**, and **<50 words** of body text.
- **David JP Phillips** ("How to avoid death by PowerPoint") — Demonstrates that object count above ~6 sharply increases perceived complexity and audience disengagement.

## Slide design and structure

- **PLOS Computational Biology — "Ten Simple Rules for Effective Presentation Slides"** (Naegle, 2021). Key rules applied here:
  - One central message per slide; the title states that message.
  - Use the title as an **assertion** ("System scales to 10K req/sec"), not a label ("Results").
  - Respect the "billboard test": a slide should land in a few seconds.
  - Pacing of roughly **~1 minute per slide** as a planning heuristic (this skill uses 90s as a more realistic default for technical content).
- **MIT Communication Lab — Slide Presentation Guide** — "Take the text off the slide and put it into your presenter notes." Slides support speech; they do not replace it. Source of the presenter-notes discipline.
- **Assertion-Evidence model (Alley, Penn State)** — Replace topic-phrase headlines + bullet lists with a sentence assertion supported by a visual. Strongly improves comprehension and recall versus traditional bullet decks.

## Storytelling and persuasion

- **Three-Act structure** — Setup → Confrontation → Resolution. Maps to Hook/Problem → Content/Evidence → Synthesis/Call-to-action.
- **Pyramid Principle (Barbara Minto)** — Lead with the conclusion, then group supporting arguments, then evidence. Executives and architects want the recommendation first.
- **Start With Why (Simon Sinek)** — Open with purpose/problem, not process or org chart.
- **Rule of Three** — Audiences retain triads well; structure main points, examples, and takeaways in threes.
- **Nancy Duarte** (*Resonate*, *Slide:ology*) — Contrast ("what is" vs "what could be"), audience as hero, emotional + analytical balance.
- **Garr Reynolds** (*Presentation Zen*) — Restraint, simplicity, signal over noise, generous white space.

## Accessibility

- **WCAG 2.1 AA** — Text contrast **≥4.5:1** (normal), **≥3:1** (large, >24pt / >18.66px bold). Don't convey meaning by **color alone** — add labels, patterns, or shapes.
- **Font sizing** — Body **≥18pt**, headings **≥24pt**; sans-serif for body legibility (Segoe UI, Calibri, Arial, Helvetica). Avoid italics, underlines, and ALL CAPS in body text.
- **Colorblind-safe palettes** — Verify with ColorBrewer or a simulator. Blue + Orange is a robust default across deuteranopia/protanopia/tritanopia.

## Timing model

```
Expected slides = (duration_minutes × 60) / seconds_per_slide
Acceptable range = expected ± 20%
```

| Pace | s/slide | Use for |
| --- | --- | --- |
| Fast | 60 | Brief updates, high-level overviews |
| Moderate (default) | 90 | Technical content, balanced detail |
| Detailed | 120 | Complex topics, deep dives |
| Deep dive | 180 | Research talks, comprehensive analysis |

## Further reading

- Naegle, K. M. (2021). *Ten simple rules for effective presentation slides.* PLOS Computational Biology.
- Alley, M. *The Craft of Scientific Presentations* (Assertion-Evidence).
- Minto, B. *The Pyramid Principle.*
- Duarte, N. *Resonate* and *Slide:ology.*
- Reynolds, G. *Presentation Zen.*
- MIT Communication Lab — Slide Presentation Guide.
- W3C — Web Content Accessibility Guidelines (WCAG) 2.1.
