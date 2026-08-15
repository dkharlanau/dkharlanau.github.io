---
name: sap-lead-assessment-drill
description: Use when evaluating or practicing a 60-90 second SAP Lead assessment answer across Sales, Procurement, Logistics, Integration, Master Data, or AI. Scores reasoning with the TRIZ Lead rubric, identifies the strongest signal and biggest gap, and produces an improved B2 English answer without inventing system facts. Do not use for factual SAP configuration lookup.
---

# SAP Lead Assessment Drill

## Purpose

Evaluate whether an answer shows Lead-level system thinking rather than only product, configuration, or delivery knowledge.

The drill uses synthetic cases and one stable rubric. A candidate does not need to choose the same technology as the reference case. Reward reasoning quality, ownership, evidence, trade-offs, and communication.

## Canonical data

- `/datasets/triz-digital-framework/drill-cases.json` — synthetic assessment cases.
- `/datasets/triz-digital-framework/lead-rubric.json` — six scoring dimensions, bands, hard-fail signals, and answer spine.
- `/datasets/triz-digital-framework/catalog.json` — TRIZ Digital method, operators, resources, authority chain, and risk tiers.
- `/datasets/triz-digital-framework/patterns.json` — reusable system transformation patterns.
- `/triz/drill/` — browser practice interface.
- `/triz/workbench/` — deeper contradiction workbench.

## Use when

- The user wants a mock SAP Lead assessment question.
- The user gives an answer and asks for evaluation.
- The browser drill provides an agent evaluation payload.
- A practice session needs structured follow-up questions.
- A Senior-level answer needs to be rewritten into a stronger Lead-level answer.

## Do not use when

- The user only needs a factual transaction, table, configuration path, API, or product capability.
- The case contains real client-confidential information that should not be processed or published in the public project.
- The answer depends on current SAP product behavior that has not been verified from current primary sources.

## Evaluation workflow

1. **Read the case and candidate answer.**
   - Keep supplied facts separate from candidate assumptions.
   - Do not assume missing configuration, policy, ownership, thresholds, or landscape details.
2. **Identify the useful function.**
   - What outcome must remain true even if the current mechanism changes?
3. **Identify the contradiction.**
   - Which useful property is being improved?
   - Which other useful property may become worse?
4. **Check for separation thinking.**
   - time;
   - condition;
   - context;
   - system level;
   - authority;
   - representation.
5. **Check system-shape distance.**
   - Did the answer consider more than one real design shape?
   - Different vendors implementing the same architecture do not count as different options.
6. **Check technology allocation.**
   - exact rules and hard constraints → deterministic;
   - known sequence → workflow/state machine;
   - non-blocking reaction → event/queue;
   - fresh/private facts → retrieval/read tool;
   - interpretation → model;
   - unknown next useful step → bounded agent;
   - value conflict/high-impact approval → explicit policy or accountable human.
7. **Check authority.**
   - read;
   - propose;
   - validate;
   - approve;
   - execute.
   These may belong to different actors or mechanisms.
8. **Check evidence and experiment.**
   - evidence requested;
   - primary metric;
   - counter-metric;
   - bounded scope;
   - failure condition;
   - rollback or recovery when relevant.
9. **Score all six rubric dimensions from 0 to 4.**
   - Use the anchor text in `lead-rubric.json`.
   - Give one short evidence statement for every score.
10. **Check hard-fail signals.**
   - vendor-first;
   - single-option thinking;
   - authority gap;
   - AI capability treated as authorization;
   - no counter-metric;
   - invented system facts.
11. **Produce an improved 60-90 second answer.**
   - English B2.
   - Clear, semi-formal, consultant style.
   - No generic AI phrases.
   - No invented SAP facts.
   - Prefer architecture and business language over a list of acronyms.
12. **Ask two interviewer follow-ups.**
   - Base them on missing evidence, ownership, risk, or a weak trade-off in the candidate answer.

## Scoring rules

Use the rubric as written. Do not convert it into keyword matching.

A technically different answer can score highly when it:

- frames the useful function correctly;
- makes the contradiction explicit;
- creates real system-shape alternatives;
- allocates authority deliberately;
- asks for the evidence that would decide;
- gives a falsifiable experiment;
- communicates clearly.

A technically fashionable answer should score poorly when it:

- starts with a preferred product;
- hides ownership;
- uses AI for deterministic policy;
- gives broad write access without risk reasoning;
- proposes only one architecture;
- optimizes one metric and ignores the counter-effect.

## Output format

```markdown
## Score
**Total:** 18/24 — Lead-ready answer

| Dimension | Score | Evidence |
|---|---:|---|
| Problem framing | 3/4 | ... |
| Contradiction | 3/4 | ... |
| System-shape options | 4/4 | ... |
| Technology and authority | 3/4 | ... |
| Evidence and experiment | 2/4 | ... |
| Lead communication | 3/4 | ... |

## Strongest signal
<one concrete strength>

## Biggest gap
<one concrete gap>

## Hard-fail signals
- none | <specific signals>

## Improved 60–90 second answer
<concise B2 English answer>

## Follow-up questions
1. ...
2. ...
```

## Quality gates

- [ ] Every dimension has a numeric score and evidence.
- [ ] Total equals the sum of dimension scores.
- [ ] The performance band matches `lead-rubric.json`.
- [ ] Technical choice is not rewarded merely because it matches the reference case.
- [ ] Missing evidence is not treated as a factual error unless the candidate invented it.
- [ ] The improved answer does not add unverified SAP configuration or product facts.
- [ ] The improved answer can be spoken in roughly 60-90 seconds.
- [ ] Two follow-up questions target genuine weak points or unknowns.

## Safety and publication

- Treat all public drill cases as synthetic.
- Do not add client names, customer-specific configuration, credentials, internal IDs, or confidential process details to public datasets.
- If the user provides current SAP product claims, verify them from current primary sources before treating them as facts.
