# Data Discovery & Mapping Examples

All examples are synthetic.

## Example 1 — Customer files with different identifiers

Observed: one file contains `customer_no`, another contains `account_id`.

Discovery:
1. Both fields are unique and non-null.
2. Direct value overlap is zero.
3. A third reference table maps `customer_no` to `account_id` one-to-one.

Mapping: valid through the reference table, not by direct equality.

## Example 2 — False key candidate

Observed: `email` looks like a natural customer key.

Discovery:
1. Null rate is 4%.
2. Several households share one email address.
3. Historical records show email changes over time.

Conclusion: email is useful matching evidence but not a stable primary key.

## Example 3 — Order header and item grain mismatch

Observed: source has 1,000 rows and target has 3,420 rows.

Discovery:
1. Source is one row per order.
2. Target is one row per order item.
3. `order_id` is one-to-many from source to target.

Conclusion: row-count mismatch is expected because grain differs. Reconciliation must aggregate or compare at compatible grain.

## Example 4 — Reusable procedure candidate

Observed: monthly CSV files arrive with the same structure and the same code translation.

Discovery result:
- stable composite key confirmed
- code mapping table approved
- date normalization rule confirmed
- exception classes stable

Next step: save keys, mapping table, transformations, and validation checks as a reusable data procedure.
