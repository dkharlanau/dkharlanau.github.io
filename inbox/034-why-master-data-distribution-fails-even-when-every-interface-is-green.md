# Why Master Data Distribution Fails Even When Every Interface Is Green

A supplier is created in a central system.

The record is distributed successfully to SAP S/4HANA, a procurement platform, a warehouse application and a data platform.

Every interface is green.

Yet the supplier still cannot be used.

In SAP, the supplier is missing the required purchasing organization.

The procurement platform contains a different payment term.

The warehouse created a second supplier because it could not match the identifier.

The data platform merged the supplier with another legal entity because the names were similar.

An AI agent later retrieves all four records and presents one confident but incorrect answer.

Nothing failed technically.

The architecture failed to establish:

- which system owns supplier identity;
- which attributes are centrally governed;
- which attributes are local;
- which identifier connects the records;
- what “supplier ready” actually means;
- which system an application or agent should trust.

This is the core problem of master data distribution.

Companies often approach it as an integration problem:

> We need to synchronize customers, suppliers and materials between systems.

But synchronization is only the movement of data.

It does not decide:

- which value is correct;
- who may change it;
- which local variation is permitted;
- when a record becomes operationally usable;
- how conflicts are resolved;
- whether a consumer is reading an authoritative value or a delayed copy.

SAP currently distinguishes these responsibilities clearly. SAP describes Master Data Governance as a governance layer that creates governed records, supports matching and consolidation, applies data-quality rules, uses workflows and preserves an audit trail. SAP also states that master data integration distributes master data in its current state and does not itself improve its quality.

That distinction should define the architecture:

> Governance determines trusted meaning. Integration distributes it. Operational applications use and extend it within controlled boundaries.

When these responsibilities are mixed, the integration platform becomes a conflict-resolution engine, cloud applications become accidental master systems and AI agents consume whichever copy is easiest to access.

### “Single source of truth” is usually too vague

Organizations often declare:

> SAP is the single source of truth for customer data.

The statement sounds decisive.

It usually becomes unclear as soon as individual attributes are examined.

For a customer, different responsibilities may exist:

- legal name owned by central business-partner governance;
- marketing consent owned by the marketing platform;
- credit status owned by finance;
- sales-area data owned by sales operations;
- service entitlement owned by the service platform;
- delivery instructions owned by the fulfilment process;
- local tax attributes owned by a country organization.

All these attributes may appear inside one object called “customer.”

One application is rarely authoritative for every meaning.

A stronger architecture does not ask only:

> Which system owns the customer?

It asks:

> Which domain owns each business meaning, decision and lifecycle?

The result may still include one central golden record.

But it will not pretend that every local operational field belongs to one central application.

### Replace “one source” with “one authority”

The architecture should aim for:

> One accountable authority for every governed business fact.

That authority may be:

- a central master data domain;
- finance;
- sales;
- procurement;
- product management;
- human resources;
- a local legal entity;
- an external authoritative provider.

There may be many copies.

There should not be many independent authorities for the same fact.

This distinction matters.

A customer address may be replicated into ten systems.

That does not create ten equally valid versions.

One system remains authoritative for the governed address.

Other systems are:

- consumers;
- operational projections;
- caches;
- local extensions;
- historical stores.

### Record presence does not prove ownership

A business partner may exist in:

- SAP MDG;
- SAP S/4HANA;
- SAP Sales Cloud;
- SAP Ariba;
- a warehouse system;
- a data platform.

The record’s presence in each system does not mean each system owns it.

A target may require the record so that it can execute its own transactions.

That target may still have no authority to redefine the centrally governed identity.

The architecture should distinguish several roles.

### Authoring system

Where a change request begins.

For example:

- supplier requests a change through a portal;
- sales employee proposes a customer address;
- product manager creates a material request.

The authoring system is not automatically authoritative.

### Governance system

Where the change is:

- validated;
- matched;
- reviewed;
- approved;
- audited.

SAP currently positions SAP Master Data Governance as providing governed models, matching and merging, data-quality monitoring, collaborative workflows and auditable changes across SAP and third-party data.

### Authoritative system

Where the approved business fact becomes the accepted reference.

This may be the governance hub itself or an operational system receiving the approved result.

### Distribution layer

Moves approved changes through:

- APIs;
- events;
- messages;
- files;
- integration services.

It should not silently redefine the governed meaning.

### Operational consumer

Uses the master record to execute processes.

It may add local operational data.

### Analytical consumer

Uses a copy for reporting, analytics or AI.

It should not become operational authority merely because it provides convenient access.

## Master data governance and master data integration are different capabilities

This distinction must remain visible in the architecture.

### Governance answers

