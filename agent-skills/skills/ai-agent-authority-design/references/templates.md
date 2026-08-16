# AI Agent Authority Design Templates

## AI Agent Authority Record

```markdown
# AI Agent Authority Record

Job ID:
Owner:
Date:

## Business job
Outcome:
Accountable owner:

## Tools and data
| Tool / source | Read scope | Write scope | Environment | Constraints |
|---|---|---|---|---|

## Action authority
| Action | Risk | Read | Propose | Validate | Approve | Execute |
|---|---|---|---|---|---|---|

## Deterministic controls
| Control | Mechanism | Failure behavior |
|---|---|---|

## Evidence required before action

## Approval
Risk tier requiring approval:
Approver:
Evidence shown:
Expiry / time limit:

## Failure handling
Timeout:
Tool error:
Uncertain model output:
Partial execution:
Duplicate request:
Rollback / recovery:

## Audit evidence

## Evaluation cases
| Case | Expected behavior | Pass / fail rule |
|---|---|---|

## Autonomy expansion
Current level:
Evidence required for next level:
Decision owner:
```

## Action approval block

```markdown
Proposed action:
Target resource:
Business reason:
Evidence:
Validation result:
Side effects:
Reversibility:
Duplicate risk:
Approver:
Decision:
```
