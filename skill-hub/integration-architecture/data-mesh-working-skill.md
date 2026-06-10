---
layout: default
title: "Data Mesh Working Skill"
description: "Apply data mesh principles to SAP and enterprise landscapes by identifying domains, defining data products, assigning ownership, and choosing integration patterns."
permalink: /skill-hub/integration-architecture/data-mesh-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">Data Mesh</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Data Mesh Working Skill</h1>
  <p class="lead">Turn centralized data bottlenecks into domain-owned data products with clear contracts, discoverable interfaces, and federated governance that works in SAP and mixed landscapes.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you identify domains in an enterprise landscape, define data products with clear output ports and ownership, assign data product owners, establish lightweight federated governance, and choose integration patterns that connect domains without recentralizing everything into a single warehouse team.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Central data warehouse or IT team is a bottleneck for domain analytics needs.</li>
      <li>Domain teams cannot access their own data without a three-week ticket to a central team.</li>
      <li>New analytics requirements cross multiple SAP modules and no one owns the cross-module view.</li>
      <li>Master data centralization is causing delays and quality disputes.</li>
      <li>You need to expose SAP domain data to external consumers with clear contracts and SLAs.</li>
      <li>A data lake project is becoming a data swamp because ownership and schema are undefined.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: Finance team waits three weeks for a new warehouse field</h3>
    <p>The central data warehouse team owns all ETL and schema changes. When Finance needs a new field from SAP for a regulatory report, the request sits in a backlog. Finance starts building shadow spreadsheets. The data becomes inconsistent.</p>
    <h3>Situation 2: Cross-module analytics with no owner</h3>
    <p>Analytics needs order data from SD, inventory from MM, and production status from PP. Each module team owns its application but no one owns the integrated data product. Reports are built ad hoc and break when any module upgrades.</p>
    <h3>Situation 3: Domain team wants to expose data but lacks contract skills</h3>
    <p>The procurement team knows their data and wants to expose a supplier performance data product. They do not know how to define an output port, schema, or SLA. IT offers a generic extract, which lacks quality guarantees and consumer support.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Domain map: business domains and their boundaries.</li>
      <li>Existing data landscape: warehouses, lakes, marts, SAP modules, external systems.</li>
      <li>Data product candidates: reports, APIs, events, files that domains already produce or need.</li>
      <li>Current ownership model: who owns data quality today.</li>
      <li>Integration capabilities: middleware, API management, event brokers, CDC tools.</li>
      <li>Governance framework: existing standards for security, privacy, quality.</li>
      <li>Consumer list: who uses data from each domain today.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which domain is the authoritative source for this data?</li>
      <li>What is the data product's output port: API, event stream, file, or analytical model?</li>
      <li>Who owns the quality, schema, and SLA of this data product?</li>
      <li>How do consumers discover that this data product exists?</li>
      <li>What is the SLA for data freshness, and how is it measured?</li>
      <li>How is access controlled: role-based, attribute-based, or consumer-specific?</li>
      <li>What happens when the source schema changes?</li>
      <li>Is this data product reusable, or is it a one-off extract?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify domains.</strong> Map business domains based on organizational boundaries, data ownership, and process autonomy. Avoid purely technical boundaries.</li>
      <li><strong>Map data products per domain.</strong> For each domain, list data it produces that other domains or systems consume. Name each data product clearly.</li>
      <li><strong>Define output ports.</strong> For each data product, specify the interface: synchronous API, event stream, batch file, or analytical export. Match the port to consumer needs.</li>
      <li><strong>Assign ownership.</strong> Name a business owner (quality, semantics) and a technical owner (schema, infrastructure, SLA) for each data product.</li>
      <li><strong>Create a data product catalog.</strong> Register each product with name, owner, description, output ports, schema location, SLA, and consumer onboarding path.</li>
      <li><strong>Define consumer onboarding.</strong> Document how a new consumer requests access, what compatibility checks are required, and how schema changes are communicated.</li>
      <li><strong>Establish federated governance.</strong> Define lightweight standards: naming conventions, schema versioning, access control patterns, quality minimums. Do not create a central committee for every decision.</li>
      <li><strong>Validate with a pilot consumer.</strong> Have one domain publish a data product and one consumer subscribe. Measure freshness, quality, and onboarding friction. Fix before scaling.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If data is used only within one domain, keep it internal; do not publish as a data product.</li>
      <li>If data is consumed by two or more domains, publish it as a data product with a defined output port.</li>
      <li>If freshness requirement is under one hour, use an event or API; if batch is acceptable, use a scheduled extract.</li>
      <li>If no domain owner exists, assign one before publishing; unowned data products become swamps.</li>
      <li>If governance is missing, start with lightweight standards and a small governance group, not a large committee.</li>
      <li>If SAP is the source, respect SAP licensing and data model constraints; do not expose raw tables directly.</li>
      <li>If a data product has no consumers after six months, deprecate it.</li>
      <li>If a consumer needs a cross-domain view, create a consumer-specific analytical model that references domain data products, not a new central warehouse.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Domain Map</strong> — Domains, boundaries, and data product candidates.</li>
      <li><strong>Data Product Definitions</strong> — One per product: owner, output ports, schema, SLA. See template below.</li>
      <li><strong>Data Product Catalog</strong> — Discoverable registry of all products.</li>
      <li><strong>Ownership Matrix</strong> — Business and technical owners per product. Link to <a href="/skill-hub/artifact-templates/">Interface Ownership Matrix template</a>.</li>
      <li><strong>Integration Pattern Decisions</strong> — ADR for how each product connects to consumers.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Data Product Definition</h3>
    <pre><code>---
