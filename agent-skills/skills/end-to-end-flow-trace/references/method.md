# End-to-End Flow Trace Method

## Trace model

Use one concrete object and follow it through boundaries:

Origin → outbound handoff → transport → inbound handoff → transformation → processing → commit → next boundary → final business state.

Each boundary should answer:

- What identifier exists here?
- What time did the object arrive and leave?
- What state was expected?
- What state was observed?
- What evidence proves the transition?

## Identity chain

Identifiers may change. Map relationships such as:

- order number → message ID
- message ID → correlation ID
- source key → transformed target key
- batch file name → load run ID
- external request ID → internal document ID

If the chain breaks, the investigation can easily jump to the wrong object.

## Timeline discipline

Normalize time zones and clock formats. Note known clock skew when relevant. Build causal theories only after timestamps are comparable.

## Boundary evidence

Useful evidence can include:

- request or message creation
- outbound acknowledgement
- gateway or broker trace
- mapping result
- inbound receipt
- queue state
- application log
- database or document commit
- generated downstream event

The exact tool depends on the domain. The reasoning does not.

## Routing rule

Once the first failing boundary is identified, stop scanning the full landscape. Switch to the smallest specialist skill that matches the failure type.
