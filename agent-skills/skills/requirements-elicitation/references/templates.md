# Requirements Elicitation — Templates

## Template 1: Requirements Brief

```markdown
---
artifact: Requirements Brief
id: REQ-001
source: Stakeholder interview | Ticket | Audit | Regulation
status: draft | reviewed | approved
---

## Business need
<!-- The underlying need, not the solution. Example: "Orders must not ship to customers with expired credit limits." -->

## Requirement statement
<!-- Clear, testable statement. Example: "The system must block outbound delivery creation when the customer credit limit is exceeded." -->

## Assumptions
<!-- What we assume to be true. Example: "Credit limit is maintained in FD32 and updated daily." -->

## Business rules
<!-- Rules that constrain the solution. Example: "Emergency orders under 1,000 EUR may bypass credit block with director approval." -->

## Constraints
<!-- Technical, budget, time, policy limits. Example: "Must use existing credit management framework; no custom development." -->

## Acceptance criteria
<!-- How we will know this is met. Example: "Given a customer with exceeded credit limit, when delivery is created, then the system blocks with status 'Credit block' and routes to credit team." -->

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

## Template 2: Stakeholder Statement Classification Table

```markdown
| Raw Statement | Classification | Source | Owner | Need It Addresses |
|---------------|----------------|--------|-------|-------------------|
| <statement> | Need / Solution / Assumption / Constraint / Risk / Complaint | <source> | <name> | <need or N/A> |
```

## Template 3: Assumptions Log

```markdown
---
artifact: Assumptions Log
id: AL-001
date: YYYY-MM-DD
---

| Assumption | Source | Validation Method | Validation Owner | Due Date | Risk if False | Status |
|------------|--------|-------------------|------------------|----------|---------------|--------|
| <assumption> | <source> | <method> | <name> | <date> | <risk> | open / validated / false |
```

## Template 4: Requirements Traceability Matrix

```markdown
| Requirement ID | Source Statement | Stakeholder | Business Rule | Acceptance Criterion | Priority | Status |
|----------------|------------------|-------------|---------------|----------------------|----------|--------|
| REQ-001 | <statement> | <name> | <rule> | <criterion> | <priority> | <status> |
```
