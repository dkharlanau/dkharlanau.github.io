# How to Modernize SAP IDoc and File Integrations Without Rewriting the Entire Landscape

A company begins an SAP integration-modernization programme.

The objective appears reasonable:

> Replace legacy IDocs and files with modern APIs and events.

The integration inventory contains 600 interfaces.

A consulting team estimates that each interface will need:

- analysis;
- redesign;
- development;
- testing;
- business validation;
- cutover;
- hypercare.

The programme becomes one of the largest parts of the S/4HANA transformation.

Three years later, many interfaces have been rewritten.

Some now use JSON instead of IDocs.

Others send files through a cloud integration platform instead of an on-premises middleware server.

The business process has not changed.

The same mappings, errors, duplicate risks and ownership problems remain.

The company has paid to rebuild its integration landscape without simplifying it.

This is the main risk of integration modernization.

Old technology can create constraints.

But the age of the protocol is not always the main problem.

An IDoc may be reliable, observable and well understood.

A REST API may be fragile, undocumented and tightly coupled.

A daily file may be the correct solution for a reconciled bulk process.

A real-time event may create complexity without producing meaningful business value.

The objective should not be:

> Replace every old interface with a new protocol.

It should be:

> Reduce integration risk, cost and coupling while preserving the business processes that already work.

That requires selective modernization.

Some integrations should be retired.

Some should remain largely unchanged.

Some should move to new infrastructure.

Some should receive a stable API or event facade.

Only a limited group should be redesigned completely.

## Old protocol does not automatically mean bad architecture

An interface may be twenty years old and still provide:

- stable business behaviour;
- complete transaction history;
- controlled retries;
- high-volume processing;
- clear ownership;
- reliable reconciliation.

Another interface may have been created six months ago and already contain:

- undocumented mappings;
- generic technical users;
- no duplicate control;
- no business monitoring;
- consumer-specific logic;
- unclear failure recovery.

Modernity should be evaluated through architectural quality, not protocol age.

Useful criteria include:

- business criticality;
- business fit;
- reliability;
- coupling;
- security;
- operability;
- change cost;
- reuse;
- lifecycle support;
- strategic constraints.

The transport format is only one factor.

## Why IDocs remain common

IDocs are deeply embedded in many SAP landscapes because they support recurring enterprise integration needs:

- sales orders;
- purchase orders;
- order confirmations;
- deliveries;
- invoices;
- master data;
- financial messages;
- partner communication.

A mature IDoc process may already provide:

- structured business-message types;
- sender and receiver context;
- processing statuses;
- asynchronous transfer;
- controlled reprocessing;
- partner-specific configuration;
- operational support procedures.

The problem is usually not that the message is called an IDoc.

Problems arise when:

- custom extensions are undocumented;
- one IDoc is used with different meanings;
- mappings are duplicated;
- status success is confused with business completion;
- reprocessing can create duplicates;
- direct dependencies prevent system change;
- monitoring is fragmented.

Changing the payload to JSON will not solve these issues by itself.

## Why files remain common

File interfaces are also used because they solve real requirements:

- large periodic data transfers;
- banking;
- payroll;
- supplier catalogues;
- historical loads;
- partner exchanges;
- regulatory submissions;
- bulk reconciliation.

A file provides a clear batch boundary.

The sender and receiver can compare:

- file name;
- record count;
- control total;
- creation time;
- processing status.

This can be operationally useful.

The weaknesses appear when files are used for processes that require:

- immediate response;
- continuous transaction flow;
- item-level recovery;
- real-time visibility;
- low-latency customer interaction.

The question is not whether files are old.

It is whether batch behaviour fits the business requirement.

## Modernization begins with discovery

Many organizations do not know their real interface landscape.

They may have:

- a middleware catalogue;
- SAP technical configurations;
- network flows;
- batch schedules;
- integration documentation;
- spreadsheets maintained by support teams.

None of these sources is complete.

An interface may also depend on:

- custom ABAP;
- background jobs;
- shared folders;
- scripts;
- database procedures;
- manual file movement;
- partner middleware;
- email.

Before selecting migration technology, create an evidence-based inventory.

For each integration, collect:

- business purpose;
- source;
- target;
- protocol;
- message type;
- direction;
- frequency;
- volume;
- schedule;
- business owner;
- technical owner;
- criticality;
- mappings;
- custom logic;
- monitoring;
- error handling;
- recovery;
- known consumers;
- current lifecycle state.

Do not begin with middleware objects alone.

One middleware flow may support several business interactions.

Several technical flows may collectively support one business process.

