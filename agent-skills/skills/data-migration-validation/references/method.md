# Data Migration Validation Method

## Validation layers

Validate migration at several layers:

1. Scope — the correct source population was selected.
2. Structure — target fields and formats can hold the intended data.
3. Population — eligible, excluded, loaded, rejected, missing, target-only, and duplicate records reconcile.
4. Identity — source and target keys map consistently.
5. Relationships — parent-child and reference links remain valid.
6. Transformation — mapping and derivation rules behave as approved.
7. Business values — critical fields and totals remain correct at compatible grain.
8. Business use — processes can consume the migrated data.

## Population equation

Do not force one universal equation when migration rules split or merge records. Instead define the expected population relationship for each object and transformation class.

## Risk-based sampling

Deterministic controls should cover the full population where possible. Sampling adds depth for cases such as:

- high-value records
- old historical records
- edge dates
- uncommon codes
- multilingual text
- complex relationships
- records with defaults or transformations

## Acceptance

A migration can be accepted with known exceptions when each exception has quantified impact, treatment, owner, and business acceptance. Unknown exceptions should not be hidden inside a generic rejection count.
