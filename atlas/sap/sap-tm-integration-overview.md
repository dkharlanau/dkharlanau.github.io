---
layout: default
title: "SAP TM Integration Overview"
description: "How SAP Transportation Management integrates with S/4HANA MM, SD, and LE: freight orders, settlement, and common breakpoints."
permalink: /atlas/sap/sap-tm-integration-overview/
atlas_section: sap
domain: SAP operations
subdomain: Transportation integration
concept_type: SAP concept
sap_area: MM / TM / logistics
business_process: Logistics execution
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - integration
  - tm
  - transportation
  - logistics
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP TM Integration Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP TM integration overview</h1>
    <p class="note-subtitle">The link between S/4HANA deliveries and TM: freight orders, carriers, and charge settlement.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Logistics execution</dd></div>
      <div><dt>SAP area</dt><dd>MM / TM / logistics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP Transportation Management (TM) plans, executes, and settles freight movements. It receives delivery requirements from S/4HANA SD and MM, builds freight orders, selects carriers, calculates charges, and writes settlement documents back. A support ticket that says "freight cost is wrong" usually traces to a missing delivery handoff, a charge master data mismatch, or a settlement document that never posted.</p>

    <h2>What data flows</h2>
    <ul>
      <li><strong>Freight order from delivery</strong> — outbound or inbound delivery requirements transferred from S/4HANA to TM. TM creates freight orders or freight bookings based on planning constraints and carrier contracts.</li>
      <li><strong>Carrier selection</strong> — TM evaluates carriers by cost, capacity, and business share. The selected carrier is communicated back to the delivery or shipment document in S/4HANA.</li>
      <li><strong>Freight settlement</strong> — after execution, TM generates freight settlement documents (FSD) that post to S/4HANA Financials as carrier invoices. Mismatches in charge calculation create reconciliation work.</li>
      <li><strong>Charge calculation</strong> — rates, scales, and agreements maintained in TM determine expected freight cost. If the rate table is outdated or the agreement expired, the calculated cost is wrong before any document is created.</li>
    </ul>

    <h2>Common breakpoints</h2>
    <h3>Delivery not transferred to TM</h3>
    <ul>
      <li>Delivery type or shipping point not assigned to a TM planning profile.</li>
      <li>Transportation planning date is in the past or the delivery is already goods-issued, making it ineligible for planning.</li>
      <li>Background job <code>/SCMTMS/PLN</code> failed or is not scheduled.</li>
    </ul>

    <h3>Freight order creation failure</h3>
    <ul>
      <li>Incompatible planning constraints — no valid carrier, equipment type unavailable, or route violation.</li>
      <li>Master data gaps: missing location, means of transport, or business partner role for the carrier.</li>
    </ul>

    <h3>Charge master data mismatch</h3>
    <ul>
      <li>Rate table scale does not match the delivery attributes (weight, distance, equipment group).</li>
      <li>Agreement validity period expired or the carrier was changed after charge calculation.</li>
    </ul>

    <h3>Settlement document errors</h3>
    <ul>
      <li>Freight settlement document (FSD) created in TM but posting to S/4HANA fails due to G/L account or cost center assignment.</li>
      <li>Carrier invoice does not match the FSD amount — dispute resolution requires tracing back to the freight order and rate table.</li>
    </ul>

    <h2>Key transactions</h2>
    <ul>
      <li><code>/SCMTMS/TOR</code> — freight order management.</li>
      <li><code>/SCMTMS/PLN</code> — transportation planning.</li>
      <li><code>/SCMTMS/SETTL</code> — freight settlement.</li>
      <li><code>VI01</code> — create shipment cost (classic LE; relevant in mixed landscapes).</li>
      <li><code>VI02</code> — change shipment cost.</li>
    </ul>

    <h2>First-pass diagnostic questions</h2>
    <ul>
      <li>Did the delivery reach TM? Check the transportation planning worklist or the delivery's TM status.</li>
      <li>Was a freight order created, and if not, what is the planning error — carrier, capacity, or route?</li>
      <li>Is the charge mismatch in the expected cost (TM calculation) or the settled cost (S/4HANA posting)?</li>
      <li>Did any rate table, agreement, or carrier master data change recently?</li>
      <li>Does the settlement failure have a specific S/4HANA accounting error (G/L, cost center, tax code)?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful TM ticket includes: delivery or freight order number, planning or settlement stage where it failed, exact error message from <code>/SCMTMS/TOR</code> or settlement posting, and whether the issue is carrier-specific or route-specific. "Freight is broken" is not actionable — the diagnostic path differs for planning failures, charge errors, and settlement posting errors.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page describes the S/4HANA–TM integration boundary, not TM configuration, rate table maintenance, or carrier onboarding. It does not cover classic LE shipment cost (VI01/VI02) in detail, though those transactions are noted for mixed landscapes. It does not replace SAP TM implementation or administration documentation.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
