---
layout: default
title: "SAP EWM Integration Overview"
description: "How SAP Extended Warehouse Management integrates with S/4HANA MM and SD, what data flows, and where warehouse integration breaks."
permalink: /atlas/sap/sap-ewm-integration-overview/
atlas_section: sap
domain: SAP operations
subdomain: Warehouse integration
concept_type: SAP concept
sap_area: MM / EWM / logistics
business_process: Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - integration
  - ewm
  - logistics
  - warehouse
related:
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/concepts/sap-stock-exists-not-promisable/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP EWM Integration Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP EWM integration overview</h1>
    <p class="note-subtitle">The handoff between S/4HANA and EWM: deliveries, tasks, and stock reconciliation.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / EWM / logistics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP Extended Warehouse Management (EWM) handles complex warehouse processes: receiving, putaway, picking, packing, shipping, and physical inventory. It does not replace S/4HANA MM or SD — it receives delivery documents from them, executes warehouse tasks, and reports stock changes back. A support ticket that says "stock is wrong" is usually a question of which system owns the truth at that moment and whether the delivery handshake completed.</p>

    <h2>What data flows</h2>
    <ul>
      <li><strong>Inbound delivery</strong> — created in S/4HANA (VL31N or from PO), transferred to EWM for receiving and putaway. EWM creates warehouse tasks and confirms handling units back to S/4HANA.</li>
      <li><strong>Outbound delivery</strong> — created in S/4HANA (VL01N or from sales order), transferred to EWM for picking, packing, and shipping. EWM confirms picked quantities and updates the delivery status.</li>
      <li><strong>Stock transfers</strong> — plant-to-plant or storage-location moves initiated in S/4HANA and executed in EWM as internal movements or stock transport orders.</li>
      <li><strong>Physical inventory</strong> — count documents created in EWM and reconciled against S/4HANA inventory. Differences post adjustment documents in S/4HANA.</li>
      <li><strong>Wave management</strong> — EWM groups outbound deliveries into waves for optimized picking. Wave release and completion status feed back into delivery scheduling.</li>
    </ul>

    <h2>Common breakpoints</h2>
    <h3>Delivery document not reaching EWM</h3>
    <ul>
      <li>Delivery type not configured for EWM distribution, or the warehouse number assignment is missing.</li>
      <li>Queue entry (SM58) shows RFC failure or the EWM system is unreachable.</li>
    </ul>

    <h3>Warehouse task creation failures</h3>
    <ul>
      <li>Storage bin determination failed — missing storage type search sequence or bin capacity exceeded.</li>
      <li>Handling unit requirements not met — packaging material missing or HU-managed storage type mismatch.</li>
    </ul>

    <h3>Stock discrepancy between S/4HANA and EWM</h3>
    <ul>
      <li>Goods receipt posted in S/4HANA but EWM putaway not confirmed — stock shows in S/4HANA but not in the correct EWM bin.</li>
      <li>Negative stock allowed in one system but not the other, causing reconciliation errors during inventory comparison.</li>
    </ul>

    <h3>Integration monitor errors</h3>
    <ul>
      <li><code>/SCWM/IMON</code> shows failed or stuck documents with specific error classes: delivery, task, or stock.</li>
      <li>Repeated reprocessing of the same document creates duplicates or locks.</li>
    </ul>

    <h2>Key transactions</h2>
    <ul>
      <li><code>/SCWM/IMON</code> — integration monitor for inbound and outbound documents.</li>
      <li><code>/SCWM/PRDI</code> — inbound processing monitor.</li>
      <li><code>/SCWM/PRDO</code> — outbound processing monitor.</li>
      <li><code>LT01</code> — create transfer order (classic WM; relevant in mixed landscapes).</li>
      <li><code>LT09</code> — confirm transfer order.</li>
    </ul>

    <h2>First-pass diagnostic questions</h2>
    <ul>
      <li>Is the delivery visible in EWM at all? Check <code>/SCWM/IMON</code> and the corresponding queue.</li>
      <li>Did the warehouse task get created, and if not, what is the specific error in task creation?</li>
      <li>Is the stock difference in total quantity or in bin-level location? EWM owns bin stock; S/4HANA owns plant-level stock.</li>
      <li>Was there a recent change in storage type search sequence, packaging material, or warehouse process type?</li>
      <li>Are both systems on the same release and support package level for the EWM integration component?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>An EWM integration ticket should state: delivery number, direction (inbound/outbound), whether the document reached EWM, the exact error in <code>/SCWM/IMON</code> or task log, and whether the issue is isolated to one warehouse number or one document type. "Stock is wrong" is not enough — specify which system shows the unexpected value and which document should have synchronized it.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers the S/4HANA–EWM integration boundary, not EWM configuration, layout design, or labor management. It does not cover classic WM (LE-WM) or decentralized EWM architecture in depth. It does not replace SAP EWM implementation or administration guides.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