- Who may propose a change?
- Which validations apply?
- Is the record a duplicate?
- Which value survives a conflict?
- Who approves the result?
- When does the change become effective?
- What is the audit trail?

### Integration answers

- Which consumers need the record?
- Which contract is used?
- How quickly must it arrive?
- How are identifiers mapped?
- What happens when a target is unavailable?
- How is delivery retried?
- How is target processing reconciled?

### Operational readiness answers

- Can the target actually use the record?
- Are local organizational extensions complete?
- Are mandatory local attributes present?
- Is the record blocked?
- Are all dependencies available?

These are three separate results.

A centrally approved supplier may still not be operationally ready in a purchasing system.

A delivered customer record may still be unusable for sales-order creation.

A technically successful replication does not prove process readiness.

## The integration layer should not repair governance silently

Suppose the central supplier record lacks a payment term.

The integration flow sets a default value so that SAP accepts the record.

The target is created successfully.

The central system still contains no payment term.

Another target applies a different default.

The company now has several values and no visible decision.

The integration prevented a technical error by creating a data-governance defect.

Defaults may occasionally be necessary.

They should be:

- approved;
- visible;
- limited to a defined scope;
- recorded;
- monitored;
- eventually removed or corrected at the source.

The integration layer should not hide missing governance by manufacturing plausible data.

### Distribution should preserve uncertainty

If the source value is missing or unresolved, the architecture should decide deliberately whether to:

- reject distribution;
- create an incomplete target record;
- route a local completion task;
- apply a controlled fallback;
- block operational use.

The consumer should know whether a value is:

- governed;
- locally maintained;
- derived;
- defaulted;
- unknown.

Without this distinction, every populated field appears equally trustworthy.

## Ownership should be defined at the attribute and decision level

Object-level ownership is often too coarse.

A useful ownership matrix may look like this:

| Customer information | Owner | Authoritative capability |
|---|---|---|
| Legal identity | Customer governance | Approved business-partner identity |
| Sales classification | Sales domain | Customer segmentation policy |
| Credit limit | Credit management | Credit-risk decision |
| Delivery address | Customer governance or fulfilment | Approved ship-to location |
| Marketing consent | Marketing domain | Consent management |
| Payment terms | Finance or sales policy | Commercial-account rule |
| Local tax data | Local finance | Country compliance |
| Portal display name | Channel domain | Customer-facing presentation |

The exact model differs by organization.

The principle does not:

> The team that understands and is accountable for the business meaning should own it.

### Ownership includes obligations

A data owner should not be only a name in a governance spreadsheet.

Ownership should include responsibility for:

- definition;
- quality requirements;
- permitted values;
- validation;
- security;
- lifecycle;
- exception decisions;
- funding improvements.

A steward may operate the daily process.

The owner remains accountable for the standard.

## Central governance does not require central maintenance of every field

A global company may govern:

- legal identity;
- global identifiers;
- duplicate decisions;
- global classifications.

Local organizations may maintain:

- company-code data;
- purchasing organization;
- sales area;
- local tax fields;
- language-dependent descriptions;
- regulatory attributes.

Trying to centralize every local field creates:

- large workflows;
- slow onboarding;
- central bottlenecks;
- excessive optional attributes;
- weak local accountability.

A practical architecture often uses:

> Centrally governed identity with federated operational extensions.

### Central attributes

Should be globally consistent.

Examples:

- legal name;
- registration identifier;
- central status;
- global product identity;
- base unit;
- central hierarchy.

### Local extensions

Exist because a specific system, company or process needs them.

Examples:

- purchasing organization;
- sales area;
- plant status;
- local tax category;
- payment method;
- regional product description.

Local extension does not mean uncontrolled local change.

The ownership and validation should still be explicit.

## A golden record is not the same as one giant record

SAP currently describes SAP Master Data Governance as supporting a golden record for domains while preserving semantics and relationships, and allowing teams to own unique attributes through workflow and validation.

This should not be interpreted as:

> Put every field from every system into one enormous central object.

A useful golden record contains the governed meaning required across the enterprise.

It may link to local extensions rather than absorb them all.

Otherwise, the golden record becomes:

- too large;
- filled with optional fields;
- difficult to approve;
- slow to change;
- dependent on every target system.

The purpose of the golden record is trusted identity and meaning.

It should not become a replica of the entire application landscape.

## Identity is the foundation of distribution

Before distributing attributes, the company must know which records represent the same business entity.

This is harder than it appears.

One supplier may have:

- central business-partner ID;
- legacy ECC vendor number;
- S/4HANA business-partner number;
- procurement-network ID;
- warehouse supplier code;
- external legal registration number;
- local accounting code.

These identifiers serve different purposes.

The architecture needs to distinguish:

### Global identity

Represents the business entity across the landscape.

### System identity

Represents the record inside one application.

