# How to Design Resilience and Disaster Recovery for SAP Integrations Without Creating Duplicate Business Transactions

An integration platform becomes unavailable.

Orders continue arriving from customers.

Warehouse confirmations stop reaching SAP.

Payment files wait on a server.

After two hours, the platform is restored.

The operations team sees a backlog and starts reprocessing messages.

Most transactions complete.

Some customer orders are created twice.

One payment is posted twice.

Several warehouse confirmations are processed in the wrong sequence.

A delivery that had already been cancelled becomes active again because an older message was replayed.

The technical recovery succeeded.

The business recovery failed.

This is the uncomfortable part of integration resilience.

Restoring servers, brokers, queues and network connections is only one part of the work.

The real task is to restore a trustworthy business state.

A resilient SAP integration architecture must answer:

- Which transactions were received before the outage?
- Which were committed in SAP?
- Which responses were lost?
- Which events were published?
- Which consumers processed them?
- Which messages can be retried safely?
- Which actions require business verification?
- Which old messages have already been superseded?
- When is the business process truly recovered?

SAP currently positions SAP Integration Suite as supporting mission-critical integration through centralized governance, real-time monitoring, built-in security, hybrid connectivity and resilient asynchronous event distribution. SAP describes Event Mesh as providing reliable asynchronous communication and advanced event mesh as supporting distributed brokers and resilient event delivery across environments.

Those capabilities provide infrastructure.

They do not decide whether replaying one message will create a second invoice.

That remains an architecture and business-control responsibility.

### Availability is not the same as resilience

A system is available when users or applications can reach it.

A process is resilient when it can:

- continue under partial failure;
- preserve business intent;
- avoid uncontrolled duplication;
- recover incomplete work;
- restore a consistent state;
- explain what happened.

An integration endpoint may be available while the target ERP is not.

A message broker may be available while one consumer is failing.

SAP may be available while the network connection to a warehouse is interrupted.

A resilient architecture assumes that failures will be partial.

The whole landscape will rarely fail in one clean, visible way.

### Disaster recovery is not only an infrastructure exercise

Traditional disaster recovery planning often focuses on:

- backup;
- secondary region;
- system restoration;
- database recovery;
- network failover;
- platform access.

These areas are necessary.

NIST contingency-planning guidance treats recovery as part of a broader process that begins with understanding system and operational requirements, priorities and organizational resilience needs.

For integration architecture, this means the recovery target cannot be defined only as:

> Integration Suite is available again.

The target should be closer to:

> Critical business transactions are processing through a controlled path, their status is known, and no transaction will be lost or repeated without detection.

### Four layers must recover

A useful recovery model separates four layers.

### 1. Platform recovery

Restore:

- integration runtime;
- API gateway;
- event broker;
- connectivity;
- certificates;
- secrets;
- monitoring;
- deployment access.

### 2. Message recovery

Determine:

- which messages are waiting;
- which were delivered;
- which failed;
- which acknowledgements were lost;
- which files remain unprocessed;
- which events need replay.

### 3. Business-object recovery

Verify:

- which SAP documents exist;
- whether they are complete;
- whether duplicates exist;
- whether downstream objects were created;
- which business state is authoritative.

### 4. Process recovery

Restore the complete service.

For an order process, that may mean:

- order accepted;
- SAP order created;
- fulfilment request received;
- delivery processing resumed;
- customer status corrected.

Recovering only the first layer leaves the most dangerous questions unanswered.

## Begin with business criticality

Not every integration requires the same recovery design.

A product-description feed and a payment-posting interface have different consequences.

Classify integration services based on business impact.

### Critical transactional flows

Examples:

- customer orders;
- payments;
- financial postings;
- goods movements;
- production instructions;
- urgent warehouse execution.

These normally require:

- durable transaction identity;
- strong duplicate protection;
- controlled replay;
- detailed reconciliation;
- tested recovery procedures.

### Important operational flows

Examples:

- delivery status;
- supplier replication;
- inventory updates;
- order confirmations.

Delay may be tolerated for a limited period, but missing or incorrect processing still causes material impact.

### Informational flows

Examples:

- analytics;
- noncritical notifications;
- reporting extracts;
- document indexing.

These may accept longer recovery times and simpler replay.

Do not give every interface the most expensive architecture.

Do not give every interface the same weak recovery procedure either.

## Define RTO and RPO in business terms

Two common recovery concepts are:

### Recovery Time Objective

How long the service may remain unavailable before the impact becomes unacceptable.

### Recovery Point Objective

How much recent data or processing state may be lost.

For integration services, these definitions need business interpretation.

### Weak RTO

> Middleware must recover within two hours.

### Stronger RTO

> New customer orders must be accepted through the primary or approved fallback channel within 30 minutes. Orders waiting during the disruption must receive a reliable disposition within two hours.

