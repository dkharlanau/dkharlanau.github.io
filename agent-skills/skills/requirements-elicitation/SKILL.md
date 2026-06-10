---
name: requirements-elicitation
description: Use when turning vague stakeholder complaints, change requests, or project scope statements into structured, testable requirements with assumptions, constraints, risks, and acceptance criteria. Do not use for writing test cases or performing technical implementation.
---

# Requirements Elicitation

## Purpose

Turn vague stakeholder complaints into requirements, assumptions, risks, and acceptance criteria that a developer, tester, or AI agent can act on.

## Use when

- A new project or phase starts and the scope is described in a single sentence.
- Scope creep is detected: new requests appear that do not map to any documented requirement.
- A change request arrives with a solution but no description of the problem it solves.
- An incident recurs and the post-mortem concludes that "the system should have caught this."
- An integration failure requires a new validation rule, but no one has defined what valid means.
- A data migration is planned and the business says "just move everything" without field-level clarity.

## Do not use when

- Requirements are already documented and the task is implementation or testing.
- The request is purely technical (e.g., "upgrade the database") with no business process impact.
- You are performing root cause analysis on an existing defect (use `root-cause-analysis` or `data-quality-root-cause`).

## Required inputs

- Stakeholder Interview Briefs from relevant business and technical owners.
- Existing system documentation, configuration guides, or transaction codes involved.
- Incident tickets or error logs that triggered the need.
- Process maps or Process Analysis Notes for the affected workflow.
- Regulatory documents or compliance constraints (if applicable).
- Current-state data samples showing the problem (if data-related).
- List of known constraints: budget, timeline, system versions, integration contracts.

## Workflow

1. **Collect raw statements.** Gather everything stakeholders have said: emails, meeting notes, tickets, complaints, proposals. Do not filter yet.
2. **Classify each statement.** Label each item as: need, solution idea, assumption, constraint, risk, or complaint.
3. **Separate solution from requirement.** For every solution idea, ask: "What problem does this solve?" Write the problem as the need. Discard the solution unless it is a constraint.
4. **Write testable requirement statements.** Format: "The system/process must [action] so that [outcome]." Each statement must be verifiable.
5. **Identify missing context.** For each requirement, list what you do not know: field names, transaction codes, volume estimates, owner names. Flag these as open questions.
6. **Map to business rules.** Identify rules that constrain the requirement. Document them separately so they can be validated.
7. **Validate with the requirement owner.** Walk through each requirement, assumption, and acceptance criterion with the named business owner. Revise based on feedback.
8. **Package into Requirements Briefs.** One brief per distinct business need. Link related briefs. Include traceability to source statements.

## Decision rules

- If a stakeholder describes a solution, ask what problem it solves before writing a requirement.
- If a requirement has no acceptance criterion, it is not a requirement yet — it is a need statement.
- If two stakeholders give conflicting requirements, document both, flag the conflict, and ask who has decision authority.
- If a requirement references a system field, table, or transaction, verify that it exists and behaves as assumed before finalizing.
- If no owner can confirm a requirement, mark it as an assumption and add a risk that the requirement may be wrong.
- If a requirement came from an incident ticket, verify that the ticket root cause is addressed, not just the symptom.
- If a requirement is stated as "must be fast," "must be secure," or "must be user-friendly," rewrite it with a measurable threshold.

## Output format

Produce a **Requirements Brief** per distinct business need:

```markdown
---
artifact: Requirements Brief
id: REQ-001
source: Stakeholder interview | Ticket | Audit | Regulation
status: draft | reviewed | approved
---

## Business need
<!-- The underlying need, not the solution. -->

## Requirement statement
<!-- Clear, testable statement. -->

## Assumptions
<!-- What we assume to be true. -->

## Business rules
<!-- Rules that constrain the solution. -->

## Constraints
<!-- Technical, budget, time, policy limits. -->

## Acceptance criteria
<!-- How we will know this is met. -->

## Priority
<!-- Must have | Should have | Could have | Won't have -->

## Owner
<!-- Business owner who can confirm this is correct -->

## Dependencies
<!-- Other requirements, systems, decisions -->

## Risks
<!-- What could make this requirement wrong or impossible -->

## Open questions
<!-- What is unknown and who can answer it -->

## Related requirements
<!-- Links to other requirement briefs -->
```

Also produce an **Assumptions Log** and a **Requirements Traceability Matrix** if multiple requirements are involved.

## Quality gates

- [ ] Every requirement has at least one acceptance criterion.
- [ ] Every requirement has a named business owner who can confirm it.
- [ ] No requirement contains a solution disguised as a need.
- [ ] Assumptions are separated from facts and have a validation plan.
- [ ] Conflicts between stakeholders are flagged, not hidden.
- [ ] Each requirement traces back to a source statement or ticket.
- [ ] All vague qualifiers (fast, secure, user-friendly) have measurable thresholds.

## References

- `references/method.md` — Detailed classification method, need-vs-solution separation, and testable statement writing.
- `references/templates.md` — Copy-ready templates for Requirements Brief, Assumptions Log, and Traceability Matrix.
- `references/examples.md` — Good and bad examples from SAP rollout, data migration, and integration contexts.

## Safety rules

- Separate facts from assumptions. Label assumptions and state the risk if each assumption is false.
- Separate decisions from open questions. List open questions explicitly and assign discovery owners.
- Do not expose client names, internal project codes, or proprietary system details.
- Do not copy proprietary framework text. Use your own words.