## Identify whether the interface is still used

A surprising number of integration objects may be:

- inactive;
- replaced;
- used only by a retired partner;
- executed but producing no consumed result;
- maintained only because nobody wants to remove them.

Technical execution does not prove business use.

An interface may send a file every night while the target team stopped using it two years ago.

Before migrating, verify:

- recent transaction volume;
- active receiving system;
- business consumer;
- current support owner;
- evidence of downstream use.

The cheapest migration is retiring an interface that no longer has a purpose.

## Build a dependency map

An interface can appear independent while supporting a larger chain.

For example:

1. customer master IDoc is distributed;
2. local mapping creates target customer;
3. order file arrives;
4. target system creates delivery request;
5. confirmation file returns;
6. SAP updates order status;
7. billing depends on that status.

Replacing one interface without understanding the chain can change:

- timing;
- identifiers;
- ordering;
- error behaviour;
- status visibility.

The inventory should therefore connect interfaces to:

- business services;
- upstream processes;
- downstream processes;
- master data;
- scheduled jobs;
- manual recovery tasks.

## Classify the modernization decision

Every interface should receive one of several treatments.

## 1. Retire

Remove the interface because:

- the business process no longer exists;
- the target system is retired;
- another interface replaced it;
- the data is not used;
- the function can be removed during process simplification.

## 2. Retain

Keep the interface largely as it is because:

- it is stable;
- the business requirement remains batch or asynchronous;
- the technology remains supported;
- replacement creates little value;
- the interface has reliable operations and reconciliation.

Retain does not mean ignore.

The interface may still need:

- stronger monitoring;
- better documentation;
- security improvement;
- ownership;
- automated tests.

## 3. Rehost

Move the interface to a different runtime while keeping most of its business contract.

Examples include:

- moving an integration flow from older middleware to a cloud integration platform;
- moving file transfer to managed SFTP;
- running hybrid integration through a controlled edge runtime.

SAP currently positions Cloud Integration as supporting A2A, B2B and B2G flows across SAP and third-party landscapes, while Integration Suite supports cloud, on-premises and hybrid connectivity. SAP also provides an edge integration cell for running centrally managed integrations in private landscapes when data should remain there.

## 4. Replatform

Rebuild the interface on a new platform but preserve the external business behaviour.

The protocol may remain:

- IDoc;
- file;
- SOAP;
- EDI.

The main change is the integration implementation and operating platform.

## 5. Wrap

Keep the current backend interface but place a stable facade around it.

Examples:

- expose a business API that internally creates an IDoc;
- accept a modern event and convert it into the existing SAP message;
- provide a status API over a file-based batch process.

This can protect new consumers from legacy details.

## 6. Redesign

Change the integration pattern because the business interaction has changed.

Examples:

- replace a nightly order file with real-time order submission;
- publish business events instead of sending separate status files;
- introduce a bulk API with transaction-level feedback;
- redesign master data ownership.

## 7. Replace with standard content

Use an available standard API, event or integration package instead of maintaining a custom interface.

SAP currently describes Integration Suite as providing thousands of prebuilt integrations, APIs, events and accelerators, while SAP Business Accelerator Hub is the discovery point for supported integration content.

Standard content should still be assessed against the actual business process.

## 8. Consolidate

Several interfaces may perform similar work.

For example:

- five customer outbound interfaces;
- three supplier code mappings;
- separate files for closely related order statuses.

They may be consolidated around:

- one governed business contract;
- one reusable mapping;
- one event;
- one API product;
- one partner-integration pattern.

## Migration value differs by category

A large programme becomes manageable when it stops treating all interfaces equally.

A possible portfolio may look like:

- 15% retire;
- 30% retain with operational improvements;
- 20% rehost or replatform;
- 20% wrap;
- 10% redesign;
- 5% consolidate into new shared services.

The exact numbers will differ.

The principle remains:

> Rewrite should be one option, not the default.

## Do not redesign before understanding current behaviour

Legacy integration logic is often poorly documented.

But it may contain years of business decisions.

Examples include:

- partner-specific identifier conversion;
- country exceptions;
- unit conversions;
- material substitutions;
- date rules;
- aggregation;
- special error handling;
- duplicate protection.

A new integration team may regard this logic as technical debt.

Some of it is.

Some represents valid business requirements.

Before rewriting, distinguish:

- required business rule;
- obsolete workaround;
- target-system limitation;
- historical defect correction;
- technical transformation;
- accidental behaviour.

Deleting unknown logic is not simplification.

It is uncontrolled process change.

## Extract the business contract from the old interface