### Weak RPO

> We may lose five minutes of integration data.

### Stronger RPO

> No accepted payment instruction may be permanently lost. Any uncertain payment transaction must be identified and reconciled before processing resumes.

The business may tolerate delayed warehouse status.

It may not tolerate one lost payment.

A generic platform RTO and RPO cannot represent every integration.

## Map the critical path

For each critical process, document the complete path.

For example:

```text
Customer channel
→ API gateway
→ Integration flow
→ SAP S/4HANA
→ Business event
→ Warehouse consumer
→ Warehouse system
```

At each boundary, define:

- transaction identifier;
- durable state;
- acknowledgement;
- timeout;
- retry owner;
- duplicate protection;
- reconciliation evidence.

The architecture should show where the business transaction becomes durable.

### Durability is not the same as business completion

An API gateway may accept a request.

An integration queue may persist it.

SAP may create a document.

These are different durability points.

For an order:

1. channel sent the request;
2. gateway received it;
3. integration persisted it;
4. SAP committed the order;
5. warehouse accepted fulfilment.

Each point answers a different recovery question.

A system should not tell the customer that the order exists merely because the request entered a queue.

## The most dangerous state is an uncertain outcome

Consider an order-creation API.

The caller sends the request.

SAP creates the sales order.

Before the response returns, the connection times out.

The caller sees a failure.

SAP contains a valid order.

If the caller retries without control, a duplicate order may be created.

This is not a theoretical edge case.

It is a standard distributed-system condition.

A timeout means:

> The caller does not know the final result.

It does not mean:

> The target did nothing.

### Model uncertainty explicitly

Possible transaction states should include:

- not received;
- accepted;
- processing;
- completed;
- rejected;
- uncertain;
- duplicate prevented;
- reconciliation required.

Do not map every timeout to `FAILED`.

A failed technical response and a failed business action are not the same thing.

### Provide a status lookup

A transactional interface should allow the caller or recovery process to query by:

- idempotency key;
- external request ID;
- correlation ID;
- business reference.

The recovery sequence becomes:

1. request times out;
2. caller checks transaction status;
3. existing result is returned where available;
4. retry occurs only when non-execution can be established.

This is safer than blind resubmission.

## Idempotency is the foundation of safe recovery

An operation is idempotent when processing the same business request repeatedly produces the same intended final effect as processing it once.

AWS architecture guidance notes that retries should be used for transient failures and that operations should be idempotent when retried; otherwise partial or repeated updates can corrupt system state. It also warns that frequent retries can overload an already degraded service.

For SAP integrations, idempotency should be considered at three levels.

### Message idempotency

Has this exact message ID already been processed?

This protects against technical redelivery of the same message.

### Request idempotency

Has this business request key already been accepted?

Example:

```text
Source system: COMMERCE-EU
External order ID: WEB-873004
Operation: CREATE_ORDER
```

This protects against a new technical message representing the same request.

### Business idempotency

Does the required business result already exist?

For example:

- does an SAP order already reference this customer purchase order?
- has this delivery already been goods-issued?
- has this payment already been posted?
- has this event version already updated the target?

This is the strongest control.

A new message ID should not bypass an existing business result.

### Do not depend only on middleware deduplication

Middleware duplicate detection is useful.

It may not protect against:

- replay with a new message ID;
- repeated source submission;
- manual reprocessing;
- a transaction sent through a fallback channel;
- old and new interfaces operating simultaneously.

Duplicate protection should exist near the business effect.

For a financial posting, the target or owning domain should be able to detect whether the business instruction has already been executed.

## Retry only what may improve

A retry is appropriate when the failure is likely to be temporary.

Examples:

- temporary network loss;
- service unavailable;
- rate limit;
- database lock;
- short-lived target maintenance.

A retry is usually not useful for:

- invalid customer;
- unknown material;
- missing mapping;
- rejected business rule;
- incompatible schema;
- cancelled document;
- expired contract.

Retrying permanent errors creates noise and backlog.

### Use error categories

A practical model may include:

#### Transient technical

Retry automatically with limits.

#### Persistent technical

Escalate after limited retries.

Examples:

- missing certificate;
- incompatible endpoint;
- configuration defect.

#### Data error

Route to the responsible data owner.

#### Business validation

Return or route for business correction.

#### Business decision

Create a task or approval.

#### Uncertain outcome

Check business state before retry.

### Use backoff and jitter

Immediate repeated retries can intensify an outage.

When many integrations retry simultaneously, the recovering target may receive more traffic than it handled before the failure.

A safer retry policy uses:

- increasing delay;
- randomized timing;
- maximum retry count;
- total retry window;
- circuit breaker;
- queue-based buffering.

