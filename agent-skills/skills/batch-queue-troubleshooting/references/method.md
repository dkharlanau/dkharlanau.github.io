# Batch & Queue Troubleshooting Method

## State model

Represent asynchronous work as explicit states:

1. Created
2. Eligible
3. Scheduled or enqueued
4. Routed
5. Picked up
6. Executing
7. Retrying or waiting
8. Completed
9. Acknowledged or committed
10. Downstream result visible

The useful question is not "why is the queue broken?" but "what is the first transition that did not occur?"

## Delay model

For delay and backlog problems, capture:

- arrival rate
- processing rate
- backlog size
- age of oldest item
- failure rate
- retry rate
- number of active workers or consumers

If arrival rate remains higher than processing rate, the backlog can grow even when individual workers are healthy.

## Retry model

Before replay, determine:

- whether the operation is idempotent
- whether a stable idempotency key exists
- whether the previous attempt may have produced side effects
- retry count and delay
- maximum retry rule
- poison-message or dead-letter handling

A retry is a business action, not merely a technical button.

## Ordering and locking

Look for:

- strict ordering requirements
- predecessor dependency
- partition key hotspots
- locks or leases
- long-running items
- single-threaded sections
- acknowledgement blocked after successful work

## Recovery hierarchy

Prefer, in order:

1. correct the proven dependency or data issue
2. replay one controlled item
3. replay a bounded group
4. restart consumer or scheduler only when evidence points there
5. scale capacity when throughput evidence proves capacity is the issue

Avoid broad restarts and mass replay as first actions.