For every interface being changed, document:

- trigger;
- source business object;
- target business object;
- mandatory data;
- identifiers;
- mappings;
- validation;
- transaction boundary;
- acknowledgement;
- retry;
- correction;
- reconciliation;
- service expectation.

This becomes the modernization baseline.

Do not use the current technical message as the only specification.

The current structure may contain unnecessary implementation details.

## Example: an old order IDoc

An outbound order interface may contain:

- order header;
- partners;
- items;
- schedule lines;
- texts;
- pricing;
- internal codes;
- custom segments.

The target may use only:

- external order reference;
- ship-to;
- material;
- confirmed quantity;
- delivery date.

A direct one-to-one conversion to JSON would preserve unnecessary coupling.

A better redesign would define the target business contract first.

The old IDoc can remain the source adapter while the new contract is introduced.

## The strangler pattern for integrations

A practical modernization strategy is to replace parts of the landscape gradually.

The pattern works like this:

1. Keep the existing integration running.
2. Introduce a controlled routing or facade layer.
3. Move one consumer or business scenario to the new path.
4. Compare results.
5. Expand gradually.
6. retire the old path when no consumers remain.

This avoids one high-risk cutover.

## Example: customer master distribution

The current process sends one customer IDoc to several systems.

A gradual approach may be:

### Stage 1

Leave the existing IDoc distribution unchanged.

### Stage 2

Publish a governed customer event alongside the IDoc.

### Stage 3

Move one low-risk consumer to the event.

### Stage 4

Reconcile customer versions and target readiness.

### Stage 5

Move additional consumers.

### Stage 6

Retire individual IDoc receivers only after proven stability.

The source process does not need to change for every consumer at once.

## Anti-corruption layers protect new consumers

A legacy message may expose:

- SAP-specific codes;
- custom segments;
- historical naming;
- inconsistent structures.

A new consumer should not necessarily depend on them.

An anti-corruption layer translates the legacy representation into a stable business contract.

It can:

- normalize identifiers;
- translate codes;
- hide obsolete fields;
- expose consistent errors;
- preserve correlation;
- shield consumers from backend changes.

The layer should not become permanent uncontrolled middleware.

It needs:

- defined scope;
- owner;
- mapping registry;
- performance expectations;
- planned lifecycle.

## Wrapping is not the same as solving

A new API may accept a clean order request and internally generate an existing IDoc.

This can be a strong transitional architecture.

It allows:

- modern consumer onboarding;
- stable external contract;
- reuse of proven SAP processing;
- gradual backend modernization.

But the wrapper does not remove weaknesses inside the old process.

If the IDoc has:

- duplicate risk;
- poor error messages;
- undocumented mapping;
- weak reconciliation,

the API must address or expose these limitations.

Do not present asynchronous IDoc acceptance as immediate business completion.

## A facade should report honest states

A facade over a legacy asynchronous process may use statuses such as:

- request accepted;
- legacy message created;
- SAP processing started;
- business document created;
- business validation failed;
- downstream completion pending.

Do not return:

```text
200 Success
```

when only the IDoc was generated.

The consumer needs to know the actual process state.

## Keep business identity across old and new paths

Every migrated transaction should preserve correlation between:

- external business reference;
- old message ID;
- new integration message ID;
- SAP document;
- target document.

This allows:

- reconciliation;
- duplicate prevention;
- support;
- rollback;
- comparison during parallel run.

Changing technology without preserving identity makes transition risk harder to control.

## Modernizing files does not always mean removing files

A file interface can be improved significantly without changing the business pattern.

Possible improvements include:

- move from unsecured shared folders to managed SFTP;
- introduce encryption and signing;
- standardize file naming;
- add manifest and control totals;
- implement duplicate-file detection;
- support record-level error reporting;
- automate archival;
- add business reconciliation;
- expose processing status through an API;
- create alerts based on expected arrival time.

The interface remains file based.

Its operational quality improves.

## Add a control record

A robust batch may include:

- file identifier;
- source;
- creation timestamp;
- schema version;
- expected record count;
- expected amount or quantity total;
- checksum;
- sequence;
- previous file reference.

The receiver can validate completeness before processing.

This is especially important for:

- payments;
- financial postings;
- payroll;
- inventory;
- billing.

## Distinguish full snapshots and deltas

A file may represent:

### Full snapshot

The complete current dataset.

### Delta

Only records changed since the prior extract.

The receiver must know which one it is.

Snapshot processing may require:

- comparison;
- deletion handling;
- replacement rules.

Delta processing requires:

