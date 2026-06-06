---
layout: default
title: "SAP Stock Transfer and In-Transit Inventory"
description: "How stock transport orders, transfer postings, and in-transit inventory work in SAP, with common visibility and reconciliation issues."
permalink: /atlas/sap/sap-stock-transfer-in-transit/
atlas_section: sap
domain: SAP operations
subdomain: Logistics and inventory
concept_type: SAP concept
sap_area: MM / WM / logistics execution
business_process: Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - inventory
  - logistics
  - stock-transfer
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/maps/procure-to-pay-map/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Stock Transfer and In-Transit Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP stock transfer and in-transit inventory</h1>
    <p class="note-subtitle">One-step vs two-step transfers, stock transport orders, and why in-transit stock sometimes disappears from reports.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / WM / logistics execution</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Stock transfer is the movement of material from one organizational unit to another: plant to plant, storage location to storage location, or warehouse to warehouse. SAP supports two main approaches: transfer posting (direct movement) and stock transport order (a purchase order-like document that tracks the transfer). The critical difference is visibility: a transfer posting can be one-step or two-step, and a two-step transfer creates in-transit stock that is easy to miss in standard stock reports.</p>

    <h2>Key sections</h2>

    <h3>Transfer posting vs stock transport order</h3>
    <ul>
      <li><strong>Transfer posting</strong> — initiated directly in <strong>MIGO</strong> or <strong>MB1B</strong> without a preceding document. Used for ad-hoc movements. One-step (301) or two-step (303/305, 313/315).</li>
      <li><strong>Stock transport order</strong> — a purchase order of type UB (intra-company) or NB with item category U (inter-company). Created in <strong>ME21N</strong>, tracked like a PO, and processed through <strong>MIGO</strong> with reference. Provides document trail, delivery scheduling, and billing for inter-company transfers.</li>
    </ul>

    <h3>One-step vs two-step transfer</h3>
    <ul>
      <li><strong>One-step</strong> — stock leaves the source and arrives at the destination in a single material document. Simple, but no visibility of goods in transit. Best for immediate movements within the same plant.</li>
      <li><strong>Two-step</strong> — step 1 (303/313) removes stock from the source and puts it in transit. Step 2 (305/315) receives it at the destination. The in-transit stock is visible in <strong>MMBE</strong> under the in-transit category, but not in standard storage location stock reports.</li>
    </ul>

    <h3>In-transit stock handling</h3>
    <p>In-transit stock is a special stock category. It is not available for consumption or sales at either the sending or receiving plant until the second step is posted. Common issues include:</p>
    <ul>
      <li>The receiving plant forgets to post the second step, leaving stock in transit indefinitely.</li>
      <li>The user runs a stock report at storage location level and does not see the in-transit quantity, leading to false conclusions about total stock.</li>
      <li>Valuation differences in cross-plant transfers when the plants use different valuation classes or currency.</li>
    </ul>

    <h3>Cross-plant transfers</h3>
    <p>When transferring between plants, the system checks plant-to-plant relationships, availability control, and valuation. For stock transport orders, the supplying plant delivers the material and the receiving plant posts the GR. In inter-company scenarios, billing and invoicing may be involved. Check the stock transport order in <strong>ME23N</strong> and the delivery in <strong>VL03N</strong> if SD delivery is used.</p>

    <h3>Key transactions and tables</h3>
    <ul>
      <li><strong>MB1B</strong> — transfer posting with movement type.</li>
      <li><strong>MIGO</strong> — goods movement with reference to stock transport order or direct transfer.</li>
      <li><strong>ME2N</strong> — display stock transport orders by number.</li>
      <li><strong>MMBE</strong> — stock overview including in-transit.</li>
      <li><strong>MB51</strong> — material document history.</li>
      <li><strong>EKPO</strong> — purchase order items (includes stock transport orders).</li>
      <li><strong>MKPF / MSEG</strong> — material document headers and items.</li>
    </ul>

    <h3>Diagnostic questions for in-transit issues</h3>
    <ul>
      <li>Was the transfer one-step or two-step? If two-step, was the second step posted?</li>
      <li>Does <strong>MMBE</strong> show in-transit stock that is not reflected in the receiving plant's storage location?</li>
      <li>Is the stock transport order fully delivered and fully received?</li>
      <li>Are there partial quantities in transit from multiple transfer documents?</li>
      <li>Does the movement type match the transfer scenario (plant-to-plant, sloc-to-sloc, with or without SD delivery)?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>In-transit stock is the most common blind spot in inventory reconciliation. When a user claims stock is missing after a transfer, check <strong>MMBE</strong> first for the in-transit category, then <strong>MB51</strong> for the movement type and document flow. A complete two-step transfer should show both a 303 and a 305 (or 313 and 315) in the material document history.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers MM-based stock transfers. It does not cover WM transfer requirements, EWM stock transfers, or handling unit movements. It does not detail inter-company billing and invoicing configuration.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