The purpose is not only to make the call succeed.

It is to avoid turning a temporary failure into a larger outage.

### Retry ownership must be clear

Retry may occur in:

- source application;
- API client;
- API gateway;
- middleware;
- queue consumer;
- target adapter;
- operator tool.

If every layer retries independently, one original request may produce many attempts.

The architecture should define one primary retry owner for each boundary.

Other layers should either fail fast or use tightly controlled behaviour.

## Circuit breakers protect the recovering system

A circuit breaker stops repeated calls to a target that is clearly failing.

This can prevent:

- thread exhaustion;
- connection saturation;
- growing timeout chains;
- overload during target recovery.

A circuit breaker should expose clear states:

- closed: calls allowed;
- open: calls blocked;
- half-open: limited test traffic allowed.

The business process still needs a fallback decision.

Possible actions include:

- queue the request;
- reject temporarily;
- switch to read-only mode;
- use an approved alternate process;
- inform the user that confirmation is pending.

A circuit breaker is a technical protection.

It is not a complete business-continuity strategy.

## Queues provide resilience but create backlog risk

Persistent queues allow producers and consumers to operate independently.

They can:

- absorb temporary outages;
- smooth traffic peaks;
- preserve work;
- enable asynchronous recovery.

SAP describes its event-driven integration capabilities as supporting reliable asynchronous communication, distributed event delivery and visibility across event flows.

But a queue can hide a business outage.

The source continues accepting transactions.

The target processes nothing.

The backlog grows silently.

### Monitor age, not only count

A queue of 20,000 messages may be normal.

One high-priority order waiting four hours may be unacceptable.

Monitor:

- oldest message age;
- backlog by business priority;
- arrival rate;
- processing rate;
- estimated clearance time;
- retry count;
- dead-letter count;
- business value in backlog.

### Define admission control

During a long outage, should the source continue accepting unlimited work?

Sometimes yes.

Sometimes the company should:

- restrict low-priority requests;
- stop optional processing;
- inform users of delayed confirmation;
- activate a fallback process;
- refuse transactions that cannot be honoured safely.

Unlimited buffering can move the outage from one system to another.

It can also create a recovery peak too large for the target to clear.

## Backpressure is a business decision

Backpressure reduces or stops incoming work when downstream capacity is insufficient.

Technical options include:

- throttling;
- rate limiting;
- queue limits;
- slower polling;
- temporary rejection;
- priority queues.

The correct response depends on the business process.

For example:

- marketing updates may wait;
- customer orders may enter a controlled backlog;
- real-time stock promises may need to stop;
- payments may require secure acceptance but delayed posting;
- warehouse execution may need an emergency manual channel.

Backpressure should be connected to service policy.

It should not appear only when a queue reaches its technical limit.

## Disaster recovery needs an active-state model

When a secondary runtime or region becomes active, the architecture must know:

- which platform instance is authoritative;
- which consumers are running;
- which queues are active;
- where new messages are sent;
- whether the old instance may still process work;
- how split-brain is prevented.

### Avoid two active writers without coordination

If primary and recovery environments both process the same input, they may create duplicate business effects.

Examples:

- two SAP orders;
- two invoices;
- repeated supplier extensions;
- duplicate customer notifications.

Failover should define one active execution authority for each operation.

Active-active infrastructure is not the same as uncontrolled active-active business processing.

### Use fencing

Fencing prevents an old or isolated component from continuing to write after authority has moved.

Possible controls include:

- lease or leadership token;
- environment-specific write permission;
- routing switch;
- disabled credentials;
- queue ownership;
- epoch number;
- recovery-mode flag.

A recovered primary should not automatically resume processing until the architecture confirms that the secondary is no longer active.

### Record the execution epoch

A recovery environment may use an incremented execution generation or epoch.

Transactions can record:

- environment;
- recovery generation;
- processing timestamp;
- active authority.

This helps diagnose whether the same request was processed across two recovery periods.

## Failover and failback are different risks

Failover moves processing away from the failed environment.

Failback returns processing to the normal environment.

Failback is often less rehearsed.

It may create:

- duplicate queues;
- different configuration versions;
- missing reconciliation data;
- stale mappings;
- message-order changes;
- active consumers in both locations.

The failback plan should include:

1. stop or drain the recovery path;
2. reconcile completed work;
3. transfer remaining durable state where required;
4. verify configuration and schema versions;
5. activate the normal path;
6. monitor duplicate and sequence controls;
7. retain recovery evidence.

Do not treat failback as simply reversing a DNS or routing change.

## Configuration is part of the recoverable state

An integration runtime is not useful without the correct:

- flows;
- routes;
- mappings;
- certificates;
- credentials;
- partner profiles;
- API policies;
- event subscriptions;
- queue definitions;
- alert rules.

