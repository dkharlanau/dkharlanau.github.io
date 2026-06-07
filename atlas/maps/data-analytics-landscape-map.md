---
layout: default
title: "Data and Analytics Landscape Map"
description: "A landscape map of data and analytics technologies in the SAP ecosystem for operational navigation."
permalink: /atlas/maps/data-analytics-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: Data and analytics landscape
concept_type: map
sap_area: "Data and analytics"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - data-analytics
  - landscape-map
  - sap-datasphere
related:
  - /atlas/maps/ai-agentic-landscape-map/
  - /atlas/maps/developer-tooling-landscape-map/
  - /atlas/maps/operations-observability-landscape-map/
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">Data and Analytics Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>Data and analytics landscape map</h1>
    <p class="note-subtitle">A navigation frame for data and analytics technologies in the SAP landscape.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until data product positioning and integration claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>A data-layer view of the SAP landscape. It traces how operational data flows from S/4HANA through modeling, warehousing, and consumption layers without replacing SAP product documentation.</p>

    <h2>Business purpose</h2>
    <p>Help data architects and AMS teams orient quickly: where master data originates, how it is modeled for analytics, and which tools consume it for reporting and decision-making.</p>

    <h2>Where it sits in the landscape</h2>
    <p><a href="/atlas/sap/sap-s4hana/">S/4HANA</a> is the operational source. <a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a> is the data warehouse layer. <a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a> is the primary consumer. CDS views bridge the gap between transactional and analytical representations.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Transactional data: sales orders, purchase orders, production orders, financial postings.</li>
      <li>Master data: material, customer, vendor, business partner, cost center, profit center.</li>
      <li>Analytical artifacts: <a href="/atlas/sap/cds-views/">CDS views</a>, <a href="/atlas/sap/cds-analytical-views/">CDS analytical views</a>, InfoObjects, analytic models.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA → Datasphere via CDS views and data integration pipelines.</li>
      <li>Datasphere → Analytics Cloud for planning, reporting, and dashboards.</li>
      <li>Third-party BI tools via OData or direct Datasphere access.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom CDS views for domain-specific analytical models.</li>
      <li>Custom <a href="/atlas/sap/semantic-layer/">semantic layer</a> extensions in Datasphere.</li>
      <li>Embedded analytics via <a href="/atlas/sap/embedded-analytics/">embedded analytics</a> in S/4HANA Fiori apps.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>CDS view performance: ST05, SAT, and runtime traces.</li>
      <li>Datasphere data load monitoring and replication status.</li>
      <li>Analytics Cloud data import and refresh logs.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Unified semantic layer via CDS across transactions and analytics.</li>
      <li>Real-time operational reporting through embedded analytics.</li>
      <li>Cloud-native warehousing with Datasphere reducing on-premise data mart sprawl.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>CDS view complexity can degrade transactional performance if poorly modeled.</li>
      <li>Data replication latency between S/4HANA and Datasphere.</li>
      <li>Analytics Cloud licensing and connectivity constraints.</li>
      <li><a href="/atlas/sap/data-quality-lineage/">Data quality and lineage</a> gaps across hybrid landscapes.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Dashboard shows stale data due to failed Datasphere replication.</li>
      <li>CDS view timeout after S/4HANA upgrade due to schema changes.</li>
      <li>KPIs mismatch between embedded analytics and Analytics Cloud.</li>
      <li>Authorization gaps preventing analytical data access post-migration.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/cds-analytical-views/">CDS Analytical Views</a></li>
      <li><a href="/atlas/sap/embedded-analytics/">Embedded Analytics</a></li>
      <li><a href="/atlas/sap/semantic-layer/">Semantic Layer</a></li>
      <li><a href="/atlas/sap/data-quality-lineage/">Data Quality and Lineage</a></li>
      <li>KPIs and Operational Analytics</li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This map is a skeleton based on public SAP documentation. Product boundaries, integration paths, and feature availability must be verified against the customer's S/4HANA release and Datasphere tenant configuration.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/ai-agentic-landscape-map/">AI and Agentic Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/developer-tooling-landscape-map/">Developer Tooling Landscape Map</a></li>
      <li><a href="/atlas/maps/operations-observability-landscape-map/">Operations and Observability Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
