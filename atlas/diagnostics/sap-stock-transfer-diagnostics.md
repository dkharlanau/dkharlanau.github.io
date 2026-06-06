---
layout: default
title: "SAP Stock Transfer Diagnostics"
description: "A conservative diagnostic frame for stock transfer and in-transit issues in SAP."
permalink: /atlas/diagnostics/sap-stock-transfer-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory management
concept_type: diagnostic guide
sap_area: "MM inventory management"
business_process: Inventory / Logistics
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - inventory-management
related:
  - /atlas/diagnostics/sap-movement-types-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Stock Transfer Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP stock transfer diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why stock is stuck in transit, missing at destination, or posted with wrong valuation.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory / Logistics</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until stock transfer behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Stock transfers move goods between plants, storage locations, or stock types. The most common support issue is not the transfer itself but the mismatch between what left the source and what arrived at the destination. In-transit stock is invisible to MRP at the destination until receipt is posted, which creates planning gaps. The support goal is to trace the transfer document, confirm the goods issue, track in-transit status, and verify the receipt.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Stock shows as in transit but never arrived at destination.</li>
      <li>Destination plant shows shortage while source plant shows the goods issue was posted.</li>
      <li>Transfer order quantity does not match goods issue or receipt quantity.</li>
      <li>Valuation difference between source and destination after transfer.</li>
      <li>MRP at destination does not consider in-transit stock as supply.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Goods issue posted but receipt not posted:</strong> the physical shipment arrived but the receiving plant did not confirm it in the system.</li>
      <li><strong>Partial shipment:</strong> only part of the transfer quantity was shipped, but the full quantity was expected.</li>
      <li><strong>Wrong movement type:</strong> a one-step transfer was used when a two-step transfer was expected, or vice versa.</li>
      <li><strong>Valuation area mismatch:</strong> source and destination plants use different valuation classes or currencies.</li>
      <li><strong>Delivery or shipment document stuck:</strong> the transfer uses SD delivery and the delivery is blocked or incomplete.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME23N — if the transfer is PO-based, check the PO history for goods issue and receipt.</li>
      <li>MIGO — display the material documents for both issue and receipt.</li>
      <li>MB5T — in-transit stock report per material and plant.</li>
      <li>MB52 — stock overview at both source and destination.</li>
      <li>VL03N — if SD delivery is used, check delivery status and shipment.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKPO / EKBE</strong> — purchase order items and history (for stock transport orders).</li>
      <li><strong>MKPF / MSEG</strong> — material documents.</li>
      <li><strong>MSLB / MSKA</strong> — special stock tables (if consignment or pipeline).</li>
      <li><strong>LIPS</strong> — delivery items (if SD delivery involved).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the transfer type: one-step (301/311) or two-step (303/305, or stock transport order).</li>
      <li>Check if a goods issue was posted at the source and capture the material document.</li>
      <li>Check MB5T or MB52 for in-transit quantity.</li>
      <li>Check if a goods receipt was posted at the destination.</li>
      <li>If receipt is missing, verify physical arrival and post the receipt or investigate why it was not posted.</li>
      <li>If quantities differ, trace partial shipments, returns, or damage.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Post the missing goods receipt at the destination if the goods physically arrived.</li>
      <li>Reverse and re-post the transfer with the correct movement type if the original was wrong.</li>
      <li>Update MRP views to consider in-transit stock if the planning gap is systematic.</li>
      <li>Escalate to logistics if the physical shipment never arrived or was damaged.</li>
    </ul>

    <h2>Retail-specific: DC-to-store delivery failures</h2>
    <p>In retail, stock transfers from a DC to a store often use stock transport orders (STOs) with SD deliveries. When a store does not receive expected stock, the issue may be in the STO, the delivery, the shipment, or the carrier.</p>
    <ul>
      <li><strong>Check STO status:</strong> ME23N shows whether the STO is released, partially delivered, or fully delivered.</li>
      <li><strong>Check delivery block:</strong> VL03N or VL06O shows if the outbound delivery is blocked for picking, packing, or goods issue.</li>
      <li><strong>Check picking status:</strong> the delivery may be created but not yet picked due to DC capacity or wave scheduling.</li>
      <li><strong>Check shipment status:</strong> VT03N or carrier tracking shows if the shipment is in transit, delayed, or delivered.</li>
      <li><strong>Check store receiving:</strong> the delivery may have arrived physically but the store has not posted the goods receipt.</li>
    </ul>
    <p>A useful DC-to-store delivery ticket should include: STO number, delivery number, shipment number, expected delivery date, current status, and whether the issue is isolated to one store or affects multiple stores on the same route.</p>

    <h2>Support takeaway</h2>
    <p>Stock transfer issues are usually process gaps between shipping and receiving, not system errors. A useful stock transfer ticket should include: source plant, destination plant, material, transfer document or PO number, goods issue document, expected receipt date, and current in-transit quantity.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a stock transfer configuration guide. It does not cover EWM-managed transfers, cross-company code transfers with intercompany billing, or pipeline materials. It does not replace SAP's logistics documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