### Business-role identity

Represents the entity in a specific role.

For example:

- customer;
- supplier;
- payer;
- ship-to party;
- carrier.

### External identity

Represents the entity in a partner or authority system.

### Transactional reference

Connects the master entity to one transaction.

### Do not use names as identity

Names can change.

Names may be:

- translated;
- abbreviated;
- duplicated;
- entered differently;
- shared by related legal entities.

A company name can help matching.

It should not be the durable identity key.

### Legal identifiers are not always globally sufficient

Registration and tax identifiers are important.

But:

- one entity may have several identifiers;
- identifiers may be country-specific;
- branches may share or differ;
- identifiers may change after restructuring;
- some objects do not have legal identifiers.

Use governed key mapping rather than assuming one external field solves identity universally.

## Key mapping is business-critical master data

A key-mapping record connects:

```text id="q4igc9"
Central business partner BP-1000456
→ ECC vendor 300271
→ S/4HANA business partner 1000456
→ Procurement platform supplier SUP-7789
```

This mapping is not merely an integration detail.

It affects:

- duplicate prevention;
- transaction routing;
- reconciliation;
- historical continuity;
- AI retrieval.

Key mappings need:

- owner;
- source and target context;
- effective period;
- status;
- audit;
- merge and split handling.

### Merges require careful propagation

Two records may be identified as duplicates.

The organization decides that supplier B should merge into supplier A.

Downstream systems may already contain transactions for both.

The architecture should decide:

- which identity survives;
- whether historical references remain;
- which systems can change keys;
- whether inactive aliases remain searchable;
- how future transactions are routed;
- how AI and analytics interpret history.

A merge is not just deleting one record.

### Splits are even harder

One master record may later be separated into two entities.

Possible reasons include:

- corporate restructuring;
- legal separation;
- incorrect historical matching;
- different business roles.

The architecture needs effective dates and transaction boundaries.

Historical documents should not be rewritten casually.

## Define the master data lifecycle as states

Master data should not be treated as simply existing or not existing.

A useful lifecycle may include:

```text id="s3hipd"
REQUESTED
→ VALIDATING
→ MATCH_REVIEW
→ APPROVED
→ ACTIVE
→ DISTRIBUTING
→ PARTIALLY_READY
→ OPERATIONALLY_READY
→ BLOCKED
→ RETIRED
```

Different domains may use different states.

The distinction between approval and readiness is especially important.

### Approved

The governed record has passed the central process.

### Distributed

The record has been sent to the relevant target.

### Created

The target has created a local record.

### Extended

Required organizational data has been added.

### Operationally ready

The intended business transaction can be executed.

A supplier may be centrally approved but not ready for purchasing.

A product may exist but be blocked for a plant.

A customer may exist but lack sales-area data.

## Readiness should be defined by the consuming process

“Customer ready” has no universal meaning.

A customer may be ready for:

- marketing;
- quotation;
- sales order;
- delivery;
- billing;
- credit sale.

Each requires different data.

Likewise, a material may be ready for:

- procurement;
- sales;
- production;
- warehousing;
- costing.

Define readiness by capability.

For example:

> Supplier is purchasing-ready for purchasing organization 1000 when central identity is approved, purchasing data exists, payment terms are valid, the supplier is not blocked and required compliance checks are complete.

This can be measured.

“Supplier replicated successfully” cannot replace it.

## Choose the distribution pattern by consumer need

Master data can be shared through several patterns.

### 1. Synchronous API lookup

The consumer retrieves current data when needed.

Useful when:

- current authoritative value is required;
- the transaction volume is manageable;
- the owner is available;
- local persistence is unnecessary.

Examples:

- retrieve current credit status;
- validate legal identity;
- obtain approved classification.

#### Risk

The consumer depends on runtime availability and latency.

### 2. Event-driven distribution

The owner publishes a meaningful state change.

Examples:

- customer address approved;
- supplier blocked;
- product activated;
- hierarchy changed.

Useful when:

- several consumers need the change;
- asynchronous processing is acceptable;
- loose coupling is valuable.

SAP Integration Suite currently supports APIs, event-driven integration, hybrid application integration and governed access for applications and agents across SAP and third-party landscapes.

#### Risk

Consumers become temporarily inconsistent and must handle duplicates, order and replay.

### 3. Replicated operational copy

The consumer maintains a local copy.

Useful when:

- low-latency local processing is required;
- the source cannot be called during every transaction;
- the consumer must operate during source downtime.

#### Risk

The copy may become stale or be mistaken for authority.

### 4. Bulk snapshot

A complete or large dataset is distributed periodically.

Useful when:

- volume is high;
- latency is not critical;
- full reconciliation is valuable;
- the consumer can replace or compare a dataset.

