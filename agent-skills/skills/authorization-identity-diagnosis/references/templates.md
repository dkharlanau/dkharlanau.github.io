# Authorization & Identity Diagnosis Templates

## Authorization & Identity Diagnosis Record

```markdown
# Authorization & Identity Diagnosis Record

Case ID:
Owner:
Date:

## Requested action
Identity:
Environment:
Resource:
Action:
Timestamp:

## Expected access
Role / group / scope / claim / business rule:

## Authentication evidence
Mechanism:
Result:

## Effective identity
Entry identity:
Target identity:
Relevant claims / scopes / groups:

## Access-layer checks
| Layer | Expected | Actual | Evidence |
|---|---|---|---|

## Known-good comparison

## First failing rule

## Correction

## Risk / approval
Privileged access impact:
Segregation-of-duties impact:
Sensitive-data impact:
Approval owner:

## Validation
Original action result:
Negative test / unintended access check:

## Open questions

## Reusable lesson
```

## Security handover

```markdown
Requested action:
Effective identity:
Authentication status:
First failing access layer:
Evidence:
What was ruled out:
Requested security decision:
Risk if changed:
```
