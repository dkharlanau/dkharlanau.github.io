---
layout: default
title: "SAP Procurement Diagnostics Hub"
description: "A review-candidate hub mapping procure-to-pay symptoms to SAP MM checks, evidence, and related diagnostics."
permalink: /atlas/diagnostics/sap-procurement-diagnostics-hub/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procure to pay
concept_type: diagnostic guide
sap_area: "Materials Management / Procurement"
business_process: "Procure to pay"
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - p2p
  - procurement
related:
  - /atlas/maps/procure-to-pay-map/
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-release-strategy-diagnostics/
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/diagnostics/sap-three-way-match-diagnostics/
  - /atlas/diagnostics/sap-contract-scheduling-agreement-diagnostics/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/maps/procure-to-pay-map/
**Practical implication:** Use the symptom matrix to decide whether a procurement blocker is master data, release strategy, price/quantity, or integration before collecting deeper evidence.
**Tags:** sap-ams, p2p, procurement

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Procurement Diagnostics Hub</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic Hub</p>
    <h1>SAP Procurement Diagnostics Hub</h1>
    <p class="note-subtitle">A first-pass map for procure-to-pay blockers, from requisition and sourcing to goods receipt and invoice verification.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>Materials Management / Procurement</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Procurement incidents repeat across a small set of themes: a document cannot be created, an approval is stuck, master data is missing or inconsistent, price or quantity does not match, or the follow-on integration fails. This hub provides a symptom-to-area matrix so the first responder can narrow the search before opening the wrong transaction.</p>

    <h2>Symptom-to-check matrix</h2>
    <table>
      <thead>
        <tr><th>Symptom</th><th>First area to check</th><th>Typical SAP touchpoints</th></tr>
      </thead>
      <tbody>
        <tr><td>Purchase requisition cannot be created or converted</td><td>Master data and account assignment</td><td>ME51N, ME54N, ME21N, material/vendor/org data</td></tr>
        <tr><td>Purchase order is blocked or cannot be released</td><td>Release strategy and approval workflow</td><td>ME22N, ME54N/ME55, release strategy traces</td></tr>
        <tr><td>Supplier cannot be determined</td><td>Source determination and info records</td><td>ME01, ME11, source list, quota arrangement</td></tr>
        <tr><td>Price or account assignment does not match</td><td>Conditions and account assignment category</td><td>ME23N, pricing conditions, account assignment tab</td></tr>
        <tr><td>Goods receipt posts wrong stock or value</td><td>Movement type and valuation</td><td>MIGO, MB51, material document, GR/IR clearing</td></tr>
        <tr><td>Invoice is blocked or mismatched</td><td>Three-way match and tolerance</td><td>MIRO, MRBR, GR/IR account, tolerance keys</td></tr>
        <tr><td>Consignment or subcontracting stock is wrong</td><td>Special procurement and liability</td><td>MB51, consignment info records, subcontracting PO</td></tr>
        <tr><td>Output was not sent to supplier</td><td>Message determination and spool</td><td>NACE, SOST, spool request, condition records</td></tr>
      </tbody>
    </table>

    <h2>Evidence to collect</h2>
    <ul>
      <li>Document number and item: requisition, purchase order, goods receipt, or invoice.</li>
      <li>Purchasing organization, plant, and vendor (use generic identifiers only).</li>
      <li>Current document status and status history.</li>
      <li>Release strategy code and approval log when approval is involved.</li>
      <li>Material and info record references (without real customer/vendor names).</li>
      <li>IDoc or output status if supplier integration is part of the symptom.</li>
    </ul>

    <h2>Related diagnostics</h2>
    <div class="atlas-card-grid">
      <a class="atlas-card" href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">
        <h2>Purchase Order Creation</h2>
        <p>PO cannot be created, saved, or released.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-contract-scheduling-agreement-diagnostics/">
        <h2>Contract and Scheduling Agreement</h2>
        <p>Release orders or delivery schedules against outline agreements fail.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-release-strategy-diagnostics/">
        <h2>Release Strategy</h2>
        <p>PO or requisition is blocked by approval workflow.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-source-determination-diagnostics/">
        <h2>Source Determination</h2>
        <p>No valid supplier is determined.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-purchasing-info-record-diagnostics/">
        <h2>Purchasing Info Record</h2>
        <p>Supplier, material, or price relationship is missing.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-account-assignment-diagnostics/">
        <h2>Account Assignment</h2>
        <p>Document posts to the wrong cost object.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">
        <h2>Invoice Verification</h2>
        <p>Invoice is blocked by price, quantity, or reference mismatch.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-three-way-match-diagnostics/">
        <h2>Three-Way Match</h2>
        <p>PO, goods receipt, and invoice do not align.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">
        <h2>Goods Receipt</h2>
        <p>Physical receipt, stock, and invoice matching diverge.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
    </div>

    <h2>Related maps and concepts</h2>
    <ul>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure-to-Pay Map</a> — verified process map.</li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a> — review candidate.</li>
    </ul>

    <h2>Boundaries and escalation</h2>
    <p>This hub is a triage guide, not a customizing playbook. Changes to release strategies, pricing procedures, message determination, or account assignment categories need functional review and change control. Escalate when the issue crosses multiple modules, affects period-end closing, or requires custom development.</p>

    <h2>Safe automation opportunity</h2>
    <p>A support agent can summarize document status, release strategy, recent goods-receipt history, and open invoice blocks from the purchase order header to reduce the time spent on status collection. The agent should not change documents or propose customizing changes.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
