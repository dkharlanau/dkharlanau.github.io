---
layout: default
title: "SAP RFQ and Quota Arrangement Diagnostics"
description: "A conservative diagnostic frame for RFQ, quotation, quota arrangement, and source split issues in SAP."
permalink: /atlas/diagnostics/sap-rfq-quota-arrangement-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - quota-arrangement
related:
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/diagnostics/sap-purchasing-info-record-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP RFQ and Quota Arrangement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP RFQ and quota arrangement diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why request for quotation, quotation comparison, or quota arrangement source split behaves unexpectedly.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>RFQs and quotations support competitive sourcing, while quota arrangements distribute requirements across multiple vendors according to predefined quotas. Problems appear as missing RFQ outputs, quotation prices that do not copy correctly, or source determination that ignores the quota arrangement. The diagnostic task is to check the quota master data, the quotation validity, and the source determination sequence.</p>
    <p>This guide focuses on operational sourcing and quota arrangement issues, not strategic sourcing or SAP SRM functionality.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>RFQ cannot be created from a purchase requisition in ME41.</li>
      <li>Quotation prices are not copied into the info record or purchase order.</li>
      <li>Source determination selects a vendor outside the quota arrangement.</li>
      <li>Quota arrangement percentages do not match actual purchase order splits.</li>
      <li>PR to PO conversion ignores the quota arrangement and always picks one vendor.</li>
      <li>Quotation is marked as rejected and blocks subsequent source determination.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing or inactive quota arrangement:</strong> no quota exists for the material and plant, or it is outside the validity period.</li>
      <li><strong>Quota not included in source determination:</strong> the source determination logic or info record priority overrides the quota.</li>
      <li><strong>Invalid quotation:</strong> the quotation is expired, rejected, or has a different purchasing organization.</li>
      <li><strong>Info record mismatch:</strong> the copied quotation did not create or update the info record correctly.</li>
      <li><strong>Plant or material mismatch:</strong> the quota arrangement was created for a different plant or material.</li>
      <li><strong>Custom enhancement:</strong> a user exit changes source determination behavior.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ME41 / ME42 / ME43</strong> — create/change/display RFQ and quotation data.</li>
      <li><strong>ME47</strong> — maintain quotation prices and conditions.</li>
      <li><strong>ME48</strong> — quotation comparison list.</li>
      <li><strong>MEQ1 / MEQ3</strong> — maintain/display quota arrangement.</li>
      <li><strong>ME11 / ME13</strong> — purchasing info record created from quotation.</li>
      <li><strong>ME01 / ME03</strong> — source list and source determination check.</li>
      <li><strong>ME51N / ME53N</strong> — purchase requisition source of supply.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKKO / EKPO</strong> — RFQ/quotation document header and item.</li>
      <li><strong>EKKN</strong> — account assignment in RFQ/quotation.</li>
      <li><strong>A501-A504</strong> — info record condition tables (examples; actual tables depend on access sequence).</li>
      <li><strong>EINA / EINE</strong> — purchasing info record general and org-level data.</li>
      <li><strong>EQBS / EQBE</strong> — quota arrangement item and source details.</li>
      <li><strong>EORD</strong> — source list entries.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material, plant, and vendors involved in the expected source split.</li>
      <li>Open MEQ3 and check whether a valid quota arrangement exists for the material and plant.</li>
      <li>Review the quota percentages, minimum quantity, and allocated quantity for each vendor.</li>
      <li>Check ME13 for info records linked to the quota vendors and confirm validity.</li>
      <li>If a quotation is involved, verify ME43/ME47 for price, validity, and rejection status.</li>
      <li>Run source determination for the PR in ME53N or ME57 and compare the result with the quota.</li>
      <li>Check ME03 for source list entries that might override the quota.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or extend the quota arrangement in MEQ1 for the missing material and plant.</li>
      <li>Correct quota percentages or minimum quantities to reflect the intended source split.</li>
      <li>Update or extend the quotation validity and reject status in ME42/ME47.</li>
      <li>Create or update the info record from the accepted quotation.</li>
      <li>Adjust source list entries so they do not override the quota arrangement.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the material, plant, purchasing organization, quota arrangement number, vendors, expected and actual split percentages, RFQ/quotation numbers, info record numbers, and the exact symptom from source determination or PO creation.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Quota arrangements are ignored across many materials after a system change.</li>
      <li>Quotations cannot be copied into info records systematically.</li>
      <li>Source determination results differ between PR conversion and standalone PO creation.</li>
      <li>A custom enhancement is suspected to alter sourcing logic.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for operational RFQ, quotation, and quota arrangement behavior, not a guide to supplier negotiation, strategic sourcing, or SAP Ariba integration.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
