---
layout: default
title: "Supplier Automatic Payments — F110 and F0770 Lead Lab"
description: "A practical SAP S/4HANA guide to supplier automatic payments: F110, Manage Automatic Payments, proposal logic, bank determination, payment media, controls, and diagnostics."
permalink: /labs/enterprise-context/procurement/suppliers/automatic-payments/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-11
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-p2p
  - delivery-ams
  - integration-recovery
tags:
  - sap-s4hana
  - fi-ap
  - f110
  - f0770
  - automatic-payment-program
  - fbzp
  - payment-medium
  - house-bank
  - supplier-payments
semantic_links:
  - type: "parent_topic"
    title: "Supplier Payments & AP"
    url: "/labs/enterprise-context/procurement/suppliers/"
  - type: "related_topic"
    title: "Supplier Payment Readiness"
    url: "/labs/enterprise-context/procurement/suppliers/readiness/"
  - type: "next_topic"
    title: "Bank Clearing and EBS"
    url: "/labs/enterprise-context/procurement/suppliers/bank-clearing/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li><a href="/labs/enterprise-context/procurement/suppliers/">Suppliers</a></li><li aria-current="page">Automatic Payments</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Supplier cluster / 02</p>
      <h1>F110 is a decision pipeline,<br />not a payment button.</h1>
      <p>The payment program selects open items, groups them, chooses payment and bank data, posts the payment result, and provides the data for payment media. A strong diagnosis identifies which decision failed.</p>
      <a class="research-canvas__button" href="#flow">Trace the run <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Automatic payment model">
      <p>Payment run</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Select</strong><small>Which items?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Decide</strong><small>How and from which bank?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Post</strong><small>What accounting state?</small></div>
      <em>Classic F110 and Fiori F0770 express the same business problem through different user experiences.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Lead rule:</strong> the proposal is your diagnostic surface. If you skip the proposal log and go directly to FBZP, you can change working configuration while the real problem sits in supplier master data, the line item, or run parameters.</p>
    <a href="#diagnostic">Open diagnostic path <span class="material-symbols-outlined" aria-hidden="true">route</span></a>
  </section>

  <section class="research-canvas__inventory" id="flow" data-reveal>
    <header><p class="research-canvas__eyebrow">Run model</p><h2>Six phases are enough to explain the APP clearly.</h2><p>Exact screens differ by deployment and release, but the business sequence remains stable.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>scope</small></div><h3>Parameters</h3><p class="ecg-question">What should this run consider?</p></header><div class="ecg-decision-columns"><div><h4>Typical inputs</h4><ul><li>Run date and identification</li><li>Posting date</li><li>Company codes</li><li>Payment methods</li><li>Selection range / free selections</li></ul></div><div><h4>Check</h4><p>Dates, company-code scope, and payment methods must match the payable items you expect.</p></div><div><h4>Failure signal</h4><p>The invoice never reaches the proposal even though the business expects it to be paid.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>selection</small></div><h3>Proposal</h3><p class="ecg-question">Which open items qualify?</p></header><div class="ecg-decision-columns"><div><h4>Program checks</h4><ul><li>Open-item status and due date</li><li>Payment block</li><li>Payment method</li><li>Supplier payment data</li><li>Bank/payment constraints</li></ul></div><div><h4>Evidence</h4><p>Proposal list, exceptions, and proposal log.</p></div><div><h4>Lead action</h4><p>Explain why each rejected item is rejected before changing data.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>group</small></div><h3>Grouping</h3><p class="ecg-question">Which items can become one payment?</p></header><div class="ecg-decision-columns"><div><h4>Principle</h4><p>Only compatible open items can be grouped into the same payment. Differences in payment-relevant fields can split payments.</p></div><div><h4>Why it matters</h4><p>A supplier can receive several payments even when users expected one.</p></div><div><h4>Diagnostic clue</h4><p>Compare method, currency, bank data, payment reference, and other grouping-relevant attributes.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>bank</small></div><h3>Payment method and bank determination</h3><p class="ecg-question">How will SAP pay and from which account?</p></header><div class="ecg-decision-columns"><div><h4>Controls</h4><ul><li>Payment-method configuration</li><li>House bank / account</li><li>Ranking and availability rules</li><li>Explicit bank data on supplier or item</li></ul></div><div><h4>Lead caution</h4><p>Explicit supplier or line-item settings can influence the result. Do not assume ranking is the only input.</p></div><div><h4>Evidence</h4><p>Proposal result plus the exact selected bank/payment data.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>05</span><small>posting</small></div><h3>Payment execution</h3><p class="ecg-question">What accounting state did SAP create?</p></header><div class="ecg-decision-columns"><div><h4>Typical result</h4><p>Supplier open items are cleared and a bank-clearing position is posted for the outgoing cash movement.</p></div><div><h4>Check</h4><ul><li>Payment document</li><li>Supplier clearing</li><li>Bank-clearing account</li><li>Payment status</li></ul></div><div><h4>Boundary</h4><p>Posting in SAP does not prove the external bank executed the transfer.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>06</span><small>medium</small></div><h3>Payment medium</h3><p class="ecg-question">What instruction is sent to the bank?</p></header><div class="ecg-decision-columns"><div><h4>Output</h4><p>Payment data is transformed into a configured medium such as XML or another bank format.</p></div><div><h4>Controls</h4><p>Payment Medium Workbench / DME format, variant, bank account, references, and country-specific requirements.</p></div><div><h4>Failure signal</h4><p>SAP payment posted successfully but the generated file is invalid or rejected externally.</p></div></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Configuration ladder</p><h2>Know what each configuration layer decides.</h2><p>FBZP is important, but “check FBZP” is not a Lead-level diagnosis.</p></header>
    <div class="ecg-input-grid">
      <article><span>CC</span><h3>Company-code participation</h3><p>Controls which company codes participate and which paying company code is used in classic automatic-payment configuration.</p><p><strong>Question:</strong> who owns the payment obligation?</p></article>
      <article><span>METHOD</span><h3>Payment method</h3><p>Country and company-code settings define where and how a method can be used and what data is required.</p><p><strong>Question:</strong> is this method valid for the supplier, currency, and country?</p></article>
      <article><span>BANK</span><h3>Bank determination</h3><p>Controls bank/account selection logic, including priority and available-amount rules in classic scenarios.</p><p><strong>Question:</strong> why did SAP choose this bank?</p></article>
      <article><span>PMW</span><h3>Payment medium</h3><p>The payment format maps SAP payment data into the structure expected by the bank.</p><p><strong>Question:</strong> what exact format/version did we generate?</p></article>
      <article><span>BP</span><h3>Supplier and item overrides</h3><p>Master and line-item data can influence payment method, bank details, and selection.</p><p><strong>Question:</strong> is the outcome driven by configuration or by explicit business data?</p></article>
      <article><span>RUN</span><h3>Run parameters</h3><p>Every payment run adds its own scope, dates, payment methods, and free selections.</p><p><strong>Question:</strong> would the same invoice be selected in a correctly scoped test run?</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Classic and Fiori</p><h2>Use transaction codes as references, not as the architecture.</h2></header>
    <div class="ecg-decision-columns">
      <div><h3>Classic references</h3><ul><li>F110 — Automatic Payment Program</li><li>FBZP — payment-program configuration</li><li>FI12 / related bank maintenance — house-bank context</li><li>FBPM — classic payment-medium processing in relevant landscapes</li><li>FBL1N — supplier/vendor line-item analysis</li></ul></div>
      <div><h3>Current Fiori references</h3><ul><li>Manage Automatic Payments (F0770)</li><li>Manage Supplier Line Items (F0712)</li><li>Manage Payment Media (F1868)</li><li>Bank and payment apps depend on deployment and scope.</li></ul></div>
      <div><h3>Lead answer</h3><ul><li>Describe the state change first.</li><li>Name the app/transaction second.</li><li>State when the exact configuration differs by release or deployment.</li><li>Do not present one on-premise customizing path as universal S/4HANA behavior.</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Approvals and controls</p><h2>Approval belongs before irreversible execution.</h2><p>Payment proposals and payment items can be subject to approval depending on the implemented process and deployment. The control objective is more important than memorising one workflow template.</p></header>
    <div class="ecg-control-stack">
      <article><span>CTRL</span><h3>Separation of duties</h3><p>The person who prepares payment data should not automatically be the person who releases high-risk payments.</p><strong>Design owner and fallback approver explicitly.</strong></article>
      <article><span>AMOUNT</span><h3>Risk-based approval</h3><p>Use amount, supplier risk, payment method, company code, or other business criteria to route approvals where the platform supports it.</p><strong>Do not make every payment follow the same heavy path.</strong></article>
      <article><span>PROOF</span><h3>Approval evidence</h3><p>Store who approved what, when, and under which conditions. The evidence is part of the payment control, not an optional audit extra.</p><strong>Production support needs this history too.</strong></article>
      <article><span>BOUNDARY</span><h3>Release-specific workflow</h3><p>Classic workflow objects, BAdIs, and configuration transactions differ from current flexible-workflow options. Verify the target release before implementing.</p><strong>Architecture before template ID.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header><p class="research-canvas__eyebrow">Diagnostic runtime</p><h2>Five checks for “F110 did not pay it”.</h2></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Item eligibility</h3><p>Open? Due? Not blocked? Correct special G/L type? Correct payment method?</p><strong>Prove the item should be eligible.</strong></article>
      <article><span>2</span><h3>Run scope</h3><p>Company code, dates, method, and free selections include the item?</p><strong>Prove the run looked at it.</strong></article>
      <article><span>3</span><h3>Proposal log</h3><p>Read the exact rejection or selection message and compare with payment-relevant master/item data.</p><strong>Use evidence, not guesswork.</strong></article>
      <article><span>4</span><h3>Bank/payment route</h3><p>Confirm method, bank details, house-bank selection, and account/format constraints.</p><strong>Find the first invalid decision.</strong></article>
      <article><span>5</span><h3>Payment medium</h3><p>If accounting posted, stop debugging item selection and move to payment-medium or bank-execution evidence.</p><strong>Do not diagnose the wrong phase.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">60-second answer</p><h2>“How does the Automatic Payment Program work?”</h2></header>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span><p>The payment program starts with run parameters and open supplier items. It creates a proposal, where SAP checks due date, blocks, payment method, bank data, and other rules. After review or approval, the payment run posts the accounting result and normally clears the supplier item against a bank-clearing account. Then SAP creates the payment medium for the bank. I treat proposal selection, payment posting, file generation, and bank execution as separate states because each has different evidence and recovery.</p><a href="/labs/assessment/">Practice more <span class="material-symbols-outlined" aria-hidden="true">school</span></a></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Primary references</p><h2>Current SAP Help baseline.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/77ead353ca9f4408e10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>How the Payment Program Works</strong><small>Proposal, payment, and data-carrier/payment-medium process.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/accounts-payable-j60-co/release-payment-proposal" target="_blank" rel="noopener"><span>SAP</span><strong>Release Payment Proposal</strong><small>Current Fiori payment-proposal flow using Manage Automatic Payments.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/d93424d8ff23402f80ac55a4cad80270/50c95445101444eb8cc6e95ffdb82dd5.html" target="_blank" rel="noopener"><span>SAP</span><strong>DME / Payment Medium Customizing</strong><small>Payment Medium Workbench and DME-format configuration baseline.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/039683576ea1a96be10000000a4450e5.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Payment Media</strong><small>Payment-medium status, download, and payment-summary operations.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
