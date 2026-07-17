# Centralized or Federated SAP Integration Architecture: How to Divide Ownership Without Creating Chaos

A global company introduces one central integration platform.

The objective is reasonable:

- reduce duplicate tools;
- standardize security;
- improve monitoring;
- reuse integration patterns;
- control interfaces across countries and business units.

All new integrations must be delivered by the central integration team.

At first, quality improves.

The team creates common naming rules, templates, logging and deployment processes.

Then demand grows.

Every SAP project, cloud application, partner onboarding and local regulatory change enters the same queue.

The central team must understand:

- sales;
- procurement;
- finance;
- warehousing;
- manufacturing;
- HR;
- master data;
- regional legal requirements.

Delivery slows down.

Business teams begin bypassing the central process. Local developers create direct APIs, automation scripts, spreadsheet transfers and shadow middleware flows.

The company now has both centralization and fragmentation.

The opposite approach can fail just as badly.

Each domain or country receives freedom to build its own integrations. Teams move quickly, but they create:

- different API conventions;
- duplicated customer mappings;
- incompatible event schemas;
- separate monitoring;
- different security controls;
- several versions of the same business rule.

The issue is not whether architecture should be centralized or decentralized.

The real question is:

> Which integration responsibilities should be centralized, and which must remain with the business domains that understand their meaning?

A strong modern SAP integration model is normally federated.

It centralizes the platform, security, standards and visibility.

It distributes ownership of business semantics, APIs, events and domain decisions.

SAP currently presents Integration Suite as a unified platform for connecting applications, processes, data, APIs, events, partners and AI agents across SAP and third-party environments. The platform includes centralized governance, monitoring and security while supporting cloud, on-premises and hybrid landscapes.

Centralized platform capability does not require centralized ownership of every business decision.

## Integration architecture has two different problems

Organizations often mix two questions.

### Platform question

How should integrations be built, secured, deployed and operated?

### Business architecture question

What does the integration mean, which domain owns it and which result must it produce?

The platform question benefits from standardization.

The business architecture question requires domain knowledge.

A platform team can determine:

- how an API is authenticated;
- how logs are structured;
- how secrets are stored;
- how an integration flow is deployed;
- how queues are monitored;
- how schema versions are registered.

It should not independently determine:

- which sales organization applies to an order;
- whether two suppliers represent the same legal entity;
- which customer receives constrained stock;
- which payment term is commercially permitted;
- what “available inventory” means to the sales process.

Those decisions belong to business domains.

The failure occurs when one team is expected to own both layers simply because it operates the integration technology.

## Centralized runtime is not centralized architecture

A company may use one strategic platform for:

- application integration;
- API management;
- event distribution;
- B2B connectivity;
- monitoring;
- governance.

This can reduce operational fragmentation.

But the integration assets running on that platform may still belong to different domains.

For example:

- order API belongs to the sales domain;
- supplier-approved event belongs to supplier governance;
- payment-status API belongs to finance;
- warehouse-confirmation event belongs to fulfilment.

The central platform team may operate the infrastructure.

It does not automatically own the meaning or lifecycle of these contracts.

This distinction should be formal.

Otherwise, the platform team becomes the default owner whenever something is difficult to classify.

## The platform team should own the integration control plane

A useful architecture separates the **control plane** from the **business contracts and processes**.

The control plane provides the shared environment in which integration assets are governed.

Its responsibilities can include:

- platform provisioning;
- tenant and environment strategy;
- connectivity;
- identity integration;
- certificates and secrets;
- deployment pipelines;
- runtime policies;
- common logging;
- monitoring integration;
- API gateway controls;
- event infrastructure;
- development templates;
- catalogues;
- technical standards;
- platform cost management.

SAP currently describes API Management as providing enterprise security policies, centralized controls, API analytics and lifecycle governance. Developer Hub provides centralized API discovery, testing and onboarding, while SAP’s current API capabilities also include governed MCP-server lifecycle management for agent access.

These are natural control-plane capabilities.

They should be available consistently across the enterprise.

## Domains should own the integration products

Domain ownership should include:

- API purpose;
- event semantics;
- data definitions;
- business validation;
- error meaning;
- permitted operations;
- service expectations;
- compatibility decisions;
- consumer relationships;
- business-level support.

For example, the sales domain should own the meaning of:

```text
Submit Customer Order
```

The platform team can define how the API is secured and published.

The sales domain must define:

