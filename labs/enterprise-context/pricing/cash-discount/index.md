---
layout: default
title: "SAP Cash Discount — Sales, Purchasing and FI"
description: "A short SAP S/4HANA guide to early-payment cash discount: SKTO/SKTV, payment terms, SD vs MM, FI clearing, configuration and checks."
permalink: /labs/enterprise-context/pricing/cash-discount/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-04
hide_global_cta: true
enterprise_context_graph: true
career_impact: mapped
career_skills:
  - sales-pricing
tags: [sap-s4hana, sap-sd, sap-mm, sap-fi, pricing, cash-discount, payment-terms, skto]
source_links:
  - title: "SAP Learning — Statistical Conditions and SKTO"
    url: "https://learning.sap.com/courses/configuring-pricing-in-sap-s-4hana-sales/using-statistical-condition-types_aaee0ff4-46d0-42e2-add2-2eee76272d17"
  - title: "SAP Learning — Payment Terms and Cash Discounts"
    url: "https://learning.sap.com/courses/customizing-core-settings-in-financial-accounting-in-sap-s4hana/configuring-payment-terms-and-cash-discounts"
  - title: "SAP Help — Cash Discount in Procurement"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/1870b6531de6b64ce10000000a174cb4.html"
  - title: "SAP Help — Cash Discount in SD"
    url: "https://help.sap.com/docs/SUPPORT_CONTENT/sd/3362915264.html?locale=en-US"
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/pricing/">Pricing</a></li><li aria-current="page">Cash discount</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero">
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Pricing / SD + MM + FI</p>
      <h1>Cash discount is earned by paying early.</h1>
      <p>A normal sales discount reduces the agreed item price. <strong>Cash discount (skonto)</strong> rewards payment before a deadline. It is defined by <strong>payment terms</strong> and ultimately settled in Finance, not by simply lowering the sales-order or purchase-order net value.</p>
    </div>
    <div class="research-canvas__signal" aria-label="Cash discount process">
      <p>Follow the ownership</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Order / PO</strong><small>Agree payment terms</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Invoice</strong><small>Create AR / AP item</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Payment</strong><small>Apply eligible discount</small></div>
      <em>Order pricing ≠ payment clearing</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="problem-and-context">
    <header>
      <p class="research-canvas__eyebrow">Problem and business context</p>
      <h2>Why does the invoice still show the full amount?</h2>
    </header>
    <p><strong>Common problem:</strong> a Sales or Purchasing pricing screen shows a potential 2% cash discount, but the invoice is still for €1,000. That is usually expected, not a pricing error: the discount must first be earned by early payment.</p>
    <p><strong>Business context:</strong> SD and MM agree the payment terms in the sales order or PO. FI uses the invoice terms, due-date rules and actual settlement to decide whether the discount applies. This distinction avoids double-counting a benefit in pricing and again in FI.</p>
  </section>

  <section class="research-canvas__boundary">
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <p><strong>Remember:</strong> <code>SKTO</code> in pricing normally shows a <em>potential</em> cash discount as a <strong>statistical</strong> condition. It does not itself reduce the order net value. The actual discount depends on the payment terms, baseline date, cash-discount base and settlement.</p>
    <a href="#example">See €1,000 example</a>
  </section>

  <section class="research-canvas__inventory" id="example">
    <header><p class="research-canvas__eyebrow">One example, two business directions</p><h2>2% within 10 days; otherwise 30 days net.</h2><p>Synthetic example: an invoice of €1,000 with no tax; gross FI posting method. The payment baseline date starts the clock.</p></header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Cash discount example in Sales and Purchasing">
      <table class="study-table__table">
        <thead><tr><th scope="col">When</th><th scope="col">Sales (we sell)</th><th scope="col">Purchasing (we buy)</th></tr></thead>
        <tbody>
          <tr><th scope="row">Order / PO</th><td>Customer is offered 2% for early payment.</td><td>Supplier offers us 2% for early payment.</td></tr>
          <tr><th scope="row">Invoice</th><td>Customer owes €1,000 (AR).</td><td>We owe supplier €1,000 (AP).</td></tr>
          <tr><th scope="row">Paid by day 10</th><td>Receive €980; €20 discount granted clears the balance.</td><td>Pay €980; €20 discount received clears the balance.</td></tr>
          <tr><th scope="row">Paid on day 20</th><td>Receive full €1,000.</td><td>Pay full €1,000.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Business consequence:</strong> Sales offers an incentive to collect cash sooner; Purchasing can save money by paying earlier. Finance should compare that benefit against the cost of cash.</p>
  </section>

  <section class="research-canvas__inventory" id="configuration">
    <header><p class="research-canvas__eyebrow">Configuration and data</p><h2>Where SAP gets the discount.</h2></header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Cash discount configuration and data references">
      <table class="study-table__table">
        <thead><tr><th scope="col">Layer</th><th scope="col">What to inspect</th></tr></thead>
        <tbody>
          <tr><th scope="row">FI payment terms</th><td><code>OBB8</code> (classic GUI): cash-discount % / days, net due date, baseline-date rule. Definition in <code>T052</code>.</td></tr>
          <tr><th scope="row">SD</th><td>Customer sales-area terms → sales document <code>VBKD-ZTERM</code> → billing / FI. In <code>V/06</code> and <code>V/08</code>, inspect <code>SKTV</code> (before tax) or <code>SKTO</code> (after the tax step), condition category <code>E</code> and <strong>statistical</strong> setting. The discount rate comes from payment terms, not a normal condition record.</td></tr>
          <tr><th scope="row">MM</th><td>Supplier purchasing data → PO header payment terms (<code>EKKO-ZTERM</code>) → supplier invoice (for example <code>MIRO</code>) → FI. Purchasing <code>SKTO</code> is also normally statistical; inspect the purchasing calculation schema and the <em>No Cash Discount</em> item indicator.</td></tr>
          <tr><th scope="row">FI clearing</th><td>Check the invoice's actual payment terms, baseline date, payment date, discount base and discount G/L account determination. <strong>Gross</strong> method recognizes discount at clearing; <strong>net</strong> method can recognize it already at invoice posting.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Tax nuance:</strong> <code>SKTV</code> and <code>SKTO</code> indicate different SD calculation paths; the actual eligible base can exclude or include tax according to FI/company-code settings. Do not assume that <code>SKTO</code> always means “2% of gross invoice including tax.”</p>
  </section>

  <section class="research-canvas__inventory" id="diagnose">
    <header><p class="research-canvas__eyebrow">Diagnostic path</p><h2>When the discount looks wrong, check four things.</h2></header>
    <ol>
      <li><strong>Terms:</strong> compare the order/PO and invoice payment terms with <code>T052</code>. Was the term changed during invoice creation?</li>
      <li><strong>Pricing:</strong> is <code>SKTO</code>/<code>SKTV</code> present and statistical? For SD, is the item eligible for cash discount? If you saw <code>ST00</code>, verify the exact condition key in your system; do not assume it is the standard cash-discount type.</li>
      <li><strong>Base:</strong> check tax inclusion/exclusion and excluded purchasing items before comparing amounts.</li>
      <li><strong>Settlement:</strong> compare baseline date with actual payment date and inspect the AR/AP clearing document. A displayed 2% is not proof that the customer or supplier earned it.</li>
    </ol>
    <p><strong>Extension decision:</strong> use standard payment terms first. Add released validation or reporting for missing terms, early-payment opportunities or discount leakage only when required. Do not implement a normal, non-statistical price reduction to imitate cash discount: that can double-count the benefit when FI also grants it. Available enhancement points differ between Public Cloud and Private/On-Premise.</p>
  </section>

  <section class="research-canvas__inventory">
    <header><p class="research-canvas__eyebrow">SAP references</p><h2>Verify the behavior in your release.</h2></header>
    <p>
      <a href="https://learning.sap.com/courses/configuring-pricing-in-sap-s-4hana-sales/using-statistical-condition-types_aaee0ff4-46d0-42e2-add2-2eee76272d17">SAP Learning: SKTO in Sales</a> ·
      <a href="https://learning.sap.com/courses/customizing-core-settings-in-financial-accounting-in-sap-s4hana/configuring-payment-terms-and-cash-discounts">SAP Learning: terms and FI clearing</a> ·
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/1870b6531de6b64ce10000000a174cb4.html">SAP Help: cash discount in Purchasing</a> ·
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/sd/3362915264.html?locale=en-US">SAP Help: SKTV/SKTO in SD</a>
    </p>
    <p>Classic transaction codes above are for supported GUI deployments; S/4HANA Cloud Public Edition uses released configuration activities and apps. Exact pricing procedures, accounts, tax rules and extension points are system-specific.</p>
    <p>Continue with <a href="/labs/enterprise-context/pricing/">Sales Pricing</a>, <a href="/labs/enterprise-context/procurement/">Procurement</a> or <a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a>.</p>
  </section>

  <div class="research-canvas__support">
    {% include atlas/disclaimer.html %}
  </div>
</div>
