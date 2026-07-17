# How to Design Event-Driven SAP Integrations Without Losing Control

A sales order is created in SAP.

An event is published.

Five systems receive it:

- a warehouse platform;
- a customer portal;
- a data platform;
- a notification service;
- an AI agent.

The warehouse creates a fulfilment request.

The portal updates the order status.

The data platform stores the transaction.

The notification service sends a confirmation.

The AI agent starts a customer-risk check.

The architecture looks modern.

Then the sales order is changed.

The change event reaches the consumers in a different order. One system processes the change before the creation event. Another receives the original event twice. The warehouse is unavailable and processes its backlog six hours later. The customer portal shows the new quantity, while the warehouse still works with the old one.

Every event was published.

The business process is inconsistent.

This is the main risk of event-driven integration.

Publishing an event is easy.

Designing a distributed business process that remains correct when events are delayed, duplicated, reordered, replayed or missed is much harder.

SAP currently positions Event Mesh as a way to distribute business events across SAP and third-party landscapes, trigger real-time processes and support reliable asynchronous communication without tight point-to-point coupling. SAP also positions advanced event mesh for distributed high-volume event streaming, resilient delivery and visibility into event flows.

These capabilities provide infrastructure.

They do not define:

- what an event means;
- who owns its schema;
- whether it may be delivered more than once;
- how consumers detect old information;
- how the business verifies that every required consumer acted correctly.

A successful event-driven architecture needs an operating model, not only a broker.

## Event-driven architecture is not simply asynchronous integration

Many teams describe any asynchronous message as an event.

This creates confusion.

A message may represent:

- a command;
- a notification;
- a business event;
- a technical event;
- a data-change event;
- a snapshot;
- an integration request.

These messages have different responsibilities.

Consider two messages:

> Create a delivery for sales order 50001234.

and:

> Sales order 50001234 was confirmed.

The first is a command.

It asks a particular capability to perform an action.

The second is an event.

It announces that a business fact already exists.

The distinction affects:

- ownership;
- expected response;
- retry behaviour;
- number of consumers;
- error handling.

An architecture becomes difficult to control when events are used as hidden commands or commands are published as public facts.

## A business event describes something that has happened

A useful business event normally uses past tense:

- `SalesOrder.Created`
- `SalesOrder.Confirmed`
- `PurchaseOrder.Approved`
- `BusinessPartner.Blocked`
- `GoodsReceipt.Posted`
- `Invoice.Cancelled`

The publisher is stating:

> This business-state change has already occurred in the authoritative system.

The event should not require the publisher to know which systems are interested.

Consumers decide whether the fact is relevant to them.

This creates loose coupling.

The publisher is separated from individual consumers.

Loose coupling does not mean no dependency.

Consumers still depend on:

- the meaning of the event;
- its schema;
- identifiers;
- timing expectations;
- versioning;
- delivery behaviour.

The coupling moves from direct system calls to a published business contract.

## A command asks for a future action

A command may look like:

- `CreateWarehouseTask`
- `GenerateInvoice`
- `NotifyCustomer`
- `RecalculatePrice`

A command usually has:

- an intended processing capability;
- a requested outcome;
- success or failure semantics;
- an accountable receiver.

Commands can still be asynchronous.

For example, SAP can place a fulfilment request into a persistent queue rather than waiting synchronously for the warehouse.

The important distinction is not synchronous versus asynchronous.

It is fact versus request.

## Do not hide commands behind event names

A message such as:

> `OrderReadyForDelivery`

may be ambiguous.

Does it mean:

- the order has reached a confirmed business state;
- or the warehouse is expected to create a delivery?

If one consumer is responsible for performing a required action, the architecture should make that responsibility clear.

A command queue may be more appropriate than a public event.

Otherwise, teams may assume that somebody else acts on the event.

The event is delivered successfully.

The business action never happens.

## Technical events and business events are different

A technical event may describe:

- application instance restarted;
- certificate nearing expiry;
- message failed;
- CPU threshold exceeded;
- integration endpoint unavailable.

A business event may describe:

- supplier approved;
- order confirmed;
- payment received;
- delivery completed.

Technical events are useful for operations and monitoring.

They should not automatically become the primary integration contract for a business process.

For example:

> Database row changed

does not explain:

- which business state changed;
- whether the transaction was committed;
- why consumers should care;
- whether the change is part of a larger process.

A business event should communicate stable business meaning rather than expose internal implementation behaviour.

## Data-change events are not always business events

A change-data-capture system may publish every inserted or updated record.

This can support:

- analytics;
- replication;
- cache updates;
- technical synchronization.

It may be a weak foundation for operational business processes.

One business action can update many tables.

