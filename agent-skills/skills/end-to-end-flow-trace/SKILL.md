---
name: end-to-end-flow-trace
description: Use when one business object, message, or transaction crosses several systems and teams disagree about where the failure occurred, or when an intermediate step reports success but the final business result is missing. Builds an identity chain and timeline, verifies every handoff, and routes the first failed boundary to a specialist skill. Produces an End-to-End Flow Trace Record.
---

# End-to-End Flow Trace

## Purpose

Trace one concrete business object across system boundaries and find the first handoff where evidence disappears, changes incorrectly, or no longer matches expected state.

## Use when

- A process crosses several applications, APIs, events, queues, or files.
- Source and target teams disagree about the failure location.
- An upstream system reports success but the final business outcome is missing.
- Identifiers change between systems and investigation loses continuity.

## Do not use when

- The failing boundary is already proven. Switch directly to the relevant specialist skill.
- The problem is fully inside one component with no cross-system handoff.
- You are designing a new integration rather than tracing a failed one.

## Required inputs

- One concrete business object, message, transaction, or case.
- Expected system path and final outcome.
- Known identifiers at each step.
- Approximate timestamps and time zone.
- Available logs, API traces, message records, files, or document history.

## Workflow

1. Select one representative trace object.
2. State the expected path from origin to final business state.
3. Build the identity chain: business key, source ID, message ID, correlation ID, target ID, and transformed identifiers.
4. Normalize timestamps and build a cross-system timeline.
5. For each boundary, verify relevant evidence for sent, received, transformed, accepted, queued, processed, committed, and acknowledged states.
6. Identify the first missing or incorrect transition.
7. Inspect mapping, filtering, enrichment, aggregation, splitting, deduplication, and reference-data behavior at that boundary.
8. For asynchronous handoffs, inspect retry, ordering, dead-letter, and acknowledgement evidence.
9. Compare with a known-good object when available.
10. Route the failure to `api-contract-troubleshooting`, `authorization-identity-diagnosis`, `batch-queue-troubleshooting`, `data-reconciliation`, `process-deviation-analysis`, or another relevant skill.
11. After correction, repeat the complete path and validate final business state.

## Decision rules

- A successful system status without outgoing boundary evidence does not prove a handoff.
- If identifiers change, map the relationship before continuing the trace.
- Normalize time zones before inferring causal order.
- Once the first failed boundary is proven, stop broad tracing and switch to a specialist skill.
- Do not replay the complete flow until duplicate and side-effect risk is understood.

## Output format

Produce an **End-to-End Flow Trace Record**:

```markdown
## Trace object
Business object:
Primary key:
Expected final result:

## Identity chain
| System / boundary | Identifier | Relationship to previous |
|---|---|---|

## Timeline and boundary evidence
| Step | Timestamp | Expected state | Actual state | Evidence |
|---|---|---|---|---|

## First failed boundary

## Transformation / handoff notes

## Known-good comparison

## Specialist skill routing
Skill:
Reason:

## Correction

## End-to-end validation
Final business result:

## Open questions
```

## Quality gates

- [ ] One concrete trace object anchors the investigation.
- [ ] Identifiers are connected across boundaries.
- [ ] Timestamps are normalized.
- [ ] Claimed successful handoffs have evidence.
- [ ] The first failed boundary is identified or missing evidence is explicit.
- [ ] Specialist routing happens after boundary isolation.
- [ ] Validation confirms the final business outcome.

## References

- `references/method.md` — Identity-chain and boundary-evidence model.
- `references/templates.md` — Trace record and handover template.
- `references/examples.md` — Synthetic API-to-queue, file-to-application, and multi-system cases.
