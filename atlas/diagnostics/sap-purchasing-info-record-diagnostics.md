---
layout: default
title: "SAP Purchasing Info Record Diagnostics"
description: "A conservative diagnostic frame for purchasing info record issues in SAP MM."
permalink: /atlas/diagnostics/sap-purchasing-info-record-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - purchasing
related:
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Purchasing Info Record Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP purchasing info record diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a supplier, material, or price relationship is missing or invalid.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until info record behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>The purchasing info record links a material, a supplier, and a purchasing organization with agreed terms, prices, and delivery data. When it is missing, expired, or inconsistent, source determination fails, PO creation blocks, or prices default incorrectly. The support goal is to identify which info record element is missing and whether the gap is a master data maintenance issue or a sourcing policy change.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ME21N cannot find a price or delivery term for a material-supplier combination.</li>
      <li>ME59N skips a material because no valid info record exists.</li>
      <li>PO price differs from the expected contract or catalog price.</li>
      <li>Info record shows a plant-specific record that conflicts with the purchasing organization level.</li>
      <li>Old info record price is used even though a new price was negotiated.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing info record:</strong> no record was created for the material, supplier, and purchasing organization.</li>
      <li><strong>Expired validity:</strong> the info record validity period ended and was not extended.</li>
      <li><strong>Wrong organizational level:</strong> a plant-specific record exists but the PO uses a different plant, or vice versa.</li>
      <li><strong>Condition record mismatch:</strong> the price condition in the info record is not the one the pricing procedure expects.</li>
      <li><strong>Supplier block:</strong> the supplier is blocked for purchasing, making the info record inactive.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME13 — display info record for material, supplier, and purchasing organization.</li>
      <li>ME1N — info record list with validity dates.</li>
      <li>ME21N — check which price and terms default from the info record.</li>
      <li>ME59N log — see if missing info record is the rejection reason.</li>
      <li>A017 — info record validity table.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EINA / EINE</strong> — info record general and purchasing organization data.</li>
      <li><strong>A017</strong> — info record validity (condition technique).</li>
      <li><strong>LFA1 / LFB1</strong> — supplier master.</li>
      <li><strong>MARA / MARC</strong> — material master general and plant data.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material, supplier, and purchasing organization where the issue occurs.</li>
      <li>Check ME13 for an existing info record and its validity period.</li>
      <li>Verify the organizational level: general, purchasing organization, or plant-specific.</li>
      <li>Check if the supplier is blocked or not extended to the purchasing organization.</li>
      <li>Compare the info record price with the PO price to identify defaulting behavior.</li>
      <li>If the info record is missing, determine if it should be created manually or via info update from a previous PO.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or extend the info record with correct validity dates and terms.</li>
      <li>Update the info record price if a new agreement exists.</li>
      <li>Ensure the info record is maintained at the correct organizational level.</li>
      <li>Unblock the supplier master if the block is no longer valid.</li>
      <li>If the issue is recurring, review the process for maintaining info records after new supplier agreements.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Info record issues are master data maintenance gaps, not system errors. A useful ticket should include: material, supplier, purchasing organization, the expected price or term, the actual result, and whether the info record ever existed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an info record configuration guide. It does not cover condition technique setup, pricing procedure design, or outline agreements. It does not replace SAP's purchasing documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
