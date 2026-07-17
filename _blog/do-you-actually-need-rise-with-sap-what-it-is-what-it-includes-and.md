---
layout: blog
title: "Do You Actually Need RISE with SAP? What It Is, What It Includes, and Where Companies Get Trapped"
description: "Its data centre is expensive. The SAP landscape contains years of custom code. Experienced Basis specialists are becoming difficult to replace."
slug: do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and
permalink: /blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP solution architecture"
tags:
  - sap-solution-architecture
  - sap-architecture
canonical_url: https://dkharlanau.github.io/blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 24
migration_sequence: 39
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/
  - /blog/your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and/
---

## On this page

- [What is RISE with SAP in 2026?](#what-is-rise-with-sap-in-2026)
- [RISE with SAP is not the same as SAP S/4HANA](#rise-with-sap-is-not-the-same-as-sap-s-4hana)
- [RISE with SAP is not the public cloud edition](#rise-with-sap-is-not-the-public-cloud-edition)
- [What is normally included?](#what-is-normally-included)
- [What does SAP manage?](#what-does-sap-manage)
- [What remains the customer’s responsibility?](#what-remains-the-customer-s-responsibility)
- [RISE does not replace an implementation partner](#rise-does-not-replace-an-implementation-partner)
- [RISE does not automatically create a clean core](#rise-does-not-automatically-create-a-clean-core)
- [RISE does not automatically produce business transformation](#rise-does-not-automatically-produce-business-transformation)
- [Why companies choose RISE with SAP](#why-companies-choose-rise-with-sap)
- [1. The company wants to exit infrastructure operations](#1-the-company-wants-to-exit-infrastructure-operations)
- [2. The company wants one contractual lead for the ERP stack](#2-the-company-wants-one-contractual-lead-for-the-erp-stack)
- [3. The company needs private-cloud flexibility](#3-the-company-needs-private-cloud-flexibility)
- [4. The company wants to accelerate the move to S/4HANA](#4-the-company-wants-to-accelerate-the-move-to-s-4hana)
- [5. The company accepts continuous lifecycle management](#5-the-company-accepts-continuous-lifecycle-management)
- [6. The company wants closer access to SAP’s cloud innovation model](#6-the-company-wants-closer-access-to-sap-s-cloud-innovation-model)
- [Where companies get trapped](#where-companies-get-trapped)
- [Trap 1: Buying RISE before defining the target operating model](#trap-1-buying-rise-before-defining-the-target-operating-model)
- [Trap 2: Assuming one contract means one operational team](#trap-2-assuming-one-contract-means-one-operational-team)
- [Trap 3: Treating the package as unlimited](#trap-3-treating-the-package-as-unlimited)
- [Trap 4: Comparing subscription cost only with hardware cost](#trap-4-comparing-subscription-cost-only-with-hardware-cost)
- [Trap 5: Underestimating dual-run cost](#trap-5-underestimating-dual-run-cost)
- [Trap 6: Believing SAP will own custom-code risk](#trap-6-believing-sap-will-own-custom-code-risk)
- [Trap 7: Postponing integration analysis](#trap-7-postponing-integration-analysis)
- [Trap 8: Misunderstanding the SLA](#trap-8-misunderstanding-the-sla)
- [Trap 9: Assuming disaster recovery covers the complete process](#trap-9-assuming-disaster-recovery-covers-the-complete-process)
- [Trap 10: Ignoring release and upgrade obligations](#trap-10-ignoring-release-and-upgrade-obligations)
- [Trap 11: Assuming all innovations arrive automatically](#trap-11-assuming-all-innovations-arrive-automatically)
- [Trap 12: Weak control over hyperscaler and location decisions](#trap-12-weak-control-over-hyperscaler-and-location-decisions)
- [Trap 13: Losing internal SAP capability](#trap-13-losing-internal-sap-capability)
- [Trap 14: Ignoring exit architecture](#trap-14-ignoring-exit-architecture)
- [RISE versus other deployment choices](#rise-versus-other-deployment-choices)
- [When RISE is likely to be rational](#when-rise-is-likely-to-be-rational)
- [When RISE may be a poor fit](#when-rise-may-be-a-poor-fit)
- [RISE may solve the wrong problem](#rise-may-solve-the-wrong-problem)
- [A practical decision framework](#a-practical-decision-framework)
- [1. Strategic case](#1-strategic-case)
- [2. Operating-model case](#2-operating-model-case)
- [3. Architecture case](#3-architecture-case)
- [4. Commercial case](#4-commercial-case)
- [5. Exit case](#5-exit-case)
- [Questions to answer before signing](#questions-to-answer-before-signing)
- [Build the TCO correctly](#build-the-tco-correctly)
- [A realistic management conclusion](#a-realistic-management-conclusion)

A company is still running SAP ECC.

Its data centre is expensive. The SAP landscape contains years of custom code. Experienced Basis specialists are becoming difficult to replace. Management knows that the ERP must eventually move to SAP S/4HANA.

SAP proposes RISE with SAP.

The presentation appears to offer one solution for everything:

- migration to the cloud;
- modern ERP;
- managed infrastructure;
- lower technical complexity;
- clean core;
- process transformation;
- access to AI;
- one accountable provider.

The contract is signed.

Two years later, the ERP is hosted in a managed cloud environment.

But the company still has:

- most of its old processes;
- thousands of custom developments;
- complex integrations;
- several external support providers;
- difficult upgrades;
- unclear support boundaries;
- growing subscription costs.

The infrastructure changed.

The operating model changed.

The business transformation did not happen automatically.

This is the first thing managers need to understand:

> RISE with SAP can be a rational way to modernize and operate SAP ERP, but it is not a transformation button.

It does not remove the need to decide:

- which processes should change;
- which custom code should disappear;
- which data should be migrated;
- which integrations should be redesigned;
- which responsibilities remain with the customer;
- whether the commercial model is better than the alternatives.

RISE is useful when it solves a defined strategic and operating problem.

It becomes expensive when it is purchased as a general answer to uncertainty about SAP’s future.

## What is RISE with SAP in 2026?

The terminology has changed over time, which is one reason many managers remain confused.

SAP currently defines RISE with SAP as a **guided transformation journey for existing SAP ERP customers** moving from on-premises ERP toward SAP’s cloud-based Business Suite. SAP describes the journey as combining a standardized methodology, advanced tools and expert guidance.

This means RISE with SAP is not simply one software product.

It is better understood as a combination of:

1. a commercial relationship;
2. a transformation methodology;
3. a cloud ERP target;
4. managed technical operations;
5. supporting tools, services and entitlements.

The main ERP product at the centre of the private-cloud route is now called **SAP Cloud ERP Private**, previously known as SAP S/4HANA Cloud, private edition.

SAP describes Cloud ERP Private as a tailored private-cloud ERP designed for companies that need the functional depth and flexibility of existing SAP ERP investments while moving to an SAP-managed cloud operating model.

That distinction matters:

> RISE with SAP is the journey and commercial framework. SAP Cloud ERP Private is the ERP product and managed environment at the centre of that journey.

## RISE with SAP is not the same as SAP S/4HANA

SAP S/4HANA is the ERP application generation.

It can exist under different deployment and commercial models.

A company may run SAP S/4HANA:

- on its own infrastructure;
- in a private data centre;
- on infrastructure from a hyperscaler;
- through a managed-service provider;
- as SAP Cloud ERP Private under the RISE journey.

Therefore:

> Moving to SAP S/4HANA does not automatically mean purchasing RISE with SAP.

And:

> Purchasing RISE does not automatically mean the business has completed an S/4HANA transformation.

The product decision and the operating-model decision are related, but they are not identical.

## RISE with SAP is not the public cloud edition

SAP currently distinguishes two cloud ERP directions:

- **SAP Cloud ERP**, the ready-to-run cloud ERP managed by SAP;
- **SAP Cloud ERP Private**, the tailored private-cloud ERP intended to preserve and modernize existing SAP ERP investments.

The public-cloud direction is generally more standardized.

The private-cloud direction provides more room for:

- existing processes;
- industry functionality;
- complex configuration;
- customer-specific extensions;
- phased transformation.

That flexibility has a cost.

A private-cloud ERP can preserve valuable differentiation.

It can also preserve unnecessary complexity.

RISE should not be selected merely because the organization does not want to challenge its current SAP design.

## What is normally included?

SAP’s current Cloud ERP Private package is presented in several broad groups:

- business applications;
- transformation tools and services;
- optimization and extensibility applications;
- infrastructure;
- technical cloud services;
- cloud support;
- operational tools.

The transformation toolchain may include capabilities associated with:

- SAP Signavio;
- SAP LeanIX;
- SAP Cloud ALM;
- SAP Build;
- master data management;
- migration and transformation tooling;
- guided onboarding and preparation services.

SAP’s current RISE methodology follows six broad stages:

1. Discover;
2. Prepare;
3. Explore;
4. Realize;
5. Deploy;
6. Run.

The methodology includes current-state analysis, project preparation, fit-to-standard work, realization, testing, deployment and continuous operation.

This sounds comprehensive.

But there is an important contractual warning:

> A marketing portfolio is not the same thing as your purchased entitlement.

The exact commercial scope depends on documents such as:

- the order form;
- supplemental terms;
- support schedules;
- service-level agreements;
- service description guides;
- data-processing terms;
- success-plan scope documents.

SAP itself states that cloud contracts consist of several documents and that the order form contains details such as price, scope and key terms.

Managers should therefore avoid the phrase:

> “It is included in RISE.”

The better question is:

> “Which exact product, edition, quantity, capacity, service level and usage right is included in our signed order form?”

## What does SAP manage?

One of the strongest arguments for Cloud ERP Private is the transfer of technical operational responsibility.

SAP currently describes Cloud ERP Private as an SAP-managed foundation where SAP runs, monitors, supports and updates the ERP. SAP also states that managed services extend beyond infrastructure to the operating system, SAP HANA database and Cloud ERP Private application.

This may reduce the customer’s responsibility for:

- physical infrastructure;
- infrastructure provisioning;
- operating-system administration;
- database operations;
- technical monitoring;
- backup infrastructure;
- parts of technical patching and lifecycle management.

SAP markets itself as a single point of accountability for the managed cloud service.

This can be valuable for companies that no longer want to operate a large SAP technical stack.

But “SAP manages the system” does not mean “SAP manages the business.”

## What remains the customer’s responsibility?

The exact boundary depends on the signed service descriptions and responsibility model.

In practical terms, the customer will still need to govern many areas, including:

- business-process design;
- configuration decisions;
- data ownership and quality;
- custom code;
- integrations;
- user roles and business authorization;
- segregation of duties;
- functional testing;
- user acceptance;
- release readiness;
- organizational change;
- business continuity outside the managed ERP boundary;
- partner and non-SAP applications.

A managed cloud platform does not know:

- whether the order-to-cash process is commercially correct;
- whether a supplier should be approved;
- whether a custom interface can create duplicates;
- whether an authorization role violates internal policy;
- whether a customer-specific development is still required.

SAP’s own product description refers to a shared-responsibility model for security, compliance and data protection.

The customer does not outsource accountability for its business simply because SAP operates the technical environment.

## RISE does not replace an implementation partner

A company moving from ECC to Cloud ERP Private will normally still require substantial project work.

This may include:

- process assessment;
- target architecture;
- greenfield, brownfield or selective-transition design;
- custom-code analysis;
- data cleansing and migration;
- configuration;
- integration redesign;
- testing;
- cutover;
- training;
- change management.

SAP may provide tools, methodology, guidance and selected services.

An implementation partner or internal programme team still has to perform much of the transformation.

The same applies after go-live.

The company may still need:

- functional application support;
- custom development;
- integration support;
- business-process monitoring;
- data stewardship;
- release testing;
- continuous improvement.

RISE can simplify part of the supplier landscape.

It does not necessarily eliminate the ecosystem around SAP.

## RISE does not automatically create a clean core

SAP places strong emphasis on clean core.

The current RISE and Cloud ERP Private materials connect clean core with:

- reduced technical debt;
- easier upgrades;
- faster innovation;
- cloud-compliant extensibility;
- use of SAP BTP and approved extension patterns.

But moving a customized ECC system into a managed cloud does not clean it.

If the company migrates:

- old modifications;
- unused reports;
- duplicated interfaces;
- hard-coded mappings;
- custom tables;
- obsolete workflows,

the resulting system will still be complex.

It will simply be complex inside an SAP-managed environment.

Clean core requires active decisions:

- remove;
- replace with standard;
- redesign;
- move to side-by-side extension;
- retain with an explicit business justification.

RISE provides pressure and tooling for this work.

It does not perform the governance decision for the customer.

## RISE does not automatically produce business transformation

A system conversion can move the technical ERP to S/4HANA while preserving most current processes.

That may be the correct first step.

But it should not be described as complete business transformation.

A company can move to RISE and still retain:

- inefficient approvals;
- manual order blocks;
- duplicate master data;
- spreadsheet planning;
- fragmented reporting;
- unstable integrations.

Business transformation requires changes to:

- ownership;
- policy;
- process;
- data;
- roles;
- metrics;
- decisions.

Cloud hosting cannot make these changes independently.

## Why companies choose RISE with SAP

There are valid reasons to select it.

## 1. The company wants to exit infrastructure operations

A company may no longer want to own:

- data-centre capacity;
- HANA infrastructure;
- backup platforms;
- operating-system maintenance;
- technical high availability;
- disaster-recovery infrastructure.

Transferring these activities to SAP can reduce operational fragmentation.

This is particularly relevant when:

- the internal Basis team is shrinking;
- infrastructure skills are scarce;
- the current data centre must close;
- several hosting providers are already involved;
- hardware renewal is approaching.

## 2. The company wants one contractual lead for the ERP stack

Traditional SAP operations may involve:

- SAP for software;
- hyperscaler for infrastructure;
- hosting provider;
- database specialists;
- Basis provider;
- application support partner;
- network provider.

When an incident occurs, providers may argue about ownership.

RISE offers SAP as the main contractual point for the managed ERP service.

This can simplify escalation.

It does not eliminate every support handover, especially when the business process crosses:

- external integrations;
- custom code;
- BTP applications;
- partner systems;
- customer networks.

## 3. The company needs private-cloud flexibility

A complex SAP customer may not be ready for a highly standardized public-cloud model.

It may have:

- industry processes;
- complex international operations;
- extensive integrations;
- phased migration requirements;
- high transaction volumes;
- valuable custom differentiation.

Cloud ERP Private provides a route that preserves more flexibility while changing the operating model.

## 4. The company wants to accelerate the move to S/4HANA

The standardized methodology, tools and transformation services can provide structure.

SAP currently presents RISE as using common checkpoints, expert guidance, fit-to-standard analysis and integrated tools across process, data, architecture, testing and project management.

This may reduce programme uncertainty.

It does not remove the need for strong customer governance.

## 5. The company accepts continuous lifecycle management

Private cloud does not mean the ERP can remain on one release indefinitely.

SAP currently states that Cloud ERP Private has a two-year release cycle, innovations every six months and seven years of maintenance for each release.

This gives more control than a highly standardized public-cloud cadence.

It still requires planned upgrades.

For some companies, this discipline is beneficial.

For others, it exposes how dependent they have become on old custom code and delayed testing.

## 6. The company wants closer access to SAP’s cloud innovation model

SAP is increasingly positioning new capabilities around:

- Business AI;
- Joule;
- data products;
- BTP;
- process transformation;
- clean-core extensions.

SAP presents RISE and Cloud ERP Private as the route for existing customers to consume these capabilities within a managed cloud model.

This can be strategically relevant.

It is not sufficient reason by itself.

AI value depends on:

- process quality;
- data quality;
- authorization;
- adoption;
- a real business use case.

## Where companies get trapped

## Trap 1: Buying RISE before defining the target operating model

The company signs the commercial agreement before deciding:

- what SAP will operate;
- what the customer will operate;
- what the implementation partner will deliver;
- what the AMS provider will support;
- who owns integrations;
- who owns security and testing.

The result is a contract without an operating design.

Before signing, create a responsibility model covering:

- infrastructure;
- Basis;
- database;
- application operations;
- configuration;
- custom code;
- releases;
- interfaces;
- jobs;
- authorization;
- monitoring;
- incidents;
- disaster recovery.

Do not assume the word “managed” answers these questions.

## Trap 2: Assuming one contract means one operational team

The commercial relationship may become simpler.

The delivery chain may still contain:

- SAP cloud operations;
- hyperscaler infrastructure;
- SAP product support;
- implementation partner;
- application-management provider;
- customer IT;
- network provider.

During an end-to-end incident, the company still needs:

- one incident commander;
- common correlation data;
- agreed escalation paths;
- clear response times;
- a business owner.

“One throat to choke” is not an operating model.

## Trap 3: Treating the package as unlimited

A package may list many products and capabilities.

Actual entitlements may be limited by:

- users;
- capacity;
- usage metric;
- environments;
- storage;
- transactions;
- credits;
- service tier;
- geographic availability.

This applies especially to adjacent capabilities such as:

- BTP;
- analytics;
- process transformation;
- integration;
- AI;
- data management.

Review the commercial documents line by line.

Create an entitlement register showing:

| Capability | Edition | Quantity | Metric | Limit | Owner |
|---|---|---:|---|---:|---|
| Cloud ERP Private | Contracted edition | Defined | Contract metric | Defined | ERP owner |
| BTP service | Specific service | Defined | Consumption or subscription | Defined | Platform owner |
| Signavio | Specific components | Defined | Users or usage | Defined | Process owner |
| Integration | Specific service | Defined | Messages or capacity | Defined | Integration owner |

Do not build a business case using functionality that has not actually been purchased.

## Trap 4: Comparing subscription cost only with hardware cost

A weak comparison looks like this:

```text
Current hardware and hosting
versus
RISE subscription
```

This is incomplete.

The current-state cost should include:

- software maintenance;
- infrastructure;
- database operations;
- Basis;
- monitoring;
- backup;
- disaster recovery;
- security;
- support vendors;
- technical upgrades;
- internal labour.

The RISE scenario should include:

- subscription;
- implementation;
- data migration;
- custom-code remediation;
- integration redesign;
- testing;
- training;
- change management;
- partner support;
- BTP and related consumption;
- network connectivity;
- dual operation;
- future upgrades;
- exit preparation.

A cloud subscription can be economically attractive.

It can also become more expensive.

The answer depends on the complete five-to-ten-year operating model.

## Trap 5: Underestimating dual-run cost

During transformation, the company may operate:

- ECC;
- Cloud ERP Private;
- old middleware;
- new integration services;
- legacy reporting;
- temporary replication;
- several test environments.

Dual operation may last much longer than planned.

Its cost includes:

- licenses;
- infrastructure;
- support;
- reconciliations;
- temporary interfaces;
- duplicate testing;
- additional people.

The programme should have explicit retirement milestones.

Without them, the company pays for both worlds.

## Trap 6: Believing SAP will own custom-code risk

SAP may operate the technical platform.

The customer remains responsible for deciding whether custom code:

- is required;
- is secure;
- performs correctly;
- survives an upgrade;
- violates clean-core goals;
- creates business risk.

The implementation partner may analyse and remediate it.

The business must approve the resulting process changes.

Do not migrate every development simply because it technically runs.

## Trap 7: Postponing integration analysis

Many ERP transformations focus first on the core.

Interfaces are analysed later.

This is dangerous because the integration landscape may contain:

- business rules;
- code mappings;
- process orchestration;
- external commitments;
- manual recovery logic.

RISE does not automatically modernize integrations.

The company still needs to decide:

- which interfaces should remain;
- which should use standard APIs;
- which should become events;
- which mappings are authoritative;
- which middleware remains;
- which direct connections must be removed.

A new ERP surrounded by old integration debt is not a clean architecture.

## Trap 8: Misunderstanding the SLA

SAP cloud agreements use service-specific SLA documents.

SAP states that an SLA defines system availability, maintenance windows and possible service credits if the committed availability is not achieved.

That is important.

But platform availability is not the same as business-process availability.

The ERP may be available while:

- one interface is broken;
- a custom job has failed;
- master data is incomplete;
- the warehouse cannot receive orders;
- users have incorrect roles;
- a partner system is unavailable.

Managers should define an end-to-end business service level separately.

For example:

> Customer orders can be received, created, confirmed and transferred to fulfilment.

That service crosses several technical components.

## Trap 9: Assuming disaster recovery covers the complete process

Cloud ERP may include backups and business-continuity provisions.

The complete customer process may also depend on:

- Integration Suite;
- BTP applications;
- identity services;
- customer networks;
- external warehouses;
- banks;
- partner systems.

A resilient ERP does not automatically create a resilient order-to-cash process.

Test:

- business recovery time;
- in-flight messages;
- duplicate prevention;
- manual fallback;
- reconciliation after recovery.

## Trap 10: Ignoring release and upgrade obligations

Cloud ERP Private offers more flexibility than the public-cloud model.

It does not allow permanent avoidance of upgrades.

The company needs:

- regression-test automation;
- custom-code control;
- interface compatibility tests;
- business release calendars;
- accountable process owners.

If every upgrade requires a large emergency project, the cloud operating model is not working.

## Trap 11: Assuming all innovations arrive automatically

Technical availability does not equal business adoption.

An AI feature may exist, but the company may still need:

- activation;
- licensing;
- configuration;
- data preparation;
- security design;
- process redesign;
- training;
- controls.

The same applies to:

- analytics;
- process mining;
- automation;
- data products;
- integration services.

“Available in the portfolio” is not the same as “producing value.”

## Trap 12: Weak control over hyperscaler and location decisions

SAP currently states that Cloud ERP Private may be deployed using a hyperscaler, private data centre or sovereign-cloud option.

The decision should consider:

- data residency;
- latency;
- proximity to connected systems;
- sovereignty;
- certifications;
- regional service availability;
- network design;
- disaster recovery.

Do not select infrastructure only because the company already has a general cloud agreement.

The ERP operating model under RISE differs from running a customer-controlled virtual machine in that cloud.

## Trap 13: Losing internal SAP capability

Some companies interpret managed cloud as permission to remove internal SAP technical and architectural knowledge.

This creates dependency.

The customer still needs people who can challenge:

- sizing;
- performance;
- security;
- upgrade plans;
- support responses;
- integration design;
- commercial consumption.

The internal team may become smaller.

It should become more capable in:

- architecture;
- vendor governance;
- business-process control;
- service management;
- data;
- release assurance.

Outsourcing execution should not mean outsourcing understanding.

## Trap 14: Ignoring exit architecture

A cloud decision should include an exit plan.

This does not mean the company expects the relationship to fail.

It means the company understands its dependencies.

Review:

- how data can be extracted;
- how historical documents are retained;
- which custom extensions depend on BTP services;
- which interfaces use SAP-specific endpoints;
- what happens to environments at termination;
- which knowledge remains internal;
- how much time a transition would require.

SAP’s Trust Center states that renewal and termination are governed through the cloud contract and associated order documents.

The architectural exit is usually harder than the administrative termination.

## RISE versus other deployment choices

A simplified comparison can help.

| Question | S/4HANA on-premises | Self-managed on hyperscaler | Cloud ERP Private through RISE | SAP Cloud ERP |
|---|---|---|---|---|
| Infrastructure responsibility | Customer | Customer or MSP | Primarily SAP-managed | SAP-managed |
| Process flexibility | High | High | High, with cloud governance | More standardized |
| Existing custom code | Broad control | Broad control | Possible but should be rationalized | More restricted |
| Upgrade control | High, but easy to postpone | High, but easy to postpone | Controlled lifecycle | Frequent standardized updates |
| Technical operations | Customer or partner | Customer or partner | Managed service from SAP | SaaS model |
| Best fit | Strong internal operations and specific control needs | Existing cloud strategy and mature SAP operations | Existing SAP customers needing private-cloud flexibility and managed operations | Organizations able to adopt standardized cloud processes |
| Main risk | Technical debt and delayed modernization | Operational complexity remains | Commercial dependency and false transformation assumptions | Fit gaps and excessive customization expectations |

This is not a universal decision table.

It illustrates that RISE is one operating model among several.

## When RISE is likely to be rational

RISE deserves serious consideration when most of the following are true:

- the company is already committed to SAP S/4HANA;
- private-cloud flexibility is required;
- the current data centre or hosting model should be retired;
- SAP technical operations are not a strategic differentiator;
- infrastructure and Basis skills are difficult to maintain;
- the company wants SAP to lead accountability for the managed ERP stack;
- the organization accepts an upgrade discipline;
- management is willing to rationalize custom code;
- transformation governance is strong;
- a complete commercial comparison shows acceptable value.

## When RISE may be a poor fit

RISE may be weak or premature when:

- the only goal is cheaper infrastructure;
- the company is not ready to begin S/4HANA transformation;
- management wants to preserve every current customization;
- an efficient S/4HANA hyperscaler environment already exists;
- the company requires unusually direct infrastructure control;
- the operating model and responsibility boundaries are undefined;
- the commercial case depends on optimistic assumptions;
- internal vendor-governance capability is weak;
- exit flexibility is strategically more important than managed-stack simplicity.

## RISE may solve the wrong problem

Suppose the main business pain is:

- unreliable planning;
- poor master data;
- manual logistics exceptions;
- slow financial close.

Moving the ERP into RISE does not automatically fix these issues.

The company needs specific improvement programmes.

RISE may provide a stronger platform and transformation structure.

But the business case should not attribute every expected process benefit to the hosting decision.

Separate the value into three categories.

### Infrastructure value

- data-centre exit;
- hardware avoidance;
- managed operations;
- resilience;
- security capability.

### ERP modernization value

- S/4HANA simplification;
- new functionality;
- improved user experience;
- upgradeability;
- clean core.

### Business transformation value

- process standardization;
- fewer exceptions;
- faster cycle time;
- automation;
- better decisions.

Each category has different causes, owners and costs.

## A practical decision framework

Management should test RISE across five cases.

## 1. Strategic case

- Is SAP still the strategic ERP?
- Why must the ERP move to cloud?
- Why is private cloud required?
- Which business capabilities depend on the move?

## 2. Operating-model case

- Which responsibilities move to SAP?
- Which remain internal?
- Which remain with partners?
- Can incidents be resolved without provider confusion?
- Does the internal organization have the right future skills?

## 3. Architecture case

- What happens to custom code?
- What happens to integrations?
- Which services move to BTP?
- How will clean core be governed?
- How will non-SAP systems connect?
- What are the data-residency requirements?

## 4. Commercial case

- What is included?
- What is consumption based?
- Which capacity assumptions are used?
- What is the five-to-ten-year TCO?
- What happens at renewal?
- What is the cost of dual operation and upgrades?

## 5. Exit case

- How is data retrieved?
- How are extensions separated?
- Which contracts can be replaced?
- Which internal knowledge is retained?
- How long would migration to another operating model take?

If one of these cases is absent, the decision is incomplete.

## Questions to answer before signing

### Product and entitlement

1. Which exact products and editions are included?
2. Which quantities and usage metrics apply?
3. Which environments are included?
4. Which BTP, Integration Suite, analytics, data and AI entitlements exist?
5. What happens when consumption exceeds the entitlement?

### Infrastructure and operations

6. Which hyperscaler or SAP infrastructure is used?
7. In which region is data stored?
8. What capacity and growth assumptions apply?
9. Which backup, recovery and availability options are included?
10. Which maintenance windows apply?

### Responsibility

11. Who patches the OS, database and SAP application?
12. Who manages jobs, interfaces and certificates?
13. Who performs functional support?
14. Who fixes custom code?
15. Who owns security roles and segregation of duties?
16. Who leads end-to-end incidents?

### Transformation

17. Which migration services are included?
18. Which work must be purchased from a partner?
19. How will unused custom code be identified and removed?
20. Which integrations will be replaced or redesigned?
21. How will data quality be improved?
22. Which process outcomes define success?

### Commercial

23. What is the contract term?
24. How are renewals handled?
25. Which future price and volume assumptions are used?
26. What is the cost of temporary and dual environments?
27. Which services may require additional purchase?

### Exit

28. How can data and documents be exported?
29. Which BTP services create architectural dependency?
30. What transition support exists at contract end?
31. Which skills and documentation remain with the customer?

## Build the TCO correctly

A useful five-year comparison might include:

### Current model

```text
Software maintenance
+ infrastructure
+ operating system and database
+ Basis and technical operations
+ security and monitoring
+ backup and disaster recovery
+ application support
+ upgrade projects
+ internal labour
+ technical-debt cost
```

### RISE model

```text
Cloud subscription
+ migration programme
+ implementation partner
+ custom-code remediation
+ data migration and archiving
+ integration modernization
+ testing and automation
+ change and training
+ internal governance
+ BTP and additional services
+ dual-run cost
+ periodic upgrades
+ exit preparation
```

Then compare:

- cash flow;
- recurring cost;
- risk;
- internal capacity;
- business value.

Do not treat a move from capital expenditure to subscription expenditure as an automatic saving.

It is a different financial and operating structure.

## A realistic management conclusion

RISE with SAP is neither a trap by definition nor a guaranteed modernization success.

It is a strategic sourcing and transformation model.

It can be a strong choice when the company wants:

- SAP Cloud ERP Private;
- managed technical operations;
- a structured transformation journey;
- closer alignment with SAP’s cloud roadmap;
- reduced responsibility for infrastructure.

It becomes weak when the company expects it to:

- repair bad processes;
- remove custom code automatically;
- eliminate implementation partners;
- provide every SAP cloud product without limits;
- guarantee lower TCO;
- solve every end-to-end support issue.

The decisive question is not:

> Is RISE with SAP good?

It is:

> Does RISE provide a better ERP operating and transformation model for this company than the alternatives, after the full responsibilities, commercial terms, architecture and exit conditions are understood?

For some companies, the answer will be yes.

For others, self-managed S/4HANA, a different managed provider or a more standardized public-cloud route may be better.

The wrong decision is not choosing RISE or rejecting it.

The wrong decision is signing before the company understands what it is buying.

---

### RISE with SAP decision checklist

- [ ] RISE is understood as a transformation journey and commercial framework.
- [ ] SAP Cloud ERP Private is understood as the core private-cloud ERP product.
- [ ] RISE is not confused with SAP S/4HANA itself.
- [ ] Private cloud and public cloud options have been compared.
- [ ] The business reason for moving to cloud is explicit.
- [ ] The target operating model is designed before contracting.
- [ ] SAP, customer and partner responsibilities are documented.
- [ ] Exact product entitlements and usage limits are recorded.
- [ ] Infrastructure sizing and growth assumptions are validated.
- [ ] Custom code is classified as remove, replace, redesign or retain.
- [ ] Integration modernization has its own scope and budget.
- [ ] Data migration includes quality and ownership.
- [ ] Clean core has governance, not only a slogan.
- [ ] Upgrade and testing capacity is funded.
- [ ] End-to-end business availability is separated from the technical SLA.
- [ ] Dual-run cost and retirement dates are included.
- [ ] BTP, AI, Signavio, LeanIX and other services are checked contractually.
- [ ] Security follows a shared-responsibility model.
- [ ] Internal SAP architecture and vendor-governance skills are retained.
- [ ] The five-to-ten-year TCO includes all transformation and operating costs.
- [ ] Renewal, consumption growth and exit conditions are understood.
- [ ] Benefits are separated into infrastructure, ERP and process value.
- [ ] Success is measured through business outcomes, not cloud migration alone.

### Sources and further reading

SAP currently defines RISE with SAP as a guided transformation journey for existing SAP ERP customers moving from on-premises ERP to SAP’s cloud-based Business Suite, supported by methodology, tools and expert guidance.

SAP’s current RISE methodology uses the stages Discover, Prepare, Explore, Realize, Deploy and Run and includes fit-to-standard analysis, transformation planning, testing, deployment and continuous improvement.

SAP currently describes SAP Cloud ERP Private as a tailored-to-fit, SAP-managed private-cloud ERP for customers migrating existing ECC, SAP ERP or S/4HANA investments. SAP states that it supports deployment on hyperscaler, private-data-centre and sovereign-cloud options.

SAP’s current Cloud ERP Private package is presented as combining business applications, transformation tools and services, optimization and extensibility applications, infrastructure, technical cloud services, cloud support and operational tooling.

SAP describes Cloud ERP Private operations as covering managed infrastructure, operating system, SAP HANA database and application-level technical services, while also referring to shared responsibility for security, compliance and data protection.

SAP’s Trust Center states that a cloud contract includes several contractual components, including the order form, cloud-service description, data-processing agreement, terms, support schedules and SLA documents. These documents define the actual commercial scope and service commitments.

*Reviewed: July 2026. SAP product names, package composition, AI entitlements, commercial metrics and service descriptions can change. Any RISE decision must be validated against the current signed order form, service-description guides, support schedules, SLAs and responsibility documents.*

## Continue exploring

- [SAP Pricing Explained: Sales, Procurement, Rebates, CPQ, Contracts, and the Right Solution for Each Business Model](/blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [How to Reduce Transportation Costs Without Destroying Delivery Reliability](/blog/how-to-reduce-transportation-costs-without-destroying-delivery/)
- Next in the migration: [SAP Pricing Explained: Sales, Procurement, Rebates, CPQ, Contracts, and the Right Solution for Each Business Model](/blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/)