- what constitutes a valid order;
- which information is mandatory;
- when the order is accepted;
- which errors are commercial;
- which order states are exposed;
- what happens after acceptance.

Without domain ownership, the API may be technically stable but semantically unreliable.

## A federated model is not unrestricted decentralization

Federation is often misunderstood as:

> Every team can use the platform however it wants.

That is decentralization without architecture.

A real federated model has three elements:

1. shared platform and mandatory controls;
2. distributed domain ownership;
3. transparent governance and accountability.

Domains receive autonomy inside defined boundaries.

They do not receive permission to create:

- arbitrary protocols;
- undocumented schemas;
- broad technical users;
- unowned APIs;
- private mapping tables;
- business events without versioning;
- integrations with no monitoring.

Federation works through guardrails, not through the absence of rules.

## What should normally be centralized

Several integration responsibilities benefit strongly from central ownership.

## 1. Platform selection and lifecycle

The organization should not allow every domain to introduce a different integration platform for the same general purpose without a strong reason.

A central platform strategy can reduce:

- licensing duplication;
- skills fragmentation;
- security variation;
- inconsistent monitoring;
- deployment complexity.

SAP currently positions Integration Suite as supporting application and process integration, APIs, event-driven integration, B2B, hybrid integration and agentic scenarios within one platform family.

This breadth can simplify the platform portfolio.

It does not mean every integration pattern must be forced into one runtime.

## 2. Identity and security foundations

Central responsibilities should include:

- identity-provider integration;
- certificate policies;
- credential storage;
- token standards;
- privileged-access controls;
- network connectivity;
- audit requirements;
- encryption standards.

A domain team should not create its own weaker authentication model because the project deadline is short.

## 3. Development and deployment standards

Shared standards should cover:

- source control;
- branching;
- code review;
- automated testing;
- environment promotion;
- rollback;
- artifact naming;
- release evidence.

These controls improve reliability without defining business semantics.

## 4. Common observability

The enterprise needs a consistent way to see:

- integration executions;
- API traffic;
- event flows;
- queue backlogs;
- certificate expiry;
- failed messages;
- correlation IDs.

SAP states that Integration Suite provides centralized governance, real-time monitoring and built-in security across distributed integration scenarios.

A shared technical observability foundation is appropriate.

Business monitoring still needs domain context.

## 5. Integration catalogues

The organization should maintain searchable catalogues for:

- interfaces;
- APIs;
- events;
- mappings;
- partners;
- owners;
- versions;
- lifecycle status.

Discovery should not depend on knowing which consultant created an interface five years ago.

## 6. Approved architecture patterns

The central architecture function should define patterns for:

- synchronous APIs;
- asynchronous commands;
- business events;
- bulk files;
- B2B;
- long-running workflow;
- master data distribution;
- analytical replication.

Teams should reuse these patterns rather than reinventing basic failure and security behaviour.

## 7. Shared technical components

Reusable components may include:

- correlation framework;
- error envelope;
- file manifest;
- idempotency service;
- schema validation;
- logging adapter;
- alerting integration;
- partner acknowledgement;
- common connectors.

These components should solve technical problems.

They should not embed one domain’s business policy and then force it on others.

## What should normally be federated

Some responsibilities cannot be owned effectively by a central integration team.

## 1. Business semantics

The domain should define what its objects and events mean.

For example:

- sales defines order confirmation;
- procurement defines supplier approval;
- finance defines posted receivable;
- warehouse defines goods movement completion.

A central team can challenge inconsistent definitions.

It cannot invent them.

## 2. API product ownership

A business API should have an owner close to the capability it exposes.

That owner decides:

- roadmap;
- consumer needs;
- compatibility;
- deprecation;
- business service level.

## 3. Event ownership

The publishing domain should own:

- event meaning;
- commit point;
- schema;
- object version;
- correction events;
- compatibility.

The event platform team owns delivery infrastructure.

It should not define what `Delivery.Completed` means.

## 4. Mapping semantics

Technical transformation can be centralized.

Semantic equivalence must be approved by the owning domains.

For example:

```text
External Supplier Type: Preferred
→ SAP Supplier Classification: Strategic
```

This is not an integration-team decision.

It may affect:

- procurement policy;
- approval;
- reporting;
- supplier management.

## 5. Business error handling

The domain should define whether an error means:

- retry;
- input correction;
- approval;
- cancellation;
- manual investigation.

A central technical team can standardize the error format.

It cannot determine the correct business response for every process.