A consumer should not need to reconstruct the meaning of an order confirmation from low-level database changes.

Conversely, several technical changes may belong to one business event.

A good rule is:

> Use data-change events when consumers need replicated data changes. Use business events when consumers need to react to a meaningful business-state transition.

## The first design question: what fact matters?

Before defining a topic or schema, write one sentence:

> When ______ happens, interested systems may need to ______.

For example:

> When a supplier is approved for purchasing, target systems may need to create or extend the supplier for the approved organizational scope.

This reveals several questions:

- Does “approved” mean centrally approved or ready in every target?
- Does the event include organizational scope?
- Should targets create the record automatically?
- Is the event a fact or a request?
- What happens when one target rejects the data?
- Who confirms end-to-end readiness?

Without this discussion, the team may publish `Supplier.Changed` and expect every consumer to infer the process.

## Publish meaningful state transitions

An event should represent a change consumers can understand and use.

Weak events include:

- `ObjectUpdated`
- `DataChanged`
- `RecordProcessed`
- `StatusChanged`

They force consumers to:

- retrieve the object;
- compare current and previous values;
- interpret internal statuses;
- decide whether the change matters.

Stronger events include:

- `Supplier.Approved`
- `Customer.CreditBlocked`
- `Delivery.GoodsIssuePosted`
- `PurchaseOrder.Released`

These events expose business meaning.

There is still a balance.

Creating an event for every small state may produce an unmanageable catalogue.

The event should represent a stable business fact with real consumer value.

## Event granularity matters

An event can be too broad or too narrow.

## Too broad

Example:

> `BusinessPartner.Changed`

The event does not tell consumers whether the change involved:

- address;
- bank details;
- sales-area extension;
- blocking status;
- contact information.

Every consumer may retrieve the full record after every change.

This increases:

- traffic;
- coupling;
- unnecessary processing;
- access to data consumers do not need.

## Too narrow

Examples:

- `BusinessPartner.StreetChanged`
- `BusinessPartner.HouseNumberChanged`
- `BusinessPartner.PostalCodeChanged`

This creates a large number of event types and may expose internal field design.

Consumers may need to combine several events into one meaningful update.

## Practical balance

Use event granularity aligned with a business capability.

Examples:

- `BusinessPartner.AddressChanged`
- `BusinessPartner.PaymentDataChanged`
- `BusinessPartner.PurchasingExtensionApproved`

The correct level depends on:

- consumer needs;
- security;
- transaction boundaries;
- process meaning;
- change frequency.

## An event is not automatically the full business object

There are two common event-content strategies.

## Notification event

Contains:

- event type;
- object identifier;
- version;
- timestamp;
- limited context.

The consumer retrieves current data through an API.

### Advantages

- smaller events;
- less sensitive data distributed;
- current data retrieved from the owner;
- simpler schema.

### Risks

- consumer now depends on API availability;
- current state may differ from state at event time;
- large bursts create many API calls;
- historical replay may retrieve a newer state.

## Data-carrying event

Contains enough information for the consumer to act without another call.

### Advantages

- lower runtime dependency on publisher;
- better replay;
- event records historical state;
- fewer follow-up calls.

### Risks

- larger schema;
- more sensitive data distribution;
- duplicated data;
- more difficult schema evolution;
- consumers may retain information longer than permitted.

Neither design is universally correct.

The choice should follow:

- business need;
- data sensitivity;
- replay requirements;
- volume;
- consistency;
- consumer autonomy.

## A useful hybrid pattern

An event can include:

- stable business identifier;
- object version;
- changed business area;
- small set of required attributes;
- link or API for additional information.

The consumer can act using the event where possible and retrieve more detail only when necessary.

## Events need stable business identifiers

A consumer must know which business object the event describes.

Useful identifiers may include:

- sales order number;
- external order reference;
- business partner ID;
- purchase order ID;
- delivery number;
- invoice ID;
- event ID;
- source-system identifier.

The event should distinguish:

### Event identity

Which occurrence is this?

### Business-object identity

Which order, customer or supplier changed?

These are not the same.

The same order may generate many events.

Each event requires its own unique identifier.

## Event identity supports duplicate protection

Asynchronous delivery should normally be designed under the assumption that the same event may be received more than once.

Reasons can include:

- retry after acknowledgement failure;
- broker redelivery;
- consumer restart;
- replay;
- manual recovery;
- network uncertainty.

A consumer should record processed event IDs or use an equivalent idempotency mechanism.

Otherwise, duplicate delivery can create:

- duplicate documents;
- repeated notifications;
- repeated workflow tasks;
- double financial effects;
- duplicate external calls.

SAP describes Event Mesh as providing reliable asynchronous communication and advanced event mesh as supporting resilient distributed delivery at scale.

