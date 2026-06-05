---
layout: default
title: "SAP MM Procurement Overview"
description: "A practical overview of SAP Materials Management procurement from purchase requisition to goods receipt and invoice verification, with common breakpoints and diagnostic questions."
permalink: /atlas/sap/sap-mm-procurement-overview/
atlas_section: sap
domain: SAP operations
subdomain: Procurement and logistics
concept_type: SAP concept
sap_area: MM procurement
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - diagnostics
related:
  - /atlas/maps/procure-to-pay-map/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP MM Procurement Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP MM procurement overview</h1>
    <p class="note-subtitle">The procure-to-pay chain in SAP MM, where it breaks, and what to check first.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until procurement claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP Materials Management (MM) procurement is the chain from identifying a need to paying the supplier. The main documents are purchase requisition, purchase order, goods receipt, and invoice receipt. Each step depends on master data, organizational assignments, and configuration that varies by landscape. A support diagnostic should trace the failure to the specific document and step rather than treating "procurement is broken" as a single problem.</p>

    <h2>The document chain</h2>
    <ul>
      <li><strong>Purchase requisition (PR)</strong> — the internal request. Created manually, by MRP, or by a workflow. Must have a valid material or account assignment, plant, and purchasing organization.</li>
      <li><strong>Purchase order (PO)</strong> — the external commitment to the supplier. Created from the PR or directly. Must reference a valid supplier, agree on terms, and respect release strategies.</li>
      <li><strong>Goods receipt (GR)</strong> — the physical arrival and system confirmation. Creates a material document and updates stock or consumption. Must match the PO quantity, delivery note, and physical count.</li>
      <li><strong>Invoice receipt (IR)</strong> — the supplier's bill. Matched against the PO and GR. Differences in price or quantity trigger tolerance checks and blocking.</li>
      <li><strong>Payment</strong> — released after invoice verification clears. Depends on payment terms, cash discount, and approval workflows.</li>
    </ul>

    <h2>Common breakpoints</h2>

    <h3>Requisition to order</h3>
    <ul>
      <li>PR cannot be converted to PO — missing source of supply, invalid info record, or blocked supplier.</li>
      <li>Release strategy prevents PO creation — approval missing or workflow error.</li>
      <li>Organizational mismatch — purchasing organization or plant in the PR does not match the supplier's assignment.</li>
    </ul>

    <h3>Order to receipt</h3>
    <ul>
      <li>GR quantity exceeds PO quantity or delivery tolerance.</li>
      <li>Material not extended to the receiving plant or storage location.</li>
      <li>Movement type incorrect for the PO item category or account assignment.</li>
      <li>Quality inspection stock required but inspection lot not created.</li>
    </ul>

    <h3>Receipt to invoice</h3>
    <ul>
      <li>Invoice price differs from PO price beyond tolerance — blocked for manual review.</li>
      <li>Invoice quantity does not match GR quantity — partial deliveries or returns not reflected.</li>
      <li>Tax code or tax amount mismatch — often caused by supplier master or jurisdiction changes.</li>
      <li>GR/IR clearing account shows persistent imbalance — missing GR, missing IR, or return not processed.</li>
    </ul>

    <h3>Master data dependencies</h3>
    <ul>
      <li>Supplier master — roles, bank details, tax numbers, and purchasing organization assignment.</li>
      <li>Material master — purchasing view, valuation class, tax indicator, and plant extension.</li>
      <li>Info record — links material, supplier, and purchasing organization with agreed terms.</li>
      <li>Source list or quota arrangement — determines which supplier is valid for automatic sourcing.</li>
    </ul>

    <h2>First-pass diagnostic questions</h2>
    <ul>
      <li>Which document is failing — PR, PO, GR, IR, or payment?</li>
      <li>Is the failure isolated to one material, one supplier, one plant, or one user?</li>
      <li>Did any master data or configuration change in the last 48 hours?</li>
      <li>What is the exact error message and transaction code where it appears?</li>
      <li>Does the document flow (ME23N, ME53N, MIGO, MIRO) show the expected preceding document?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful procurement ticket should include: document number, item, plant, supplier, error message, transaction code, and whether the issue is recurring. Avoid asking the MM team to "fix procurement" without showing which document in the chain failed and what changed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is an overview, not a configuration guide. It does not cover every procurement variant — consignment, subcontracting, pipeline, stock transport, or third-party processing. It does not replace SAP's MM documentation or implementation guides.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