## 6. Business reconciliation

The domain or end-to-end process owner should define what proves completion.

For an order flow, technical message delivery is not enough.

The business may need to prove:

- order created;
- quantity confirmed;
- fulfilment request accepted;
- invoice produced.

## The hardest responsibility: end-to-end process ownership

Domain ownership alone is not enough.

Processes cross domains.

Consider order to cash:

- customer domain;
- sales;
- pricing;
- inventory;
- fulfilment;
- billing;
- finance.

Each domain may perform its part correctly.

The customer order may still fail end to end.

The architecture therefore needs an **end-to-end process owner**.

This role should own:

- business outcome;
- cross-domain service expectations;
- critical dependencies;
- exception priorities;
- reconciliation;
- operational recovery.

The process owner does not own every application or API.

The role owns whether the complete business service works.

## Platform ownership, domain ownership and process ownership are different

A practical responsibility model can be expressed like this:

| Responsibility | Primary owner |
|---|---|
| Integration runtime | Platform team |
| API security policy | Platform/security team |
| Order API semantics | Sales domain |
| Order-created event | Sales domain |
| Customer mapping meaning | Customer/data domain |
| Structural transformation | Integration engineering |
| End-to-end order fulfilment | Order-to-cash process owner |
| Warehouse processing | Fulfilment domain |
| Business reconciliation | Process owner with domains |
| API discovery catalogue | Platform governance |
| API version retirement | Domain owner with platform governance |

The architecture becomes unstable when all rows point to one central integration team.

## Build a platform team, not an integration factory

A traditional central integration team often operates as a factory.

Projects submit requirements.

The team analyses, develops and deploys every interface.

This model may work for a small landscape.

At scale, it creates:

- long queues;
- excessive handovers;
- weak domain knowledge;
- little ownership after project completion;
- dependence on a few specialists.

A platform operating model is different.

The platform team provides:

- environments;
- templates;
- reusable components;
- guardrails;
- self-service;
- expert support;
- complex pattern assistance;
- governance automation.

Domain teams can deliver approved integrations themselves or through embedded integration engineers.

The central team enables delivery rather than monopolizing it.

## Self-service requires stronger controls, not fewer controls

Self-service may allow domain teams to:

- create API proxies;
- deploy integration flows;
- register schemas;
- subscribe to events;
- onboard partners;
- access reusable templates.

This works only when controls are built into the platform.

Examples include:

- mandatory metadata;
- automated security scanning;
- naming validation;
- owner assignment;
- contract testing;
- deployment approval;
- monitoring configuration;
- lifecycle review.

Manual architecture review should focus on high-impact decisions.

Routine compliance should be automated.

## Use a paved road

A paved road is the recommended and easiest way to deliver an integration.

It may provide:

- repository template;
- deployment pipeline;
- logging;
- error handling;
- API policies;
- documentation structure;
- test harness;
- monitoring dashboard;
- catalogue registration.

Teams can leave the paved road when they have a justified requirement.

The alternative should require an explicit architecture decision.

The goal is not to prohibit variation.

It is to make the safe pattern easier than the unsafe shortcut.

## Do not centralize every mapping

A central mapping repository can improve visibility.

A central mapping team for every transformation can become a bottleneck.

Mappings should be classified.

### Shared reference mappings

Examples:

- country codes;
- currencies;
- organizational identifiers;
- partner IDs.

These may require central governance.

### Domain mappings

Examples:

- supplier classification;
- product hierarchy;
- order status.

These should be owned by domains.

### Partner-specific mappings

These may be implemented in B2B integration under a stable internal contract.

### Technical mappings

Examples:

- date format;
- boolean conversion;
- protocol structure.

These can be owned by integration engineering.

The registry can be central.

The semantic ownership should remain distributed.

## A central canonical model is not a substitute for federation

Some organizations attempt to solve ownership conflict through one enterprise canonical data model.

The model includes all possible fields for:

- customer;
- supplier;
- product;
- order;
- invoice.

Every system maps to it.

The model then requires a central committee to approve every field.

This often creates:

- slow changes;
- hundreds of optional attributes;
- unclear definitions;
- constant extensions;
- system-specific logic hidden inside the “enterprise” model.

A federated architecture prefers bounded domain contracts.

Examples include:

- customer identity contract;
- order fulfilment contract;
- supplier approval event;
- invoice-posting event.

Common definitions should be shared where meaning is genuinely common.

They should not be forced into one universal object.

