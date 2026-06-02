# Danish Report Writer Test Notes

Skill creation followed documentation TDD: pressure scenarios first, baseline failures observed, then skill content written to close those gaps.

## RED Baseline Scenarios

### Scenario A: Fast AI In Schools Report

Prompt: The user asks for a Danish academic report about AI in Danish schools and says to draft it now.

Baseline result:

- Agent drafted immediately.
- It did not ask for local formal requirements, assignment brief, rubric, page count, citation style, or template.
- It inserted a problem formulation after drafting began rather than establishing it first.
- It treated Google/chatbots correctly as non-sources, but still risked premature drafting.

Observed failure pattern: speed pressure caused standard-report drafting before `formalia`, `målgruppe`, `formål`, report type, and source basis were established.

### Scenario B: Messy Notes To Report

Prompt: The user says they have messy notes from interviews, websites, and ChatGPT about employee well-being and asks for a Danish report without many questions.

Baseline result:

- Agent asked for some context, but did not require a `synopsis`.
- It did not classify material as core substance, background, or irrelevant.
- It recognized the risk of a generic report or source dump.

Observed failure pattern: vague material pressure caused generic structure suggestions without a strong planning and classification gate.

### Scenario C: Conclusion And Bibliography Patch

Prompt: The user asks to fix a conclusion and bibliography fast. The `problemformulering` concerns why young people mistrust municipalities, but the conclusion summarizes digital communication. Sources include Google, ChatGPT, webpages, and an interview.

Baseline result:

- Agent compared problem formulation and conclusion.
- Agent rejected Google and ChatGPT as sources.
- Agent required claim-level references and source metadata.
- It still risked offering a pasteable patched conclusion rather than forcing revision of the underlying argument.

Observed failure pattern: repair pressure can lead to symptom patching unless the skill explicitly says the report is not done when conclusion and question do not match.

## GREEN Expectations

The skill must make agents:

- Ask for or visibly assume local `formalia` before drafting full prose.
- Establish `afsender`, `målgruppe`, `formål`, report type, `problemformulering`, and source basis.
- Use the 9-part `synopsis` when planning is missing.
- Classify source material before drafting.
- Reject Google, image search, and chatbots as sources.
- Require claim-level references plus `kildefortegnelse`.
- Compare `problemformulering` and `konklusion` side by side.
- Refuse to treat a topic summary as a finished conclusion.
