---
layout: default
title: "SAP S/4HANA Landscape Map"
description: "A landscape map of SAP S/4HANA functional domains, products, and integration points for operational navigation."
permalink: /atlas/maps/sap-s4hana-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: S/4HANA landscape
concept_type: map
sap_area: "S/4HANA core"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-s4hana
  - landscape-map
  - enterprise-operations
related:
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">SAP S/4HANA Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>SAP S/4HANA landscape map</h1>
    <p class="note-subtitle">A navigation frame for S/4HANA functional domains and where they connect.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain boundaries and product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>A high-level navigation frame for SAP S/4HANA functional areas. It does not replace SAP documentation; it provides a support-oriented view of where processes, data, and integration points sit.</p>

    <h2>Business purpose</h2>
    <p>Help AMS teams and process analysts orient quickly: which domain owns a transaction, where master data originates, and which integrations cross domain boundaries.</p>

    <h2>Top-level domains (S/4HANA 2025)</h2>
    <ul>
      <li><a href="/atlas/sap/sales-domain/">Sales</a> — customer demand, pricing, contracts, billing.</li>
      <li><a href="/atlas/sap/service-domain/">Service</a> — service orders, contracts, resource planning.</li>
      <li><a href="/atlas/sap/manufacturing-domain/">Manufacturing</a> — production planning, execution, quality.</li>
      <li><a href="/atlas/sap/sourcing-and-procurement-domain/">Sourcing and Procurement</a> — purchasing, contracts, supplier management.</li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain</a> — inventory, warehousing, transportation, planning.</li>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology</a> — reporting, data warehousing, embedded analytics.</li>
      <li><a href="/atlas/sap/enterprise-technology-domain/">Enterprise Technology</a> — platform, development, integration, security.</li>
    </ul>

    <h2>Where it sits in the landscape</h2>
    <p>S/4HANA is the core ERP. Around it sit satellite products (BTP, Ariba, EWM, TM, IBP, Datasphere, Analytics Cloud, Integration Suite) and a technology layer (ABAP, CDS, OData, Fiori, events, IDoc).</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Organizational structure: company code, plant, storage location, sales organization, purchasing organization.</li>
      <li>Master data: material, customer, vendor, business partner, GL account, cost center.</li>
      <li>Transactional data: sales orders, purchase orders, deliveries, invoices, production orders.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>Cloud satellite products via SAP BTP and Integration Suite.</li>
      <li>Third-party systems via OData, IDoc, RFC, and business events.</li>
      <li>Analytics via CDS views and Datasphere.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Side-by-side extensions on BTP (CAP, Kyma).</li>
      <li>In-app extensions via ABAP Cloud and RAP.</li>
      <li>Custom fields and logic via CDS extensions.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Application logs (SLG1, ST22).</li>
      <li>IDoc monitoring (WE02, WE05, BD87).</li>
      <li>Business event monitoring (SAP Integration Suite).</li>
      <li>Performance: ST03, SAT, SQL trace.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Single source of truth for financial and logistics data.</li>
      <li>Tight integration between SD, MM, PP, WM, TM.</li>
      <li>Modern extensibility model (Clean Core, ABAP Cloud).</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Complex upgrade and release management.</li>
      <li>Custom code remediation burden during upgrades.</li>
      <li>Cloud satellite licensing and connectivity costs.</li>
      <li>Business partner convergence complexity in master data.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Cross-domain issues: a sales order block caused by procurement or inventory.</li>
      <li>Integration failures: IDoc stuck, OData timeout, event not delivered.</li>
      <li>Master data replication: business partner missing roles in target system.</li>
      <li>Authorization: new Fiori app missing roles after upgrade.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This map is a skeleton based on public SAP documentation hierarchy. Domain boundaries, product inclusion, and integration claims need verification against system-specific documentation before being treated as authoritative.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
