---
layout: blog
title: "Modern SAP Integrations: How to Choose Between APIs, Events, Files, Queues, and Mapping Strategies"
description: "The team discusses REST, OData, Kafka, Event Mesh, IDocs, webhooks and SAP Integration Suite."
slug: modern-sap-integrations-how-to-choose-between-apis-events-files-queues
permalink: /blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP integration architecture"
tags:
  - sap-integration-architecture
  - integration
canonical_url: https://dkharlanau.github.io/blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 28
migration_sequence: 23
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/where-should-mapping-logic-live-in-modern-sap-integrations/
  - /blog/how-to-design-event-driven-sap-integrations-without-losing-control/
---

## On this page

- [What mapping actually means](#what-mapping-actually-means)
- [Where should mapping logic live?](#where-should-mapping-logic-live)
- [Point-to-point mapping versus a canonical model](#point-to-point-mapping-versus-a-canonical-model)
- [Do not map one system’s internal model directly into every consumer](#do-not-map-one-system-s-internal-model-directly-into-every-consumer)
- [Versioning is part of mapping design](#versioning-is-part-of-mapping-design)
- [Error handling should be designed before the happy path](#error-handling-should-be-designed-before-the-happy-path)
- [Reconciliation is different from monitoring](#reconciliation-is-different-from-monitoring)
- [A practical selection framework](#a-practical-selection-framework)
- [A practical decision table](#a-practical-decision-table)
- [Hybrid patterns are normal](#hybrid-patterns-are-normal)
- [Example: customer order integration](#example-customer-order-integration)
- [Example: supplier master data distribution](#example-supplier-master-data-distribution)
- [Integration governance should be lightweight but real](#integration-governance-should-be-lightweight-but-real)
- [A mapping registry is often more valuable than another diagram](#a-mapping-registry-is-often-more-valuable-than-another-diagram)
- [AI can assist integration work, but it should not define semantics](#ai-can-assist-integration-work-but-it-should-not-define-semantics)
- [Common mistakes](#common-mistakes)
- [Questions architects and managers should ask](#questions-architects-and-managers-should-ask)
- [A practical implementation sequence](#a-practical-implementation-sequence)
- [The goal is not the most modern protocol](#the-goal-is-not-the-most-modern-protocol)

An integration project begins with a familiar question:

> Should we use an API or an event?

The team discusses REST, OData, Kafka, Event Mesh, IDocs, webhooks and SAP Integration Suite.

Several architecture diagrams are created.

But the most important questions remain unanswered:

- What business result should move between the systems?
- Does the receiving system need an immediate answer?
- Which system owns the meaning of the data?
- What happens when the target system is unavailable?
- Can the same message be processed twice?
- Does the order of messages matter?
- Where should business rules and mappings live?
- How will the complete process be reconciled?

The technology choice is important.

It should not be the first decision.

A modern integration architecture starts by defining the interaction between business capabilities. Only then should the team select APIs, events, messages, files or partner standards.

SAP currently positions SAP Integration Suite as an integration platform covering application and process integration, API management, event-driven integration, B2B, hybrid landscapes and agentic integration scenarios. It supports SAP and third-party environments through APIs, events, adapters, prebuilt content and integration flows.

That provides a broad technical platform.

It does not automatically provide a good integration architecture.

### Integration is a business contract between systems

An interface is often described technically:

- send an IDoc;
- call an API;
- publish an event;
- upload a file;
- run an integration flow.

The real contract is wider.

For example:

> When a supplier is approved in the governance system, all systems that require the supplier should receive the approved identity and organizational data, reject invalid local values and report whether the supplier is ready for business use.

This contract defines:

- trigger;
- data;
- ownership;
- expected result;
- failure behaviour;
- confirmation;
- recovery.

The protocol is only one implementation decision.

If the business contract is unclear, changing from IDoc to REST will not solve the problem.

It will create a modern interface with the same unclear ownership.

### Begin with the interaction type

Most integrations can be understood through a small number of interaction patterns.

### 1. Query

One system needs information from another system now.

Examples:

- retrieve customer credit status;
- check product availability;
- read an order status;
- request current pricing;
- look up a supplier.

The caller expects a response.

A synchronous API is often appropriate.

### 2. Command

One system requests that another system perform an action.

Examples:

- create a sales order;
- block a supplier;
- start a workflow;
- cancel a delivery;
- release a payment proposal.

A command can be synchronous or asynchronous.

The correct choice depends on whether the caller needs immediate confirmation of the final result.

### 3. Event

A system announces that something has already happened.

Examples:

- sales order created;
- business partner changed;
- goods issue posted;
- invoice cancelled;
- supplier approved.

The publisher should not need to know every consumer.

An event-driven approach may be appropriate.

SAP currently describes Event Mesh as supporting publication and subscription of business events across SAP and third-party hybrid landscapes, with reliable asynchronous communication and reduced tight coupling between systems.

### 4. Bulk synchronization

A large quantity of data must be transferred or synchronized.

Examples:

- daily product catalogue;
- historical transactions;
- complete supplier extract;
- opening balances;
- analytical data.

A file, batch API or data integration process may be more efficient than thousands of individual synchronous calls.

### 5. Partner document exchange

The integration connects external companies using established business documents.

Examples:

- purchase order;
- order confirmation;
- delivery advice;
- invoice;
- shipping instruction.

EDI, B2B standards and trading-partner management may be more appropriate than a custom REST interface.

SAP Integration Suite currently includes B2B and EDI capabilities such as partner management, validation, message mapping, reusable templates and centralized monitoring.

These interaction types should not be mixed without a reason.

An event is not simply a faster API.

An API is not automatically better than a file.

### When a synchronous API is the right choice

A synchronous API works well when:

- the caller needs an immediate answer;
- the transaction is relatively short;
- the target can respond within a controlled time;
- the caller can handle a failure;
- one request has one clear response;
- the interaction requires current data.

Examples include:

- availability check;
- price calculation;
- validation;
- customer status lookup;
- small transactional creation with immediate confirmation.

A synchronous API creates a direct dependency.

The caller depends on:

- target availability;
- network;
- response time;
- authentication;
- API version;
- capacity.

This is acceptable when the business interaction itself requires immediate feedback.

For example, an order-entry application may need to know immediately whether a material is valid.

It may not need to wait synchronously until the complete warehouse fulfilment process finishes.

### The synchronous-chain problem

A modern application may call several services:

1. customer service;
2. pricing service;
3. availability service;
4. tax service;
5. credit service;
6. order service.

Each service may be healthy most of the time.

The complete chain becomes less reliable as dependencies increase.

A slow response in one system delays the whole process.

This is why synchronous integration should be used for required immediate decisions, not for every downstream action.

A common stronger pattern is:

1. validate essential information synchronously;
2. accept the transaction;
3. continue downstream processing asynchronously;
4. report final status later.

### When an event is the right choice

Events are useful when one system needs to inform other systems about a completed business-state change.

Good event candidates include:

- customer created;
- purchase order approved;
- goods receipt posted;
- employee changed;
- delivery completed.

Events are especially useful when:

- several consumers may be interested;
- consumers should be loosely coupled from the producer;
- processing can happen asynchronously;
- the publisher should not wait for every subscriber;
- transaction volumes may arrive in bursts.

SAP describes event-driven integration as enabling real-time event distribution, immediate reaction to business changes and loose coupling across distributed landscapes.

### An event should describe a fact

A useful event name usually uses past tense:

- `SalesOrder.Created`
- `BusinessPartner.Changed`
- `Delivery.GoodsIssuePosted`

The event announces that something occurred.

It should not be a hidden remote command such as:

- `PleaseCreateInvoice`
- `UpdateThisCustomerNow`

Commands and events have different meaning.

A command has an intended receiver and expected action.

An event announces a fact and may have several consumers.

Confusing them creates unclear responsibility.

### Events introduce eventual consistency

With synchronous integration, the caller may receive an immediate result.

With events, different systems may update at different times.

For a short period:

- SAP S/4HANA may contain the new customer;
- CRM may still contain the old data;
- the data platform may not have processed the event;
- a downstream application may be temporarily unavailable.

This is eventual consistency.

The business process must tolerate it.

Before selecting events, ask:

- How long can systems be inconsistent?
- Which system remains authoritative?
- Can users see stale data?
- What happens when a subscriber is delayed?
- Can the event be replayed?
- How is missing consumption detected?

Event-driven architecture is not simply real-time integration.

It is a different consistency model.

### Events require idempotency

An event may be delivered more than once.

A consumer should recognize that it has already processed the same business event.

Useful identifiers include:

- event ID;
- business object ID;
- object version;
- source-system timestamp;
- sequence number.

Without duplicate control, repeated event delivery may create:

- duplicate orders;
- duplicate notifications;
- repeated workflow tasks;
- repeated financial effects.

The consumer must be designed for repeated delivery.

### Event ordering must be explicit

Consider the sequence:

1. customer created;
2. customer changed;
3. customer blocked.

If consumers receive the events in another order, the final state may be wrong.

Ordering can matter by:

- business object;
- account;
- document;
- aggregate;
- partition.

Do not assume global ordering.

Define:

- which events must stay in sequence;
- how versions are compared;
- what happens when an older event arrives late;
- whether consumers can retrieve the current authoritative state.

A useful pattern is to include an object version and allow the consumer to ignore older updates.

### When a message queue is the right choice

A queue supports asynchronous work between a sender and a receiver.

It is useful when:

- the sender should not wait for completion;
- work must survive temporary target unavailability;
- load needs buffering;
- processing should be retried;
- one consumer should process a command.

Examples include:

- create a business document asynchronously;
- process an image;
- send a customer communication;
- execute a background action;
- transfer a transaction to a slower target.

A queue is different from a public business event.

A queued command usually expects one processing responsibility.

An event may have many independent subscribers.

### Queues absorb load but do not remove it

A queue can protect a target from sudden traffic.

It does not solve insufficient processing capacity.

If the producer creates 100,000 messages per hour and the consumer handles 60,000, the backlog continues to grow.

Monitoring should include:

- queue length;
- oldest message age;
- processing rate;
- retry count;
- dead-letter volume;
- business priority.

A queue that accepts every message can still hide a failing business process.

### When files and batch integration are still correct

Files are often described as legacy integration.

That is too simplistic.

A file can be a good solution when:

- a large data volume is transferred periodically;
- the partner supports established file formats;
- immediate processing is not required;
- the complete dataset must be reconciled;
- restart and audit are important;
- the source cannot provide reliable APIs or events.

Examples include:

- daily bank statements;
- large supplier catalogues;
- payroll files;
- EDI batches;
- historical data loads;
- regulatory submissions.

A file has advantages:

- clear transfer boundary;
- easy archival;
- complete batch count;
- controlled replay;
- simple reconciliation.

It also has weaknesses:

- delayed processing;
- large failure scope;
- difficult partial correction;
- less immediate status;
- file-level rather than transaction-level feedback.

The correct question is not whether a file is modern.

It is whether the interaction requirements justify batch transfer.

### Avoid file interfaces for one-record real-time processes

A file is a weak choice when:

- users need immediate confirmation;
- transactions arrive continuously;
- individual failures need immediate handling;
- the source generates very small updates;
- the target supports stable transactional APIs.

Creating files every few minutes may combine the weaknesses of batch and real-time integration.

### B2B integrations need partner governance

External partner integrations differ from internal application connections.

Partners may have:

- different identifiers;
- different standards;
- different message versions;
- different onboarding processes;
- different security methods;
- different operational contacts.

One standard purchase-order structure may need a different implementation for each customer or supplier.

This is where partner-specific mapping and trading-partner management are justified.

The architecture should distinguish:

#### Core business message

The company’s internal meaning of an order, invoice or delivery.

#### Partner representation

How a specific partner sends or receives the message.

Partner-specific differences should not change the internal business meaning.

### API management is not application integration

An API gateway or API management layer can:

- secure APIs;
- apply policies;
- manage access;
- monitor usage;
- control versions;
- provide developer onboarding;
- collect analytics.

SAP currently positions API Management around security policies, centralized governance, API analytics, anomaly detection, developer discovery and lifecycle management.

API management should not become the main location for complex business-process logic.

A gateway policy can:

- validate a token;
- apply a rate limit;
- transform a header;
- route versions;
- mask selected data.

It should not normally contain the complete order-creation business process.

Keeping business logic in an API gateway makes it:

- difficult to test;
- difficult to find;
- tightly coupled to the gateway;
- invisible to process owners.

### Integration logic and API products are different

A reusable API exposes a stable business capability.

An integration flow connects a specific process between systems.

For example:

#### Business API

`Create Sales Order`

#### Integration flow

Receive a partner EDI order, validate partner identifiers, map it to the sales-order API, call the API, process the response and send an order confirmation.

The API should remain reusable.

The integration flow handles partner and process-specific orchestration.

### Use prebuilt APIs and integration content carefully

SAP provides APIs, events and integration content through its product ecosystem and SAP Business Accelerator Hub. SAP Integration Suite also promotes thousands of prebuilt integrations and accelerators.

Prebuilt content can reduce implementation effort.

It should still be reviewed for:

- actual product version;
- required fields;
- business assumptions;
- extensions;
- error handling;
- volume;
- security;
- lifecycle ownership.

Prebuilt does not mean production-ready for every customer.

It means the starting point is stronger than creating everything from zero.

## What mapping actually means

Teams often use the word “mapping” for several different activities.

These activities should be separated.

### 1. Structural mapping

Transforms one message structure into another.

Example:

```text
Source.Customer.Address.PostalCode
→
Target.BusinessPartner.StandardAddress.PostCode
```

This is technical transformation.

### 2. Value mapping

Converts one system’s code into another system’s code.

Example:

```text
Source country value: DEU
Target country value: DE
```

Or:

```text
Partner unit: EACH
SAP unit: EA
```

This is not only technical.

Someone must own the equivalence.

### 3. Semantic mapping

Determines whether two fields have the same business meaning.

Example:

```text
RequestedDeliveryDate
```

may mean:

- date requested by customer;
- date goods should leave the warehouse;
- date goods should arrive;
- date currently confirmed.

The field names may look similar.

The meanings may be different.

Semantic mapping is the most important and most frequently underestimated type.

### 4. Enrichment

Adds information that the source does not contain.

Example:

- source sends customer ID;
- integration retrieves sales organization;
- target message includes both.

Enrichment creates a dependency on the enrichment source.

The architecture should define what happens when enrichment is unavailable.

### 5. Derivation

Calculates a value from rules.

Example:

- determine company code from plant;
- determine order type from partner and process;
- derive shipping condition from service level.

Derivation may contain business logic.

It needs an owner.

### 6. Aggregation and splitting

One source message may become several target messages.

Or several source messages may become one target object.

Examples:

- split one global supplier record by target company;
- aggregate usage events into a billing record;
- combine order lines by delivery group.

This affects transaction boundaries and reconciliation.

It is more than field mapping.

### Mapping is a business design artefact

A mapping should not be only a graphical line between two fields.

For every important mapped value, record:

- source field;
- source definition;
- target field;
- target definition;
- transformation rule;
- default;
- validation;
- owner;
- exception treatment;
- effective version.

For example:

| Element | Definition |
|---|---|
| Source field | `deliveryDate` |
| Source meaning | Customer-requested arrival date |
| Target field | Requested delivery date |
| Transformation | Convert customer timezone to plant calendar date |
| Required enrichment | Customer ship-to timezone |
| Exception | Missing timezone creates manual review |
| Owner | Order fulfilment process owner |

This is a real mapping specification.

A line connecting two fields is not enough.

## Where should mapping logic live?

This is one of the most important integration decisions.

Mapping can live in:

- source application;
- target application;
- middleware;
- API facade;
- data platform;
- partner gateway.

There is no universal answer.

Use ownership and reuse to decide.

### Put logic in the source when the source owns the meaning

The source should provide a standardized value when:

- the source understands the business meaning best;
- several consumers need the same interpretation;
- the transformation is part of the source domain;
- publishing internal technical codes would create unnecessary coupling.

For example, a warehouse system should publish a stable business status instead of forcing every consumer to interpret internal status tables.

### Put logic in the target when it is target-specific

The target should handle logic when:

- the rule is unique to the target;
- the target owns local validation;
- the target derives its own internal fields;
- other consumers should not know target-specific codes.

For example, a target system may determine its internal document category from an external order type.

That rule may belong in the target domain.

### Put logic in middleware when it connects representations

Middleware is the right location for:

- protocol conversion;
- structural mapping;
- partner-specific formats;
- routing;
- message splitting;
- aggregation;
- cross-system correlation;
- controlled enrichment;
- technical value mapping.

SAP Cloud Integration supports design, execution and monitoring of integration flows for A2A, B2B and B2G scenarios, as well as message mapping and connectivity between SAP and third-party applications.

Middleware should translate between systems.

It should not silently become the owner of every business rule.

### The hidden-business-logic problem

Integration middleware often accumulates rules such as:

- if customer is from country X, use sales organization Y;
- if order value exceeds a limit, change order type;
- if supplier category is missing, derive it from material group;
- if tax code is blank, apply a default.

These rules may be necessary.

But they represent business decisions.

When they exist only in integration flows:

- business owners may not know them;
- source and target systems show no explanation;
- testing becomes difficult;
- changes in one interface do not update others;
- different flows implement different versions.

A useful rule is:

> Middleware can execute a business rule, but it should not own the business meaning of that rule.

Every such rule needs:

- accountable owner;
- source of truth;
- documented reason;
- version;
- test cases;
- review date.

## Point-to-point mapping versus a canonical model

Suppose five systems exchange customer data.

A direct point-to-point design may require many mappings:

- A to B;
- A to C;
- B to D;
- C to D;
- D to E.

A canonical model introduces a shared representation:

- source to canonical;
- canonical to target.

This can reduce mapping duplication.

It can also create a large central model that nobody can change.

### When a canonical model helps

A canonical model is useful when:

- many systems exchange the same business object;
- the shared meaning is stable;
- multiple integrations reuse the same representation;
- the company can govern common definitions;
- source and target changes should be isolated.

Examples include bounded models for:

- business partner;
- product;
- order;
- shipment;
- invoice.

### When a canonical model becomes harmful

A universal enterprise model may become:

- too large;
- politically difficult;
- slow to change;
- filled with optional fields;
- disconnected from real system behaviour;
- another transformation layer.

Teams then map:

> source → universal model → local model → target

without creating practical simplification.

### Prefer bounded canonical models

Instead of one model for the whole enterprise, use a smaller model for a clear domain or process.

Examples:

- order fulfilment model;
- supplier onboarding model;
- warehouse event model;
- billing-event model.

The model should contain only the information required by that domain.

This reduces governance overhead and improves meaning.

## Do not map one system’s internal model directly into every consumer

A common integration design exposes internal source structures.

Every consumer then depends on:

- internal field names;
- internal status values;
- database-oriented relationships;
- source-specific extensions.

When the source changes, every consumer must change.

A stronger design exposes a stable business contract.

This is one reason APIs and events should be treated as products rather than technical endpoints.

The published contract should be understandable without knowing the source system’s internal tables.

## Versioning is part of mapping design

Mappings change because:

- source adds a field;
- target changes validation;
- business meaning changes;
- partner upgrades an EDI version;
- an old code is retired;
- a new country or organization is added.

A mapping should have a version.

The team should know:

- which message version it accepts;
- which version it produces;
- whether old and new versions can run together;
- how consumers are notified;
- how historical messages are replayed;
- how rollback works.

### Additive changes are safer

Adding an optional field is usually easier to manage than:

- renaming a field;
- changing its meaning;
- changing data type;
- removing a value;
- making an optional field mandatory.

Backward compatibility should be an explicit design goal.

### Events need schema governance

An event is a published contract.

Changing the event structure without control can break many consumers that the publisher does not know.

Event governance should include:

- owner;
- schema;
- version;
- required fields;
- semantic definitions;
- compatibility policy;
- consumer communication;
- deprecation period.

Loose coupling does not mean no governance.

It means the producer and consumer are connected through a stable contract rather than direct implementation knowledge.

## Error handling should be designed before the happy path

Every integration should answer:

- What can fail?
- Where is the failure recorded?
- Who owns it?
- Can it be retried?
- Can it create duplicates?
- How is partial processing detected?
- How is business completion verified?
- How is a message replayed?
- When must processing stop?

The answer should differ by integration style.

### API failure

Possible actions:

- return a clear error;
- allow caller retry;
- use idempotency key;
- create asynchronous follow-up;
- avoid ambiguous timeout.

### Event failure

Possible actions:

- retain message;
- retry consumer processing;
- use dead-letter queue;
- replay from known position;
- alert when consumer lag grows.

### File failure

Possible actions:

- reject complete file;
- process valid rows and report rejects;
- archive original file;
- create reconciliation totals;
- restart from controlled checkpoint.

### B2B failure

Possible actions:

- send technical acknowledgement;
- send functional acknowledgement;
- notify partner;
- retain partner document;
- use agreed correction protocol.

Error handling is part of the interface contract.

It should not be invented during the first production incident.

## Reconciliation is different from monitoring

Monitoring answers:

- Did the message move?
- Was the endpoint available?
- Did the integration flow finish?
- Is the queue growing?

Reconciliation answers:

- Did every expected business transaction arrive?
- Was any transaction duplicated?
- Was the correct target document created?
- Do source and target totals agree?
- Is the complete business process finished?

An interface can be technically green and commercially incomplete.

Every critical integration should define a reconciliation method.

Examples:

- source order count versus target order count;
- sent supplier IDs versus created business partners;
- goods issues versus warehouse confirmations;
- rated events versus invoices;
- payment file totals versus posted payments.

### Do not rely only on transport-level success

HTTP 200 means that a request was accepted or processed according to the API contract.

It does not necessarily prove:

- downstream workflow completed;
- document was financially correct;
- related systems updated;
- business user can continue.

Technical acknowledgement and business completion should be measured separately.

## A practical selection framework

Use the following questions before choosing the integration style.

### Does the caller require an immediate answer?

- Yes: consider synchronous API.
- No: consider event, queue or batch.

### Is the interaction a request or a fact?

- Request: API or queued command.
- Fact: event.

### Is there one receiver or many potential consumers?

- One controlled receiver: API or queue.
- Many independent consumers: event.

### Is the volume continuous or periodic?

- Continuous: API, queue or event.
- Large periodic volume: file or bulk interface.

### Must processing survive target downtime?

- Yes: queue, event broker or persistent integration layer.
- Synchronous API alone may be insufficient.

### Does message order matter?

- If yes, design sequence and partitioning explicitly.

### Can the same message be processed twice safely?

- If no, add idempotency and duplicate control.

### Is the data format industry-standard?

- If yes, consider B2B or EDI standards before custom design.

### Is this operational transaction flow or analytical replication?

- Operational: APIs, events, messaging or B2B.
- Analytical: data replication or data platform patterns may be more suitable.

## A practical decision table

| Requirement | Preferred starting pattern | Main risk |
|---|---|---|
| Immediate lookup | Synchronous API | Runtime dependency |
| Immediate validation | Synchronous API | Chain latency |
| Create work asynchronously | Queue or asynchronous API | Duplicate execution |
| Announce business-state change | Event | Eventual consistency |
| Multiple independent consumers | Event | Schema and consumer governance |
| High-volume periodic transfer | File or bulk API | Delayed error discovery |
| External partner document | B2B/EDI | Partner-specific variation |
| Large analytical replication | Data integration | Confusing analytics with operations |
| Real-time user transaction | API | Target availability |
| Buffer traffic spikes | Queue | Growing hidden backlog |

This table is a starting point.

Real processes often combine several patterns.

## Hybrid patterns are normal

A modern process may use more than one integration style.

For example, sales order processing may use:

1. synchronous API to validate customer and material;
2. synchronous API to create the sales order;
3. event to announce that the order was created;
4. queue to trigger a slower fulfilment action;
5. file to send a daily forecast to a partner;
6. reconciliation job to compare order and fulfilment results.

This is not architectural inconsistency.

Different interactions have different requirements.

The mistake is choosing one technology for every scenario because it is the current strategic platform.

## Example: customer order integration

Consider an external commerce platform creating orders in SAP.

### Weak design

- Commerce sends a large custom JSON structure.
- Middleware contains pricing, plant and order-type logic.
- Middleware calls several SAP services.
- On timeout, commerce repeats the request.
- Duplicate orders sometimes appear.
- No end-to-end business reference exists.

### Stronger design

#### Step 1: Define the contract

The commerce platform sends:

- external order ID;
- customer;
- items;
- quantities;
- requested delivery information;
- approved commercial context.

#### Step 2: Use a stable business API

The API creates the SAP sales order using an idempotency or external reference.

#### Step 3: Keep business logic with the owner

SAP owns:

- order type;
- organizational determination;
- pricing;
- availability;
- blocks.

Middleware handles:

- authentication;
- structural transformation;
- protocol;
- technical routing;
- controlled value mappings.

#### Step 4: Return a clear result

The API returns:

- SAP sales order number;
- accepted or rejected status;
- business errors;
- correlation ID.

#### Step 5: Publish later changes

Events announce:

- order confirmed;
- delivery created;
- order cancelled.

#### Step 6: Reconcile

The company compares external order IDs with SAP order IDs and detects missing or duplicate transactions.

This architecture separates responsibilities.

## Example: supplier master data distribution

Consider central governance distributing suppliers to several ERP systems.

### Possible pattern

1. Governance system activates supplier.
2. Business event announces approved change.
3. Distribution service retrieves or receives approved data.
4. Mapping converts the central representation to target-specific formats.
5. Each target confirms technical processing.
6. Target-readiness checks confirm required company and purchasing data.
7. Exceptions are routed to data owners.

### Mapping ownership

- central system owns supplier identity;
- local target owns local organizational requirements;
- middleware handles structural and technical transformation;
- business owners approve local extensions;
- reconciliation confirms target usability.

The integration should not mark success only because the message was delivered.

## Integration governance should be lightweight but real

SAP currently provides Integration Assessment and the SAP Integration Solution Advisory Methodology as tools and frameworks for evaluating landscapes, applying reference architectures and managing integration as a governed discipline.

The governance process does not need to become a large architecture committee.

Every important integration should still have:

- business owner;
- technical owner;
- integration pattern;
- source of truth;
- data contract;
- security classification;
- error model;
- reconciliation;
- lifecycle state;
- review date.

### Build an integration catalogue

A useful catalogue records:

- interface name;
- business purpose;
- source and target;
- business objects;
- interaction type;
- API, event, queue, file or B2B pattern;
- frequency and volume;
- criticality;
- owner;
- mapping owner;
- monitoring;
- recovery;
- dependencies;
- current version.

This catalogue is more useful than a list of technical endpoints.

It helps answer:

- Which business process fails if this interface stops?
- Which interfaces use this customer mapping?
- Which consumers use this event?
- Which integrations depend on one certificate?
- Which interfaces are still point to point?
- Which mappings duplicate the same business rule?

## A mapping registry is often more valuable than another diagram

Mappings are frequently stored inside individual integration flows.

The organization cannot easily see:

- where one value is translated;
- whether two flows use the same rule;
- who approved a code mapping;
- which mappings are obsolete;
- which business objects are inconsistent.

A mapping registry can contain:

- mapping ID;
- source system;
- target system;
- business object;
- field or value;
- rule;
- owner;
- version;
- effective date;
- affected interfaces;
- test evidence.

This turns mapping from hidden implementation detail into governed operational knowledge.

## AI can assist integration work, but it should not define semantics

SAP currently promotes AI-assisted integration development, including generated integration flows and mapping recommendations.

AI can help:

- propose field mappings;
- identify similar integration content;
- generate transformation drafts;
- explain message structures;
- summarize failures;
- generate test cases.

But AI cannot determine business equivalence only from field names.

For example:

```text
CustomerType
```

may refer to:

- legal classification;
- sales segment;
- account group;
- retail versus wholesale;
- credit category.

A generated mapping should be reviewed by someone who understands both source and target meaning.

AI can accelerate mapping preparation.

It should not become the owner of semantic truth.

## Common mistakes

### Mistake 1: Choosing REST for every new integration

REST is useful, but not every process needs synchronous request-response.

### Mistake 2: Using events for commands

A fact and a requested action have different ownership.

### Mistake 3: Treating files as automatically obsolete

Batch can be correct for large, periodic and auditable transfers.

### Mistake 4: Hiding business rules in middleware

Integration logic becomes an unofficial decision system.

### Mistake 5: Creating one universal canonical model

A model designed for everyone may become useful to nobody.

### Mistake 6: Mapping fields by name

Similar names do not prove the same meaning.

### Mistake 7: Ignoring duplicate and sequence behaviour

Reliable delivery does not guarantee correct business processing.

### Mistake 8: Measuring only message success

Technical delivery does not prove business completion.

### Mistake 9: Publishing events without schema ownership

Loose coupling still requires stable contracts.

### Mistake 10: Creating point-to-point mappings repeatedly

The same business translation is implemented differently across interfaces.

### Mistake 11: Putting complex orchestration in API policies

API management and business-process integration serve different purposes.

### Mistake 12: Starting with the platform instead of the interaction

A product cannot compensate for an unclear business contract.

## Questions architects and managers should ask

1. What business result does the integration support?
2. Is the interaction a query, command, event, bulk transfer or partner document?
3. Does the caller need an immediate response?
4. Which system owns the data meaning?
5. How long can systems remain inconsistent?
6. Can the transaction be processed twice safely?
7. Does event or message order matter?
8. What happens when the target is unavailable?
9. Where does each mapping rule belong?
10. Which rules represent business decisions?
11. Is a canonical model justified by real reuse?
12. How are schemas and mappings versioned?
13. How is business completion verified?
14. Can failed processing be replayed safely?
15. Who owns the interface after go-live?
16. Can the company trace one business transaction end to end?
17. Does the selected pattern reduce coupling or only move it?

## A practical implementation sequence

### Phase 1: Define the business interaction

Document:

- trigger;
- purpose;
- source;
- target;
- business result;
- ownership.

### Phase 2: Classify the pattern

Choose:

- query;
- command;
- event;
- bulk;
- B2B.

### Phase 3: Define consistency and timing

Specify:

- immediate or asynchronous;
- allowed delay;
- ordering;
- availability dependency.

### Phase 4: Define the data contract

Document:

- fields;
- meaning;
- required values;
- identifiers;
- version.

### Phase 5: Assign mapping ownership

Separate:

- source-owned meaning;
- target-specific logic;
- middleware transformation;
- governed business rules.

### Phase 6: Design failure behaviour

Define:

- retry;
- duplicate control;
- dead-letter handling;
- manual fallback;
- replay.

### Phase 7: Define reconciliation

Prove that the expected business objects were created correctly.

### Phase 8: Implement with reusable platform capabilities

Use standard APIs, events, adapters and prebuilt integration content where they fit.

### Phase 9: Test difficult conditions

Include:

- target unavailable;
- duplicate message;
- missing field;
- late event;
- incorrect order;
- schema version mismatch;
- partial processing.

### Phase 10: Operate the integration as a product

Maintain:

- owner;
- monitoring;
- mapping;
- documentation;
- versions;
- deprecation;
- performance;
- recovery.

## The goal is not the most modern protocol

A modern integration is not defined by using REST, events or cloud middleware.

A modern integration has:

- clear business ownership;
- stable contracts;
- deliberate coupling;
- controlled mappings;
- safe failure behaviour;
- end-to-end observability;
- version management;
- reconciliation.

A file-based interface with complete reconciliation and clear ownership may be more reliable than a poorly designed real-time API.

An event-driven architecture without idempotency and schema governance may be less modern than a controlled message queue.

An API with business rules hidden in middleware may be harder to change than an old IDoc.

SAP Integration Suite provides current capabilities for application integration, APIs, events, B2B connectivity, governance and hybrid landscapes.

The platform gives teams options.

Architecture is the discipline of choosing the right option for each business interaction.

The correct starting question is therefore not:

> Which integration technology should we use?

It is:

> What are the business contract, consistency requirement, ownership and failure behaviour of this interaction?

Once those are clear, choosing between an API, event, queue, file or B2B message becomes much easier.

---

### Modern SAP integration checklist

- [ ] The business purpose is defined before the protocol.
- [ ] The interaction is classified as query, command, event, bulk or B2B.
- [ ] Immediate-response requirements are justified.
- [ ] Source and target ownership are explicit.
- [ ] Business identifiers support traceability and duplicate control.
- [ ] Eventual consistency is understood.
- [ ] Ordering requirements are documented.
- [ ] Retry behaviour is safe and limited.
- [ ] Technical acknowledgement and business completion are separated.
- [ ] Mapping specifications include semantic definitions.
- [ ] Business rules hidden in middleware have accountable owners.
- [ ] Canonical models are bounded to real domains.
- [ ] API and event schemas are versioned.
- [ ] Error handling is designed before production.
- [ ] Reconciliation proves completeness and uniqueness.
- [ ] Standard APIs, events and prebuilt content are reviewed before reuse.
- [ ] Monitoring includes queues, failures, age and business impact.
- [ ] Every critical integration has a recovery procedure.
- [ ] Integration and mapping catalogues remain current.
- [ ] Technology selection follows the business interaction.

### Sources and further reading

SAP currently positions SAP Integration Suite as a cloud integration platform supporting application and process integration, API lifecycle management, event-driven architecture, B2B integration, hybrid landscapes and agentic integration scenarios across SAP and third-party environments.

SAP Cloud Integration supports integration flows for application-to-application, business-to-business and business-to-government scenarios, including message mapping, adapters, prebuilt content and hybrid connectivity.

SAP API Management currently provides API security policies, centralized governance, usage analytics, anomaly monitoring, developer discovery and lifecycle management.

SAP Event Mesh currently supports asynchronous publication and subscription of events across hybrid environments, while advanced event mesh supports distributed, high-volume event streaming and event-flow visibility.

SAP Integration Assessment and SAP Integration Solution Advisory Methodology currently provide structured assessment, reference architecture and governance approaches for integration strategy and lifecycle management.

*Reviewed: July 2026. SAP Integration Suite capabilities, packaging, adapters and supported scenarios can change. Architecture decisions should be validated against current SAP documentation, actual source and target systems, transaction volumes and business-control requirements.*

## Continue exploring

- [Where Should Mapping Logic Live in Modern SAP Integrations?](/blog/where-should-mapping-logic-live-in-modern-sap-integrations/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [Where Automation Actually Makes Sense in SAP SD Sales Order Processing](/blog/where-automation-actually-makes-sense-in-sap-sd-sales-order-processing/)
- Next in the migration: [Where Should Mapping Logic Live in Modern SAP Integrations?](/blog/where-should-mapping-logic-live-in-modern-sap-integrations/)