#### Risk

Changes are delayed and partial recovery may be difficult.

### 5. Delta feed

Only changed records are sent.

Useful when:

- the dataset is large;
- consumers need regular updates;
- sequencing and checkpoints can be controlled.

#### Risk

A missed delta creates lasting inconsistency.

### 6. Federated access or semantic data product

Applications or analytical consumers access a governed representation without necessarily receiving an operational copy.

SAP currently positions SAP Business Data Cloud as unifying and governing SAP and third-party data through a business data fabric, with semantically rich data products and business context intended for applications, analytics and agentic AI.

#### Risk

A semantically governed analytical view should not automatically become an operational write authority.

## Do not use one distribution pattern for every consumer

A warehouse may require a local product copy for resilient execution.

An analytics platform may need a historical data product.

A customer portal may need a current API lookup.

An AI agent may need a bounded semantic view.

The underlying product identity may be the same.

The consumption contracts are different.

A modern architecture centralizes meaning, not necessarily transport.

## Publish facts, not generic changes

An event such as:

```text id="sng0s2"
BusinessPartner.Changed
```

may force every consumer to retrieve and compare the complete record.

More useful events may include:

- `BusinessPartner.IdentityApproved`;
- `BusinessPartner.AddressChanged`;
- `Supplier.PurchasingExtensionApproved`;
- `Customer.CreditBlocked`;
- `Product.Activated`.

The event should express a business fact that consumers can understand.

It should not expose every internal field update as a public contract.

### Include version and effective time

Master data changes may be:

- valid immediately;
- valid from a future date;
- corrections to historical data;
- superseded by a later change.

Consumers may need:

- object version;
- approval timestamp;
- effective-from date;
- effective-to date;
- publication timestamp.

A late event should not overwrite a newer valid state.

## Snapshot and event must not conflict

Some architectures use:

- initial snapshot;
- later delta events.

This can work well.

But the architecture must define the handover point.

Possible failure:

1. consumer loads snapshot version 100;
2. events 101–110 arrive during loading;
3. consumer activates snapshot afterward;
4. newer changes are overwritten.

A controlled process should use:

- snapshot version;
- delta checkpoint;
- ordered activation;
- reconciliation.

## Consumers should not write back through the distribution channel

A dangerous architecture loop looks like this:

1. central system distributes customer;
2. target changes customer;
3. target publishes the change back;
4. central system treats it as authoritative;
5. the update is redistributed.

Without ownership controls, this creates:

- update loops;
- field oscillation;
- lost approvals;
- accidental overwrites.

### Use change requests for non-owning systems

A consumer that wants to change governed data should submit:

- change request;
- proposed value;
- reason;
- evidence;
- requester identity.

The owner decides whether to approve it.

The target should not directly overwrite the authoritative record simply because it has a local edit screen.

### Separate local fields physically or logically

If a target owns local attributes, keep them distinguishable from governed central attributes.

For example:

```text id="b4i9al"
Central supplier identity
+
Local purchasing extension
```

The local target may update its purchasing extension.

It should not accidentally republish local values as global identity.

## Avoid last-write-wins for business master data

Last-write-wins is easy to implement.

It assumes the newest timestamp represents the correct value.

This is weak for governed business data.

A later change may be:

- unauthorized;
- based on stale information;
- a local override;
- technically delayed;
- sent from a non-owning system.

Conflict resolution should use:

- ownership;
- approval status;
- object version;
- effective date;
- domain rules.

Time is evidence.

It is not authority.

## Local copies need a freshness contract

A consumer using replicated data should know:

- authoritative source;
- last successful update;
- object version;
- expected latency;
- maximum acceptable staleness;
- current replication health.

For example:

> Product status copy is normally updated within five minutes. If no update has been received for 30 minutes, new product activations must not be assumed available.

This is stronger than calling the integration “real time.”

### Staleness should be visible to applications and agents

An AI agent may retrieve a customer classification from a convenient local index.

The index may be six hours old.

The answer should distinguish:

- value;
- source;
- version;
- last updated time;
- authority.

Otherwise, the agent presents a stale copy as current truth.

## Analytical truth and operational truth are different

A data platform may contain the best consolidated customer view.

That does not automatically make it the right system for operational updates.

An analytical record may:

- combine multiple systems;
- apply historical corrections;
- use delayed replication;
- optimize for reporting;
- include derived classifications.

An operational process may require:

- current status;
- transaction-safe validation;
- approved write path;
- immediate business rule.

Use the analytical platform for:

- reporting;
- segmentation;
- model training;
- cross-domain insight.

Use an operational domain capability for:

- creation;
- approval;
- blocking;
- transaction validation;
- controlled change.

## AI agents amplify poor ownership

A person working in one application may see one version of a customer.