The recovery architecture should define how these assets are:

- versioned;
- backed up or reproducible;
- deployed;
- verified;
- synchronized between environments.

SAP Cloud Integration supports designing, managing and monitoring integration flows across application, B2B and government scenarios, while Integration Suite supports centralized governance across cloud and hybrid landscapes.

The company still needs its own deployment and recovery discipline.

### Prefer reproducible deployment over manual reconstruction

Recovery should not depend on an administrator remembering:

- which mapping file was active;
- which certificate alias was used;
- which retry count was configured;
- which partner exception was applied.

Use controlled repositories and deployment automation where possible.

The target environment should be built from known versions.

### Runtime data also matters

Infrastructure-as-code and integration artifacts do not preserve:

- queued messages;
- processed-event IDs;
- idempotency records;
- correlation state;
- workflow progress;
- dead-letter queues;
- replay decisions.

These are operational data.

The disaster-recovery design should state which of them must survive and how.

## Idempotency storage is a critical recovery dependency

Suppose the integration runtime is restored, but its processed-message registry is lost.

Old messages are replayed.

The system no longer knows they were processed before the outage.

This can create duplicate business transactions.

The idempotency store may require a stronger recovery design than ordinary technical logs.

Define:

- retention period;
- replication;
- recovery point;
- business key;
- behaviour when the store is unavailable.

### Do not fail open for high-risk operations

If duplicate-control storage is unavailable, should the interface continue?

For a low-risk notification, perhaps.

For a payment or goods movement, probably not.

A safe design may:

- stop the operation;
- queue the request;
- require status verification;
- use target-side duplicate checks.

Continuing without duplicate protection can be more dangerous than temporary unavailability.

## Exactly once is a business outcome, not a transport slogan

Integration products may provide strong delivery guarantees within a bounded technical component.

The complete business path still crosses:

- producer;
- network;
- middleware;
- target application;
- database;
- downstream systems.

The most realistic end-to-end model is often:

- at-least-once delivery;
- idempotent business processing;
- reconciliation.

This means messages may be repeated.

The business effect should not be.

### Distinguish delivery from execution

Exactly one message delivery does not prove exactly one SAP document.

One message may trigger two internal actions.

Two different messages may represent the same request.

One SAP commit may occur even though the acknowledgement is lost.

The architecture should protect the business operation, not only the transport unit.

## Recovery needs compensation, not database rollback

A distributed business process may complete several steps before a later step fails.

Example:

1. SAP order created;
2. inventory reserved;
3. warehouse request created;
4. customer confirmation sent;
5. export compliance check fails.

There is no single database transaction to roll back.

The process may require business compensation.

Possible actions include:

- block the order;
- release the reservation;
- cancel the warehouse request;
- notify the customer;
- create a review task.

Microsoft’s architecture guidance describes compensating transactions as business-specific actions used to undo or offset completed steps in an eventually consistent process. It emphasizes that compensation itself can fail, should be resumable, and often requires idempotent steps and human involvement for high-impact decisions.

### Compensation does not always restore the original state

A delivery may already have left the warehouse.

An invoice may already have been sent.

A customer may have acted on a confirmation.

The correct recovery may be:

- reversal;
- credit;
- return;
- new corrective document;
- explicit exception.

Do not assume every business action can be erased.

### Identify points of no return

Examples include:

- legally binding message sent;
- payment executed;
- goods physically shipped;
- tax document issued;
- external partner action completed.

Before the point of no return, automated rollback may be possible.

After it, recovery requires a business correction.

The process architecture should identify this boundary.

## A saga needs state and ownership

A saga coordinates several local transactions across domains.

Each step may have:

- forward action;
- expected result;
- compensation;
- timeout;
- owner.

For example:

| Step | Forward action | Possible compensation |
|---|---|---|
| Order | Create sales order | Cancel or block order |
| Inventory | Reserve stock | Release reservation |
| Warehouse | Create fulfilment request | Cancel request |
| Payment | Authorize payment | Void authorization |
| Customer | Send confirmation | Send correction |

The orchestrator should record:

- completed steps;
- failed step;
- compensation progress;
- irreversible actions;
- manual decision.

Events can support the process.

They do not remove the need to know the overall state.

## Recovery order matters

After an outage, teams often want to process the oldest message first.

That may not always be correct.

A backlog may contain:

1. order created;
2. order changed;
3. order cancelled.

If the target currently knows nothing about the order, sequence matters.

If the cancellation represents the latest authoritative state, it may be safer to retrieve the current object and process the final state rather than replay every intermediate event blindly.

### Choose replay strategy by consumer purpose

#### Audit consumer

May require every event in order.

#### Current-state projection

May need only the latest object version.

#### Transactional consumer

