---
layout: default
title: "SAP ATP Is Not Inventory"
description: "A practical explanation of why SAP available-to-promise is customer commitment logic, not a simple inventory count."
permalink: /atlas/concepts/sap-atp-is-not-inventory/
atlas_section: concepts
domain: SAP operations
subdomain: Sales and fulfillment
concept_type: business concept
sap_area: "SD availability check / ATP"
business_process: Order to cash
status: reviewed
verified: true
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /services/sap-ams-consulting/
source_files:
  - "private-source/kb-drafts/sap-domain-atlas/domains/sales/concepts/atp.md"
robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP ATP Is Not Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concept</p>
    <h1>SAP ATP is not inventory</h1>
    <p class="note-subtitle">ATP is promise logic. Inventory is stock visibility. Confusing the two creates bad support tickets and bad customer commitments.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Availability check / ATP</dd></div>
      <div><dt>Reviewed</dt><dd>06 May 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Available-to-promise answers a commitment question: what quantity can the business responsibly promise to a customer, and when? It is not the same as asking what quantity exists physically in a plant or warehouse.</p>
    <p>Inventory can exist and still be unavailable for a new promise. It may already be committed to another order, blocked for quality, reserved for production, held in the wrong location, or not considered by the relevant availability check configuration.</p>

    <h2>Why the distinction matters</h2>
    <p>Many support issues start with a simple mismatch: a user sees stock in one report, but the sales order confirms less than expected. The first reaction is often “ATP is wrong.” A better first question is: which supply and demand elements is the check allowed to consider for this material, plant, date, and document context?</p>
    <p>The answer depends on master data, configuration, document type, timing, existing commitments, and sometimes product allocation or supply protection rules. The exact behavior is landscape-specific.</p>

    <h2>Practical diagnostic questions</h2>
    <ul>
      <li>Is the stock physically available, unrestricted, and relevant for the plant or storage location being checked?</li>
      <li>Are existing sales orders, reservations, or dependent requirements already consuming the supply?</li>
      <li>Are purchase orders, production orders, or planned receipts included in the check scope?</li>
      <li>Is the requested delivery date before the next reliable receipt?</li>
      <li>Is a product allocation, supply protection, or special stock rule changing the result?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Do not diagnose ATP from stock quantity alone. Diagnose it as a time-based promise calculation shaped by business commitments, supply reliability, and configuration. A useful ATP support note should include the material, plant, requested date, confirmed date, confirmed quantity, visible stock, open requirements, open receipts, and the document context that triggered the check.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/services/sap-ams-consulting/">SAP AMS consulting</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
