---
layout: default
title: "SAP Consignment Procurement Diagnostics"
description: "A conservative diagnostic frame for consignment procurement issues in SAP MM."
permalink: /atlas/diagnostics/sap-consignment-procurement-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM special procurement"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - special-procurement
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Consignment Procurement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP consignment procurement diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why consignment stock is not visible, cannot be consumed, or creates wrong liability postings.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM special procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until consignment procurement behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Consignment procurement means the supplier places stock at the customer's premises, but ownership only transfers when the stock is consumed. When consignment stock is not visible, cannot be issued, or creates unexpected liability postings, the support goal is to identify whether the issue is in the special procurement type, the consignment info record, the goods issue process, or the settlement run.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Consignment stock does not appear in MMBE or MB52 for the supplier.</li>
      <li>Goods issue against consignment stock fails with 'no stock available'.</li>
      <li>Consignment settlement (MRKO) does not create the expected liability or invoice document.</li>
      <li>Wrong supplier is charged for consignment consumption.</li>
      <li>Consignment stock was received but the liability posting is missing or delayed.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Wrong special procurement type:</strong> the material or plant does not use the consignment special procurement type (K).</li>
      <li><strong>Missing consignment info record:</strong> no info record exists for consignment with the supplier and purchasing organization.</li>
      <li><strong>Stock not in consignment:</strong> the goods receipt was posted as own stock instead of consignment stock.</li>
      <li><strong>Settlement run issue:</strong> MRKO was not run, or the settlement period is closed.</li>
      <li><strong>Supplier master mismatch:</strong> the consignment stock is linked to a different supplier than the one in the settlement run.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MMBE / MB52 — stock overview showing consignment stock per supplier.</li>
      <li>ME13 — consignment info record display.</li>
      <li>MIGO — material document showing movement type and special stock indicator.</li>
      <li>MRKO — consignment settlement run and results.</li>
      <li>MB51 — material documents for consignment receipts and issues.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>MKPF / MSEG</strong> — material documents (special stock indicator K).</li>
      <li><strong>MSLB / MSKA</strong> — special stock tables for consignment.</li>
      <li><strong>EINA / EINE</strong> — consignment info record.</li>
      <li><strong>RBKP / RSEG</strong> — settlement documents.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material, supplier, and plant where consignment stock is expected.</li>
      <li>Check MMBE or MB52 for consignment stock quantity and supplier assignment.</li>
      <li>Verify the material master uses special procurement type K for consignment.</li>
      <li>Check ME13 for a valid consignment info record.</li>
      <li>Review MIGO documents to confirm receipts were posted as consignment (movement type 101 K).</li>
      <li>Check MRKO settlement status and any error messages.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the special procurement type in the material master if it was wrong.</li>
      <li>Create or extend the consignment info record for the supplier and purchasing organization.</li>
      <li>Reverse and re-post the goods receipt as consignment if it was posted as own stock.</li>
      <li>Run MRKO for the correct supplier and period to generate settlement documents.</li>
      <li>Investigate repeated settlement failures as potential process or scheduling issues.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Consignment issues are usually master data or process errors in receiving and settlement. A useful ticket should include: material, supplier, plant, expected consignment stock, actual stock visible, movement type used, and settlement run status.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a consignment procurement configuration guide. It does not cover vendor-managed inventory (VMI), pipeline materials, or consignment pricing. It does not replace SAP's special procurement documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