An AI agent may search:

- SAP;
- CRM;
- data warehouse;
- documents;
- support tickets;
- local databases.

This increases retrieval power.

It also increases the chance of finding contradictory values.

If the architecture has no authority model, the agent must guess.

That is not an AI problem.

It is a data-ownership problem exposed by AI.

### Agents should consume governed contracts

SAP currently positions SAP Master Data Governance as ensuring that data products consumed by applications and agents begin from governed master data, while SAP Business Data Cloud emphasizes business context, policies and semantics for agentic AI.

A practical agent architecture should expose:

- authoritative APIs;
- governed data products;
- approved semantic views;
- ownership metadata;
- freshness;
- permitted actions.

It should not give the agent unrestricted access to every replicated table and ask it to infer truth.

### A data product is not automatically authoritative

A data product may provide a high-quality view for a specific purpose.

Examples:

- customer profitability;
- supplier risk;
- product availability history.

It may contain:

- governed master data;
- transactional data;
- derived metrics;
- model outputs.

The product contract should state:

- intended use;
- source;
- refresh;
- owner;
- quality;
- whether it is authoritative for operational action.

An agent may use supplier-risk data to prepare a recommendation.

It should not treat a derived risk score as authority to block the supplier unless policy explicitly permits it.

## Agent-facing master data needs provenance

A useful response to an agent may contain:

```text id="i7sot8"
Customer legal name: Example Industries GmbH
Authority: Central Business Partner Governance
Object version: 27
Effective from: 2026-06-01
Last distributed to S/4HANA: 2026-06-01 14:07 UTC
S/4HANA sales readiness: Complete for sales organization 1000
```

This gives the agent more than a value.

It gives context required to use the value responsibly.

### Separate fact, inference and recommendation

An agent may report:

- governed fact;
- local operational fact;
- analytical inference;
- recommendation.

These should not be merged.

For example:

```text id="6l70hj"
Governed fact: Supplier is centrally approved.
Operational fact: Purchasing extension for organization 2000 is missing.
Inference: Delay may affect the planned purchase order.
Recommendation: Route an extension request to procurement data stewardship.
```

The agent should not state:

> Supplier is ready.

because one central status is positive.

## Agent write access should follow ownership

An agent may be able to:

- find duplicate candidates;
- prepare a change request;
- collect missing attributes;
- propose a classification;
- route an exception.

It should not automatically:

- merge legal entities;
- overwrite governed identifiers;
- approve bank changes;
- activate a product;
- release a blocked supplier.

SAP’s current API lifecycle capabilities include exposing curated APIs as governed MCP servers with access controls and production observability for agents.

The architecture should expose task-specific tools such as:

- `prepare_supplier_change_request`;
- `retrieve_customer_authority`;
- `request_sales_extension`;
- `compare_duplicate_candidates`.

Avoid generic tools such as:

- `update_business_partner`;
- `merge_customer`;
- `change_product`.

## Master data distribution requires end-to-end reconciliation

Monitoring the integration flow is not enough.

For every important distribution process, compare:

1. approved source records;
2. records scheduled for distribution;
3. messages or events published;
4. target records created or changed;
5. target operational readiness;
6. unresolved exceptions.

Example:

```text id="k1u92y"
1,000 suppliers approved
1,000 distribution records created
1,000 delivered to target
998 supplier records created
970 purchasing extensions complete
28 awaiting local completion
2 target errors
```

The process is not 100% complete because message delivery reached 100%.

### Reconcile attributes where risk is high

For critical fields, verify:

- legal identifier;
- bank data;
- base unit;
- tax classification;
- block status;
- organizational assignment.

The target may create the object successfully while transforming an important value incorrectly.

### Reconcile key mappings

Verify:

- each central identity maps to expected targets;
- no central identity maps to multiple active target records unexpectedly;
- no target record points to two central identities;
- merges and splits are reflected.

## Errors should be classified by ownership

### Governance error

Examples:

- duplicate unresolved;
- invalid legal identifier;
- approval missing;
- policy violation.

Owner:

- data steward or data owner.

### Distribution error

Examples:

- connectivity;
- transformation;
- event delivery;
- schema failure.

Owner:

- integration engineering.

### Target validation error

Examples:

- target requires local field;
- organizational extension missing;
- local configuration rejects value.

Owner:

- target domain or local steward.

### Identity error

Examples:

- key mapping missing;
- multiple possible target records;
- wrong central identity.

Owner:

- identity or master data governance.

### Readiness error

Examples:

- record created but unusable for intended process.

Owner:

- consuming process.

A generic “master data interface error” queue hides these distinctions.

## Architecture for governed master data distribution

A practical target model can be represented as follows:

