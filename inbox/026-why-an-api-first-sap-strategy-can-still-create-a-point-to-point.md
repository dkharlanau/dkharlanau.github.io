# Why an API-First SAP Strategy Can Still Create a Point-to-Point Integration Mess

A company decides to modernize its SAP integrations.

The architecture principle is clear:

> All new integrations must use APIs.

Old files, RFC connections, IDocs and direct database access should gradually disappear.

The programme begins well.

A customer portal receives an order API. A warehouse application receives a delivery API. A procurement platform receives a supplier API. A new mobile application gets several lightweight services.

Two years later, the landscape contains hundreds of endpoints.

Many of them expose similar data in different structures. Each consumer uses its own authentication, custom fields, error handling and retry logic. One application needs five API calls to create one business transaction. Another application knows internal SAP document types and organizational codes.

The protocols are modern.

The architecture is still point to point.

This is the main weakness of many API-first programmes.

Replacing an IDoc or file with a REST endpoint does not automatically reduce coupling.

An API creates value when it exposes a stable business capability with clear ownership, controlled lifecycle and predictable behaviour.

It creates another integration problem when it is only a technical wrapper around one application’s internal structure.

The correct objective is not:

> Build APIs for everything.

It is:

> Provide governed business capabilities that applications, partners and agents can use without becoming dependent on SAP implementation details.

## API-first is a design principle, not a protocol policy

API-first should mean that a business capability has a defined contract before individual consumers are implemented.

The contract should explain:

- what the API does;
- which business problem it serves;
- who owns it;
- what data it accepts;
- what result it returns;
- which rules it applies;
- how errors work;
- how versions evolve;
- what service level consumers may expect.

A weak API-first rule says:

> Use REST rather than IDoc.

A stronger rule says:

> Expose reusable, secure and versioned business capabilities through managed contracts, and choose synchronous APIs only when the business interaction requires them.

The first rule modernizes the transport.

The second modernizes the operating model.

## An API is not automatically reusable

Consider an endpoint named:

```text
POST /create-sales-order
```

It may appear reusable.

But the payload requires:

- SAP sales document type;
- sales organization;
- distribution channel;
- division;
- internal partner-function codes;
- item categories;
- SAP material numbers;
- plant;
- pricing condition types.

A consumer must understand the internal SAP sales model before it can call the service.

The API has not reduced coupling.

It has published SAP internals through HTTP.

A business-oriented order API might instead accept:

- external order reference;
- customer identity;
- commercial channel;
- products;
- quantities;
- requested fulfilment;
- agreed offer or contract reference.

SAP or a governed sales-domain service can then determine target-specific values.

This does not mean every API must hide all complexity.

It means consumers should not need implementation details that do not belong to their business purpose.

## APIs should expose capabilities, not tables

A technical API may expose:

- one table;
- one internal structure;
- one application object;
- one CRUD operation.

A capability API exposes something the business can use.

Examples include:

- check product availability;
- submit customer order;
- retrieve order status;
- request supplier onboarding;
- confirm warehouse execution;
- obtain an approved invoice copy.

The difference becomes important when SAP changes.

If the contract follows internal fields, every consumer changes with the source application.

If the contract follows a stable business capability, the internal implementation can evolve while the external promise remains controlled.

This is one of the practical meanings of keeping a clean core.

The SAP core can change without forcing every connected application to understand its internal design.

## Not every SAP object needs a public API

An organization may discover thousands of potential business objects and services.

Publishing all of them does not create useful architecture.

It creates an endpoint catalogue.

A good API candidate normally has:

- a real consumer need;
- clear ownership;
- stable business meaning;
- controlled access;
- expected reuse;
- measurable service expectations.

An internal maintenance operation used by one tightly coupled component may not need to become an enterprise API product.

Publishing an API creates lifecycle obligations:

- security;
- documentation;
- testing;
- monitoring;
- support;
- versioning;
- deprecation.

The API portfolio should therefore be designed, not generated indiscriminately.

## Start with the interaction

Before creating an API, ask what the caller is trying to do.

## Query

The caller needs current information.

Examples:

- retrieve an order;
- check availability;
- read invoice status;
- obtain customer eligibility.

A synchronous API may be appropriate.

## Command

The caller asks the target domain to perform an action.

Examples:

- create an order;
- submit a return request;
- request a supplier extension;
- block a delivery.

The API should return a clear acceptance or business result.

