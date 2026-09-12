---
layout: default
title: "Supplier Payment Readiness — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA supplier-payment readiness guide covering Business Partner data, company-code settings, payment terms, bank data, blocks, invoice readiness, and supplier line-item diagnostics."
permalink: /labs/enterprise-context/procurement/suppliers/readiness/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-11
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-master-data
tags:
  - sap-s4hana
  - supplier-master
  - business-partner
  - accounts-payable
  - payment-terms
  - payment-block
  - supplier-bank-data
  - procure-to-pay
semantic_links:
  - type: "parent_topic"
    title: "Supplier Payments & AP"
    url: "/labs/enterprise-context/procurement/suppliers/"
  - type: "related_topic"
    title: "Business Partner"
    url: "/labs/enterprise-context/business-partner/"
  - type: "related_topic"
    title: "Master Data"
    url: "/labs/enterprise-context/master-data/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li><a href="/labs/enterprise-context/procurement/suppliers/">Suppliers</a></li><li aria-current="page">Readiness</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Supplier cluster / 01</p>
      <h1>Payment problems often start<br />before the payment run.</h1>
      <p>If the supplier, invoice, payment terms, bank data, or block state is wrong, F110 is only where the defect becomes visible. Supplier payment readiness is the control layer before automatic payment processing.</p>
      <a class="research-canvas__button" href="#readiness-map">Check payment readiness <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Supplier readiness model">
      <p>Readiness test</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Who</strong><small>Correct supplier/BP?</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>When</strong><small>Correct due date?</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>How</strong><small>Correct payment route?</small></div>
      <em>A payment run cannot repair a bad payable.</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="readiness-map" data-reveal>
    <header><p class="research-canvas__eyebrow">Readiness map</p><h2>Seven fields can decide whether an invoice moves.</h2><p>Start with the business meaning. Then check where the value came from.</p></header>
    <div class="ecg-input-grid">
      <article><span>BP</span><h3>Supplier identity</h3><p>In S/4HANA, supplier processing is based on Business Partner master data. Purchasing and company-code views serve different parts of P2P.</p><p><strong>Ask:</strong> is this the correct supplier role and company code?</p></article>
      <article><span>RECON</span><h3>Reconciliation account</h3><p>The supplier subledger posts automatically to the assigned reconciliation account. It connects AP detail to the G/L.</p><p><strong>Ask:</strong> is the liability reaching the intended AP reconciliation account?</p></article>
      <article><span>TERM</span><h3>Payment terms</h3><p>Payment terms determine baseline date, cash-discount periods, and net due date. A wrong term changes when the item becomes payable.</p><p><strong>Ask:</strong> which term was defaulted, and was it overridden on the invoice?</p></article>
      <article><span>METHOD</span><h3>Payment method</h3><p>The supplier or line item can carry a payment method that must be compatible with the company code, country, currency, and payment run.</p><p><strong>Ask:</strong> is the method allowed and complete for this supplier?</p></article>
      <article><span>BANK</span><h3>Bank data</h3><p>Bank account and bank master data may be required for electronic payments. Missing or inconsistent bank details often stop the proposal.</p><p><strong>Ask:</strong> which bank account will be used, and is it valid?</p></article>
      <article><span>BLOCK</span><h3>Payment block</h3><p>A supplier item can be posted correctly but intentionally blocked from payment. Blocks can come from invoice verification, workflow, or manual action.</p><p><strong>Ask:</strong> is the block a defect or a control that still has a reason?</p></article>
      <article><span>ITEM</span><h3>Line-item state</h3><p>Due date, amount, currency, special G/L indicator, house bank, and other payment-relevant fields can change the selection result.</p><p><strong>Ask:</strong> what exactly does the payable item say now?</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>S/4HANA rule:</strong> use “supplier” and Business Partner as the main model. Classic transactions and tables may still use “vendor” wording, so a Lead should understand both vocabularies without mixing the data ownership.</p>
    <a href="/labs/enterprise-context/business-partner/">Open Business Partner <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Invoice entry</p><h2>Different entry paths can create the same AP question.</h2><p>The payment team should know how the liability was created, because the upstream owner can be different.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Logistics invoice</h3><ul><li>Invoice verification is linked to purchasing and receipt context.</li><li>Typical questions include PO reference, GR-based invoice verification, quantity and price variance, and invoice block.</li><li>Classic reference: MIRO.</li></ul></div>
      <div><h3>Direct FI supplier invoice</h3><ul><li>The liability can be posted without a PO-based logistics chain.</li><li>Payment terms, tax, account assignment, and payment data are central.</li><li>Classic references include FB60 / F-43 depending on process.</li></ul></div>
      <div><h3>Lead boundary</h3><ul><li>Do not treat every payment block as an FI problem.</li><li>If Logistics Invoice Verification created the block, find the purchasing/invoice-verification cause first.</li><li>AP owns the payment result, not every upstream cause.</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Operational view</p><h2>Read the supplier line item before you change configuration.</h2><p>Current S/4HANA provides Manage Supplier Line Items (F0712) as a central AP worklist. Classic systems often use FBL1N for the same diagnostic idea.</p></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Open or cleared?</h3><p>Confirm whether the invoice is still open. If it was already cleared, the question is no longer “why was it not selected?”</p><strong>State first, transaction second.</strong></article>
      <article><span>2</span><h3>Due when?</h3><p>Check baseline date, payment terms, cash-discount date, and net due date. The payment program uses the payable state, not the human expectation.</p><strong>Explain the date calculation.</strong></article>
      <article><span>3</span><h3>Blocked?</h3><p>Check payment blocks and why they exist. Removing a valid block can bypass an approval or invoice-verification control.</p><strong>Do not “fix” governance.</strong></article>
      <article><span>4</span><h3>How should it pay?</h3><p>Check payment method, bank details, currency, and any explicit house-bank data on the item.</p><strong>Line-item overrides matter.</strong></article>
      <article><span>5</span><h3>Special item?</h3><p>Down payments, payment requests, and other special G/L scenarios can follow different payment and clearing logic.</p><strong>Name the item type before applying a normal-invoice rule.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="failures" data-reveal>
    <header><p class="research-canvas__eyebrow">Failure patterns</p><h2>Recognize the pattern before touching FBZP.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/procurement/suppliers/automatic-payments/"><span>A</span><strong>Invoice is due, but proposal does not select it</strong><small>Check item status, block, method, supplier payment data, run parameters, and proposal log.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#readiness-map"><span>B</span><strong>Supplier bank data is missing or wrong</strong><small>Confirm whether bank data is mandatory for the chosen method and which BP bank account should be used.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#readiness-map"><span>C</span><strong>Invoice is not yet due</strong><small>Trace payment terms and baseline date. Do not change payment-run dates to hide a wrong invoice term.</small><i class="material-symbols-outlined" aria-hidden="true">event</i></a>
      <a href="#readiness-map"><span>D</span><strong>Payment block exists</strong><small>Find the owner and reason. For PO invoices, check whether invoice verification or approval created the block.</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="#readiness-map"><span>E</span><strong>Wrong house bank selected later</strong><small>Check explicit supplier/item bank data before assuming bank-determination customizing is wrong.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance_wallet</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">60-second answer</p><h2>“What must be correct before a supplier can be paid automatically?”</h2></header>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span><p>I start with the supplier and the AP item. The supplier needs valid company-code payment data, terms, and the required bank details. The invoice must be open, due, not blocked, and compatible with the payment method and currency. Then I check the payment-run parameters and proposal log. If the item never becomes payment-ready, changing bank determination or the payment format is too late in the process.</p><a href="/labs/assessment/">Practice more <span class="material-symbols-outlined" aria-hidden="true">school</span></a></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Fill the gaps</p><h2>Complete the explanation before opening the answer.</h2></header>
    <div class="ecg-input-grid">
      <article><span>01</span><h3>Terms of payment decide …</h3><p><strong>Answer:</strong> baseline date, discount periods, and net due date for the payable.</p></article>
      <article><span>02</span><h3>A reconciliation account connects …</h3><p><strong>Answer:</strong> supplier subledger postings with the General Ledger.</p></article>
      <article><span>03</span><h3>A payment block should be removed only after …</h3><p><strong>Answer:</strong> the business/control reason for the block is understood and resolved.</p></article>
      <article><span>04</span><h3>The best first screen for a payment-selection issue is …</h3><p><strong>Answer:</strong> the supplier/AP line item and then the payment proposal log, not customizing.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Primary references</p><h2>Current SAP Help baseline.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/86248754a0cd9d62e10000000a445394.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Supplier Line Items</strong><small>Open items, payment blocks, payment data changes, and manual payment actions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/a34bd953189a424de10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Terms of Payment (Accounts Payable)</strong><small>Baseline date, cash-discount periods, and due-date logic.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-best-practices/create-supplier-master-bne-56ccaf9fbaf5bc19a4cd462421191488/mandatory-and-optional-master-data" target="_blank" rel="noopener"><span>SAP</span><strong>Mandatory and Optional Supplier Master Data</strong><small>Bank master and reconciliation-account context in supplier/BP data.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
