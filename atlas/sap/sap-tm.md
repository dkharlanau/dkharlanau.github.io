---
layout: default
title: "SAP TM"
description: "Analytical overview of SAP TM: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-tm/
atlas_section: sap
domain: SAP operations
subdomain: Transportation management
concept_type: product
sap_area: "TM"
business_process: "Transportation planning and execution"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-tm
  - transportation
  - logistics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/supply-chain-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-ewm/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP TM</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP TM</h1>
    <p class="note-subtitle">Transportation Management for freight planning, execution, and costing.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Transportation planning and execution</dd></div>
      <div><dt>SAP area</dt><dd>TM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP TM (Transportation Management) is a logistics execution system for planning, optimizing, and executing freight movements. It covers order management, planning, carrier selection, freight costing, and settlement.</p>

    <h2>Business purpose</h2>
    <p>Plan and execute transportation efficiently. Consolidate freight, select carriers, calculate costs, track shipments, and settle freight invoices. Reduce transportation spend and improve delivery reliability.</p>

    <h2>Where it sits in the landscape</h2>
    <p>TM sits between order management (SD, LE) and physical execution (EWM, carriers). It receives delivery requirements, plans routes and loads, creates freight orders, and hands off to EWM or carriers for execution.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Freight order: planned or actual shipment with carrier and route.</li>
      <li>Freight unit: demand for transportation (delivery, stock transfer).</li>
      <li>Transportation requirement: order-based or delivery-based demand.</li>
      <li>Carrier: profile, contract, rate, availability.</li>
      <li>Route: stages, distances, durations, constraints.</li>
      <li>Freight settlement: cost distribution, invoice matching.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: delivery, shipment, stock transport order.</li>
      <li>EWM: warehouse task, goods issue, yard management.</li>
      <li>Carrier: EDI, portal, track and trace.</li>
      <li>Event management: status updates, delays, proof of delivery.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom planning algorithms and optimization rules.</li>
      <li>Carrier integration adapters.</li>
      <li>Side-by-side track and trace apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Planning completion: freight units planned vs. unplanned.</li>
      <li>Carrier performance: on-time delivery, cost per km.</li>
      <li>Freight settlement backlog: invoices pending, disputed.</li>
      <li>Event tracking: missing status updates, delays.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Integrated planning with S/4HANA deliveries and EWM.</li>
      <li>Multi-modal and cross-border transportation support.</li>
      <li>Freight cost visibility and settlement automation.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Planning complexity increases with constraints and multi-modal.</li>
      <li>Carrier integration is often custom.</li>
      <li>Performance: large planning problems with many freight units.</li>
      <li>Master data quality: locations, distances, carrier rates.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Freight unit not planned — capacity, route, or carrier constraint.</li>
      <li>Carrier assignment failed — contract expired or rate missing.</li>
      <li>Freight settlement mismatch — cost distribution or invoice error.</li>
      <li>Event not received — carrier EDI or portal issue.</li>
      <li>Delivery delay — planning or execution bottleneck.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. TM deployment options, features, and integration mechanisms vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
