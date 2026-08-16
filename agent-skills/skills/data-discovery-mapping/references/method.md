# Data Discovery & Mapping Method

## Dataset grain

Before matching fields, define what one row represents. Examples:

- one customer
- one order header
- one order item
- one daily balance
- one event
- one product-location combination

Many bad mappings begin by comparing datasets with different grain.

## Column profiling

Measure at least:

- inferred type
- null count and rate
- distinct count
- duplicate frequency
- common values
- min and max where meaningful
- length and format patterns
- representative samples

Do not infer business meaning from the field name alone.

## Candidate-key test

For every key candidate check:

- uniqueness
- null behavior
- stability across time
- composite-key requirement
- technical versus business meaning
- whether the value is transformed between systems

## Relationship test

For candidate relationships measure:

- value overlap
- unmatched left values
- unmatched right values
- one-to-one, one-to-many, many-to-one, or many-to-many cardinality
- duplicate impact

## Mapping confidence

Use simple confidence labels:

- High: meaning confirmed and data behavior supports it.
- Medium: strong data evidence but business meaning still needs confirmation.
- Low: mainly inferred from names or weak samples.

## Reusable-procedure handoff

A mapping becomes reusable only when it includes:

- input identity
- keys
- transformations
- filters
- mapping tables
- validation checks
- exception classes
- tolerance rules

Transformation without validation is only automated uncertainty.
