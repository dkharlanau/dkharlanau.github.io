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
level: 1
robots: noindex,follow
sitemap: false
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
    <h2>Start with the last completed step</h2>
    <p>A sales order can have a confirmed quantity while the warehouse cannot pick it. A warehouse can also finish picking while goods issue is still open in SAP. These are different failures. Find the last completed business event before choosing a transaction or changing data.</p>
    <p>This guide follows a normal stock sale in SAP S/4HANA: sales order and availability confirmation, outbound delivery, picking and packing where required, post goods issue (PGI), then delivery-related billing. In a typical valuated stock sale, PGI reduces inventory and records the inventory value change and cost of goods sold. Billing records revenue and customer receivables. Some processes, including configured EWM direct billing, allow billing before goods issue; check the actual process design rather than assuming that this sequence is universal.</p>

    <h2>Find the owner of the failed step</h2>
    <ol>
      <li><strong>No delivery exists:</strong> read the sales order item and schedule lines, delivery due date, incompletion and relevant credit or delivery blocks. Check the actual shipping point and route. In the conventional determination model the shipping point depends on delivering plant, shipping condition and loading group; plant-only determination is also available in supported configurations. A route depends on shipping data and influences scheduling. A missing route is not proof of a picking or PGI problem.</li>
      <li><strong>Delivery exists but picking is incomplete:</strong> compare required and confirmed picking quantities by item, unit, storage location and batch. Check the warehouse execution model before looking for warehouse documents. Inventory stock and ATP confirmation do not prove that the correct stock is physically available for picking.</li>
      <li><strong>Picking is complete but PGI is open:</strong> inspect packing, batch or serial requirements, warehouse status and the last posting error. If the error concerns posting period, movement or account determination, route it to the MM/FI owner with the exact message and organizational context.</li>
      <li><strong>Warehouse reports goods issue but S/4HANA does not:</strong> check the warehouse outbound document, goods issue confirmation and relevant integration monitor. Compare document references, quantities and times. Do not start a second goods issue to make the status match.</li>
      <li><strong>PGI is complete:</strong> inspect the delivery document flow, material document and associated accounting document where expected. If the invoice is still missing, investigate billing relevance, due date or billing block instead of repeating the warehouse process.</li>
    </ol>

    <h2>Read the correct warehouse evidence</h2>
    <ul>
      <li><strong>Inventory Management without warehouse task processing:</strong> read delivery item quantities and status; check stock by plant, storage location and batch. In classic SAP GUI, VL03N and MMBE are useful display transactions. In supported cloud scenarios, the Pick Outbound Delivery app (F0868) shows picking progress.</li>
      <li><strong>Classic WM / Stock Room Management:</strong> inspect the transfer order and its confirmation if the delivery uses that process. LT03 and LT12 are execution transactions, not read-only checks; use existing display evidence rather than creating or confirming a transfer order during diagnosis.</li>
      <li><strong>Extended Warehouse Management (EWM):</strong> inspect the outbound delivery order and the planned and confirmed warehouse tasks. A completed picking planning status means that tasks cover the required quantity, not that the physical picking has been confirmed. EWM reports goods issue and reversals to S/4HANA; inspect the confirmation path if the documents disagree.</li>
    </ul>
    <p>For the sales order use VA03, and for the outbound delivery use VL03N where these transactions are available. CO09 may help investigate the availability situation in classic ATP scenarios; use the availability tool appropriate to your release and checking model. Transaction and app availability depends on edition, release and authorizations. Do not use a production PGI attempt as a diagnostic probe: it may succeed and post real stock and financial changes.</p>

    <h2>Worked example: 10 ordered, 8 picked</h2>
    <p><em>Synthetic example, not a project incident.</em> A delivery contains 10 units. The inventory snapshot shows 10 units, the warehouse task plan covers 10, but confirmed picking is only 8. PGI is open. The two unconfirmed units are the first gap in the evidence. The snapshot alone cannot tell us whether the remaining stock is in the wrong bin, unavailable for picking, or simply not yet confirmed.</p>
    <p>Now change one condition: all 10 units are confirmed and EWM records goods issue, but the S/4HANA delivery still shows PGI open. The next check is the goods issue confirmation and its processing result, not a stock transfer or a new goods issue. A status lag is a possible explanation, not a confirmed root cause.</p>

    <h2>Three ways to resolve the case</h2>
    <ol>
      <li><strong>Complete the warehouse process:</strong> if the warehouse owner confirms that the goods are present and the remaining task is valid, complete picking and the required shipping activities through the approved process. If stock is genuinely short, agree a permitted quantity change or later shipment with sales and the warehouse. Never confirm quantities that were not physically handled.</li>
      <li><strong>Resolve a confirmation or integration issue:</strong> if goods issue already exists at the warehouse, establish whether the target posting succeeded, failed or is still pending. The integration owner can evaluate controlled recovery of the existing confirmation after checking for an existing material document and duplicate risk. Reconcile both systems before closing the case.</li>
      <li><strong>Correct a posting control:</strong> if warehouse readiness is established and the existing PGI error identifies an MM/FI control, investigate the posting date, relevant movement and account settings in the target system. Correct the proven cause with the responsible owner; test changes outside production and use the approved posting procedure. Do not widen controls or bypass an accounting error to meet a shipment deadline.</li>
    </ol>
    <p>Closure means that the physical shipment, delivery quantity and goods movement agree, the expected accounting evidence exists, and the next billing step is either available or has a separately explained status. For partial shipments, also check the remaining order quantity. Do not use a green status alone as proof.</p>

    <h2>Try an offline SAP + AI experiment</h2>
    <p>Hypothesis: an assistant can group delivery, warehouse and posting evidence into a more useful next-check recommendation than a fixed decision tree. No SAP API or system access is needed. Over 10 working days, prepare 40 synthetic or approved anonymized case snapshots: eight each for no delivery, incomplete picking, posting error, confirmation mismatch and completed PGI with a billing issue. Include stale snapshots and missing evidence across the groups. A consultant labels the correct next check and owner before testing.</p>
    <p>Give both methods the same data: document and item aliases, warehouse model, quantity and unit, picking and PGI statuses with timestamps, material document presence, error text and billing status. The rule-based baseline follows the five steps above and returns “insufficient evidence” when the key field is missing. The assistant must return one next check, the supporting evidence identifiers, the owner and any missing evidence. Use a fixed prompt and a held-out set; do not tune on the test cases.</p>
    <p>Measure correct next-check recommendations out of 40, false warehouse-shortage flags among cases without a confirmed shortage, unsupported recommendations and median analyst review time including correction. Proposed success criteria: at least the baseline accuracy, no increase in false shortage flags, at least 20% lower median review time and zero recommendations to post or repeat goods issue without evidence and approval. Stop the trial on any unsafe posting recommendation or exposure of sensitive data. Otherwise keep the rule-based method if the assistant does not meet the targets. The consultant decides the next action; the assistant has no SAP credentials, write-back, execution or approval rights. These are test targets, not measured results.</p>

    <h2>Sources and review boundary</h2>
    <ul>
      <li><a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-sales-fundamental-business-processes/understanding-the-sell-from-stock-process_f487b5b8-429f-4f14-bacf-39d063789bad">SAP Learning: Understanding the Sell from Stock Process</a> — process sequence and accounting effects in a normal stock sale.</li>
      <li><a href="https://help.sap.com/docs/PRODUCT_ID/c7894a248ca14f74aca67f97528e5ad7/5d1bbf53d25ab64ce10000000a174cb4.html">SAP Help: Shipping Points</a> — determination variants and delivery constraints.</li>
      <li><a href="https://learning.sap.com/courses/discovering-extended-warehouse-management-with-sap-s-4hana/posting-the-goods-issue-for-a-sales-order_c0ec19d1-076a-4974-927d-67f6540aa719">SAP Learning: Posting the Goods Issue for a Sales Order</a> — route, shipping data and scheduling.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9832125c23154a179bfa1784cdc9577a/3ecccb53ad377114e10000000a174cb4.html">SAP Help: Creation of Warehouse Tasks for Stock Removal</a> — planned picking quantities and planning status in EWM.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9832125c23154a179bfa1784cdc9577a%20/adc8cb53ad377114e10000000a174cb4.html">SAP Help: Processing of Outbound Deliveries</a> — EWM goods issue confirmations and the direct-billing exception.</li>
      <li><a href="https://help.sap.com/docs/sap_s4hana_on-premise/b2dee5e83e2446149294f9860a7c08f0/e15bbb536b13b44ce10000000a174cb4.html">SAP Help: Transfer Order</a> — the role of transfer orders in classic WM.</li>
      <li><a href="https://help.sap.com/docs/PRODUCT_ID/aff0b3f5f46c42a2b2c0fabfc233bab2/a15a8a566641d95fe10000000a441470.html">SAP Help: Pick Outbound Delivery</a> — picking and goods issue in supported cloud scenarios.</li>
    </ul>
    <p>Public SAP sources were checked on 24 November 2026. The diagnostic sequence and experiment are proposed guidance; exact status behavior, configuration and recovery procedures require review in the relevant release. Author: Dzmitryi Kharlanau. New editorial and SAP functional review pending author approval. No system test or experiment result is claimed.</p>
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
