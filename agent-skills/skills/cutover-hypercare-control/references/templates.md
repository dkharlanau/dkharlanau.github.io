# Cutover & Hypercare Control Templates

## Cutover & Hypercare Control Record

```markdown
# Cutover & Hypercare Control Record

Release:
Command owner:
Window:
Current transition state:

## Critical path
| Step | Predecessor | Owner | Planned | Actual | Evidence | Status |
|---|---|---|---|---|---|---|

## Checkpoints
| Checkpoint | Continue criteria | Stop criteria | Decision owner | Result |
|---|---|---|---|---|

## Recovery
Method:
Trigger:
Decision owner:
Latest safe decision point:

## Technical validation
| Control | Expected | Actual | Evidence |
|---|---|---|---|

## Business validation
| Scenario | Expected | Actual | Owner |
|---|---|---|---|

## Hypercare issues
| Issue / pattern | Impact | Workaround | Owner | Permanent action |
|---|---|---|---|---|

## Stabilization
| Signal | Exit criterion | Actual | Trend |
|---|---|---|---|

## Handover and exit
Normal support owner:
Open risks:
Knowledge transferred:
Exit decision:
```

## Checkpoint decision block

```markdown
Checkpoint:
Evidence complete: yes | no
Stop condition triggered: yes | no
Recovery still possible: yes | no
Decision: continue | hold | rollback | forward recover
Decision owner:
Reason:
Next checkpoint:
```
