---
layout: default
title: "SAP S/4HANA"
description: "Analytical overview of SAP S/4HANA: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-s4hana/
atlas_section: sap
domain: SAP operations
subdomain: Core ERP
concept_type: product
sap_area: "S/4HANA"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-s4hana
  - erp
  - core-system
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-platform/
  - /atlas/sap/abap-cloud/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/sap-data-product/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP S/4HANA</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP S/4HANA</h1>
    <p class="note-subtitle">SAP's core ERP for financials, logistics, manufacturing, and enterprise operations.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Enterprise operations</dd></div>
      <div><dt>SAP area</dt><dd>S/4HANA core</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP S/4HANA is SAP's modern ERP suite, built on the SAP HANA in-memory database. It replaces SAP ECC and consolidates financial and logistics data into a single source of truth with real-time analytics.</p>

    <h2>Business purpose</h2>
    <p>Run the core financial, logistics, manufacturing, sales, procurement, and human resources processes of an enterprise. Provide real-time visibility, simplified data model, and modern extensibility.</p>

    <h2>Where it sits in the landscape</h2>
    <p>S/4HANA is the transactional core. Around it orbit satellite products (Ariba, EWM, TM, IBP, Datasphere, Analytics Cloud, Integration Suite) and the extension platform (BTP). It connects to external systems via APIs, events, and documents.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Universal Journal (ACDOCA) — single table for financial and management accounting.</li>
      <li>Material ledger — actual costing, inventory valuation.</li>
      <li>Business partner — unified master data for customers, vendors, contacts.</li>
      <li>Organizational structure: company code, plant, storage location, sales org, purchasing org.</li>
      <li>Document chain: sales order → delivery → billing → accounting.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>Satellite products: Ariba, EWM, TM, IBP via BTP and Integration Suite.</li>
      <li>Analytics: CDS views, Datasphere, Analytics Cloud.</li>
      <li>Extensions: ABAP Cloud, RAP, CAP on BTP.</li>
      <li>External: OData, IDoc, RFC, business events.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>In-app: ABAP Cloud, RAP, CDS, BAdIs.</li>
      <li>Side-by-side: CAP, Kyma, Node.js, Java on BTP.</li>
      <li>UI: Fiori launchpad, custom apps.</li>
      <li>Data: custom fields, business objects, analytical models.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>System: SM21, SLG1, ST22, ST03.</li>
      <li>Financial: universal journal reconciliation, material ledger closing.</li>
      <li>Integration: IDoc, OData, event monitoring.</li>
      <li>Performance: SQL trace, SAT, workload analysis.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Single source of truth for financial and logistics data.</li>
      <li>Real-time analytics via HANA and CDS views.</li>
      <li>Modern extensibility with Clean Core strategy.</li>
      <li>Cloud and on-premise deployment options.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Upgrade and migration complexity from ECC.</li>
      <li>Custom code remediation burden.</li>
      <li>HANA hardware and licensing costs.</li>
      <li>Business partner convergence complexity.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Universal journal reconciliation mismatch.</li>
      <li>Material ledger closing errors.</li>
      <li>Business partner replication failures.</li>
      <li>Custom dump after release change.</li>
      <li>Performance degradation after data volume growth.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Specific features, deployment options, and licensing terms must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
