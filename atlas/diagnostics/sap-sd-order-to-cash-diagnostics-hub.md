---
layout: default
title: "SAP SD Order-to-Cash Diagnostics Hub"
description: "A review-candidate hub mapping order-to-cash blockers to SAP SD diagnostics, from sales order to billing."
permalink: /atlas/diagnostics/sap-sd-order-to-cash-diagnostics-hub/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Order to cash
concept_type: diagnostic guide
sap_area: "Sales and Distribution / OTC"
business_process: "Order to cash"
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - o2c
  - sd
related:
  - /atlas/maps/order-to-cash-map/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-delivery-block-analysis/
  - /atlas/diagnostics/sap-billing-block-analysis/
  - /atlas/sap/sap-pricing-procedure-debugging/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/maps/order-to-cash-map/
**Practical implication:** Work forward from the sales order through delivery and billing; a blocker early in the chain is often the root cause of later symptoms.
**Tags:** sap-ams, o2c, sd

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP SD Order-to-Cash Diagnostics Hub</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic Hub</p>
    <h1>SAP SD Order-to-Cash Diagnostics Hub</h1>
    <p class="note-subtitle">A first-pass map for order-to-cash blockers: sales order, delivery, billing, pricing, credit, and account determination.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales and Distribution / OTC</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Order-to-cash incidents tend to cluster around blocks and configuration at four points: the sales order cannot be completed, the delivery cannot be created, the billing cannot be generated, or the price/account is wrong. This hub routes the symptom to the right first check and discourages fixing downstream symptoms before the upstream blocker is understood.</p>

    <h2>Symptom-to-check matrix</h2>
    <table>
      <thead>
        <tr><th>Symptom</th><th>First area to check</th><th>Typical SAP touchpoints</th></tr>
      </thead>
      <tbody>
        <tr><td>Sales order is blocked or incomplete</td><td>Incompletion, credit, delivery, or billing block</td><td>VA02, VBAP/VBAK blocks, incompletion log, credit exposure</td></tr>
        <tr><td>Delivery cannot be created</td><td>Delivery block, route, or ATP</td><td>VL01N, delivery block, schedule line, availability check</td></tr>
        <tr><td>Billing cannot be generated</td><td>Billing block or billing relevance</td><td>VF01, billing block, item category, billing relevance</td></tr>
        <tr><td>Price is wrong or missing</td><td>Pricing procedure and condition records</td><td>VK11/VK12, pricing procedure, condition type</td></tr>
        <tr><td>Account determination is wrong</td><td>Account determination procedure</td><td>VKOA, account key, chart of accounts</td></tr>
        <tr><td>One order produces multiple invoices</td><td>Invoice split criteria</td><td>Billing document header, split criteria, VBRK/VBRP</td></tr>
        <tr><td>Partner or address is missing</td><td>Partner determination</td><td>Partner procedure, customer master, sales area</td></tr>
        <tr><td>Return cannot be credited or received</td><td>Returns process and reference</td><td>VA01 return, delivery, credit memo</td></tr>
      </tbody>
    </table>

    <h2>Evidence to collect</h2>
    <ul>
      <li>Sales order, delivery, and billing document numbers.</li>
      <li>Sales area, item category, and schedule line category.</li>
      <li>Block reasons and incompletion logs.</li>
      <li>Pricing procedure and condition type values.</li>
      <li>Credit account and exposure when credit is involved.</li>
      <li>Account determination key and G/L account result.</li>
    </ul>

    <h2>Related diagnostics</h2>
    <div class="atlas-card-grid">
      <a class="atlas-card" href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">
        <h2>Sales Order Block Diagnosis</h2>
        <p>Split between incompletion, credit, delivery, billing, and master-data blockers.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-delivery-block-analysis/">
        <h2>Delivery Block Analysis</h2>
        <p>Why a sales order cannot create a delivery.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-billing-block-analysis/">
        <h2>Billing Block Analysis</h2>
        <p>Why a sales document cannot be billed.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">
        <h2>Incompletion Procedure</h2>
        <p>Why a sales document is incomplete.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-credit-management-diagnostics/">
        <h2>Credit Management</h2>
        <p>Separating credit blocks from other causes.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/sap/sap-pricing-procedure-debugging/">
        <h2>Pricing Procedure Debugging</h2>
        <p>Why a price or condition is wrong.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-invoice-split-analysis/">
        <h2>Invoice Split Analysis</h2>
        <p>Why billing creates multiple invoices.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-returns-processing-diagnostics/">
        <h2>Returns Processing</h2>
        <p>Return cannot be created, received, or credited.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
    </div>

    <h2>Related maps and concepts</h2>
    <ul>
      <li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a> — verified process map.</li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash Concept</a> — if exists.</li>
    </ul>

    <h2>Boundaries and escalation</h2>
    <p>This hub is a triage guide. Changes to pricing procedures, account determination, billing relevance, or partner determination require functional review and change control. Escalate when the issue affects revenue recognition, legal reporting, or requires mass correction.</p>

    <h2>Safe automation opportunity</h2>
    <p>A support agent can summarize sales order blocks, delivery blocks, billing blocks, and recent pricing conditions to reduce initial triage time. It should not propose customizing changes or update documents.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