May need all commands and compensations in strict order.

#### Notification consumer

May need to suppress outdated messages.

One replay policy does not fit every consumer.

### Use object versions

When state changes are versioned, the consumer can detect:

- older message;
- duplicate version;
- missing sequence;
- newer state already processed.

A version-aware consumer can ignore an old confirmation that arrives after cancellation.

## File recovery requires sequence control

File-based integrations have their own disaster-recovery risks.

A file may be:

- sent but not acknowledged;
- received twice;
- partially processed;
- resent under a different name;
- processed before an earlier file;
- restored from backup after newer files.

### Use a manifest

A recoverable file should carry or be associated with:

- file ID;
- sequence number;
- source;
- creation time;
- schema version;
- record count;
- control total;
- checksum.

### Track record-level results

A file containing 10,000 orders may have:

- 9,950 completed;
- 30 permanently rejected;
- 20 uncertain.

Reprocessing the whole file may duplicate 9,950 orders.

Recovery should target only unresolved records unless the target provides strong idempotency for all of them.

### Do not use file rename as the only processing state

Moving a file from `/incoming` to `/processed` does not prove:

- every row completed;
- target commits succeeded;
- financial totals match;
- partial failures were resolved.

Keep a durable processing register.

## Events require publisher and consumer recovery

An event-driven flow has at least two separate recovery problems.

### Publisher recovery

Did every committed business change produce the required event?

### Consumer recovery

Did every mandatory consumer process the event correctly?

Broker availability does not answer either question completely.

### Reconcile commit to publication

For critical events, compare:

- committed source objects;
- event outbox or publication record;
- events published;
- publication failures.

### Reconcile publication to business effect

Compare:

- event delivered;
- consumer accepted;
- target object created or updated;
- final state verified.

SAP describes Event Mesh as enabling reliable asynchronous distribution and advanced event mesh as supporting resilient delivery and event-flow monitoring.

The business still needs source-to-event and event-to-outcome reconciliation.

## Dead-letter queues need business triage

A dead-letter queue stores messages that could not be processed normally.

It protects against silent loss.

It does not resolve the failure.

Every dead-letter item should include:

- business reference;
- failure category;
- business impact;
- current object state;
- retry safety;
- owner;
- age;
- recommended action.

### Do not mass replay dead-letter queues after recovery

Some messages may be:

- obsolete;
- manually completed;
- replaced by newer versions;
- permanently invalid;
- unsafe to repeat.

A recovery process should classify before replay.

The correct action may be:

- correct and replay;
- ignore as superseded;
- compensate;
- close with evidence;
- create a new business transaction.

## Manual fallback must be designed in advance

During a long outage, the business may use:

- spreadsheets;
- email;
- phone;
- direct SAP entry;
- partner portal;
- offline forms.

These fallback channels can preserve operations.

They also create later duplication.

For example:

1. customer order API is unavailable;
2. sales employee enters the order manually;
3. original API request remains queued;
4. integration recovers and creates the order again.

### Assign fallback identifiers

Every manual fallback transaction should preserve:

- original external reference;
- outage identifier;
- source;
- timestamp;
- manual document number.

The recovery process can then match queued transactions to manually completed work.

### Define who stops the fallback

When the primary service returns, both channels must not remain active indefinitely.

The business-continuity plan should state:

- when fallback starts;
- who authorizes it;
- how users are informed;
- when it stops;
- how outstanding fallback work is reconciled.

## Read-only degraded mode can be safer than full fallback

Not every outage requires an alternate write path.

A channel may continue to:

- show existing orders;
- accept draft requests;
- provide estimated status;
- collect information without final submission.

This may be safer than creating transactions in an uncontrolled temporary system.

The architecture should consider degraded modes such as:

- read only;
- accept and queue;
- accept without confirmation;
- restricted product scope;
- emergency-priority only.

Resilience does not always mean full functionality.

It means controlled continuity.

## Partner recovery requires explicit agreements

External partners may independently resend messages after a timeout.

The company should define:

- acknowledgement semantics;
- duplicate key;
- resend window;
- file sequence;
- support contact;
- outage communication;
- recovery confirmation.

A partner may interpret no acknowledgement as permission to resend.

The receiving company may have processed the transaction successfully.

Without agreed idempotency, both parties behave reasonably and still create duplicates.

## Recovery testing must include business effects

A technical DR test may prove that:

- the secondary environment starts;
- connectivity works;
- one test message passes.

This is not enough.

A meaningful test should cover:

- in-flight API call;
- queued command;
- duplicate event;
- partially processed file;
- lost acknowledgement;
- target already committed;
- stale message;
- manual fallback;
- failback.

### Test the uncomfortable scenarios

Examples:

#### Scenario 1: SAP commits, response is lost