- sequence;
- missing-file detection;
- replay;
- dependency on earlier files.

Confusing these models creates silent inconsistency.

## File arrival is not business completion

Monitoring should distinguish:

1. file expected;
2. file received;
3. file validated;
4. records processed;
5. target business objects created;
6. rejected records resolved;
7. totals reconciled.

A successfully transferred file may contain thousands of rejected records.

The transfer protocol can be green while the business process fails.

## When an IDoc should be retained

Retaining an IDoc may be rational when:

- SAP and receiver already support it well;
- the business process is stable;
- asynchronous processing is appropriate;
- volume is manageable;
- status handling is mature;
- mappings are controlled;
- no new consumer needs a different contract;
- replacement value is low.

Retain it, but improve:

- documentation;
- security;
- monitoring;
- business reconciliation;
- automated regression tests;
- ownership.

Modernization should not create change merely to produce a more fashionable diagram.

## When an IDoc should be wrapped

Wrapping is useful when:

- new consumers should not learn IDoc structure;
- a modern API or event contract is needed;
- the SAP backend cannot change immediately;
- several consumers need one stable representation;
- S/4HANA migration is underway.

The wrapper can translate between:

- business API and IDoc;
- business event and IDoc;
- canonical domain message and IDoc.

## When an IDoc should be redesigned

Redesign is justified when:

- the business needs immediate response;
- the current message exposes excessive SAP internals;
- many custom extensions exist;
- consumers require only a small stable capability;
- error recovery is unmanageable;
- the business interaction has changed;
- the interface prevents clean-core or cloud adoption.

## When a file should be retained

Retain a file when:

- the process is genuinely batch oriented;
- complete reconciliation is valuable;
- partner capability is limited;
- volume is large;
- latency is acceptable;
- recovery at batch level is appropriate.

## When a file should become an API

Consider an API when:

- transactions arrive continuously;
- callers need immediate validation;
- item-level status matters;
- batch delays affect customers;
- the source can manage individual retries and idempotency.

## When a file should become an event stream

Consider events when:

- state changes should reach several consumers;
- the producer should not wait for consumers;
- near-real-time reaction matters;
- consumers can tolerate eventual consistency;
- replay and ordering are designed.

Do not convert a reconciled financial batch into thousands of events without proving that the new control model is stronger.

## Rehost versus redesign

This distinction should be explicit.

## Rehost

The interface behaviour remains largely the same.

The runtime changes.

Advantages:

- lower business risk;
- faster migration;
- easier testing;
- continuity.

Limitations:

- old coupling remains;
- old mappings remain;
- old process limitations remain.

## Redesign

The business contract or interaction pattern changes.

Advantages:

- potential simplification;
- improved consumer experience;
- new real-time or event capabilities;
- reduced coupling.

Risks:

- larger testing scope;
- changed timing;
- new failure behaviour;
- process change;
- more business involvement.

A migration portfolio normally needs both.

Calling every rehost a transformation exaggerates value.

Treating every interface as a redesign increases cost unnecessarily.

## SAP’s current migration position supports phased modernization

SAP currently presents migration from SAP Process Orchestration to Integration Suite as a journey that can proceed at the customer’s pace. Its migration material emphasizes assessment, planning, mapping existing patterns to the new platform, reusing integration artifacts, testing and preserving business continuity.

That is a more realistic model than a universal rewrite.

The platform transition and the architecture redesign can occur at different speeds.

## Build a migration decision score

A useful scoring model can evaluate each interface across several dimensions.

## Business criticality

- What happens if it fails?
- Is there a workaround?
- Does it affect customers, finance or physical operations?

## Technical risk

- Is the current technology supported?
- Does it depend on fragile infrastructure?
- Are security controls weak?
- Is specialist knowledge disappearing?

## Change demand

- How often does the interface change?
- Do new consumers regularly request access?
- Does it block product or process changes?

## Coupling

- How much source-specific structure does the target understand?
- How much target logic exists in middleware?
- Are mappings duplicated?

## Operational quality

- Is monitoring complete?
- Can messages be replayed safely?
- Are errors actionable?
- Is reconciliation available?

## Modernization value

- Will redesign reduce interfaces?
- Will it enable new business behaviour?
- Will it lower support effort?
- Will it improve security or speed?

An interface with high risk and high value should be redesigned early.

An interface with low risk and low value should often be retained.

## Avoid scoring only technical age

A simple rule such as:

> All interfaces older than ten years must be replaced

is weak.

Age may correlate with:

- old security;
- unsupported software;
- limited skills.

But the interface’s business behaviour and replacement value still matter.

