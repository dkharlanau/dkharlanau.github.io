---
name: data-discovery-mapping
description: Use when unfamiliar Excel, CSV, database, or application extracts must be understood and connected before migration, reconciliation, integration, reporting, or reusable processing. Profiles real values, finds candidate keys and relationships, proposes mappings with confidence, validates them on real rows, and produces a Data Discovery & Mapping Record. Do not use when approved mappings already exist and only reconciliation is needed.
---

# Data Discovery & Mapping

## Purpose

Learn the real structure and business relationships of unfamiliar datasets before creating mappings or reusable transformation logic.

## Use when

- Several files or extracts must be connected.
- Column names are inconsistent or weakly documented.
- A migration, interface, reconciliation, or report needs a mapping.
- Repeated manual file work should become a reusable data procedure.

## Do not use when

- Approved keys and mappings already exist and only comparison is required. Use `data-reconciliation`.
- The task is broad data governance rather than a concrete dataset relationship.
- Sensitive data cannot be processed under the available handling rules.

## Required inputs

- Representative datasets or extracts.
- Known business purpose and desired result.
- Any available dictionary, mapping, process context, or report definition.
- Sensitive-field handling restrictions.

## Workflow

1. Inventory datasets: source, time period, row count, columns, encoding, and refresh logic.
2. Define business grain for each dataset.
3. Profile every column: type, null rate, distinct count, common values, min/max, patterns, duplicates, and representative samples.
4. Separate confirmed business meaning from inferred meaning.
5. Find candidate keys and measure uniqueness, nulls, composite-key need, and stability.
6. Test relationships between candidate fields using value overlap and cardinality.
7. Identify transformations: formatting, code translation, units, concatenation, splitting, dates, defaults, filtering, aggregation, and enrichment.
8. Propose mappings with source, target, transformation, confidence, and evidence.
9. Validate mappings on real rows and measure matched, unmatched, duplicate, and ambiguous cases.
10. Classify exceptions: missing key, duplicate, unmapped code, format issue, timing issue, source defect, target rule, or unknown.
11. Ask domain owners only where data evidence cannot resolve business meaning.
12. Save approved keys, mappings, transformations, checks, and tolerances as reusable procedure inputs when work repeats.

## Decision rules

- Similar column names do not prove semantic equivalence.
- Do not accept a key before measuring uniqueness and null behavior.
- If a mapping needs many exceptions, challenge the relationship before adding rules.
- Record uncertain semantics and mapping confidence instead of hiding guesses inside code.
- Minimize sensitive data samples and do not copy unnecessary values into public artifacts.

## Output format

Produce a **Data Discovery & Mapping Record**:

```markdown
## Dataset inventory
| Dataset | Source | Grain | Rows | Time scope |
|---|---|---|---:|---|

## Column profile
| Dataset | Field | Type | Null % | Distinct | Pattern / notes |
|---|---|---|---:|---:|---|

## Candidate keys
| Dataset | Key | Unique % | Null % | Confidence |
|---|---|---:|---:|---|

## Relationships
| Left field | Right field | Cardinality | Match % | Evidence |
|---|---|---|---:|---|

## Mapping
| Source | Target | Transformation | Confidence | Evidence |
|---|---|---|---|---|

## Validation
Matched:
Unmatched:
Duplicates:
Ambiguous:

## Exception classes

## Open semantic questions

## Reusable procedure candidate
Keys:
Mappings:
Checks:
Tolerances:
```

## Quality gates

- [ ] Every dataset has grain and time scope.
- [ ] Key uniqueness and null behavior are measured.
- [ ] Relationships include cardinality and match evidence.
- [ ] Mapping hypotheses are separated from confirmed rules.
- [ ] Mappings are validated on real rows.
- [ ] Exceptions are classified.
- [ ] Reusable logic includes validation checks.

## References

- `references/method.md` — Profiling, key discovery, relationship testing, and confidence model.
- `references/templates.md` — Discovery record and mapping table.
- `references/examples.md` — Synthetic customer, order, reference-data, and multi-file cases.