## Domain contracts should be treated as products

An API or event should not be treated as a project deliverable that becomes nobody’s responsibility after go-live.

A product model includes:

- named owner;
- intended consumers;
- support;
- roadmap;
- service objective;
- usage metrics;
- version policy;
- deprecation;
- documentation;
- feedback.

The product does not need a commercial price.

It needs lifecycle accountability.

## API governance should not become approval theatre

A governance process may require:

- architecture form;
- security checklist;
- naming review;
- approval meeting;
- documentation upload.

Teams complete the process.

The actual API may still expose internal SAP structures and weak error semantics.

Good governance should test architecture quality.

For a new API, ask:

1. What business capability does it expose?
2. Which domain owns it?
3. Why is it synchronous?
4. Can repeated requests create duplicate effects?
5. Does it expose unnecessary backend codes?
6. How is final business completion determined?
7. How will consumers migrate to a new version?
8. Who supports it after go-live?

These questions matter more than whether the URL follows one naming pattern.

## Event governance needs consumer transparency

The publisher should not need to know every runtime consumer.

The organization should still know:

- which business capabilities depend on the event;
- which consumers are mandatory;
- what delay they tolerate;
- which schema versions they use;
- who supports them.

SAP describes event-driven capabilities as supporting asynchronous distribution, loose coupling and centralized visibility into event flows.

Loose coupling helps consumers evolve independently.

It does not remove operational dependency.

## Separate event infrastructure from event ownership

The central platform team may own:

- brokers;
- topic provisioning;
- access policies;
- retention controls;
- monitoring;
- schema registry.

The domain should own:

- event name;
- business fact;
- payload semantics;
- publication point;
- object version;
- correction model.

For example, the platform can guarantee that a message is distributed according to the configured service.

Only the finance domain can define when an invoice is considered posted.

## Integration engineering should become a distributed capability

A federated model does not eliminate integration specialists.

It changes where they work.

Possible arrangements include:

- central platform engineers;
- domain integration engineers;
- embedded architects;
- community of practice;
- shared expert pool.

Domain integration engineers understand:

- business objects;
- local applications;
- process dependencies;
- domain errors.

Platform engineers understand:

- runtime;
- connectivity;
- security;
- deployment;
- resilience;
- observability.

Both capabilities are required.

A business analyst should not be expected to design idempotent event consumers alone.

A platform specialist should not define procurement semantics alone.

## Create an integration community of practice

A community of practice can connect distributed teams.

Its responsibilities may include:

- sharing patterns;
- reviewing difficult designs;
- improving templates;
- discussing incidents;
- maintaining examples;
- aligning naming and semantics;
- developing skills.

The community should not become another approval board.

Its value is in improving shared capability.

## Architecture governance needs decision rights

Federation fails when responsibilities are collaborative but nobody has final authority.

For each decision type, define who:

- proposes;
- approves;
- implements;
- operates;
- can make an exception.

Example:

| Decision | Authority |
|---|---|
| New integration platform | Enterprise architecture |
| New business API | Domain owner |
| API security policy | Security/platform |
| Breaking API change | Domain owner with consumer review |
| New business event | Publishing domain |
| Shared customer code mapping | Customer-data owner |
| Partner-specific format | B2B integration team |
| Architecture-pattern exception | Architecture authority |
| Production replay | Process owner and operations |

This removes ambiguity during delivery and incidents.

## Local autonomy needs defined limits

Global organizations often have local requirements.

Examples include:

- regulatory files;
- tax integrations;
- local banks;
- country logistics providers;
- regional customer portals.

A global central team cannot design every local detail.

Local teams may need authority to build integrations.

The architecture should define:

### Global mandatory controls

- security;
- ownership;
- catalogue registration;
- monitoring;
- data classification;
- lifecycle;
- approved runtime.

### Local design authority

- local partner format;
- country-specific business rule;
- local schedule;
- local operational support.

### Global domain contracts

Where the local process interacts with global business capabilities, it should use the global contract where practical.

This allows local variation without creating a separate enterprise architecture in every country.

## Do not force local requirements into the global core

A country-specific tax or partner requirement should not necessarily become part of the global customer or order API.

It may be better implemented through:

- local adapter;
- country service;
- bounded extension;
- partner integration.

The global contract should change only when the business meaning is genuinely global.

Otherwise, global APIs accumulate hundreds of optional local fields.

## Funding determines architecture behaviour

Organizations may define federated ownership but fund integrations only through temporary projects.

