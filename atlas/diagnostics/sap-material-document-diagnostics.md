---
layout: default
title: "SAP Material Document Diagnostics"
description: "A conservative diagnostic frame for material document issues in SAP inventory management."
permalink: /atlas/diagnostics/sap-material-document-diagnostics/
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
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-stock-transfer-diagnostics/
  - /atlas/diagnostics/sap-physical-inventory-diagnostics/
  - /atlas/diagnostics/sap-reservation-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Material Document Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP material document diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a goods movement document is missing, incorrect, or cannot be reversed.</p>
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
    <h2>Core idea</h2>
    <p>Every goods movement in SAP creates a material document that records what moved, where, when, and with what accounting impact. When a document is missing, shows wrong quantities, posts to wrong accounts, or cannot be reversed, the support goal is to trace the document chain, identify the mismatch, and determine if a correction movement or reversal is needed.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>User reports a goods movement was posted but no material document exists.</li>
      <li>Material document shows wrong quantity, movement type, or storage location.</li>
      <li>Reversal fails because the original document is already reversed or cleared.</li>
      <li>Accounting document linked to the material document shows unexpected GL accounts.</li>
      <li>Goods movement posted in wrong period and period is now closed.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>User error:</strong> wrong quantity, movement type, or storage location entered during posting.</li>
      <li><strong>Document not saved:</strong> the user thought the document was posted but it was only simulated or an error prevented commit.</li>
      <li><strong>Already reversed:</strong> the original document was reversed earlier and a second reversal is not allowed.</li>
      <li><strong>Period closed:</strong> the posting period for MM or FI is closed, preventing new documents or reversals.</li>
      <li><strong>Valuation mismatch:</strong> the material document triggers a valuation that does not match the material's current valuation class or price.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MIGO — display material document by document number.</li>
      <li>MB51 — material documents list, filter by material, plant, or movement type.</li>
      <li>MBST — reversal transaction and error messages.</li>
      <li>MMRV — allow posting to previous period.</li>
      <li>FB03 — display accounting document linked to the material document.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>MKPF</strong> — material document header.</li>
      <li><strong>MSEG</strong> — material document items.</li>
      <li><strong>BKPF / BSEG</strong> — accounting documents.</li>
      <li><strong>MBEW</strong> — material valuation.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material document number or the expected document that is missing.</li>
      <li>Check MIGO or MB51 for the document details: material, plant, storage location, movement type, quantity.</li>
      <li>Verify the accounting document in FB03 to confirm GL accounts and amounts.</li>
      <li>If reversal is needed, check MBST for the reversal status and any error messages.</li>
      <li>Check posting period status if the reversal or new posting fails.</li>
      <li>Determine if the correction should be a reversal, a return movement, or a manual adjustment.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Reverse the incorrect document with MBST if the period is open and the document is not already reversed.</li>
      <li>Re-post the movement with correct data if the original was wrong.</li>
      <li>Open the posting period temporarily if the correction is urgent and authorized.</li>
      <li>If reversal is not possible, use a compensating movement to correct stock or accounting.</li>
      <li>Document the correction with business justification and approval.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Material document issues are usually user entry or timing problems. A useful ticket should include: material, plant, movement type, expected versus actual quantity, document number if it exists, and the business reason for correction.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>A material document was posted to the wrong material, plant, or storage location and must be reversed.</li>
      <li>The reversal affects inventory valuation, cost accounting, or a closed accounting period.</li>
      <li>Multiple documents show the same unexpected movement type or account assignment.</li>
      <li>The document ties to a production order, sales delivery, or physical inventory adjustment that needs cross-team validation.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a material document configuration guide. It does not cover WM transfer orders, EWM goods movements, or period-end closing procedures. It does not replace SAP's inventory management documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">SAP Stock Transfer Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