Reliable delivery does not mean that consumers may ignore duplicate processing design.

## Business idempotency is stronger than event deduplication

Recording an event ID protects against receiving the same event twice.

It may not protect against receiving two different events representing the same business intention.

For example:

- a source republishes an order event with a new event ID;
- a user triggers the same action again;
- an integration flow regenerates the message;
- historical events are replayed.

The consumer may need a stable business key such as:

> Source system + external order ID + requested action version

This protects the business effect, not only the technical message.

## Ordering is rarely global

A common assumption is:

> Events are processed in the order in which they happened.

This should not be assumed across an entire distributed landscape.

Ordering may differ because of:

- parallel publishing;
- several broker partitions;
- consumer scaling;
- retries;
- network delays;
- replay;
- different event sources.

Global ordering is expensive and often unnecessary.

What normally matters is ordering for one business object or aggregate.

For example:

- events for one sales order should follow object version;
- events for unrelated orders can be processed in parallel.

## Include object version or sequence

A consumer can use a version number such as:

- order version 1;
- order version 2;
- order version 3.

If version 3 arrives before version 2, the consumer can:

- process version 3 and ignore version 2 later;
- hold version 3 until version 2 arrives;
- retrieve the current authoritative state;
- route the sequence gap for investigation.

The correct strategy depends on whether every intermediate state matters.

## Not every consumer needs every intermediate state

A customer portal may need only the latest order status.

It can ignore older events after receiving a newer version.

An audit or financial process may need every state transition.

It cannot skip an intermediate event.

Event design should therefore consider consumer intent.

One delivery strategy may not suit every use case.

## Eventual consistency must be a business decision

In event-driven architecture, systems normally do not update at exactly the same time.

This creates temporary inconsistency.

For example:

- supplier is approved centrally;
- procurement system receives the event in seconds;
- warehouse system receives it in minutes;
- one local ERP is unavailable for three hours.

The organization must define:

- acceptable delay;
- authoritative system;
- user experience during delay;
- blocked processes;
- escalation threshold;
- reconciliation requirement.

“Near real time” is not a complete business rule.

A process should say:

> Supplier data should be available in required purchasing systems within 15 minutes. Orders must remain blocked until target readiness is confirmed.

This connects event delivery to business control.

## Do not promise immediate consistency through asynchronous events

An application that must know the current authoritative value before completing a transaction may need a synchronous validation API.

For example, before releasing a high-value order, the system may need current credit status.

An event-driven local copy may be slightly outdated.

Whether this is acceptable depends on:

- risk;
- update frequency;
- permitted staleness;
- fallback.

Events are useful for distributing change.

They are not automatically the right source for every real-time decision.

## The dual-write problem

A source application may need to:

1. commit a business transaction;
2. publish an event.

If these actions are independent, one may succeed while the other fails.

### Transaction succeeds, event fails

The authoritative system contains the new order.

Consumers never learn about it.

### Event succeeds, transaction fails

Consumers act on a business state that does not exist.

This is one of the central risks in event publishing.

The source needs a reliable relationship between business commit and event publication.

Common design approaches include:

- transactional event capability provided by the application;
- an outbox record committed with the business transaction;
- change capture from a durable business-event record;
- controlled retry from an event-publication log.

The essential requirement is:

> The system must be able to prove which committed business changes still need events.

## Do not publish before the business transaction is final

An application may publish an event when processing begins.

Later validation fails and the transaction rolls back.

Consumers have already reacted.

Events that represent completed business facts should be published after the authoritative state is committed.

If the process needs to communicate an earlier stage, use a different event with honest meaning:

- `OrderSubmissionReceived`
- `OrderValidationCompleted`
- `OrderConfirmed`

These are different facts.

## Event publication needs monitoring

The organization should monitor:

- events created;
- events published;
- publication failures;
- publication delay;
- events waiting for retry;
- event schema version;
- source transaction reference.

Monitoring only broker availability is insufficient.

The broker may be healthy while the application fails to publish business events.

## Consumers are operational services

A consumer is not only a small piece of code.

It has operational responsibilities:

- subscribe;
- authenticate;
- validate schema;
- process event;
- detect duplicates;
- handle ordering;
- record outcome;
- retry safely;
- expose monitoring;
- support replay.

Every important consumer should have:

- owner;
- service level;
- support procedure;
- version;
- backlog monitoring;
- dead-letter handling;
- recovery plan.

A publisher should not be responsible for debugging every consumer.

The end-to-end business service still needs ownership.

## Successful broker delivery is not successful business processing

A broker may confirm that a consumer received a message.

The consumer may then fail while:

