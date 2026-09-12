---
layout: default
title: "Supplier Payments & AP — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA supplier cluster connecting supplier master data, invoice readiness, automatic payments, payment media, bank clearing, EBS, and payment recovery."
permalink: /labs/enterprise-context/procurement/suppliers/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-11
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-p2p
  - integration-recovery
  - delivery-ams
tags:
  - sap-s4hana
  - sap-mm
  - sap-fi-ap
  - suppliers
  - procure-to-pay
  - f110
  - automatic-payments
  - bank-clearing
  - electronic-bank-statement
  - troubleshooting
semantic_links:
  - type: "parent_topic"
    title: "Procurement"
    url: "/labs/enterprise-context/procurement/"
  - type: "integrates_with"
    title: "FI/CO for Logistics"
    url: "/labs/enterprise-context/finance-logistics/"
  - type: "related_topic"
    title: "Payments, Banks and Rejections"
    url: "/labs/enterprise-context/finance-logistics/payments-banks-rejections/"
  - type: "related_topic"
    title: "Business Partner"
    url: "/labs/enterprise-context/business-partner/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li aria-current="page">Suppliers</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Procure-to-Pay / supplier cluster</p>
      <h1>A supplier invoice is not finished<br />when it is posted.</h1>
      <p>The payable still needs a due date, a payment method, a bank route, a payment decision, a payment medium, bank execution, and final reconciliation. This cluster follows that chain from supplier readiness to recovery.</p>
      <a class="research-canvas__button" href="#cluster">Open the cluster <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Supplier payment model">
      <p>Lead model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Ready</strong><small>Can this supplier be paid correctly?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Pay</strong><small>What did SAP decide and post?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Prove</strong><small>What did the bank actually do?</small></div>
      <em>Supplier master, AP item, payment run, bank, and statement are one control chain.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>Lead rule:</strong> separate the purchasing event, the AP liability, the payment instruction, and the bank settlement. A green status in one layer does not prove the supplier was paid correctly.</p>
    <a href="/labs/enterprise-context/finance-logistics/">Connect to FI/CO <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="cluster" data-reveal>
    <header><p class="research-canvas__eyebrow">Cluster map</p><h2>Four deep-dives cover the supplier payment chain.</h2><p>Use the hub for the full story. Open a deep-dive when the interviewer or incident moves into one failure layer.</p></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/procurement/suppliers/readiness/"><span>01</span><strong>Supplier payment readiness</strong><small>Business Partner, company-code data, payment terms, bank data, payment method, invoice blocks, and supplier line items.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/procurement/suppliers/automatic-payments/"><span>02</span><strong>Automatic payments</strong><small>F110 / Manage Automatic Payments, proposal logic, bank determination, payment media, controls, and approval boundary.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="/labs/enterprise-context/procurement/suppliers/bank-clearing/"><span>03</span><strong>Bank clearing and EBS</strong><small>Payment media, bank execution, clearing accounts, F1680, F1520, bank statements, and reconciliation evidence.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="/labs/enterprise-context/procurement/suppliers/rejections-recovery/"><span>04</span><strong>Rejections and recovery</strong><small>Proposal exceptions, bank-file rejection, unmatched statement items, reversal, duplicate-payment risk, and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">End-to-end path</p><h2>Read the payable as a sequence of state changes.</h2><p>This sequence is more useful than memorising transaction codes.</p></header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>01</span><strong>Supplier</strong><h3>Payment-ready master data</h3><p>Supplier/BP data provides the company-code payment settings, bank details, reconciliation account, and terms that influence later processing.</p></article>
      <article class="ecg-memory-card"><span>02</span><strong>Invoice</strong><h3>Open AP item</h3><p>An invoice posted through FI or Logistics Invoice Verification creates a supplier liability. The item needs a valid due date and payment state.</p></article>
      <article class="ecg-memory-card"><span>03</span><strong>Proposal</strong><h3>Payment decision</h3><p>The payment program selects, groups, and checks open items. The proposal log explains why an item is included or rejected.</p></article>
      <article class="ecg-memory-card"><span>04</span><strong>Payment</strong><h3>Accounting execution</h3><p>The payment run posts the accounting result and normally clears the supplier open item against a bank-clearing position.</p></article>
      <article class="ecg-memory-card"><span>05</span><strong>Medium</strong><h3>Instruction to the bank</h3><p>SAP creates the payment medium using the configured format and payment data. This is the bank-facing instruction.</p></article>
      <article class="ecg-memory-card"><span>06</span><strong>Bank</strong><h3>External execution</h3><p>The bank accepts, rejects, partially processes, or executes the instruction. SAP status alone does not prove the bank outcome.</p></article>
      <article class="ecg-memory-card"><span>07</span><strong>Statement</strong><h3>Cash evidence</h3><p>Electronic or manual bank statement processing posts and clears the bank-side movement. Unmatched items require reprocessing.</p></article>
      <article class="ecg-memory-card"><span>08</span><strong>Recovery</strong><h3>Close the exception safely</h3><p>Before resending or reversing, confirm whether the bank executed the payment. The main operational risk is paying twice while trying to repair one failure.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Two truths</p><h2>Purchasing truth and cash truth meet in AP.</h2><p>A strong P2P answer connects operational completion to the liability and then to the bank.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Purchasing truth</h3><ul><li>Was the supplier selected correctly?</li><li>Was the PO or service entry valid?</li><li>Did goods or services arrive?</li><li>Did invoice verification complete?</li></ul></div>
      <div><h3>AP truth</h3><ul><li>Is the supplier item open and payable?</li><li>Are terms, block, method, and bank data correct?</li><li>Did the proposal include the item?</li><li>Did the payment run post and clear it?</li></ul></div>
      <div><h3>Bank truth</h3><ul><li>Was the payment medium technically valid?</li><li>Did the bank accept and execute it?</li><li>Did the bank statement clear the clearing position?</li><li>Is the final cash state reconciled?</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header><p class="research-canvas__eyebrow">Diagnostic runtime</p><h2>Find the first wrong state.</h2><p>Start from evidence and move one boundary at a time.</p></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Supplier and item</h3><p>Check supplier/BP payment data, invoice due date, payment block, payment method, currency, and bank information.</p><strong>Question: should this item be payable now?</strong></article>
      <article><span>2</span><h3>Proposal</h3><p>Check whether the item entered the proposal and read the proposal log before touching configuration.</p><strong>Question: why did SAP select or reject it?</strong></article>
      <article><span>3</span><h3>Payment posting</h3><p>Confirm the payment document, supplier clearing, bank-clearing account, and payment status.</p><strong>Question: what accounting state now exists?</strong></article>
      <article><span>4</span><h3>Payment medium</h3><p>Check format, file generation, references, bank account, and the exact payload or medium sent externally.</p><strong>Question: what instruction left SAP?</strong></article>
      <article><span>5</span><h3>Bank and statement</h3><p>Confirm acceptance or rejection and compare it with the imported bank statement or payment-status file.</p><strong>Question: what did the bank actually execute?</strong></article>
      <article><span>6</span><h3>Recovery decision</h3><p>Choose reprocess, correct master/configuration, reverse, or resend only after the external execution state is known.</p><strong>Question: how do we avoid a duplicate payment?</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Assessment practice</p><h2>Questions a Lead should answer without opening SPRO.</h2><p>Give the business flow first. Add transactions and configuration only when they explain a decision.</p></header>
    <div class="research-route-list">
      <a href="/labs/assessment/"><span>Q1</span><strong>A supplier invoice is overdue but F110 does not select it. What do you check first?</strong><small>Item state → supplier payment data → proposal parameters → proposal log → configuration.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="/labs/assessment/"><span>Q2</span><strong>The payment run posted, but the bank rejected the file. Is the supplier still open?</strong><small>Explain supplier clearing versus bank execution and the recovery decision.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="/labs/assessment/"><span>Q3</span><strong>The bank executed the payment, but the clearing account is still open. Where do you look?</strong><small>Bank statement import, matching rule, external transaction, reference, amount, and reprocessing.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="/labs/assessment/"><span>Q4</span><strong>Why can changing FBZP be the wrong first action?</strong><small>Because the defect may be master data, line-item state, run parameters, payment media, bank execution, or EBS matching.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
    <p><strong>Evidence boundary:</strong> the current SAP Help baseline confirms supplier line-item management, automatic payment processing, payment-medium handling, incoming payment-file processing, and bank-statement reprocessing. Classic transaction names and detailed configuration steps remain release- and deployment-dependent and must be checked in the target system.</p>
    <a href="/labs/assessment/factual-review/">Review before promotion <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Primary references</p><h2>Use current SAP Help for the baseline.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/86248754a0cd9d62e10000000a445394.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Supplier Line Items</strong><small>Supplier/AP line-item operations and payment-relevant changes.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/77ead353ca9f4408e10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>How the Payment Program Works</strong><small>Proposal, payment, and payment-medium processing baseline.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/PRODUCT_ID/3cb1182b4a184bdd93f8d62e3f1f0741/a1597b757dfd404283a050ab12585e5a.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Incoming Payment Files</strong><small>Bank statements, payment rejections, and incoming payment-file operations.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/PRODUCT_ID/3cb1182b4a184bdd93f8d62e3f1f0741/bc1fe656fe590950e10000000a44147b.html" target="_blank" rel="noopener"><span>SAP</span><strong>Reprocess Bank Statement Items</strong><small>Manual and rule-based recovery for items that did not post or clear automatically.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
