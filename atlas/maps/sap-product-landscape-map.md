---
layout: default
title: "SAP Product Landscape Map"
description: "A landscape map of SAP products and cloud services around S/4HANA for operational navigation."
permalink: /atlas/maps/sap-product-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: Product landscape
concept_type: map
sap_area: "SAP product portfolio"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-products
  - landscape-map
  - cloud-services
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">SAP Product Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>SAP product landscape map</h1>
    <p class="note-subtitle">A navigation frame for SAP products and cloud services around the ERP core.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product positioning and integration claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>A product-level view of the SAP ecosystem. It groups products by their operational role relative to S/4HANA, not by SAP's commercial packaging.</p>

    <h2>Business purpose</h2>
    <p>Help teams understand which product handles which process, where handoffs occur, and what integration complexity to expect.</p>

    <h2>Core ERP</h2>
    <ul>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a> — financials, logistics, manufacturing, sales, procurement.</li>
    </ul>

    <h2>Business Technology Platform</h2>
    <ul>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a> — extension platform, integration, analytics, AI services.</li>
    </ul>

    <h2>Master Data Governance</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a> — centralized master data governance and distribution.</li>
    </ul>

    <h2>Procurement and Business Network</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a> — strategic sourcing, procurement, supplier collaboration.</li>
    </ul>

    <h2>Supply Chain Execution</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a> — extended warehouse management.</li>
      <li><a href="/atlas/sap/sap-tm/">SAP TM</a> — transportation management and freight.</li>
    </ul>

    <h2>Planning</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a> — integrated business planning (demand, supply, S&amp;OP).</li>
    </ul>

    <h2>Analytics and Data</h2>
    <ul>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a> — data warehousing and semantic layer.</li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a> — BI, planning, and predictive analytics.</li>
    </ul>

    <h2>Integration</h2>
    <ul>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a> — middleware, APIs, events, and prebuilt integrations.</li>
    </ul>

    <h2>Where they sit</h2>
    <p>S/4HANA is the transactional core. Satellite products extend specific functions: EWM for warehousing, TM for freight, Ariba for external procurement, IBP for planning, Datasphere/Analytics Cloud for reporting. BTP is the platform layer that connects them.</p>

    <h2>Integration patterns</h2>
    <ul>
      <li>S/4HANA ↔ EWM: direct integration or via SAP Integration Suite.</li>
      <li>S/4HANA ↔ Ariba: cloud integration for purchase orders and invoices.</li>
      <li>S/4HANA ↔ IBP: real-time or batch planning data exchange.</li>
      <li>S/4HANA ↔ Datasphere: CDS views and replication for analytics.</li>
      <li>All satellites → BTP: for extensions, events, and custom apps.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Best-of-breed depth in each functional area.</li>
      <li>Prebuilt integrations reduce custom middleware.</li>
      <li>Unified data model via CDS and Datasphere.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Multiple cloud contracts and SLAs to manage.</li>
      <li>Integration latency and failure points multiply.</li>
      <li>Data consistency across satellite systems.</li>
      <li>User experience fragmentation across product UIs.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Cloud connector or integration tenant downtime.</li>
      <li>Data sync lag between S/4HANA and satellite (e.g., IBP planning versions).</li>
      <li>Authentication issues across BTP subaccounts.</li>
      <li>License or entitlement mismatches blocking access.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Product names and integration patterns are based on public SAP documentation. Specific integration mechanisms, release compatibility, and licensing terms must be verified against SAP's current product documentation and the customer's entitlement.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