- mapping data;
- validating a business rule;
- calling another system;
- creating a document;
- committing the transaction.

The architecture should distinguish:

1. event published;
2. event delivered;
3. event accepted by consumer;
4. consumer processing completed;
5. target business result verified.

These are separate milestones.

## Acknowledgement timing matters

If a consumer acknowledges the event before business processing completes, a later failure may lose the event.

If it acknowledges only after full processing, long processing may trigger redelivery.

A common stronger pattern is:

1. receive event;
2. persist it locally;
3. acknowledge receipt;
4. process from the durable local record;
5. track business result separately.

This separates broker delivery from business execution.

The exact implementation depends on the platform and process.

The principle is durability before acknowledgement.

## Retries must distinguish temporary and permanent failures

A temporary failure may include:

- target service unavailable;
- network timeout;
- temporary database lock;
- rate limit.

Retry may help.

A permanent failure may include:

- unsupported schema;
- missing mandatory value;
- unknown business code;
- invalid customer;
- policy rejection.

Retrying the same event repeatedly will not correct permanent data.

The consumer should classify failures.

## Temporary failure

Actions may include:

- delayed retry;
- exponential backoff;
- limited retry count;
- target-health check.

## Permanent business failure

Actions may include:

- dead-letter or exception queue;
- data-owner notification;
- correction workflow;
- no automatic replay until input changes.

## Unknown failure

Actions may include:

- stop automatic processing;
- preserve evidence;
- escalate to technical owner.

## Dead-letter queues are not resolution

A dead-letter queue prevents failed messages from disappearing.

It can also become a graveyard.

Every dead-letter process should define:

- owner;
- reason classification;
- maximum age;
- business impact;
- correction process;
- replay authority;
- verification.

A message should not be replayed simply because its technical error was cleared.

The team should check:

- whether a later event already superseded it;
- whether the business transaction was completed manually;
- whether replay creates duplicate effects;
- whether order still matters.

## Replay is a business operation

Event replay is valuable when:

- a consumer was unavailable;
- a new consumer needs historical events;
- a defect has been corrected;
- a projection must be rebuilt;
- data must be re-synchronized.

Replay can also recreate old business actions.

Before replaying, define:

- event range;
- consumers;
- original versus current schema;
- ordering;
- duplicate controls;
- business effects;
- rate limit;
- stop conditions.

A consumer that sends customer notifications should not resend three years of confirmations when rebuilding its state.

Different consumers may require different replay behaviour.

## Separate state reconstruction from side effects

A consumer may use events to build a local read model.

Replaying events to rebuild that model can be safe.

The same consumer may also perform side effects:

- send email;
- create external transaction;
- trigger payment;
- notify partner.

These side effects should not automatically repeat during state reconstruction.

The consumer needs a replay mode or separate processing paths.

## Event schema is a product contract

An event schema should define:

- event type;
- event version;
- source;
- event ID;
- timestamp;
- business-object ID;
- object version;
- data payload;
- correlation context.

It should also define semantics:

- what business fact occurred;
- when it is considered complete;
- which system is authoritative;
- which fields are mandatory;
- whether absence means unknown or empty;
- whether consumers may store the data;
- compatibility rules.

A technically valid JSON schema does not define complete business meaning.

## Avoid exposing internal table structures

An event payload built directly from internal tables may include:

- source-specific names;
- technical status codes;
- implementation details;
- fields consumers should not use.

This makes consumers dependent on source internals.

A better event exposes a stable domain contract.

The source application may change internally while preserving the published event.

This is the event-driven equivalent of a stable business API.

## Use bounded event domains

Avoid one global topic such as:

> `SAPChanges`

with every system change.

Prefer domains such as:

- sales;
- procurement;
- master data;
- logistics;
- finance.

Within each domain, define clear event families.

This improves:

- ownership;
- security;
- discoverability;
- schema governance;
- lifecycle management.

## Topic naming should not carry all business logic

Topics can support:

- routing;
- authorization;
- domain separation;
- environment separation.

They should not require consumers to decode complex meaning from the topic path alone.

Important information should also exist in the event envelope and schema.

## Schema evolution requires compatibility rules

Events may exist longer than the application release that created them.

Consumers may update at different times.

Safer changes include:

- adding optional fields;
- adding new event types;
- adding new code values with consumer preparation;
- publishing a new major version for breaking changes.

Riskier changes include:

- removing fields;
- changing data type;
- changing field meaning;
- renaming mandatory fields;
- reusing old values for new meanings.

## Additive does not always mean harmless

Adding a new code value may be structurally compatible.

A consumer with a fixed list may still fail or map it incorrectly.

Compatibility testing should cover:

- schema;
- values;
- semantics;
- consumer behaviour.