After go-live:

- project team dissolves;
- API owner changes role;
- monitoring remains with central operations;
- no budget exists for version upgrades;
- consumers continue using obsolete contracts.

Integration products need ongoing funding for:

- support;
- maintenance;
- security;
- compatibility;
- documentation;
- monitoring;
- deprecation.

Without lifecycle funding, “product ownership” is only a title.

## Chargeback models can create bad incentives

A central platform may charge every domain for:

- messages;
- API calls;
- runtime;
- development effort.

Transparent cost is useful.

Poor chargeback can encourage teams to:

- bypass the platform;
- combine unrelated messages;
- avoid monitoring;
- retain local tools.

Cost allocation should support good architecture.

It should not make unsafe shortcuts financially attractive.

## Measure total integration cost

The cost of an integration includes more than development.

It includes:

- platform consumption;
- support;
- incidents;
- mapping maintenance;
- certificate renewal;
- consumer onboarding;
- version migration;
- business reconciliation;
- architectural review;
- partner coordination.

A reusable contract may cost more initially but reduce the cost of every new consumer.

A central one-off flow may appear cheap but create permanent dependence on the integration team.

## The platform team should publish service levels

Domains need to know what the integration platform provides.

Examples include:

- platform availability;
- deployment support;
- incident response;
- certificate management;
- monitoring retention;
- broker retention;
- API gateway capacity;
- environment provisioning time.

The domain contract may have its own higher or lower service level.

Platform availability and business API availability are related but not identical.

## Domain teams must publish service expectations too

An API provider should state:

- supported hours;
- response targets;
- throughput;
- data freshness;
- maintenance process;
- escalation;
- consumer notification.

An event publisher should state:

- expected publication delay;
- retention;
- ordering model;
- replay policy;
- compatibility.

Federation requires contracts between teams, not only between applications.

## Centralized monitoring needs distributed response

A central operations centre may detect:

- failed flow;
- rising event lag;
- API errors;
- expired certificate.

It may not understand the business correction.

A good incident model routes based on cause.

### Platform failure

Examples:

- runtime unavailable;
- network failure;
- broker issue;
- shared certificate problem.

Owner:

- platform team.

### Integration implementation failure

Examples:

- transformation error;
- technical routing;
- adapter defect.

Owner:

- integration engineering.

### Domain business failure

Examples:

- customer blocked;
- unknown supplier category;
- invalid price;
- unavailable stock.

Owner:

- business domain.

### End-to-end process failure

Examples:

- order accepted but warehouse not reached;
- supplier approved but unusable in target;
- goods issue completed but invoice missing.

Owner:

- process owner coordinating domains.

Central monitoring should accelerate routing.

It should not turn the platform team into the resolver for every business exception.

## Incidents expose ownership quality

A practical test of the operating model is:

> When one transaction fails, how many teams must discuss it before an owner is found?

High transfer rates indicate:

- weak domain boundaries;
- generic alerts;
- unclear contracts;
- missing process ownership.

Architecture metrics should include incident routing and transfer, not only message uptime.

## Replay authority must be distributed carefully

Replaying a message can create a business effect.

The platform team may have technical ability to replay.

It should not always have business authority.

For example:

- replaying a product-description update may be low risk;
- replaying an order, payment or goods movement may create duplicates or financial consequences.

A replay policy should define:

- technical operator;
- business approver;
- duplicate checks;
- scope;
- verification;
- audit.

The same principle applies to automated recovery.

Technical ability does not equal business authority.

## AI agents increase the need for federation

AI agents may consume:

- APIs;
- events;
- documents;
- monitoring signals.

They may prepare or execute actions across several domains.

SAP’s current API lifecycle capabilities include the ability to expose curated APIs as governed MCP servers, apply design-time and runtime controls and monitor agent activity.

This can centralize technical governance.

It does not give one central AI team ownership of every business action.

Each domain should decide:

- which capabilities are available to agents;
- which data is exposed;
- which actions are read-only;
- which actions require approval;
- which thresholds apply;
- how results are verified.

## Do not expose the platform catalogue directly as an agent toolbox

An API may be safe for a deterministic application with tightly controlled inputs.

It may be unsafe for probabilistic agent use.

Agent-facing tools should be:

- bounded;
- purpose-specific;
- well described;
- auditable;
- limited by business authority.

For example, avoid giving an agent generic access to:

```text
Update Business Partner
```

Prefer:

```text
Prepare Supplier Bank Change for Verification
```

