# End-to-End Flow Trace Examples

All examples are synthetic.

## Example 1 — API accepted, queue failed

Observed: source application reports success but target record is missing.

Trace:
1. Source business object created.
2. API request accepted with tracking ID.
3. Queue message created from tracking ID.
4. Worker sends message to dead-letter state after repeated validation failure.

First failed boundary: asynchronous processing after API acceptance.

Next skill: `batch-queue-troubleshooting`.

## Example 2 — File loaded, records missing

Observed: source file contains 5,000 rows, target shows 4,820.

Trace:
1. File received and load run created.
2. 5,000 rows parsed.
3. 180 rows filtered by an undocumented code rule.
4. Target commit contains 4,820 records.

First failed expectation: transformation/filtering rule, not transport.

Next skill: `data-reconciliation` or `data-discovery-mapping`.

## Example 3 — Identifier chain breaks

Observed: target team cannot find the source order ID in its logs.

Trace:
1. Source order ID is transformed into a partner reference.
2. Message broker uses a separate correlation ID.
3. Target stores the partner reference, not the source order number.

Diagnosis: no processing failure. Investigation was searching with the wrong identifier.

Closure: document the identity chain in the interface runbook.
