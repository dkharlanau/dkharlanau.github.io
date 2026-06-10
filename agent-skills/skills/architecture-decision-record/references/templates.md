# Architecture Decision Record — Templates

## Template 1: Architecture Decision Record (ADR)

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

## Template 2: Decision Log Entry

```markdown
| ID | Date | Question | Decision | Status | Owner | Review Date |
|----|------|----------|----------|--------|-------|-------------|
| ADR-001 | YYYY-MM-DD | <question> | <decision> | <status> | <name> | <date> |
```

## Template 3: Stakeholder Input Summary

```markdown
---
artifact: Stakeholder Input Summary
id: SIS-001
adr: ADR-001
---

## Stakeholder positions

| Stakeholder | Role | Preferred Option | Key Arguments |
|-------------|------|------------------|---------------|
| <name> | <role> | <option> | <arguments> |

## Conflicts
<!-- Where stakeholders disagreed and how the decision resolved it -->

## Escalation
<!-- If escalation was required, who decided and on what basis -->
```

## Template 4: Option Evaluation Matrix

```markdown
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| <criterion> | <weight> | <score> | <score> | <score> |
| **Total** | | <score> | <score> | <score> |
```
