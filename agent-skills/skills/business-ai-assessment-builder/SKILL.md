---
name: business-ai-assessment-builder
description: Use when creating a review-ready SAP Lead practice case from canonical SAP Enterprise, Business AI graph, decision-profile, integration, data, control, and evidence records. Reuses the existing assessment model and avoids a second SAP topic database.
---

# Business AI Assessment Builder

## Purpose

Create SAP Lead practice cases that test cross-domain decision quality with traceable evidence, not only product recall.

## Use when

- Assessment coverage has a gap in Sales, Procurement/Logistics, Integration/Architecture, AI/Data, or Lead judgment.
- A Business AI decision profile can support a realistic synthetic practice case.
- Existing SAP Enterprise evidence should be reused in a blind assessment scenario.

## Do not use when

- The task is factual SAP lookup without a decision problem.
- The proposed case depends on unverified current SAP behavior.
- A near-duplicate assessment already tests the same process, decision, authority, and failure pattern.

## Required inputs

- `/ai/business-ai-agent-context.json`, pack `assessment_builder`.
- Existing Assessment and Interview Readiness coverage/state.
- Relevant SAP process, stage, integration, data, control, case, and decision-profile IDs.
- Existing Lead rubric and current case fingerprints.

## Workflow

1. Select a genuine coverage gap and define the Lead decision being tested.
2. Resolve canonical SAP and Business AI IDs.
3. Check existing assessment fingerprints for a near duplicate.
4. Build a synthetic scenario with only the evidence available to the candidate.
5. Add a cross-domain tension, constraint, or failure signal that requires Lead judgment.
6. Keep hidden challenge points and scoring guidance outside the blind prompt.
7. Build rubric criteria for process reasoning, architecture, integration, data, controls, trade-offs, evidence, ownership, and communication.
8. Separate factual recall from decision quality in the rubric.
9. Add interviewer follow-ups that test assumptions, authority, failure handling, and missing evidence.
10. Link canonical study/evidence material for use after the attempt.
11. Set publication state through the existing Assessment workflow, not a new state store.

## Decision rules

- Prefer one hard cross-domain decision over a long inventory of SAP facts.
- A different technology choice can score well when reasoning and controls are stronger.
- Weak public evidence must not become a factual exam answer.
- Hidden rubric material stays hidden until the attempt is complete where the current UX requires it.
- Synthetic cases must not resemble confidential client incidents closely enough to expose private facts.

## Output format

Produce an **Assessment Case Proposal** with: case ID proposal, coverage gap, canonical IDs, blind prompt, supplied evidence, assumptions allowed, hidden challenge points, Lead decisions expected, scoring rubric, hard-fail signals, follow-up questions, duplicate fingerprint, and post-attempt study links.

## Quality gates

- [ ] Canonical IDs exist and are referenced instead of copied topic definitions.
- [ ] Duplicate fingerprint was checked.
- [ ] The prompt tests a decision, not only factual recall.
- [ ] Rubric separates process, architecture, integration, data, controls, trade-offs, evidence, and communication.
- [ ] Weak evidence is not promoted into a factual answer key.
- [ ] Hidden rubric is separate from the blind prompt.
- [ ] Existing Assessment state and scoring model remain authoritative.
- [ ] No client-confidential material is present.

## References

- `references/method.md` — Case selection and scoring method.
- `references/templates.md` — Assessment proposal template.
- `references/examples.md` — Cross-domain SAP Lead examples.