Expected outcome:

- retry does not create another order;
- status can be retrieved.

#### Scenario 2: Event is delivered twice

Expected outcome:

- one warehouse request exists.

#### Scenario 3: Primary and secondary consumers overlap

Expected outcome:

- fencing prevents double processing.

#### Scenario 4: Idempotency store is unavailable

Expected outcome:

- high-risk writes stop or use target-side verification.

#### Scenario 5: Newer event was processed before replay

Expected outcome:

- old event does not overwrite the current state.

#### Scenario 6: Manual fallback created the transaction

Expected outcome:

- queued original is matched and closed without duplication.

### Test business reconciliation after recovery

The exercise is not complete until teams can prove:

- expected transaction count;
- target document count;
- duplicates;
- missing transactions;
- unresolved uncertainty;
- business totals where relevant.

## Disaster-recovery runbooks should be transaction aware

A useful runbook should include more than platform restart commands.

It should contain:

1. declare incident and recovery authority;
2. freeze unsafe replay;
3. identify affected business processes;
4. establish last known reliable transaction boundary;
5. restore platform and connectivity;
6. verify configuration versions;
7. inspect queues, events, files and in-flight calls;
8. reconcile target business objects;
9. classify uncertain transactions;
10. resume processing by controlled priority;
11. verify duplicates and sequence;
12. communicate business status;
13. perform failback only after reconciliation;
14. record corrective actions.

### Do not clear queues to make monitoring green

Deleting failed or old messages may remove evidence.

A message should leave the recovery backlog only because it was:

- successfully processed;
- superseded;
- compensated;
- manually completed;
- formally closed with evidence.

Operational cleanliness is not the same as business correctness.

## Prioritize recovery by business impact

Oldest-first recovery is easy to automate.

Business priority may be better.

Possible priority factors include:

- financial value;
- customer commitment;
- physical shipment;
- regulatory deadline;
- production dependency;
- perishability;
- manual workaround availability.

Priority processing must still preserve ordering where required.

Do not process a high-priority change before the target has received the object creation on which it depends.

## A reference resilience architecture

A practical design can be represented as follows:

```text
Channels and Partners
        |
Idempotent Business Contracts
Request ID | Status lookup | Safe error model
        |
Admission and Load Protection
Rate limit | Circuit breaker | Queue | Backpressure
        |
Durable Integration Execution
Persistent message | Correlation | Controlled retry
        |
Business Domains and SAP
Target duplicate check | Transaction commit | Object version
        |
Events and Downstream Consumers
Durable delivery | Idempotent consumer | Sequence control
        |
Recovery Control
Reconciliation | Replay authority | Compensation | Audit
```

Cross-cutting capabilities:

```text
Business identity
Configuration versioning
Observability
RTO and RPO
Fencing
Fallback control
DR testing
```

The architecture is resilient because it can determine business state.

Not merely because it has a second runtime.

## Example: resilient customer-order integration

### Normal flow

1. commerce creates external order ID;
2. order API receives idempotency key;
3. request is persisted;
4. SAP creates one sales order;
5. API stores SAP order reference;
6. order-created event is published;
7. warehouse creates one fulfilment request.

### API timeout

The commerce system receives no response.

It calls transaction-status lookup with the same external order ID.

The API returns the existing SAP order.

No new creation occurs.

### SAP unavailable

The API validates basic input and accepts the request into a durable queue where business policy permits.

The customer receives:

> Order received. Final confirmation pending.

### Warehouse unavailable

Orders remain in a persistent backlog.

Sales-order processing continues only within approved backlog limits.

The oldest-message age and business value are visible.

### Integration runtime failure

Recovery environment starts.

A fencing mechanism ensures only one consumer set processes the order queue.

### Manual fallback

Sales manually creates a priority order using the same external order reference.

When integration recovers, target-side business duplicate detection identifies the existing order and closes the queued request.

### Reconciliation

The process compares:

- accepted external orders;
- durable requests;
- SAP orders;
- published events;
- warehouse requests;
- unresolved exceptions.

## Example: resilient payment integration

Payment processing requires stricter controls.

### Requirements

- no accepted payment instruction lost;
- no payment posted twice;
- amount totals reconciled;
- uncertain transactions stopped for review;
- replay requires business authority.

### Recovery approach

1. each payment has a stable external instruction ID;
2. file or API request is persisted;
3. SAP posting stores the external instruction reference;
4. response loss triggers status lookup;
5. idempotency registry and SAP document reference are reconciled;
6. automatic retry applies only when non-posting is known;
7. batch totals are compared after recovery.

### Unsafe approach

- integration times out;
- operator replays all failed messages;
- SAP has no strong external-reference check;
- duplicate payments are discovered later.

