---
name: acceptance-criteria
description: Use when a requirement is approved and ready for implementation, but no one has defined how to verify it. Produces testable pass/fail standards with Given/When/Then scenarios, edge cases, and non-functional thresholds. Do not use for vague requirements that need elicitation first.
---

# Acceptance Criteria

## Purpose

Define pass/fail standards before work starts, so that delivery disputes are replaced by verifiable evidence.

## Use when

- A requirement is approved and ready for implementation, but no one has defined how to verify it.
- A user story is written and the development team asks "how will we know this is working?"
- A change request is scoped and the approver wants to know what success looks like.
- A test plan is being prepared and the testers need specific inputs and expected outputs.
- A contract milestone is defined and the vendor and client disagree on whether it was met.
- An incident fix is deployed and the business asks how to confirm the fix is permanent.

## Do not use when

- The requirement is vague or unapproved (use `requirements-elicitation` first).
- You are writing test scripts or automation code (this skill defines what to test, not how to automate).
- The task is exploratory testing or usability evaluation.

## Required inputs

- Approved Requirements Brief with a clear requirement statement.
- System documentation showing current behavior, fields, and transactions involved.
- Test data samples or production data extracts that represent normal and edge cases.
- Stakeholder availability to validate that the criteria match their intent.
- Non-functional requirements: performance, availability, security, compliance constraints.
- Regulatory or audit constraints that affect what must be demonstrable.
- Previous test plans or criteria from similar requirements (if available).

## Workflow

1. **Read the requirement statement.** Ensure it is testable. If it contains words like "easy," "fast," or "user-friendly," rewrite the requirement first.
2. **Identify the scenario, precondition, action, and expected outcome.** For each requirement, break it into: what must be true before, what happens, and what must be true after.
3. **Write Given/When/Then criteria for each scenario.** Use the format: Given [precondition], When [action or event], Then [expected outcome].
4. **Add non-functional criteria.** For each requirement, specify performance, availability, security, and compliance thresholds.
5. **List edge cases.** Identify at least three: normal case, boundary case, and error case.
6. **Define test data needs.** State exactly what data is needed, in which system, and how to obtain or create it.
7. **Identify who signs off.** Name the person who will approve that criteria are met. Verify they have authority.
8. **Document in an Acceptance Criteria Set.** One set per requirement. Link to the Requirements Brief.
9. **Validate with the requirement owner.** Walk through each criterion and confirm it matches their intent.

## Decision rules

- If a requirement has no measurable outcome, rewrite the requirement before writing acceptance criteria.
- If criteria require data that does not exist in test systems, flag a test environment gap.
- If edge case handling is not specified, the criterion is incomplete.
- If the sign-off owner is not the requirement owner, verify their authority to approve.
- If non-functional criteria are missing, the deliverable may pass functionally and fail operationally.
- If criteria can be automated, note the automation approach and tool.
- If criteria conflict with existing system behavior, flag the conflict before implementation.

## Output format

Produce an **Acceptance Criteria Set** per requirement:

```markdown
---
artifact: Acceptance Criteria Set
id: AC-001
requirement: Link to requirement brief
status: draft | reviewed | approved
---

## Scenario: Normal case
Given <precondition>
When <action or event>
Then <expected outcome>

## Scenario: Boundary case
Given <precondition>
When <action or event>
Then <expected outcome>

## Scenario: Error case
Given <precondition>
When <action or event>
Then <expected outcome>

## Non-functional criteria
- Performance: <metric>
- Availability: <metric>
- Security: <requirement>
- Compliance: <requirement>

## Edge cases
- <Edge case 1>
- <Edge case 2>

## Test data requirements
<!-- What data is needed to verify these criteria -->

## Verification method
<!-- Manual test | Automated test | Review | Demonstration -->

## Sign-off owner
<!-- Who approves that criteria are met -->
```

Also produce **Test Data Requirements** and a **Verification Plan** if multiple criteria sets are involved.

## Quality gates

- [ ] Every requirement has at least one acceptance criterion.
- [ ] Criteria are testable pass/fail statements, not open to interpretation.
- [ ] Edge cases are covered: normal, boundary, and error.
- [ ] Non-functional requirements have specific metrics or thresholds.
- [ ] Test data is identified with source and creation method.
- [ ] Sign-off owner is named and has authority.
- [ ] No criterion contains implementation detail or solution design.

## References

- `references/method.md` — Detailed Given/When/Then writing, non-functional criteria definition, and edge case identification.
- `references/templates.md` — Copy-ready templates for Acceptance Criteria Set, Test Data Requirements, and Verification Plan.
- `references/examples.md` — Good and bad examples from SAP credit management, data migration, and IDoc processing contexts.

## Safety rules

- Separate facts from assumptions. Label assumptions about test data availability and system behavior.
- Separate decisions from open questions. List open questions about sign-off authority or test environment gaps.
- Do not expose client names, internal project codes, or proprietary system details.
- Do not copy proprietary framework text. Use your own words.