Some commands can complete synchronously.

Others should accept the request and continue asynchronously.

## Process initiation

The caller starts a longer process.

Examples:

- supplier onboarding;
- credit review;
- mass-price update;
- contract change.

A synchronous request should not remain open while the complete process runs.

A stronger pattern is:

1. validate and accept the request;
2. return a process ID;
3. continue asynchronously;
4. expose status;
5. publish completion or failure events.

## Bulk transfer

The caller needs to send or retrieve a large dataset.

A transactional API may not be the best choice.

A bulk API, file transfer or data-integration pattern may be more efficient and easier to reconcile.

API-first does not mean every interaction must use small synchronous REST calls.

## The synchronous API trap

APIs are often used synchronously because it feels simple.

The caller sends a request and receives a response.

But a complete SAP process may require several systems.

For example, an order application may call:

1. customer API;
2. product API;
3. price API;
4. availability API;
5. tax API;
6. credit API;
7. order-creation API.

Each dependency adds:

- latency;
- availability risk;
- authentication;
- rate limits;
- timeout handling;
- version dependency.

A service chain can become fragile even when each individual API is reliable.

The team should decide which information is truly required before accepting the transaction.

Some processing can continue asynchronously after acceptance.

## Do not wait synchronously for a long business process

Suppose a supplier-onboarding API attempts to:

- create the request;
- validate tax data;
- run duplicate checks;
- obtain approvals;
- create the supplier;
- replicate to target systems;
- confirm business readiness.

This may take hours or days.

A single synchronous API cannot represent the complete lifecycle reliably.

The API should create the request and return:

- request ID;
- initial validation result;
- current state;
- status location.

Later progress can be exposed through:

- status API;
- event;
- notification;
- workflow task.

Trying to make every process look like one immediate API transaction produces timeouts, uncertain states and repeated requests.

## API acceptance and business completion are different

An API can return:

```text
202 Accepted
```

This means the request was accepted for processing.

It does not mean:

- the SAP document exists;
- downstream approval completed;
- the warehouse received the order;
- the invoice was posted;
- the complete business process succeeded.

The contract should distinguish:

- request received;
- request validated;
- processing started;
- business object created;
- downstream processing complete;
- final failure.

Consumers should not treat technical acceptance as final success.

## Use stable business identities

An API consumer should not depend only on the target system’s generated number.

For example, an external commerce platform may send order `WEB-739201`.

SAP creates order `50018421`.

Both identifiers should remain connected.

The stable external business key supports:

- idempotency;
- status lookup;
- reconciliation;
- customer support;
- duplicate prevention.

A good transactional API normally supports:

- external request ID;
- source-system identity;
- correlation ID;
- target object ID.

This allows the complete transaction to be traced across systems.

## Idempotency is part of API design

A caller sends a request.

The target creates the SAP order.

Before the response reaches the caller, the network connection fails.

The caller does not know whether the order was created.

It retries.

Without idempotency, the second request may create another order.

The API should allow the caller to submit a stable request key.

The target can then return the original result rather than repeat the business action.

Idempotency is especially important for:

- order creation;
- payment requests;
- invoice creation;
- goods movements;
- workflow initiation;
- master data creation.

A retry strategy without duplicate control is not resilience.

It is repeated risk.

## Timeouts create uncertain outcomes

An HTTP timeout does not prove that the target did nothing.

The target may have:

- received the request;
- completed processing;
- committed the SAP document;
- failed only while sending the response.

The caller should not automatically repeat a high-impact command after every timeout.

A stronger design provides:

- idempotency key;
- request-status lookup;
- correlation ID;
- controlled retry;
- clear timeout semantics.

The question after a timeout is not:

> Should we call the API again?

It is:

> Can we prove whether the original business action completed?

## Errors should be useful to the consumer

An API error such as:

```text
400 Bad Request
```

is technically valid.

It is operationally weak.

The consumer needs to know:

- which field failed;
- whether the problem is technical or business;
- whether retry may help;
- whether input must be corrected;
- whether partial processing occurred;
- which reference should be used for support.

A structured error may contain:

- error code;
- business category;
- human-readable explanation;
- affected field or item;
- retryability;
- correlation ID;
- documentation reference.

Do not expose raw stack traces or internal table messages as the public contract.

Translate internal errors into stable consumer-facing meaning.

## Separate temporary and permanent errors

A temporary error may include:

- target unavailable;
- resource limit;
- temporary lock;
- network failure.

Retry may help.

A permanent business error may include:

- customer blocked;
- unknown material;
- invalid organizational scope;
- missing mandatory approval;
- document already cancelled.

Retrying unchanged input will not help.

The API contract should allow the consumer to distinguish these cases.

Otherwise, clients create aggressive retry loops against permanent errors.

## Do not use HTTP codes as the complete business model

HTTP status codes are useful transport semantics.

They cannot represent every SAP process condition.

For example:

- request accepted but approval required;
- order created with some rejected items;
- transaction complete but customer communication failed;
- object created with a business block.

Use HTTP correctly.

Add a structured business result.

The consumer should not need to interpret `200` as proof that every business outcome succeeded.

## API composition can recreate the monolith outside SAP

A team may create one composite API that calls:

- customer;
- product;
- pricing;
- availability;
- credit;
- tax;
- order;
- workflow.

The composite service becomes the new central process engine.

This may be justified when it represents one stable business capability.

It becomes dangerous when:

- it owns many domain rules;
- every consumer needs a different variation;
- failures are difficult to locate;
- internal services cannot evolve independently;
- the composition layer becomes a second ERP.

API composition should coordinate capabilities.

It should not casually copy core business logic out of the owning applications.

## Orchestration requires ownership

If an API starts a process across several systems, define who owns the complete outcome.

The orchestration layer should know:

- current process state;
- completed steps;
- failed steps;
- compensation options;
- final result;
- business owner.

An API gateway is usually not the right place for this stateful orchestration.

A workflow or process service may be more appropriate.

## API management is not process integration

SAP currently describes API Management as providing security policies, centralized governance, usage and performance analytics, anomaly monitoring, developer discovery and lifecycle controls across environments.

These are important capabilities.

API management can:

- authenticate callers;
- authorize access;
- apply rate limits;
- manage traffic;
- transform headers;
- route versions;
- collect analytics;
- expose documentation.

It should not become the main home for:

- pricing rules;
- sales organization determination;
- supplier classification;
- financial posting logic;
- multi-step order orchestration.

A gateway policy is not a substitute for a business service.

## The gateway should protect and govern the contract

Strong API gateway responsibilities include:

- authentication;
- authorization;
- token validation;
- quotas;
- rate limiting;
- threat protection;
- request-size controls;
- routing;
- observability;
- controlled protocol adaptation.

Weak gateway responsibilities include:

- complex master data derivation;
- long-running workflow;
- business transaction state;
- extensive system-of-record decisions;
- customer-specific commercial logic.

The more business logic is hidden in the gateway, the harder the API becomes to test, move and understand.

## An API proxy does not create an API product

A technical service can be placed behind API Management.

It is now secured and monitored.

It is not automatically well designed.

An API product also needs:

- business purpose;
- owner;
- consumer documentation;
- support model;
- service expectations;
- version policy;
- deprecation policy.

Governance cannot be reduced to routing traffic through one platform.

## API products need owners

Every important API should have at least two ownership perspectives.

## Business or domain owner

Owns:

- purpose;
- business semantics;
- permitted use;
- expected outcome;
- policy.

## Technical product owner

Owns:

- implementation;
- security;
- availability;
- performance;
- lifecycle;
- support.

An integration team may operate the platform.

It should not automatically own every business API.

## Reuse should be measured, not assumed

A generic API may be created with the expectation that many consumers will use it.

In practice:

- one application needs extra fields;
- another needs different validation;
- a partner needs a custom format;
- an agent needs a safer limited action.

The team adds optional parameters and flags.

The API becomes difficult to understand.

Reuse is valuable when consumers share the same business capability.

It is harmful when unrelated use cases are forced through one oversized contract.

Measure:

- actual consumers;
- shared behaviour;
- consumer-specific exceptions;
- change conflicts;
- support burden.

A focused API used by three consumers may be better than one “universal” API with fifty conditional options.

## Avoid consumer-specific APIs where the business meaning is shared

The opposite problem also occurs.

Teams create:

- customer API for portal;
- customer API for CRM;
- customer API for mobile;
- customer API for AI agent.

Each contains slightly different mappings and status meanings.

The landscape recreates point-to-point integration.

A better design may use:

- one governed customer capability;
- purpose-specific access scopes;
- filtered views;
- bounded agent tools;
- consumer-side presentation logic.

