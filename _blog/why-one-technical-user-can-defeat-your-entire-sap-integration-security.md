---
layout: blog
title: "Why One Technical User Can Defeat Your Entire SAP Integration Security Architecture"
description: "External applications call managed APIs. Connections are encrypted. Tokens expire. The API gateway applies security policies and rate limits."
slug: why-one-technical-user-can-defeat-your-entire-sap-integration-security
permalink: /blog/why-one-technical-user-can-defeat-your-entire-sap-integration-security/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP integration architecture"
tags:
  - sap-integration-architecture
  - integration
  - sap-architecture
canonical_url: https://dkharlanau.github.io/blog/why-one-technical-user-can-defeat-your-entire-sap-integration-security/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 29
migration_sequence: 33
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/
  - /blog/where-should-mapping-logic-live-in-modern-sap-integrations/
---

## On this page

- [Shared technical users create hidden privilege aggregation](#shared-technical-users-create-hidden-privilege-aggregation)
- [Preserve user identity where accountability requires it](#preserve-user-identity-where-accountability-requires-it)
- [Service identity and user identity should not be confused](#service-identity-and-user-identity-should-not-be-confused)
- [Technical connectivity should not bypass domain authorization](#technical-connectivity-should-not-bypass-domain-authorization)
- [Design trust boundaries explicitly](#design-trust-boundaries-explicitly)
- [API Management protects the front door, not the whole process](#api-management-protects-the-front-door-not-the-whole-process)
- [Sensitive business flows require special protection](#sensitive-business-flows-require-special-protection)
- [Protect resource consumption](#protect-resource-consumption)
- [Inventory is a security control](#inventory-is-a-security-control)
- [Data minimization should begin at the contract](#data-minimization-should-begin-at-the-contract)
- [Secrets are production assets](#secrets-are-production-assets)
- [Do not log secrets or authorization tokens](#do-not-log-secrets-or-authorization-tokens)
- [Events need security boundaries too](#events-need-security-boundaries-too)
- [B2B and file integrations have different security risks](#b2b-and-file-integrations-have-different-security-risks)
- [AI agents create a new authority layer](#ai-agents-create-a-new-authority-layer)
- [Security monitoring should include business behaviour](#security-monitoring-should-include-business-behaviour)
- [Security audit must preserve business context](#security-audit-must-preserve-business-context)
- [Security should be tested through negative scenarios](#security-should-be-tested-through-negative-scenarios)
- [Security incidents require business reconciliation](#security-incidents-require-business-reconciliation)
- [A reference security architecture](#a-reference-security-architecture)
- [Example: secure order-submission architecture](#example-secure-order-submission-architecture)
- [Example: secure supplier bank-change process](#example-secure-supplier-bank-change-process)
- [Example: secure agent-assisted credit review](#example-secure-agent-assisted-credit-review)
- [A practical implementation sequence](#a-practical-implementation-sequence)
- [Metrics that matter](#metrics-that-matter)
- [Common mistakes](#common-mistakes)
- [Questions architects and managers should ask](#questions-architects-and-managers-should-ask)
- [The goal is controlled authority](#the-goal-is-controlled-authority)

A company builds a modern integration platform.

External applications call managed APIs. Connections are encrypted. Tokens expire. The API gateway applies security policies and rate limits. SAP systems are not exposed directly to the internet.

The architecture passes a security review.

Behind the integration layer, however, most interfaces use one technical SAP user.

The user can:

- create and change sales orders;
- update business partners;
- create purchase orders;
- release blocks;
- read pricing;
- access financial documents.

The integration platform decides which operation to execute.

SAP sees the same technical identity for almost everything.

If one API, integration flow or credential is compromised, the attacker does not receive the limited authority of the original application.

The attacker receives the combined authority of the shared technical user.

The network is protected.

The tokens are valid.

The calls are authenticated.

The business is still exposed.

This is the central problem of SAP integration security:

> Technical authentication is not the same as controlled business authority.

A secure integration architecture must protect more than connections.

It must protect:

- business objects;
- individual operations;
- organizational scope;
- sensitive properties;
- transaction volume;
- financial thresholds;
- approval boundaries;
- human and machine accountability.

SAP currently positions Integration Suite as a secure integration platform with centralized governance, monitoring and security across applications, APIs, events, partners and AI agents. API Management provides centralized security policies, traffic insight and lifecycle controls, while SAP’s current MCP capabilities allow curated APIs to be exposed to agents with design-time and runtime governance.

These are platform capabilities.

The organization still needs to decide what every identity is allowed to do after it reaches SAP.

### Integration security starts with business authority

Most security diagrams show:

- internet;
- firewall;
- API gateway;
- integration platform;
- private network;
- SAP backend.

This describes the path.

It does not describe the authority travelling through that path.

For every integration request, the architecture should answer:

1. Who or what initiated the request?
2. Which business purpose does the caller represent?
3. Which operation is permitted?
4. Which business objects may be accessed?
5. Which fields may be read or changed?
6. Which organizational scope applies?
7. Which financial or quantity limit applies?
8. Is approval required?
9. Which identity executes the action in SAP?
10. Can the complete chain be audited?

A request should not become more powerful as it moves deeper into the landscape.

Yet this is exactly what happens when a narrowly authorized API request is converted into a call using a broad SAP technical account.

### The integration layer is a trust boundary

An integration platform receives information from one security domain and sends it into another.

Examples include:

- external customer application to SAP;
- supplier portal to procurement;
- cloud application to on-premises ERP;
- partner EDI network to internal systems;
- AI agent to business API;
- event consumer to financial process.

At each boundary, the platform may:

- authenticate the caller;
- validate the message;
- transform identifiers;
- add data;
- call another service;
- use a different technical identity.

This means the integration layer is not only a message processor.

It is a security mediator.

If it accepts a low-authority request and executes a high-authority backend action, it performs privilege amplification.

That amplification must be intentional and controlled.

### Network location should not create implicit trust

A common architecture assumption is:

> The request came through the corporate network or approved middleware, so it can be trusted.

NIST’s Zero Trust Architecture guidance explicitly rejects implicit trust based only on network location or asset ownership. It shifts protection toward users, assets and resources, with authentication and authorization performed before access to enterprise resources is established.

For SAP integration, this means:

- a call from middleware is not automatically safe;
- an on-premises connection is not automatically trusted;
- a known partner may still send an unauthorized operation;
- a valid token does not prove the requested business action is permitted;
- a technical user should not receive broad rights because it operates inside the network.

Private connectivity reduces exposure.

It does not replace authorization.

### Separate four identity types

A modern SAP landscape usually contains at least four kinds of identity.

### 1. Human identity

Represents a known person.

Examples:

- customer-service employee;
- buyer;
- credit manager;
- warehouse supervisor.

The system may need to preserve the person’s identity when the integration acts directly on their behalf.

### 2. Workload identity

Represents an application, service, integration flow or background process.

Examples:

- commerce platform;
- warehouse connector;
- invoice-processing service;
- nightly master data distribution.

The workload has its own purpose and authority.

It should not impersonate a generic human user.

### 3. Partner identity

Represents an external company or partner channel.

Examples:

- supplier;
- logistics provider;
- bank;
- customer EDI connection.

Partner identity should normally include both:

- the organization;
- the specific technical connection or application.

### 4. Agent identity

Represents an AI agent or automated decision-support service.

An agent may act for:

- one user;
- one domain;
- one workflow;
- one bounded business purpose.

It should not be treated as an invisible extension of the integration platform.

These identities should remain distinguishable in logs, authorization and audit records.

### Authentication, authorization and approval are separate controls

These concepts are often mixed together.

### Authentication

Answers:

> Who or what is calling?

Examples:

- certificate;
- token;
- signed partner message;
- user session.

### Authorization

Answers:

> Is this identity allowed to perform this action on this resource?

Examples:

- may read order status;
- may submit orders for sales organization 1000;
- may update delivery instructions;
- may not release credit blocks.

### Business approval

Answers:

> Has the accountable business role accepted this specific decision?

Examples:

- discount approved;
- supplier bank change verified;
- payment released;
- credit block removed.

A technically authenticated application is not automatically authorized for every operation.

An authorized application does not automatically have business approval for a sensitive transaction.

### Do not use API scopes as the only business control

API scopes are useful for broad capabilities such as:

- `orders.read`;
- `orders.create`;
- `suppliers.read`;
- `invoices.download`.

But real SAP processes often require more detailed control.

For example, an application may be allowed to create orders only:

- for one sales organization;
- for one customer channel;
- below a value threshold;
- using approved products;
- without manual pricing conditions.

A scope such as `orders.write` is too broad to express these conditions.

Use layered authorization.

### Layer 1: API gateway authorization

The gateway can verify:

- approved client;
- token;
- broad scope;
- environment;
- rate;
- request size;
- permitted endpoint.

### Layer 2: Domain authorization

The business service should verify:

- operation;
- business object;
- organizational scope;
- property access;
- commercial threshold;
- current object state.

### Layer 3: SAP backend authorization

The SAP user or technical identity should have only the permissions required to execute the approved backend operation.

### Layer 4: Workflow approval

Sensitive decisions should use explicit approval where policy requires it.

The gateway should not be the only control preventing an application from releasing a financial or commercial block.

### Object-level authorization matters

Suppose a customer portal can retrieve an order through:

```text
GET /orders/{orderId}
```

Authentication proves the user or application is known.

The API must still prove that the caller is allowed to see that particular order.

Otherwise, changing the order ID may expose another customer’s data.

OWASP lists broken object-level authorization as a leading API risk and states that object-level checks should be applied whenever user-supplied identifiers are used to access data.

In SAP scenarios, object-level checks may depend on:

- sold-to party;
- supplier;
- company code;
- sales organization;
- employee;
- legal entity;
- partner relationship.

Do not assume that knowledge of an SAP document number grants access to the document.

### Property-level authorization matters

A caller may be authorized to read a business partner.

It may not be authorized to read:

- bank details;
- tax identifiers;
- credit limits;
- personal contact information;
- internal risk classification.

A caller may be authorized to update an order.

It may not be authorized to update:

- price;
- payer;
- payment terms;
- delivery block;
- billing relevance.

OWASP’s API security guidance distinguishes object-property authorization failures, where APIs expose or allow manipulation of fields that the caller should not access.

This is particularly important when generic SAP objects are exposed through broad APIs.

A filtered read model or task-specific command is often safer than exposing the complete backend structure.

### Function-level authorization matters

Reading an order and cancelling an order are different authorities.

Creating a supplier request and approving the supplier are different authorities.

Viewing a credit block and releasing it are different authorities.

OWASP identifies broken function-level authorization as a separate API risk, especially where administrative and normal operations are not clearly separated.

Do not expose sensitive operations through one generic endpoint such as:

```text
POST /business-object/action
```

Prefer explicit operations:

- request order cancellation;
- approve order cancellation;
- read supplier readiness;
- propose supplier bank change;
- approve verified bank change.

The contract itself should expose the security boundary.

## Shared technical users create hidden privilege aggregation

A shared SAP technical user is convenient.

It simplifies:

- connection configuration;
- credential management;
- role maintenance;
- support.

It also combines the permissions of unrelated interfaces.

For example, one user may support:

- order creation;
- delivery update;
- billing;
- customer change;
- supplier distribution.

The effective access of every connected application becomes difficult to understand.

Even when the API gateway limits each application, a defect or compromised integration flow may call backend operations outside the original application’s purpose.

### Use purpose-specific workload identities

A stronger design creates separate identities for bounded capabilities.

Examples:

- `ORDER_SUBMISSION_EU`;
- `WAREHOUSE_CONFIRMATION_DE`;
- `SUPPLIER_DISTRIBUTION`;
- `INVOICE_READ_PORTAL`.

The exact naming is not important.

The separation is.

Each identity should have:

- defined business purpose;
- system owner;
- permitted operations;
- organizational scope;
- credential owner;
- expiry or review date;
- monitoring;
- emergency revocation procedure.

### Do not create one identity per message

Over-segmentation can create unmanageable administration.

The correct boundary is normally a stable workload or business capability.

Separate identities when they have meaningfully different:

- owners;
- permissions;
- risk;
- consumers;
- lifecycle;
- incident-containment requirements.

### Environment identities must be separate

Development, test and production should not share:

- credentials;
- certificates;
- service accounts;
- API keys;
- secret aliases.

A non-production integration should not be able to call production SAP accidentally.

Production credentials should not be copied into test tooling for convenience.

## Preserve user identity where accountability requires it

Some integration operations are performed directly on behalf of a person.

For example:

- buyer approves a purchase-order change;
- credit manager releases a block;
- customer-service employee cancels an order;
- finance user approves a refund.

Using one technical backend user may remove the identity of the actual decision-maker.

### User propagation can improve accountability

Where the architecture and products support it, the user identity may be propagated or exchanged so that downstream authorization and audit can reflect the actual person.

This is useful when:

- the user’s SAP authorization should apply;
- individual accountability matters;
- separation of duties must be preserved;
- the integration should not gain more authority than the user.

### User propagation is not always appropriate

Background and system-to-system processes need workload identities.

Examples:

- nightly replication;
- warehouse confirmation;
- automatic order intake;
- business-event processing.

Do not invent a human identity for a process that is not performed by a person.

### Preserve the chain of delegation

An action may involve:

```text
Human user
→ Portal
→ Business API
→ Integration flow
→ SAP
```

The audit evidence should distinguish:

- human initiator;
- calling application;
- integration workload;
- backend execution identity;
- approval where relevant.

Recording only the SAP technical user loses the chain.

Recording only the human user hides which application and automation executed the action.

## Service identity and user identity should not be confused

Suppose a user asks an AI assistant to prepare an order cancellation.

The chain may contain:

- user identity;
- agent identity;
- agent platform;
- API client identity;
- workflow approval;
- SAP execution identity.

The action should not appear as if the user directly called SAP when an agent interpreted, transformed and submitted the request.

The audit trail should reflect each actor.

## Technical connectivity should not bypass domain authorization

A private connection to SAP may allow the integration runtime to reach backend services.

This is necessary for connectivity.

It should not allow unrestricted access to all available endpoints.

Control:

- reachable systems;
- reachable services;
- allowed ports;
- permitted paths;
- backend roles;
- application authorization.

Network restriction and application authorization should reinforce each other.

Neither should compensate for the absence of the other.

## Design trust boundaries explicitly

A useful architecture diagram should mark trust transitions such as:

```text
External user or partner
        |
Public API boundary
        |
Integration platform boundary
        |
Private network boundary
        |
SAP application boundary
        |
Sensitive business object
```

At every boundary, document:

- identity entering;
- identity leaving;
- authentication method;
- authorization decision;
- data classification;
- transformation;
- logging;
- failure behaviour.

This exposes privilege amplification.

For example:

```text
Partner certificate
→ Integration workload identity
→ SAP technical user
```

The team can then ask whether the SAP user has more authority than the partner should ever obtain.

## API Management protects the front door, not the whole process

SAP currently describes API Management as providing enterprise security policies, centralized controls, analytics and anomaly monitoring.

These controls can protect APIs through:

- authentication enforcement;
- access policy;
- traffic control;
- threat protection;
- monitoring;
- centralized governance.

They do not automatically verify:

- whether the customer owns the requested order;
- whether the application may change the price;
- whether the transaction exceeds a business limit;
- whether a human approval exists;
- whether the backend user has excessive rights.

API Management should enforce the edge contract.

The domain and SAP systems should enforce the business contract.

## Sensitive business flows require special protection

Some APIs are dangerous not because of one software defect, but because they expose a valuable business operation that can be abused at scale.

OWASP identifies unrestricted access to sensitive business flows as an API risk. The weakness may exist even when authentication and implementation are technically correct.

SAP examples include:

- submitting thousands of orders;
- reserving scarce stock;
- downloading large numbers of invoices;
- checking prices across an entire catalogue;
- initiating returns;
- creating suppliers;
- requesting password or bank-detail changes;
- cancelling orders;
- triggering expensive simulations.

A valid client may still misuse a valid operation.

### Protect flows, not only endpoints

Possible controls include:

- business quotas;
- customer-specific limits;
- velocity checks;
- amount thresholds;
- duplicate detection;
- approval for unusual patterns;
- delayed execution;
- anomaly alerts;
- temporary circuit breaker;
- step-up authentication.

### Rate limits are necessary but insufficient

A rate limit may allow 100 requests per minute.

One request may still:

- cancel a million-euro order;
- download a sensitive dataset;
- update a supplier bank account;
- trigger a large financial posting.

Security needs both:

- frequency control;
- business-impact control.

## Protect resource consumption

APIs consume:

- CPU;
- memory;
- SAP work processes;
- database capacity;
- network;
- third-party paid services.

OWASP identifies unrestricted resource consumption as a risk that can cause denial of service or increased operational cost.

SAP integrations should control:

- page size;
- query complexity;
- date ranges;
- payload size;
- batch size;
- concurrency;
- expensive calculations;
- repeated polling;
- agent loops.

An authenticated internal application can still overload SAP.

### Avoid unrestricted generic search APIs

A query that allows arbitrary filters across a large SAP object may be flexible.

It may also create:

- unpredictable database load;
- data exposure;
- difficult authorization;
- denial-of-service risk.

Prefer bounded query capabilities with:

- defined indexes;
- maximum ranges;
- pagination;
- controlled fields;
- expected response limits.

## Inventory is a security control

An organization cannot protect APIs it does not know exist.

OWASP’s API security list includes improper inventory management as a risk category.

A secure integration inventory should include:

- API;
- event;
- file flow;
- partner connection;
- backend service;
- owner;
- consumer;
- authentication method;
- execution identity;
- data classification;
- production URL or topic;
- version;
- lifecycle state.

Look for:

- undocumented endpoints;
- old API versions;
- inactive partners;
- temporary credentials;
- test interfaces reachable from production;
- APIs with no owner;
- broad technical users.

## Data minimization should begin at the contract

Do not send the complete SAP object because it is available.

A consumer that needs order status may not need:

- internal margin;
- pricing conditions;
- credit information;
- partner bank data;
- employee notes.

A warehouse may need:

- product;
- quantity;
- shipping instruction.

It may not need:

- customer credit limit;
- invoice history;
- commercial discount details.

Data minimization reduces:

- privacy exposure;
- security impact;
- schema coupling;
- logging risk;
- accidental reuse.

### Filter at the provider, not only at the consumer

Sending sensitive data and asking the consumer to ignore it is not minimization.

The provider should expose a contract containing only permitted information.

## Secrets are production assets

Integration landscapes contain:

- client secrets;
- certificates;
- private keys;
- API keys;
- passwords;
- signing keys;
- encryption keys.

These assets should not live in:

- source code;
- integration payloads;
- email;
- spreadsheets;
- deployment scripts;
- ticket comments;
- copied test configurations.

### Every secret needs an owner and lifecycle

Record:

- purpose;
- owner;
- system;
- environments;
- issue date;
- expiry;
- rotation procedure;
- emergency revocation;
- dependent integrations.

### Rotation must be tested

A certificate-renewal procedure that has never been executed is not a control.

Test whether:

- the new credential can coexist during transition;
- dependent consumers update correctly;
- the old credential can be revoked;
- rollback is possible;
- monitoring detects failed rotation.

### Prefer short-lived credentials where practical

Long-lived static secrets increase the impact of leakage.

Where supported and suitable, use mechanisms that provide:

- limited lifetime;
- narrow scope;
- clear audience;
- controlled renewal;
- revocation.

The technology should fit the connected systems and operational model.

## Do not log secrets or authorization tokens

Integration logs may capture:

- HTTP headers;
- request payloads;
- partner messages;
- error details.

Production troubleshooting often leads teams to enable complete payload logging.

This can expose:

- access tokens;
- passwords;
- bank details;
- personal data;
- commercial data.

Logging should use:

- field masking;
- header suppression;
- data classification;
- restricted access;
- limited retention;
- controlled diagnostic mode.

Debug visibility should not become a permanent data leak.

## Events need security boundaries too

Event-driven architecture may distribute one business event to many consumers.

Security design should cover:

- who may publish;
- who may subscribe;
- which topic or queue;
- which event types;
- which data fields;
- retention;
- replay authority;
- schema validation.

### Protect against unauthorized publication

A malicious or defective producer could publish:

- fake order cancellation;
- fake supplier approval;
- false goods issue;
- repeated invoice event.

Consumers should verify:

- trusted producer;
- permitted event type;
- schema;
- source identity;
- required identifiers;
- object version.

A connection to the broker should not grant authority to publish every enterprise event.

### Protect subscriptions

A consumer should not receive all events because filtering is easier locally.

Separate access by:

- domain;
- event family;
- organization;
- sensitivity;
- consumer purpose.

### Replay is a privileged operation

Replaying events may repeat:

- notifications;
- workflows;
- documents;
- partner calls.

Replay authority should be limited and audited.

Before replay, verify:

- current business state;
- idempotency;
- superseding versions;
- consumer purpose;
- side effects.

## B2B and file integrations have different security risks

Partner integrations may use:

- EDI;
- managed file transfer;
- SFTP;
- AS2-like exchanges;
- partner APIs;
- industry networks.

Security should establish:

- partner identity;
- permitted document type;
- message origin;
- integrity;
- confidentiality;
- sequence;
- acknowledgement;
- duplicate control.

### Shared folders are weak trust boundaries

A file appearing in a directory does not automatically prove:

- which partner created it;
- whether it was changed;
- whether it was sent before;
- whether it belongs to the expected sequence.

Use controls appropriate to the risk, such as:

- authenticated transfer;
- restricted partner directories;
- signature or integrity validation;
- encryption;
- checksums;
- file sequence;
- manifest;
- duplicate-file detection.

### Partner onboarding is a security process

Onboarding should record:

- legal partner;
- technical endpoint;
- certificate or credential;
- permitted messages;
- identifiers;
- test evidence;
- operational contact;
- expiry;
- offboarding procedure.

A partner connection should not remain active because nobody knows whether it is still used.

## AI agents create a new authority layer

SAP currently describes its API lifecycle capabilities as supporting curated APIs exposed as governed MCP servers, with centralized discovery, runtime controls and production monitoring for agent use.

This is useful because an agent should not call arbitrary backend services.

But exposing an API through MCP does not automatically make it safe for agent execution.

### Agent tools should be narrower than application APIs

A deterministic application may call:

```text
PATCH /sales-orders/{id}
```

An agent-facing tool should often be more specific:

```text
request_delivery_date_change
prepare_order_cancellation
retrieve_blocked_order_evidence
```

The narrow tool can enforce:

- permitted field;
- allowed state;
- reason;
- organizational scope;
- approval;
- simulation.

### Agents need separate identities

Do not let all agents operate through one shared integration user.

Separate by:

- agent;
- business purpose;
- domain;
- environment;
- action type.

### Distinguish recommendation from execution

An agent may be permitted to:

- investigate;
- summarize;
- recommend;
- prepare a request.

It may not be permitted to:

- approve;
- release;
- post;
- cancel;
- change bank data.

The architecture should encode this distinction.

### Defend against repeated and circular actions

An event may trigger an agent.

The agent changes an object.

The change publishes another event.

The agent triggers again.

Use:

- causation IDs;
- loop detection;
- maximum action count;
- cooldown;
- idempotency;
- human escalation.

### Record the complete agent action chain

Audit evidence should include:

- user or event trigger;
- agent identity;
- tools called;
- data accessed;
- recommendation;
- approval;
- executed action;
- SAP result;
- verification.

A log entry saying “updated by integration user” is insufficient.

## Security monitoring should include business behaviour

Traditional monitoring looks for:

- failed authentication;
- invalid token;
- blocked IP;
- unusual endpoint usage.

Business abuse may use valid credentials.

Monitor patterns such as:

- unusual number of order cancellations;
- supplier changes outside normal hours;
- invoice downloads across many customers;
- price requests covering the full catalogue;
- sudden increase in free-of-charge orders;
- repeated block-release attempts;
- agent actions beyond normal domain volume.

SAP currently describes API anomaly detection as monitoring API traffic patterns and triggering alerts for irregular behaviour.

Traffic anomaly detection should be combined with business context.

One unusual call may matter more than ten thousand normal calls.

## Security audit must preserve business context

For important write operations, record:

- initiator;
- workload identity;
- API;
- operation;
- business object;
- organizational scope;
- approval;
- timestamp;
- correlation ID;
- result;
- previous and new state where appropriate.

Do not rely only on middleware logs.

The target domain should retain the business record required for audit and investigation.

### Logs are not the business record

Technical logs may be:

- sampled;
- deleted;
- inaccessible to business auditors;
- missing final SAP state.

The authoritative business application should retain the formal transaction and approval evidence where required.

## Security should be tested through negative scenarios

A normal integration test proves that an authorized operation works.

Security testing should prove that unauthorized operations fail.

Examples include:

- customer A requests customer B’s order;
- application changes a field outside its scope;
- test credential calls production;
- order-submission client tries to release a credit block;
- agent attempts a generic update;
- event producer publishes an unauthorized event type;
- partner reuses an expired certificate;
- payload requests an excessive date range;
- caller repeats a sensitive transaction;
- technical user attempts an operation outside its role.

### Test the backend identity directly

Security review often checks the API layer but not the SAP technical user.

Verify:

- actual assigned roles;
- unused permissions;
- organizational restrictions;
- accessible services;
- change history;
- emergency access.

## Security incidents require business reconciliation

Suppose a technical credential is compromised.

Revoking the credential stops future calls.

The company must still determine:

- which calls occurred;
- which SAP documents were created;
- which objects were changed;
- which partner messages were sent;
- which financial effects happened;
- which actions must be reversed or reviewed.

Security incident response and integration reconciliation must work together.

### Prepare an integration isolation plan

The company should be able to:

- revoke one client;
- disable one API;
- stop one consumer;
- block one partner;
- remove one backend identity;
- pause one sensitive operation.

A security incident in one channel should not require shutting down the entire integration platform.

This is another reason to avoid shared technical users and shared credentials.

## A reference security architecture

A logical model may look like this:

```text
Users | Applications | Partners | AI Agents
                  |
        Identity and Authentication
                  |
         API / Event / B2B Boundary
 Scope | Rate | Schema | Threat Protection
                  |
       Domain Authorization and Policy
 Object | Property | Function | Organization
 Value | State | Approval | Business limits
                  |
      Integration Execution and Translation
 Controlled workload identity | Correlation
                  |
             SAP Backend
 Least-privilege role | Business validation
                  |
      Audit, Monitoring and Reconciliation
```

Cross-cutting controls:

```text
Secret lifecycle
Credential rotation
Environment separation
Data classification
Security inventory
Incident isolation
Agent governance
```

### The critical rule

Authority should narrow or remain equal as the request moves deeper.

It should not widen.

## Example: secure order-submission architecture

### Caller

A commerce platform submits customer orders.

### API access

The client receives permission to call:

```text
customer-orders.submit
customer-orders.status.read
```

It cannot call cancellation, pricing override or credit-release operations.

### Domain authorization

The order service checks:

- approved sales channel;
- allowed sold-to party;
- permitted sales organization;
- supported products;
- order-value threshold;
- duplicate external order ID.

### Integration identity

A purpose-specific order-submission workload identity calls SAP.

Its SAP role permits only the required order-creation operation and organizational scope.

### Sensitive exceptions

Manual price conditions or credit release require a separate workflow and identity.

### Audit

The order stores:

- external order ID;
- client identity;
- channel;
- integration identity;
- SAP order number;
- approval where applicable.

A compromised order-submission client cannot automatically become a supplier-maintenance or financial-posting client.

## Example: secure supplier bank-change process

A supplier requests a bank-account change.

This should not be exposed as:

```text
PATCH /suppliers/{id}
```

A stronger process is:

1. supplier submits change request through authenticated channel;
2. request is stored without updating active bank data;
3. verification is performed through an independent control;
4. authorized role approves the change;
5. a bounded backend operation updates the approved field;
6. downstream distribution occurs;
7. the result is reconciled.

Separate identities should exist for:

- supplier request;
- verification;
- approval;
- execution.

The integration platform coordinates the process.

It does not collapse all steps into one high-privilege API call.

## Example: secure agent-assisted credit review

An agent receives an event that an order is credit blocked.

The agent may:

- retrieve order value;
- retrieve overdue receivables;
- summarize payment history;
- prepare a recommendation.

The agent may not directly release the block.

A credit manager reviews the recommendation.

A separate approved action performs the release using the manager’s or workflow’s authority.

The audit records:

- event;
- agent;
- evidence;
- recommendation;
- manager decision;
- execution;
- SAP result.

This uses AI to reduce preparation work without transferring credit authority to the agent.

## A practical implementation sequence

### Phase 1: Inventory identities

List:

- human identities;
- service accounts;
- certificates;
- API clients;
- partner credentials;
- agent identities;
- SAP technical users.

### Phase 2: Map authority

For each identity, document:

- business purpose;
- permitted operations;
- organizational scope;
- data access;
- owner;
- consumers.

### Phase 3: Find privilege aggregation

Identify shared users and clients that combine unrelated permissions.

### Phase 4: Define trust boundaries

Document identity changes and privilege changes across:

- channel;
- gateway;
- middleware;
- network;
- SAP.

### Phase 5: Separate authentication from authorization

Define which layer checks:

- client identity;
- business object;
- field;
- operation;
- approval.

### Phase 6: Reduce backend rights

Create purpose-specific roles and workload identities.

### Phase 7: Protect sensitive flows

Add:

- thresholds;
- quotas;
- approval;
- anomaly detection;
- duplicate control.

### Phase 8: Establish secret lifecycle

Implement:

- secure storage;
- expiry monitoring;
- rotation;
- revocation;
- environment separation.

### Phase 9: Secure events and partners

Restrict producers, consumers, topics, message types and replay authority.

### Phase 10: Govern agent access

Expose bounded tools, separate identities and explicit approval paths.

### Phase 11: Add negative testing

Prove that forbidden operations fail at several layers.

### Phase 12: Build incident reconciliation

Be able to determine which business actions occurred under a compromised identity.

## Metrics that matter

### Shared high-privilege identity count

How many technical users support unrelated business capabilities?

### Least-privilege coverage

What percentage of production integrations uses purpose-specific backend roles?

### Credential-owner coverage

How many credentials have a current named owner?

### Expiry visibility

How many certificates and secrets lack monitored expiry or rotation plans?

### User-attribution coverage

What percentage of human-initiated sensitive actions preserves the initiator identity?

### Unauthorized-action test coverage

How many APIs have negative object-, property- and function-level authorization tests?

### Sensitive-flow protection coverage

Which high-impact operations have thresholds, quotas or approval controls?

### API inventory completeness

How many active endpoints, versions and clients are registered?

### Orphaned-client count

How many clients or partner connections have no active consumer or owner?

### Agent-tool breadth

How many agent tools expose generic write operations rather than bounded actions?

### Incident-isolation time

How quickly can one client or workload be stopped without disabling unrelated integrations?

### Business-reconciliation time after security incident

How long does it take to identify all affected SAP transactions?

## Common mistakes

### Mistake 1: Treating private connectivity as authorization

A trusted network path does not prove a permitted business action.

### Mistake 2: Using one SAP technical user for the entire platform

Every integration inherits the combined backend authority.

### Mistake 3: Enforcing security only at the API gateway

A gateway cannot replace domain and SAP authorization.

### Mistake 4: Using broad scopes such as `write`

The scope does not express object, property, organization or threshold.

### Mistake 5: Exposing generic CRUD APIs

The caller receives more authority than the business task requires.

### Mistake 6: Logging only the technical user

The human, client, agent and workflow identities disappear.

### Mistake 7: Reusing production credentials in test

Environment boundaries become ineffective.

### Mistake 8: Rotating certificates only after expiry incidents

The documented procedure has never been proven.

### Mistake 9: Sending complete SAP objects to every consumer

Sensitive fields are exposed unnecessarily.

### Mistake 10: Allowing every event consumer to subscribe broadly

Loose coupling becomes broad data access.

### Mistake 11: Treating replay as a normal support action

A technical recovery operation repeats a sensitive business effect.

### Mistake 12: Giving agents the same APIs as deterministic applications

The trust and decision models are different.

### Mistake 13: Monitoring invalid logins but not valid business abuse

A compromised valid identity remains invisible.

### Mistake 14: Testing only authorized happy paths

Broken object, property and function authorization remains undetected.

### Mistake 15: Revoking a credential without reconciling business effects

Future access stops, but completed malicious or accidental actions remain.

## Questions architects and managers should ask

1. Which identity does SAP see for each integration?
2. How many processes share the same technical user?
3. Can one compromised flow execute operations belonging to another domain?
4. Where does human identity need to be preserved?
5. Which actions are performed by workload identities?
6. Are authentication, authorization and approval separated?
7. Does authorization include business object and organization?
8. Can a read client call a write operation?
9. Can a caller change fields outside its purpose?
10. Which APIs expose sensitive business flows?
11. Are business volume and value limits enforced?
12. Which consumer can publish each business event?
13. Who may replay events and messages?
14. Are secrets stored and rotated through a controlled process?
15. Can one production client be isolated quickly?
16. Are old API versions and partner connections still active?
17. Which data is logged unnecessarily?
18. Are agent tools narrower than normal application APIs?
19. Can the complete human–agent–integration–SAP action chain be audited?
20. After a credential compromise, can we identify every business effect?

## The goal is controlled authority

A secure integration architecture does not merely verify that a request came from an approved application.

It limits what that application can do.

It does not merely encrypt the connection to SAP.

It controls the backend identity and role.

It does not merely protect endpoints.

It protects business objects, properties, functions and sensitive workflows.

SAP Integration Suite and API Management currently provide platform-level capabilities for centralized governance, enterprise security policies, traffic monitoring, anomaly detection and governed exposure of APIs and MCP servers.

NIST’s zero-trust principles provide the wider architectural direction: do not grant implicit trust based on location, and focus security decisions on identities, resources and individual access.

OWASP’s API guidance shows why authentication alone is insufficient. Object-level, property-level and function-level authorization, resource controls, sensitive business-flow protection and inventory management must all be considered.

The decisive test is simple:

> If this one API client, integration flow or agent is compromised, what can it actually do in SAP?

When the honest answer is “almost everything,” the architecture is not secure.

It has a secure entrance connected to an overprivileged backend.

A strong design preserves identity where required, uses bounded workload identities, enforces business authorization in the owning domain and keeps SAP permissions aligned with the real purpose of the integration.

That is how security survives beyond the gateway.

---

### SAP integration security architecture checklist

- [ ] Every human, workload, partner and agent identity is distinguishable.
- [ ] Authentication, authorization and business approval are separated.
- [ ] Network location does not create implicit trust.
- [ ] Trust boundaries and identity changes are documented.
- [ ] API scopes are supplemented by domain authorization.
- [ ] Object-level authorization is enforced.
- [ ] Property-level authorization protects sensitive fields.
- [ ] Function-level authorization separates normal and privileged actions.
- [ ] Shared high-privilege SAP technical users are eliminated or reduced.
- [ ] Workload identities are aligned with bounded business purposes.
- [ ] Production, test and development identities are separate.
- [ ] Human identity is propagated where individual authority matters.
- [ ] The delegation chain remains auditable.
- [ ] API gateway controls do not replace backend authorization.
- [ ] Sensitive business flows have value, volume and velocity controls.
- [ ] Expensive queries and payloads have resource limits.
- [ ] APIs, events, partners and identities are inventoried.
- [ ] Contracts expose only the data required by the consumer.
- [ ] Secrets are stored, owned, rotated and revocable.
- [ ] Tokens, passwords and sensitive payloads are excluded from logs.
- [ ] Event producers and consumers have bounded permissions.
- [ ] Replay is treated as a privileged business operation.
- [ ] Partner files and messages include origin, integrity and duplicate controls.
- [ ] Agent-facing tools are narrower than generic backend APIs.
- [ ] Agent recommendation and execution authority are separated.
- [ ] Security monitoring includes valid but abnormal business activity.
- [ ] Negative authorization tests are automated.
- [ ] Backend technical roles are reviewed directly.
- [ ] Security incidents trigger business-transaction reconciliation.
- [ ] One compromised identity can be isolated without stopping the platform.

### Sources and further reading

SAP currently describes SAP Integration Suite as a secure iPaaS connecting applications, data, processes, business partners and AI agents across SAP and third-party landscapes, with centralized governance, real-time monitoring and built-in security.

SAP API Management currently provides enterprise security policies, centralized controls, usage and performance analytics, anomaly monitoring and API lifecycle governance. SAP’s current MCP lifecycle capabilities allow curated APIs to be exposed to agents with design-time and runtime controls and production traceability.

NIST SP 800-207 defines zero trust as an architectural approach that removes implicit trust based solely on network location or asset ownership and focuses security on users, assets and resources.

The OWASP API Security Top 10 for 2023 covers risks including broken object-level authorization, broken authentication, broken property- and function-level authorization, unrestricted resource consumption, unrestricted access to sensitive business flows, security misconfiguration and improper inventory management.

*Reviewed: July 2026. SAP Integration Suite security capabilities, supported authentication methods, service packaging and agent-related features can change. Final security design should be validated against current SAP documentation, the connected systems, contractual controls and the organization’s identity and access-management policies.*

## Continue exploring

- [Modern SAP Integrations: How to Choose Between APIs, Events, Files, Queues, and Mapping Strategies](/blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [How to Design Resilience and Disaster Recovery for SAP Integrations Without Creating Duplicate Business Transactions](/blog/how-to-design-resilience-and-disaster-recovery-for-sap-integrations/)
- Next in the migration: [Why Master Data Distribution Fails Even When Every Interface Is Green](/blog/why-master-data-distribution-fails-even-when-every-interface-is-green/)