## Consumers should tolerate unknown optional fields

A consumer should normally ignore fields it does not use.

This allows publishers to extend the event without forcing every consumer to update.

Consumers should not silently accept unknown values in fields that affect business decisions.

Unknown structure and unknown meaning require different treatment.

## Create an event catalogue

An event catalogue should record:

- event name;
- business meaning;
- publisher;
- domain owner;
- schema;
- version;
- business-object identifier;
- expected volume;
- ordering model;
- retention;
- security classification;
- known consumers;
- support owner;
- deprecation state.

SAP Integration Suite currently presents centralized governance and visibility across APIs, events, applications and partner integrations as part of its platform direction.

A catalogue turns events into governed products instead of invisible technical messages.

## Do not require publishers to know every consumer

Loose coupling is weakened when every new consumer needs a publisher change.

The publisher should provide:

- stable event;
- clear contract;
- access policy;
- service expectations.

Consumers should subscribe independently where governance permits.

However, critical business processes should still maintain an end-to-end dependency map.

The publisher does not need runtime knowledge of every consumer.

The organization needs operational knowledge of which business services depend on each event.

## Consumer ownership must be explicit

For every consumer, define:

- why it consumes the event;
- what action it performs;
- whether that action is mandatory;
- acceptable delay;
- failure impact;
- retry behaviour;
- reconciliation.

A customer analytics consumer and warehouse fulfilment consumer should not have the same service expectations.

One is informational.

The other may be required for order completion.

## Separate mandatory and optional consumers

### Mandatory consumer

The business process is incomplete until it succeeds.

Example:

- warehouse must receive an approved delivery request.

### Optional consumer

Failure does not block the transaction.

Example:

- marketing analytics receives order information.

This distinction affects:

- monitoring;
- escalation;
- service levels;
- reconciliation;
- incident priority.

The broker should not treat every subscriber as equally critical.

## Event-driven does not mean orchestration-free

A simple process may react independently to events.

A complex process may require coordination across several steps.

For example:

1. order accepted;
2. credit approved;
3. inventory reserved;
4. warehouse request created;
5. customer confirmation sent.

If each service reacts independently with no process state, the organization may struggle to answer:

- which steps completed;
- which step failed;
- whether compensation is required;
- who owns the overall outcome.

A process orchestrator or workflow may still be necessary.

Events can connect steps.

They do not automatically replace process coordination.

## Choreography versus orchestration

## Choreography

Each service reacts to events and publishes new events.

Advantages:

- low direct coupling;
- independent evolution;
- flexible subscribers.

Risks:

- hidden process flow;
- difficult end-to-end visibility;
- circular reactions;
- unclear ownership;
- complex failure recovery.

## Orchestration

A coordinator manages process steps.

Advantages:

- visible process state;
- explicit sequencing;
- centralized recovery;
- easier business monitoring.

Risks:

- coordinator becomes central dependency;
- services may become tightly controlled;
- orchestration logic can grow too large.

A practical architecture often combines both.

Use events for domain facts.

Use orchestration where the business requires controlled multi-step completion.

## Avoid event chains with no owner

A dangerous architecture may look like:

1. event A triggers service B;
2. B publishes event C;
3. C triggers D;
4. D publishes E;
5. E triggers an agent;
6. the agent updates the original object.

Nobody can explain the complete loop.

This creates risks of:

- recursion;
- duplicate action;
- unpredictable timing;
- hidden dependencies;
- difficult rollback.

Every event chain should have:

- business purpose;
- end condition;
- owner;
- observability;
- loop prevention.

## Correlation IDs support end-to-end visibility

A business transaction may generate many events and commands.

Use identifiers that connect them:

- business process ID;
- original request ID;
- correlation ID;
- causation ID.

### Correlation ID

Groups messages belonging to one process.

### Causation ID

Shows which event or command caused the current message.

This helps answer:

- What started this process?
- Which event triggered this action?
- Which downstream events followed?
- Where did processing stop?

## Observability should follow the business process

Technical monitoring may show:

- broker healthy;
- topic active;
- consumer connected;
- message delivered.

Business monitoring should show:

- order created;
- fulfilment request processed;
- warehouse accepted order;
- customer confirmation sent;
- exceptions remaining.

SAP Integration Suite currently describes event-flow monitoring, tracing and centralized visibility across distributed event landscapes among its event-driven capabilities.

Use this technical visibility as part of a wider business-service view.

## Measure event lag

Important operational measures include:

### Publication lag

Time from business commit to event publication.

### Delivery lag

Time from publication to consumer receipt.

### Processing lag

Time from receipt to completed consumer action.

### Business-completion lag

Time until the full required process outcome exists.