Create separate APIs when the business behaviour is genuinely different, not merely because the consumer has a different name.

## Separate system APIs, process APIs and experience APIs carefully

Some API architecture methods distinguish:

### System API

Provides controlled access to a system of record.

### Process API

Combines data or actions across systems for a business process.

### Experience API

Adapts the result for a specific channel or user experience.

This can be useful.

It can also create three API layers for every simple request.

Use the layers only when they provide real separation.

A system API should prevent direct dependency on internal implementation.

A process API should own a real reusable process.

An experience API should adapt to meaningful channel needs.

Do not create layers because a diagram says every integration needs them.

## Graph and unified access do not remove ownership

SAP currently presents Graph as a unified, extensible API and semantic layer for accessing SAP and third-party business data through a single endpoint. SAP states that the capability is intended to simplify development and allow data models to be adapted to business needs.

This can reduce the need for applications to understand several source-specific APIs.

But a semantic access layer does not remove questions such as:

- Which system owns the customer?
- Which value is authoritative?
- How fresh is the data?
- Can the consumer update it?
- Which local extensions are included?
- What happens when sources disagree?

Unified access is valuable.

It should not be confused with unified truth.

## Read APIs and write APIs have different risk

A read API may expose information.

A write API changes business state.

The write API needs stronger controls.

For a read API, consider:

- data sensitivity;
- field-level access;
- freshness;
- caching;
- load.

For a write API, also consider:

- authorization to act;
- idempotency;
- validation;
- approval;
- transaction boundaries;
- audit;
- reversal;
- duplicate prevention.

An agent may safely retrieve order status through a broad read service.

The same agent should not automatically receive authority to cancel orders or release credit blocks.

## Use purpose-specific authorization

An API token should not mean:

> This application may do anything the backend technical user can do.

Access should reflect business purpose.

Examples include:

- read order status;
- submit standard order;
- request cancellation;
- retrieve approved supplier data;
- create a support case.

The authorization model should distinguish:

- data access;
- business action;
- organizational scope;
- financial threshold;
- customer or supplier scope.

Backend technical users with broad roles can undermine API-level controls.

## Rate limits are business protection

Rate limiting is not only a technical concern.

An uncontrolled consumer may:

- overload SAP;
- create thousands of duplicate requests;
- trigger excessive pricing calls;
- start too many background processes;
- consume licensed capacity;
- create financial documents at an unsafe rate.

Limits should reflect:

- backend capacity;
- normal consumer behaviour;
- business criticality;
- burst requirements;
- recovery scenarios.

SAP’s current API Management description includes enterprise security policies, real-time traffic monitoring, alerts, centralized controls and usage analytics.

These controls are useful only when thresholds are connected to actual backend and business behaviour.

## Caching requires semantic care

Caching a product description is usually low risk.

Caching may be more sensitive for:

- credit status;
- price;
- inventory availability;
- compliance block;
- payment state.

Before caching, define:

- acceptable staleness;
- invalidation;
- authoritative source;
- effect of outdated data.

An API response can be technically fast and commercially wrong because it uses an old value.

## APIs need service objectives

Consumers need to know what they can rely on.

Useful expectations include:

- availability;
- response time;
- throughput;
- maximum request size;
- support hours;
- recovery time;
- data freshness;
- change-notification period.

Not every API requires the same service level.

An employee-directory lookup and a real-time sales-order API have different business impact.

Classify APIs by criticality.

## Monitor consumer experience, not only gateway traffic

API monitoring often focuses on:

- request count;
- response time;
- HTTP errors;
- policy violations.

Business monitoring should also consider:

- orders created;
- duplicate orders prevented;
- requests accepted but unfinished;
- business validation errors;
- abandoned processes;
- downstream completion.

An API may return fast responses while the asynchronous backend queue is delayed for hours.

The operational view should connect gateway, backend and business outcome.

## API analytics should answer practical questions

Useful analysis includes:

- Which consumers use the API?
- Which operations are most frequent?
- Which error codes are increasing?
- Which clients retry excessively?
- Which APIs have no active consumers?
- Which versions remain in use?
- Which calls create the most backend load?
- Which consumers depend on deprecated fields?

SAP describes built-in analytics and dashboards for tracking API usage and performance as part of its current API lifecycle capabilities.

These metrics should support portfolio decisions, not only platform reporting.

## Version only when necessary, but version clearly

Breaking changes may require a new API version.

