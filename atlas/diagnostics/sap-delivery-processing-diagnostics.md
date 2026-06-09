---
layout: default
title: "SAP Delivery Processing Diagnostics"
description: "Diagnostic guide for SAP delivery processing failures including picking, packing, warehouse transfer order, and post goods issue blockers."
permalink: /atlas/diagnostics/sap-delivery-processing-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Delivery and logistics execution
concept_type: diagnostic guide
sap_area: "SD / LE / WM delivery"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - delivery
  - sap-sd
  - sap-le
  - sap-wm
  - diagnostics
  - order-to-cash
related:
  - /atlas/diagnostics/sap-delivery-block-analysis/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-movement-types-diagnostics/
  - /atlas/diagnostics/sap-batch-determination-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Delivery Processing Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP delivery processing diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a delivery cannot be picked, packed, or posted with goods issue in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>SD / LE / WM delivery</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until delivery processing behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Delivery processing in SAP moves a sales order into physical execution: picking from warehouse stock, packing into shipping units, and posting goods issue (PGI). A failure at any step stops the outbound process. The diagnostic task is to identify whether the issue is in delivery creation, warehouse integration (WM/EWM), stock availability, batch/serial determination, or shipping point configuration.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Delivery is created but picking quantity is zero or less than the delivery quantity.</li>
      <li>Transfer order (TO) cannot be created in WM; error "No transfer requirements found" or "Storage bin not found."</li>
      <li>Picking is confirmed but packing fails due to handling unit (HU) configuration or weight/volume limits.</li>
      <li>Post goods issue (PGI) fails with account determination error, movement type error, or stock insufficient.</li>
      <li>Delivery is stuck in "Being processed" status and cannot be changed or deleted.</li>
      <li>Batch or serial number is required but not determined or manually entered incorrectly.</li>
      <li>Delivery date or route is incorrect, causing the delivery to be excluded from the due list.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Stock availability:</strong> the required stock is not available in the delivering plant and storage location, or is blocked by other reservations or deliveries.</li>
      <li><strong>WM integration:</strong> the warehouse number is not assigned to the plant/storage location, or the WM movement type is not configured for the delivery type.</li>
      <li><strong>Storage bin or picking area:</strong> the material has no fixed bin, or the picking area is not defined for the warehouse number.</li>
      <li><strong>Batch/serial determination:</strong> the material requires batch or serial number, but determination failed or the batch is restricted.</li>
      <li><strong>Delivery type or item category:</strong> the delivery type or item category does not allow picking, packing, or PGI for the combination of sales document type and material.</li>
      <li><strong>Shipping point determination:</strong> the shipping point is not determined or is determined incorrectly due to missing loading point or calendar assignment.</li>
      <li><strong>Credit or delivery block:</strong> the underlying sales order has a block that propagates to the delivery.</li>
      <li><strong>Handling unit management:</strong> packing requires HUs but the packaging material or HU type is not configured.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>VL02N / VL03N</strong> — delivery change and display; check picking status, packing status, and goods movement status.</li>
      <li><strong>LT03 / LT12</strong> — create and confirm transfer order in WM; check WM movement type and storage bin.</li>
      <li><strong>LS26</strong> — warehouse stock by material; verify stock in the warehouse and storage type.</li>
      <li><strong>CO09</strong> — stock availability overview; check reservations and other deliveries consuming the stock.</li>
      <li><strong>MMBE</strong> — stock overview by plant, storage location, and batch.</li>
      <li><strong>MSC3N</strong> — batch master; check batch status and stock if batch-managed.</li>
      <li><strong>IQ09</strong> — serial number stock display if serial-managed.</li>
      <li><strong>0VTA / 0VTD</strong> — delivery type and item category configuration (consulting view, not for direct change).</li>
      <li><strong>SPRO</strong> — shipping point determination and delivery type assignment.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>LIKP / LIPS</strong> — delivery header and item data (picking quantity, packing status, movement status).</li>
      <li><strong>VBFA</strong> — document flow between sales order and delivery.</li>
      <li><strong>LTAK / LTAP</strong> — transfer order header and items in WM.</li>
      <li><strong>LQUA</strong> — warehouse stock quant data (bin, batch, stock category).</li>
      <li><strong>MCHA / MCHB</strong> — batch stocks at plant and storage location.</li>
      <li><strong>Equi / SER01 / SER02</strong> — serial number master and stock data.</li>
      <li><strong>TVLK / TVLP</strong> — delivery type and item category configuration.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Open the delivery in VL03N and confirm the delivery status: picking, packing, and goods movement.</li>
      <li>Check the sales order in VA03 for any blocks (credit, delivery block) that may affect the delivery.</li>
      <li>Verify stock availability in MMBE or CO09 for the delivering plant, storage location, and batch.</li>
      <li>If WM is active, check LS26 for warehouse stock and LT03 for transfer order creation errors.</li>
      <li>Check batch or serial number determination: is the required batch/serial present and unrestricted?</li>
      <li>Attempt PGI in VL02N and capture the exact error message; map it to account determination, movement type, or stock issue.</li>
      <li>Check the delivery item category in 0VTD to confirm picking relevance and packing relevance.</li>
      <li>Review shipping point determination if the delivery was created with the wrong shipping point or route.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Move stock to the correct storage location or adjust reservations if stock is blocked.</li>
      <li>Create or confirm the WM transfer order in LT03/LT12 to enable picking.</li>
      <li>Correct batch or serial number assignment in the delivery item if determination failed.</li>
      <li>Remove the delivery block in the sales order (VA02) if the block is no longer valid.</li>
      <li>Check and correct account determination or movement type configuration if PGI fails with accounting errors.</li>
      <li>Adjust handling unit or packaging material master if packing fails.</li>
      <li>Escalate to the warehouse team if the issue is physical stock location or picking strategy.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Delivery processing failures are usually stock, warehouse, or master data issues. A useful ticket should include: delivery number, sales order number, item number, exact error message, picking/packing/PGI status, and confirmation of stock availability in the delivering plant and storage location.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a delivery or warehouse configuration guide. It does not cover EWM-specific processes, transportation planning, or shipment cost calculation. It does not replace SAP's logistics execution documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-delivery-block-analysis/">SAP Delivery Block Analysis</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-batch-determination-diagnostics/">SAP Batch Determination Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
