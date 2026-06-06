---
layout: default
title: "Embedded Analytics"
description: "Analytical overview of SAP Embedded Analytics: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/embedded-analytics/
atlas_section: sap
domain: SAP operations
subdomain: Data and analytics
concept_type: technology
sap_area: "Embedded Analytics"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - embedded-analytics
  - s4hana
  - real-time-analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/cds-views/
  - /atlas/sap/cds-analytical-views/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-datasphere/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Embedded Analytics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Embedded Analytics</h1>
    <p class="note-subtitle">Real-time analytics embedded in S/4HANA transactional screens and Fiori apps.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Analytics and reporting</dd></div>
      <div><dt>SAP area</dt><dd>Embedded Analytics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>Embedded Analytics delivers real-time analytical content directly inside S/4HANA transactional screens. It uses CDS analytical views, analytical queries, KPI tiles, and Fiori analytical apps to present metrics without data replication or external BI tools.</p>

    <h2>Business purpose</h2>
    <p>Enable operational decision-making without leaving the transaction context. Users see relevant KPIs, trends, and comparisons while processing orders, invoices, or inventory movements.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Embedded Analytics sits inside S/4HANA, between the HANA database and the Fiori launchpad. It consumes CDS analytical views and exposes them as tiles, lists, charts, and multidimensional reports within the same system.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>CDS analytical query: multidimensional view with key figures and dimensions.</li>
      <li>KPI catalog: repository of predefined and custom KPIs.</li>
      <li>KPI tile: Fiori launchpad tile showing a single metric.</li>
      <li>Fiori analytical app: interactive chart and table views.</li>
      <li>Smart Business KPI: drill-down enabled KPI with filters.</li>
      <li>Multidimensional report: OLAP-style grid with drag-and-drop.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: CDS analytical views, transactional screens, Fiori launchpad.</li>
      <li>Analytics Cloud: advanced visualizations via live connection.</li>
      <li>Datasphere: cross-system analytics when single-system view is insufficient.</li>
      <li>Smart Business: KPI modeling, evaluation, and alerting.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom CDS analytical queries extending standard views.</li>
      <li>Custom KPIs and KPI tiles in the Fiori launchpad.</li>
      <li>Custom Fiori analytical apps with UI5.</li>
      <li>BAdIs for data selection and authorization.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Query response time: HANA execution plan, filter pushdown.</li>
      <li>HANA memory consumption: large analytical queries.</li>
      <li>KPI refresh failures: evaluation schedule, data source.</li>
      <li>Tile loading performance: network, metadata, cache.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>No replication latency — queries run on live operational data.</li>
      <li>Contextual analytics inside the transaction workflow.</li>
      <li>Tight integration with Fiori and S/4HANA authorizations.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Performance impact on the operational HANA database.</li>
      <li>Limited to HANA-optimized queries; complex aggregations may timeout.</li>
      <li>Not suitable for cross-system or historical trend analytics.</li>
      <li>Large data volumes require careful filter design.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>KPI tile timeout — missing filter or large data volume.</li>
      <li>Analytical query memory limit exceeded — aggregation too broad.</li>
      <li>Blank tiles after upgrade — CDS view or annotation change.</li>
      <li>Filter mismatch — transaction filter not passed to analytical query.</li>
      <li>Drill-down error — hierarchy or association issue.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/cds-analytical-views/">CDS Analytical Views</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA Embedded Analytics — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9e3f5c4f67424a1f9f9b5c7a5a7a7a7a/embedded-analytics.html">SAP Help Portal</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Embedded Analytics features, KPI availability, and performance characteristics vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/cds-analytical-views/">CDS Analytical Views</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