Examples include:

- field meaning changes;
- mandatory field added;
- structure removed;
- operation behaviour changed;
- identifier model replaced;
- error contract changed.

Non-breaking changes may include:

- optional field added;
- new optional response information;
- new operation;
- additional non-disruptive metadata.

A version policy should define:

- what counts as breaking;
- how versions are named;
- how long old versions remain supported;
- how consumers are notified;
- how usage is monitored;
- who approves retirement.

## Do not maintain every version forever

Versioning without deprecation produces permanent complexity.

The provider should:

1. announce the new version;
2. publish migration guidance;
3. identify active consumers;
4. agree a transition window;
5. monitor remaining usage;
6. retire the old version deliberately.

A version is not deprecated merely because documentation says so.

It is deprecated when consumers have a real migration path and the organization is prepared to stop support.

## Consumer-driven contracts can expose hidden dependencies

A provider may believe a field is unused.

A consumer may depend on:

- exact error text;
- field ordering;
- undocumented code;
- optional field always being present;
- response timing.

Contract testing helps reveal these dependencies before release.

Consumers should declare the parts of the contract they rely on.

Providers should test compatibility against those expectations.

This does not give consumers control over every provider change.

It makes real coupling visible.

## API documentation should explain business behaviour

Generated OpenAPI documentation is useful.

It usually explains:

- paths;
- parameters;
- data types;
- response schemas.

It may not explain:

- when to use the API;
- what business rules apply;
- which state changes occur;
- what approval may follow;
- whether processing is asynchronous;
- how duplicates are handled;
- how errors should be corrected.

Good documentation needs examples and process meaning.

A developer should be able to understand the business contract without asking the original project team.

## Discovery matters

SAP currently describes Developer Hub as a centralized location for API discovery, interactive documentation, testing and developer onboarding.

A catalogue is valuable when it helps consumers answer:

- Does an approved API already exist?
- Who owns it?
- Can I test it?
- Which environment is available?
- What access do I need?
- Which version should I use?
- Is it intended for my purpose?

A catalogue filled with duplicate or undocumented endpoints does not improve discovery.

It only makes the integration estate more visible.

## SAP Business Accelerator Hub should be a starting point, not an automatic design decision

SAP provides discoverable APIs, events and integration content through SAP Business Accelerator Hub.

This can reduce the need to invent interfaces without checking available standard contracts.

But a listed API still needs to be assessed against:

- deployed SAP release;
- edition;
- scope activation;
- extension fields;
- volume;
- authentication;
- business requirements;
- lifecycle expectations.

Standard-first is a good principle.

Blind standard adoption is not.

## Standard API versus custom API

Use a standard API when it:

- supports the required business capability;
- provides stable semantics;
- fits the target SAP release;
- meets volume and performance needs;
- can be extended safely where required.

Consider a custom API when:

- no standard capability exists;
- the standard API exposes unsuitable internal complexity;
- the business process is genuinely customer-specific;
- a bounded facade is needed to protect consumers from backend variation.

A custom API should not duplicate standard services merely because the project team finds custom development more familiar.

## An API facade can protect consumers

A facade may provide a stable contract in front of:

- SAP S/4HANA;
- legacy ERP;
- cloud application;
- several backend services.

This can help during migration.

Consumers use one contract while the backend changes.

The facade is valuable when it owns:

- stable external semantics;
- routing during transition;
- compatibility;
- controlled composition.

It becomes harmful when it accumulates every business rule from both old and new systems and never gets simplified after migration.

A transition layer needs an exit strategy.

## Do not confuse abstraction with duplication

An API abstraction should hide unnecessary implementation differences.

It should not copy the entire backend data model.

For example, a customer capability may expose:

- identity;
- status;
- approved addresses;
- relevant commercial context.

It does not need to reproduce every field from every SAP customer view.

The contract should serve actual consumer needs while maintaining stable business meaning.

## APIs and events should work together

An API-first strategy does not mean event-free architecture.

A common pattern is:

1. API accepts a command;
2. backend commits the business transaction;
3. API returns accepted or completed status;
4. event announces the resulting business fact;
5. consumers retrieve additional detail through an API where necessary.

Example:

1. commerce platform calls `SubmitOrder`;
2. SAP creates the sales order;
3. API returns the SAP and external order references;
4. `SalesOrder.Created` event is published;
5. portal and analytics consume the event;
6. later status can be queried through `GetOrderStatus`.