A low delivery lag can coexist with a large business-processing backlog.

## Monitor consumer backlog age, not only volume

A queue of 10,000 events may be normal for a high-volume consumer.

One event waiting two hours may be critical.

Useful measures include:

- oldest unprocessed event;
- backlog by business priority;
- processing rate;
- failed-event age;
- retry count;
- event version distribution.

## Reconciliation remains necessary

Events improve distribution.

They do not prove completeness.

For a critical process, reconcile:

- source business objects committed;
- events published;
- events delivered;
- mandatory consumers completed;
- target objects created;
- duplicates detected;
- exceptions unresolved.

For example:

> 10,000 confirmed orders → 10,000 order events → 9,998 warehouse requests → two documented exceptions.

This is stronger than:

> Event broker availability was 99.99%.

## Do not depend on users to detect missing events

A missing event may produce no technical error.

The source transaction succeeds.

No event is published.

No consumer receives anything.

Nothing fails because nothing begins.

Reconciliation or expected-volume monitoring is required to detect this silent loss.

## Security should follow least data and least authority

Events may be distributed widely.

Avoid placing unnecessary sensitive data in a broadly subscribed event.

Consider:

- personal data;
- bank data;
- pricing;
- salary;
- tax identifiers;
- security status;
- customer confidential information.

Use:

- topic-level access;
- field minimization;
- encryption;
- retention control;
- approved consumer registration.

A consumer should receive only the data required for its purpose.

## Event retention is a business and compliance decision

Longer retention supports:

- replay;
- recovery;
- audit;
- new consumer onboarding.

It also increases:

- storage;
- exposure of sensitive data;
- risk of outdated replay;
- lifecycle complexity.

Retention should consider:

- business recovery window;
- legal requirements;
- data sensitivity;
- source-system retention;
- replay design.

Do not retain events indefinitely only because storage is available.

## AI agents make event governance more important

SAP currently positions Integration Suite as supporting event-driven agents and secure connections between agents, applications and business processes through APIs, events and integration services.

An event can trigger an AI agent to:

- investigate an exception;
- prepare a recommendation;
- update a ticket;
- start a workflow;
- request approval.

The agent should not automatically receive broad authority because the trigger is real time.

Define:

- which event may trigger the agent;
- which context it may retrieve;
- which actions it may prepare;
- which actions require approval;
- how repeated events are handled;
- how agent output is verified.

A duplicated event should not make an agent perform the same high-impact action twice.

## Use events to trigger investigation before execution

A strong first agentic pattern is:

1. business exception event occurs;
2. agent collects evidence;
3. agent classifies the situation;
4. deterministic rules check permitted actions;
5. person approves where required;
6. workflow executes;
7. result is verified.

This preserves the benefits of real-time reaction without allowing probabilistic interpretation to control production directly.

## A reference SAP event architecture

A controlled architecture can contain several layers.

## 1. Authoritative application

Commits the business state.

Examples:

- SAP S/4HANA;
- SAP MDG;
- procurement platform;
- warehouse application.

## 2. Event publication layer

Creates a durable event linked to the committed transaction.

## 3. Event broker or mesh

Routes and retains events according to configured policies.

SAP describes Event Mesh as distributing events across cloud and hybrid landscapes and advanced event mesh as supporting distributed event brokers and high-volume workloads across environments.

## 4. Consumer ingestion layer

Validates, deduplicates and stores received events.

## 5. Consumer business processing

Performs the domain-specific action.

## 6. Verification layer

Confirms the target business result.

## 7. Reconciliation layer

Checks end-to-end completeness across required consumers.

## 8. Governance layer

Maintains:

- event catalogue;
- schema versions;
- owners;
- access;
- service levels;
- retention;
- deprecation.

## Example: sales order events

Consider an order created in SAP.

## Event 1: Sales order created

Payload may contain:

- event ID;
- order ID;
- external reference;
- order version;
- sold-to party;
- high-level item references;
- creation timestamp;
- source system.

Possible consumers:

- customer portal;
- analytics;
- fulfilment coordination;
- notification service.

## Event 2: Sales order confirmed

Contains:

- order ID;
- confirmed version;
- confirmed quantities;
- important dates;
- confirmation timestamp.

## Event 3: Sales order blocked

Contains:

- order ID;
- block category;
- business impact class;
- owner domain;
- timestamp.

Sensitive details may remain accessible through a controlled API rather than being distributed to every consumer.

## Event 4: Sales order cancelled

Contains:

- order ID;
- cancelled scope;
- effective time;
- version.

Consumers should ignore older confirmation events arriving after the cancellation version.

## Example: business partner distribution

A generic `BusinessPartner.Changed` event may be too broad.

