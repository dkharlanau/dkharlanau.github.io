---
name: architecture-decision-record
description: Use when choosing between two or more technical approaches where the choice will be hard to reverse, or when a design review, audit, or new team member questions a past architectural choice. Produces a concise ADR with context, options, decision, consequences, and reversibility. Do not use for trivial or reversible decisions.
---

# Architecture Decision Record

## Purpose

Record why a significant architectural choice was made, what options were rejected, and what consequences follow.

## Use when

- You must choose between two or more technical approaches and the choice will be hard to reverse.
- A design review identified a decision point that needs explicit documentation.
- A new team member or vendor is questioning a design choice that was made two years ago.
- An audit or compliance review requires evidence that architecture decisions were made with due diligence.
- You are standardizing decision records across a program so that all projects produce comparable documentation.

## Do not use when

- Only one option is viable (record as a constraint note, not an ADR).
- The decision is trivial and easily reversible (e.g., library version bump).
- You need a high-level enterprise architecture strategy without a specific decision.

## Required inputs

- The decision question, stated as a single sentence.
- The context: what situation, constraint, or requirement forces this decision now.
- At least two viable options with descriptions, not just one preferred option.
- Evaluation criteria: what dimensions matter (cost, time, risk, maintainability, scalability, compliance).
- Stakeholder input: who advocated for each option and why.
- Reversibility assessment: how hard and expensive it would be to change this decision later.

## Workflow

1. **State the decision question.** Write one sentence that captures exactly what must be decided. Avoid framing the question to favor one option.
2. **Describe the context.** Explain the situation, constraints, and requirements that make this decision necessary. Include deadlines, budget limits, and regulatory factors.
3. **Define evaluation criteria.** List 3–5 criteria that will be used to compare options. Weight them if the team agrees on relative importance.
4. **List options.** Describe each option at a consistent level of detail. Include at least two viable options and a "do nothing" or status quo option where relevant.
5. **Evaluate each option.** Against each criterion, record pros, cons, and risks. Be honest about drawbacks of the option you prefer.
6. **Make the decision.** State which option is chosen and why. Cite the criteria that tipped the balance.
7. **Record consequences.** List positive consequences (what we gain) and negative consequences (what we accept or lose). Include technical debt, new dependencies, and skill requirements.
8. **Assess reversibility.** Rate the decision as easily reversible, moderately reversible, or irreversible. Describe what would be required to reverse it.
9. **Assign ownership and review date.** Name the person or role accountable for this decision. Set a date when the decision should be revisited.
10. **Link related decisions.** Reference other ADRs that this decision depends on or affects.

## Decision rules

- If only one option is viable, the decision is not architectural — it is a constraint. Record it as a constraint note, not an ADR.
- If the preferred option is custom development when a standard alternative exists, require explicit justification with named trade-offs.
- If a decision is irreversible or expensive to reverse, escalate to program or enterprise architecture for approval before recording.
- If an option introduces a new vendor or platform, evaluate exit cost and data portability explicitly.
- If two options score equally on all criteria, choose the one that is closer to existing team skills and operational tooling.
- If a decision contradicts a previous ADR, record the superseding relationship and update the status of the old ADR.
- If no one can be named as the decision owner, the decision is not ready to be recorded.

## Output format

Produce an **Architecture Decision Record (ADR)**:

```markdown
---
artifact: Architecture Decision Record
id: ADR-001
date: YYYY-MM-DD
status: proposed | accepted | deprecated | superseded
owner: Name | Role
review_date: YYYY-MM-DD
---

## Decision question
<!-- One sentence. Example: How should customer master data be distributed to downstream systems? -->

## Context
<!-- What situation forces this decision? Constraints, requirements, deadlines. -->

## Evaluation criteria
<!-- 3-5 criteria used to compare options. Weight if agreed. -->

## Options considered

### Option 1: <Name>
- Description:
- Pros:
- Cons:
- Risks:

### Option 2: <Name>
- Description:
- Pros:
- Cons:
- Risks:

### Option 3: <Name> (if applicable)
- Description:
- Pros:
- Cons:
- Risks:

## Decision
<!-- Which option was chosen and why. Cite the criteria that tipped the balance. -->

## Consequences

### Positive
- 

### Negative
- 

## Reversibility
<!-- Easily reversible | Moderately reversible | Irreversible. What would be required to reverse? -->

## Related decisions
<!-- Links to other ADRs this depends on or affects -->
```

Also produce a **Decision Log Entry** for the master decision log.

## Quality gates

- [ ] The decision question is a single sentence with no embedded preference.
- [ ] At least two viable options are described at a consistent level of detail.
- [ ] Every option has at least one con or risk recorded honestly.
- [ ] The decision explicitly cites which criteria tipped the balance.
- [ ] Consequences include both positive and negative outcomes.
- [ ] Reversibility is rated and the reversal cost is described.
- [ ] A named owner and a review date are assigned.
- [ ] The ADR is linked to related decisions where applicable.
- [ ] The ADR has been shared with the team that will implement and operate it.

## References

- `references/method.md` — Detailed option evaluation, criteria weighting, and reversibility assessment.
- `references/templates.md` — Copy-ready templates for ADR and Decision Log Entry.
- `references/examples.md` — Good and bad examples from SAP integration, cloud migration, and custom-vs-standard decisions.

## Safety rules

- Separate facts from assumptions. Label assumptions about option performance, cost, or team capacity.
- Separate decisions from open questions. List open questions about unverified options or missing stakeholder input.
- Do not expose client names, proprietary vendor contracts, or internal pricing.
- Do not copy proprietary framework text. Use your own words.
- Do not invent stakeholder input. If the user does not provide who advocated for which option, leave it empty or ask.