APIs handle intentional interaction.

Events distribute completed change.

## APIs and files can also coexist

An application may use:

- API for real-time order submission;
- file for nightly catalogue synchronization;
- event for order-status changes;
- bulk API for historical migration.

Choosing several patterns is not inconsistency.

Forcing every interaction through one protocol is.

## AI agents change the API consumer model

SAP currently presents Integration Suite as connecting agents, applications, data and processes through governed APIs, events and integration services. SAP’s API lifecycle page also describes exposing curated APIs as governed MCP servers, applying runtime controls and monitoring MCP activity.

This increases the importance of API product design.

An agent needs:

- understandable descriptions;
- bounded actions;
- predictable errors;
- explicit required inputs;
- safe read and write separation;
- auditability;
- rate and authority limits.

An internal API created for a deterministic application may be unsafe as an agent tool.

For example:

```text
POST /update-sales-order
```

is too broad.

A safer agent-facing capability may be:

```text
POST /sales-orders/{id}/request-delivery-date-change
```

The second contract limits:

- object;
- action;
- expected workflow;
- authority.

## Do not expose unrestricted CRUD as agent tools

An agent should not receive generic update access to sensitive business objects when the required task is narrow.

Prefer task-oriented actions such as:

- request supplier review;
- prepare order cancellation;
- retrieve blocked-order evidence;
- propose delivery-date change;
- submit approved service request.

The API should express the permitted business action.

Security policies alone cannot compensate for an overly broad contract.

## Agent-ready does not mean agent-authorized

An API may be easy for an agent to understand and call.

The agent may still need:

- human approval;
- policy check;
- transaction limit;
- restricted organizational scope;
- simulation;
- post-action verification.

Agent readiness is a usability property.

Authority is a governance decision.

## Build an API portfolio, not only APIs

An API portfolio should contain:

- business domains;
- approved API products;
- owners;
- consumers;
- versions;
- usage;
- service level;
- data sensitivity;
- lifecycle state;
- dependencies.

This allows the organization to identify:

- duplicates;
- unused APIs;
- overloaded generic APIs;
- missing capabilities;
- risky write services;
- old versions;
- backend concentration.

The portfolio should be managed like an application or product landscape.

## Classify APIs by role

A useful classification may include:

## Core business APIs

Expose stable enterprise capabilities.

Examples:

- submit order;
- retrieve business partner;
- obtain invoice;
- confirm shipment.

## Internal operational APIs

Support specific internal components.

They may have narrower reuse and lifecycle expectations.

## Partner APIs

Expose controlled contracts to customers, suppliers or logistics partners.

They require stronger external version and support discipline.

## Experience APIs

Adapt capabilities for channels such as portal or mobile.

## Agent-facing APIs and tools

Expose bounded actions and data for AI-assisted workflows.

The classification helps define governance without treating every endpoint equally.

## Build APIs around domain boundaries

A customer API should not casually become responsible for:

- pricing;
- inventory;
- credit;
- billing;
- delivery.

Those capabilities belong to different domains.

One process may compose them.

The API ownership should remain clear.

Domain boundaries reduce:

- duplicated rules;
- oversized payloads;
- ambiguous accountability;
- change conflicts.

## A practical API design sequence

## Step 1: Define the business capability

Write what the consumer is trying to achieve.

Avoid beginning with backend tables or transactions.

## Step 2: Identify the domain owner

Decide who owns the meaning and policy.

## Step 3: Choose synchronous or asynchronous behaviour

Determine whether the final outcome must be immediate.

## Step 4: Define the business contract

Specify:

- input;
- result;
- identity;
- state;
- errors;
- side effects.

## Step 5: Design idempotency and uncertainty handling

Define what happens after timeout, retry and repeated request.

## Step 6: Define authorization by purpose

Limit access to required data and actions.

## Step 7: Decide what remains backend-specific

Do not expose internal codes without a consumer need.

## Step 8: Define lifecycle

Set:

- owner;
- version policy;
- service level;
- support;
- deprecation.

## Step 9: Test contracts and failure conditions

Include:

- invalid input;
- duplicate request;
- timeout;
- backend unavailable;
- partial completion;
- older consumer;
- rate limit.

## Step 10: Monitor business outcomes

Connect API calls to resulting SAP and downstream business objects.

## Example: designing an order-submission API

## Weak contract

```text
POST /sap/order
```

