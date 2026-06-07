---
layout: default
title: "CDS Analytical Views"
description: "Analytical overview of CDS Analytical Views: what they are, where they sit, and how they break."
permalink: /atlas/sap/cds-analytical-views/
atlas_section: sap
domain: SAP operations
subdomain: Data and analytics
concept_type: technology
sap_area: "CDS Analytical Views"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - cds-views
  - analytical-views
  - olap
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/cds-views/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/embedded-analytics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CDS Analytical Views</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CDS Analytical Views</h1>
    <p class="note-subtitle">CDS views optimized for analytics with OLAP annotations and multidimensional behavior.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Analytics and reporting</dd></div>
      <div><dt>SAP area</dt><dd>CDS Analytical Views</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>CDS Analytical Views are Core Data Services views specifically optimized for analytics. They include analytical queries, cube views, dimension views, and key figures, enriched with OLAP annotations that define aggregation behavior, hierarchies, and multidimensional semantics. They contrast with transactional CDS views, which focus on single-record operations.</p>

    <h2>Business purpose</h2>
    <p>Provide a structured, reusable analytical data layer for OLAP-style reporting, dashboards, and planning. Eliminate ad-hoc SQL and ensure consistent metrics across all analytical consumers.</p>

    <h2>Where it sits in the landscape</h2>
    <p>CDS Analytical Views sit in the S/4HANA ABAP layer, above the HANA database and below consumption tools: Embedded Analytics, Datasphere, Analytics Cloud, and OData services.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Analytical query: top-level view consumed by reporting tools.</li>
      <li>Cube view: fact-like view with key figures and dimensions.</li>
      <li>Dimension view: master data view with attributes and texts.</li>
      <li>Key figure: measurable numeric field with aggregation.</li>
      <li>Hierarchy annotation: drill-down path definition.</li>
      <li>OLAP annotation: aggregation, exception, and presentation metadata.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>Embedded Analytics: Fiori tiles, KPIs, and multidimensional reports.</li>
      <li>Datasphere: replication and remote access for modeling.</li>
      <li>Analytics Cloud: live connection for stories and dashboards.</li>
      <li>OData: auto-generated analytical service.</li>
      <li>Fiori analytical apps: UI5 charts and tables.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom analytical queries extending standard cube views.</li>
      <li>Custom key figures and calculated measures.</li>
      <li>Custom dimensions and hierarchy extensions.</li>
      <li>Side-by-side consumption via OData.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Query execution time: HANA plan, filter pushdown.</li>
      <li>Aggregation behavior: exception aggregation, reference points.</li>
      <li>Hierarchy performance: deep or unbalanced hierarchies.</li>
      <li>Annotation consistency: mapping to SAC and Datasphere.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Native HANA optimization for analytical workloads.</li>
      <li>Declarative OLAP semantics reduce custom SQL.</li>
      <li>Reusable across Embedded Analytics, Datasphere, and SAC.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Complex OLAP annotations are hard to debug and validate.</li>
      <li>HANA-specific optimizations limit portability.</li>
      <li>Deep hierarchies and large dimensions impact performance.</li>
      <li>Released view changes can break analytical extensions.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Analytical query timeout — missing filter or large aggregation.</li>
      <li>Wrong aggregation results — exception aggregation misconfiguration.</li>
      <li>Hierarchy display error — missing or broken hierarchy annotation.</li>
      <li>Annotation mismatch in SAC — CDS annotation not mapped correctly.</li>
      <li>Extension broken — released cube view changed in upgrade.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/embedded-analytics/">Embedded Analytics</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA CDS Analytical Views — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/cds-analytical-views.html">SAP Help Portal</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. CDS Analytical View availability, annotations, and performance characteristics vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/embedded-analytics/">Embedded Analytics</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
