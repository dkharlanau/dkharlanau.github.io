# Configuration Drift Analysis Templates

## Configuration Drift Analysis Record

```markdown
# Configuration Drift Analysis Record

Case ID:
Owner:
Date:

## Scenario
Failing environment:
Known-good environment:
Same input / case:
Expected behavior:
Observed behavior:

## Comparison scope

## Effective-state diff
| Layer | Failing state | Known-good state | Relevance | Evidence |
|---|---|---|---|---|

## Version diff

## Configuration diff

## Identity / reference diff

## Dependency diff

## Data-condition diff

## Candidate causes
| Candidate | Reason | Test | Result | Keep / reject |
|---|---|---|---|---|

## Proven causal difference

## Source of truth

## Correction

## Validation

## Prevention / drift control
```

## Controlled diff block

```markdown
Difference:
Layer:
Why it can affect the scenario:
Recent change evidence:
Safe test:
Result:
Causal status: proven | rejected | unresolved
```