## Create modernization waves

Do not migrate interfaces randomly.

Group them by:

- business domain;
- source system;
- target system;
- integration pattern;
- shared mappings;
- partner;
- cutover dependency.

Example waves might be:

### Wave 1: Retire and clean

Remove unused interfaces and improve the inventory.

### Wave 2: Low-risk replatform

Move straightforward mappings and file transfers.

### Wave 3: Shared foundations

Create common security, monitoring, error handling and mapping services.

### Wave 4: High-value redesign

Modernize customer-facing and frequently changing integrations.

### Wave 5: Complex B2B and financial flows

Move only after operational controls are proven.

### Wave 6: Final legacy decommissioning

Remove old runtime after all dependencies are confirmed.

## Start with common capabilities

Before migrating hundreds of interfaces, create standard patterns for:

- authentication;
- certificate management;
- correlation;
- logging;
- error messages;
- retries;
- dead-letter handling;
- file naming;
- alerts;
- mapping versioning;
- deployment;
- testing.

Otherwise, each migration team will create its own modern solution.

The company will reproduce inconsistency on the new platform.

## Migration factories can scale good and bad designs

A migration factory can accelerate repetitive conversion.

It works well for:

- inventory;
- pattern classification;
- mechanical flow conversion;
- test generation;
- deployment;
- documentation.

It can also reproduce:

- obsolete mappings;
- poor errors;
- excessive point-to-point connections;
- unused interfaces.

Automation should not remove the architecture review.

Every migrated interface should pass a simple question:

> Are we preserving this behaviour deliberately, or only because the old flow contained it?

## Use automated assessment carefully

Assessment tools can help identify:

- interface objects;
- adapters;
- mappings;
- custom components;
- migration complexity;
- dependencies.

SAP currently describes assessment and migration-automation tooling, reuse of existing integration artifacts and partner-supported migration services as part of its Process Orchestration migration programme.

The output supports planning.

It does not determine business value or semantic correctness.

## Mapping reuse should be governed

An old middleware flow may contain a customer or material mapping used by several interfaces.

During migration, teams may copy it into new flows.

The organization should instead ask:

- Is this still the approved mapping?
- Who owns it?
- Can it become a reusable asset?
- Is it target-specific?
- Should it be replaced by master data or a source-system rule?

Migration is an opportunity to expose hidden mapping logic.

It should not merely copy it to a new runtime.

## Preserve traceability during dual operation

During transition, old and new paths may run together.

Every transaction should record:

- source reference;
- old-flow message ID;
- new-flow message ID;
- target result;
- processing timestamp;
- comparison result.

Without this, teams cannot prove whether the two paths behave consistently.

## Use shadow mode before active cutover

In shadow mode, the new integration processes a copy of the message but does not create the final business effect.

It can compare:

- mapped output;
- target determination;
- errors;
- processing time;
- record counts.

For example, a new order mapping can generate a proposed target payload without creating a second SAP order.

This detects semantic differences safely.

## Shadow mode has limitations

It may not reproduce:

- target updates;
- locks;
- real transactional validations;
- downstream side effects;
- production load.

It is a useful evidence source, not complete proof.

## Parallel run needs duplicate protection

In active parallel processing, both old and new paths may reach the target.

This is dangerous for:

- orders;
- invoices;
- payments;
- goods movements;
- master data creation.

Use:

- separate test target;
- dry-run mode;
- controlled document type;
- stable business idempotency key;
- one active writer and one observer.

Do not create duplicate production transactions merely to compare implementations.

## Reconcile outputs, not only payloads

Two integrations may produce different technical messages but the same correct business result.

They may also produce identical payloads while target processing differs.

Comparison should cover:

- target document;
- business status;
- quantities;
- values;
- relationships;
- errors;
- downstream completion.

The migration goal is business equivalence, not byte-for-byte equality.

## Define acceptable differences

A redesigned interface may intentionally change:

- timing;
- grouping;
- error format;
- identifiers;
- batch size;
- status model.

The team should define expected differences before comparison.

Otherwise, every variation becomes an unexplained defect.

## Test production history

Use representative historical cases:

- common transactions;
- high-value transactions;
- unusual countries;
- maximum lengths;
- unknown codes;
- cancellations;
- corrections;
- duplicate messages;
- late files;
- partial processing.

Do not test only clean current examples.

Legacy interfaces often contain their hardest behaviour in rare historical cases.

## Build golden datasets

A golden dataset contains approved source inputs and expected business outcomes.

It may include:

- input message;
- mapping result;
- target document;
- expected errors;
- reconciliation totals.