The platform team can standardize agent-tool exposure.

The supplier and finance domains must own the action semantics.

## Federated architecture needs a shared vocabulary

Teams cannot own contracts independently if they use incompatible meanings.

The organization needs common definitions for important concepts such as:

- customer;
- supplier;
- product;
- order;
- delivery;
- invoice;
- business event;
- acceptance;
- completion;
- cancellation.

This does not require one universal data model.

It requires explicit semantic alignment where domains interact.

A term catalogue or domain glossary can support this.

## Use bounded contexts to manage different meanings

The same word may legitimately mean different things in different domains.

For example, “customer” may mean:

- legal party;
- sold-to party;
- service subscriber;
- billing account;
- marketing contact.

The architecture should not force these into one vague object.

It should define the context.

An integration contract should state which meaning it uses.

Federation becomes manageable when boundaries and translations are explicit.

## Create one architecture decision process

Teams should know when they can proceed independently and when broader review is required.

### Domain-level decision

May be sufficient when:

- one domain is affected;
- approved patterns are used;
- no shared contract changes;
- risk is limited.

### Cross-domain review

Required when:

- shared API changes;
- event semantics change;
- new canonical contract is introduced;
- authority moves between systems;
- several domains are affected.

### Enterprise review

Required when:

- new platform is proposed;
- strategic security model changes;
- major exception to architecture standards;
- regulatory or company-wide risk exists.

This prevents both over-governance and uncontrolled change.

## Automate governance evidence

A deployment pipeline can check:

- owner metadata exists;
- API contract is registered;
- version policy is defined;
- security tests pass;
- monitoring is configured;
- schema compatibility is checked;
- documentation exists;
- production support is assigned.

Architecture governance should move left into delivery.

A committee should not manually check every technical detail that a pipeline can validate.

## Governance automation cannot assess semantic quality alone

A pipeline can confirm that an event has:

- version;
- schema;
- owner;
- documentation.

It cannot prove that the event represents the correct business fact.

Semantic review remains a domain responsibility.

This is the recurring principle:

> Automate compliance. Assign meaning.

## A reference federated operating model

A practical structure may include five groups.

## 1. Integration platform team

Owns:

- Integration Suite platform;
- API gateway;
- event infrastructure;
- connectivity;
- shared monitoring;
- CI/CD;
- templates;
- cost transparency.

## 2. Enterprise integration architecture

Owns:

- principles;
- approved patterns;
- reference architectures;
- strategic platform boundaries;
- exception decisions;
- portfolio coherence.

SAP currently positions Integration Assessment and the SAP Integration Solution Advisory Methodology as structured approaches for assessing architectures, applying reference designs and embedding standards and governance.

These methods can support this function.

## 3. Domain integration teams

Own:

- APIs;
- events;
- domain mappings;
- business validation;
- consumer support;
- domain service levels.

## 4. End-to-end process owners

Own:

- business outcome;
- cross-domain dependency;
- reconciliation;
- service priorities;
- major process incidents.

## 5. Integration operations

Owns:

- production monitoring;
- first response;
- platform runbooks;
- incident coordination;
- technical recovery within authority.

These roles can be implemented through existing teams.

The important part is the responsibility split.

## A practical responsibility matrix

| Activity | Platform | Domain | Process owner | Architecture |
|---|---:|---:|---:|---:|
| Provision runtime | A/R | C | I | C |
| Define API semantics | C | A/R | C | C |
| Define event semantics | C | A/R | C | C |
| Configure API security | A/R | C | I | C |
| Define business mapping | C | A/R | C | C |
| Build structural mapping | R | A/C | I | I |
| Define reconciliation | C | R | A | C |
| Operate platform | A/R | I | I | I |
| Resolve business exception | C | A/R | C | I |
| Approve architecture exception | C | C | C | A/R |
| Retire API version | R | A | C | C |
| Approve high-risk replay | R | C | A | I |

`A` means accountable.
`R` means responsible.
`C` means consulted.
`I` means informed.

The exact matrix may differ.

What matters is that accountability is explicit.

## A strong pilot for federation

Do not begin by reorganizing the entire integration department.

Select one domain, such as order management.

## Pilot scope

- one order API;
- two consuming channels;
- one order-created event;
- one warehouse integration;
- one end-to-end reconciliation flow.

## Platform responsibilities

- API publication;
- authentication;
- quotas;
- deployment pipeline;
- event topic;
- monitoring;
- catalogue.

