---
name: data-migration-validation
description: Use when master, transactional, reference, or historical data is moved between systems and the migration must be proven complete, correct, relationally consistent, and usable by business processes. Reconciles source scope, target population, keys, transformations, exceptions, and business-use tests. Produces a Data Migration Validation Record. Do not use when no migration has occurred and only normal dataset comparison is needed.
---

# Data Migration Validation

## Purpose

Prove that the intended business population survived migration with correct identity, relationships, transformations, values, and process usability.

## Use when

- A mock, rehearsal, cutover, or post-go-live migration load needs validation.
- Technical load counts are green but business correctness is not proven.
- Data is filtered, transformed, defaulted, deduplicated, split, or merged during migration.
- Business acceptance needs traceable evidence.

## Do not use when

- There is no migration and only two datasets need comparison. Use `data-reconciliation`.
- Keys and mappings are still unknown. Use `data-discovery-mapping` first.
- The task is only technical loader troubleshooting.

## Required inputs

- Migration scope and business objects.
- Source and target extracts or controlled samples.
- Approved mappings, keys, filters, transformations, and defaults.
- Expected population, time scope, and business grain.
- Critical business scenarios that consume the migrated data.

## Workflow

1. Define the validation contract: eligible population, allowed exclusions, target outcome, and acceptance conditions.
2. Freeze source scope with extraction time, filters, row counts, and data version.
3. Validate target structure and mandatory fields.
4. Reconcile eligible, excluded, loaded, rejected, missing, target-only, and duplicate populations.
5. Validate source-to-target identity mapping and parent-child or reference relationships.
6. Validate transformations such as code mapping, defaults, units, dates, currencies, splitting, aggregation, and derivation.
7. Compare business-critical values and control totals at compatible grain.
8. Classify every material exception.
9. Run critical business-use tests with migrated data.
10. Sample risk-based edge cases in addition to deterministic controls.
11. Correct defects and rerun the same controls.
12. Record remaining exceptions, owners, acceptance, and post-go-live controls.

## Decision rules

- Equal row counts do not prove correctness when records can be split, merged, filtered, or deduplicated.
- Compare at business grain before comparing totals.
- If identity mapping is unstable, stop value reconciliation until keys are resolved.
- A rejected record is acceptable only when reason, owner, and treatment are known.
- Technical load success does not replace business-use validation.
- For large populations, combine deterministic controls with risk-based sampling.

## Output format

Produce a **Data Migration Validation Record**:

```markdown
## Migration scope
Objects:
Source freeze timestamp:
Source filters:
Target load / run:

## Population reconciliation
| Class | Count | Expected? | Explanation |
|---|---:|---|---|

## Key and relationship controls
| Control | Expected | Actual | Status |
|---|---|---|---|

## Transformation controls
| Rule | Sample / population | Result | Evidence |
|---|---|---|---|

## Business value controls

## Exceptions
| Class | Count | Owner | Treatment |
|---|---:|---|---|

## Business-use tests
| Scenario | Result | Evidence |
|---|---|---|

## Acceptance
Remaining risks:
Owner:
Decision:

## Rerun evidence
```

## Quality gates

- [ ] Source scope and extraction point are reproducible.
- [ ] Population classes are reconciled and explained.
- [ ] Identity and relationship integrity is measured.
- [ ] Transformations are tested with real records.
- [ ] Business-use tests prove migrated data is usable.
- [ ] Exceptions have owner and treatment.
- [ ] Corrections can be rerun with the same controls.

## References

- `references/method.md` — Migration control model and risk-based validation.
- `references/templates.md` — Migration validation and acceptance templates.
- `references/examples.md` — Synthetic master-data, transaction, relationship, and transformation cases.