Golden datasets support:

- migration comparison;
- regression testing;
- later platform upgrades;
- mapping changes.

They also preserve knowledge that would otherwise remain inside consultants’ experience.

## Cutover needs an in-flight strategy

At cutover, some transactions may be:

- created but not transferred;
- transferred but not processed;
- failed and waiting for retry;
- partially processed;
- waiting for partner response.

The cutover plan should identify:

- queue and file backlogs;
- open IDocs;
- retry queues;
- messages in middleware;
- target processing state;
- manual recovery actions.

For each category, decide:

- complete on old path;
- move to new path;
- cancel;
- reconcile manually.

Do not route the same in-flight transaction through both paths.

## Establish a cutover boundary

A useful boundary may be based on:

- timestamp;
- business document number;
- file sequence;
- message ID;
- posting date.

The boundary should be visible and auditable.

For example:

> All purchase orders created before 22:00 are completed through the old integration. Orders created after 22:00 use the new API.

The actual rule depends on process behaviour.

## Plan rollback honestly

A middleware deployment can be rolled back.

The business transactions created during the new path may remain.

Rollback planning should cover:

- messages already delivered;
- documents created;
- files acknowledged;
- partner responses;
- sequence numbers;
- duplicate protection.

Reactivating the old interface is not enough if the same business transactions can be sent again.

## Do not decommission too early

The new interface may work for normal volume but fail during:

- month-end;
- seasonal peak;
- partner batch;
- mass master data update;
- rare correction process.

Decommissioning criteria should include:

- stable production period;
- peak-cycle completion;
- resolved migration defects;
- complete reconciliation;
- support readiness;
- no active old consumers;
- archived documentation and logs.

## Do not keep old runtime indefinitely

The opposite failure is permanent dual operation.

This creates:

- duplicate support cost;
- old security exposure;
- confusion about active path;
- continued specialist dependency;
- pressure to maintain both environments.

Every retained coexistence state should have:

- purpose;
- owner;
- end date;
- retirement conditions.

## Hybrid integration is a transition and operating model

Some SAP systems and data will remain:

- on premises;
- in private cloud;
- in public cloud;
- in partner environments.

SAP currently states that Integration Suite supports cloud, on-premises and hybrid scenarios, with centrally managed integration and private runtime options through edge integration cell where required.

Hybrid does not necessarily mean temporary.

It still requires architectural clarity:

- where runtime occurs;
- where data travels;
- where logs are stored;
- who operates connectivity;
- what happens when cloud or network access fails.

## Security modernization may justify migration even when the process stays the same

An interface may need replatforming because of:

- unsupported encryption;
- weak authentication;
- unmanaged credentials;
- broad technical users;
- exposed shared folders;
- missing audit;
- outdated runtime.

The business contract can remain stable while security and operations improve.

This is a valid modernization benefit.

## Modern monitoring should combine technical and business signals

Technical monitoring should include:

- connectivity;
- message status;
- processing time;
- retries;
- certificate status;
- file arrival;
- queue backlog.

Business monitoring should include:

- orders missing in target;
- invoices rejected;
- supplier records not ready;
- payment totals mismatched;
- shipment confirmations delayed.

SAP currently describes Integration Suite as providing centralized governance, real-time monitoring and security across APIs, events, application integrations and partner interactions.

The organization still needs to define business completion.

## Support processes must be migrated too

A new interface is not production-ready because the development test passed.

Operations need:

- dashboard;
- alert;
- ownership;
- runbook;
- replay procedure;
- reconciliation report;
- escalation;
- access;
- known-error knowledge.

Migration projects often move the flow but leave the support model behind.

The new platform then depends on project consultants for every incident.

## Compare total cost, not only development effort

A redesign may require more initial work but reduce:

- manual monitoring;
- consumer onboarding;
- duplicated mappings;
- support incidents;
- future change cost.

A rehost may be cheaper initially but preserve ongoing complexity.

Estimate:

### One-time cost

- discovery;
- design;
- development;
- testing;
- cutover;
- training.

### Recurring cost

- platform;
- runtime;
- support;
- monitoring;
- specialist skills;
- mapping changes;
- security maintenance.

### Risk cost

- business interruption;
- duplicate transactions;
- lost messages;
- failed cutover;
- extended dual operation.

The lowest migration estimate is not automatically the lowest total cost.

## A practical modernization decision table

