---
layout: default
title: "SAP Retail Replenishment Diagnostics"
description: "A conservative diagnostic frame for retail replenishment and allocation issues in SAP."
permalink: /atlas/diagnostics/sap-retail-replenishment-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Retail operations
concept_type: diagnostic guide
sap_area: "SAP Retail / S/4HANA Retail"
business_process: Retail operations
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - retail
  - sap-sd
  - diagnostics
  - inventory-management
related:
  - /atlas/concepts/store-receiving-sap-retail/
  - /atlas/diagnostics/sap-stock-transfer-diagnostics/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-retail-assortment-listing-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Retail Replenishment Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP retail replenishment diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a store is not receiving expected replenishment stock, or why some stores overstock while others stock out on the same SKU.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Retail operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP Retail / S/4HANA Retail</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until replenishment behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Retail replenishment moves stock from a DC to stores based on consumption, stock targets, and allocation rules. When a store does not receive expected stock, or when some stores chronically overstock while others stock out, the issue is usually in the replenishment parameters, allocation logic, DC capacity, or store-level inventory accuracy. The support goal is to identify whether the problem is in planning, execution, or data quality.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A store has empty shelves but the DC shows available stock.</li>
      <li>Some stores receive too much of a product while others receive none.</li>
      <li>Replenishment orders are not generated for a store despite low stock.</li>
      <li>Store stock is above target but replenishment continues to arrive.</li>
      <li>DC-to-store deliveries are delayed, cancelled, or arrive with wrong quantities.</li>
      <li>Online orders show available stock but cannot be fulfilled from the assigned store.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Min/max or target stock misconfiguration:</strong> the article-site master has wrong minimum, maximum, or target stock levels that do not match actual store capacity or sales velocity.</li>
      <li><strong>Replenishment profile mismatch:</strong> the profile assigned to the article or store uses the wrong replenishment method (reorder point, periodic, continuous, or demand-driven).</li>
      <li><strong>DC capacity constraint:</strong> the DC cannot pick and ship the required volume, causing delivery delays or partial shipments.</li>
      <li><strong>Allocation rule imbalance:</strong> the allocation rule distributes stock based on criteria (sales rate, store size, shelf space) that do not reflect current demand.</li>
      <li><strong>Store inventory inaccuracy:</strong> phantom inventory or unrecorded shrinkage causes the system to think the store has stock when the shelf is empty.</li>
      <li><strong>ATP scope mismatch:</strong> the replenishment planning run does not consider in-transit stock, reserved stock, or channel-specific allocations.</li>
      <li><strong>Listing or assortment block:</strong> the product is not listed at the store, so replenishment is not triggered even if the product is in the DC assortment.</li>
      <li><strong>Delivery block or shipment issue:</strong> the stock transfer order or outbound delivery is blocked, stuck in picking, or delayed by carrier.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WRP1 / WRP1R — replenishment run and results per site and article.</li>
      <li>WRP4 — replenishment list showing what was ordered, what was delivered, and what is in transit.</li>
      <li>ME23N — stock transfer order status if replenishment uses STOs.</li>
      <li>VL03N / VL06O — outbound delivery status from DC to store.</li>
      <li>MB52 / MMBE — stock overview at DC and store, including in-transit.</li>
      <li>WSOA3 — listing condition to confirm the product is valid at the store.</li>
      <li>MD04 / MD05 — MRP list if MRP-based replenishment is used.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>WRP1 / WRP1R</strong> — replenishment run transactions.</li>
      <li><strong>WRP4</strong> — replenishment list.</li>
      <li><strong>WRF1</strong> — site master with replenishment parameters.</li>
      <li><strong>WRF_MAT_SIT</strong> — article-site master (min/max, target stock, replenishment profile).</li>
      <li><strong>EKPO / EKBE</strong> — stock transfer order items and history.</li>
      <li><strong>LIKP / LIPS</strong> — outbound delivery header and items.</li>
      <li><strong>MARD</strong> — storage location stock (store backroom and sales floor).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the article number, store number, and the symptom (stockout, overstock, missing delivery, wrong quantity).</li>
      <li>Check WRP4 or WRP1R to see if a replenishment order was generated for the store and article.</li>
      <li>If no order was generated, check the article-site master (WRF_MAT_SIT) for min/max, target stock, and replenishment profile settings.</li>
      <li>Check MB52/MMBE for current stock at the store, DC, and in-transit.</li>
      <li>If an order exists, check ME23N for STO status and VL03N for delivery status. Identify blocks or delays.</li>
      <li>Check WSOA3 to confirm the article is listed at the store.</li>
      <li>If the issue is imbalance across stores, review the allocation rule and store cluster assignments.</li>
      <li>If online fulfillment is affected, check ATP scope of check and inventory reservation status.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Adjust min/max or target stock levels in the article-site master to match actual store capacity and sales velocity.</li>
      <li>Change the replenishment profile if the current method does not fit the product or store characteristics.</li>
      <li>Release blocked deliveries or stock transfer orders if the issue is in execution.</li>
      <li>Correct store inventory through cycle count or stock adjustment if phantom inventory is causing under-replenishment.</li>
      <li>Escalate to the planning or merchandising team if the allocation rule or store cluster needs redesign.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Replenishment issues are usually planning parameter or execution gaps, not system errors. A useful ticket should include: article number, store number, current stock, expected stock, last replenishment date, delivery document number if one exists, and whether the issue is isolated to one store or widespread.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a replenishment or allocation configuration guide. It does not cover demand forecasting, promotional planning, or IBP integration. It does not replace SAP Retail documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/store-receiving-sap-retail/">Store Receiving in SAP Retail</a></li>
      <li><a href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">SAP Stock Transfer Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-retail-assortment-listing-diagnostics/">SAP Retail Assortment and Listing Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
