# Change Impact Analysis — Templates

## Template 1: Change Impact Assessment

```markdown
---
artifact: Change Impact Assessment
id: CIA-001
date: YYYY-MM-DD
change: Description
status: draft | reviewed | approved
---

## Change description
<!-- Exact object, current value, proposed value, system -->

## Change driver
<!-- Why this change is needed -->

## Systems affected
<!-- Direct and indirect system impacts -->

| System | Component | Risk | Action Required | Owner |
|--------|-----------|------|-----------------|-------|
| SAP PRD | <object> | Medium | <action> | <name> |

## Data affected
<!-- Tables, fields, records that change -->

## Interfaces affected
<!-- APIs, IDocs, events that may break or need update -->

| Interface | Direction | Risk | Action Required | Owner |
|-----------|-----------|------|-----------------|-------|
| <ID> | <direction> | High | <action> | <name> |

## Processes affected
<!-- Business processes that change -->

## Stakeholders affected
<!-- Who needs to know or act -->

## Testing required
<!-- What must be tested before go-live -->

| Test | Tester | Data | Success Criteria |
|------|--------|------|------------------|
| <test> | <name> | <data> | <criteria> |

## Rollback plan
<!-- How to undo if the change fails -->

## Risk level
<!-- Low | Medium | High | Critical -->

## Approval required
<!-- Who must approve before implementation -->

## Owner
<!-- Who drives this assessment and the change -->

## Related changes
<!-- Links to other change impact assessments -->
```

## Template 2: Affected Component List

```markdown
---
artifact: Affected Component List
id: ACL-001
date: YYYY-MM-DD
change: CIA-001
---

## Components

| Component | Type | System | Risk | Action | Owner | Status |
|-----------|------|--------|------|--------|-------|--------|
| <name> | Program / Interface / Report / Process | <system> | <risk> | <action> | <name> | open / done |

## Risk summary
- Low: <count>
- Medium: <count>
- High: <count>
- Critical: <count>
```

## Template 3: Test Plan

```markdown
---
artifact: Test Plan
id: TP-001
date: YYYY-MM-DD
change: CIA-001
---

## Test cases

| Test | Type | Tester | Data | Success Criteria | Date | Result |
|------|------|--------|------|------------------|------|--------|
| <test> | Unit / Integration / Regression / UAT | <name> | <data> | <criteria> | <date> | Pass / Fail |

## Test data
<!-- What data is needed and how to obtain it -->

## Environment
<!-- Which system and client -->

## Sign-off
<!-- Who approves the test results -->
```

## Template 4: Rollback Procedure

```markdown
---
artifact: Rollback Procedure
id: RBP-001
date: YYYY-MM-DD
change: CIA-001
---

## Trigger
<!-- When to execute this rollback -->

## Steps
1. <step>
2. <step>

## Validation
<!-- How to confirm the rollback is complete -->

## Risks
<!-- What could go wrong during rollback -->

## Owner
<!-- Who executes the rollback -->
```
