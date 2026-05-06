---
layout: default
title: "SAP Sales Order Block Diagnosis"
description: "A practical diagnostic frame for separating common SAP sales order block causes in AMS support."
permalink: /atlas/diagnostics/sap-sales-order-block-diagnosis/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Sales order support
concept_type: diagnostic guide
sap_area: "SD sales order processing"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/concepts/sap-atp-is-not-inventory/
  - /services/sap-ams-consulting/
source_files:
  - "private-source/kb-drafts/sap-domain-atlas/publishing/article-backlog.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/sales/concepts/delivery-block.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/sales/concepts/billing-document.md"
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Sales Order Block Diagnosis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP sales order block diagnosis</h1>
    <p class="note-subtitle">A first-pass structure for finding why an order is stopped before delivery, billing, or completion.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales order processing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until detailed block behavior is verified against a target SAP context.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>A blocked sales order is a symptom, not a root cause. The block may be intentional control, incomplete master data, credit exposure, delivery constraints, billing relevance, compliance logic, or custom governance.</p>
    <p>The support goal is to identify which control is active and whether it is working as designed.</p>

    <h2>First split</h2>
    <ul>
      <li><strong>Incomplete order:</strong> required fields are missing or inconsistent.</li>
      <li><strong>Credit or risk control:</strong> release requires commercial or finance review.</li>
      <li><strong>Delivery block:</strong> fulfillment is prevented until a condition is cleared.</li>
      <li><strong>Billing block:</strong> billing is prevented while delivery or order handling may continue.</li>
      <li><strong>Master data issue:</strong> customer, material, partner, plant, shipping, or pricing data does not support the transaction.</li>
      <li><strong>Custom rule:</strong> enhancement, workflow, interface, or compliance logic applies in this landscape.</li>
    </ul>

    <h2>Evidence to collect</h2>
    <p>A good diagnostic note should capture order number, item, block type, user-visible message, customer, material, sales area, requested delivery date, credit status if relevant, and the business reason the user expected the order to continue.</p>

    <h2>Support takeaway</h2>
    <p>Do not release blocks blindly. A block is often the only visible control protecting delivery, finance, compliance, or customer communication. Diagnose the control first, then decide whether to correct master data, change configuration, release the order, or escalate the business rule.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
      <li><a href="/services/sap-ams-consulting/">SAP AMS consulting</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