| Current situation | Preferred starting action |
|---|---|
| Interface unused | Retire |
| Stable IDoc with mature operations | Retain or replatform |
| Stable file with genuine batch requirement | Retain and strengthen controls |
| New consumers need modern access | Wrap with API or event facade |
| Old middleware unsupported | Replatform |
| Excessive custom mappings | Redesign semantics and consolidate |
| Customer-facing process needs immediate response | Redesign toward API |
| Many consumers need state-change notification | Add governed event |
| High-volume reconciled financial batch | Keep batch unless controls improve through change |
| Temporary S/4HANA transition | Use anti-corruption layer |
| Multiple duplicate interfaces | Consolidate around shared contract |
| Security weakness | Rehost or replatform even if process remains |

## A practical programme sequence

## Phase 1: Discover

Build the technical and business inventory.

## Phase 2: Remove

Retire unused interfaces and duplicate schedules.

## Phase 3: Stabilize

Improve ownership, monitoring, security and reconciliation for critical existing flows.

## Phase 4: Create standards

Define patterns for APIs, events, IDocs, files, B2B, errors and mapping.

## Phase 5: Build shared foundations

Implement:

- connectivity;
- security;
- observability;
- deployment;
- testing;
- mapping governance.

## Phase 6: Replatform low-risk flows

Move technically straightforward integrations.

## Phase 7: Wrap strategic legacy capabilities

Protect new consumers with stable business contracts.

## Phase 8: Redesign high-value interactions

Focus on customer experience, business agility and major operational pain.

## Phase 9: Validate through shadow and controlled cutover

Use golden datasets and reconciliation.

## Phase 10: Decommission deliberately

Remove old infrastructure only after evidence-based completion.

## A strong first pilot

A useful pilot could modernize one inbound customer-order file.

### Current state

- customer sends a CSV file every hour;
- integration script maps customer material numbers;
- SAP order creation occurs through an existing interface;
- errors are sent by email;
- customers receive no transaction-level status.

### Pilot objective

Improve operability and consumer experience without changing SAP order processing immediately.

### New design

1. Keep the existing SAP order-creation mechanism.
2. Move file receipt to managed secure transfer.
3. validate file manifest, schema and totals.
4. split records into individual tracked transactions.
5. preserve customer order references.
6. send valid orders through the existing SAP mechanism.
7. expose processing status through a portal or API.
8. create structured exceptions instead of generic email.
9. reconcile customer records, SAP orders and rejects.

### What remains

- file-based customer channel;
- existing SAP business processing;
- approved customer-material mappings.

### What changes

- security;
- traceability;
- transaction-level visibility;
- error handling;
- reconciliation;
- support.

### Future option

A customer may later move to an order-submission API without forcing an immediate SAP backend rewrite.

This is practical modernization.

## Metrics that matter

## Interfaces retired

How many unused flows were removed before migration?

## Business capabilities consolidated

How many duplicate interfaces were replaced by shared contracts?

## Migration reuse rate

How much proven logic or content was retained deliberately?

## Redesign rate

Which percentage of interfaces received real business redesign rather than technical conversion?

## Cutover reconciliation accuracy

Did old and new paths produce equivalent business outcomes?

## Duplicate-transaction rate

Did migration create repeated orders, invoices or postings?

## Post-migration incident rate

Did operational quality improve?

## Error-resolution time

Are new errors easier to classify and correct?

## Consumer onboarding time

Can new consumers use stable contracts more quickly?

## Legacy-runtime reduction

Has the organization actually reduced old platform cost and risk?

## Mapping duplication

How many repeated mappings remain after modernization?

## Business monitoring coverage

Can the organization prove end-to-end completion?

## Common mistakes

## Mistake 1: Declaring every IDoc obsolete

Maturity and business fit matter more than protocol fashion.

## Mistake 2: Converting every file into a synchronous API

Batch may remain the correct interaction model.

## Mistake 3: Copying the old message structure into JSON

The protocol changes while coupling remains.

## Mistake 4: Treating migration inventory as business analysis

Technical objects do not explain business purpose.

## Mistake 5: Rewriting undocumented logic without classifying it

Valid business rules may be lost.

## Mistake 6: Migrating unused interfaces

The programme pays to preserve dead complexity.

## Mistake 7: Calling rehosting transformation

Platform modernization and process redesign are different.

## Mistake 8: Running old and new writers in parallel

Duplicate business transactions can be created.

## Mistake 9: Comparing only payloads

The target business outcome may differ.

## Mistake 10: Ignoring in-flight transactions at cutover

The same transaction may be lost or processed twice.

## Mistake 11: Decommissioning before a peak business cycle

Rare but critical processes remain untested.

## Mistake 12: Keeping dual platforms permanently

Migration cost becomes permanent operating cost.

