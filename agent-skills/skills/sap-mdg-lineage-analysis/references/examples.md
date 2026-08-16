# Examples

## Synthetic Material example

A material exists globally and for Plant DE01. Plant DE02 is added with a loading-group value. The trace confirms the plant-grain entity, the staged value, rule result, approval, activation evidence, outbound material slice, local target identity, and finally outbound-delivery determination. If MDG active data is correct but the target material plant slice is stale, the first broken boundary is distribution/target processing, not workflow.

## Synthetic Supplier example

A supplier purchasing-organization attribute is approved centrally. The central record is correct, but a purchase order in a connected system still fails. Trace the supplier application-data grain, approval and activation, replication payload, key mapping, target supplier purchasing-organization record, then purchase-order proof. Do not reopen the MDG workflow when the evidence already shows the break is target-side mapping or persistence.
