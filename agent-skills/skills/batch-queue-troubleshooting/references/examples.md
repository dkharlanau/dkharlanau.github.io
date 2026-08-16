# Batch & Queue Troubleshooting Examples

All examples are synthetic.

## Example 1 — Queue grows, consumers healthy

Observed: backlog increases every hour.

Evidence path:
1. Consumers are running and processing successfully.
2. Processing rate is stable at 1,000 items/hour.
3. Arrival rate increased to 1,300 items/hour after a business volume change.

Diagnosis: capacity gap, not an application exception.

Closure: adjust capacity or processing design, then confirm backlog age decreases.

## Example 2 — One poison item blocks ordered processing

Observed: one partition stops while others continue.

Evidence path:
1. Same item fails repeatedly.
2. Strict ordering prevents later items in that partition from passing it.
3. Other partitions are healthy.

Diagnosis: poison item combined with ordering rule.

Closure: correct or safely isolate the item according to business rules, then validate ordered continuation.

## Example 3 — Job never starts

Observed: expected nightly work is missing.

Evidence path:
1. Unit of work is eligible.
2. No execution instance exists for the expected time.
3. Scheduler configuration was disabled during a maintenance change.

Diagnosis: scheduling transition failed before application execution.

## Example 4 — Work completed but message remains pending

Observed: business record exists, but the queue item is retried.

Evidence path:
1. Worker completed the business action.
2. Acknowledgement failed after the action committed.
3. Retry could create a duplicate side effect.

Diagnosis: completion/acknowledgement boundary.

Closure: do not blind-retry. Use idempotency or a controlled reconciliation before replay.