```text id="jzgrg3"
Change Sources
Users | Portals | Applications | Partners | Agents
                         |
Governance and Decision Layer
Validation | Matching | Workflow | Approval | Audit
                         |
Authoritative Domain Record
Identity | Governed attributes | Versions | Effective dates
                         |
Distribution Contracts
APIs | Business events | Deltas | Snapshots
                         |
Integration Execution
Routing | Mapping | Protocol | Retry | Correlation
                         |
Operational Consumers
S/4HANA | Cloud Apps | Warehouses | Legacy Systems
                         |
Local Extensions and Readiness
Organization | Plant | Sales area | Purchasing | Tax
                         |
Reconciliation and Control
Completeness | Accuracy | Key mapping | Readiness | Exceptions
```

Alongside the operational flow:

```text id="7j5xio"
Governed Data Products and Semantic Access
Analytics | Applications | AI Agents
```

Cross-cutting:

```text id="kshqk2"
Ownership
Security
Lineage
Freshness
Quality rules
Lifecycle
```

## The distribution layer should stay thin

The distribution layer may handle:

- routing;
- structural mapping;
- technical normalization;
- protocol conversion;
- target-specific packaging;
- retry;
- correlation.

It should not independently decide:

- which duplicate survives;
- whether a supplier is approved;
- which legal identity is correct;
- whether a product should be activated;
- whether a local override becomes global.

Those decisions belong to governance or the relevant domain.

## Use domain contracts rather than target-specific source models

Suppose the central product system distributes materials to five applications.

A weak model creates five direct contracts:

```text id="d5db3c"
Central product → S/4HANA structure
Central product → Warehouse structure
Central product → Commerce structure
Central product → Planning structure
Central product → Data platform structure
```

Some target-specific transformation is unavoidable.

But the governed source should first expose a stable product-domain contract.

Adapters can then translate the domain representation into local target needs.

This prevents target-specific requirements from reshaping the central master record.

## Do not create a universal enterprise master object

A universal customer object may attempt to include:

- legal identity;
- sales data;
- marketing consent;
- service status;
- credit information;
- billing accounts;
- analytics segments.

It becomes difficult to own and version.

Prefer bounded contracts:

- customer identity;
- commercial account;
- credit status;
- ship-to location;
- service subscriber.

These contracts can reference the same global identity.

They should not pretend every domain uses the word “customer” identically.

## Master data architecture during S/4HANA transition

During migration, ECC and S/4HANA may both contain customers, suppliers and materials.

The architecture should define:

- central authority;
- active process owner;
- legacy target;
- new target;
- migration wave;
- effective mapping;
- decommission point.

### Replicating into S/4HANA does not transfer ownership automatically

A customer may be loaded into S/4HANA before sales processes move.

The record exists.

ECC may still own current sales execution.

The migration registry should distinguish:

- replicated;
- validated;
- operationally active;
- authoritative for new transactions.

### Avoid bi-directional synchronization without field ownership

A temporary design may synchronize customer changes between ECC and S/4HANA.

Without attribute ownership, the systems can overwrite each other.

Define:

- which fields can change in ECC;
- which can change in S/4HANA;
- which changes must return through central governance;
- effective migration date;
- conflict handling.

“Keep both systems in sync” is not an architecture rule.

## Build a master data control register

For critical objects, a control register can track:

- global identity;
- governance status;
- current version;
- required targets;
- target identifiers;
- distribution status;
- local extension status;
- readiness;
- exceptions;
- owner.

This should not duplicate every master data attribute.

It records the lifecycle and distribution evidence.

### Example

| Target | Target ID | Distributed version | Local extension | Ready |
|---|---|---:|---:|---:|
| S/4HANA EU | BP 1000456 | 27 | Complete | Yes |
| Procurement cloud | SUP-7789 | 27 | Complete | Yes |
| Warehouse DE | V-9082 | 26 | Complete | No |
| Analytics | Global ID | 27 | N/A | Yes |

The warehouse has an older version.

The architecture can now identify the inconsistency before it causes a transaction error.

## A strong pilot: supplier onboarding and distribution

Supplier data is a useful pilot because it crosses:

- governance;
- procurement;
- finance;
- compliance;
- local SAP extensions;
- partner interaction.

### Pilot scope

- one supplier type;
- one legal entity;
- two purchasing organizations;
- SAP S/4HANA plus one procurement application.

### Governed attributes

- legal name;
- registration ID;
- central address;
- global supplier classification;
- central status.

### Local attributes

- purchasing organization;
- payment terms;
- reconciliation account;
- local tax;
- ordering currency.

### Process

1. request submitted;
2. duplicate check performed;
3. legal and compliance data validated;
4. central supplier approved;
5. supplier identity distributed;
6. target records created;
7. local extensions completed;
8. purchasing readiness confirmed.

