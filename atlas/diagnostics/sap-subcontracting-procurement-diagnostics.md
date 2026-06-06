---
layout: default
title: "SAP Subcontracting Procurement Diagnostics"
description: "A conservative diagnostic frame for subcontracting procurement issues in SAP MM."
permalink: /atlas/diagnostics/sap-subcontracting-procurement-diagnostics/
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
  - /atlas/diagnostics/sap-consignment-procurement-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Subcontracting Procurement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP subcontracting procurement diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why subcontracting components are not issued, finished goods are not received, or costs are misallocated.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM special procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until subcontracting procurement behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Subcontracting procurement means the company provides components to a supplier who assembles or processes them into a finished product. When components cannot be issued, finished goods cannot be received, or costs do not match expectations, the support goal is to identify whether the issue is in the BOM, component stock, PO item category, goods issue, or goods receipt process.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ME2N shows subcontracting PO but components cannot be issued to the supplier.</li>
      <li>Goods issue (MB1B 541) fails due to missing component stock or wrong storage location.</li>
      <li>Goods receipt of finished product does not consume the expected component quantity.</li>
      <li>Subcontracting stock shows in MMBE but is not available for issue.</li>
      <li>Invoice verification shows wrong price or missing component cost.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing BOM:</strong> the subcontracting PO references a BOM that is missing, expired, or has wrong component quantities.</li>
      <li><strong>Component stock shortage:</strong> the required components are not in stock at the issuing plant or storage location.</li>
      <li><strong>Wrong PO item category:</strong> the PO item is not set to L (subcontracting), so the system does not expect component issue or BOM explosion.</li>
      <li><strong>Goods issue not posted:</strong> the finished product was received but components were never issued, causing stock and cost mismatches.</li>
      <li><strong>Over- or under-consumption:</strong> the supplier used more or fewer components than the BOM specifies, and the variance was not adjusted.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME23N — subcontracting PO with BOM and component overview.</li>
      <li>MB1B / MIGO — component issue to subcontractor (movement type 541).</li>
      <li>MMBE — component stock at plant and subcontractor stock.</li>
      <li>ME2N — PO history showing goods issue and receipt.</li>
      <li>CK13N — cost estimate for finished product including component costs.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKPO / EKBE</strong> — PO items and history.</li>
      <li><strong>MKPF / MSEG</strong> — material documents (541 for issue, 101 for receipt).</li>
      <li><strong>MSLB</strong> — subcontracting stock at supplier.</li>
      <li><strong>STPO / STAS</strong> — BOM items.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the subcontracting PO and the exact error during component issue or finished goods receipt.</li>
      <li>Check ME23N for the BOM and component list. Verify the BOM is valid and components are correct.</li>
      <li>Check MMBE or MB52 for component stock availability at the issuing plant.</li>
      <li>Verify the PO item category is L (subcontracting).</li>
      <li>Check ME2N or MIGO for goods issue documents (541) and goods receipt documents (101).</li>
      <li>Compare expected component consumption (BOM quantity × finished quantity) with actual consumption.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Update or create the BOM if it is missing or has wrong component quantities.</li>
      <li>Transfer or procure missing components before issuing to the subcontractor.</li>
      <li>Correct the PO item category to L if it was wrong.</li>
      <li>Post the missing component issue (541) before or with the goods receipt.</li>
      <li>Adjust component consumption with a subsequent adjustment movement if actual usage differed from BOM.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Subcontracting issues are usually BOM or stock availability problems. A useful ticket should include: PO number, finished material, component material, expected and actual component quantities, movement types used, and any BOM or stock errors.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a subcontracting configuration guide. It does not cover BOM design, routing, or production integration. It does not replace SAP's special procurement documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-consignment-procurement-diagnostics/">SAP Consignment Procurement Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
