---
layout: default
title: "Sales — SAP S/4HANA Domain"
description: "Analytical overview of the Sales domain in SAP S/4HANA: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sales-domain/
atlas_section: sap
domain: SAP operations
subdomain: Sales
concept_type: domain
sap_area: "SD"
business_process: "Order to cash"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-sd
  - sales
  - order-to-cash
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-invoice-split-analysis/
  - /atlas/sap/sap-s4hana/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Sales Domain</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Domain</p>
    <h1>Sales — SAP S/4HANA domain</h1>
    <p class="note-subtitle">Customer demand, pricing, contracts, delivery commitment, billing, and receivables.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>SD</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>The Sales domain in S/4HANA covers the commercial relationship with customers: quotations, orders, contracts, scheduling agreements, deliveries, billing documents, and credit management. It is the demand-side anchor of the order-to-cash process.</p>

    <h2>Business purpose</h2>
    <p>Capture customer demand, validate it against availability and credit, commit to delivery, bill accurately, and post receivables. The domain sits between customer-facing channels and internal fulfillment.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Upstream: CRM, e-commerce, EDI orders. Downstream: inventory/warehousing (MM/WM/LE), production (PP), transportation (TM), billing and finance (FI-AR). Cross-domain: credit management (FI), pricing (condition technique), output control.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Customer master / business partner (sold-to, ship-to, bill-to, payer).</li>
      <li>Material master (sales views, units, tax classification).</li>
      <li>Sales documents: inquiry, quotation, order, contract, scheduling agreement.</li>
      <li>Delivery and shipment documents.</li>
      <li>Billing documents: invoice, debit memo, credit memo.</li>
      <li>Pricing: condition types, procedure, access sequence, condition records.</li>
      <li>Credit management: credit limit, risk category, check rules.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>MM/WM/LE: stock availability, reservation, goods issue.</li>
      <li>PP: make-to-order, assemble-to-order, configurable products.</li>
      <li>TM: freight cost, shipment planning.</li>
      <li>FI-AR: billing, account determination, payment terms.</li>
      <li>External: EDI, OData APIs, IDoc ORDERS/DESADV/INVOIC.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>User exits and BAdIs in sales document processing (MV45AFZZ, etc.).</li>
      <li>Custom pricing routines and condition base formulas.</li>
      <li>RAP-based extensions for S/4HANA Cloud and Clean Core.</li>
      <li>Side-by-side apps on BTP for order entry and tracking.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Document flow (VBFA) for order-to-delivery-to-billing trace.</li>
      <li>Delivery due list (VL10*) for backlog monitoring.</li>
      <li>Billing due list (VF04) for invoice backlog.</li>
      <li>Credit management worklist (UKM_CASE) for blocked orders.</li>
      <li>Incompletion log for missing master data or configuration.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Deep configurability for pricing, partner determination, and output.</li>
      <li>Tight integration with logistics and finance.</li>
      <li>Robust document flow and audit trail.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Pricing procedure complexity makes debugging slow.</li>
      <li>Credit management blocks are often the first visible symptom of upstream issues.</li>
      <li>Partner determination and incompletion rules are easy to misconfigure.</li>
      <li>Custom enhancements complicate upgrade and Clean Core migration.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Sales order blocked — credit, delivery, billing, or incompletion.</li>
      <li>Wrong price — condition record, pricing procedure, or customer-specific pricing.</li>
      <li>Delivery not created — schedule line, availability, or warehouse block.</li>
      <li>Invoice split — unexpected splitting due to header differences.</li>
      <li>Partner missing — sold-to/ship-to determination failure.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/atlas/diagnostics/sap-invoice-split-analysis/">SAP Invoice Split Analysis</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Object names, transaction codes, and configuration paths may vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