### Key controls

- one global identity;
- governed key mapping;
- versioned events or messages;
- target acknowledgement;
- readiness check;
- no local overwrite of central identity;
- change requests for central attributes.

### Agent role

An AI agent may:

- detect missing information;
- compare duplicate candidates;
- summarize target errors;
- route local extension tasks.

It may not approve a duplicate merge or activate bank data.

### Success measures

- onboarding lead time;
- duplicate rate;
- first-time-right distribution;
- target-readiness time;
- local completion effort;
- unresolved identity conflicts;
- repeated data errors.

## A practical implementation sequence

### Phase 1: Define domains

Identify master data domains such as:

- customer;
- supplier;
- product;
- finance;
- asset;
- location.

### Phase 2: Define ownership

Assign authority by:

- attribute;
- relationship;
- decision;
- lifecycle state.

### Phase 3: Identify identities

Document:

- global ID;
- system IDs;
- external IDs;
- business roles;
- key mappings.

### Phase 4: Define governance

Specify:

- authoring;
- validation;
- matching;
- approval;
- audit;
- effective dates.

### Phase 5: Define readiness

For each consuming process, specify what makes the object usable.

### Phase 6: Select distribution patterns

Choose API, event, replicated copy, snapshot or delta based on consumer need.

### Phase 7: Design local extensions

Separate central and local ownership.

### Phase 8: Create contracts

Define:

- semantics;
- versions;
- identifiers;
- effective time;
- provenance;
- error behaviour.

### Phase 9: Build reconciliation

Compare source approval, distribution, target creation, key mapping and readiness.

### Phase 10: Expose governed consumption

Provide approved APIs, semantic views and data products for applications and agents.

### Phase 11: Control writeback

Use change requests rather than uncontrolled target updates.

### Phase 12: Improve through recurrence

Repeated target errors should lead to:

- better governance;
- stronger source validation;
- improved contracts;
- reduced local variation.

## Metrics that matter

### Authoritative-ownership coverage

What percentage of critical attributes has a named accountable owner?

### Duplicate rate

How many business entities have more than one active global identity?

### Key-mapping completeness

What percentage of governed records has the required target mappings?

### Distribution completeness

What percentage of approved records reached every mandatory target?

### Target-readiness rate

What percentage is operationally usable, not merely created?

### Version consistency

How many targets operate on older object versions?

### Local-extension time

How long from central approval until local readiness?

### Source-correction rate

How often does the integration or target repair data that should have been correct at the source?

### Default-use rate

How often are fallback values applied?

### Writeback-conflict rate

How often do non-owning systems attempt conflicting changes?

### Agent-authority compliance

What percentage of agent answers and actions use governed sources and bounded tools?

### Unclear-provenance rate

How often can users or agents not determine the source and freshness of a value?

## Common mistakes

### Mistake 1: Treating distribution as governance

Bad data is synchronized successfully.

### Mistake 2: Declaring one system owner of the entire object

Different domains actually own different attributes and decisions.

### Mistake 3: Using record presence as proof of authority

A target copy becomes an accidental source.

### Mistake 4: Using last-write-wins

The newest update overrides the accountable owner.

### Mistake 5: Hiding missing data with integration defaults

Technical success creates inconsistent truth.

### Mistake 6: Calling a record ready after message delivery

Local organizational data remains incomplete.

### Mistake 7: Managing identifiers only inside mapping code

Merges, splits and reconciliation become unmanageable.

### Mistake 8: Allowing direct target writeback

Local changes overwrite governed values or create loops.

### Mistake 9: Building one enormous golden record

Every local field enters the central workflow.

### Mistake 10: Using one distribution pattern for every consumer

Operational, analytical and agent needs are different.

### Mistake 11: Treating a data platform as operational authority

A delayed or derived view drives production decisions.

### Mistake 12: Giving AI access to every copy

The agent guesses which conflicting value is correct.

### Mistake 13: Exposing generic master-data write tools to agents

Preparation, approval and execution are collapsed.

### Mistake 14: Monitoring messages but not target readiness

Every interface is green while the process remains blocked.

### Mistake 15: Synchronizing ECC and S/4HANA without field ownership

The transitional landscape becomes multi-master by accident.

## Questions architects and managers should ask

1. Which domain owns each important master data fact?
2. Which system is authoritative, and for which attributes?
3. Which systems are only consumers or local extensions?
4. What is the global identity?
5. How are system-specific IDs mapped?
6. How are duplicate merges and splits handled?
7. What does operational readiness mean for each process?
8. Does distribution preserve approval, version and effective date?
9. Which fields may local systems change?
10. How do non-owning systems request governed changes?
11. Are defaults hiding source-quality problems?
12. How stale may each local copy become?
13. Can applications see provenance and version?
14. Are analytical and operational uses separated?
15. Which source should an AI agent trust?
16. Can the agent distinguish governed fact from inference?
17. Are agent write operations bounded by domain authority?
18. Can we reconcile approval through target readiness?
19. Which master data errors are repeatedly repaired downstream?
20. Are we distributing trusted meaning or merely synchronizing records?

