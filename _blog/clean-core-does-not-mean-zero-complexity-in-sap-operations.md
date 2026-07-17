---
layout: blog
title: "Clean Core Does Not Mean Zero Complexity in SAP Operations"
description: "The old logic is rebuilt as an application on SAP BTP. It uses released APIs, follows the clean core direction and no longer modifies the ERP system."
slug: clean-core-does-not-mean-zero-complexity-in-sap-operations
permalink: /blog/clean-core-does-not-mean-zero-complexity-in-sap-operations/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP AMS operations"
tags:
  - sap-ams-operations
  - sap-architecture
canonical_url: https://dkharlanau.github.io/blog/clean-core-does-not-mean-zero-complexity-in-sap-operations/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 20
migration_sequence: 8
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/why-sap-teams-keep-solving-the-same-incidents/
  - /blog/sap-ams-is-not-a-ticket-factory-what-a-better-operating-model-looks-like/
---

## On this page

- [Clean core is not “no customization”](#clean-core-is-not-no-customization)
- [The real promise of clean core](#the-real-promise-of-clean-core)
- [Complexity does not disappear](#complexity-does-not-disappear)
- [Clean core should move complexity to the right place](#clean-core-should-move-complexity-to-the-right-place)
- [Fit-to-standard is a business decision](#fit-to-standard-is-a-business-decision)
- [The hidden cost of preserving historical processes](#the-hidden-cost-of-preserving-historical-processes)
- [Removing code without removing the rule changes little](#removing-code-without-removing-the-rule-changes-little)
- [Side-by-side extensions create a second operating system](#side-by-side-extensions-create-a-second-operating-system)
- [Every extension needs an operational owner](#every-extension-needs-an-operational-owner)
- [Released APIs reduce one risk and create another dependency](#released-apis-reduce-one-risk-and-create-another-dependency)
- [Event-driven architecture does not remove failure](#event-driven-architecture-does-not-remove-failure)
- [A cleaner core can create more distributed support](#a-cleaner-core-can-create-more-distributed-support)
- [Clean core changes the role of AMS](#clean-core-changes-the-role-of-ams)
- [The “not in the core” problem](#the-not-in-the-core-problem)
- [Standardization creates organizational complexity](#standardization-creates-organizational-complexity)
- [Local requirements need expiration dates](#local-requirements-need-expiration-dates)
- [Clean core is not a one-time project](#clean-core-is-not-a-one-time-project)
- [Emergency changes are where discipline breaks](#emergency-changes-are-where-discipline-breaks)
- [Clean core must include data](#clean-core-must-include-data)
- [Clean core must include integration](#clean-core-must-include-integration)
- [Clean core must include operations](#clean-core-must-include-operations)
- [The new dependency on platform skills](#the-new-dependency-on-platform-skills)
- [The new dependency on commercial services](#the-new-dependency-on-commercial-services)
- [More frequent upgrades require better testing](#more-frequent-upgrades-require-better-testing)
- [Test the complete business service](#test-the-complete-business-service)
- [Clean core metrics can become misleading](#clean-core-metrics-can-become-misleading)
- [Better clean core metrics](#better-clean-core-metrics)
- [Every extension needs a business case](#every-extension-needs-a-business-case)
- [1. What business problem does it solve?](#1-what-business-problem-does-it-solve)
- [2. Why is standard capability insufficient?](#2-why-is-standard-capability-insufficient)
- [3. What value does the difference create?](#3-what-value-does-the-difference-create)
- [4. What is the full lifecycle cost?](#4-what-is-the-full-lifecycle-cost)
- [5. What is the exit strategy?](#5-what-is-the-exit-strategy)
- [A practical extension classification](#a-practical-extension-classification)
- [What managers should ask](#what-managers-should-ask)
- [A practical clean core operating model](#a-practical-clean-core-operating-model)
- [1. Process ownership](#1-process-ownership)
- [2. Architecture governance](#2-architecture-governance)
- [3. Product ownership](#3-product-ownership)
- [4. Operational readiness](#4-operational-readiness)
- [5. Release management](#5-release-management)
- [6. Continuous review](#6-continuous-review)
- [7. Retirement](#7-retirement)
- [A practical review of one extension](#a-practical-review-of-one-extension)
- [Clean core should reduce future friction](#clean-core-should-reduce-future-friction)
- [Clean core operations checklist](#clean-core-operations-checklist)
- [Sources and further reading](#sources-and-further-reading)

A company removes a large custom development from SAP S/4HANA.

The old logic is rebuilt as an application on SAP BTP. It uses released APIs, follows the clean core direction and no longer modifies the ERP system.

The architecture review is successful.

Six months later, the support team is responsible for:

- another application runtime;
- additional integrations;
- identity and access setup;
- API monitoring;
- application logs;
- data synchronization;
- separate deployments;
- new support skills;
- another provider.

The SAP core is cleaner.

The complete operating landscape may not be simpler.

This does not mean that clean core is a bad strategy. It means that clean core should not be confused with zero complexity.

Clean core changes where complexity is allowed, how it is controlled and who must operate it.

That is a much more useful way to understand it.

## Clean core is not “no customization”

SAP describes a clean core as an up-to-date ERP system with current releases, cloud-compliant extensions and integrations, strong master data quality and well-designed processes. SAP’s current learning material treats clean core across several areas: extensibility, processes, data, integration and operations.

This definition is broader than custom code.

A system can contain little custom ABAP and still have:

- inconsistent business processes;
- duplicated master data;
- poorly governed APIs;
- unstable external applications;
- manual workarounds;
- weak monitoring;
- unclear ownership;
- outdated integrations.

It may be technically close to standard while remaining expensive to operate.

Clean core should therefore not be treated as a code-cleaning programme.

It is an operating discipline.

## The real promise of clean core

The main idea is reasonable.

A company should be able to:

- adopt SAP updates more easily;
- reduce upgrade conflicts;
- use new product capabilities faster;
- limit technical debt;
- avoid unnecessary modifications;
- keep business differentiation where it creates value.

SAP does not say that companies should never extend the system. Its guidance is to use standard processes where possible and apply controlled extensions where differentiation is justified. SAP’s learning content explicitly says that clean core does not mean avoiding customization; it means applying it strategically while protecting system integrity and upgradeability.

This is important because companies often move toward one of two extremes.

The first extreme is:

> We are unique, so every process must be customized.

The second is:

> Clean core means the business must accept every standard process without discussion.

Both approaches are weak.

The useful question is:

> Where does variation create measurable business value, and where does it only preserve historical habits?

## Complexity does not disappear

A business requirement creates complexity even when it is implemented correctly.

Suppose a company needs a special approval process for high-risk orders.

The company can:

- modify ERP logic;
- use an in-app extension;
- use developer extensibility;
- build a side-by-side application;
- use workflow or automation;
- redesign the process to use standard functionality.

Each option creates a different type of complexity.

A core modification creates upgrade and maintenance risk.

A side-by-side application creates distributed architecture, integration and operational responsibility.

A standard process may require business change, training and local adoption.

The requirement does not disappear because the company selected a clean extension.

The complexity has been placed into a more controlled form.

## Clean core should move complexity to the right place

This is the main management value of clean core.

Not all complexity is avoidable.

Some complexity comes from:

- regulation;
- industry requirements;
- business model;
- customer commitments;
- local legal rules;
- competitive differentiation.

The goal is not to remove all of it.

The goal is to avoid putting every difference directly into the ERP core.

A strong clean core model separates:

### Commodity complexity

Work that many companies perform in a similar way.

Examples:

- standard purchasing approval;
- normal invoice processing;
- basic order entry;
- common financial posting;
- standard employee administration.

These processes should usually stay close to the product standard.

### Required complexity

Variation needed because of law, industry or contractual obligations.

This should be documented and controlled.

### Differentiating complexity

Capabilities that create measurable business value.

These may justify extension and investment.

### Accidental complexity

Variation that exists because:

- “we always did it this way”;
- an old system worked differently;
- a temporary workaround became permanent;
- a local team avoided a process decision;
- nobody removed an obsolete development.

This is the best target for removal.

## Fit-to-standard is a business decision

Fit-to-standard is often treated as a workshop method.

It is more important than that.

It changes the starting question.

The old question is:

> How can SAP reproduce our existing process?

The clean core question is:

> Why should our process differ from the standard?

SAP’s current guidance says that standard processes should be used as widely as possible and deviations should be justified by regulatory, industry or measurable differentiating needs. It also connects process governance with architecture and solution governance.

This requires business ownership.

A consultant cannot decide alone whether a process is strategically different.

An architect cannot decide whether a local exception is commercially necessary.

The process owner must explain:

- what value the difference creates;
- which risk it controls;
- how often it is used;
- what the standard process cannot provide;
- whether the benefit is larger than the lifecycle cost.

Without this discipline, clean core becomes a technical restriction rather than a business design method.

## The hidden cost of preserving historical processes

Many custom SAP processes were created for good reasons.

The problem is that those reasons may no longer exist.

A development may remain because:

- the old process owner requested it;
- documentation is missing;
- nobody wants to test its removal;
- users are familiar with it;
- another system may depend on it;
- the risk of change looks larger than the visible maintenance cost.

The code continues to run.

The company continues to pay through:

- testing;
- incident analysis;
- upgrade checks;
- regression risk;
- developer dependency;
- process training;
- integration maintenance.

This is historical process debt.

A clean core programme should not only classify technical objects.

It should ask whether the business rule is still needed.

## Removing code without removing the rule changes little

A common clean core mistake is technical relocation.

A custom rule is removed from SAP S/4HANA and rebuilt outside it.

The core becomes cleaner according to one technical measure.

But the company still owns:

- the same business exception;
- the same maintenance need;
- the same testing requirement;
- the same user training;
- the same support dependency.

It may now also own a new integration.

This can still be the correct architecture.

But it should not be presented as simplification unless the complete lifecycle becomes simpler.

Moving code is not the same as removing complexity.

## Side-by-side extensions create a second operating system

SAP describes side-by-side extensions as applications that run on SAP BTP and use released remote APIs to work with SAP S/4HANA Cloud data. These extensions may use Java, Node.js or the SAP BTP ABAP environment and can combine SAP data with other systems and platform services.

This protects the ERP core.

It also creates a new operational surface.

A side-by-side application may require:

- runtime management;
- destinations and connectivity;
- authentication;
- authorization;
- API lifecycle management;
- event or message handling;
- application monitoring;
- log management;
- deployment pipelines;
- security patching;
- cost monitoring;
- backup or recovery planning;
- support documentation.

The application may be technically separate from ERP.

The business process is not separate.

If the extension fails, users may still say:

> SAP is not working.

## Every extension needs an operational owner

Projects often assign a development owner.

Operations need more than that.

Every important extension should have:

- a business owner;
- a product owner;
- a technical owner;
- a support owner;
- a security owner;
- an integration owner.

These roles do not always require six different people.

But the responsibilities must exist.

Someone must decide:

- which changes are allowed;
- which SAP releases must be tested;
- what service level is required;
- how incidents are handled;
- how costs are controlled;
- when the extension should be retired.

Without these decisions, a side-by-side extension becomes orphaned custom code on a newer platform.

## Released APIs reduce one risk and create another dependency

Using released APIs is a central clean core principle.

It provides a supported contract between the ERP system and extensions.

This is much safer than reading internal tables or calling unstable objects.

But the API becomes part of the business service.

The company now depends on:

- API availability;
- authentication;
- version lifecycle;
- data completeness;
- performance;
- throttling;
- error handling;
- backward compatibility.

A clean API does not remove integration work.

It makes the integration contract clearer.

The operations team should still know:

- which processes use the API;
- what happens when it is unavailable;
- how failed calls are recovered;
- which data may be duplicated;
- how consumers are notified about changes;
- who verifies business completion.

## Event-driven architecture does not remove failure

Events are often used to reduce direct coupling.

A system publishes an event, and other applications react to it.

This can improve flexibility.

It can also create new operational questions:

- Was the event published?
- Was it delivered?
- Was it delivered more than once?
- Did consumers process it?
- Did events arrive in the expected order?
- What happened while a consumer was unavailable?
- Can missed events be replayed?
- Who knows all current consumers?

The core may remain untouched.

The complete process may become more difficult to trace.

Clean architecture still needs operational observability.

## A cleaner core can create more distributed support

In a classic SAP landscape, many issues remain inside one system.

The team can use:

- one authorization model;
- one transport system;
- one application log;
- one runtime;
- one set of transactions;
- one main support team.

In a distributed clean core landscape, the same process may include:

- SAP S/4HANA;
- SAP BTP;
- Integration Suite;
- an external service;
- an identity provider;
- a custom user interface;
- an event broker.

Each component may be well designed.

The support path becomes longer.

This is not an argument against distribution.

It is an argument for designing support together with architecture.

## Clean core changes the role of AMS

A traditional AMS team often focuses on:

- incidents;
- configuration;
- custom ABAP;
- transports;
- user support;
- recurring jobs.

A clean core operating model requires broader capability.

AMS may need to understand:

- APIs;
- cloud applications;
- BTP services;
- event flows;
- CI/CD pipelines;
- identity and access;
- platform observability;
- product release cycles;
- service dependencies;
- consumption costs.

The functional consultant still matters.

But the operating unit must understand the full service.

A clean core programme that modernizes architecture without modernizing AMS creates a support gap.

## The “not in the core” problem

Projects sometimes use a simple decision rule:

> If it is outside S/4HANA, it is clean.

This is too weak.

A poorly designed external extension can still:

- duplicate SAP data;
- bypass business controls;
- create inconsistent authorization;
- introduce unsupported dependencies;
- perform direct updates through unsafe interfaces;
- create difficult recovery scenarios;
- become impossible to upgrade;
- depend on one developer.

It may not contaminate the ERP core.

It can still contaminate the operating model.

Clean core should include quality standards for everything around the core.

## Standardization creates organizational complexity

Moving toward standard processes reduces technical variation.

It can increase organizational work in the short term.

Business units may need to:

- change roles;
- remove local steps;
- accept common definitions;
- change approval limits;
- standardize master data;
- retrain users;
- retire local reports;
- align policies.

The technical solution may become simpler.

The transformation becomes politically harder.

This is why clean core cannot be delivered only by developers and architects.

It requires process leadership.

## Local requirements need expiration dates

Some local exceptions are necessary.

Others were necessary once.

A useful governance rule is to give every deviation:

- an owner;
- a reason;
- a business value;
- an approval date;
- a review date;
- an exit condition.

For example:

> This extension is required until the local regulation changes or SAP standard supports the requirement.

Without review dates, temporary exceptions become permanent architecture.

## Clean core is not a one-time project

A company cannot declare the core clean after go-live and assume that it will stay clean.

New complexity enters through:

- urgent business requests;
- local developments;
- acquired companies;
- regulatory changes;
- integration shortcuts;
- copied extensions;
- emergency fixes;
- cloud services bought outside architecture governance.

Clean core therefore needs continuous governance.

SAP’s current guidance includes ongoing process, architecture and solution governance rather than treating clean core as a one-time technical cleanup.

The difficult part is not reaching a cleaner state once.

It is preventing gradual return to the old state.

## Emergency changes are where discipline breaks

Most architecture principles look clear during design workshops.

They become weaker during production pressure.

A critical customer process fails.

The business needs a correction today.

The fastest option may be:

- direct code;
- an unsupported API;
- a manual table update;
- a temporary integration;
- a local script.

Sometimes an emergency workaround is necessary.

The risk appears when nobody returns to remove it.

Every emergency exception should have:

- documented reason;
- risk owner;
- expiry date;
- permanent target solution;
- follow-up review.

Otherwise, operational urgency slowly rebuilds technical debt.

## Clean core must include data

A technically clean extension can still depend on poor data.

For example, a new workflow may use customer classification, supplier risk status or material category.

If these values are inconsistent, the extension produces inconsistent decisions.

SAP’s clean core definition includes data quality because stable processes and extensions require reliable primary data.

This means that clean core governance must ask:

- Which data is authoritative?
- Who owns the attributes?
- Are duplicates controlled?
- Are required fields complete?
- Are definitions aligned across systems?
- Can the extension trust the data?

Moving logic outside ERP without improving data can create a modern interface around an old problem.

## Clean core must include integration

A clean ERP core connected through dozens of poorly governed interfaces is not a clean operating landscape.

Integration complexity grows when:

- every project creates its own pattern;
- mappings contain hidden business logic;
- interfaces have no owners;
- errors require manual reprocessing;
- APIs are copied rather than reused;
- events have undocumented consumers;
- monitoring stops at technical delivery.

Clean core integration requires more than supported technology.

It requires consistent patterns and ownership.

## Clean core must include operations

SAP includes operations as one of the main clean core dimensions.

This is easy to overlook.

An architecture is not clean in practice if it cannot be:

- monitored;
- supported;
- changed;
- recovered;
- understood;
- retired.

Operational cleanliness means that teams know:

- which services exist;
- who owns them;
- how they are monitored;
- which dependencies matter;
- how failure is handled;
- how changes are tested;
- how lifecycle decisions are made.

A solution that is elegant in design but opaque in production is not operationally clean.

## The new dependency on platform skills

Custom code inside SAP traditionally requires ABAP and functional knowledge.

Side-by-side solutions may require:

- JavaScript or TypeScript;
- Java;
- Python;
- ABAP Cloud;
- SAP CAP;
- container platforms;
- databases;
- cloud security;
- APIs;
- events;
- DevOps.

This can reduce dependency on one technology.

It can increase dependency on a broader skill set.

The company should decide whether it can support these skills long term.

A project may build an extension with an external specialist team.

The extension remains after the project leaves.

The architecture decision should include the future support model, not only development speed.

## The new dependency on commercial services

A side-by-side extension may consume:

- application runtime;
- integration messages;
- database capacity;
- workflow executions;
- AI services;
- API management;
- logging;
- monitoring.

These services can create variable cost.

A small pilot may be inexpensive.

A high-volume production process may behave differently.

Operational governance should track:

- consumption;
- volume growth;
- inactive resources;
- duplicated services;
- unexpected peaks;
- cost ownership.

A clean core design that ignores consumption may create a clean technical architecture with weak cost control.

## More frequent upgrades require better testing

One goal of clean core is easier adoption of new releases.

But easier upgrades do not mean no testing.

A business process may depend on:

- standard configuration;
- released APIs;
- extension logic;
- external systems;
- data;
- user interfaces.

Any part can change.

The company still needs:

- impact analysis;
- regression tests;
- interface tests;
- process tests;
- production observation.

The difference is that testing becomes more predictable when the core and extension contracts are controlled.

Clean core reduces unnecessary upgrade risk.

It does not remove release responsibility.

## Test the complete business service

A test that confirms the extension starts is not enough.

A test that confirms the API responds is not enough.

The business service must be tested end to end.

For example:

1. create the SAP business document;
2. trigger the extension;
3. process the business rule;
4. return or distribute the result;
5. continue downstream processing;
6. confirm the expected business outcome.

This is especially important when the architecture becomes distributed.

Each component may pass its own test while the service fails between them.

## Clean core metrics can become misleading

Companies may measure:

- number of modifications removed;
- percentage of standard processes;
- custom objects retired;
- released API usage;
- extensions moved to BTP.

These are useful indicators.

They are not the final outcome.

A programme can improve all these measures while:

- support cost rises;
- incident resolution slows;
- process ownership remains unclear;
- users create manual workarounds;
- external applications multiply;
- integration failures increase.

A balanced clean core scorecard should include operational outcomes.

## Better clean core metrics

Useful measures include:

### Standard process adoption

How much of the process uses supported standard capability?

### Justified deviation rate

How many deviations have documented business value, ownership and review dates?

### Upgrade effort

How much effort is required to analyze and test a release?

### Extension reliability

How often do extensions create production incidents?

### End-to-end recovery time

How quickly can a distributed process recover after failure?

### Unsupported dependency count

How many extensions depend on internal objects or unstable interfaces?

### Operational ownership coverage

How many business-critical extensions have named support and product owners?

### Custom functionality usage

Which custom developments are still used?

Unused code should not remain only because it is difficult to evaluate.

### Lifecycle cost

What does the extension cost to operate, test, secure and change?

### Retirement rate

How many obsolete extensions and process deviations are actually removed?

The goal is not only a cleaner technical score.

It is a more adaptable operating system.

## Every extension needs a business case

A useful extension decision should answer five questions.

## 1. What business problem does it solve?

The requirement should be described in business terms.

Not:

> We need a custom app.

But:

> The current process causes a two-day delay and cannot support the required approval rule.

## 2. Why is standard capability insufficient?

The gap should be specific and verified.

Sometimes the standard solution exists but is not known, configured or adopted.

## 3. What value does the difference create?

Possible value includes:

- regulatory compliance;
- lower process time;
- lower risk;
- better customer service;
- reduced manual effort;
- competitive differentiation.

## 4. What is the full lifecycle cost?

Include:

- design;
- development;
- integration;
- testing;
- security;
- operation;
- upgrades;
- support;
- retirement.

## 5. What is the exit strategy?

The extension may become unnecessary when:

- SAP adds standard functionality;
- the business process changes;
- a regulation expires;
- another platform replaces it.

A custom solution without an exit strategy usually lives longer than its business value.

## A practical extension classification

Companies can classify requirements into four groups.

### Adopt standard

The standard process meets the need with acceptable business change.

### Configure or use key-user extensibility

The requirement is limited, supported and close to the standard process.

### Develop a controlled extension

The requirement creates real value and needs custom logic.

Select the correct extensibility model and supported interfaces.

### Reject or retire

The requirement preserves unnecessary variation or creates more lifecycle cost than value.

This final option is often missing.

Architecture governance should be allowed to say no.

## What managers should ask

Managers do not need to choose between every SAP extensibility technology.

They should ask whether the total operating model is improving.

Useful questions include:

1. Which business differences truly create measurable value?
2. Which custom processes only preserve historical behaviour?
3. Did we remove complexity or move it to another platform?
4. Who owns every business-critical extension after go-live?
5. How is the complete service monitored?
6. Which skills are required to support it?
7. What happens when the extension is unavailable?
8. Which released APIs and events does it depend on?
9. How will SAP releases affect it?
10. What is the full lifecycle cost?
11. Which manual workarounds remain around the clean solution?
12. Which data quality risks affect it?
13. When will the business need be reviewed again?
14. What is the retirement plan?
15. Is the operating landscape becoming easier to change?

These questions keep clean core connected to business value.

## A practical clean core operating model

A strong operating model can use seven controls.

## 1. Process ownership

Every core process has an accountable owner.

That owner decides whether deviations are justified.

## 2. Architecture governance

Extensions and integrations follow defined patterns.

Exceptions are documented and reviewed.

## 3. Product ownership

Every important extension has a roadmap and lifecycle owner.

## 4. Operational readiness

Before go-live, the team defines:

- monitoring;
- support;
- recovery;
- service levels;
- documentation;
- cost ownership.

## 5. Release management

The complete process is tested against SAP and extension changes.

## 6. Continuous review

Usage, cost, incidents and business value are reviewed regularly.

## 7. Retirement

Unused and obsolete functionality is removed.

Without retirement, the extension portfolio only grows.

## A practical review of one extension

A company can begin with one important custom capability.

### Step 1: Define the original business need

Why was it built?

Is the need still valid?

### Step 2: Measure actual use

Which users and processes depend on it?

How often is it executed?

### Step 3: Review standard capability

Has SAP added a supported alternative?

Could the business process now change?

### Step 4: Map all dependencies

Include:

- APIs;
- data;
- events;
- integrations;
- identity;
- monitoring;
- external services.

### Step 5: calculate lifecycle effort

Include incidents, testing, upgrades, security and provider cost.

### Step 6: choose the target

- retain;
- redesign;
- move;
- replace with standard;
- retire.

### Step 7: define the operating owner

Do not complete the architecture decision without this role.

## Clean core should reduce future friction

The purpose of clean core is not architectural purity.

A company does not create value because its ERP has fewer custom objects.

The value appears when the company can:

- change processes faster;
- adopt product improvements;
- reduce upgrade effort;
- understand its extensions;
- recover from failures;
- avoid unnecessary dependency;
- retire obsolete solutions.

A core can be technically clean while the surrounding landscape becomes difficult to control.

A core can also contain justified extensions while remaining well governed and upgradeable.

The useful distinction is not:

> Standard or custom?

It is:

> Controlled or uncontrolled?

Clean core works when complexity is visible, justified, supported and removable.

It fails when complexity is simply moved out of sight.

---

## Clean core operations checklist

- [ ] Clean core is treated across process, data, integration, extension and operations.
- [ ] Business deviations have measurable justification.
- [ ] Standard capability is reviewed before development.
- [ ] Historical custom processes are challenged.
- [ ] Moving code outside ERP is not counted automatically as simplification.
- [ ] Every extension has business, product and support ownership.
- [ ] Released APIs and supported extension models are used.
- [ ] API and event dependencies are documented.
- [ ] End-to-end monitoring covers the complete business service.
- [ ] Recovery and fallback procedures exist.
- [ ] Lifecycle and consumption costs are measured.
- [ ] SAP releases trigger complete process testing.
- [ ] Data quality is included in extension readiness.
- [ ] Emergency exceptions have expiry dates.
- [ ] Custom functionality usage is measured.
- [ ] Obsolete extensions are retired.
- [ ] The business value of deviations is reviewed regularly.
- [ ] Clean core success is measured through business adaptability, not only custom-code reduction.

## Sources and further reading

SAP currently defines clean core as an up-to-date ERP environment with current releases, compliant extensions and integrations, good primary data quality and effective process design. SAP’s framework covers extensibility, processes, data, integration and operations.

SAP’s clean core process guidance recommends fit-to-standard adoption, controlled deviations, process ownership and connected architecture, process and solution governance. It also states that extensions remain valid where they support regulatory, industry or measurable differentiating requirements.

SAP’s current extensibility guidance describes side-by-side applications as extensions running on SAP BTP and using released remote APIs to access SAP S/4HANA Cloud data and processes.

SAP also explains that its cloud extensibility model is intended to preserve customer differentiation while allowing smoother software updates than traditional modification-heavy approaches.

*Reviewed: July 2026. SAP product names, extensibility options and clean core assessment methods continue to change. Architecture decisions should be checked against current SAP documentation and the actual deployment model.*

## Continue exploring

- [Why SAP Teams Keep Solving the Same Incidents](/blog/why-sap-teams-keep-solving-the-same-incidents/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [The Hidden Operational Cost of Poor Master Data in SAP](/blog/the-hidden-operational-cost-of-poor-master-data-in-sap/)
- Next in the migration: [Why Traditional SAP AMS SLAs Reward the Wrong Behaviour](/blog/why-traditional-sap-ams-slas-reward-the-wrong-behaviour/)
