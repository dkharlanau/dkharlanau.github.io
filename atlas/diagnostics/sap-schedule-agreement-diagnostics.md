---
layout: default
title: "SAP Schedule Agreement Diagnostics"
description: "A conservative diagnostic frame for scheduling agreements, delivery schedules, and releases in SAP."
permalink: /atlas/diagnostics/sap-schedule-agreement-diagnostics/
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
  - scheduling-agreement
related:
  - /atlas/diagnostics/sap-purchase-order-diagnostics/
  - /atlas/diagnostics/sap-vendor-confirmation-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Schedule Agreement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP schedule agreement diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why scheduling agreement releases, delivery schedules, or confirmations do not match expectations.</p>
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
    <p>Scheduling agreements in SAP are outline purchase agreements with fixed delivery schedules. They combine the stability of an outline agreement with the detail of individual schedule lines. Problems usually appear as missing releases, incorrect quantities, or delivery dates that do not match the vendor confirmation. The diagnostic task is to compare the agreement header, the schedule lines, the release, and the inbound delivery or goods receipt.</p>
    <p>This guide covers standard scheduling agreement processing in MM, not JIT or Kanban-specific flows.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Release cannot be created for a scheduling agreement in ME38.</li>
      <li>Delivery schedule shows quantities or dates different from the vendor agreement.</li>
      <li>Goods receipt cannot be posted against a schedule line.</li>
      <li>MRP creates new schedule lines that conflict with an existing release.</li>
      <li>Vendor confirmation is not reflected in the scheduling agreement.</li>
      <li>Invoice verification fails because the purchase order history does not match the schedule.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing or expired schedule line:</strong> the requested delivery date falls outside the valid schedule lines.</li>
      <li><strong>Release strategy or blocking:</strong> the scheduling agreement or release is blocked and cannot be transmitted.</li>
      <li><strong>Source list or info record issue:</strong> the material and vendor combination is not valid for the plant.</li>
      <li><strong>Confirmation not updated:</strong> vendor confirmation was received but not entered in ME38.</li>
      <li><strong>MRP settings:</strong> lot size, rounding value, or schedule agreement MRP indicator causes unexpected quantities.</li>
      <li><strong>Organizational mismatch:</strong> plant, purchasing organization, or storage location differs between documents.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ME33N / ME32N</strong> — display/change scheduling agreement and schedule lines.</li>
      <li><strong>ME38</strong> — maintain scheduling agreement delivery schedules and releases.</li>
      <li><strong>ME2N / ME2L</strong> — list purchasing documents including scheduling agreements.</li>
      <li><strong>ME23N</strong> — purchase order history and goods receipt references.</li>
      <li><strong>ME11 / ME13</strong> — purchasing info record for price and vendor data.</li>
      <li><strong>ME01 / ME03</strong> — source list validity for the material and plant.</li>
      <li><strong>MMBE / MD04 / MD05</strong> — stock and MRP exception overview for schedule line impact.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKKO / EKPO</strong> — scheduling agreement header and item data.</li>
      <li><strong>EKET</strong> — scheduling agreement delivery schedule lines.</li>
      <li><strong>EKES</strong> — vendor confirmations against schedule lines.</li>
      <li><strong>EKKN</strong> — account assignment data for schedule agreement items.</li>
      <li><strong>EORD</strong> — source list entries.</li>
      <li><strong>EINA / EINE</strong> — purchasing info record general and purchasing-organization data.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Open the scheduling agreement in ME33N and confirm the agreement is not blocked or deleted.</li>
      <li>Review the schedule lines in the item detail and compare quantities and dates with the user report.</li>
      <li>Check ME38 for existing releases and whether the schedule line has an active release.</li>
      <li>Compare vendor confirmations in EKES or the confirmation tab with the schedule lines.</li>
      <li>Verify source list and info record validity for the material, vendor, and plant.</li>
      <li>Check MRP results in MD04/MD05 if quantities look unexpected.</li>
      <li>Review purchase order history in ME23N to confirm receipts and invoices match the schedule.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Add or correct schedule lines in ME38 to match the required delivery dates and quantities.</li>
      <li>Release the scheduling agreement or release document if a release strategy is blocking it.</li>
      <li>Enter or correct vendor confirmations in the confirmation tab.</li>
      <li>Update the source list or info record if the vendor is not valid for the plant.</li>
      <li>Adjust MRP lot-size settings if MRP creates schedule lines with rounding issues.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the scheduling agreement number, item number, schedule line number, release number, material, plant, vendor, expected quantity and date, actual quantity and date, and any exact error message from ME38 or goods receipt.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Multiple scheduling agreements show missing releases after an MRP run.</li>
      <li>Vendor confirmations are systematically not reflected in delivery schedules.</li>
      <li>EDI or IDoc inbound schedules fail to update scheduling agreements.</li>
      <li>Release strategy configuration blocks a high volume of agreements.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for standard scheduling agreement processing, not a guide to JIT/Kanban, vendor-managed inventory, or EDI message design. It does not cover subcontracting scheduling agreements.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
