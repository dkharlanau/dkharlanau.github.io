---
layout: default
title: "SAP Datasphere"
description: "Analytical overview of SAP Datasphere: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-datasphere/
atlas_section: sap
domain: SAP operations
subdomain: Data warehousing
concept_type: product
sap_area: "Datasphere"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-datasphere
  - data-warehouse
  - analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/analytics-technology-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/cds-views/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Datasphere</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Datasphere</h1>
    <p class="note-subtitle">Data warehousing and semantic data layer for SAP analytics.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Analytics and reporting</dd></div>
      <div><dt>SAP area</dt><dd>Datasphere</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP Datasphere is a cloud data warehousing solution that provides a semantic data layer, data integration, and modeling capabilities. It replaces SAP BW/4HANA for new cloud-centric analytics architectures and connects to S/4HANA via CDS views and replication.</p>

    <h2>Business purpose</h2>
    <p>Consolidate transactional data from S/4HANA and other sources into a unified semantic layer. Enable self-service analytics, enterprise reporting, and data science without replicating logic into every tool.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Datasphere sits between S/4HANA (source) and Analytics Cloud (consumer). It can also feed external BI tools. It runs on SAP BTP as a managed service.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Space: organizational and security boundary.</li>
      <li>Table / view: raw or modeled data.</li>
      <li>Data flow: ETL/ELT pipeline for data movement.</li>
      <li>Semantic model: business-friendly view of data.</li>
      <li>Remote table: live access without replication.</li>
      <li>Replication flow: scheduled or real-time data sync.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: CDS views, SLT, data flows.</li>
      <li>Analytics Cloud: live connection or import.</li>
      <li>Non-SAP sources: JDBC, OData, file, cloud storage.</li>
      <li>BTP: HANA Cloud, Data Intelligence.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom data flows and transformations.</li>
      <li>Custom semantic models and calculations.</li>
      <li>Side-by-side data quality apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Data flow status: success, failure, runtime.</li>
      <li>Replication lag: source to Datasphere latency.</li>
      <li>Query performance: execution time, data volume.</li>
      <li>Space usage: storage, memory, compute.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Semantic layer unifies data from multiple sources.</li>
      <li>Managed service reduces infrastructure overhead.</li>
      <li>Tight integration with S/4HANA CDS views.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Replication latency for near-real-time use cases.</li>
      <li>Learning curve for BW practitioners migrating to Datasphere.</li>
      <li>Cost: storage, compute, and data transfer.</li>
      <li>Data quality issues propagate from source systems.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Data flow failed — source connection, transformation error.</li>
      <li>Replication lag — SLT issue, network, or volume.</li>
      <li>Query timeout — model complexity or missing filter.</li>
      <li>Space quota exceeded — storage or compute limit.</li>
      <li>Analytics Cloud connection error — certificate or network.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology Domain</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Datasphere features, integration mechanisms, and pricing vary by release and must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology Domain</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
