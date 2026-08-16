# Data Migration Validation Templates

## Data Migration Validation Record

```markdown
# Data Migration Validation Record

Case ID:
Owner:
Date:

## Scope
Business objects:
Source system / extract:
Target system / load:
Source freeze timestamp:
Filters:

## Population
| Class | Count | Expected? | Explanation |
|---|---:|---|---|

## Keys and relationships
| Control | Expected | Actual | Status | Evidence |
|---|---|---|---|---|

## Transformations
| Rule | Population / sample | Expected | Actual | Status |
|---|---|---|---|---|

## Critical values and totals

## Exceptions
| Class | Count | Impact | Owner | Treatment |
|---|---:|---|---|---|

## Business-use tests
| Scenario | Result | Evidence | Owner |
|---|---|---|---|

## Acceptance
Remaining exceptions:
Risk acceptance:
Decision owner:
Decision:

## Rerun evidence
```

## Migration acceptance block

```markdown
Population reconciled: yes | no
Key integrity proven: yes | no
Relationship integrity proven: yes | no
Critical transformations proven: yes | no
Business-use scenarios passed: yes | no
Known exceptions:
Open risks:
Decision: accept | conditional accept | reject
Owner:
```
