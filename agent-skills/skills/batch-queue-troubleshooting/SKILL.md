---
name: batch-queue-troubleshooting
description: Use when scheduled jobs, queues, asynchronous workers, retries, or background processing are delayed, stuck, failing, or producing duplicates. Traces the unit of work through creation, eligibility, enqueue, pickup, execution, retry, acknowledgement, and completion. Produces a Batch & Queue Troubleshooting Record. Do not use when the failure is still inside a synchronous API exchange.
---

# Batch & Queue Troubleshooting

## Purpose

Find the first failed state transition in scheduled or asynchronous processing and recover work without creating duplicate or unsafe side effects.

## Use when

- A scheduled job did not run or completed without the expected result.
- A queue grows or messages remain pending.
- A worker repeatedly fails the same item.
- Retries create duplicate work or delayed business processing.
- One partition, consumer, object, or time window differs from healthy processing.

## Do not use when

- The failure is still a synchronous request/response problem. Use `api-contract-troubleshooting`.
- The task is only to design monitoring. Use `integration-observability`.
- The business process itself took the wrong route before work was queued. Use `process-deviation-analysis`.

## Required inputs

- Job, queue, topic, subscription, worker, or process identity.
- Unit of work or failing item identifier.
- Expected trigger or schedule and expected completion state.
- Timestamp and lifecycle status.
- Logs, retry history, dependency evidence, and recent changes when available.
- Retry, timeout, ordering, idempotency, and dead-letter rules when known.

## Workflow

1. Define the unit of work and successful completion state.
2. Map lifecycle states from creation to completion.
3. Confirm the item was created and was eligible for processing.
4. Confirm schedule, event, enqueue, routing, partition, priority, or destination.
5. Confirm whether a worker or job instance picked up the item.
6. Capture the first execution error, timeout, validation issue, business exception, or dependency failure.
7. Record retry count, retry delay, backoff, dead-letter behavior, and whether replay is safe.
8. Check locks, ordering, serialization, partition hotspots, and blocked predecessors.
9. Check completion, commit, acknowledgement, status update, and next-event publication.
10. Compare lifecycle timestamps with a healthy item.
11. Recover using the smallest safe replay or correction after duplicate risk is understood.
12. Validate the failed item, new items, downstream state, backlog trend, and throughput.

## Decision rules

- If the unit of work is never created, investigate upstream trigger or business rules rather than queue internals.
- If queued work is never picked up, inspect consumers, routing, capacity, locks, and subscriptions before application logic.
- If one item blocks others, isolate poison-message or ordering behavior before increasing capacity.
- Do not mass-retry until idempotency and duplicate side effects are understood.
- If backlog grows while throughput is stable, compare arrival rate with processing capacity.
- If business work completes but the item remains open, inspect acknowledgement, commit, status update, or next-step publication.

## Output format

Produce a **Batch & Queue Troubleshooting Record**:

```markdown
## Work identity
Process / job / queue:
Item / correlation ID:
Expected trigger:
Expected completion:

## Lifecycle
| State | Expected time | Actual time | Evidence |
|---|---|---|---|

## First failed transition

## Backlog and throughput
Backlog:
Arrival rate:
Processing rate:
Oldest item:

## Retry behavior
Retry count:
Backoff:
Dead-letter state:
Idempotency known: yes | no
Duplicate side-effect risk:

## Dependencies

## Recovery action

## Validation
Failed item:
New items:
Backlog trend:
Downstream business result:

## Open questions
```

## Quality gates

- [ ] Unit of work and lifecycle are explicit.
- [ ] The first failed transition is identified or evidence gaps are listed.
- [ ] Retry history is known before replay.
- [ ] Idempotency, duplicate, ordering, and lock risks are considered.
- [ ] Backlog and throughput are measured when delay is the symptom.
- [ ] Validation covers both the original item and continuing flow health.

## References

- `references/method.md` — Lifecycle, throughput, retry, and recovery model.
- `references/templates.md` — Troubleshooting record and replay decision template.
- `references/examples.md` — Synthetic stuck queue, poison item, capacity, and acknowledgement cases.
