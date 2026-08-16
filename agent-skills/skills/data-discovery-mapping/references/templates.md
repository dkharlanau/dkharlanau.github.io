# Data Discovery & Mapping Templates

## Data Discovery & Mapping Record

```markdown
# Data Discovery & Mapping Record

Case ID:
Owner:
Date:

## Dataset inventory
| Dataset | Source | Grain | Rows | Time scope | Refresh |
|---|---|---|---:|---|---|

## Column profile
| Dataset | Field | Type | Null % | Distinct | Sample pattern | Meaning status |
|---|---|---|---:|---:|---|---|

## Candidate keys
| Dataset | Key | Unique % | Null % | Stability | Confidence |
|---|---|---:|---:|---|---|

## Relationships
| Left | Right | Cardinality | Match % | Confidence | Evidence |
|---|---|---|---:|---|---|

## Mapping
| Source field | Target field | Transformation | Confidence | Evidence / owner |
|---|---|---|---|---|

## Validation statistics
Matched:
Source only:
Target only:
Duplicates:
Ambiguous:

## Exception classes
| Class | Count | Example pattern | Action |
|---|---:|---|---|

## Open semantic questions

## Reusable procedure candidate
Input rules:
Keys:
Mappings:
Transformations:
Checks:
Tolerances:
```

## Mapping review block

```markdown
Mapping:
Evidence:
Confidence: high | medium | low
Known exceptions:
Business confirmation needed:
Validation test:
```