## Sales-domain responsibilities

- order contract;
- validation;
- error semantics;
- event meaning;
- version roadmap;
- consumer support.

## Fulfilment responsibilities

- warehouse command contract;
- acceptance;
- fulfilment events;
- processing service level.

## Process-owner responsibilities

- order-to-fulfilment completion;
- exception priorities;
- reconciliation;
- release decision.

## Architecture responsibilities

- pattern review;
- domain boundary;
- synchronous versus asynchronous decisions;
- reuse and lifecycle.

## Pilot success criteria

- new consumer can onboard without direct SAP knowledge;
- domain team can change implementation without breaking consumers;
- platform controls are applied automatically;
- business exception reaches the correct owner;
- one transaction is traceable end to end;
- no central development queue is required for every change.

## How to scale the model

## Phase 1: Define responsibilities

Agree what belongs to platform, domains and process owners.

## Phase 2: Build the platform paved road

Provide templates, pipelines, monitoring and catalogues.

## Phase 3: Select mature domains

Begin with domains that have:

- clear ownership;
- stable capabilities;
- active product teams;
- meaningful integration demand.

## Phase 4: Assign API and event owners

Do not migrate assets without assigning lifecycle responsibility.

## Phase 5: Establish communities of practice

Share patterns and incident lessons across domains.

## Phase 6: Automate governance checks

Move routine controls into pipelines and catalogues.

## Phase 7: Introduce business reconciliation

Ensure process owners can see cross-domain completion.

## Phase 8: Measure bottlenecks and duplication

Identify where centralization or decentralization is producing waste.

## Phase 9: Adjust decision rights

Federation is an operating model that needs tuning.

## Phase 10: Extend to agent integration

Expose only governed domain capabilities to AI agents.

## Metrics that reveal whether federation works

## Central delivery queue time

How long do domains wait for the central integration team?

A falling queue may indicate successful enablement.

It may also indicate uncontrolled bypassing, so compare it with governance compliance.

## Domain-owned contract rate

What percentage of business APIs and events has a real domain owner?

## Unknown-owner rate

How many active integration assets lack accountable ownership?

## Reuse without forks

How many consumers use the same contract without consumer-specific variants?

## Architecture compliance

How many integrations use approved patterns?

## Exception volume

How many projects require architecture exceptions?

High volume may mean the standards do not fit actual needs.

## Consumer onboarding time

Can a new application discover, understand and access a capability quickly?

## Business-logic duplication

How many domains or integration flows implement the same rule?

## Incident transfer rate

How often are incidents moved between platform, domain and business teams?

## End-to-end reconciliation coverage

What percentage of critical processes can prove completion across domains?

## API version retirement time

Can domains actually remove obsolete versions?

## Self-service success rate

How many integrations are delivered through the paved road without central custom development?

## Platform bypass rate

How many unregistered scripts, direct connections and local tools exist?

## Common mistakes

## Mistake 1: Centralizing all integration development

The central team becomes a bottleneck and a weak owner of domain semantics.

## Mistake 2: Decentralizing without mandatory controls

Every domain creates its own platform conventions and security model.

## Mistake 3: Treating the platform team as the business owner

Runtime ownership is confused with semantic ownership.

## Mistake 4: Assigning an API owner only on paper

No capacity or funding exists for support and lifecycle work.

## Mistake 5: Building self-service without a paved road

Teams receive access but no safe default patterns.

## Mistake 6: Forcing every local requirement into global APIs

Global contracts become oversized and unstable.

## Mistake 7: Creating one central mapping team

Semantic decisions wait in another central queue.

## Mistake 8: Letting domains create private mappings

Shared values become inconsistent across processes.

## Mistake 9: Governing naming but not business behaviour

The API path looks standard while semantics remain poor.

## Mistake 10: Assuming event consumers are optional because they are loosely coupled

Some consumers are mandatory for business completion.

## Mistake 11: Allowing the platform team to replay high-risk transactions independently

Technical access bypasses business authority.

## Mistake 12: Exposing all enterprise APIs to AI agents

The agent receives capabilities designed for a different trust model.

## Mistake 13: Measuring the number of integrations delivered

Speed may increase while duplication and operational risk grow.

## Mistake 14: Forgetting the end-to-end process owner

Domains optimize their components while the complete service fails.

## Questions managers and architects should ask