A stronger event family may include:

- `BusinessPartner.IdentityUpdated`
- `BusinessPartner.AddressChanged`
- `BusinessPartner.SalesExtensionApproved`
- `BusinessPartner.Blocked`

Each event should state:

- central object ID;
- version;
- approved scope;
- source system;
- effective time.

Target systems may still require local extensions or validation.

The central event confirms central truth.

It does not automatically prove local business readiness.

## Example: goods movement and downstream action

When goods issue is posted:

- billing may become due;
- customer portal may update;
- analytics may record fulfilment;
- transport system may close shipment activity.

The event should represent the committed goods issue.

Consumers should not interpret a preliminary warehouse status as the same fact.

The organization should define whether reversal produces:

- a separate `GoodsIssue.Reversed` event;
- a new object version;
- both.

Consumers need an explicit correction path.

## Corrections should be events, not silent history edits

A business fact may later be reversed or corrected.

Do not assume the original event can be deleted from every consumer.

Publish a new fact:

- invoice cancelled;
- goods issue reversed;
- supplier unblocked;
- order quantity corrected.

Consumers can then update their state while preserving history.

This is particularly important for audit and financial processes.

## A practical rollout sequence

## Phase 1: Select one business event

Choose a meaningful, low-risk event such as:

- order created;
- supplier approved;
- delivery completed.

Avoid beginning with a large enterprise event programme.

## Phase 2: Define semantics

Document:

- exact business fact;
- commit point;
- authoritative system;
- identifiers;
- version;
- consumers.

## Phase 3: Define delivery assumptions

Specify:

- duplicate handling;
- ordering;
- retention;
- replay;
- acceptable delay.

## Phase 4: Create the event contract

Define:

- envelope;
- payload;
- mandatory fields;
- data sensitivity;
- compatibility.

## Phase 5: Build one controlled consumer

The consumer should:

- persist;
- deduplicate;
- process;
- verify;
- expose monitoring.

## Phase 6: Add reconciliation

Prove source event completeness and target business completion.

## Phase 7: Test failure conditions

Include:

- duplicate event;
- delayed event;
- old version;
- missing event;
- unavailable consumer;
- schema change;
- replay;
- partial processing.

## Phase 8: Add more consumers

Only after the contract and operating model are stable.

## Phase 9: Introduce catalogue and governance

Make event discovery, ownership and versioning visible.

## Phase 10: Expand by domain

Build event families around stable business capabilities rather than random technical changes.

## A strong first pilot

A useful pilot may be:

> Publish an event when a sales order is created and update a customer portal asynchronously.

### Publisher responsibility

- commit order;
- create durable event;
- publish order ID, external reference and object version.

### Consumer responsibility

- persist event;
- reject invalid schema;
- deduplicate event ID;
- compare order version;
- update portal;
- record completion.

### Failure behaviour

- retry temporary portal failure;
- quarantine permanent mapping failure;
- alert on backlog age;
- support controlled replay.

### Reconciliation

Compare:

- committed sales orders in pilot scope;
- published order events;
- portal records;
- unresolved exceptions.

### Explicit exclusions

The pilot should not:

- allocate inventory;
- release credit blocks;
- create financial documents;
- trigger customer communication with unverified dates.

### Success measures

- publication completeness;
- consumer-processing success;
- duplicate safety;
- processing delay;
- reconciliation accuracy;
- support effort.

## Metrics that matter

## Event-publication completeness

What percentage of committed business changes produced the required event?

## Duplicate-processing rate

How often did repeated delivery create repeated business effects?

## Out-of-order handling rate

How often did events arrive out of sequence, and were they handled correctly?

## Consumer lag

How long do mandatory consumers take to complete processing?

## Dead-letter age

How long do failed business events remain unresolved?

## Replay success

Can events be replayed without duplicate or unintended side effects?

## Schema compatibility

How many consumers fail after event evolution?

## Business-completion rate

What percentage of published events produce all mandatory downstream results?

## Silent-loss detection time

How quickly is a missing event discovered?

## Event-related incident rate

How many production incidents arise from event semantics, ordering, duplication or consumer failure?

## Common mistakes

## Mistake 1: Calling every asynchronous message an event

Commands, events and data replication have different contracts.

## Mistake 2: Publishing technical changes as business facts

Consumers become coupled to source internals.

## Mistake 3: Assuming exactly-once business processing

Reliable delivery still requires idempotent consumers.

## Mistake 4: Assuming events arrive in order

Object version and sequence rules must be explicit.

## Mistake 5: Ignoring the dual-write problem

A committed transaction can exist without its event.

## Mistake 6: Acknowledging before durable receipt

