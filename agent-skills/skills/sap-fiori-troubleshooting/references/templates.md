# Templates

## Fiori Troubleshooting Record

```markdown
---
artifact: Fiori Troubleshooting Record
id: FIORI-001
date: YYYY-MM-DD
owner: Name / Team
status: open | isolated | fixed | validated
---

## Case
App:
System / client:
User:
Timestamp:
Business process:

## Symptom
Observed:
Expected:
Working comparison:

## Launch identity
Semantic object / action:
Launchpad content / role:
Target system / alias:

## Browser evidence
Console error:
Failed or slow request:
HTTP method:
HTTP status:
Response:
Request / correlation ID:

## Layer classification
launchpad | ui | service | gateway | backend | authorization | cache | performance | platform | unknown

## SAP evidence
/IWFND/ERROR_LOG result:
/IWBEP/ERROR_LOG result:
Application log / dump / document evidence:
Authorization evidence:

## Recent changes

## Hypotheses tested
1. Hypothesis:
   Test:
   Evidence:
   Result: keep | reject

## Root cause or failing layer

## Action
Containment:
Fix:
Risk / rollback:
Owner:

## Validation
Original case retested:
Network result:
Business result:
Regression check:

## Reusable lesson
Next skill / runbook update:
```

## Compact evidence table

```markdown
| Layer | Check | Evidence | Result | Owner / next step |
|---|---|---|---|---|
| Launchpad | Intent / role / target mapping |  |  |  |
| Browser | Console |  |  |  |
| Network | Failed or slow request |  |  |  |
| Gateway | Frontend/backend error log |  |  |  |
| Backend | Business/app evidence |  |  |  |
| Authorization | Failed authorization evidence |  |  |  |
| Cache | Stale resource/version evidence |  |  |  |
| Validation | Original case repeated |  |  |  |
```

## Handoff note

```markdown
### Failing layer

### Evidence

### Question for owner

### Business impact

### Containment already applied

### What has been ruled out
```
