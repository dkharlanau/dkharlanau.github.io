---
layout: default
title: "SAP Source Determination Diagnostics"
description: "A conservative diagnostic frame for source determination failures in SAP procurement."
permalink: /atlas/diagnostics/sap-source-determination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - purchasing
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-purchasing-info-record-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/maps/procure-to-pay-map/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Source Determination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP source determination diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why the system cannot determine a valid supplier for a purchase requisition or order.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Source determination is the logic that selects which supplier should fulfill a procurement need. When it fails, the PR cannot be converted to a PO or automatic PO creation produces no result. The support goal is to identify which source element is missing or invalid: info record, source list, quota arrangement, contract, or preferred supplier setting.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ME59N or ME21N reports 'no source of supply could be determined'.</li>
      <li>PR remains unassigned to a supplier after MRP run.</li>
      <li>Automatic PO creation skips certain materials even though a supplier exists.</li>
      <li>Wrong supplier is selected for a material that has multiple potential sources.</li>
      <li>Source list validity expired but users expected the supplier to remain valid.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing info record:</strong> no purchasing info record exists for the material, supplier, and purchasing organization combination.</li>
      <li><strong>Source list block:</strong> the source list entry is blocked, expired, or not marked as relevant for automatic sourcing.</li>
      <li><strong>Quota arrangement mismatch:</strong> the quota arrangement does not cover the required period or plant.</li>
      <li><strong>Supplier master block:</strong> the supplier is blocked for purchasing at the plant or organization level.</li>
      <li><strong>Plant / org mismatch:</strong> the material is not extended to the plant, or the supplier is not assigned to the purchasing organization.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME03 — source list display for material and plant.</li>
      <li>ME13 — info record display.</li>
      <li>MEQ1 — quota arrangement display.</li>
      <li>ME53N — PR item to see if a source was proposed.</li>
      <li>ME59N log — automatic PO creation rejection reasons.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EINA / EINE</strong> — purchasing info record.</li>
      <li><strong>A017</strong> — info record validity.</li>
      <li><strong>ESLH / ESLP</strong> — source list header and items.</li>
      <li><strong>EQBS / EQBP</strong> — quota arrangement.</li>
      <li><strong>LFA1 / LFB1</strong> — supplier master.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material, plant, and purchasing organization where source determination failed.</li>
      <li>Check ME03 for a valid source list entry.</li>
      <li>Check ME13 for a valid info record.</li>
      <li>Check MEQ1 for a quota arrangement if multiple suppliers exist.</li>
      <li>Verify the supplier master is not blocked and is extended to the purchasing organization.</li>
      <li>If automatic sourcing fails, test manual PO creation (ME21N) to isolate the issue.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or extend the purchasing info record for the material and supplier.</li>
      <li>Update the source list to include the correct supplier with valid dates.</li>
      <li>Adjust the quota arrangement if the wrong supplier is being selected.</li>
      <li>Unblock the supplier master or extend it to the required organization.</li>
      <li>If the material has no fixed source, train users to create POs manually or maintain the info record.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Source determination failures are almost always master data gaps. A useful ticket should include: material, plant, purchasing organization, the expected supplier, the transaction where the failure appeared, and whether a source list or info record ever existed.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>No valid source is found for a material across multiple plants or purchasing organizations.</li>
      <li>The selected source conflicts with an existing contract, quota arrangement, or procurement policy.</li>
      <li>Info records or outline agreements appear incorrect and procurement must confirm commercial validity.</li>
      <li>The issue affects a strategic material category or regulatory sourcing requirement.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a source determination configuration guide. It does not cover MRP sourcing logic, scheduling agreements, or outline agreements. It does not replace SAP's purchasing documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-purchasing-info-record-diagnostics/">SAP Purchasing Info Record Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