Requires:

- document type;
- sales area;
- partner codes;
- item categories;
- condition types;
- schedule-line details.

The caller effectively constructs an SAP sales order.

## Stronger contract

```text
POST /customer-orders
```

Accepts:

- external order ID;
- customer identity;
- items;
- requested quantities;
- requested fulfilment;
- contract or offer reference;
- source channel.

The sales domain determines:

- SAP organizational values;
- document type;
- pricing;
- availability;
- blocks.

The result contains:

- request ID;
- SAP order ID where created;
- processing state;
- business warnings;
- rejected items;
- correlation ID.

The caller can query status using the external order ID.

A later event announces confirmed order state.

## Example: designing an availability API

A weak API returns internal stock tables.

A stronger API accepts:

- product;
- quantity;
- destination;
- requested date;
- relevant customer context.

It returns:

- confirmed quantity;
- earliest feasible date;
- fulfilment source where appropriate;
- confidence or state;
- validity timestamp.

The API should state whether the response is:

- current stock;
- ATP confirmation;
- estimated availability;
- non-binding indication.

These meanings are commercially different.

## Example: designing a supplier API

A generic `UpdateSupplier` API may permit changes to:

- name;
- bank data;
- tax data;
- purchasing data;
- blocks.

This is too broad for many consumers.

Use bounded capabilities such as:

- submit supplier-onboarding request;
- request purchasing extension;
- retrieve approved supplier identity;
- propose bank-data change;
- retrieve supplier readiness.

Sensitive changes can then trigger appropriate verification and approval.

## A strong first API-first pilot

A practical pilot may focus on one external order channel.

### Scope

- one order type;
- one sales organization;
- one customer segment;
- controlled item volume;
- one standard fulfilment path.

### API capability

- submit order;
- retrieve processing status;
- retrieve resulting order reference.

### Controls

- external-order idempotency;
- structured validation;
- purpose-based authorization;
- rate limit;
- correlation;
- business-error contract;
- no direct internal document-type selection by consumer.

### Asynchronous support

- order-created event;
- order-confirmed event;
- processing-failed status.

### Reconciliation

Compare:

- external requests;
- accepted API requests;
- SAP orders;
- duplicate attempts;
- unresolved exceptions.

### Success measures

- first-time-right order rate;
- duplicate prevention;
- consumer integration effort;
- average response time;
- business-completion time;
- support incidents;
- reuse by a second approved consumer.

## Metrics that matter

## API reuse

How many real consumers use the same business contract without consumer-specific forks?

## Business-success rate

What percentage of accepted requests produce the intended business outcome?

## Duplicate-prevention rate

How many repeated requests are handled without repeated effects?

## Uncertain-outcome rate

How often does a timeout leave the caller unable to determine business status?

## Consumer onboarding time

How long does a new approved consumer need to understand, test and use the API?

## Breaking-change rate

How often do provider changes force consumer updates?

## Version distribution

Which versions are active, and which consumers prevent retirement?

## Business-error rate

Which process or master data problems are most common?

## Backend-load concentration

Which APIs create disproportionate SAP workload?

## Unused-API rate

How many published APIs have no active consumers?

## Agent-action exception rate

How often do agent-facing calls exceed policy, require correction or fail verification?

## Common mistakes

## Mistake 1: Defining API-first as REST-only

Modern protocols do not guarantee modern architecture.

## Mistake 2: Wrapping SAP internals in JSON

Consumers remain tightly coupled to the backend.

## Mistake 3: Building an API for every table or object

The portfolio becomes expensive and hard to govern.

## Mistake 4: Using synchronous APIs for long processes

Timeouts create uncertain business outcomes.

## Mistake 5: Retrying commands without idempotency

Resilience logic creates duplicate transactions.

## Mistake 6: Returning only technical errors

Consumers cannot correct or route business problems.

## Mistake 7: Putting orchestration in the API gateway

The gateway becomes a hidden process engine.

## Mistake 8: Forcing every consumer through one universal API

Conditional logic and optional fields make the contract unstable.

## Mistake 9: Creating consumer-specific versions of the same capability

Point-to-point architecture returns under new names.

## Mistake 10: Publishing APIs without owners

Security may be centralized while business meaning remains unmanaged.

## Mistake 11: Keeping every version indefinitely

The API estate accumulates permanent complexity.

## Mistake 12: Giving agents generic write APIs