artifact: Data Product Definition
id: DP-001
status: draft | published | deprecated
---

## Data product name
<!-- Clear, domain-scoped name: Procurement.SupplierPerformance -->

## Domain
<!-- Owning business domain -->

## Description
<!-- What this product contains and what it is for -->

## Owner
<!-- Business owner + technical owner -->

## Output ports
| Port | Type | Interface | SLA | Consumers |
|------|------|-----------|-----|-----------|
| API | Synchronous | REST / OData | p99 < 500ms | CRM, Portal |
| Event stream | Asynchronous | Kafka topic | < 5 min lag | Analytics |
| Batch export | Scheduled | Parquet to S3 | Daily 06:00 | Data science |

## Schema
<!-- Link to schema registry or document fields, types, constraints -->

## Quality SLAs
| Metric | Target | Measurement |
|--------|--------|-------------|
| Completeness | > 99.5% | Daily audit |
| Freshness | < 1 hour | Last update timestamp |
| Accuracy | Zero known defects | Monthly review |

## Access control
<!-- Who can request access and how -->

## Consumer onboarding
<!-- Steps to become a consumer: request, compatibility check, contract, access grant -->

## Change process
<!-- How schema or SLA changes are communicated -->

## Deprecation policy
<!-- Notice period and migration support -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every data product has a named business owner and technical owner.</li>
      <li>Output port is defined with interface type and SLA.</li>
      <li>Schema is documented and versioned.</li>
      <li>Consumer onboarding path is documented and tested.</li>
      <li>Quality SLAs are stated and measurable.</li>
      <li>Access control is defined.</li>
      <li>Change process is documented.</li>
      <li>Data product is registered in the catalog.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating data mesh as a technology project. <strong>Consequence:</strong> The organization buys a data catalog and Kafka but keeps central IT ownership; nothing changes.</li>
      <li><strong>Mistake:</strong> Centralizing governance instead of federating it. <strong>Consequence:</strong> Domain teams still wait for committee approval, recreating the bottleneck.</li>
      <li><strong>Mistake:</strong> Publishing data without ownership. <strong>Consequence:</strong> Schema changes break consumers and no one is accountable.</li>
      <li><strong>Mistake:</strong> Ignoring SAP-specific constraints. <strong>Consequence:</strong> Licensing violations, exposed internal data models, or unsupported direct table access.</li>
      <li><strong>Mistake:</strong> Creating a data product for every table. <strong>Consequence:</strong> Catalog noise, low-quality products, and consumer confusion.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Gather context first:</strong> Collect the domain map, existing data landscape, and current ownership model before proposing data products.</li>
      <li><strong>Focus on ownership and contracts, not tools:</strong> Do not recommend technology before ownership is clear.</li>
      <li><strong>Produce artifacts:</strong> Generate a Domain Map and at least one Data Product Definition. Do not stop at conceptual recommendations.</li>
      <li><strong>Avoid generic language:</strong> Do not write "data mesh decentralizes data ownership." Write "Assign the Procurement domain owner for the SupplierPerformance data product."</li>
      <li><strong>Handle missing information:</strong> If domain boundaries are unclear, propose boundaries based on existing org structure and process ownership, flagging them as assumptions.</li>
      <li><strong>Link to Atlas:</strong> Reference <a href="/atlas/concepts/data-mesh-for-sap-landscapes/">Data Mesh for SAP Landscapes</a> for SAP-specific constraints and <a href="/atlas/concepts/data-contracts/">Data Contracts</a> for contract design.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Assign owners to data product output ports.</li>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Design synchronous output ports.</li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — Trace data product origins.</li>
      <li><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration and Interoperability</a> — Cross-domain data flow patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/data-mesh-for-sap-landscapes/">Data Mesh for SAP Landscapes</a> — SAP-specific application.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — Contract design for data products.</li>
      <li><a href="/atlas/concepts/cdc-change-data-capture/">CDC (Change Data Capture)</a> — Event-based data product emission.</li>
      <li><a href="/atlas/concepts/integration-ownership-model/">Integration Ownership Model</a> — Ownership patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of data mesh practice. It is not official DAMA, Zhamak Dehghani, or SAP documentation. It simplifies federated governance for operational applicability. SAP-specific guidance respects common licensing and data model constraints but does not replace legal or contractual review. Use this skill as a structured starting point, not as an authoritative framework substitute.</p>
  </section>
</article>