1. Which responsibilities are centralized today?
2. Which of them require business-domain knowledge?
3. Is the central integration team a platform team or a delivery factory?
4. Who owns each API and event after the project ends?
5. Who owns mapping semantics?
6. Which controls can be automated in the delivery pipeline?
7. Can domain teams use a safe self-service path?
8. Which decisions require cross-domain review?
9. Are local requirements separated from global business contracts?
10. Who owns end-to-end process completion?
11. Can incidents be routed without several team transfers?
12. Who can authorize message replay?
13. How are obsolete API and event versions retired?
14. Are platform costs visible without encouraging bypass?
15. Do domain teams have capacity for lifecycle ownership?
16. Are AI-agent capabilities governed by the domains whose actions they expose?
17. Is the model reducing bottlenecks without increasing inconsistency?

## The goal is centralized control without centralized meaning

A company needs a coherent integration platform.

It also needs business domains that can change without waiting for one central team to understand every process.

These objectives are not contradictory.

The right operating model centralizes:

- infrastructure;
- security;
- standards;
- visibility;
- deployment controls;
- reusable technical capabilities.

It federates:

- business semantics;
- APIs;
- events;
- mappings;
- business errors;
- domain lifecycle decisions.

End-to-end process owners connect the domains and remain accountable for the complete result.

SAP’s current integration portfolio combines centralized governance and runtime visibility with capabilities for APIs, events, application integration, B2B and agent access. SAP’s Integration Assessment and advisory methodology are positioned as ways to align integration architecture with business goals, reference architectures and long-term adaptability.

The technology can support either a centralized or federated operating model.

The organization decides which one it actually creates.

A centralized platform should not become a centralized brain.

A federated model should not become a collection of independent technical kingdoms.

The strongest architecture creates one controlled integration ecosystem in which business meaning remains close to the people who understand and own it.

That is how integration can scale without becoming either a bottleneck or a new form of shadow IT.

---

## Federated SAP integration architecture checklist

- [ ] Platform ownership and business ownership are explicitly separated.
- [ ] The integration platform team operates as an enablement team, not only a delivery queue.
- [ ] Core security, identity and connectivity controls are centralized.
- [ ] Development and deployment standards are shared.
- [ ] APIs and events have accountable domain owners.
- [ ] End-to-end business processes have separate process owners.
- [ ] Semantic mappings are owned by the relevant domains.
- [ ] Technical mappings remain an integration-engineering responsibility.
- [ ] Approved architecture patterns are reusable and documented.
- [ ] The paved road includes testing, monitoring and catalogue registration.
- [ ] Self-service access includes automated guardrails.
- [ ] Architecture review focuses on business and failure semantics.
- [ ] Local teams can implement local requirements within global controls.
- [ ] Global contracts do not accumulate every local field.
- [ ] API and event lifecycle work has ongoing funding.
- [ ] Platform and domain service expectations are published.
- [ ] Central monitoring routes failures to the correct owner.
- [ ] High-risk replay requires business authority.
- [ ] Event infrastructure and event semantics have different owners.
- [ ] Canonical models remain bounded by domain.
- [ ] Contract metadata and owners are machine-searchable.
- [ ] Governance evidence is automated where possible.
- [ ] Semantic quality remains a human domain responsibility.
- [ ] AI-agent tools expose bounded domain actions.
- [ ] Success is measured through lower bottlenecks, lower duplication and higher business reliability.

## Sources and further reading

SAP currently positions SAP Integration Suite as a unified integration platform connecting AI agents, applications, data and processes across SAP and third-party environments. Its current scope includes application integration, API lifecycle management, event-driven integration, B2B, centralized governance, real-time monitoring and security.

SAP currently describes API Management as providing enterprise security policies, usage and performance analytics and centralized API governance. Its API lifecycle capabilities also include Developer Hub for discovery and onboarding, Graph as a semantic access layer and governed MCP-server lifecycle management for AI-agent use.

SAP currently presents Integration Assessment as a structured method for evaluating integration readiness and identifying architecture gaps. The SAP Integration Solution Advisory Methodology is positioned as a framework for using reference architectures, development guidelines, standards and governance to create an adaptable integration discipline.

SAP currently describes its event-driven capabilities as supporting asynchronous event distribution, loose coupling, resilient processing and centralized visibility into event flows across hybrid SAP and third-party landscapes.

*Reviewed: July 2026. SAP Integration Suite capabilities, packaging and product scope can change. The operating model should be designed around the organization’s actual domain ownership, skills, regulatory obligations and support structure.*
