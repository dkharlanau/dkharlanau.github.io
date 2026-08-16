# Data Migration Validation Examples

All examples are synthetic.

## Example 1 — Counts match, identity does not

Observed: source and target both contain 10,000 customer rows.

Evidence:
1. 120 target records use the wrong source-to-target identifier mapping.
2. Total count remains equal because all rows loaded.
3. Downstream orders cannot reference those customers correctly.

Diagnosis: population count passed, identity integrity failed.

## Example 2 — Expected exclusions

Observed: 800 source records do not exist in target.

Evidence:
1. Approved scope excludes inactive records older than the migration cutoff.
2. All 800 records match the exclusion rule.
3. No eligible record is missing.

Result: explained exclusion, not migration defect.

## Example 3 — Transformation defect

Observed: loaded quantities look correct but financial totals differ.

Evidence:
1. Source and target grain match.
2. Currency code mapping is correct.
3. One conversion rule uses an incorrect decimal scale for a subset of records.

Diagnosis: transformation defect.

Closure: correct rule, reload controlled population, rerun the same reconciliation.

## Example 4 — Business-use failure

Observed: technical validation passes for migrated products.

Evidence:
1. Required fields exist.
2. Counts and key mapping pass.
3. A critical business transaction rejects several products because a required relationship was not migrated.

Diagnosis: business usability and relationship integrity failed despite a successful load.
