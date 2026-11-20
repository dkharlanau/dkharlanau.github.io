---
layout: default
title: "Data Architecture Field Guide — Warehouse, Lakehouse, Fabric, or Mesh?"
description: "A compact, decision-led guide to modern data architecture, from warehouse and lakehouse choices to governance, modeling, ingestion, and SAP examples."
permalink: /atlas/concepts/data-architecture-field-guide/
atlas_section: concepts
domain: Enterprise data
subdomain: Data architecture
concept_type: decision guide
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
author: Dzmitryi Kharlanau
last_modified_at: 2026-11-20
tags:
  - data-architecture
  - data-warehouse
  - data-lakehouse
  - data-fabric
  - data-mesh
  - data-governance
  - sap
related:
  - /skill-hub/architecture/data-architecture-selection-working-skill/
  - /skill-hub/dama-dmbok/
  - /atlas/data-quality/sap-master-data-quality/
  - /skill-hub/architecture/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/concepts/">Concepts</a></li><li aria-current="page">Data Architecture Field Guide</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Knowledge Atlas / Decision guide</p>
    <h1>Data architecture: choose the problem before the platform.</h1>
    <p class="note-subtitle">Warehouse, lake, lakehouse, fabric and mesh are not five products competing for the same job. They solve different problems — and can coexist.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The 60-second mental model</h2>
    <p><strong>A data architecture is a set of decisions</strong> about where data lives, how it moves, which meaning it carries, who can use it, and who is accountable when it is wrong. First define the consumer and the business decision. Then measure freshness, quality, history, access, scale, and cost. Only then select technologies.</p>
    <p>James Serra's <a href="https://www.oreilly.com/library/view/deciphering-data-architectures/9781098150754/">Deciphering Data Architectures</a> is the starting point for this independent guide. Its most transferable lesson is that architecture selection is a trade-off, not a popularity contest.</p>

    <h2 id="choose">Choose the architecture by the job</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Comparison of data architecture patterns">
      <table class="study-table__table">
        <thead><tr><th scope="col">Pattern</th><th scope="col">Start here when…</th><th scope="col">Watch out for…</th></tr></thead>
        <tbody>
          <tr><th scope="row">Relational warehouse (RDW)</th><td>Business users need stable, governed SQL reporting and historical comparisons.</td><td>Rigid ingestion and modeling can slow exploration; complex ETL has a cost.</td></tr>
          <tr><th scope="row">Data lake</th><td>You need inexpensive landing and exploration of raw files, logs, events or documents.</td><td>Without catalog, ownership and quality zones, it becomes a data swamp.</td></tr>
          <tr><th scope="row">Modern data warehouse (MDW)</th><td>Raw/varied data and structured BI must work together with different processing needs.</td><td>Copies, transformations and warehouse/lake boundaries need explicit ownership.</td></tr>
          <tr><th scope="row">Data lakehouse</th><td>Open table formats, object storage and multiple analytics/engineering workloads fit the team.</td><td>Catalog interoperability, table maintenance, BI performance and governance still need proof.</td></tr>
          <tr><th scope="row">Data fabric</th><td>Many systems need shared discovery, metadata, access policy, lineage and integration.</td><td>A catalog or virtualization tool alone does not fix source quality or ownership.</td></tr>
          <tr><th scope="row">Data mesh</th><td>Independent business domains can own and operate trustworthy data products.</td><td>It changes responsibilities, funding and standards. Tooling alone does not make a mesh.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Useful distinction:</strong> warehouse/lakehouse primarily describe storage and analytical serving choices; fabric emphasizes connective governance and access capabilities; mesh emphasizes organizational ownership and data-as-a-product. This is a practical lens, not a universal formal taxonomy.</p>

    <h2>Six decisions that matter more than the label</h2>
    <ol>
      <li><strong>Operational or analytical?</strong> OLTP supports business transactions; OLAP supports analysis. Do not load operational ERP tables with uncontrolled analytical workloads.</li>
      <li><strong>Copy or query in place?</strong> Replication improves isolation and repeatable history; federation may reduce copies but depends on source availability, authorizations and query latency.</li>
      <li><strong>Batch or streaming?</strong> Choose the least frequent refresh that meets the decision's actual latency requirement. “Real time” without a business deadline is an unpriced requirement.</li>
      <li><strong>ETL, ELT or CDC?</strong> Define transformations, change detection, deletes, replay, idempotency and reconciliation. The acronym does not provide correctness.</li>
      <li><strong>How will data be modeled?</strong> Use normalized models for integrity, facts and dimensions for readable analytics, and Data Vault only when auditability and change patterns justify its extra complexity.</li>
      <li><strong>Who owns the truth?</strong> Identify operational system of record, master-data governance, data-product owner, semantic definition, access policy and defect escalation path.</li>
    </ol>

    <h2 id="data-models">Modeling: choose the question, not the diagram</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Comparison of data modeling concepts">
      <table class="study-table__table">
        <thead><tr><th>Concept</th><th>Useful test</th></tr></thead>
        <tbody>
          <tr><th>3NF</th><td>Can we update a customer's core attributes without fixing duplicate copies?</td></tr>
          <tr><th>Star schema</th><td>Can a business user ask for sales by customer, product and month with consistent measures?</td></tr>
          <tr><th>Conformed dimensions</th><td>Does “customer” mean the same thing across billing and delivery analytics?</td></tr>
          <tr><th>SCD Type 1</th><td>Correct/overwrite a value when history is not required.</td></tr>
          <tr><th>SCD Type 2</th><td>Create dated dimension versions when historical reporting must preserve the prior state.</td></tr>
          <tr><th>SCD Type 3</th><td>Store a limited previous/alternate value alongside the current value — not a complete new row per change.</td></tr>
          <tr><th>Data Vault</th><td>Are evolving source systems, traceability and detailed history worth additional links, satellites and serving views?</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Terminology check:</strong> the uploaded edition's explanation of SCD Type 3 differs from Ralph Kimball's definition. Use <a href="https://www.kimballgroup.com/2008/08/slowly-changing-dimensions/">Kimball's primary explanation</a> when implementing slowly changing dimensions. Likewise, streaming architectures can use stateful processing; “Kappa = stateless” is not a design rule (see <a href="https://docs.confluent.io/platform/current/streams/architecture.html">Kafka Streams state stores</a>).</p>

    <h2 id="example">Worked example: customer analytics across SAP and other systems</h2>
    <p><em>Illustrative design exercise, not a description of a client project.</em> An enterprise needs reliable customer revenue by region, operational customer status, and AI-assisted analysis of support documents. Sources include SAP S/4HANA, a governed Business Partner master, a CRM, and PDF documents.</p>
    <ol>
      <li><strong>Define semantics:</strong> business partner, sold-to, payer and legal entity are distinct roles. Agree on keys, effective dates, ownership and sensitive fields before making a “Customer 360” table.</li>
      <li><strong>Separate consumers:</strong> an operational customer-status screen may need API access or an ODS; historical revenue needs a modeled analytical layer; document experiments may use a governed object store.</li>
      <li><strong>Choose ingestion:</strong> use approved interfaces or replication for source data, with incremental change handling, deletion semantics and traceable reconciliation. Do not infer a complete customer state from a partial change event.</li>
      <li><strong>Choose the platform:</strong> compare a managed warehouse plus raw zone against a lakehouse and logical/virtual access. Evaluate SAP Datasphere's semantic and federation capabilities where available; validate licensing, connectivity and deployment scope.</li>
      <li><strong>Prove the result:</strong> sample customer IDs reconcile across systems; role and historical joins work; restricted data remains restricted; refresh meets SLA; failure recovery does not duplicate records.</li>
    </ol>
    <p>For SAP-specific context, see <a href="https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/11f9c5c5273e4a7bacfe01bb188a26e8.html">SAP Datasphere's data-integration and semantic-modeling capabilities</a> and <a href="https://help.sap.com/docs/portfolio-category/data-cloud">SAP Business Data Cloud</a>. Product capability is not proof that a given landscape is configured or licensed for it.</p>

    <h2>Four traps to reject in an architecture review</h2>
    <ul>
      <li><strong>“We need a mesh because it is modern.”</strong> Ask which domain will fund, own, support and publish a data product. Without this, start with clear ownership and contracts, not a reorganization.</li>
      <li><strong>“Put everything in the lake and users will self-serve.”</strong> Show the catalog, semantic model, permissions, data-quality checks and first usable report.</li>
      <li><strong>“Streaming makes data correct.”</strong> Require replay, ordering, deduplication, late-arrival handling and a measurable reconciliation control.</li>
      <li><strong>“One platform is the architecture.”</strong> Show people, process, lineage, security, costs, and evidence of a working consumer.</li>
    </ul>

    <h2>Use it, do not memorize it</h2>
    <p><strong>Practice task:</strong> your business requests five-minute inventory visibility, seven-year financial history, and a searchable collection of product documents. Design one solution, then change the inventory requirement to next-day refresh. Which component disappears or becomes simpler? Write the cost, risk and operational consequence of that change.</p>
    <p>Turn this into a repeatable deliverable with the <a href="/skill-hub/architecture/data-architecture-selection-working-skill/">Data Architecture Selection working skill</a>. It includes a discovery method, option matrix, template, quality gates and AI-agent handoff. Continue with <a href="/skill-hub/architecture/">Architecture Skills</a> and <a href="/skill-hub/dama-dmbok/">Data Governance Skills</a>.</p>

    <h2>Sources and scope</h2>
    <p>This is an original field guide, not a chapter reproduction. Primary inspiration: James Serra, <em>Deciphering Data Architectures</em> (O'Reilly, 2024; Russian edition supplied for review, 2026), particularly chapters 3–15. Complementary references: <a href="https://martinfowler.com/articles/data-mesh-principles.html">Zhamak Dehghani's four Data Mesh principles</a>; <a href="https://www.kimballgroup.com/2008/08/slowly-changing-dimensions/">Kimball on slowly changing dimensions</a>; <a href="https://docs.confluent.io/platform/current/streams/architecture.html">Confluent on stateful streaming</a>; and <a href="https://help.sap.com/docs/SAP_DATASPHERE/86054eedd0dd480f92b0824c281923d5/2bbf33852e3942c8bff52e64fd661680.html">SAP Datasphere feature scope</a>. Platform capabilities change; validate them for the target release.</p>
    <p><small>Editorial state: review candidate. Noindex until human technical and editorial review; synthetic examples only.</small></p>
  </div>
</article>
