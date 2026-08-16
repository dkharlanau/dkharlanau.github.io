# Examples

## Duplicate external request
Detect idempotency key reuse, return prior result where safe, and avoid a second business posting.

## Missing reference data
Hold the transaction with visible reason and owner; do not retry every five minutes forever.

## Partial downstream completion
Reconcile authoritative state before choosing compensation or replay.