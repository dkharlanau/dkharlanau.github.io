# Root Cause Analysis — Templates

## Template 1: Root Cause Analysis Note

```markdown
---
artifact: Root Cause Analysis Note
id: RCA-001
date: YYYY-MM-DD
author: Name
status: draft | reviewed | closed
---

## Symptom
<!-- Exact observation. Error text, transaction, record IDs. -->

## Defect classification
<!-- data | config | code | process | integration | infrastructure | user error | unknown -->

## Affected scope
<!-- Systems, records, users, business areas, time period -->

## Timeline
<!-- Chronological list of events: last success, first failure, changes, maintenance -->

## Immediate cause
<!-- What directly produced the symptom -->

## Root cause
<!-- The underlying reason. Ask "why" until you reach a process or governance gap. -->

## Entry point
<!-- Where the defect entered the lifecycle -->

## Business impact
<!-- Quantified: orders blocked, invoices delayed, revenue at risk, hours lost -->

## Correction approach
<!-- Manual, mass update, reprocessing, reversal, rollback -->

## Prevention control
<!-- What stops recurrence: validation, workflow, monitoring, process change -->

## Correction owner
<!-- Who fixes the affected records -->

## Prevention owner
<!-- Who implements the control -->

## Deadlines
<!-- Correction by: YYYY-MM-DD. Prevention by: YYYY-MM-DD. -->

## Verification
<!-- How we confirm the fix and the control work -->

## Related incidents
<!-- Ticket numbers, IDocs, change requests, previous RCAs -->
```

## Template 2: Remediation Backlog Item

```markdown
---
artifact: Remediation Backlog Item
id: REM-001
date: YYYY-MM-DD
source: RCA-001
priority: P1 | P2 | P3
---

## Description
<What needs to be corrected or implemented>

## Scope
- Records affected: <count>
- Systems involved: <list>
- Timeline: <start date> to <end date>

## Method
<Step-by-step correction or implementation plan>

## Validation
<How to confirm the remediation is complete and correct>

## Risks
<What could go wrong during remediation>

## Rollback plan
<How to undo if the remediation causes issues>

## Owner
<Name and team>

## Deadline
<YYYY-MM-DD>
```

## Template 3: Prevention Control Proposal

```markdown
---
artifact: Prevention Control Proposal
id: PCP-001
date: YYYY-MM-DD
source: RCA-001
---

## Control description
<!-- What will be implemented to prevent recurrence -->

## Type
<!-- validation | workflow | monitoring | process change | automation -->

## Implementation steps
1. <step>
2. <step>

## Owner
<!-- Who implements the control -->

## Deadline
<!-- When the control must be in place -->

## Verification
<!-- How to confirm the control works -->

## Cost estimate
<!-- One-time and ongoing cost -->
```

## Template 4: 5 Whys Trace

```markdown
| Level | Question | Answer |
|-------|----------|--------|
| Symptom | What was observed? | <answer> |
| Why 1 | Why did this happen? | <answer> |
| Why 2 | Why did that happen? | <answer> |
| Why 3 | Why did that happen? | <answer> |
| Why 4 | Why did that happen? | <answer> |
| Why 5 | Why did that happen? | <answer> |
| Root cause | What systemic gap allows this? | <answer> |
```
