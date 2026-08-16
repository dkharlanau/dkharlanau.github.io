# Release Readiness Templates

## Release Readiness Record

```markdown
# Release Readiness Record

Release ID:
Owner:
Date:
Environment:
Window:

## Scope
Included:
Excluded:
Still changing:

## Risk and evidence
| Risk | Level | Evidence / control | Status | Owner |
|---|---|---|---|---|

## Defects and limitations
| Item | Impact | Blocker / accepted / limitation / cosmetic | Workaround | Owner |
|---|---|---|---|---|

## Dependencies
| Dependency | Required state | Actual state | Evidence | Owner |
|---|---|---|---|---|

## Execution plan
| Step | Owner | Checkpoint | Stop condition |
|---|---|---|---|

## Rollback / recovery
Trigger:
Method:
Decision owner:
Evidence that it is feasible:

## Production validation
| Signal | Expected | Owner | Window |
|---|---|---|---|

## Business readiness
Support coverage:
Communication:
Training / process change:
Business acceptance:

## Decision
GO | CONDITIONAL GO | NO-GO
Reason:
Conditions:

## Post-release validation
Observed signals:
Issues:
Final closure:
```

## Compact go/no-go decision

```markdown
Scope stable: yes | no
Critical risks evidenced: yes | no | partial
Critical dependencies confirmed: yes | no
Recovery credible: yes | no
Monitoring ready: yes | no
Business owner ready: yes | no | not required
Open blockers:
Decision:
Conditions and owners:
```
