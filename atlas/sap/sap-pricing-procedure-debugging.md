---

layout: default
title: "SAP Pricing Procedure Debugging"
description: "A practical way to trace SAP sales pricing from procedure determination to condition records, calculation, copying, and manual changes."
permalink: /atlas/sap/sap-pricing-procedure-debugging/
atlas_section: sap
domain: SAP operations
subdomain: Sales pricing
concept_type: support diagnostic
sap_area: "SD pricing"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Pricing Procedure Debugging</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP pricing procedure debugging</h1>
    <p class="note-subtitle">Pricing becomes much easier to debug when you stop asking “why is the price wrong?” and trace the exact condition that produced the result.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales pricing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until detailed SAP configuration claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Price is a result, not one setting</h2>
    <p>A sales document price is built from several decisions. The system selects a pricing procedure, processes its condition types in sequence, searches for condition records where required, applies formulas and exclusions, and may also keep copied or manually entered values.</p>
    <p>Because of this, “pricing is wrong” is too broad for support. Pick one condition and one document item. Then explain what you expected, what SAP calculated, and where the two paths separate.</p>

    <h2>Read the pricing result from the inside</h2>
    <div class="decision-table">
      <table>
        <thead><tr><th>Question</th><th>If the answer is wrong</th><th>Typical evidence</th></tr></thead>
        <tbody>
          <tr><td>Was the expected pricing procedure determined?</td><td>The problem is above the individual condition record.</td><td>Sales area, document pricing context, customer pricing context, selected procedure.</td></tr>
          <tr><td>Is the expected condition type in the procedure?</td><td>The condition may never be evaluated for this document.</td><td>Procedure step, requirement, statistical/manual settings, exclusion logic.</td></tr>
          <tr><td>Did the access find the expected record?</td><td>Check keys, validity, date, organizational data, customer/material data, and record maintenance.</td><td>Pricing analysis and access result.</td></tr>
          <tr><td>Was a value found but calculated differently?</td><td>The issue may be scale, unit, currency, formula, base value, rounding, or condition interaction.</td><td>Rate, base, value, calculation type, units, scales, formulas.</td></tr>
          <tr><td>Was the result copied or changed later?</td><td>The automatic determination may be correct while document history changes the final value.</td><td>Pricing type during copy, manual condition, change history, redetermination behaviour.</td></tr>
        </tbody>
      </table>
    </div>

    <h2>A practical investigation</h2>
    <ol>
      <li><strong>Choose one failing item.</strong> Capture document, item, customer, material, sales area, currency, quantity, pricing date, expected value, and actual value.</li>
      <li><strong>Open the pricing analysis.</strong> Do not start with condition maintenance. First see which procedure and condition path the document actually used.</li>
      <li><strong>Find the first unexpected condition.</strong> Is it missing, inactive, zero, duplicated, excluded, or simply calculated with a different base?</li>
      <li><strong>Follow the access result.</strong> If a record was not found, compare the access keys and validity with the business data in the document.</li>
      <li><strong>Check calculation context.</strong> Units, currency, scales, condition base values, formulas, taxes, and rounding can make a valid record produce an unexpected result.</li>
      <li><strong>Check document history.</strong> A quotation, contract, order, delivery, or billing document may copy pricing under rules that differ from a fresh determination.</li>
      <li><strong>Compare with a working case.</strong> A nearby working document often exposes the relevant difference faster than browsing configuration without a hypothesis.</li>
    </ol>

    <h2>Three mistakes that waste time</h2>
    <p><strong>Changing the condition record first.</strong> If the document did not try to read that record, maintaining it only creates another variable.</p>
    <p><strong>Treating every price difference as SD pricing.</strong> Tax, settlement, external pricing, POS replication, commerce platforms, and custom logic can change the business result outside the classic sales pricing path.</p>
    <p><strong>Ignoring the pricing date and copy logic.</strong> Two documents with the same customer and material can legitimately use different records because their dates or pricing types differ.</p>

    <h2>When the problem is reported from retail or POS</h2>
    <p>A store price mismatch should first be split into two questions: did SAP calculate the expected price, and did the downstream store or POS system receive and apply the same price? This avoids debugging an outbound replication delay as if it were a pricing-procedure defect.</p>
    <p>Useful evidence is the article or material, store, business date, expected and actual price, promotion context, the SAP pricing result, and the last successful price distribution to the affected location. The exact interface and store-assortment logic are landscape-specific.</p>

    <h2>What a strong pricing ticket contains</h2>
    <ul>
      <li>Document and item, expected price, actual price, and business impact.</li>
      <li>Pricing date, currency, quantity, customer, material, and sales area.</li>
      <li>The expected condition type and its actual status in pricing analysis.</li>
      <li>Access result or condition-record evidence when relevant.</li>
      <li>Any manual condition, copy/redetermination event, or recent pricing change.</li>
      <li>A working comparison document when available.</li>
    </ul>

    <h2>The useful end state</h2>
    <p>Do not close the analysis with “condition record fixed.” State the failed pricing step: for example, the wrong procedure was selected, the access keys did not match, the record was outside validity, a formula changed the base, or copied pricing was not redetermined. That explanation is reusable. A changed number is not.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