For financial integrations, a slower controlled recovery is often better than a fast uncertain recovery.

## Example: resilient goods-movement integration

A warehouse sends goods-issue confirmation.

The first message reaches SAP and posts the movement.

The acknowledgement is lost.

The warehouse sends the confirmation again.

The interface must not create a second material movement.

Possible controls include:

- stable warehouse execution ID;
- reference stored in the SAP business result;
- target-side duplicate check;
- status API;
- movement-reversal process for genuine correction.

A message ID alone may be insufficient because the warehouse may generate a new message during resend.

## Metrics that matter

### Business recovery time

Time until the critical business service is trustworthy again.

This may be longer than platform recovery time.

### Unknown-outcome count

How many transactions lack evidence of completion or non-completion?

### Duplicate business-effect rate

How many orders, postings or movements were repeated during retry or recovery?

### Recovery backlog age

How long has the oldest critical transaction waited?

### Recovery backlog value

What financial or operational value remains incomplete?

### Idempotency coverage

What percentage of high-impact write operations uses stable business duplicate protection?

### Safe-retry rate

How many retried transactions were verified as safe before execution?

### Compensation completion rate

How many partially completed processes reached a controlled final state?

### Failover overlap time

How long could primary and recovery consumers both have been active?

### Configuration recovery accuracy

Did the restored environment use the approved flow, mapping and policy versions?

### Reconciliation completion time

How long after platform restoration until missing and duplicate transactions are accounted for?

### DR test business coverage

How many critical process scenarios were tested beyond infrastructure startup?

## Common mistakes

### Mistake 1: Defining recovery as platform availability

The runtime returns while business state remains unknown.

### Mistake 2: Retrying every failed message

Permanent errors and uncertain outcomes enter endless loops.

### Mistake 3: Using message IDs as the only duplicate control

The same business request returns with a new message ID.

### Mistake 4: Allowing retries at several layers

One request multiplies into many attempts.

### Mistake 5: Assuming timeout means no commit

The target may already contain the transaction.

### Mistake 6: Treating queues as unlimited resilience

Backlogs grow beyond recoverable capacity.

### Mistake 7: Running primary and recovery consumers together

Active-active infrastructure creates duplicate business execution.

### Mistake 8: Recovering flows but losing idempotency records

Old messages become new again.

### Mistake 9: Mass replaying dead-letter queues

Obsolete and manually completed work is repeated.

### Mistake 10: Ignoring message order during recovery

Old states overwrite newer business states.

### Mistake 11: Reprocessing entire files after partial success

Thousands of completed records are executed again.

### Mistake 12: Treating compensation as technical rollback

Completed physical, financial or legal effects require business correction.

### Mistake 13: Using manual fallback without original references

Queued and manual transactions cannot be matched.

### Mistake 14: Testing failover but not failback

Both environments later process work.

### Mistake 15: Declaring DR success before reconciliation

The systems run, but the business cannot trust the result.

## Questions architects and managers should ask

1. Which integration services are truly business critical?
2. What are their business RTO and RPO?
3. Where does each transaction become durable?
4. How is an uncertain API outcome resolved?
5. Which operations are idempotent?
6. Does duplicate protection use a business key?
7. Which layer owns retry?
8. Which failures are actually transient?
9. How is retry traffic limited during recovery?
10. How much backlog can the business safely accept?
11. Can primary and recovery environments process the same work?
12. What fences the inactive environment?
13. Which runtime state must survive disaster recovery?
14. What happens if the idempotency store is unavailable?
15. Which process steps are compensable?
16. Where is the point of no return?
17. How are obsolete events prevented from overwriting newer state?
18. How are partially processed files recovered?
19. How are manually completed transactions matched?
20. When is the business process considered recovered?
21. Who may authorize replay?
22. Has failback been tested?
23. Can the company prove there are no missing or duplicate transactions?

## A practical implementation sequence

### Phase 1: Select critical business services

Do not begin with every interface.

Focus on:

- orders;
- payments;
- fulfilment;
- financial postings;
- critical master data.

### Phase 2: Define business recovery objectives

Set:

- maximum outage;
- maximum delay;
- permitted data loss;
- acceptable degraded mode;
- recovery priority.

### Phase 3: Map transaction boundaries

Identify:

- durable acceptance;
- SAP commit;
- acknowledgement;
- event publication;
- downstream completion.

### Phase 4: Design identity and idempotency

Use:

- external request ID;
- source context;
- target reference;
- object version;
- processed-request registry.

### Phase 5: Classify failures

Separate transient, permanent, data, business and uncertain outcomes.

### Phase 6: Assign retry ownership

Avoid competing retry layers.

### Phase 7: Design load protection

Use queues, rate limits, circuit breakers and backpressure deliberately.

### Phase 8: Design failover authority

