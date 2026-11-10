---
layout: default
title: "SAP Stock Transfer Diagnostics"
description: "Trace STO goods issue, stock in transit, goods receipt and safe correction options in SAP S/4HANA."
permalink: /atlas/diagnostics/sap-stock-transfer-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory management
concept_type: diagnostic guide
sap_area: "MM inventory management"
business_process: Inventory / Logistics
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
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
  - /atlas/concepts/sap-stock-exists-not-promisable/
robots: index,follow
sitemap: true
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
    <p class="note-subtitle">Identify the posting route before treating stock in transit as lost stock.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory / Logistics</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The decision: where did the quantity stop?</h2>
    <p>A store is short of material, while the supplying plant says the transfer has left. Before posting a goods receipt (GR), find out which SAP transfer process was used. A direct transfer posting, a stock transport order (STO) without delivery, and an STO with outbound delivery do not have the same document flow or in-transit stock behavior.</p>
    <p><strong>Start with the document chain, not the stock balance.</strong> The next safe action depends on whether goods issue (GI) happened, whether the goods arrived physically, and whether a valid GR or reversal already exists.</p>

    <h2>Follow the business chain</h2>
    <ul>
      <li><strong>Direct one-step transfer:</strong> a single posting moves the stock. Standard examples are movement 301 between plants and 311 between storage locations within a plant. There is no separate receiving step to chase.</li>
      <li><strong>Direct two-step transfer:</strong> issue and receipt are separate. Standard plant-to-plant movements 303 then 305 use <em>stock in transfer</em>; storage-location movements 313 then 315 follow a different stock-in-transfer path. Do not confuse either with an STO.</li>
      <li><strong>STO without outbound delivery:</strong> Purchasing creates the STO, Inventory Management posts GI (commonly 351), and the receiving plant posts GR (commonly 101). The STO and PO history link the steps.</li>
      <li><strong>STO with outbound delivery:</strong> Purchasing → shipping delivery → picking / GI → transport → receiving GR. For a standard intra-company two-step flow, GI commonly uses 641 and GR 101. A one-step delivery-based STO may use 647 and does not require a second GR. Cross-company transfers and advanced/valuated stock-in-transit scenarios have different accounting and document rules: confirm the process variant before using these movement types as a checklist.</li>
    </ul>
    <p>These are <strong>SAP standard examples</strong>, not instructions to select a movement type manually. Delivery relevance, one-step versus two-step setup, movement types, valuation, and receipt references depend on the system and its configuration.</p>

    <h2>Why the same symptom has different causes</h2>
    <p><strong>Synthetic case:</strong> an intra-company STO requests 20 units. Its outbound delivery shows GI for 20, but the receiving plant has recorded GR for only 14. The six-unit difference may be goods still travelling, a partial receipt, damage under investigation, a missing receipt posting, or a document-reference problem. It is <em>not</em> proof that six units are lost or that SAP needs a stock correction.</p>
    <p>If GI is missing, investigate the source-side delivery and picking process first. If GI exists but GR is missing, compare the receiving evidence and PO history. If GR exists but inventory still looks wrong, check the receiving stock type, reversal, batch, storage location and unit of measure before creating another posting.</p>
    <p>For MRP, separate <strong>physical availability</strong> from a <strong>planned receipt</strong>. An STO can be relevant to MRP even while its shipped quantity is not unrestricted-use stock. Check the actual stock category and the material's planning elements (for example, MD04 in an applicable on-premise setup); do not assume that changing an MRP view will make goods in transit usable.</p>

    <h2>Evidence-first diagnostic workflow</h2>
    <ol>
      <li><strong>Identify the scenario:</strong> plant and company-code relationship, material, quantity and unit, direct transfer versus STO, delivery present or absent, and the expected one-step or two-step procedure.</li>
      <li><strong>Find the last completed event:</strong> for an STO, read the item and purchase order history in ME23N (EKPO / EKBE); for delivery-based flows, trace the outbound delivery and its goods-movement status in VL03N or the relevant Fiori apps. A created delivery is not proof of GI.</li>
      <li><strong>Reconcile documents by item:</strong> inspect material documents, GI and GR quantities, posting dates, reversals, and references using the available material-document display or MIGO display function. Compare posted quantities, not just the ordered quantity.</li>
      <li><strong>Read stock in the correct category:</strong> MMBE and relevant stock reports can help. MB5T is useful for classic intra-company STO stock in transit; it is not a universal cross-company or advanced stock-in-transit reconciliation report. For direct two-step transfers, look for <em>stock in transfer</em> instead.</li>
      <li><strong>Confirm physical evidence:</strong> dispatch record, carrier proof, receipt scan, damage/shortage report, and whether a receiving queue or interface is waiting. Do not post GR based only on a screen showing stock in transit.</li>
      <li><strong>Check FI and planning only where the flow requires it:</strong> cross-plant valuation may post accounting at the issuing step; cross-company processes can include clearing and billing. Reconcile the actual documents with Finance before any backdated or month-end correction.</li>
    </ol>
    <p><strong>Data-model boundary:</strong> in SAP S/4HANA, material documents use MATDOC as the central persistence model. Older MKPF / MSEG interfaces can still be accessible for compatibility; do not design a new reconciliation around direct updates to those tables.</p>

    <h2>Three resolution paths</h2>
    <ol>
      <li><strong>Goods arrived, receipt not recorded:</strong> the receiving team verifies the physical quantity and posts the permitted GR against the correct STO or delivery reference. Recheck PO history and the destination stock type. <em>Risk:</em> a second GR creates an overstatement if the receipt already exists.</li>
      <li><strong>Wrong or duplicate posting:</strong> identify the original material document, downstream documents and accounting period. An authorized MM/FI owner assesses reversal and reposting in the supported process, with a traceable reason. <em>Risk:</em> blind reversals can break delivery history, inventory valuation or period-close controls.</li>
      <li><strong>Repeated gap across transfers:</strong> compare the configured process with the intended business flow. Fix the relevant delivery, interface, receiving, or master-data control, then retest GI → transit/transfer → GR and the FI effect on a controlled example. <em>Risk:</em> changing movement or MRP settings globally to clear one incident can create new discrepancies.</li>
    </ol>

    <h2>A small SAP + AI experiment: suggest the next check, never the posting</h2>
    <p><strong>Proposed offline pilot, not a reported implementation:</strong> prepare 40 synthetic transfer cases with process variant, PO/delivery references, GI and GR totals, reversal flags, stock category, and a short receiving note. Two reviewers agree on a reference classification and the next <em>read-only</em> check. Do not use live customer, carrier, user or financial data.</p>
    <p>Run a <strong>rule-based baseline</strong> first: if no STO, select the direct-transfer branch; if a delivery exists without GI, check shipping; if GI exceeds GR, request receiving evidence; if GR exceeds net GI or references do not match, escalate for reconciliation. Compare this with an AI assistant given the same sanitized case and the source-backed decision rules.</p>
    <p>Over 10 working days, measure (1) correct next-check recommendation against the two-reviewer reference, (2) missing or invented evidence, and (3) unsafe posting advice. Report both methods on the same 40 cases, including cases where the answer is <em>insufficient evidence</em>. <strong>Stop</strong> if the assistant invents a posted document, recommends an unapproved write, or exposes identifiable data. No SAP API connection or write authorization is needed. A human MM/logistics owner decides every operational action.</p>

    <h2>What a useful support ticket contains</h2>
    <p>Capture the transfer process, source and receiving plants, company-code relationship, material and unit, STO/item or direct-transfer reference, outbound delivery (if any), net GI and GR material documents, stock category, expected arrival, physical evidence, and whether Finance or a period close is affected. If the same symptom repeats, state how many transfers are affected.</p>

    <h2>Scope and sources</h2>
    <p>This guide focuses on standard SAP S/4HANA on-premise-oriented MM/LE diagnosis; transaction availability differs in cloud editions. EWM, advanced intercompany and valuated stock-in-transit processes need their own variant-specific checks. The synthetic case and AI pilot above are illustrative, not project results.</p>
    <ul>
      <li><a href="https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/performing-stock-transfers-between-plants">SAP Learning — Performing Stock Transfers Between Plants</a> (direct transfer, STO, movement and valuation principles).</li>
      <li><a href="https://learning.sap.com/courses/configuring-cross-application-processes-in-sap-s-4hana-sales-and-procurement/setting-up-a-stock-transfer-process-for-an-intra-company-stock-transfer_ad0e9a99-4f15-42d1-9ba5-8eecac49d235">SAP Learning — Setting Up an Intra-Company Stock Transfer</a> (STO, shipping, one-step versus two-step and MRP).</li>
      <li><a href="https://help.sap.com/docs/SAP_ERP/39d6d7a325d04826b95328b25fad91ab/0962bd534f22b44ce10000000a174cb4.html">SAP Help — STO with Delivery via Shipping</a> (641 / 647 flow and goods receipt reference).</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/75bcb6531de6b64ce10000000a174cb4.html">SAP Help — Archiving Material Documents</a> (MATDOC and compatibility views).</li>
    </ul>
    <p>For the underlying distinction between stock in transfer and stock in transit, see <a href="/atlas/sap/sap-stock-transfer-in-transit/">Stock Transfer and In-Transit Inventory</a> (separate working note, pending verification).</p>
    <p class="disclaimer">This is not official SAP documentation. Confirm the process and permissions in the target system before making changes.</p>
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
