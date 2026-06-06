---
layout: default
title: "SAP Analytics Cloud"
description: "Analytical overview of SAP Analytics Cloud: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-analytics-cloud/
atlas_section: sap
domain: SAP operations
subdomain: Business intelligence
concept_type: product
sap_area: "Analytics Cloud"
business_process: "Reporting and analytics"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-analytics-cloud
  - bi
  - analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/analytics-technology-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Analytics Cloud</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Analytics Cloud</h1>
    <p class="note-subtitle">Cloud BI, planning, and predictive analytics for SAP data.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Reporting and analytics</dd></div>
      <div><dt>SAP area</dt><dd>Analytics Cloud</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP Analytics Cloud (SAC) is a cloud-based business intelligence, planning, and predictive analytics platform. It connects to S/4HANA, Datasphere, and other sources to provide dashboards, stories, planning models, and predictive scenarios.</p>

    <h2>Business purpose</h2>
    <p>Provide self-service analytics and enterprise dashboards. Run financial and operational planning. Apply predictive analytics to forecast demand, detect anomalies, and optimize decisions.</p>

    <h2>Where it sits in the landscape</h2>
    <p>SAC sits at the analytics consumption layer. It reads from S/4HANA (live connection), Datasphere (semantic layer), and other sources. It can also write back planning data to S/4HANA or Datasphere.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Story: interactive dashboard with charts, tables, filters.</li>
      <li>Model: data model with dimensions, measures, hierarchies.</li>
      <li>Planning model: versioned model for budgeting and forecasting.</li>
      <li>Predictive scenario: forecast, classification, regression.</li>
      <li>Connection: live or import to S/4HANA, Datasphere, other.</li>
      <li>Calendar: scheduled data refresh and distribution.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: live connection for operational reporting.</li>
      <li>Datasphere: semantic layer and data integration.</li>
      <li>IBP: planning data visualization and comparison.</li>
      <li>Non-SAP: JDBC, OData, file, cloud sources.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom stories and analytics applications.</li>
      <li>Custom planning logic and data actions.</li>
      <li>Predictive model extensions with Python/R.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Connection health: live vs. import status.</li>
      <li>Data refresh: success, failure, latency.</li>
      <li>Story performance: query time, rendering time.</li>
      <li>User adoption: views, interactions, sharing.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Unified platform for BI, planning, and predictive.</li>
      <li>Live connection to S/4HANA without data replication.</li>
      <li>Cloud-native, no infrastructure management.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Live connection performance depends on S/4HANA load.</li>
      <li>Complex planning models are hard to debug.</li>
      <li>Licensing: user tiers and capacity units.</li>
      <li>Data security: cloud data access and row-level security.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Live connection timeout — S/4HANA load or network.</li>
      <li>Data refresh failed — source connection or transformation.</li>
      <li>Story shows wrong data — model, filter, or version issue.</li>
      <li>Planning data action failed — validation or lock.</li>
      <li>User cannot access story — role, team, or data access.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology Domain</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Analytics Cloud features, licensing, and integration mechanisms vary by release and must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology Domain</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
