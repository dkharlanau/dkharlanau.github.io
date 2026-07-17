---
layout: blog
title: "SAP Business Data Cloud Explained: Architecture, Data Products, BW Modernization, Databricks, AI, and the Limits Behind the Marketing"
description: "SAP S/4HANA; - several legacy SAP ERP systems; - SAP BW; - SAP Datasphere; - SAP Analytics Cloud; - a cloud data lake; - Databricks or Snowflake; -."
slug: sap-business-data-cloud-explained-architecture-data-products-bw
permalink: /blog/sap-business-data-cloud-explained-architecture-data-products-bw/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP solution architecture"
tags:
  - sap-solution-architecture
  - ai-operations
  - sap-architecture
  - data-platforms
canonical_url: https://dkharlanau.github.io/blog/sap-business-data-cloud-explained-architecture-data-products-bw/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 35
migration_sequence: 49
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/
  - /blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/
---

## On this page

- [What SAP Business Data Cloud is](#what-sap-business-data-cloud-is)
- [What Business Data Cloud is not](#what-business-data-cloud-is-not)
- [The high-level architecture](#the-high-level-architecture)
- [The business data fabric idea](#the-business-data-fabric-idea)
- [Component 1: SAP Datasphere](#component-1-sap-datasphere)
- [Datasphere spaces](#datasphere-spaces)
- [Semantic modelling](#semantic-modelling)
- [Virtualization versus replication](#virtualization-versus-replication)
- [Component 2: SAP Analytics Cloud](#component-2-sap-analytics-cloud)
- [SAC is not the enterprise semantic authority](#sac-is-not-the-enterprise-semantic-authority)
- [Live connection versus acquired data](#live-connection-versus-acquired-data)
- [Planning](#planning)
- [Component 3: SAP Databricks](#component-3-sap-databricks)
- [Where SAP Databricks fits](#where-sap-databricks-fits)
- [Data sharing](#data-sharing)
- [Zero-copy claims require qualification](#zero-copy-claims-require-qualification)
- [SAP Databricks versus an existing Databricks estate](#sap-databricks-versus-an-existing-databricks-estate)
- [Component 4: SAP data products](#component-4-sap-data-products)
- [What a data product should contain](#what-a-data-product-should-contain)
- [SAP-managed data products](#sap-managed-data-products)
- [Custom data products](#custom-data-products)
- [Data product is not a synonym for table](#data-product-is-not-a-synonym-for-table)
- [Data-product granularity](#data-product-granularity)
- [Data contracts and change](#data-contracts-and-change)
- [Component 5: Business Warehouse modernization](#component-5-business-warehouse-modernization)
- [Why BW remains important](#why-bw-remains-important)
- [Data Product Generator for BW](#data-product-generator-for-bw)
- [What the Data Product Generator solves](#what-the-data-product-generator-solves)
- [What it does not solve](#what-it-does-not-solve)
- [BW Bridge](#bw-bridge)
- [A sensible BW modernization strategy](#a-sensible-bw-modernization-strategy)
- [The danger of “lift and modernize later”](#the-danger-of-lift-and-modernize-later)
- [Component 6: Intelligent content and applications](#component-6-intelligent-content-and-applications)
- [What these applications contain in practice](#what-these-applications-contain-in-practice)
- [Installation model](#installation-model)
- [Entitlements](#entitlements)
- [Extending intelligent content](#extending-intelligent-content)
- [Formations](#formations)
- [Formation considerations](#formation-considerations)
- [Business Data Cloud versus S/4HANA embedded analytics](#business-data-cloud-versus-s-4hana-embedded-analytics)
- [Business Data Cloud versus SAP BW](#business-data-cloud-versus-sap-bw)
- [Business Data Cloud versus a generic lakehouse](#business-data-cloud-versus-a-generic-lakehouse)
- [Business Data Cloud versus Microsoft Fabric](#business-data-cloud-versus-microsoft-fabric)
- [Business Data Cloud versus Snowflake](#business-data-cloud-versus-snowflake)
- [Data ownership in BDC](#data-ownership-in-bdc)
- [Data quality](#data-quality)
- [Master Data Governance](#master-data-governance)
- [Security and access](#security-and-access)
- [Row-level security](#row-level-security)
- [Source authorization versus analytical authorization](#source-authorization-versus-analytical-authorization)
- [Sensitive data](#sensitive-data)
- [Freshness and operational use](#freshness-and-operational-use)
- [BDC is not an operational event engine](#bdc-is-not-an-operational-event-engine)
- [AI and Business Data Cloud](#ai-and-business-data-cloud)
- [Strong AI use cases](#strong-ai-use-cases)
- [Weak AI use cases](#weak-ai-use-cases)
- [Knowledge graph and semantics](#knowledge-graph-and-semantics)
- [Intelligent supply-chain applications](#intelligent-supply-chain-applications)
- [Commercial and cost model](#commercial-and-cost-model)
- [The hidden cost of coexistence](#the-hidden-cost-of-coexistence)
- [Cost allocation](#cost-allocation)
- [FinOps for analytical workloads](#finops-for-analytical-workloads)
- [Main strengths of Business Data Cloud](#main-strengths-of-business-data-cloud)
- [1. SAP semantics](#1-sap-semantics)
- [2. Data products](#2-data-products)
- [3. Integrated SAP analytical stack](#3-integrated-sap-analytical-stack)
- [4. BW transition](#4-bw-transition)
- [5. Databricks integration](#5-databricks-integration)
- [6. Planning and analytics](#6-planning-and-analytics)
- [7. AI grounding](#7-ai-grounding)
- [8. Managed content](#8-managed-content)
- [Main limitations and traps](#main-limitations-and-traps)
- [Limitation 1: BDC is still a portfolio](#limitation-1-bdc-is-still-a-portfolio)
- [Limitation 2: Product maturity varies](#limitation-2-product-maturity-varies)
- [Limitation 3: Not every SAP dataset is a delivered data product](#limitation-3-not-every-sap-dataset-is-a-delivered-data-product)
- [Limitation 4: Data products do not remove modelling](#limitation-4-data-products-do-not-remove-modelling)
- [Limitation 5: “Zero copy” is scenario-dependent](#limitation-5-zero-copy-is-scenario-dependent)
- [Limitation 6: Business context is not the same as company truth](#limitation-6-business-context-is-not-the-same-as-company-truth)
- [Limitation 7: BW migration can become permanent coexistence](#limitation-7-bw-migration-can-become-permanent-coexistence)
- [Limitation 8: Duplicate semantic layers](#limitation-8-duplicate-semantic-layers)
- [Limitation 9: Another Databricks estate](#limitation-9-another-databricks-estate)
- [Limitation 10: Intelligent content may be narrower than the marketing name](#limitation-10-intelligent-content-may-be-narrower-than-the-marketing-name)
- [Limitation 11: Source data quality remains](#limitation-11-source-data-quality-remains)
- [Limitation 12: Security is multi-layered](#limitation-12-security-is-multi-layered)
- [Limitation 13: Freshness is not universal](#limitation-13-freshness-is-not-universal)
- [Limitation 14: Commercial scope is complex](#limitation-14-commercial-scope-is-complex)
- [Limitation 15: Vendor concentration](#limitation-15-vendor-concentration)
- [Limitation 16: Non-SAP data may still fit better elsewhere](#limitation-16-non-sap-data-may-still-fit-better-elsewhere)
- [When Business Data Cloud is a strong fit](#when-business-data-cloud-is-a-strong-fit)
- [When Business Data Cloud may be excessive](#when-business-data-cloud-may-be-excessive)
- [Target architecture pattern 1: SAP-centred enterprise](#target-architecture-pattern-1-sap-centred-enterprise)
- [Target architecture pattern 2: BDC as SAP data-product layer](#target-architecture-pattern-2-bdc-as-sap-data-product-layer)
- [Target architecture pattern 3: BW transition](#target-architecture-pattern-3-bw-transition)
- [Target architecture pattern 4: AI and data science](#target-architecture-pattern-4-ai-and-data-science)
- [A practical implementation programme](#a-practical-implementation-programme)
- [Phase 1: Define the decision problem](#phase-1-define-the-decision-problem)
- [Phase 2: Inventory the current landscape](#phase-2-inventory-the-current-landscape)
- [Phase 3: Select two or three data products](#phase-3-select-two-or-three-data-products)
- [Phase 4: Define ownership](#phase-4-define-ownership)
- [Phase 5: Create the formation architecture](#phase-5-create-the-formation-architecture)
- [Phase 6: Prove delivered content](#phase-6-prove-delivered-content)
- [Phase 7: Decide copy versus virtual access](#phase-7-decide-copy-versus-virtual-access)
- [Phase 8: Define the BW disposition](#phase-8-define-the-bw-disposition)
- [Phase 9: Integrate the external platform](#phase-9-integrate-the-external-platform)
- [Phase 10: Govern AI consumption](#phase-10-govern-ai-consumption)
- [Phase 11: Measure retirement](#phase-11-measure-retirement)
- [KPIs that matter](#kpis-that-matter)
- [Data-product KPIs](#data-product-kpis)
- [Platform KPIs](#platform-kpis)
- [Semantic KPIs](#semantic-kpis)
- [BW-modernization KPIs](#bw-modernization-kpis)
- [Business KPIs](#business-kpis)
- [AI-readiness KPIs](#ai-readiness-kpis)
- [Common mistakes](#common-mistakes)
- [Questions managers and architects should ask](#questions-managers-and-architects-should-ask)
- [The management conclusion](#the-management-conclusion)

A company has accumulated a familiar SAP data landscape:

- SAP S/4HANA;
- several legacy SAP ERP systems;
- SAP BW;
- SAP Datasphere;
- SAP Analytics Cloud;
- a cloud data lake;
- Databricks or Snowflake;
- dozens of extraction pipelines;
- hundreds of reports;
- several definitions of revenue, inventory and margin.

Every platform contains part of the truth.

Finance trusts BW.

Data scientists trust the lakehouse.

Business users export data to Excel.

AI teams ask for direct access to S/4HANA tables.

Management concludes that the company needs one data platform.

SAP proposes SAP Business Data Cloud.

The presentation promises:

- unified SAP and non-SAP data;
- preserved business context;
- governed data products;
- BW modernization;
- integrated analytics and planning;
- Databricks-based engineering and AI;
- intelligent applications;
- a trusted foundation for AI agents.

All of these capabilities can create value.

But SAP Business Data Cloud does not remove the hardest parts of enterprise data management:

- agreeing on business definitions;
- assigning data ownership;
- correcting poor master data;
- resolving conflicting source systems;
- controlling access;
- proving freshness;
- retiring old reports;
- paying for storage and computation;
- changing how people make decisions.

The most important conclusion is:

> SAP Business Data Cloud can simplify access to SAP business data and preserve more SAP semantics than a generic data platform. It cannot create one trusted enterprise truth unless the company governs the meaning and ownership of that truth.

## What SAP Business Data Cloud is

SAP Business Data Cloud, usually abbreviated as SAP BDC, is a fully managed SaaS portfolio for data, analytics, planning, data engineering and AI.

SAP currently describes it as a managed solution that unifies and governs SAP data, connects third-party data and provides a business data fabric across applications and analytical workloads. Its main components include:

- SAP Datasphere;
- SAP Analytics Cloud;
- SAP Business Warehouse capabilities;
- SAP Databricks;
- data products;
- intelligent content and applications.

SAP announced Business Data Cloud in February 2025 as an evolution of its existing data and analytics products, built in partnership with Databricks. It was not introduced as a completely new database replacing those products. Rather, it brought them into a broader product and commercial experience.

This distinction matters.

> Business Data Cloud is primarily an integrated product and governance layer around several engines, not one universal execution engine.

## What Business Data Cloud is not

Business Data Cloud is not:

- the transactional database of S/4HANA;
- a replacement for SAP application logic;
- a master-data governance process;
- a universal operational integration platform;
- an automatic BW conversion utility;
- a single storage engine;
- a guarantee of zero data duplication;
- a replacement for every existing lakehouse;
- an autonomous AI decision system.

It can support all these areas indirectly.

It does not assume their responsibilities automatically.

## The high-level architecture

A simplified Business Data Cloud architecture is:

```text
SAP applications
S/4HANA | SuccessFactors | Ariba | CX | IBP | other SAP systems
                         |
                         v
SAP-managed data products and application integration
                         |
                         v
SAP Business Data Cloud
 ├─ SAP Datasphere
 │  Semantics, modelling, integration, cataloguing, sharing
 │
 ├─ SAP Analytics Cloud
 │  Reporting, analytics, planning, user consumption
 │
 ├─ SAP Business Warehouse
 │  Existing BW models and BW modernization path
 │
 ├─ SAP Databricks
 │  Data engineering, data science, ML and AI
 │
 ├─ Intelligent content
 │  Preconfigured models, metrics, dashboards and planning content
 │
 └─ Data products
    Governed reusable datasets
                         |
                         v
External data and AI ecosystem
Databricks | Snowflake | hyperscalers | enterprise data platforms
```

Each component has a different responsibility.

The architecture becomes weak when all of them are treated as interchangeable places to store tables and build reports.

## The business data fabric idea

SAP describes Business Data Cloud through the concept of a business data fabric.

A conventional data platform often extracts data from applications and reconstructs the business meaning later.

For example, a data team receives tables containing:

- company code;
- material;
- document category;
- movement type;
- posting date.

The team must understand how those fields represent:

- revenue;
- inventory;
- purchase commitments;
- customer orders;
- production.

SAP’s argument is that Business Data Cloud can preserve more application semantics and deliver curated data products based on SAP business-process definitions.

Conceptually:

```text
Traditional extraction

Application tables
→ technical extraction
→ data lake
→ rebuild joins
→ rebuild definitions
→ dashboard


Business-data-fabric direction

SAP application
→ governed data product
→ preserved semantics and metadata
→ reusable analytical or AI consumption
```

The idea is sound.

Rebuilding SAP semantics repeatedly is expensive and error-prone.

The limitation is that SAP semantics are not automatically the same as the company’s final management semantics.

For example:

- SAP may define document revenue correctly.
- Management may need revenue adjusted for expected rebates.
- Inventory may be technically available but operationally unusable.
- Supplier spend may require cross-system supplier harmonization.

SAP-delivered context is a foundation.

It is not the end of business modelling.

## Component 1: SAP Datasphere

SAP Datasphere is the semantic and data-fabric core of Business Data Cloud.

SAP describes Datasphere as combining:

- data integration;
- cataloguing;
- semantic modelling;
- data warehousing;
- data virtualization;
- governed access across SAP and non-SAP sources.

In a Business Data Cloud architecture, Datasphere typically owns:

- spaces and domain organisation;
- data connections;
- replication and transformation flows;
- semantic models;
- analytical models;
- data-product publication and consumption;
- governed sharing.

## Datasphere spaces

A space is an isolated modelling and resource boundary.

It can represent:

- finance;
- supply chain;
- sales;
- human resources;
- a project;
- a source system;
- a data product.

A space may control:

- users;
- storage;
- workload;
- connections;
- objects;
- permissions.

A useful domain model might be:

```text
Foundation spaces
S/4HANA raw and replicated data

Domain spaces
Finance | Procurement | Sales | Supply Chain

Consumption spaces
Executive reporting | AI features | Regulatory reporting
```

Creating one large space for the whole enterprise weakens governance.

Creating hundreds of narrow spaces increases administration and duplication.

## Semantic modelling

Datasphere can model business entities and relationships such as:

- customer;
- product;
- supplier;
- sales order;
- invoice;
- inventory;
- cost centre.

The semantic layer can define:

- measures;
- dimensions;
- associations;
- currencies;
- units;
- hierarchies;
- analytical behaviour.

This is one of Datasphere’s strongest capabilities.

A raw table can tell a model that a field contains a number.

A semantic model can state that it represents:

> Net sales amount in transaction currency, aggregated by billing date and sales organisation.

That context is useful for:

- Analytics Cloud;
- data consumers;
- AI agents;
- data catalogues.

## Virtualization versus replication

Datasphere can access some data remotely or replicate it locally.

### Virtual access

Advantages:

- less duplication;
- current source data;
- lower storage requirement.

Limitations:

- source-system dependency;
- query latency;
- source workload;
- network dependency;
- limited transformation freedom.

### Replication

Advantages:

- predictable analytical performance;
- reduced source workload during consumption;
- local transformation;
- historical persistence.

Limitations:

- storage;
- latency between source and target;
- reconciliation;
- data-pipeline operation;
- duplicated sensitive data.

The correct choice depends on:

- freshness;
- volume;
- source capacity;
- query pattern;
- regulatory requirement.

“Zero copy” should not be treated as a universal goal.

Sometimes the economically correct design is to create a controlled copy.

## Component 2: SAP Analytics Cloud

SAP Analytics Cloud, or SAC, is the main user-facing analytics and planning layer in the BDC portfolio.

SAP currently describes it as a SaaS platform combining:

- business intelligence;
- enterprise planning;
- predictive analytics;
- analytical applications.

Typical responsibilities include:

- dashboards;
- stories;
- planning models;
- forecasts;
- simulations;
- commentary;
- executive consumption.

## SAC is not the enterprise semantic authority

SAC can contain models and calculations.

But if every dashboard implements its own:

- margin calculation;
- currency logic;
- supplier grouping;
- inventory definition,

the company recreates semantic fragmentation at the presentation layer.

Reusable business semantics should preferably be governed lower in the architecture, for example through:

- source application logic;
- data products;
- Datasphere semantic models;
- approved planning models.

## Live connection versus acquired data

SAC can consume data through different connection and modelling approaches.

The architecture must decide:

- whether SAC queries the source live;
- whether data is imported;
- whether Datasphere provides the model;
- whether planning data is stored in SAC.

The correct answer depends on:

- performance;
- planning requirement;
- security;
- latency;
- source availability.

## Planning

SAC planning can support:

- financial planning;
- workforce planning;
- sales planning;
- operational plans;
- scenario modelling.

But the company should not use SAC to recreate transactional planning engines.

For example:

- MRP remains in S/4HANA.
- Detailed production scheduling remains in PP/DS.
- Network supply planning may remain in IBP.
- SAC can support management plans and scenario comparison.

## Component 3: SAP Databricks

SAP Databricks is a managed Databricks edition delivered as an application inside Business Data Cloud.

SAP describes it as a serverless offering integrated with the SAP landscape, with managed compute and storage, single sign-on and preconfigured Delta Sharing. It supports data engineering, exploratory analysis, machine learning, forecasting, model development and AI workloads.

This provides SAP customers with a serious engineering and data-science environment.

It is not merely a notebook attached to Datasphere.

## Where SAP Databricks fits

SAP Databricks is appropriate for:

- large-scale transformation;
- Spark workloads;
- SQL analytics;
- machine-learning feature engineering;
- model training;
- time-series forecasting;
- unstructured and semi-structured data;
- custom AI applications;
- combining SAP and non-SAP datasets.

## Data sharing

SAP states that SAP Databricks can access Business Data Cloud data products through preconfigured Delta Sharing and can publish data products back into Business Data Cloud.

A possible flow is:

```text
S/4HANA data product
→ Business Data Cloud
→ Delta Share
→ SAP Databricks
→ engineering and ML
→ custom derived data product
→ Datasphere and Analytics Cloud
```

This can reduce custom extraction.

It does not remove the need to govern:

- who can access the share;
- which data is included;
- when it was refreshed;
- whether derived data may be redistributed;
- who owns the resulting model.

## Zero-copy claims require qualification

SAP markets open data sharing with reduced or zero-copy access between supported platforms.

This can be valuable.

But “zero copy” does not mean:

- data never moves anywhere;
- no local tables exist;
- no cache exists;
- no replication flows are required;
- storage cost disappears.

For example, SAP’s documentation for installing intelligent content states that the installation can create:

- replication flows;
- local tables;
- views;
- analytical models;
- initial and delta loads in Datasphere.

A more accurate statement is:

> Business Data Cloud supports copy-reducing and sharing-based patterns for selected scenarios, while other scenarios still use ingestion and replication.

## SAP Databricks versus an existing Databricks estate

Many companies already have Databricks on:

- Azure;
- AWS;
- Google Cloud.

The company should not assume that SAP Databricks automatically replaces it.

Questions include:

- Where do existing non-SAP data products reside?
- Which workspace owns machine-learning operations?
- Can existing pipelines be reused?
- How are Unity Catalog and enterprise governance handled?
- Which compute commitment already exists?
- Is SAP Databricks required to access particular SAP-delivered capabilities?
- Will two Databricks estates create duplicate engineering teams?

SAP Databricks can be attractive where the value of managed SAP integration exceeds the cost of another platform boundary.

## Component 4: SAP data products

Data products are the central architectural concept in Business Data Cloud.

SAP defines a data product as a self-contained dataset exposed for consumption outside its producing application.

SAP-managed data products can be delivered from applications such as SAP S/4HANA Cloud and activated through Business Data Cloud for use in Datasphere, SAP Databricks, HANA Cloud and other supported services.

## What a data product should contain

A mature data product should include:

- clear business purpose;
- defined owner;
- data contract;
- schema;
- semantics;
- refresh expectation;
- quality expectation;
- access policy;
- lifecycle;
- documentation.

Examples:

- Sales Orders;
- Supplier Spend;
- Inventory Position;
- Manufacturing Orders;
- Workforce Skills;
- Journal Entries.

## SAP-managed data products

SAP-managed packages can reduce custom extraction and modelling.

SAP controls their technical lifecycle and updates. SAP’s documentation notes that SAP Technical Support creates, updates and manages the lifecycle of SAP-managed data packages.

Advantages:

- SAP-defined semantics;
- reduced extraction engineering;
- reusable content;
- compatibility with intelligent content;
- less reverse-engineering of application tables.

Limitations:

- only available where SAP has delivered the relevant product;
- source edition and release prerequisites apply;
- delivered fields may not cover customer extensions;
- lifecycle changes are controlled by SAP;
- management definitions may still require extension.

## Custom data products

Customers can create custom data products in Datasphere and share them with supported systems such as SAP Databricks. SAP documents custom data-product publication using Delta Share in Business Data Cloud formations.

A custom data product is useful when the company needs to combine:

- SAP data;
- non-SAP data;
- company-specific calculations;
- harmonized identities;
- derived features.

Example:

```text
SAP billing documents
+ customer rebates
+ freight cost
+ service cost
= Customer Pocket Margin data product
```

## Data product is not a synonym for table

A table becomes a data product only when it has:

- stable meaning;
- ownership;
- service expectation;
- governed consumption.

Publishing every source table as a data product recreates a technical data lake with a new label.

## Data-product granularity

Too broad:

```text
All S/4HANA financial data
```

Too narrow:

```text
One table containing sales-order item schedule lines for one report
```

Better:

```text
Open Sales Order Commitments

Includes:
- order;
- item;
- confirmed schedule;
- customer;
- product;
- requested date;
- value;
- status;
- documented refresh and ownership.
```

## Data contracts and change

A consumer may depend on:

- field;
- data type;
- semantic definition;
- update frequency;
- allowed values.

Data-product changes should be versioned.

A new field is normally safe.

Changing the meaning of an existing measure is not.

## Component 5: Business Warehouse modernization

Business Data Cloud is also SAP’s strategic answer for customers with large BW investments.

This does not mean every BW system is automatically replaced.

SAP currently supports several coexistence and modernization patterns, including:

- existing BW or BW/4HANA integration;
- SAP BW Bridge;
- semantic imports into Datasphere;
- Business Data Cloud Data Product Generator;
- private-cloud BW scenarios.

## Why BW remains important

A mature BW system may contain:

- decades of transformation logic;
- finance reconciliation;
- historical snapshots;
- non-SAP data;
- regulatory reporting;
- thousands of reports;
- process chains;
- planning applications;
- security roles.

Replacing this in one project is rarely rational.

## Data Product Generator for BW

SAP provides the Data Product Generator for selected BW and BW/4HANA versions.

It can extract data from existing InfoProviders into object storage associated with Datasphere and expose it as data products for Business Data Cloud consumption.

SAP currently documents minimum supported levels including:

- SAP BW 7.5 SP24 or higher;
- SAP BW/4HANA 2021 SP04 or higher;
- SAP BW/4HANA 2023.

The documented process also requires specific Business Data Cloud and private-cloud prerequisites.

This is not a universal connector for any historical BW release.

## What the Data Product Generator solves

It can help:

- reuse existing InfoProvider outputs;
- avoid immediately rebuilding all BW logic;
- publish selected BW results as data products;
- expose trusted historical models to Databricks and Datasphere.

## What it does not solve

It does not automatically:

- rationalize obsolete transformations;
- remove duplicate InfoProviders;
- convert every BEx query;
- replace process chains;
- redesign authorizations;
- prove data quality;
- reduce BW operating cost immediately.

It can preserve BW value during transition.

It can also preserve BW complexity if no retirement plan exists.

## BW Bridge

SAP Datasphere BW Bridge provides selected BW modelling capabilities in a cloud environment and supports migration or reuse of established BW skills and artefacts.

It can be useful where:

- ABAP-based extraction remains important;
- BW transformations must be preserved;
- the organisation wants staged migration.

It should not become a permanent landing zone for every new model simply because the BW team knows the tools.

## A sensible BW modernization strategy

Classify BW content into four groups.

### Retain

Examples:

- regulated reporting;
- highly stable financial models;
- complex historical snapshots.

### Publish

Expose trusted BW outputs as governed data products.

### Rebuild

Recreate high-value models in Datasphere or another modern architecture.

### Retire

Remove:

- unused queries;
- duplicate cubes;
- obsolete extractors;
- abandoned process chains.

## The danger of “lift and modernize later”

Moving BW into a private-cloud component may reduce infrastructure responsibility.

It does not reduce model complexity.

Without an explicit decommissioning roadmap, the company can end up paying for:

- BW;
- Datasphere;
- SAC;
- Databricks;
- the existing lakehouse

at the same time.

## Component 6: Intelligent content and applications

SAP currently offers intelligent content across business areas such as:

- finance;
- supply chain;
- people;
- spend;
- revenue;
- Cloud ERP.

The terminology has evolved from “intelligent applications” toward “intelligent content” in current product materials.

## What these applications contain in practice

SAP documentation describes intelligent applications as prebuilt Business Data Cloud content delivered through:

- SAP application data products;
- Datasphere models;
- analytical models;
- SAP Analytics Cloud stories or analytical applications.

They may also include:

- predefined KPIs;
- planning models;
- AI or ML models;
- recommended insights.

This is valuable.

But it is important to understand the current practical scope.

> Many intelligent applications are primarily managed analytical content and models, not fully autonomous operational applications.

## Installation model

When eligible intelligent content is installed, SAP documentation states that the system can create:

- protected Datasphere spaces;
- connections;
- replication flows;
- local tables;
- views;
- analytical models;
- an SAC workspace;
- SAC stories.

This is more substantial than importing one dashboard.

It also means:

- source prerequisites matter;
- entitlements matter;
- permissions matter;
- data loads must be monitored;
- custom extensions must respect protected content.

## Entitlements

Availability is not only technical.

SAP’s documentation states that installation requires commercial entitlement to the relevant SAP business solution and the intelligent application or content.

For example, access to private-cloud ERP intelligent content may require the corresponding Cloud ERP Intelligence entitlement.

Do not build the business case using content shown in a demonstration until the order form is checked.

## Extending intelligent content

Delivered content can provide a strong starting point.

Companies will still need to extend:

- organisational mappings;
- management hierarchies;
- custom fields;
- calculation logic;
- non-SAP data;
- security;
- targets.

The extension model should avoid changing SAP-protected artefacts directly.

## Formations

Business Data Cloud uses the concept of formations to connect the BDC cockpit with provisioned systems such as:

- Datasphere;
- Analytics Cloud;
- SAP Databricks;
- source SAP business applications.

SAP for Me is used to provision and organise these formations.

A formation is effectively an administrative and integration grouping.

It determines which systems participate in a particular BDC landscape.

## Formation considerations

A large company may need to decide:

- one global formation;
- formations by region;
- formations by legal or data-residency boundary;
- separate development, test and production formations;
- source-system participation.

Poor formation design can create:

- access complexity;
- duplicate tenants;
- unclear promotion paths;
- data-residency problems.

## Business Data Cloud versus S/4HANA embedded analytics

S/4HANA contains embedded analytical capabilities.

These can be appropriate for:

- operational reporting;
- current transactions;
- process monitoring;
- role-based Fiori applications.

Business Data Cloud is more appropriate where the company needs:

- cross-application data;
- history;
- harmonization;
- enterprise analytics;
- planning;
- data science;
- reusable data products.

Do not move every operational report out of S/4HANA.

An overdue-delivery worklist may belong close to the transaction.

A five-year customer-profitability model belongs in the analytical platform.

## Business Data Cloud versus SAP BW

| Requirement | SAP BW | Business Data Cloud direction |
|---|---|---|
| Mature historical enterprise warehouse | Strong | Can consume or modernize |
| Existing ABAP extractors | Strong | Integration and migration options |
| New semantic data fabric | Limited by architecture | Datasphere-centred |
| Cloud planning and dashboards | Requires adjacent products | SAC integrated |
| Data science and ML | External integration | SAP Databricks |
| SAP-managed application data products | Not the original model | Core BDC concept |
| Existing regulated reports | Often already proven | Migration may add risk |
| Open data ecosystem | Possible through integration | Strategic product direction |

BDC does not make BW immediately obsolete.

It provides a target architecture in which BW can be:

- retained;
- moved;
- published;
- gradually reduced.

## Business Data Cloud versus a generic lakehouse

A generic lakehouse such as Databricks or Snowflake is strong in:

- open data engineering;
- broad data ingestion;
- machine learning;
- scalable storage and compute;
- non-SAP ecosystems.

Business Data Cloud is differentiated by:

- SAP business semantics;
- SAP-managed data products;
- direct alignment with SAP applications;
- Datasphere semantic modelling;
- SAP Analytics Cloud planning and consumption;
- BW transition options.

A generic platform may remain better when:

- most enterprise data is non-SAP;
- an established data platform already exists;
- engineering standards are cloud-native;
- SAP represents only one source domain;
- vendor concentration is a concern.

A hybrid model is often the correct answer.

## Business Data Cloud versus Microsoft Fabric

Microsoft Fabric can be attractive where the company is deeply standardised on:

- Azure;
- Power BI;
- Microsoft 365;
- OneLake;
- Microsoft data engineering.

Business Data Cloud may be stronger for preserving SAP semantics and consuming SAP-managed data products.

The decision should not be based on which dashboard tool looks better.

It should consider:

- existing skills;
- SAP extraction cost;
- semantic ownership;
- non-SAP data volume;
- platform commitments;
- governance;
- AI ecosystem;
- total cost.

## Business Data Cloud versus Snowflake

Snowflake may remain the enterprise platform for:

- cross-domain data sharing;
- SQL analytics;
- multi-cloud data;
- broad partner ecosystem.

BDC can be used as the governed SAP semantic and data-product layer feeding or interoperating with Snowflake.

SAP currently markets an open data ecosystem that includes interoperability with providers such as Snowflake, Collibra, Confluent and Google BigQuery.

The company does not need to move all non-SAP data into BDC merely to gain governed SAP data access.

## Data ownership in BDC

A robust ownership model might be:

| Object | Primary authority |
|---|---|
| Sales order | S/4HANA |
| Employee | SuccessFactors or HR authority |
| Supplier | Governed master-data process |
| Source financial posting | S/4HANA Finance |
| Delivered SAP data product | SAP and source application contract |
| Enterprise revenue definition | Finance data owner |
| Semantic model | Domain data owner |
| Analytics story | Reporting product owner |
| ML feature set | Data-science product owner |
| AI recommendation | AI service owner |
| Final transactional action | Source application |

BDC should not replace the source system’s authority.

It should expose and combine it.

## Data quality

Business Data Cloud can govern and distribute data.

It does not correct poor source data automatically.

Examples:

- duplicate suppliers;
- incorrect units;
- missing product hierarchy;
- inconsistent company codes;
- invalid dates;
- unclosed orders.

The sequence should be:

```text
Source controls
→ master-data governance
→ quality rules
→ data product
→ analytical consumption
```

Do not wait until data reaches the analytical platform before assigning an owner.

## Master Data Governance

SAP includes Master Data Governance in the broader BDC and business-data-fabric positioning.

MDG can improve:

- identity;
- lifecycle;
- approval;
- duplicate prevention;
- distribution.

But BDC does not automatically include a complete MDG implementation for every domain.

It remains a separate governance process and product scope.

## Security and access

BDC security crosses several layers:

- source application;
- BDC cockpit;
- formation;
- Datasphere space;
- data product;
- analytical model;
- SAC story;
- Databricks workspace;
- external share.

## Row-level security

A user may be permitted to see:

- only one company code;
- one country;
- one sales organisation;
- one employee group.

SAP documents permission-record and scoped-role mechanisms for delivered intelligent content.

Security must be tested end to end.

A restricted SAC story is insufficient if the same user can access the underlying table through another tool.

## Source authorization versus analytical authorization

Possible approaches include:

- inherit source permissions;
- reproduce them in BDC;
- define analytical access separately.

Each has limitations.

Source authorization may be too transactional.

Replicated authorization requires synchronization.

Independent analytical authorization creates another governance model.

## Sensitive data

Pay special attention to:

- payroll;
- personal data;
- bank details;
- customer data;
- pricing;
- supplier terms;
- product cost;
- health data.

Data-product reuse increases the number of potential consumers.

The contract must define who may access each field and purpose.

## Freshness and operational use

A BDC model may be:

- live;
- virtual;
- delta replicated;
- batch loaded;
- manually refreshed.

Every data product should state its freshness.

Example:

```text
Inventory Position data product

Refresh:
Every 15 minutes

Use:
Management and replenishment analysis

Not suitable for:
Binding e-commerce reservation
```

A dashboard labelled “real time” is not necessarily an operational commitment service.

## BDC is not an operational event engine

Business Data Cloud can provide insights and support intelligent workflows.

But transactional orchestration should remain in:

- S/4HANA;
- workflow engine;
- event mesh;
- integration layer;
- operational applications.

An AI agent should not query yesterday’s replicated data and autonomously change today’s customer order.

## AI and Business Data Cloud

SAP increasingly positions Business Data Cloud as the trusted knowledge foundation for Business AI and agents.

This direction has merit.

AI systems need:

- context;
- semantics;
- relationships;
- governed access;
- consistent identifiers.

## Strong AI use cases

- financial anomaly analysis;
- supply-risk detection;
- demand forecasting;
- customer-margin modelling;
- supplier classification;
- inventory optimization;
- feature engineering;
- natural-language analytics;
- agent grounding.

## Weak AI use cases

- asking an agent to interpret raw SAP tables;
- releasing transactions based on stale analytical data;
- assuming a data product is free from bias;
- using one broad dataset for every agent;
- giving agents unrestricted Databricks or Datasphere access.

## Knowledge graph and semantics

SAP’s current BDC positioning includes connected knowledge and business context for applications and AI.

This can help represent relationships such as:

```text
Customer
→ places
Sales Order
→ contains
Product
→ supplied by
Supplier
→ operates at
Location
```

The practical value depends on:

- quality of relationships;
- stable identity;
- current state;
- permitted access;
- business ownership.

A knowledge graph built on duplicate business partners becomes a sophisticated representation of bad identity.

## Intelligent supply-chain applications

SAP currently positions Supply Chain Intelligence in BDC as connecting planning, procurement, manufacturing, logistics, inventory and finance data, with simulation and AI-based recommendations.

This may help answer questions such as:

- Which supplier disruption affects revenue?
- Which inventory shortage threatens high-margin customers?
- What is the financial impact of delayed production?
- Which sourcing alternative is available?

The quality of these insights depends on linking:

- supplier;
- material;
- order;
- inventory;
- production;
- customer;
- cost.

The dashboard is the final layer.

The difficult work is the governed cross-domain model underneath.

## Commercial and cost model

SAP’s public pricing page currently directs customers to sales engagement and does not expose a simple universal price list.

The commercial model must be assessed through the actual contract.

Potential cost areas include:

- BDC base entitlement;
- Datasphere capacity;
- SAC users and planning;
- Databricks compute;
- storage;
- data egress;
- intelligent-content entitlements;
- BW private-cloud component;
- source-application entitlements;
- implementation;
- migration;
- parallel operation.

## The hidden cost of coexistence

During transition, the company may operate:

- legacy BW;
- BW private cloud;
- Datasphere;
- SAC;
- external lakehouse;
- SAP Databricks;
- Power BI.

This can be rational temporarily.

It becomes a problem when no platform has a retirement date.

## Cost allocation

The company should assign cost by:

- domain;
- product;
- workload;
- environment;
- team;
- data product.

Otherwise, one analytical workload can consume capacity paid for by the whole enterprise.

## FinOps for analytical workloads

Databricks, HANA and data replication can generate variable costs.

Controls should include:

- workload limits;
- auto-stop;
- environment sizing;
- query monitoring;
- storage lifecycle;
- cost attribution;
- development quotas.

“Managed SaaS” does not mean “cost is automatically managed.”

## Main strengths of Business Data Cloud

## 1. SAP semantics

BDC can reduce the need to rebuild the meaning of SAP application data repeatedly.

## 2. Data products

Reusable application and custom data products can create clearer contracts between producers and consumers.

## 3. Integrated SAP analytical stack

Datasphere, SAC, BW and SAP Databricks can be administered as a connected portfolio rather than unrelated products.

## 4. BW transition

BDC provides a path to reuse and publish existing BW value instead of requiring immediate replacement.

## 5. Databricks integration

SAP customers gain an advanced data-engineering and machine-learning environment with managed SAP data access.

## 6. Planning and analytics

SAC connects reporting with enterprise planning.

## 7. AI grounding

Business semantics and governed data products can provide stronger context for AI applications.

## 8. Managed content

Delivered intelligent content can shorten implementation for standard analytical use cases.

## Main limitations and traps

## Limitation 1: BDC is still a portfolio

The name suggests one platform.

The architecture contains several products, runtimes, roles and administration models.

## Limitation 2: Product maturity varies

Datasphere, SAC and BW are established.

Some BDC-specific data products, intelligent content and integration patterns are newer and continue to evolve.

Verify availability for the exact source product and region.

## Limitation 3: Not every SAP dataset is a delivered data product

Companies may still need:

- standard extractors;
- CDS views;
- APIs;
- replication;
- custom integration.

## Limitation 4: Data products do not remove modelling

The delivered product may still need:

- harmonization;
- currency conversion;
- customer extensions;
- historical logic;
- non-SAP context.

## Limitation 5: “Zero copy” is scenario-dependent

Some patterns use sharing.

Others use replication flows and local tables.

## Limitation 6: Business context is not the same as company truth

SAP semantics may need adjustment for:

- management reporting;
- rebates;
- internal allocations;
- custom organisational models.

## Limitation 7: BW migration can become permanent coexistence

The company adds BDC without retiring any BW content.

## Limitation 8: Duplicate semantic layers

Definitions may remain in:

- BW;
- Datasphere;
- SAC;
- Databricks;
- Power BI.

## Limitation 9: Another Databricks estate

Customers with existing Databricks may create duplicate workspaces, governance and skills.

## Limitation 10: Intelligent content may be narrower than the marketing name

Current delivered content may primarily comprise:

- data products;
- models;
- dashboards;
- planning content.

It should not automatically be interpreted as autonomous operational intelligence.

## Limitation 11: Source data quality remains

BDC can expose bad master and transactional data more efficiently.

## Limitation 12: Security is multi-layered

Permissions can diverge between:

- source;
- Datasphere;
- SAC;
- Databricks;
- external consumers.

## Limitation 13: Freshness is not universal

Replicated analytical data may be unsuitable for operational decisions.

## Limitation 14: Commercial scope is complex

Different capabilities and intelligent content may require additional entitlements.

## Limitation 15: Vendor concentration

Using SAP for:

- applications;
- data fabric;
- analytics;
- planning;
- AI;
- data engineering

can simplify accountability.

It also increases strategic dependence.

## Limitation 16: Non-SAP data may still fit better elsewhere

BDC should not become the destination for every log, image, clickstream and scientific dataset merely because SAP is important.

## When Business Data Cloud is a strong fit

BDC deserves serious consideration when:

- SAP applications contain a large part of the company’s critical data;
- BW has major reusable business logic;
- extracting SAP semantics is expensive;
- Datasphere or SAC is already strategic;
- planning and analytics need stronger integration;
- governed SAP data products are valuable;
- the company wants managed Databricks access close to SAP context;
- AI initiatives require trusted SAP business data.

## When Business Data Cloud may be excessive

BDC may be premature or excessive when:

- SAP is a relatively small part of the data landscape;
- the company already has a mature enterprise data platform;
- only a few operational SAP reports are needed;
- BW already satisfies stable reporting with no modernization case;
- the organisation lacks data-product ownership;
- management expects a platform purchase to solve data governance;
- no BDC-delivered use case has measurable value.

## Target architecture pattern 1: SAP-centred enterprise

```text
SAP applications
        |
SAP-managed data products
        |
Business Data Cloud
 ├─ Datasphere semantic layer
 ├─ SAC analytics and planning
 ├─ BW modernization
 └─ SAP Databricks AI and engineering
        |
Governed non-SAP data integration
```

Best fit:

- SAP-dominant business;
- strong SAP analytics team;
- substantial BW estate.

## Target architecture pattern 2: BDC as SAP data-product layer

```text
SAP applications
        |
Business Data Cloud
SAP semantics and governed SAP data products
        |
        +------------------+
        |                  |
Enterprise lakehouse   SAP Analytics Cloud
Databricks/Snowflake   SAP-focused analytics
```

Best fit:

- established enterprise data platform;
- need for cleaner SAP access;
- no desire to centralize everything in SAP.

This may be the most rational model for many large organisations.

## Target architecture pattern 3: BW transition

```text
Existing BW
    |
Data Product Generator
    |
Business Data Cloud
    |
Datasphere and SAC
    |
Selected models rebuilt
    |
BW content retired gradually
```

Best fit:

- mature BW;
- no tolerance for a big-bang rewrite;
- need to retain trusted reporting.

## Target architecture pattern 4: AI and data science

```text
SAP data products
        |
SAP Databricks
        |
SAP and non-SAP feature engineering
        |
ML model or analytical data product
        |
Datasphere / SAC / operational workflow
```

Best fit:

- forecasting;
- anomaly detection;
- AI models;
- advanced analytics.

The model output should not update SAP transactions directly without a controlled workflow and validation layer.

## A practical implementation programme

## Phase 1: Define the decision problem

Do not start with:

> Implement Business Data Cloud.

Start with:

- reduce the cost of extracting S/4HANA data;
- modernize BW;
- standardize finance KPIs;
- connect supply-chain and financial impact;
- prepare governed data for AI.

## Phase 2: Inventory the current landscape

Record:

- source systems;
- BW models;
- data lake;
- BI tools;
- planning tools;
- reports;
- interfaces;
- semantic definitions;
- cost.

## Phase 3: Select two or three data products

Good pilots:

- open sales orders;
- inventory and costing;
- supplier spend;
- working capital.

Avoid starting with “all enterprise data.”

## Phase 4: Define ownership

For each data product:

- business owner;
- technical owner;
- source;
- consumers;
- freshness;
- quality;
- security;
- lifecycle.

## Phase 5: Create the formation architecture

Decide:

- systems;
- tenants;
- environments;
- regions;
- lifecycle path;
- separation.

## Phase 6: Prove delivered content

Install and evaluate relevant intelligent content where entitled.

Compare:

- delivered definition;
- company definition;
- source coverage;
- custom-field support;
- performance;
- security.

## Phase 7: Decide copy versus virtual access

For each workload, document:

- volume;
- latency;
- source impact;
- transformation;
- history;
- cost.

## Phase 8: Define the BW disposition

For every major BW object:

- retain;
- publish;
- rebuild;
- retire.

## Phase 9: Integrate the external platform

Define whether:

- BDC is the enterprise platform;
- BDC supplies SAP data products to the enterprise platform;
- workloads are split by domain.

## Phase 10: Govern AI consumption

Every AI use case should specify:

- approved data products;
- allowed fields;
- freshness;
- security;
- model;
- output authority.

## Phase 11: Measure retirement

A BDC programme should remove:

- pipelines;
- duplicate models;
- unused reports;
- infrastructure;
- manual reconciliations.

Adding new capability without retiring old complexity is not modernization.

## KPIs that matter

## Data-product KPIs

- consumers;
- freshness compliance;
- schema changes;
- quality failures;
- reuse;
- time to access;
- owner coverage.

## Platform KPIs

- storage;
- compute;
- query performance;
- pipeline failures;
- source-system impact;
- cost by domain;
- idle resource.

## Semantic KPIs

- duplicate business definitions;
- reconciliation differences;
- unmanaged measures;
- data lineage coverage.

## BW-modernization KPIs

- objects retired;
- reports migrated;
- process chains removed;
- operating cost reduced;
- parallel-run duration.

## Business KPIs

- reporting cycle time;
- reconciliation effort;
- planning latency;
- decision lead time;
- forecast quality;
- working-capital visibility.

## AI-readiness KPIs

- data products approved for AI;
- data provenance;
- sensitive-field controls;
- feature reuse;
- model errors caused by data quality.

## Common mistakes

### Mistake 1: Calling BDC one database

Teams fail to design responsibilities across Datasphere, SAC, BW and Databricks.

### Mistake 2: Buying BDC without a use case

The platform becomes another empty strategic layer.

### Mistake 3: Publishing raw tables as data products

Technical complexity receives a new label.

### Mistake 4: Rebuilding SAP semantics in Databricks

The architecture loses the main value BDC was supposed to provide.

### Mistake 5: Recreating every calculation in SAC

Dashboard logic becomes ungoverned.

### Mistake 6: Assuming delivered content matches company reporting

Finance discovers different definitions after implementation.

### Mistake 7: Promising zero replication

The design later requires local tables and delta loads.

### Mistake 8: Moving BW without rationalizing it

Technical debt becomes cloud technical debt.

### Mistake 9: Operating two Databricks platforms without ownership

Data scientists do not know where new workloads belong.

### Mistake 10: Giving AI broad BDC access

Agents receive payroll, pricing or personal data unnecessarily.

### Mistake 11: Using analytical data for binding operational decisions

Freshness and reservation are insufficient.

### Mistake 12: Ignoring entitlements

A demonstrated data package or intelligent application is not included in the signed contract.

### Mistake 13: Assuming managed SaaS means no operations

Pipelines, security, cost, models and data quality still require ownership.

### Mistake 14: Moving every non-SAP dataset to BDC

The platform becomes an expensive generic lake.

### Mistake 15: Never retiring the old stack

The company pays for modernization and legacy indefinitely.

## Questions managers and architects should ask

1. Which business problem requires Business Data Cloud?
2. What is the target role of Datasphere?
3. What remains in BW?
4. What belongs in SAP Databricks?
5. What remains in the existing enterprise lakehouse?
6. Which SAP-managed data products are actually available?
7. Which source editions and releases are supported?
8. Which intelligent content is commercially entitled?
9. Which content is a dashboard, and which performs a real operational function?
10. Who owns each data product?
11. What is its freshness commitment?
12. Is access virtual, replicated or shared?
13. Where is the historical record stored?
14. Which system owns the semantic definition?
15. How are custom S/4HANA fields included?
16. How are source authorizations reflected?
17. Can a user bypass SAC security through Datasphere or Databricks?
18. Which data may AI agents access?
19. Is the data current enough for the proposed action?
20. How are schema changes communicated?
21. How is BW content classified for retirement?
22. How long will parallel platforms operate?
23. What is the compute and storage cost by domain?
24. Does SAP Databricks duplicate an existing estate?
25. Which existing extraction pipelines will be removed?
26. Which reports will be retired?
27. Is the organisation building reusable products or another project warehouse?
28. What is the exit architecture?
29. Can data be shared with the broader enterprise ecosystem?
30. What measurable business outcome justifies the platform?

## The management conclusion

SAP Business Data Cloud is a significant change in SAP’s data strategy.

It brings together:

- SAP Datasphere;
- SAP Analytics Cloud;
- SAP BW modernization;
- SAP Databricks;
- governed data products;
- intelligent analytical content.

Its strongest value is not that it stores more data.

Its value is the possibility of accessing SAP business data without repeatedly destroying and rebuilding its meaning.

Its most credible uses are:

- governed SAP data products;
- cross-application analytics;
- BW modernization;
- enterprise planning;
- advanced engineering and AI through Databricks;
- semantically grounded AI applications.

Its main risk is becoming another broad platform layered on top of:

- BW;
- Datasphere;
- SAC;
- lakehouse;
- Power BI;
- existing Databricks,

without retiring anything or clarifying ownership.

The decisive question is not:

> Is SAP Business Data Cloud the future of SAP analytics?

SAP has clearly positioned it as the strategic direction.

The useful question is:

> Which part of our current data landscape becomes simpler, cheaper, more governed or more reusable because Business Data Cloud exists?

A good implementation has a precise answer:

- these SAP extractions disappear;
- these BW models remain temporarily;
- these data products become authoritative;
- this external platform continues to own non-SAP engineering;
- these dashboards are retired;
- these AI use cases consume governed semantics;
- these costs and reconciliations are removed.

A weak implementation says:

> All our data will be unified for AI.

That is not an architecture.

It is a future problem described as a strategy.

---

### SAP Business Data Cloud architecture checklist

- [ ] BDC is understood as an integrated portfolio, not one database.
- [ ] The business problem is defined before platform selection.
- [ ] Datasphere has a clear semantic and modelling role.
- [ ] SAC owns governed analytics and planning consumption.
- [ ] SAP Databricks has a defined engineering and AI role.
- [ ] Existing Databricks or lakehouse platforms are considered.
- [ ] BW content is classified as retain, publish, rebuild or retire.
- [ ] Data Product Generator prerequisites are verified.
- [ ] SAP-managed data products are confirmed for the exact source edition.
- [ ] Custom fields and extensions have an inclusion strategy.
- [ ] Every data product has a business owner.
- [ ] Data contracts include freshness, quality and lifecycle.
- [ ] Raw tables are not presented as business data products.
- [ ] Semantic definitions are governed outside individual dashboards.
- [ ] Virtual, replicated and shared-access patterns are selected deliberately.
- [ ] Zero-copy claims are validated per scenario.
- [ ] Formation design covers environment, region and source participation.
- [ ] Intelligent content entitlements are verified contractually.
- [ ] Delivered content is compared with company definitions.
- [ ] Protected SAP content is extended through supported patterns.
- [ ] Source-system authorization and analytical authorization are reconciled.
- [ ] Row-level security is tested across every consumption path.
- [ ] Sensitive fields are minimised.
- [ ] Data-product use by AI is explicitly approved.
- [ ] Analytical data is not treated as an operational reservation service.
- [ ] BW, Datasphere, SAC and Databricks calculations do not compete.
- [ ] Compute and storage costs are allocated to domains.
- [ ] Parallel-run periods have end dates.
- [ ] Legacy reports and pipelines have retirement owners.
- [ ] Non-SAP data remains on the economically appropriate platform.
- [ ] The architecture supports interoperability rather than forced centralisation.
- [ ] Benefits are measured through removed extraction, reconciliation and decision effort.
- [ ] The company can explain what becomes simpler because of BDC.

### Sources and further reading

SAP currently defines Business Data Cloud as a fully managed SaaS solution combining SAP and third-party data within a business data fabric and bringing together Datasphere, Analytics Cloud, Business Warehouse, SAP Databricks, data products and intelligent content.

SAP Datasphere currently provides data integration, cataloguing, semantic modelling, data warehousing and virtualization across SAP and non-SAP sources.

SAP Databricks is currently a serverless, SAP-managed Databricks edition inside BDC, with preconfigured Delta Sharing, SAP single sign-on and support for data engineering, ML, AI and publication of derived data products.

SAP-managed data products are reusable application datasets that can be activated through BDC and consumed in supported services such as Datasphere, SAP Databricks and HANA Cloud.

Custom data products can be published from Datasphere through Delta Share to supported systems in a Business Data Cloud formation.

SAP currently supports several BW integration and modernization patterns, including Data Product Generator, BW Bridge, semantic import and legacy connections.

The Data Product Generator currently has defined BW release prerequisites and requires a compatible Business Data Cloud and private-cloud setup.

Current intelligent content is delivered through SAP application data products, Datasphere models and SAP Analytics Cloud stories or analytical applications, with separate commercial entitlements and installation prerequisites.

*Reviewed: July 2026. SAP Business Data Cloud capabilities, data-product availability, intelligent content, source-system support, entitlements and regional availability are evolving. Final architecture should be validated against the exact SAP source editions, current Help documentation, service catalogue, SAP Notes and signed commercial order forms.*

## Continue exploring

- [Do You Actually Need RISE with SAP? What It Is, What It Includes, and Where Companies Get Trapped](/blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [SAP Quality Management Explained: From Inspection Planning to Supplier Quality, Production Control, Complaints, CAPA, and Certificates](/blog/sap-quality-management-explained-from-inspection-planning-to-supplier/)
