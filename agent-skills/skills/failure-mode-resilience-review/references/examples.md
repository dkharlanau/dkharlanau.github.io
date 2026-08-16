# Examples

All examples are synthetic.

## Example 1: asynchronous order confirmation
A sales order is accepted by an API and forwarded through a queue. The queue is available but the consumer stops.

Failure mode: backlog grows while the caller still receives success.

Detection gap: API availability remains green. Improvement: add age-of-oldest-message and business confirmation lag metrics. Recovery: restart consumer, then replay only unprocessed messages using idempotency keys.

## Example 2: duplicate batch restart
A nightly batch writes financial adjustments. The job fails after writing 70% of records and is restarted from the beginning.

Risk: duplicate adjustments. Required resilience design: checkpoint or restart-safe key, reconciliation before retry, and stop condition when completion state is uncertain.

## Example 3: identity dependency
A service depends on an identity provider. Token refresh fails intermittently.

Effect: users see random authorization errors. Detection: token refresh failure metric plus 401 trend. Recovery: controlled token renewal and escalation, not repeated business transactions.

## Example 4: configuration drift
A feature flag differs between two environments and changes routing logic.

The component is healthy, but messages go to the wrong downstream path. This is a resilience issue because configuration state is a dependency and the business outcome is wrong even without an outage.
