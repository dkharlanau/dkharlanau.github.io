# Batch & Queue Troubleshooting Templates

## Batch & Queue Troubleshooting Record

```markdown
# Batch & Queue Troubleshooting Record

Case ID:
Owner:
Date:

## Work identity
Process / job / queue:
Item / correlation ID:
Expected trigger:
Expected completion:

## Lifecycle
| State | Expected | Actual | Evidence |
|---|---|---|---|

## First failed transition

## Backlog and throughput
Backlog size:
Oldest item age:
Arrival rate:
Processing rate:
Failure rate:
Retry rate:

## Retry and safety
Retry count:
Retry rule:
Idempotency known:
Duplicate side-effect risk:
Ordering requirement:

## Dependencies
| Dependency | Status | Evidence |
|---|---|---|

## Hypotheses
| Hypothesis | Test | Result | Keep / reject |
|---|---|---|---|

## Recovery action

## Validation
Original item:
New items:
Backlog trend:
Downstream result:

## Reusable lesson
```

## Replay decision

```markdown
Item / scope:
Previous attempt may have committed: yes | no | unknown
Idempotency proven: yes | no
Duplicate business risk:
Replay method:
Approval required:
Validation after replay:
```
