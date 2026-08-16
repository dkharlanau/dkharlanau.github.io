---
name: decision-facilitation
description: Use when an enterprise discussion repeats without closure, teams argue about solutions before agreeing on the decision, several materially different options exist, or a decision is blocked by missing evidence, hidden constraints, or unclear authority. Produces a Decision Facilitation Record with decision statement, owner, criteria, evidence, trade-offs, blockers, choice or deferment, and actions.
---

# Decision Facilitation

## Purpose

Turn an ambiguous multi-stakeholder discussion into a clear decision, or into an explicit deferment with the exact missing evidence and owner needed to decide later.

## Use when

- A design or delivery meeting keeps returning to the same topic.
- Product or implementation debate starts before the decision is clear.
- Several real options exist and trade-offs matter.
- Missing evidence, authority, or constraints block closure.

## Do not use when

- A decision was already made and only documentation is required. Use `architecture-decision-record` or another decision-record skill.
- There is only one allowed option because of a verified non-negotiable constraint.
- The task is detailed implementation planning after the choice is made.

## Required inputs

- Decision topic and required business or technical outcome.
- Known options or current proposed direction.
- Stakeholders and accountable decision owner.
- Constraints, risks, dependencies, and available evidence.
- Deadline or trigger that makes the decision necessary.

## Workflow

1. Write the decision in one sentence that can be answered with a choice or explicit deferment.
2. Name the accountable decision owner.
3. Define the outcome the decision must protect.
4. Separate non-negotiable constraints from preferences and assumptions.
5. Build materially different options rather than vendor variations of the same system shape.
6. Define decision criteria before scoring options.
7. Attach evidence, assumptions, and unknowns to important claims.
8. State the trade-off for each option: what improves and what becomes worse.
9. Identify blockers and the smallest evidence or experiment that can remove them.
10. Make the decision or defer explicitly.
11. Record rationale, conditions, rejected options, and trigger for review.
12. Convert open conditions and questions into owned actions.

## Decision rules

- If the decision cannot be written in one sentence, reduce the scope before comparing options.
- If no accountable owner exists, escalate governance rather than treating consensus as authority.
- Do not score options before criteria are agreed.
- Different vendors do not count as different options when architecture and trade-offs are effectively the same.
- If one unknown can change the preferred option, test that unknown before polishing a large matrix.
- A deferred decision must name missing evidence, owner, and trigger for reopening.

## Output format

Produce a **Decision Facilitation Record**:

```markdown
## Decision
Decision statement:
Decision owner:
Decision deadline / trigger:

## Outcome to protect

## Constraints
| Constraint | Type | Evidence | Negotiable? |
|---|---|---|---|

## Options
| Option | System shape | Benefits | Costs / risks | Reversibility |
|---|---|---|---|---|

## Criteria
| Criterion | Why it matters | Weight / priority if used |
|---|---|---|

## Evidence and unknowns
| Claim / question | Evidence | Assumption | Unknown |
|---|---|---|---|

## Trade-offs

## Decision blockers

## Decision result
CHOSEN | DEFERRED
Chosen option / reason:
Conditions:
Rejected options / reason:

## Follow-up actions
| Action | Owner | Trigger / due condition |
|---|---|---|
```

## Quality gates

- [ ] Decision is one clear sentence.
- [ ] Accountable owner is named.
- [ ] Constraints and preferences are separated.
- [ ] Options are materially different.
- [ ] Criteria exist before option scoring.
- [ ] Evidence, assumptions, and unknowns are visible.
- [ ] Trade-offs are explicit.
- [ ] Decision or deferment includes rationale and owned actions.

## References

- `references/method.md` — Decision framing, option-shape, evidence, and deferment model.
- `references/templates.md` — Decision Facilitation Record and meeting decision canvas.
- `references/examples.md` — Synthetic integration, AI, delivery, and architecture decisions.