A consumer can lose the event after acknowledgement.

## Mistake 7: Retrying permanent business errors

The same invalid data is processed repeatedly.

## Mistake 8: Treating dead-letter storage as resolution

Failed messages need owners and recovery.

## Mistake 9: Replaying events without controlling side effects

Customers may receive repeated communication or duplicate transactions.

## Mistake 10: Changing schemas without consumer governance

Loose coupling does not remove version dependencies.

## Mistake 11: Measuring only broker health

The business process may remain incomplete.

## Mistake 12: Building event chains with no end-to-end owner

No team understands the complete business result.

## Questions architects and managers should ask

1. Is this message a command, business event, technical event or data-change notification?
2. What exact business fact has occurred?
3. At what transaction point is the event valid?
4. Which system is authoritative?
5. How is the event linked to the committed transaction?
6. Can the event be delivered more than once?
7. Can the consumer perform the action more than once safely?
8. Does ordering matter for this business object?
9. How long may consumers remain inconsistent?
10. Which consumers are mandatory?
11. How is downstream completion verified?
12. What happens when a consumer is unavailable?
13. Who owns dead-letter recovery?
14. Can the event be replayed safely?
15. How are schema and semantic changes versioned?
16. What sensitive data should not be placed in the event?
17. Can the complete process be reconstructed from correlation data?
18. Does the architecture need choreography, orchestration or both?
19. How will missing events be detected?
20. Does event-driven design reduce coupling or only hide it?

## The goal is controlled asynchronous independence

Event-driven architecture can make SAP landscapes more responsive and flexible.

Publishers do not need to call every consumer directly.

Consumers can evolve independently.

New applications can react to existing business facts.

Temporary unavailability does not always stop the source transaction.

SAP Integration Suite currently presents event-driven integration as part of a unified integration platform spanning APIs, applications, B2B, hybrid environments and agentic scenarios, with centralized governance, monitoring and security.

But asynchronous independence comes with new obligations:

- semantic contracts;
- idempotency;
- object versioning;
- consumer ownership;
- replay control;
- reconciliation;
- business observability.

The broker can deliver events.

It cannot guarantee that the distributed business process is correct.

The strongest event-driven architecture is not the one with the largest number of events.

It is the one where the organization can answer:

- what happened;
- which systems needed to react;
- which reactions completed;
- which remain delayed;
- whether anything happened twice;
- whether the final business state is correct.

That is the point where event-driven integration becomes an operating model rather than a collection of asynchronous messages.

---

## Event-driven SAP integration checklist

- [ ] Commands, events and data-change messages are separated.
- [ ] Every event describes a committed business fact.
- [ ] Event names and schemas use stable business meaning.
- [ ] The authoritative system is explicit.
- [ ] Event and business-object identities are separate.
- [ ] Object version or sequence is included where order matters.
- [ ] Consumers are designed for duplicate delivery.
- [ ] Business operations are idempotent where required.
- [ ] The publication process is linked reliably to the business commit.
- [ ] Publication failures and delay are monitored.
- [ ] Notification and data-carrying event strategies are chosen deliberately.
- [ ] Eventual-consistency limits are approved by the business.
- [ ] Mandatory and optional consumers are distinguished.
- [ ] Consumers persist events before risky processing.
- [ ] Temporary and permanent failures use different recovery.
- [ ] Dead-letter queues have owners and age limits.
- [ ] Replay does not repeat uncontrolled side effects.
- [ ] Event schemas and semantics are versioned.
- [ ] Topics and access follow domain and security boundaries.
- [ ] Correlation and causation identifiers support tracing.
- [ ] Broker delivery and business completion are measured separately.
- [ ] Reconciliation detects missing and duplicate processing.
- [ ] Choreography has end-to-end ownership.
- [ ] AI agents triggered by events operate inside defined guardrails.
- [ ] Event catalogues include owners, consumers and lifecycle status.

## Sources and further reading

SAP currently describes Event Mesh as supporting distribution of business events across SAP and third-party cloud and hybrid landscapes, real-time subscription-based reactions and reliable asynchronous communication without tight coupling. SAP describes advanced event mesh as supporting distributed brokers, high-volume event streaming, resilient delivery and event-flow monitoring.

SAP currently positions SAP Integration Suite as a unified integration platform for SAP and third-party applications, APIs, events, B2B connections, data and AI agents. Its current product description includes event-driven integration, centralized governance, real-time monitoring, security and visibility into distributed event flows.

*Reviewed: July 2026. SAP Integration Suite and Event Mesh capabilities, packaging and supported scenarios can change. Event contracts, delivery semantics and recovery designs should be validated against current SAP documentation and the behaviour of the actual publishing and consuming systems.*