## Mistake 13: Moving flows without migrating support procedures

The new platform enters production without operational ownership.

## Mistake 14: Assuming prebuilt content removes design work

Standard content must still fit the actual business contract.

## Mistake 15: Measuring success by number of interfaces converted

The real outcomes are lower risk, cost and coupling.

## Questions architects and managers should ask

1. Is this interface still used?
2. Which business capability does it support?
3. Is the current interaction genuinely batch, asynchronous or real time?
4. What does the existing logic actually do?
5. Which rules are valid, obsolete or accidental?
6. Can the interface be retired instead of migrated?
7. Does the business need redesign or only a new runtime?
8. Can new consumers be protected through a facade?
9. Which standard APIs, events or integration content are available?
10. How will business identity be preserved?
11. How will old and new outputs be compared?
12. Can transactions be duplicated during cutover?
13. What happens to messages already in flight?
14. How is end-to-end business completion reconciled?
15. Which support procedures must move with the interface?
16. When can the old runtime actually be decommissioned?
17. Does the migration reduce future change cost?
18. Are we simplifying the landscape or repainting it?

## Modernization should remove uncertainty, not working capability

SAP currently presents Integration Suite as a secure iPaaS supporting application integration, APIs, events, B2B, hybrid environments and agentic scenarios. It also provides prebuilt content, centralized governance, real-time monitoring and migration support for customers moving from older integration platforms.

These capabilities create a strong modernization platform.

They do not make every legacy interface a redesign candidate.

A good integration-modernization programme is selective.

It removes dead interfaces.

It keeps reliable patterns where they still fit.

It improves security and operations.

It places stable contracts around legacy systems.

It redesigns only where business value justifies the change.

The best result is not a landscape with zero IDocs and zero files.

It is a landscape where every integration has a deliberate reason to exist, a controlled business contract and a practical path for future change.

That is modernization.

Rewriting everything is only one way to spend money.

---

## SAP legacy-integration modernization checklist

- [ ] Every interface has a confirmed business purpose.
- [ ] Inactive and unused flows are retired before migration.
- [ ] Interfaces are classified as retain, retire, rehost, replatform, wrap, redesign, replace or consolidate.
- [ ] Business contracts are extracted from technical implementations.
- [ ] Existing rules are classified as valid, obsolete or accidental.
- [ ] Protocol age is not used as the only modernization criterion.
- [ ] Stable IDocs are retained where they remain appropriate.
- [ ] File interfaces remain where batch behaviour is justified.
- [ ] New consumers do not depend unnecessarily on legacy structures.
- [ ] Anti-corruption layers have clear scope and lifecycle.
- [ ] External and internal business identifiers remain correlated.
- [ ] Technical acceptance is separated from business completion.
- [ ] Mapping logic is governed before being reused.
- [ ] Prebuilt SAP content is assessed before custom rebuild.
- [ ] Common monitoring, security and error patterns are established first.
- [ ] Shadow processing is used where practical.
- [ ] Parallel processing cannot create duplicate business effects.
- [ ] Golden datasets cover common and difficult historical scenarios.
- [ ] Comparison validates business results, not only payloads.
- [ ] In-flight transactions have a cutover strategy.
- [ ] Rollback covers messages and business documents already created.
- [ ] Decommissioning includes peak-cycle and reconciliation evidence.
- [ ] Coexistence states have owners and end dates.
- [ ] Support procedures migrate with technical flows.
- [ ] Success is measured through lower risk, cost and coupling.

## Sources and further reading

SAP currently positions SAP Integration Suite as a cloud integration platform spanning application and process integration, APIs, events, B2B, hybrid connectivity and agentic integration scenarios. SAP states that the platform supports SAP and third-party applications through prebuilt integrations, adapters, APIs and event-based connectivity, with centralized governance, monitoring and security.

SAP currently describes Cloud Integration as supporting A2A, B2B and B2G integration flows, prebuilt integration content, mapping recommendations, AI-generated flow drafts and migration from older integration tools such as SAP Process Orchestration. Its edge integration cell provides an option to run centrally managed integrations in private-cloud or on-premises environments.

SAP’s current migration guidance for moving from SAP Process Orchestration to Integration Suite emphasizes phased modernization, assessment, migration planning, reuse of existing integration artifacts, testing and maintaining continuity for business-critical processes.

*Reviewed: July 2026. SAP Integration Suite capabilities, migration tools, adapters, packaging and deployment options can change. Modernization decisions should be validated against current SAP documentation, platform support terms and the operational behaviour of the actual interfaces.*