Define:

- active environment;
- fencing;
- routing;
- consumer ownership;
- recovery epoch.

### Phase 9: Design compensation

Record forward and corrective actions for long-running processes.

### Phase 10: Build reconciliation

Compare expected, processed, duplicated and incomplete business results.

### Phase 11: Design fallback

Preserve original identifiers and define start and stop authority.

### Phase 12: Test failure and recovery

Include timeout after commit, duplicate delivery, partial files, stale messages, environment overlap and failback.

## The goal is not zero failure

No serious integration architecture can promise that:

- networks never fail;
- targets never become unavailable;
- messages never arrive twice;
- consumers never process out of order;
- recovery never requires people.

The real objective is controlled failure.

A resilient landscape should:

- preserve business intent;
- prevent silent loss;
- tolerate repeated delivery;
- expose uncertainty;
- avoid uncontrolled duplicate effects;
- recover through evidence;
- compensate when rollback is impossible.

SAP Integration Suite provides current capabilities for application integration, APIs, event-driven communication, hybrid connectivity, centralized governance and monitoring. Event Mesh and advanced event mesh are positioned for reliable asynchronous communication and resilient event distribution.

Those are important building blocks.

The recovery architecture must still be built around business transactions.

A second runtime does not protect the company from sending the same payment twice.

A persistent queue does not prove that one order was created exactly once.

A successful failover does not prove that old and new consumers did not overlap.

The decisive question is not:

> How quickly can we restart the integration platform?

It is:

> How quickly can we restore a business process whose transactions are complete, traceable and safe to continue?

That is the standard a resilient SAP integration architecture should meet.

---

### SAP integration resilience and disaster-recovery checklist

- [ ] Critical integrations are classified by business impact.
- [ ] RTO and RPO are defined in business terms.
- [ ] Platform, message, business-object and process recovery are separated.
- [ ] Every critical write operation has a stable business request key.
- [ ] Message and business idempotency are both considered.
- [ ] Timeout is treated as an uncertain outcome, not automatic failure.
- [ ] Transaction-status lookup is available where required.
- [ ] Retry ownership is explicit.
- [ ] Transient and permanent errors are treated differently.
- [ ] Retries use limits, backoff and load protection.
- [ ] Queue age and business value are monitored.
- [ ] Admission control and degraded modes are defined.
- [ ] One execution authority exists during failover.
- [ ] Fencing prevents overlapping primary and recovery processing.
- [ ] Failback has a separate tested plan.
- [ ] Integration artifacts and configurations are reproducible.
- [ ] Runtime state such as queues and idempotency records has recovery rules.
- [ ] High-risk processing stops when duplicate protection is unavailable.
- [ ] Events are reconciled from source commit to consumer outcome.
- [ ] File recovery supports batch and record-level control.
- [ ] Dead-letter messages are classified before replay.
- [ ] Compensation is designed for multi-step processes.
- [ ] Irreversible actions and points of no return are identified.
- [ ] Manual fallback preserves original business references.
- [ ] Recovery runbooks include transaction reconciliation.
- [ ] DR tests cover business effects, not only infrastructure.
- [ ] Failover success is followed by missing and duplicate checks.
- [ ] The business process is not declared recovered until outcomes are trustworthy.

### Sources and further reading

SAP currently positions SAP Integration Suite as a secure integration platform for applications, APIs, events, data, partners and AI agents, with centralized governance, real-time monitoring, built-in security and support for hybrid landscapes.

SAP currently describes Event Mesh as supporting reliable asynchronous communication across SAP and third-party cloud and hybrid environments. Advanced event mesh is positioned for distributed brokers, high-volume workloads, business continuity, resilient event delivery and monitoring of event flows.

SAP Cloud Integration currently supports designing, running and monitoring A2A, B2B and B2G integration flows, prebuilt content and hybrid execution, including private-landscape deployment through edge integration cell for selected requirements.

NIST SP 800-34 Rev. 1 provides contingency-planning guidance intended to help organizations evaluate systems and operations, determine recovery priorities and connect contingency planning with broader organizational resilience.

AWS Prescriptive Guidance describes retry with backoff as a pattern for transient failures and emphasizes idempotency, limited retries and failure handling that avoids further overloading degraded services.

Microsoft’s Compensating Transaction pattern describes recovery for multi-step, eventually consistent processes where completed work cannot be rolled back through one atomic transaction. It emphasizes business-specific compensation, idempotent corrective steps, durable progress and human intervention for difficult decisions.

*Reviewed: July 2026. SAP Integration Suite capabilities, deployment options, service levels and recovery responsibilities can vary by edition, region and contract. Detailed recovery designs should be validated against current SAP documentation, contractual SLAs and the actual behaviour of every connected system.*