A broad technical operation becomes an uncontrolled business tool.

## Questions architects and managers should ask

1. What business capability does this API expose?
2. Why must the interaction be synchronous?
3. Is the consumer dependent on SAP internal codes?
4. Who owns the business meaning?
5. Is this API actually reusable?
6. What happens after a timeout?
7. Can a request be repeated safely?
8. How does the caller determine final business completion?
9. Are errors actionable?
10. Which logic belongs in the backend, middleware or gateway?
11. What service level does the consumer need?
12. Which data and actions does the consumer really require?
13. How will the API evolve without breaking consumers?
14. Which consumers are using each version?
15. Is the API documented as a business contract or only as a schema?
16. Can events support later state changes?
17. Is a standard SAP API already available?
18. Does a facade have a planned end state?
19. Is an agent receiving more authority than the use case requires?
20. Are we reducing coupling or publishing it through HTTP?

## The goal is controlled business access

SAP currently positions Integration Suite as a unified platform for connecting applications, data, events, APIs, partners and agents across SAP and third-party environments. Its API lifecycle capabilities include centralized governance, security policies, analytics, anomaly monitoring, developer discovery, Graph and governed MCP exposure.

These capabilities can provide a strong platform.

They do not replace API product design.

An API-first architecture works when APIs are:

- business-oriented;
- bounded;
- owned;
- secure;
- idempotent;
- observable;
- versioned;
- connected to final business outcomes.

It fails when every project publishes another custom endpoint directly shaped by its backend and consumer.

The measure of success is not the number of APIs in the catalogue.

It is whether new applications, partners and agents can use stable business capabilities without learning the internal structure of every SAP system.

That is the real promise of API-first integration.

Without that discipline, the company will replace its old point-to-point landscape with a larger point-to-point landscape that happens to use JSON.

---

## API-first SAP integration checklist

- [ ] APIs are designed around business capabilities.
- [ ] API-first is not treated as REST-only.
- [ ] Synchronous behaviour is justified by business need.
- [ ] Long processes return status rather than holding connections open.
- [ ] External and target business identifiers remain correlated.
- [ ] Write operations support idempotency where required.
- [ ] Timeout behaviour does not cause uncontrolled retries.
- [ ] Technical acceptance and business completion are separate.
- [ ] Error responses are stable and actionable.
- [ ] Temporary and permanent failures are distinguished.
- [ ] Consumers do not need unnecessary SAP internal codes.
- [ ] Business logic remains with accountable domains.
- [ ] API gateways protect and govern rather than own processes.
- [ ] API products have business and technical owners.
- [ ] Reuse is measured through real consumers.
- [ ] Generic APIs do not accumulate unlimited conditional behaviour.
- [ ] Consumer-specific APIs are created only for genuine differences.
- [ ] Read and write APIs use different risk controls.
- [ ] Authorization reflects purpose and organizational scope.
- [ ] Rate limits protect backend and business processes.
- [ ] Data freshness and caching rules are explicit.
- [ ] API service objectives follow business criticality.
- [ ] Monitoring connects requests to final business results.
- [ ] Breaking changes follow a defined version policy.
- [ ] Old versions have an enforced retirement path.
- [ ] Documentation explains business behaviour and side effects.
- [ ] Standard SAP APIs are assessed before custom development.
- [ ] Transition facades have a target end state.
- [ ] APIs and events are combined where appropriate.
- [ ] Agent-facing tools expose bounded actions rather than generic CRUD.

## Sources and further reading

SAP currently describes API Management as supporting enterprise security policies, centralized governance, API usage and performance analytics, anomaly monitoring and developer discovery across environments. The same current capability page includes Graph as a unified and extensible semantic API layer and Developer Hub for API discovery, testing and onboarding.

SAP currently positions SAP Integration Suite as an iPaaS connecting applications, data, APIs, events, B2B partners and AI agents across SAP and third-party environments. Its current product description includes centralized governance, real-time monitoring, prebuilt content, API security, Graph, developer onboarding and agent-ready APIs.

SAP’s current API lifecycle description also includes governed MCP server lifecycle management for exposing curated API investments to AI agents, applying runtime controls and monitoring production usage.

*Reviewed: July 2026. SAP Integration Suite, API Management, Graph, Developer Hub and MCP capabilities, packaging and supported scenarios can change. API designs should be validated against current SAP documentation, the actual SAP release and the organization’s security and business-control requirements.*
