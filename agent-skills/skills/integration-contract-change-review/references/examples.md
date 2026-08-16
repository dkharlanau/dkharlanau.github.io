# Examples

All examples are synthetic.

## Example 1: new status value
An order event keeps the same schema but adds a new status value `PARTIALLY_CONFIRMED`.

Risk: consumers with closed value mappings may reject or misclassify the event. Classification: conditionally compatible or breaking depending on consumer behaviour. Review requires consumer inventory and test evidence.

## Example 2: optional field with strict consumer
A producer adds an optional JSON field. One legacy consumer rejects unknown properties.

Result: syntactically additive does not mean operationally compatible. Use tolerant-reader fix or staged producer rollout after consumer update.

## Example 3: changed retry policy
An API client changes from one retry to five automatic retries for timeout errors.

Risk: non-idempotent create operations may execute multiple times. Contract review must include idempotency and provider-side duplicate handling.

## Example 4: semantic break without schema change
A field called `requestedDate` changes from customer-requested date to calculated promise date while name and type stay identical.

Result: semantic breaking change. Introduce a new field or version unless all consumers can coordinate the meaning change safely.
