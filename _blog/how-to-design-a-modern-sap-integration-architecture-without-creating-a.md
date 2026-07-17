---
layout: blog
title: "How to Design a Modern SAP Integration Architecture Without Creating a New Middleware Monolith"
description: "Around it are SAP S/4HANA, CRM, procurement, warehouses, banks, partners, data platforms, mobile applications and AI agents."
slug: how-to-design-a-modern-sap-integration-architecture-without-creating-a
permalink: /blog/how-to-design-a-modern-sap-integration-architecture-without-creating-a/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP integration architecture"
tags:
  - sap-integration-architecture
  - integration
  - sap-architecture
canonical_url: https://dkharlanau.github.io/blog/how-to-design-a-modern-sap-integration-architecture-without-creating-a/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 30
migration_sequence: 28
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/
  - /blog/where-should-mapping-logic-live-in-modern-sap-integrations/
---

## On this page

- [A practical target SAP integration architecture](#a-practical-target-sap-integration-architecture)
- [Where should logic live?](#where-should-logic-live)
- [The anti-corruption layer in SAP transformations](#the-anti-corruption-layer-in-sap-transformations)
- [Canonical models should be bounded](#canonical-models-should-be-bounded)
- [Separate operational integration from analytical integration](#separate-operational-integration-from-analytical-integration)
- [Separate operational events from data replication](#separate-operational-events-from-data-replication)
- [Design failure boundaries](#design-failure-boundaries)
- [Security architecture should follow business capability](#security-architecture-should-follow-business-capability)
- [AI should not become another integration layer](#ai-should-not-become-another-integration-layer)
- [Design-time and runtime architecture should be connected](#design-time-and-runtime-architecture-should-be-connected)
- [The architecture repository should contain decisions](#the-architecture-repository-should-contain-decisions)
- [Architecture decision records](#architecture-decision-records)
- [Architecture reviews should focus on a small number of questions](#architecture-reviews-should-focus-on-a-small-number-of-questions)
- [Common architecture failures](#common-architecture-failures)
- [A practical architecture programme](#a-practical-architecture-programme)
- [A strong pilot: order-to-fulfilment architecture](#a-strong-pilot-order-to-fulfilment-architecture)
- [Metrics for integration architecture](#metrics-for-integration-architecture)
- [Questions managers should ask](#questions-managers-should-ask)
- [The architecture should make change local](#the-architecture-should-make-change-local)

A company draws its target SAP integration architecture.

At the centre is one large box:

> Integration Platform

Around it are SAP S/4HANA, CRM, procurement, warehouses, banks, partners, data platforms, mobile applications and AI agents.

Every line passes through the central box.

The diagram looks controlled.

Then the implementation begins.

The integration platform starts to contain:

- customer matching;
- sales organization determination;
- supplier classification;
- material conversion;
- pricing adjustments;
- routing;
- workflow decisions;
- retries;
- temporary databases;
- process state;
- partner-specific exceptions;
- AI-agent tools.

Five years later, the company has reduced direct point-to-point connections.

It has also created a new central monolith.

The ERP still contains business logic.

The connected applications contain business logic.

The integration platform now contains another version of the same business logic.

No team can change a process without analysing all three.

This is the architectural problem that integration projects often miss.

A modern SAP integration architecture is not defined by the number of APIs, events or cloud services it contains.

It is defined by where responsibility lives.

A good architecture should make it possible to answer:

- Which system owns each business fact?
- Which domain owns each decision?
- Which layer translates data?
- Which layer coordinates processes?
- Which layer exposes capabilities?
- Which layer observes the result?
- What happens when one part is unavailable?
- How can one system be replaced without rebuilding every consumer?

SAP currently positions Integration Suite as a unified platform for connecting SAP and third-party applications, APIs, events, data, business partners and AI agents, with centralized governance, monitoring and security.

That is a platform scope.

Architecture begins one level above the platform.

### Architecture is the allocation of responsibility

An integration diagram usually shows components and connections.

A useful architecture must also show ownership.

Consider a customer order.

Several systems may participate:

- commerce application captures customer demand;
- CRM owns the commercial relationship;
- SAP S/4HANA owns the executable sales order;
- availability service confirms supply;
- warehouse system fulfils the delivery;
- finance owns the receivable;
- integration platform moves and translates messages;
- customer portal presents status.

The architecture should define which system is authoritative for each state.

For example:

- customer request: commerce;
- negotiated offer: CRM or CPQ;
- accepted sales order: SAP S/4HANA;
- physical warehouse execution: warehouse system;
- accounting receivable: finance;
- customer-facing view: portal projection.

If these responsibilities remain unclear, middleware will gradually try to reconcile them through custom logic.

The platform becomes responsible for deciding which system is correct.

That is not integration.

That is accidental master data and process governance.

### Start with business domains, not applications

Applications are implementation choices.

Business domains are more stable.

A landscape may contain domains such as:

- customer;
- sales;
- product;
- procurement;
- supplier;
- inventory;
- fulfilment;
- finance;
- billing;
- workforce.

SAP S/4HANA may implement several domains.

A cloud application may implement another.

A legacy system may still own part of a domain during transition.

The important point is that integration contracts should follow domain responsibility rather than application topology alone.

For example, a `Customer` domain may expose:

- retrieve approved customer identity;
- request customer creation;
- publish customer block changes;
- provide customer organizational readiness.

The contract should not change completely because the customer record moves from one technical system to another.

This is how architecture reduces migration coupling.

### A system of record is not the owner of every interpretation

The term “system of record” is often used too broadly.

A system may be authoritative for one part of an object and not another.

For a business partner:

- central governance may own legal identity;
- finance may own payment-risk status;
- sales may own sales-area attributes;
- procurement may own supplier purchasing data;
- a local system may own regulatory enrichment.

The architecture needs attribute-level or capability-level authority where necessary.

Otherwise, teams say:

> SAP is the system of record.

But several SAP and non-SAP components maintain different parts of the object.

Integration then becomes a constant attempt to synchronize records without a clear ownership model.

### The target architecture should separate six responsibilities

A practical modern SAP integration architecture can be divided into six main responsibilities:

1. domain systems and business capabilities;
2. interaction contracts;
3. integration execution;
4. process coordination;
5. control and governance;
6. operational and business observability.

These are logical responsibilities.

They do not always require six separate products.

The separation matters because each responsibility changes for different reasons.

### Layer 1: Domain systems and business capabilities

This layer contains the applications that own business state.

Examples include:

- SAP S/4HANA;
- SAP SuccessFactors;
- SAP Ariba;
- SAP Sales Cloud;
- SAP MDG;
- warehouse systems;
- planning systems;
- banking platforms;
- custom BTP applications;
- external partner systems.

These systems should own their domain behaviour.

For example:

#### SAP sales domain

May own:

- sales order creation;
- sales document status;
- pricing execution;
- delivery relevance;
- billing relevance.

#### Warehouse domain

May own:

- warehouse task;
- picking;
- packing;
- physical stock movement;
- warehouse execution status.

#### Supplier governance domain

May own:

- supplier identity;
- approval state;
- duplicate decision;
- centrally governed attributes.

The integration layer should not recreate this behaviour.

It should call, publish or translate it.

### Domain applications should expose deliberate boundaries

A domain application should not expose every internal structure to every consumer.

It should provide controlled interaction boundaries:

- business APIs;
- business events;
- approved bulk extracts;
- commands;
- status queries.

The external contract should describe a business capability.

It should not require consumers to understand internal tables, status values or technical configuration unless those details are genuinely part of the business contract.

### Layer 2: Interaction contracts

This layer defines how domains communicate.

It includes:

- synchronous APIs;
- asynchronous commands;
- business events;
- bulk data contracts;
- B2B documents;
- files where appropriate.

The key architectural principle is:

> Select the contract based on the business interaction, not based on the preferred integration technology.

### Synchronous API contract

Use when the caller needs an immediate result or validation.

Examples:

- check availability;
- retrieve price;
- validate customer;
- submit a short business transaction;
- retrieve current status.

The contract creates runtime dependency.

The caller depends on the provider being available and responsive.

Use that dependency deliberately.

### Asynchronous command contract

Use when one domain requests another domain to perform work, but the result does not need to be immediate.

Examples:

- create fulfilment request;
- generate customer document;
- start onboarding workflow;
- process a large adjustment.

The command has an intended responsibility.

It should not be disguised as an event.

### Business event contract

Use when a domain announces that a meaningful state change has already occurred.

Examples:

- sales order confirmed;
- supplier approved;
- goods issue posted;
- invoice cancelled.

SAP currently describes Event Mesh as supporting the distribution of business events across SAP and third-party hybrid landscapes, real-time subscription-based reactions and reliable asynchronous communication without tight coupling.

The broker supports delivery.

The architecture must define event meaning, version, ordering, replay and consumer responsibility.

### Bulk contract

Use for large periodic or historical transfer where:

- immediate response is not required;
- reconciliation matters;
- transaction volume is high;
- processing can occur in batches.

A modern architecture does not prohibit files.

It makes their role explicit.

### B2B contract

Use for external partner interaction where:

- partner identifiers differ;
- industry standards apply;
- acknowledgement protocols matter;
- partner onboarding and versioning are required.

The internal business contract should remain separate from the partner-specific representation.

### Contracts should remain stable while implementations change

Suppose SAP ECC is replaced by S/4HANA.

A customer-facing order API should not necessarily change because the internal document model changed.

The contract should represent the stable business interaction.

An adapter or anti-corruption layer can translate the contract during the transition.

This is one of the most important goals of an integration architecture:

> Consumers depend on capabilities, not on migration projects.

### Layer 3: Integration execution

This is the layer most commonly associated with middleware.

Its proper responsibilities include:

- connectivity;
- protocol conversion;
- structural transformation;
- message routing;
- technical enrichment;
- partner-specific mapping;
- splitting and aggregation;
- security mediation;
- technical retry;
- correlation;
- integration-flow execution.

SAP Cloud Integration currently supports A2A, B2B and B2G integration flows across SAP and third-party landscapes, including transformation, prebuilt content, mapping assistance and hybrid execution options.

This is a legitimate and important architectural layer.

The mistake is allowing it to become responsible for domain truth.

### Integration execution should not own business policy

Weak integration logic includes:

- deciding which customers receive limited stock;
- approving a supplier classification;
- determining a commercial discount;
- deciding whether a blocked order should be released;
- defining accounting meaning.

These rules may technically execute inside an integration flow.

Their definition and ownership should remain in the appropriate business domain.

A useful distinction is:

#### Execution location

Where the rule runs.

#### Semantic ownership

Who defines and approves what the rule means.

The integration platform may execute a governed mapping.

It should not become the only place where the business rule exists.

### Create a clear policy for middleware logic

A practical policy may classify integration logic into four levels.

#### Level 1: Technical transformation

Examples:

- XML to JSON;
- date format;
- protocol;
- header;
- compression;
- encryption.

Owner:

- integration engineering.

#### Level 2: Cross-system representation

Examples:

- partner code to internal code;
- source structure to target structure;
- identifier correlation;
- message grouping.

Owner:

- integration engineering with data-domain approval.

#### Level 3: Domain derivation

Examples:

- determine sales organization;
- classify supplier;
- derive financial category;
- calculate fulfilment priority.

Owner:

- business domain.

Middleware may execute only through an approved rule or service.

#### Level 4: Business decision

Examples:

- accept credit risk;
- approve price exception;
- allocate scarce inventory;
- approve sensitive master data.

Owner:

- accountable role or domain workflow.

Do not hide these decisions in integration code.

### Layer 4: Process coordination

Some business processes cross several domains and require explicit coordination.

Examples include:

- order-to-cash;
- supplier onboarding;
- return and refund;
- hire-to-retire;
- invoice dispute;
- master data distribution.

Event-driven choreography can connect independent reactions.

But complex processes often need:

- current process state;
- deadlines;
- approval;
- compensation;
- escalation;
- human tasks;
- recovery.

This is the role of orchestration or workflow.

### Do not confuse integration flow with business workflow

An integration flow may:

- receive message;
- transform it;
- call target;
- process response.

A business workflow may:

- request approval;
- wait two days;
- escalate;
- request additional data;
- perform several domain actions;
- compensate a completed step;
- close only after business verification.

Putting a long-running business process inside a technical integration flow creates operational problems:

- process state is difficult to understand;
- human tasks are external;
- retries can repeat business actions;
- timeouts and waiting become technical constructs;
- business owners cannot see the process.

Use integration middleware to connect process steps.

Use workflow or process orchestration to own the long-running business state.

### Choreography versus orchestration

#### Choreography

Domains publish events and react independently.

Good for:

- optional consumers;
- projections;
- notifications;
- loosely coupled follow-up actions;
- simple state propagation.

Risks:

- hidden process chain;
- weak end-to-end ownership;
- circular reactions;
- difficult recovery.

#### Orchestration

A coordinator manages the sequence and state.

Good for:

- mandatory multi-step process;
- approvals;
- deadlines;
- compensating action;
- explicit completion criteria.

Risks:

- coordinator becomes oversized;
- domain autonomy is reduced;
- process logic centralizes excessively.

A practical architecture normally uses both.

Use events to communicate facts.

Use orchestration where the business requires controlled completion.

### The orchestrator should not become another ERP

An orchestrator should coordinate domains.

It should not duplicate their internal decision logic.

For example, a supplier-onboarding workflow may coordinate:

1. collect request;
2. request duplicate check;
3. request compliance review;
4. request finance approval;
5. request supplier creation;
6. wait for target readiness.

The workflow should not implement:

- duplicate-matching algorithm;
- tax validation;
- account determination;
- target-specific supplier configuration.

Those responsibilities belong to the relevant domains.

The orchestrator owns process state, not every rule.

### Layer 5: Control and governance

A modern integration platform needs a control plane.

The control plane governs:

- API lifecycle;
- event catalogue;
- schema versions;
- integration inventory;
- security policies;
- deployment standards;
- ownership;
- runtime policies;
- deprecation;
- design decisions.

This is different from the data plane, where production messages and calls move.

### API management belongs to the control boundary

API Management should provide:

- authentication and authorization;
- traffic policies;
- quotas;
- monitoring;
- version exposure;
- developer onboarding;
- central governance.

SAP currently describes API Management as providing enterprise security policies, centralized controls, usage and performance analytics and lifecycle governance.

It should not become the primary home of business orchestration or pricing logic.

### Event governance is equally important

An event catalogue should show:

- publisher;
- business meaning;
- schema;
- version;
- ordering;
- retention;
- security;
- consumers;
- owner;
- lifecycle state.

Without this, the event mesh becomes a distributed message network that nobody can safely change.

### Integration Assessment and ISA-M are governance tools, not substitutes for ownership

SAP currently positions Integration Assessment as a structured way to evaluate integration readiness and architecture gaps, and the SAP Integration Solution Advisory Methodology as a framework using reference architectures, standards and development guidelines.

These methods can improve consistency.

They cannot resolve questions such as:

- Who owns customer classification?
- Which process may tolerate eventual consistency?
- Which system is authoritative for order status?
- Which team owns a failed supplier replication?

The method supports decisions.

The organization must still make them.

### Governance should define allowed patterns

A useful architecture does not approve every interface individually from zero.

It defines approved patterns.

For example:

#### Pattern A: Synchronous business query

- managed API;
- strict timeout;
- no long-running process;
- caching policy;
- actionable errors.

#### Pattern B: Asynchronous business command

- persistent queue;
- idempotency;
- process-status API;
- retry classification;
- business verification.

#### Pattern C: Business event

- committed business fact;
- versioned schema;
- duplicate-safe consumer;
- replay policy;
- event catalogue.

#### Pattern D: Bulk transfer

- manifest;
- record count;
- control totals;
- sequence;
- restart;
- reconciliation.

#### Pattern E: Partner integration

- partner profile;
- standard document;
- acknowledgement;
- partner-specific mapping;
- operational contact.

Teams should choose from these patterns and justify exceptions.

This is faster and safer than building a new architecture for every project.

### Layer 6: Operational and business observability

Integration observability is often too technical.

Teams monitor:

- endpoint availability;
- HTTP code;
- message status;
- queue depth;
- runtime error;
- certificate expiry.

These signals are necessary.

They do not prove that the business process worked.

### Technical observability

Should answer:

- Did the integration execute?
- Was the endpoint available?
- Was the message transformed?
- Did authentication succeed?
- Is the queue growing?
- Are retries increasing?

### Business observability

Should answer:

- Did every expected order reach the target?
- Was any invoice duplicated?
- Which suppliers remain unusable?
- Are warehouse confirmations delayed?
- Which payments were not posted?
- Did the end-to-end process complete?

The architecture must connect both views.

### Reconciliation is an architectural component

Reconciliation should not be added as a support report after go-live.

It should be designed with the integration.

For every critical flow, define:

- expected source transactions;
- published or transmitted transactions;
- accepted target transactions;
- rejected items;
- duplicates;
- final business state.

For example:

```text
10,000 orders accepted by source
10,000 integration requests created
9,997 SAP orders created
2 rejected for master data
1 awaiting manual review
0 duplicates
```

This is an operationally controlled architecture.

A dashboard showing 100% middleware availability does not provide the same assurance.

### The architecture should expose uncertainty

Distributed systems produce uncertain states.

Examples include:

- API timed out after target commit;
- event was delivered but consumer outcome is unknown;
- file was received but record processing is incomplete;
- one target accepted master data and another rejected it.

Do not force every status into success or failure.

Use states such as:

- accepted;
- processing;
- completed;
- partially completed;
- failed;
- uncertain;
- awaiting decision.

Uncertainty should trigger controlled investigation.

It should not trigger blind replay.

## A practical target SAP integration architecture

A useful target model can be expressed as the following logical structure:

```text
Channels, Partners, Applications, AI Agents
                 |
         Managed Business APIs
         Business Events
         B2B / Bulk Contracts
                 |
      Process Coordination Layer
        Workflow / Orchestration
                 |
      Integration Execution Layer
 Transformation / Routing / Protocol
 Correlation / Technical Retry / B2B
                 |
       Domain Capability Boundaries
 Sales | Procurement | Product | Finance
 Customer | Supplier | Fulfilment | Billing
                 |
        Systems of Business Record
 SAP S/4HANA | SAP Cloud Apps | Legacy
 Warehouses | Banks | Partner Platforms
```

Across every layer:

```text
Security
Identity
Observability
Reconciliation
Lifecycle Governance
Schema and Mapping Registry
```

This is not a product deployment diagram.

It is a responsibility diagram.

### Channels should not call SAP internals directly

Channels include:

- web portal;
- mobile application;
- commerce platform;
- partner application;
- AI assistant.

They should consume stable business capabilities.

A channel should not need to know:

- internal SAP document type;
- condition technique;
- target-specific status codes;
- internal table keys;
- backend migration state.

Channel-specific presentation may exist in an experience layer.

The business capability should remain reusable.

### Avoid one universal enterprise service layer

A common architecture creates one central service layer that every application must use.

Over time, it becomes responsible for:

- all data access;
- all orchestration;
- all mappings;
- all security;
- all canonical models.

This creates organizational and technical bottlenecks.

Prefer domain-aligned capabilities with centralized governance.

Centralize:

- standards;
- platform;
- security controls;
- discovery;
- shared tooling.

Federate:

- business semantics;
- domain APIs;
- domain events;
- domain ownership;
- process decisions.

This is the difference between a centralized platform and a centralized application.

### Platform team versus domain teams

A practical operating model separates responsibilities.

### Integration platform team

Owns:

- Integration Suite environments;
- connectivity;
- API gateway;
- event infrastructure;
- deployment pipeline;
- shared observability;
- runtime standards;
- security integration;
- reusable technical components.

### Domain teams

Own:

- business APIs;
- business events;
- semantic contracts;
- domain rules;
- data quality;
- consumer commitments;
- domain support.

### Process owners

Own:

- end-to-end business outcome;
- cross-domain service levels;
- business exceptions;
- priorities;
- recovery requirements.

### Enterprise architecture

Owns:

- principles;
- target patterns;
- lifecycle governance;
- exception decisions;
- portfolio coherence.

The platform team should not become responsible for every failed business transaction simply because it passed through the platform.

### Create a federated integration model

Pure centralization is slow.

Pure decentralization creates inconsistency.

A federated model combines:

#### Central platform and standards

- approved technologies;
- common policies;
- shared security;
- runtime;
- templates;
- catalogues;
- observability.

#### Distributed domain ownership

- API design;
- event meaning;
- data semantics;
- business rules;
- service commitments.

This allows teams to move independently while preserving architectural consistency.

## Where should logic live?

This is the most important decision in integration architecture.

A practical placement model can use four questions.

### Question 1: Who owns the business meaning?

Place the rule with or under governance of that domain.

### Question 2: Is the logic specific to one target?

Keep it near the target or its adapter.

### Question 3: Is the logic a cross-system transformation?

Middleware is appropriate.

### Question 4: Is the logic a long-running process decision?

Use workflow or orchestration.

### Example: sales organization determination

Possible logic:

- external channel sends customer and fulfilment region;
- SAP needs sales organization and distribution channel.

The business meaning belongs to the sales domain.

The integration platform may translate identifiers.

SAP or a sales-domain service should determine the sales organization using governed rules.

Do not copy the determination separately into every integration flow.

### Example: unit conversion

The material or product domain should own:

- base unit;
- conversion factor;
- packaging relationship.

Middleware can convert partner representation.

It should not independently maintain product conversion truth.

### Example: partner EDI mapping

Partner-specific message representation belongs in B2B integration.

The internal order meaning should remain a stable domain contract.

The partner mapping should not implement SAP pricing or availability logic.

### Example: credit block release

The integration layer may:

- collect evidence;
- invoke workflow;
- call the approved release action.

The credit decision belongs to the credit domain and accountable role.

## The anti-corruption layer in SAP transformations

An anti-corruption layer protects a new domain or consumer from a legacy model.

This is especially useful during:

- ECC to S/4HANA migration;
- phased cloud adoption;
- replacement of legacy warehouse;
- consolidation of multiple ERPs;
- acquisition integration.

The layer may:

- translate old codes;
- normalize identifiers;
- hide legacy structures;
- expose stable APIs;
- publish business events;
- preserve correlation.

### The layer needs a defined purpose

A strong anti-corruption layer has:

- bounded scope;
- clear owner;
- documented mappings;
- performance target;
- decommissioning conditions.

A weak layer becomes permanent middleware that contains both old and new business logic.

### Do not design the future model as a copy of the legacy system

During migration, teams often expose the old structure through a new API.

This makes cutover easier.

It also carries historical coupling into the new architecture.

Use the anti-corruption layer to translate toward the intended domain model.

Do not use it only to repaint legacy structures.

## Canonical models should be bounded

A canonical model can reduce repeated mapping.

It can also become an enterprise-wide schema that nobody can change.

Use canonical models where real semantic reuse exists.

Good bounded examples include:

- customer identity;
- order fulfilment request;
- shipment event;
- supplier-onboarding request;
- billing event.

Avoid one object that attempts to combine every customer field from:

- CRM;
- ERP;
- marketing;
- finance;
- service;
- analytics.

That model becomes too broad to own.

### Canonical models are contracts, not databases

A canonical model should define shared interaction meaning.

It should not become a central copy of all business data unless that is an explicit data-platform requirement.

Operational integration and analytical data consolidation are different architectures.

## Separate operational integration from analytical integration

Operational integration supports business execution.

Examples:

- create order;
- approve supplier;
- send warehouse task;
- post payment.

It requires:

- transaction control;
- error handling;
- low or predictable latency;
- idempotency;
- business verification.

Analytical integration supports:

- reporting;
- forecasting;
- machine learning;
- historical analysis.

It may use:

- replication;
- data pipelines;
- change data capture;
- lakehouse;
- batch.

Do not use an analytical data platform as the operational source merely because it contains a convenient copy.

Do not call operational APIs millions of times to build analytical datasets when a controlled replication pattern is more suitable.

## Separate operational events from data replication

A business event announces a meaningful state transition.

A data-change stream distributes data changes.

The same platform may support both.

The contracts and consumers are different.

For example:

#### Business event

`Invoice.Posted`

Used to:

- notify customer portal;
- trigger collection process;
- start downstream business action.

#### Data replication

Invoice records and line items copied to analytics.

Used for:

- reporting;
- trend analysis;
- model training.

Consumers should not reconstruct critical process actions from low-level data replication unless that is a deliberate design.

## Design failure boundaries

A good architecture limits the effect of failure.

Consider a customer order.

The architecture should define:

- what must succeed before the customer receives acceptance;
- what can continue asynchronously;
- which downstream failure blocks fulfilment;
- which optional consumer failure can be ignored temporarily;
- how the order is reconciled.

### Do not make every dependency synchronous

If order acceptance synchronously depends on:

- CRM;
- pricing;
- inventory;
- tax;
- credit;
- warehouse;
- analytics;
- notification,

the complete service becomes fragile.

Separate:

#### Required immediate decisions

Examples:

- customer valid;
- product valid;
- minimum commercial validation.

#### Required later processing

Examples:

- warehouse preparation;
- document generation;
- analytics;
- notification.

This reduces runtime coupling while preserving business control.

### Use circuit breakers and load protection deliberately

Technical resilience patterns may include:

- timeout;
- circuit breaker;
- retry;
- rate limit;
- queue;
- backpressure.

They should reflect business semantics.

Retrying a price lookup may be safe.

Retrying a payment command may not be safe without idempotency.

Buffering warehouse requests may protect availability.

It may also create an invisible operational backlog.

Every resilience pattern needs business observability.

## Security architecture should follow business capability

Integration security is not only network and authentication.

It includes:

- which consumer may access which data;
- which action may be performed;
- which organization is in scope;
- which amount or risk limit applies;
- whether approval is required.

A generic technical user with broad SAP roles weakens the entire architecture.

Use purpose-specific access.

For example:

- read order status;
- submit standard order;
- request cancellation;
- retrieve approved supplier;
- propose bank change.

Do not expose generic unrestricted update operations merely because they are easier to implement.

### API and agent security need bounded tools

SAP’s current API lifecycle capabilities include governed exposure of curated APIs as MCP servers for agent use, with design-time and runtime controls and production observability.

This makes architecture discipline more important.

An AI agent should receive:

- narrow read tools;
- narrow prepared-action tools;
- explicit approval paths;
- rate limits;
- audit;
- post-action verification.

The integration layer should not convert a broad backend API into an equally broad agent tool.

## AI should not become another integration layer

A dangerous pattern is:

1. agent reads data from several systems;
2. agent interprets inconsistencies;
3. agent decides which system is correct;
4. agent updates several targets.

This appears flexible.

It bypasses:

- domain ownership;
- deterministic mappings;
- workflow approval;
- reconciliation.

AI can assist with:

- evidence gathering;
- schema comparison;
- mapping proposals;
- error classification;
- documentation;
- impact analysis.

Business truth should still be governed through stable domains and controlled workflows.

## Design-time and runtime architecture should be connected

Many organizations govern design through documents.

Runtime implementation evolves separately.

A good architecture should connect:

- integration requirement;
- selected pattern;
- API or event contract;
- mapping;
- implementation artifact;
- deployment;
- owner;
- monitoring;
- incident history.

This allows the organization to answer:

- Why was this pattern selected?
- Which business service depends on it?
- Which mapping version is active?
- Which consumers use this API?
- Which incidents indicate architecture weakness?

A static diagram cannot provide this.

## The architecture repository should contain decisions

A useful integration repository should include:

- domain map;
- application map;
- capability catalogue;
- API catalogue;
- event catalogue;
- interface catalogue;
- mapping registry;
- ownership;
- architecture decision records;
- service-level expectations;
- lifecycle status.

Do not document only technical endpoints.

Document why the interaction exists and why the chosen pattern fits.

## Architecture decision records

For each material integration decision, record:

- context;
- business requirement;
- options considered;
- chosen pattern;
- reasons;
- trade-offs;
- failure model;
- owner;
- review date.

Example:

**Decision:** Use business event for delivery completion
**Reason:** Multiple consumers require the fact; source must not wait
**Trade-off:** Eventual consistency
**Controls:** Object version, replay, reconciliation, mandatory warehouse consumer monitoring

This preserves reasoning for future teams.

## Architecture reviews should focus on a small number of questions

A review should not become a large theoretical exercise.

Ask:

1. Which domain owns the business state?
2. Is the interaction a query, command, event, bulk flow or B2B exchange?
3. Why is the interaction synchronous or asynchronous?
4. Where does semantic mapping live?
5. Is business policy hidden in integration code?
6. Can duplicate processing create a business effect?
7. How is the complete outcome verified?
8. What happens when one system is unavailable?
9. How will the contract evolve?
10. Who operates and supports it?

These questions expose most serious architecture weaknesses.

## Common architecture failures

### Failure 1: One central middleware monolith

Every integration and rule is placed in one platform.

Result:

- central bottleneck;
- duplicated domain logic;
- difficult testing;
- broad blast radius.

### Failure 2: Pure point-to-point APIs

Every consumer receives its own endpoint and payload.

Result:

- modern protocol;
- old coupling;
- duplicated mappings;
- consumer-specific logic.

### Failure 3: Enterprise canonical model for everything

One universal schema attempts to represent the whole company.

Result:

- hundreds of optional fields;
- unclear ownership;
- slow change;
- constant translation.

### Failure 4: Event-driven architecture without process ownership

Services publish and consume events independently.

Result:

- hidden process chains;
- no completion view;
- difficult recovery;
- circular behaviour.

### Failure 5: API gateway as workflow engine

Business logic and state are added to gateway policies.

Result:

- invisible process behaviour;
- difficult lifecycle;
- platform lock-in.

### Failure 6: Integration team owns business semantics

Technical specialists become the only people who understand mappings and routing decisions.

Result:

- business rules hidden in code;
- inconsistent outcomes;
- provider dependency.

### Failure 7: System-of-record declared at object level only

Different domains own different attributes, but architecture treats one application as authoritative for everything.

Result:

- data conflicts;
- unclear correction responsibility;
- integration loops.

### Failure 8: Technical monitoring without reconciliation

Every message is green.

Business transactions are missing or duplicated.

Result:

- incidents discovered by users or finance.

### Failure 9: Operational and analytical flows mixed together

Data platform copies become operational sources.

Transactional APIs are used for mass analytics.

Result:

- performance issues;
- stale decisions;
- unclear authority.

### Failure 10: AI agents bypass domain boundaries

Agents call broad APIs and resolve conflicts probabilistically.

Result:

- uncontrolled business changes;
- weak audit;
- inconsistent truth.

## A practical architecture programme

### Phase 1: Map business domains

Identify:

- domain;
- owner;
- authoritative capabilities;
- main business objects;
- cross-domain dependencies.

### Phase 2: Inventory interactions

Record:

- source;
- target;
- purpose;
- pattern;
- volume;
- criticality;
- ownership;
- failure behaviour.

### Phase 3: Find misplaced logic

Search for business rules inside:

- middleware;
- scripts;
- files;
- API policies;
- custom adapters;
- manual support procedures.

Classify what should move or become governed.

### Phase 4: Define target patterns

Create approved designs for:

- synchronous API;
- asynchronous command;
- business event;
- B2B;
- bulk transfer;
- long-running workflow;
- analytical replication.

### Phase 5: Establish the control plane

Implement:

- API catalogue;
- event catalogue;
- mapping registry;
- lifecycle;
- security policies;
- deployment standards;
- ownership.

### Phase 6: Establish business observability

Add:

- correlation;
- business status;
- reconciliation;
- service dashboards;
- exception ownership.

### Phase 7: Select one end-to-end business service

Choose a meaningful process such as:

- customer order;
- supplier onboarding;
- delivery confirmation;
- invoice creation.

Redesign the interactions using the target architecture.

### Phase 8: Migrate by domain

Avoid random interface migration.

Modernize related contracts and mappings together.

### Phase 9: Remove duplicate logic

Consolidate rules under domain ownership.

Do not merely copy them to new Integration Suite flows.

### Phase 10: Govern through evidence

Use incidents, change lead time, consumer onboarding and reconciliation results to improve the architecture.

## A strong pilot: order-to-fulfilment architecture

Consider one customer-order process.

### Channel layer

A commerce application submits:

- external order ID;
- customer;
- products;
- quantities;
- requested fulfilment.

### Sales API

The sales domain validates and creates the SAP order.

It returns:

- request status;
- SAP order reference;
- business warnings;
- correlation ID.

### Sales event

After commit, the sales domain publishes:

- `SalesOrder.Created`;
- object version;
- relevant fulfilment context.

### Process coordinator

A coordinator tracks mandatory fulfilment steps where necessary.

### Integration execution

Integration Suite handles:

- protocol;
- customer and product identifier translation;
- message routing;
- technical retry;
- correlation.

It does not determine price or inventory policy.

### Warehouse command

A persistent asynchronous command requests fulfilment.

### Warehouse event

Warehouse publishes:

- accepted;
- picking completed;
- goods issued;
- rejected.

### Customer portal

Consumes status events and retrieves additional details through managed APIs.

### Reconciliation

The service verifies:

- accepted customer orders;
- SAP orders;
- warehouse requests;
- fulfilment results;
- unresolved exceptions.

### Ownership

- sales domain owns order;
- warehouse domain owns physical execution;
- process owner owns customer fulfilment outcome;
- platform team owns integration runtime;
- integration team owns technical translation;
- business domains own semantics.

This is architecture.

It is more than connecting two endpoints.

## Metrics for integration architecture

### Change amplification

How many integrations must change when one domain changes a contract?

A good architecture should reduce unnecessary propagation.

### Duplicate business-rule count

How many times is one determination implemented across systems and flows?

### Consumer onboarding time

How long does a new consumer need to use an approved capability?

### End-to-end completion rate

How many transactions complete across all mandatory domains?

### Reconciliation coverage

What percentage of critical integrations has business-level reconciliation?

### Unknown-owner rate

How many APIs, events, mappings and interfaces lack accountable owners?

### Contract reuse

How many consumers use stable shared contracts without forks?

### Middleware business-logic density

How much domain policy is implemented only inside integration assets?

### Incident transfer rate

How often does an integration incident move between teams before ownership is established?

### Recovery time

How quickly can the organization determine:

- what happened;
- what completed;
- what must be replayed;
- what must not be repeated?

### Version retirement time

How long do obsolete API and event versions remain active?

### Architecture exception rate

How many new integrations require patterns outside the approved architecture?

## Questions managers should ask

1. Which business domains does our integration landscape connect?
2. Which system owns each important business fact?
3. Is Integration Suite translating processes or deciding them?
4. How much business logic exists only in middleware?
5. Which APIs expose SAP internals directly?
6. Which events represent stable business facts?
7. Which processes require orchestration rather than choreography?
8. Can we trace one transaction from source intent to final outcome?
9. Which integrations lack reconciliation?
10. Can a new consumer use a capability without understanding the backend?
11. How would we replace one SAP or legacy system?
12. Which canonical models are actually reused?
13. Who owns mapping semantics?
14. Are platform and domain responsibilities separated?
15. Are AI agents using bounded governed capabilities?
16. Does our architecture reduce change cost, or only centralize runtime?

## The architecture should make change local

The main benefit of integration architecture is not visual order.

It is change isolation.

When a warehouse system changes, customer channels should not need to learn its internal model.

When SAP moves from ECC to S/4HANA, external applications should not need to redesign every business interaction.

When a new AI agent is introduced, it should use governed capabilities rather than receive unrestricted backend access.

When a business rule changes, the organization should know which domain owns it and which contracts are affected.

SAP Integration Suite currently brings together application integration, API lifecycle management, event-driven connectivity, B2B, hybrid deployment and agent-oriented access under one governed platform.

That breadth is useful.

It also makes architectural discipline more important.

When one platform can perform almost every integration task, teams may be tempted to place almost every responsibility inside it.

That is the wrong conclusion.

The platform should unify integration capabilities.

It should not centralize business ownership.

A modern SAP integration architecture has a controlled centre but does not have a central brain.

Business meaning remains in domains.

Processes have explicit owners.

Integration translates and connects.

APIs expose bounded capabilities.

Events communicate committed facts.

Workflow coordinates long-running outcomes.

Governance controls lifecycle.

Observability proves the business result.

The real architecture test is simple:

> Can one part of the landscape change without forcing the rest of the company to understand its internal implementation?

When the answer is yes, the architecture is doing its job.

When the answer is no, the organization may have modern technology, but it still has a tightly coupled system.

---

### Modern SAP integration architecture checklist

- [ ] Business domains are defined independently of applications.
- [ ] Authoritative ownership is explicit at capability or attribute level.
- [ ] Domain systems retain ownership of business logic.
- [ ] Interaction contracts are selected by business need.
- [ ] Queries, commands, events, bulk flows and B2B documents are separated.
- [ ] External contracts do not expose unnecessary SAP internals.
- [ ] APIs represent bounded business capabilities.
- [ ] Events represent committed business facts.
- [ ] Long-running processes use explicit workflow or orchestration.
- [ ] Middleware focuses on connectivity, translation and technical coordination.
- [ ] Business rules executed in middleware have external owners.
- [ ] API Management governs traffic and lifecycle rather than owning processes.
- [ ] Event schemas have owners, versions and replay policies.
- [ ] Canonical models are bounded to real domains.
- [ ] Operational and analytical integration are separated.
- [ ] Anti-corruption layers have clear scope and exit conditions.
- [ ] Synchronous dependencies are limited to immediate business needs.
- [ ] Asynchronous processing includes idempotency and reconciliation.
- [ ] Technical success and business completion are separate states.
- [ ] Critical flows include end-to-end business reconciliation.
- [ ] Platform teams and domain teams have distinct responsibilities.
- [ ] Governance is centralized while semantics remain federated.
- [ ] Security reflects business purpose and authority.
- [ ] AI agents receive bounded, governed capabilities.
- [ ] Architecture decisions and mappings are searchable.
- [ ] Success is measured through change isolation and business reliability.

### Sources and further reading

SAP currently positions SAP Integration Suite as a unified, secure integration platform for SAP and third-party applications, APIs, events, business partners, data and AI agents. Its current product scope includes centralized governance, monitoring, security, prebuilt content and support for cloud, on-premises and hybrid landscapes.

SAP Cloud Integration currently supports A2A, B2B and B2G integration flows, prebuilt content, third-party connectivity, mapping assistance and private runtime through edge integration cell for selected hybrid requirements.

SAP currently describes Event Mesh as supporting reliable asynchronous distribution of business events across SAP and third-party hybrid landscapes, while advanced event mesh supports distributed brokers, high-volume event streaming and event-flow visibility.

SAP currently describes API Management as providing security policies, analytics, centralized controls and API lifecycle governance. Its API capabilities also include Developer Hub, Graph and governed MCP server lifecycle management for AI-agent access.

SAP Integration Assessment and the SAP Integration Solution Advisory Methodology are currently positioned as structured approaches for assessing integration landscapes, using reference architectures and embedding governance and development standards.

*Reviewed: July 2026. SAP Integration Suite capabilities, packaging, deployment options and product naming can change. The target architecture should be validated against current SAP documentation, the deployed system editions and the organization’s actual domain ownership and operational requirements.*

## Continue exploring

- [Modern SAP Integrations: How to Choose Between APIs, Events, Files, Queues, and Mapping Strategies](/blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [How to Modernize SAP IDoc and File Integrations Without Rewriting the Entire Landscape](/blog/how-to-modernize-sap-idoc-and-file-integrations-without-rewriting-the/)
- Next in the migration: [How to Design a Transitional SAP Integration Architecture During an S/4HANA Transformation](/blog/how-to-design-a-transitional-sap-integration-architecture-during-an-s/)
