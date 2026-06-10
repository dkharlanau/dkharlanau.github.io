# Acceptance Criteria — Templates

## Template 1: Acceptance Criteria Set

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

## Template 2: Test Data Requirements

```markdown
---
artifact: Test Data Requirements
id: TDR-001
requirement: Link to requirement brief
---

## Data needed

| Data Element | Source System | Creation Method | Anonymization | Owner |
|--------------|---------------|-----------------|---------------|-------|
| <element> | <system> | <method> | <yes/no> | <name> |

## Environment
- Test system: <name>
- Client: <client>
- Refresh date: <date>

## Gaps
<!-- Data that does not exist and must be created -->
```

## Template 3: Verification Plan

```markdown
---
artifact: Verification Plan
id: VP-001
requirement: Link to requirement brief
---

## Verification methods

| Criterion | Method | Tool | Tester | Date | Result |
|-----------|--------|------|--------|------|--------|
| <criterion> | Manual / Automated / Review / Demo | <tool> | <name> | <date> | Pass / Fail / N/A |

## Sign-off
- Verified by: <name>
- Date: <date>
- Approved by: <name>
```
