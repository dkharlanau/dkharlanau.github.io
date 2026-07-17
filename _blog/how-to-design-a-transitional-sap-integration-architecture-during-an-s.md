---
layout: blog
title: "How to Design a Transitional SAP Integration Architecture During an S/4HANA Transformation"
description: "SAP ECC will be replaced by SAP S/4HANA. Old middleware will move to SAP Integration Suite. New applications will use APIs and events."
slug: how-to-design-a-transitional-sap-integration-architecture-during-an-s
permalink: /blog/how-to-design-a-transitional-sap-integration-architecture-during-an-s/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP integration architecture"
tags:
  - sap-integration-architecture
  - integration
  - sap-architecture
canonical_url: https://dkharlanau.github.io/blog/how-to-design-a-transitional-sap-integration-architecture-during-an-s/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 30
migration_sequence: 29
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/
  - /blog/where-should-mapping-logic-live-in-modern-sap-integrations/
---

## On this page

- [The transition state is usually more complex than the target state](#the-transition-state-is-usually-more-complex-than-the-target-state)
- [Target architecture and transition architecture are different deliverables](#target-architecture-and-transition-architecture-are-different-deliverables)
- [Start with process migration boundaries](#start-with-process-migration-boundaries)
- [Migration by country or legal entity](#migration-by-country-or-legal-entity)
- [Migration by business process](#migration-by-business-process)
- [Migration by product or business unit](#migration-by-product-or-business-unit)
- [Migration by transaction date](#migration-by-transaction-date)
- [Migration by customer or partner segment](#migration-by-customer-or-partner-segment)
- [Define one operational writer for each business state](#define-one-operational-writer-for-each-business-state)
- [Avoid dual write](#avoid-dual-write)
- [Dual read is usually safer than dual write](#dual-read-is-usually-safer-than-dual-write)
- [Separate operational ownership from historical access](#separate-operational-ownership-from-historical-access)
- [Use stable business identifiers across the transition](#use-stable-business-identifiers-across-the-transition)
- [Do not reuse identifiers without source context](#do-not-reuse-identifiers-without-source-context)
- [The transition architecture needs an explicit routing model](#the-transition-architecture-needs-an-explicit-routing-model)
- [Central routing service versus distributed routing](#central-routing-service-versus-distributed-routing)
- [Routing must be based on governed migration status](#routing-must-be-based-on-governed-migration-status)
- [API facade as a transition boundary](#api-facade-as-a-transition-boundary)
- [The facade must not duplicate both ERPs](#the-facade-must-not-duplicate-both-erps)
- [Normalize results carefully](#normalize-results-carefully)
- [Anti-corruption layers protect the target model](#anti-corruption-layers-protect-the-target-model)
- [A good anti-corruption layer has an exit plan](#a-good-anti-corruption-layer-has-an-exit-plan)
- [Event bridge for old and new landscapes](#event-bridge-for-old-and-new-landscapes)
- [Do not turn every legacy message into an event](#do-not-turn-every-legacy-message-into-an-event)
- [Outbound event publication needs completeness checks](#outbound-event-publication-needs-completeness-checks)
- [Replication should have a declared purpose](#replication-should-have-a-declared-purpose)
- [Operational replication](#operational-replication)
- [Reporting replication](#reporting-replication)
- [Validation replication](#validation-replication)
- [Historical replication](#historical-replication)
- [Replicated data needs staleness rules](#replicated-data-needs-staleness-rules)
- [Do not use replicated copies for decisions they cannot safely support](#do-not-use-replicated-copies-for-decisions-they-cannot-safely-support)
- [Mapping must be versioned by migration wave](#mapping-must-be-versioned-by-migration-wave)
- [Mapping changes and cutover changes are linked](#mapping-changes-and-cutover-changes-are-linked)
- [Open transactions are harder than master data](#open-transactions-are-harder-than-master-data)
- [Finish in old system](#finish-in-old-system)
- [Migrate open transactions](#migrate-open-transactions)
- [Reference and continue](#reference-and-continue)
- [Process ownership may move at a different time from data](#process-ownership-may-move-at-a-different-time-from-data)
- [Shadow processing is safer than active dual processing](#shadow-processing-is-safer-than-active-dual-processing)
- [Shadow processing does not prove everything](#shadow-processing-does-not-prove-everything)
- [Active parallel run requires strict boundaries](#active-parallel-run-requires-strict-boundaries)
- [Design cutover as an architectural state change](#design-cutover-as-an-architectural-state-change)
- [Define the cutover boundary](#define-the-cutover-boundary)
- [Time alone may not be enough](#time-alone-may-not-be-enough)
- [In-flight messages need explicit treatment](#in-flight-messages-need-explicit-treatment)
- [Rollback must restore authority, not only software](#rollback-must-restore-authority-not-only-software)
- [Feature toggles help, but they do not reverse business state](#feature-toggles-help-but-they-do-not-reverse-business-state)
- [Transitional observability needs a cross-system view](#transitional-observability-needs-a-cross-system-view)
- [Record the routing decision](#record-the-routing-decision)
- [Reconciliation should be wave-specific](#reconciliation-should-be-wave-specific)
- [Build a transition control plane](#build-a-transition-control-plane)
- [Temporary architecture needs owners and expiry dates](#temporary-architecture-needs-owners-and-expiry-dates)
- [Treat temporary components as production software](#treat-temporary-components-as-production-software)
- [Decommissioning is part of architecture](#decommissioning-is-part-of-architecture)
- [Do not keep ECC because one interface still uses it](#do-not-keep-ecc-because-one-interface-still-uses-it)
- [A reference transitional architecture](#a-reference-transitional-architecture)
- [Example: phased order-to-cash migration](#example-phased-order-to-cash-migration)
- [Current state](#current-state)
- [Wave 1](#wave-1)
- [Inbound order architecture](#inbound-order-architecture)
- [Business identity](#business-identity)
- [Order status](#order-status)
- [Warehouse integration](#warehouse-integration)
- [Billing](#billing)
- [Reconciliation](#reconciliation)
- [Later waves](#later-waves)
- [Final state](#final-state)
- [Example: supplier master data during coexistence](#example-supplier-master-data-during-coexistence)
- [Central ownership](#central-ownership)
- [Target ownership](#target-ownership)
- [Distribution](#distribution)
- [Readiness](#readiness)
- [Transition rule](#transition-rule)
- [Decommission](#decommission)
- [Example: warehouse coexistence](#example-warehouse-coexistence)
- [Transitional architecture and clean core](#transitional-architecture-and-clean-core)
- [Architecture governance must approve transition debt](#architecture-governance-must-approve-transition-debt)
- [Architecture decision records for migration waves](#architecture-decision-records-for-migration-waves)
- [Measure transition complexity](#measure-transition-complexity)
- [Dual-write count](#dual-write-count)
- [Temporary-component count](#temporary-component-count)
- [Temporary-component age](#temporary-component-age)
- [Routing-exception rate](#routing-exception-rate)
- [Cross-system reconciliation coverage](#cross-system-reconciliation-coverage)
- [Wrong-system transaction rate](#wrong-system-transaction-rate)
- [Duplicate business-reference rate](#duplicate-business-reference-rate)
- [Historical-access dependency](#historical-access-dependency)
- [Decommission blockers](#decommission-blockers)
- [Change amplification](#change-amplification)
- [Support transfer rate](#support-transfer-rate)
- [Common mistakes](#common-mistakes)
- [Mistake 1: Designing only current and target states](#mistake-1-designing-only-current-and-target-states)
- [Mistake 2: Allowing both ERPs to write the same business state](#mistake-2-allowing-both-erps-to-write-the-same-business-state)
- [Mistake 3: Using record existence as proof of ownership](#mistake-3-using-record-existence-as-proof-of-ownership)
- [Mistake 4: Hiding routing rules in many integration flows](#mistake-4-hiding-routing-rules-in-many-integration-flows)
- [Mistake 5: Creating a transition facade that owns business logic](#mistake-5-creating-a-transition-facade-that-owns-business-logic)
- [Mistake 6: Converting every legacy message directly into an event](#mistake-6-converting-every-legacy-message-directly-into-an-event)
- [Mistake 7: Using replicated data without freshness limits](#mistake-7-using-replicated-data-without-freshness-limits)
- [Mistake 8: Migrating open transactions without an explicit state model](#mistake-8-migrating-open-transactions-without-an-explicit-state-model)
- [Mistake 9: Running active parallel processing without output suppression](#mistake-9-running-active-parallel-processing-without-output-suppression)
- [Mistake 10: Treating cutover as only a transport activity](#mistake-10-treating-cutover-as-only-a-transport-activity)
- [Mistake 11: Rolling back software without reconciling created transactions](#mistake-11-rolling-back-software-without-reconciling-created-transactions)
- [Mistake 12: Building temporary solutions without retirement criteria](#mistake-12-building-temporary-solutions-without-retirement-criteria)
- [Mistake 13: Leaving historical-access design until the end](#mistake-13-leaving-historical-access-design-until-the-end)
- [Mistake 14: Moving interfaces randomly](#mistake-14-moving-interfaces-randomly)
- [Mistake 15: Measuring migration by converted interface count](#mistake-15-measuring-migration-by-converted-interface-count)
- [Questions architects and managers should ask](#questions-architects-and-managers-should-ask)
- [A practical implementation sequence](#a-practical-implementation-sequence)
- [Phase 1: Define the migration units](#phase-1-define-the-migration-units)
- [Phase 2: Assign state ownership](#phase-2-assign-state-ownership)
- [Phase 3: Design stable external contracts](#phase-3-design-stable-external-contracts)
- [Phase 4: Create the migration registry](#phase-4-create-the-migration-registry)
- [Phase 5: Build identity and correlation](#phase-5-build-identity-and-correlation)
- [Phase 6: Design transition patterns](#phase-6-design-transition-patterns)
- [Phase 7: Version mappings by wave](#phase-7-version-mappings-by-wave)
- [Phase 8: Design open-transaction treatment](#phase-8-design-open-transaction-treatment)
- [Phase 9: Build cross-system observability](#phase-9-build-cross-system-observability)
- [Phase 10: Rehearse cutover and rollback](#phase-10-rehearse-cutover-and-rollback)
- [Phase 11: Operate the wave under reconciliation](#phase-11-operate-the-wave-under-reconciliation)
- [Phase 12: Decommission immediately when conditions are met](#phase-12-decommission-immediately-when-conditions-are-met)
- [The goal is controlled movement of ownership](#the-goal-is-controlled-movement-of-ownership)
- [SAP transitional integration architecture checklist](#sap-transitional-integration-architecture-checklist)
- [Sources and further reading](#sources-and-further-reading)

The target architecture looks simple.

SAP ECC will be replaced by SAP S/4HANA. Old middleware will move to SAP Integration Suite. New applications will use APIs and events. Legacy systems will gradually disappear.

The programme is approved.

Then the transition begins.

Some countries move to S/4HANA first. Others remain on ECC. Customer master data is governed centrally but maintained locally for several processes. New sales orders are created in S/4HANA, while old contracts and invoices remain in ECC. A warehouse receives transactions from both systems. The customer portal needs one order view across the old and new landscapes.

The integration architecture becomes more complex than either the old or target state.

This is normal.

The mistake is treating the transition as a short technical phase that does not need its own architecture.

Large SAP transformations rarely move all processes, countries, data and systems at once. The transitional landscape may operate for several years.

During that time, it must support:

- current business operations;
- phased process migration;
- historical data access;
- new cloud applications;
- old partner interfaces;
- changed ownership;
- cutover and rollback;
- eventual legacy decommissioning.

The objective is not only to design the future state.

It is to move from the current state to the future state without losing control of business identity, process ownership and transaction history.

SAP currently presents migration to Integration Suite as a phased journey that can proceed at the customer’s pace, supported by assessment, migration tools, prebuilt content and hybrid connectivity. SAP also emphasizes maintaining continuity for business-critical processes during modernization.

That is the correct starting assumption.

The transition architecture is not temporary documentation.

It is a production architecture with its own risks, controls and operating model.

## The transition state is usually more complex than the target state

A target-state diagram may contain:

- SAP S/4HANA;
- SAP Integration Suite;
- several strategic cloud platforms;
- managed APIs;
- business events;
- a data platform.

The transitional landscape may contain all of those plus:

- SAP ECC;
- SAP Process Orchestration or another middleware;
- legacy databases;
- old warehouse applications;
- temporary replication;
- duplicate interfaces;
- cross-system lookups;
- historical-document access;
- local workarounds.

This creates an important architectural principle:

> A simpler target state does not make the transition simple.

The programme should explicitly design:

- which systems coexist;
- which processes move first;
- where each business object is created;
- how old and new documents are distinguished;
- how users retrieve a complete view;
- how messages are routed;
- how ownership changes by wave;
- when temporary components can be removed.

Without these decisions, temporary solutions become permanent architecture.

## Target architecture and transition architecture are different deliverables

The target architecture answers:

- What should the final landscape look like?
- Which strategic platforms remain?
- Which integration patterns are preferred?
- Which systems own each business capability?

The transition architecture answers:

- What operates during each migration wave?
- How do old and new systems coexist?
- How is traffic routed?
- How is data synchronized?
- Which system may write each business object?
- How are historical transactions accessed?
- What is the cutover boundary?
- How can a migration wave be rolled back?
- What temporary dependencies are created?

A programme needs both.

A target architecture without transition states is a destination without a route.

A transition plan without a target architecture is a collection of temporary fixes.

## Start with process migration boundaries

Integration architecture should follow how business processes move.

Several migration strategies are common.

## Migration by country or legal entity

One company code or country moves to S/4HANA while others remain on ECC.

Integration routing may depend on:

- company code;
- sales organization;
- plant;
- purchasing organization;
- legal entity.

## Migration by business process

A process such as procurement moves before sales.

The same customer or material may therefore participate in transactions in both systems.

## Migration by product or business unit

One product family or division moves first.

Routing may depend on:

- product hierarchy;
- division;
- business unit;
- fulfilment model.

## Migration by transaction date

New transactions begin in S/4HANA after a cutover date.

Older documents remain in ECC until completion.

## Migration by customer or partner segment

Selected customers, suppliers or partners move first.

Each strategy creates different integration and data requirements.

The migration unit must be explicit.

Otherwise, routing rules become a growing collection of exceptions.

## Define one operational writer for each business state

The most important transitional rule is:

> One business state should have one active operational writer.

A system may replicate or display the state.

It should not update the same state independently unless a controlled multi-master design is intentional.

Consider a customer address.

During transition:

- SAP MDG may own legal identity;
- ECC may still execute legacy orders;
- S/4HANA may execute new orders;
- CRM may allow sales updates.

If several systems can change the same address, the architecture needs:

- conflict detection;
- precedence rules;
- timestamps;
- version comparison;
- correction ownership.

This becomes expensive and unreliable.

A stronger model defines:

- one owner for legal identity;
- controlled requests from other systems;
- distribution to operational consumers;
- local fields separated from central attributes.

Replication is not ownership.

A copied record should not automatically become an independent source of truth.

## Avoid dual write

Dual write means one business action attempts to update two operational systems.

For example:

1. customer portal submits an order;
2. integration creates it in ECC;
3. integration creates the same order in S/4HANA.

This may be proposed during parallel operation.

It creates serious risks.

One write may succeed and the other fail.

The systems may assign different:

- document numbers;
- prices;
- confirmations;
- blocks;
- tax results;
- statuses.

The integration layer then has to decide whether the orders are equivalent.

Dual write should not be a normal coexistence pattern.

Prefer:

- one active writer;
- shadow processing in the second system;
- replication for reporting;
- controlled migration of ownership by cutover wave.

## Dual read is usually safer than dual write

A portal may need to retrieve orders from both ECC and S/4HANA.

This is a dual-read problem.

The architecture can:

- query both systems;
- combine results in a read model;
- identify the owning source;
- route detail requests to the correct backend.

No business transaction is changed in both systems.

This is usually much safer than writing to both.

A useful transition pattern is therefore:

> Single write, federated read.

## Separate operational ownership from historical access

After a process moves to S/4HANA, users may still need old ECC data for:

- returns;
- credits;
- disputes;
- audit;
- service;
- customer questions;
- financial reconciliation.

This does not mean ECC should remain an active operational system indefinitely.

Historical access can be provided through:

- a read-only archive;
- a reporting platform;
- a federated query service;
- a dedicated historical API;
- document replication.

The architecture should distinguish:

### Operational system

Creates and changes current business transactions.

### Historical repository

Provides past data but does not own new processing.

Failing to separate these responsibilities often keeps legacy ERP systems alive because one team occasionally needs an old document.

## Use stable business identifiers across the transition

A business transaction may appear in several systems.

For example:

- external order ID;
- ECC sales order;
- S/4HANA follow-on order;
- warehouse document;
- customer portal reference.

Every transition architecture needs an identity strategy.

Useful identifiers include:

- original business request ID;
- source-system ID;
- source document number;
- target document number;
- migration wave;
- object version;
- correlation ID.

A global identifier does not always need to replace local SAP document numbers.

It needs to connect them.

Without stable correlation, the company cannot reliably:

- prevent duplicates;
- route status queries;
- reconcile transactions;
- investigate incidents;
- migrate open documents.

## Do not reuse identifiers without source context

ECC and S/4HANA may both contain sales order `50001234`.

A central application should not treat the number alone as globally unique.

Use a compound identity such as:

```text
Source system + document type + document number
```

Or assign a stable cross-system business ID.

This should be designed before integrations and data products begin combining records.

## The transition architecture needs an explicit routing model

During coexistence, inbound transactions must reach the correct operational system.

Routing may depend on:

- company code;
- sales organization;
- plant;
- business unit;
- customer;
- supplier;
- product;
- transaction date;
- migration-wave status.

The routing rule is a business-critical component.

It should not be hidden in several integration flows.

## Central routing service versus distributed routing

There are two main approaches.

### Central routing

A shared service decides which backend owns the transaction.

Advantages:

- one rule set;
- easier transition changes;
- consistent routing;
- clear monitoring.

Risks:

- central dependency;
- possible performance bottleneck;
- routing service can become another business monolith.

### Distributed routing

Each channel or integration determines the target.

Advantages:

- fewer runtime dependencies;
- local autonomy.

Risks:

- duplicated rules;
- inconsistent migration-wave status;
- difficult cutover changes;
- higher risk of wrong-system processing.

For a multi-wave transformation, a governed central routing capability is often useful.

It should remain narrow.

It should answer:

> Which system owns this transaction?

It should not also calculate price, determine supply and transform every message.

## Routing must be based on governed migration status

Do not maintain cutover routing through manually edited conditions in multiple interfaces.

Create a controlled migration registry containing, where applicable:

- organization;
- process;
- object type;
- active backend;
- cutover date;
- status;
- exception;
- owner;
- effective version.

The routing layer can use this registry.

Changes should follow approval and testing.

A wrong routing update can send production transactions to the wrong ERP.

## API facade as a transition boundary

An API facade provides a stable contract in front of one or more backends.

For example:

```text
POST /customer-orders
GET /customer-orders/{business-id}
```

During the first migration wave:

- the facade routes most orders to ECC;
- selected organizations route to S/4HANA.

Later:

- more traffic moves to S/4HANA;
- consumers keep using the same contract.

The facade can protect channels from:

- backend-specific APIs;
- SAP document types;
- migration timing;
- legacy message formats.

SAP Integration Suite currently supports APIs, application integration, events, hybrid connectivity and centralized governance across SAP and non-SAP systems.

These capabilities can support a facade pattern.

The architectural value comes from maintaining a stable business contract, not simply placing an API gateway in front of two SAP systems.

## The facade must not duplicate both ERPs

A transition facade can become dangerous when it starts owning:

- pricing;
- order validation;
- customer rules;
- availability;
- financial logic.

Those responsibilities already exist in the business domains.

The facade should normally own:

- external contract;
- target routing;
- correlation;
- result normalization;
- controlled error translation.

The backend should still own the business transaction.

## Normalize results carefully

ECC and S/4HANA may return different:

- status codes;
- error structures;
- field names;
- document states.

The facade can expose a stable external result.

For example:

- accepted;
- rejected;
- blocked;
- processing;
- completed.

But it should not hide material differences.

If one backend supports only partial functionality, the contract should expose that limitation honestly.

Normalization should reduce unnecessary backend coupling.

It should not create false equivalence.

## Anti-corruption layers protect the target model

A legacy system may expose structures that should not become part of the future architecture.

An anti-corruption layer translates between:

- legacy model;
- future domain model.

Its responsibilities may include:

- code conversion;
- structural transformation;
- legacy status interpretation;
- identifier translation;
- old error normalization;
- protocol adaptation.

The purpose is not only to connect systems.

It is to stop historical implementation decisions from contaminating the target model.

## A good anti-corruption layer has an exit plan

For each temporary translation, record:

- why it exists;
- legacy dependency;
- future replacement;
- affected consumers;
- owner;
- retirement condition.

Otherwise, the anti-corruption layer becomes a permanent translation platform containing the logic of both worlds.

## Event bridge for old and new landscapes

A transformation may introduce business events while ECC continues using IDocs or other messages.

An event bridge can:

1. receive a committed legacy message;
2. translate it into a governed business event;
3. publish it for new consumers.

For example:

```text
Legacy customer IDoc
→ BusinessPartner.AddressChanged event
```

This allows new consumers to use a stable event contract without waiting for the legacy source to become fully event native.

## Do not turn every legacy message into an event

An IDoc may contain:

- complete object snapshot;
- technical processing details;
- several unrelated changes.

A useful business event should represent a meaningful state transition.

The bridge must determine:

- which business fact occurred;
- whether the source transaction committed;
- which object version applies;
- whether the event can be duplicated;
- how corrections are represented.

A mechanical IDoc-to-JSON conversion is not an event architecture.

## Outbound event publication needs completeness checks

A legacy transaction may commit successfully while event publication fails.

The architecture should be able to identify:

- source transactions requiring events;
- events created;
- events published;
- events waiting for retry.

Otherwise, new consumers can silently miss business changes.

## Replication should have a declared purpose

During transformation, data is frequently replicated between ECC and S/4HANA.

Before creating replication, state why it is required.

Common purposes include:

- operational dependency;
- temporary lookup;
- reporting;
- migration validation;
- downstream compatibility;
- historical access.

Each purpose needs a different design.

## Operational replication

A target requires current data to execute business transactions.

Requirements may include:

- low latency;
- target readiness;
- error correction;
- business ownership.

## Reporting replication

Data is copied for analytics.

It does not become operational truth.

## Validation replication

Data is compared between old and new systems during testing or shadow operation.

## Historical replication

Old data is copied to reduce dependency on the legacy system.

The architecture should not use one general replication stream for all purposes without defining consumer expectations.

## Replicated data needs staleness rules

A copied value may be:

- seconds old;
- hours old;
- one day old.

The acceptable delay depends on usage.

For example:

- customer name for reporting may tolerate delay;
- credit block for order release may not;
- warehouse stock may become outdated quickly;
- legal identity may change rarely but require strong control.

Every replicated dataset should state:

- source;
- refresh model;
- maximum expected delay;
- allowed operational use;
- reconciliation;
- failure behaviour.

## Do not use replicated copies for decisions they cannot safely support

A local copy can improve performance and resilience.

It can also produce decisions based on stale information.

Before using replicated data, ask:

- What happens if the copy is old?
- Can the user proceed?
- Must the system validate against the source?
- Can a temporary fallback be used?
- How is staleness visible?

The architecture should not present a copied value as current truth without a defined freshness guarantee.

## Mapping must be versioned by migration wave

During transition, one source value may map differently depending on:

- target system;
- target release;
- country migration wave;
- effective date;
- partner version.

For example:

```text
ECC order type ZOR1
→ S/4HANA order type OR
```

This mapping may apply only after a specific cutover date.

The mapping registry should contain:

- source representation;
- target representation;
- business meaning;
- effective period;
- migration scope;
- owner;
- version;
- affected interfaces.

Do not overwrite the old mapping immediately.

Historical transactions and rollback may still require it.

## Mapping changes and cutover changes are linked

A migration wave may change:

- system routing;
- organizational mapping;
- document types;
- customer identifiers;
- product identifiers;
- error codes.

These changes should be deployed and activated as one controlled cutover package.

If routing changes before mapping is ready, transactions fail.

If mapping changes early, old-system transactions may be transformed incorrectly.

## Open transactions are harder than master data

Master data can often be loaded before cutover and reconciled.

Open transactions contain process state.

Examples include:

- sales orders;
- purchase orders;
- deliveries;
- invoices;
- production orders;
- workflow requests.

An open transaction may have:

- completed and incomplete items;
- references to previous documents;
- reservations;
- pricing state;
- external-system status;
- follow-on documents.

The migration architecture must decide whether open transactions:

- remain and finish in ECC;
- move completely to S/4HANA;
- split by document state;
- receive a reference copy only;
- trigger new follow-on transactions in S/4HANA.

There is no universal answer.

## Finish in old system

Advantages:

- preserves document history;
- lower migration complexity;
- existing integrations continue.

Risks:

- longer ECC coexistence;
- new and old documents appear in different systems;
- cross-system reporting required.

## Migrate open transactions

Advantages:

- faster operational move to S/4HANA;
- earlier legacy reduction.

Risks:

- complex state conversion;
- document-flow reconciliation;
- duplicate or missing follow-on processing;
- larger cutover.

## Reference and continue

An old document remains in ECC, but a new S/4HANA transaction continues the process.

This requires:

- stable cross-reference;
- clear ownership transfer;
- customer and financial explanation;
- cross-system document flow.

The architecture should make the chosen model visible to integrations and users.

## Process ownership may move at a different time from data

Customer master data may be loaded into S/4HANA months before sales-order creation moves there.

The presence of a record does not mean the new system owns the process.

Similarly, historical orders may be copied to S/4HANA for viewing without becoming operational documents.

The architecture must distinguish:

- data present;
- data authoritative;
- process active;
- write permitted.

These should not be inferred from simple technical existence.

## Shadow processing is safer than active dual processing

Shadow processing allows the new system or integration to process a copy without creating the final production effect.

For example:

1. customer order is created in ECC;
2. the same input is sent to an S/4HANA test or shadow path;
3. the programme compares:
 - pricing;
 - determination;
 - availability;
 - errors;
 - expected document result.

This helps find differences before ownership moves.

## Shadow processing does not prove everything

It may not fully test:

- production locks;
- real number ranges;
- downstream warehouse execution;
- financial postings;
- high-volume performance;
- physical processes.

Shadow output is evidence.

It is not complete production validation.

## Active parallel run requires strict boundaries

Some processes require a period of active parallel operation.

For financial or regulated processes, old and new systems may both calculate results for comparison.

Only one should normally produce the authoritative business effect.

For example:

- both systems calculate an invoice;
- only the designated system sends it to the customer and posts the receivable.

The architecture should define:

- authoritative output;
- comparison output;
- suppression controls;
- variance thresholds;
- owner;
- stop conditions.

A parallel run without output suppression can create duplicate business transactions.

## Design cutover as an architectural state change

Cutover is not only a technical deployment.

It changes:

- system authority;
- routing;
- mappings;
- user access;
- event publishers;
- monitoring;
- support ownership.

The cutover plan should therefore include an architecture activation sequence.

For example:

1. stop new transactions in the old system;
2. record the final transaction boundary;
3. drain or freeze outbound queues;
4. reconcile in-flight messages;
5. activate new mappings;
6. change target routing;
7. enable S/4HANA write access;
8. enable new event publication;
9. execute business validation;
10. keep the old system read-only.

The exact sequence will differ.

It must be designed end to end.

## Define the cutover boundary

A boundary can use:

- timestamp;
- document number;
- company code;
- business unit;
- file sequence;
- migration-wave identifier.

The boundary must answer:

> Which system owns a transaction created at this moment?

Ambiguous boundaries create duplicate or lost transactions.

## Time alone may not be enough

Systems may use:

- different time zones;
- delayed files;
- asynchronous queues;
- offline partner processing.

A transaction created before the cutover time may arrive afterward.

The architecture should define whether ownership depends on:

- source creation time;
- message arrival time;
- business effective date;
- accepted migration-wave status.

This should be tested with delayed and replayed transactions.

## In-flight messages need explicit treatment

At cutover, messages may be:

- created but not sent;
- sent but not acknowledged;
- received but not processed;
- failed and waiting for retry;
- partially processed;
- manually corrected.

For each category, decide:

- finish through old route;
- convert to new route;
- cancel and recreate;
- reconcile manually.

Do not simply restart all failed messages after cutover.

Some may create duplicate business effects in the new system.

## Rollback must restore authority, not only software

A technical rollback can restore:

- old integration version;
- old routing configuration;
- previous mapping.

But business transactions may already have been created in S/4HANA.

Rollback planning must consider:

- new documents;
- external confirmations;
- warehouse actions;
- customer messages;
- financial postings;
- event consumption;
- number sequences.

The architecture should define a rollback point after which full rollback is no longer safe.

After that point, a controlled forward correction may be the only realistic option.

## Feature toggles help, but they do not reverse business state

A routing toggle can send new transactions back to ECC.

It does not remove transactions already created in S/4HANA.

A toggle controls future traffic.

Recovery still requires reconciliation of completed and partially completed transactions.

## Transitional observability needs a cross-system view

During coexistence, support teams cannot rely on one system’s monitor.

A business transaction may pass through:

- channel;
- API facade;
- old middleware;
- Integration Suite;
- ECC or S/4HANA;
- warehouse;
- partner.

The operations view should show:

- business request;
- routing decision;
- source system;
- target system;
- integration status;
- SAP document;
- downstream completion;
- current owner.

SAP Integration Suite currently emphasizes centralized governance, monitoring and security across APIs, events, application integrations and partner connections.

That platform visibility should be combined with business-level correlation and reconciliation.

## Record the routing decision

For every important transaction, retain:

- routing-rule version;
- migration status used;
- selected target;
- timestamp;
- correlation ID.

This helps explain why one transaction entered ECC and another entered S/4HANA.

Without this, incidents become arguments about what the routing configuration probably contained at the time.

## Reconciliation should be wave-specific

For each migration wave, reconcile:

- source requests;
- routed requests;
- old-system documents;
- new-system documents;
- failed transactions;
- duplicates;
- downstream outcomes.

Example:

```text
12,400 customer orders received
10,100 routed to ECC
2,300 routed to S/4HANA
12,398 orders created
2 orders in controlled exception
0 duplicate business references
```

This proves transition control.

A middleware dashboard alone cannot provide it.

## Build a transition control plane

A practical transition architecture needs a governed control layer containing:

- migration registry;
- routing rules;
- mapping versions;
- interface versions;
- system authority;
- cutover state;
- temporary exceptions;
- decommission dates.

This is not necessarily one new application.

It can be implemented through several controlled repositories and services.

The important point is that transition decisions are explicit and searchable.

## Temporary architecture needs owners and expiry dates

Every temporary component should record:

- purpose;
- business owner;
- technical owner;
- migration waves using it;
- operating cost;
- retirement condition;
- target retirement date.

Examples include:

- ECC-to-S/4 replication;
- dual-read service;
- legacy API facade;
- temporary mapping table;
- event bridge;
- historical-document proxy.

Temporary does not mean unmanaged.

## Treat temporary components as production software

A bridge expected to operate for two years needs:

- testing;
- security;
- monitoring;
- support;
- capacity;
- documentation;
- release management.

Underengineering it because it is “temporary” creates production risk.

Overengineering it without an exit condition creates permanent cost.

## Decommissioning is part of architecture

The architecture is not complete until it explains how legacy components disappear.

For every old interface or runtime, define:

- replacement;
- remaining consumers;
- historical dependencies;
- data-retention requirement;
- final reconciliation;
- shutdown approval.

SAP’s current Integration Suite migration guidance includes assessment and migration tooling intended to support planning and reduce migration risk and cost.

Assessment should not stop after conversion planning.

It should also identify what can be retired.

## Do not keep ECC because one interface still uses it

A small legacy dependency can prevent large infrastructure reduction.

Examples include:

- one historical-order lookup;
- one partner file;
- one tax report;
- one old warehouse message.

The programme should identify these dependencies early.

Possible solutions include:

- archive API;
- partner adapter;
- historical data store;
- replacement report;
- bounded legacy service.

Leaving them until the end makes decommissioning expensive and politically difficult.

## A reference transitional architecture

A practical logical model can look like this:

```text
Channels, Partners and New Applications
                    |
            Stable Business Contracts
        APIs | Commands | Events | B2B
                    |
         Transition Routing and Facades
    Target selection | Identity | Correlation
                    |
       Process Coordination Where Required
                    |
       Integration Execution and Translation
  Integration Suite | Legacy Middleware | Bridges
                    |
        ---------------------------------
        |                               |
      SAP ECC                       SAP S/4HANA
   Legacy processes                Migrated processes
        |                               |
        ---------------------------------
                    |
       Warehouses, Banks and Partners
```

Cross-cutting controls:

```text
Migration registry
Mapping versions
Business identity
Observability
Reconciliation
Security
Cutover control
Decommission lifecycle
```

The central transition layer should remain narrow.

It handles coexistence.

It should not become the permanent owner of sales, procurement, finance or master data.

## Example: phased order-to-cash migration

Consider a company moving sales organizations to S/4HANA in waves.

## Current state

- all orders created in ECC;
- warehouse receives IDocs;
- customer portal reads ECC;
- billing and finance operate in ECC.

## Wave 1

Sales organization 1000 moves to S/4HANA.

Other organizations stay in ECC.

## Inbound order architecture

The channel calls one stable order API.

The transition router checks:

- sales organization;
- migration status;
- effective date.

It routes the order to:

- S/4HANA for organization 1000;
- ECC for all others.

## Business identity

The channel provides one external order ID.

The facade returns:

- external ID;
- owning ERP;
- SAP order number;
- processing status.

## Order status

The customer portal calls one order-status API.

The facade retrieves the order from its owning system.

## Warehouse integration

The internal warehouse contract remains stable.

Adapters translate:

- ECC IDoc to warehouse message;
- S/4HANA API or event to the same warehouse contract.

The warehouse does not need to understand the ERP migration.

## Billing

Orders remain billed in the system where they were created unless an explicitly designed cross-system process exists.

## Reconciliation

The company compares:

- accepted channel orders;
- routing decisions;
- ERP orders;
- warehouse requests;
- invoices.

## Later waves

More sales organizations move by changing the governed migration registry.

The channel and warehouse contracts remain stable.

## Final state

All active order processing moves to S/4HANA.

The ECC adapter and routing branch are removed.

Historical orders remain available through a read-only service.

This is a controlled strangler pattern.

## Example: supplier master data during coexistence

Suppose SAP MDG governs suppliers centrally.

ECC and S/4HANA both require supplier data during transition.

## Central ownership

MDG owns:

- legal identity;
- approved central attributes;
- duplicate decision;
- governance status.

## Target ownership

ECC and S/4HANA own local operational extensions required by their active processes.

## Distribution

An approved supplier event or governed distribution process sends central data to both systems.

## Readiness

Each target reports:

- technical receipt;
- local validation;
- organizational extension;
- operational readiness.

## Transition rule

A supplier may exist in both systems.

But purchasing transactions are created only in the system owning the relevant purchasing organization.

## Decommission

When the last purchasing organization leaves ECC:

- ECC supplier updates stop;
- historical supplier records remain read only;
- ECC distribution is retired.

This avoids treating record presence as process ownership.

## Example: warehouse coexistence

A warehouse may receive fulfilment requests from both ECC and S/4HANA.

The warehouse should not need two completely different business models.

Create a stable warehouse command containing:

- source document identity;
- fulfilment location;
- products;
- quantities;
- dates;
- service requirements.

Adapters handle ERP-specific representations.

Warehouse responses use:

- stable external reference;
- source-system context;
- warehouse execution state.

This isolates the warehouse from ERP migration waves.

## Transitional architecture and clean core

A transition often creates pressure to add custom compatibility logic directly inside S/4HANA.

Examples include:

- legacy fields;
- old status values;
- copied ECC determination;
- custom interfaces shaped like old structures.

Some compatibility is unavoidable.

But the target core should not permanently reproduce every historical interface contract.

Use external facades and anti-corruption layers where they protect the future model.

SAP currently describes Integration Suite as supporting hybrid integration and cleaner core integration through governed APIs, events and reusable integration capabilities across SAP and third-party systems.

The practical objective is not zero compatibility logic.

It is keeping temporary compatibility from becoming permanent S/4HANA design.

## Architecture governance must approve transition debt

A temporary component is a form of transition debt.

It may be justified.

The programme should record:

- reason;
- cost;
- risk;
- exit condition;
- owner.

Examples include:

- temporary dual-read API;
- replicated customer table;
- ECC event bridge;
- legacy code mapping;
- old partner format.

This prevents the target architecture from slowly absorbing every temporary exception.

## Architecture decision records for migration waves

Important decisions should be written down.

For example:

**Decision:** Open sales orders will finish in ECC
**Reason:** Migrating document flow and fulfilment state creates excessive risk
**Consequence:** Customer portal requires dual-read capability until the final open order closes
**Retirement condition:** No operational ECC sales orders remain
**Owner:** Order-to-cash process owner

Another example:

**Decision:** Supplier identity is distributed to both ERPs, but purchasing ownership follows purchasing organization
**Reason:** Both landscapes require supplier visibility during coexistence
**Control:** One active transaction owner per purchasing organization
**Retirement condition:** Final purchasing organization migrates from ECC

These records preserve reasoning when project teams change.

## Measure transition complexity

Useful architecture metrics include:

## Dual-write count

How many business processes update the same state in two systems?

The target should normally be zero or tightly limited.

## Temporary-component count

How many facades, bridges, replications and routing exceptions exist?

## Temporary-component age

How long have supposedly temporary components operated?

## Routing-exception rate

How many transactions require manual or exceptional target selection?

## Cross-system reconciliation coverage

Which coexistence flows have complete business-level reconciliation?

## Wrong-system transaction rate

How often is a transaction created in the incorrect ERP?

## Duplicate business-reference rate

How often does the same request create more than one operational document?

## Historical-access dependency

Which users and interfaces still require the old ERP for read-only information?

## Decommission blockers

How many remaining dependencies prevent legacy shutdown?

## Change amplification

How many transition components must change for each migration wave?

## Support transfer rate

How often does a transition incident move between ECC, S/4HANA and integration teams before ownership is found?

## Common mistakes

## Mistake 1: Designing only current and target states

The multi-year coexistence landscape remains undefined.

## Mistake 2: Allowing both ERPs to write the same business state

Conflicts become an integration problem.

## Mistake 3: Using record existence as proof of ownership

A replicated object does not automatically own the process.

## Mistake 4: Hiding routing rules in many integration flows

Cutover changes become inconsistent and difficult to audit.

## Mistake 5: Creating a transition facade that owns business logic

The facade becomes another ERP layer.

## Mistake 6: Converting every legacy message directly into an event

Technical messages are not automatically business facts.

## Mistake 7: Using replicated data without freshness limits

Operational decisions rely on stale copies.

## Mistake 8: Migrating open transactions without an explicit state model

Document flow and follow-on processing become inconsistent.

## Mistake 9: Running active parallel processing without output suppression

Duplicate orders, invoices or postings are created.

## Mistake 10: Treating cutover as only a transport activity

Authority, routing, mappings and support ownership also change.

## Mistake 11: Rolling back software without reconciling created transactions

The old path repeats business effects.

## Mistake 12: Building temporary solutions without retirement criteria

The transitional architecture becomes the permanent architecture.

## Mistake 13: Leaving historical-access design until the end

ECC cannot be shut down because users still need old documents.

## Mistake 14: Moving interfaces randomly

Related domains and mappings remain split across platforms.

## Mistake 15: Measuring migration by converted interface count

The programme may move technical objects without reducing operational complexity.

## Questions architects and managers should ask

1. How long will ECC and S/4HANA coexist?
2. What is the migration unit: country, process, product or date?
3. Which system writes each business state during every wave?
4. Where is dual write occurring?
5. How are inbound transactions routed?
6. Where is migration status governed?
7. Can channels use stable contracts across both ERPs?
8. How are business identifiers correlated?
9. Which data is replicated, and for what purpose?
10. How stale may replicated data become?
11. How will open transactions be handled?
12. Which system completes follow-on processing?
13. What happens to delayed messages after cutover?
14. What is the exact cutover boundary?
15. How is rollback limited after business effects occur?
16. Which components are temporary?
17. What conditions remove each temporary component?
18. How will users access historical transactions?
19. Which dependencies still block ECC decommissioning?
20. Is the transition architecture moving toward the target, or becoming a second target?

## A practical implementation sequence

## Phase 1: Define the migration units

Identify the organizations, processes and objects moving in each wave.

## Phase 2: Assign state ownership

For every important business state, define one active operational writer.

## Phase 3: Design stable external contracts

Protect channels and partners from backend migration details.

## Phase 4: Create the migration registry

Govern routing, ownership and effective dates centrally.

## Phase 5: Build identity and correlation

Connect old, new and external document identifiers.

## Phase 6: Design transition patterns

Select where to use:

- facade;
- anti-corruption layer;
- event bridge;
- replication;
- dual read;
- shadow processing;
- orchestration.

## Phase 7: Version mappings by wave

Do not overwrite rules needed by old transactions and rollback.

## Phase 8: Design open-transaction treatment

Decide what finishes in ECC and what moves.

## Phase 9: Build cross-system observability

Track routing, processing and business completion.

## Phase 10: Rehearse cutover and rollback

Test delayed messages, duplicates, in-flight transactions and partial completion.

## Phase 11: Operate the wave under reconciliation

Prove transaction completeness before closing stabilization.

## Phase 12: Decommission immediately when conditions are met

Do not leave unused bridges and routes active for convenience.

## The goal is controlled movement of ownership

An S/4HANA transformation is not complete when the new system is technically available.

It is complete when business responsibility has moved safely from the old landscape to the new one.

That movement includes:

- transaction ownership;
- data authority;
- integrations;
- monitoring;
- support;
- historical access;
- recovery.

SAP currently offers a broad integration platform covering cloud and hybrid application integration, APIs, events, B2B connections, governance and monitoring. It also provides assessment and migration support for organizations moving from legacy integration platforms.

Those capabilities can support the journey.

They do not decide how business authority should move.

That remains an architecture responsibility.

The strongest transition architecture does not try to make ECC and S/4HANA behave as one large distributed ERP.

It defines clear boundaries:

- which system owns which transaction;
- which data is copied;
- which data is authoritative;
- which contracts remain stable;
- which temporary components exist;
- when each temporary dependency disappears.

A transition architecture is successful when every migration wave reduces the role of the old landscape.

If every wave adds another bridge, another replication and another routing exception without removing anything, the programme is not approaching the target state.

It is constructing a more expensive coexistence state.

---

## SAP transitional integration architecture checklist

- [ ] Current, transition and target architectures are documented separately.
- [ ] Migration units and waves are explicit.
- [ ] Every important business state has one operational writer.
- [ ] Dual write is avoided or tightly controlled.
- [ ] Dual read does not imply dual ownership.
- [ ] Historical access is separated from operational processing.
- [ ] Cross-system business identifiers are stable.
- [ ] Routing rules use a governed migration registry.
- [ ] Routing decisions are logged with rule versions.
- [ ] External channels use stable business contracts.
- [ ] Facades do not duplicate ERP business logic.
- [ ] Anti-corruption layers protect the future domain model.
- [ ] Temporary layers have retirement conditions.
- [ ] Legacy messages are converted into business events only where semantics are clear.
- [ ] Replication has a declared purpose and freshness limit.
- [ ] Replicated copies are not used outside their approved purpose.
- [ ] Mappings are versioned by system, wave and effective date.
- [ ] Open-transaction treatment is designed by process.
- [ ] Record presence and process ownership are not confused.
- [ ] Shadow processing is preferred to uncontrolled dual execution.
- [ ] Parallel runs suppress duplicate business effects.
- [ ] Cutover changes authority, routing, mappings and monitoring as one package.
- [ ] In-flight messages have an explicit cutover decision.
- [ ] Rollback covers business transactions, not only technical deployment.
- [ ] Cross-system observability follows the business transaction.
- [ ] Every migration wave includes business reconciliation.
- [ ] Temporary components are treated as production services.
- [ ] Decommission dependencies are identified early.
- [ ] Each wave removes old capability rather than only adding new capability.
- [ ] Success is measured through transfer of ownership and legacy reduction.

## Sources and further reading

SAP currently positions SAP Integration Suite as a secure integration platform connecting applications, data, APIs, events, business partners and AI agents across SAP and third-party cloud, on-premises and hybrid landscapes. The platform includes centralized governance, monitoring, security and prebuilt integration capabilities.

SAP’s current migration guidance for moving from SAP Process Orchestration to SAP Integration Suite describes modernization as a phased journey that can proceed at the customer’s pace. SAP lists assessment, migration-automation tools, partner services, testing support and reuse of existing integration content among the available migration resources.

SAP currently presents Integration Assessment and the SAP Integration Solution Advisory Methodology as structured capabilities for documenting requirements, evaluating integration landscapes, applying reference architectures and embedding integration governance and development standards.

SAP Cloud Integration currently supports application-to-application, business-to-business and business-to-government integration across SAP and third-party systems, including mappings, prebuilt content and hybrid execution options.

*Reviewed: July 2026. SAP Integration Suite capabilities, migration tools, packaging and supported deployment options can change. Transitional architecture decisions should be validated against the actual migration scope, SAP releases, business-process ownership and cutover constraints.*

## Continue exploring

- [Modern SAP Integrations: How to Choose Between APIs, Events, Files, Queues, and Mapping Strategies](/blog/modern-sap-integrations-how-to-choose-between-apis-events-files-queues/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [How to Design a Modern SAP Integration Architecture Without Creating a New Middleware Monolith](/blog/how-to-design-a-modern-sap-integration-architecture-without-creating-a/)
- Next in the migration: [Centralized or Federated SAP Integration Architecture: How to Divide Ownership Without Creating Chaos](/blog/centralized-or-federated-sap-integration-architecture-how-to-divide/)