## The goal is trusted meaning, not identical databases

A modern enterprise will not have one database containing the only copy of every customer, supplier and product.

SAP, cloud applications, warehouses, partner platforms, data products and AI agents will all need different representations.

The architecture should not attempt to eliminate every copy.

It should ensure that every copy has a defined role.

SAP currently positions SAP Master Data Governance as the governance layer for trusted master records, policies, matching, workflow, data quality and audit. SAP explicitly distinguishes master data integration as the distribution of current master data rather than a mechanism that improves its quality.

SAP Integration Suite provides the APIs, events, application integration and governance capabilities through which applications and agents can consume or receive that data across hybrid landscapes.

SAP Business Data Cloud extends the consumption model toward governed business context, semantically rich data products and AI use cases.

These capabilities solve different parts of the problem.

They should not be collapsed into one technical layer.

The strongest architecture establishes:

- accountable ownership;
- governed identity;
- explicit local extensions;
- stable distribution contracts;
- target readiness;
- end-to-end reconciliation;
- provenance for applications and agents.

The key question is not:

> Are all systems synchronized?

It is:

> Can the company explain which value is authoritative, why it is trusted, where it has been distributed and whether every consuming process can use it correctly?

When that answer is clear, master data becomes an enterprise capability.

When it is not, faster distribution only spreads uncertainty more efficiently.

---

### Master data ownership and distribution checklist

- [ ] Governance and distribution are treated as separate capabilities.
- [ ] Every critical business fact has one accountable authority.
- [ ] Ownership is defined at attribute, relationship and decision level.
- [ ] Authoring, governance, authority and consumption roles are distinguished.
- [ ] Central and local attributes are explicitly separated.
- [ ] The golden record does not absorb every local operational field.
- [ ] Global, system, role and external identities are distinguished.
- [ ] Key mappings are governed master data.
- [ ] Merge and split processes preserve history and references.
- [ ] Master data lifecycle states are explicit.
- [ ] Approval, distribution, creation and readiness are separate states.
- [ ] Readiness is defined by the consuming business process.
- [ ] APIs, events, snapshots and replicated copies are selected by need.
- [ ] Consumers know authority, version, effective date and freshness.
- [ ] Last-write-wins is not used as a substitute for ownership.
- [ ] Defaults are approved, visible and monitored.
- [ ] Non-owning systems submit change requests rather than direct overwrite.
- [ ] Local copies have staleness limits and health indicators.
- [ ] Operational and analytical authority are separated.
- [ ] Events communicate meaningful governed state changes.
- [ ] Snapshot and delta handover is controlled.
- [ ] Distribution is reconciled through target readiness.
- [ ] Key mappings and critical attributes are reconciled.
- [ ] Errors are routed by governance, integration, target and process cause.
- [ ] AI agents consume governed APIs and data products.
- [ ] Agent outputs preserve provenance and distinguish inference from fact.
- [ ] Agent write tools are bounded to preparation and approved actions.
- [ ] S/4HANA transition ownership is explicit by field and migration wave.
- [ ] Success is measured through trusted and usable business data.

### Sources and further reading

SAP currently describes SAP Master Data Governance as the governance layer of a business data fabric, supporting golden records, profiling, matching, merging, semantic reconciliation, workflows, data-quality monitoring and auditable change processes across SAP and third-party data.

SAP explicitly distinguishes master data integration from master data management: integration distributes master data to applications and provides a harmonized view, but does not itself improve the quality of the data being distributed.

SAP currently positions SAP Integration Suite as a secure integration platform for APIs, events, applications, data, processes and AI agents across SAP and third-party cloud, on-premises and hybrid landscapes, with centralized governance, monitoring and security.

SAP currently positions SAP Business Data Cloud as a governed business data fabric that unifies SAP and third-party data, preserves business semantics and provides semantically rich data products and business context for applications, analytics and agentic AI.

SAP’s current API lifecycle capabilities include Graph as a semantic access layer, centralized Developer Hub capabilities and governed MCP-server lifecycle management for exposing curated APIs to AI agents with runtime controls and production traceability.

*Reviewed: July 2026. SAP Master Data Governance, SAP Business Data Cloud, SAP Integration Suite and agent-related capabilities continue to evolve. Final ownership, distribution and agent-access decisions should be validated against current SAP documentation and the organization’s actual data domains, legal requirements and operating model.*
