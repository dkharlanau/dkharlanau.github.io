# API Contract Troubleshooting Templates

## API Contract Troubleshooting Record

```markdown
# API Contract Troubleshooting Record

Case ID:
Owner:
Date:

## Exchange identity
Caller:
Provider:
Environment:
Endpoint:
Method:
Timestamp:
Correlation / trace ID:

## Expected exchange
Contract version:
Required headers:
Expected request shape:
Expected response shape:
Expected business result:

## Observed failure
HTTP status:
Error summary:
Request summary:
Response summary:

## Boundary classification
client | identity | routing | transport | schema | provider | downstream | consumer | unknown

## Evidence
| Evidence | Location / ID | Observation |
|---|---|---|

## Hypotheses
| Hypothesis | Test | Result | Keep / reject |
|---|---|---|---|

## First broken contract

## Correction

## Retry and side-effect risk

## Validation
Technical result:
Business result:
Known-good comparison:

## Open questions

## Reusable lesson
```

## Handover block

```markdown
Problem:
First failing boundary:
Evidence collected:
What was ruled out:
Current hypothesis:
Risk of replay:
Next owner:
Exact next check:
```
