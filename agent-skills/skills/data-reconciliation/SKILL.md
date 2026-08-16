---
name: data-reconciliation
description: Use when two or more files, extracts, tables, reports, migrations, or interface datasets should represent the same business population but do not match. Profile structure, validate keys, normalize comparison rules, classify exceptions, and prove the result with rerunnable controls. Produces a Data Reconciliation Record. Do not use when the main problem is a technical runtime failure rather than a data difference.
---

# Data Reconciliation

## Purpose

Compare datasets at the correct business grain, explain differences, and create rerunnable evidence.

## Use when

- Source and target counts or values differ.
- A migration, interface, report, or file load must be validated.
- Teams compare spreadsheets manually and recurring exceptions are not classified.
- Control totals match but record-level values do not.

## Do not use when

- The system or job is failing before data can be compared. Use `evidence-driven-troubleshooting`.
- The task is broad data governance rather than one reconciliation question.

## Required inputs

- Datasets or extracts.
- Business meaning and expected population.
- Candidate keys.
- Filters, time window, units, currencies, and business grain.
- Known mappings, transformations, and allowed tolerances.

## Workflow

1. State what should match and at which grain.
2. Profile columns, types, row counts, nulls, duplicates, and date ranges.
3. Normalize formats and approved transformations.
4. Validate key uniqueness, completeness, and relationship cardinality.
5. Compare structure and population.
6. Compare important values and control totals.
7. Classify source-only, target-only, duplicate, transformed, timing, mapping, source-defect, target-defect, and unknown exceptions.
8. Trace representative material exceptions end to end.
9. Define correction and ownership.
10. Re-run the same rules after correction.
11. Save stable keys, mappings, tolerances, and checks as a reusable procedure when the work repeats.

## Decision rules

- Do not compare totals until scope and grain are aligned.
- If no stable key exists, define a matching strategy before calculating exception counts.
- A duplicate on a supposed unique key is a separate data-quality issue.
- An allowed difference needs an explicit rule and tolerance.
- For large exception populations, classify first and sample by class.

## Output format

Produce a **Data Reconciliation Record** with dataset identity, scope, grain, keys, normalization rules, control totals, match statistics, exception classes, examples, causes, correction, and rerun evidence.

## Quality gates

- [ ] Business grain is explicit for every dataset.
- [ ] Key quality is measured before matching.
- [ ] Filters and time windows are aligned or explained.
- [ ] Exceptions are classified.
- [ ] Material differences are traceable.
- [ ] The reconciliation can be rerun after correction.

## References

- `references/method.md` — Reconciliation sequence and exception model.
- `references/templates.md` — Copy-ready reconciliation record.
- `references/examples.md` — File, migration, and reporting examples.

## Safety rules

- Do not expose sensitive source data in examples or outputs.
- Preserve original extracts before normalization or correction.
- Label assumptions about mappings, tolerances, and business grain.
