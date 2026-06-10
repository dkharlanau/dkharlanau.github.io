# Data Quality Root Cause — Templates

## Template 1: Data Quality Root Cause Note

```markdown
---
artifact: Data Quality Root Cause Note
id: DQRC-001
date: YYYY-MM-DD
author: Name
status: draft | reviewed | closed
---

## Symptom
- Field: <exact field>
- Wrong value: <observed>
- Expected value: <target>
- System: <where observed>
- Business process affected: <process>
- Records affected: <count>
- First occurrence: <date>

## Business impact
<quantified or described in process terms>

## Root cause classification
<Type from classification table>

## Entry point
<System, transaction, interface, or user action>

## Scope assessment
- Currently affected: <count>
- Potentially affected: <count>
- Downstream spread: <yes/no + systems>

## Correction approach
- Method: <manual / mass update / reprocessing / mapping fix / merge>
- Validation steps: <what to check before and after>
- Approval required: <who>

## Prevention control
- Control type: <validation / workflow / mapping / sync / monitoring / UI>
- Implementation owner: <name>
- Monitoring: <how to detect recurrence>

## Owners
- Correction: <name>
- Validation: <name>
- Prevention implementation: <name>
- Monitoring: <name>

## Validation
- Confirmed by: <business owner> and <technical owner>
- Date: <YYYY-MM-DD>
```

## Template 2: Remediation Backlog Item

```markdown
---
artifact: Remediation Backlog Item
id: REM-001
date: YYYY-MM-DD
source: DQRC-001
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

## Template 3: Data Quality Rule

```markdown
---
artifact: Data Quality Rule
id: DQR-001
date: YYYY-MM-DD
status: draft | approved | active | retired
---

## Rule name
<Short descriptive name>

## Applies to
<Data element, table, system>

## Condition
<When this rule is checked>

## Validation logic
<Exact condition that must be true>

## Enforcement point
<System, transaction, or API where this is checked>

## Failure action
<What happens when the rule is violated>

## Owner
<Who maintains this rule>

## Review frequency
<How often the rule is reviewed>
```

## Template 4: Defect Trace Log

```markdown
| Step | System | Field Value | Rule Checked? | Result | Next Step |
|------|--------|-------------|---------------|--------|-----------|
| 1 | <system> | <field> = <value> | <rule> | <pass/fail> | <next> |
| 2 | <system> | <field> = <value> | <rule> | <pass/fail> | <next> |
```
