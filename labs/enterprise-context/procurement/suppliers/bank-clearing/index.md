---
layout: default
title: "Supplier Bank Clearing & EBS — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA guide to supplier-payment bank clearing, payment media, bank execution, electronic bank statements, F1680, F1520, and reconciliation."
permalink: /labs/enterprise-context/procurement/suppliers/bank-clearing/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-11
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-observability
  - integration-recovery
  - delivery-ams
tags:
  - sap-s4hana
  - fi-ap
  - bank-clearing
  - electronic-bank-statement
  - f1680
  - f1520
  - camt053
  - camt054
  - payment-media
  - reconciliation
semantic_links:
  - type: "parent_topic"
    title: "Supplier Payments & AP"
    url: "/labs/enterprise-context/procurement/suppliers/"
  - type: "previous_topic"
    title: "Supplier Automatic Payments"
    url: "/labs/enterprise-context/procurement/suppliers/automatic-payments/"
  - type: "next_topic"
    title: "Supplier Rejections and Recovery"
    url: "/labs/enterprise-context/procurement/suppliers/rejections-recovery/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li><a href="/labs/enterprise-context/procurement/suppliers/">Suppliers</a></li><li aria-current="page">Bank Clearing</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Supplier cluster / 03</p>
      <h1>The payment run can be complete<br />while cash reconciliation is not.</h1>
      <p>Supplier clearing and bank clearing are different completion points. The payment run can clear the supplier item, while the bank-clearing account stays open until bank execution is represented and matched in SAP.</p>
      <a class="research-canvas__button" href="#accounting">Trace supplier to cash <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Bank clearing model">
      <p>Three states</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>AP</strong><small>Supplier cleared?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Bank</strong><small>Instruction executed?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Cash</strong><small>Clearing reconciled?</small></div>
      <em>Do not use one status to prove all three.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <p><strong>Important correction:</strong> in the standard AP pattern, the supplier invoice is normally cleared by the payment run itself. The later bank statement usually clears the bank-clearing position against the main bank account. A bank acknowledgement is therefore not the same thing as supplier clearing.</p>
    <a href="#accounting">See the posting chain <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
  </section>

  <section class="research-canvas__inventory" id="accounting" data-reveal>
    <header><p class="research-canvas__eyebrow">Accounting chain</p><h2>Two postings explain the standard clearing model.</h2><p>Exact accounts and posting rules vary, but the control logic is stable.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Payment run</h3><p><strong>Typical reading:</strong> Debit supplier / Credit outgoing bank-clearing account.</p><ul><li>The supplier liability is cleared.</li><li>A temporary bank-side open position remains.</li><li>SAP has created the accounting result for the payment instruction.</li></ul></div>
      <div><h3>Bank statement</h3><p><strong>Typical reading:</strong> Debit outgoing bank-clearing account / Credit main bank account.</p><ul><li>The external cash movement is represented.</li><li>The clearing position is matched and closed.</li><li>The main bank balance changes according to the statement.</li></ul></div>
      <div><h3>Reconciliation result</h3><ul><li>Supplier item cleared.</li><li>Bank-clearing position cleared.</li><li>Main bank account reflects external cash.</li><li>Payment reference and statement evidence connect the chain.</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Payment medium</p><h2>The file is the bank-facing contract.</h2><p>Once payment accounting is posted, the next question is what data SAP generated for the bank.</p></header>
    <div class="ecg-input-grid">
      <article><span>FORMAT</span><h3>Format</h3><p>XML, flat file, cheque data, or another medium is generated according to the configured Payment Medium Workbench / DME format and local bank requirements.</p><p><strong>Ask:</strong> which exact format and version was produced?</p></article>
      <article><span>PAYLOAD</span><h3>Payment data</h3><p>Supplier account, amount, currency, bank account, remittance/reference information, and execution data must be consistent with the bank contract.</p><p><strong>Ask:</strong> can we trace the rejected field back to SAP data?</p></article>
      <article><span>REF</span><h3>Reference</h3><p>A stable payment reference is critical for bank matching, support, and duplicate-payment control.</p><p><strong>Ask:</strong> which identifier connects the payment run, file, bank status, and statement?</p></article>
      <article><span>MEDIA</span><h3>Operational view</h3><p>Manage Payment Media provides a current Fiori view for payment-media status and download. Classic landscapes can use other PMW transactions and file flows.</p><p><strong>Ask:</strong> what exactly left SAP?</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Bank communication</p><h2>Transport success is not business success.</h2><p>An integration layer can deliver a file successfully while the bank rejects the business content.</p></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>SAP creates payment data</h3><p>The payment run and payment-medium process create the accounting and bank instruction.</p><strong>Evidence: run, payment document, medium, reference.</strong></article>
      <article><span>2</span><h3>Integration sends it</h3><p>File transfer, API, SAP Multi-Bank Connectivity, middleware, or another channel moves the instruction externally.</p><strong>Evidence: transmission ID and delivery status.</strong></article>
      <article><span>3</span><h3>Bank validates it</h3><p>The bank can accept, reject, partially accept, or execute individual payments depending on the service and format.</p><strong>Evidence: bank response/status file.</strong></article>
      <article><span>4</span><h3>Bank statement returns cash truth</h3><p>Electronic bank statement processing represents the actual cash movement and attempts automatic posting and clearing.</p><strong>Evidence: bank statement and posting result.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ebs" data-reveal>
    <header><p class="research-canvas__eyebrow">Electronic Bank Statement</p><h2>EBS is a rule engine for cash posting and clearing.</h2><p>Incoming bank statement data is interpreted through transaction types, posting rules, account symbols, references, and matching logic.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>import</small></div><h3>Receive the bank file</h3><p class="ecg-question">Did SAP import the statement or payment-status file successfully?</p></header><div class="ecg-decision-columns"><div><h4>Current app</h4><p>Manage Incoming Payment Files (F1680) can import bank statements, payment rejections, intraday statements, and other supported payment files.</p></div><div><h4>Classic reference</h4><p>FF_5 is a common classic EBS import transaction.</p></div><div><h4>Failure signal</h4><p>File rejected at import level before statement items can be processed.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>interpret</small></div><h3>Map external transaction</h3><p class="ecg-question">Which posting rule should this bank transaction use?</p></header><div class="ecg-decision-columns"><div><h4>Inputs</h4><p>External transaction code, transaction type, account symbol, posting rule, and bank account.</p></div><div><h4>Output</h4><p>Posting proposal for the cash/bank-clearing movement.</p></div><div><h4>Failure signal</h4><p>Unknown transaction code or missing posting rule.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>match</small></div><h3>Find the clearing target</h3><p class="ecg-question">Can SAP match the bank movement to the expected bank-clearing item?</p></header><div class="ecg-decision-columns"><div><h4>Evidence</h4><p>Payment reference, amount, currency, value date, bank account, and other matching fields.</p></div><div><h4>Success</h4><p>Automatic posting and clearing close the bank-clearing position.</p></div><div><h4>Failure signal</h4><p>Statement item posts incompletely or remains unmatched.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>recover</small></div><h3>Reprocess the exception</h3><p class="ecg-question">Is the problem data, rule, or one-off business context?</p></header><div class="ecg-decision-columns"><div><h4>Current app</h4><p>Reprocess Bank Statement Items (F1520) supports manual and rule-based reprocessing.</p></div><div><h4>Classic references</h4><p>FEBA / FEBAN are common classic post-processing references.</p></div><div><h4>Lead rule</h4><p>Fix the reusable rule only when the same pattern should work automatically next time.</p></div></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Formats</p><h2>Do not treat CAMT names as accounting logic.</h2><p>ISO 20022 messages describe bank communication. The SAP posting and clearing result still depends on configuration and matching.</p></header>
    <div class="ecg-input-grid">
      <article><span>pain.001</span><h3>Payment initiation</h3><p>A common ISO 20022 credit-transfer initiation message used for outgoing payments. The exact version is bank- and country-dependent.</p></article>
      <article><span>camt.053</span><h3>Bank statement</h3><p>Common ISO 20022 bank-to-customer statement format used to represent booked account activity.</p></article>
      <article><span>camt.054</span><h3>Debit/credit notification</h3><p>Can carry bank-to-customer debit/credit notifications and may be used in payment communication scenarios.</p></article>
      <article><span>MT940</span><h3>Legacy statement format</h3><p>Still present in many bank landscapes. A Lead should know the process can be modern even when the bank format is not ISO 20022.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header><p class="research-canvas__eyebrow">Diagnostic runtime</p><h2>Supplier is cleared, clearing account is not. What next?</h2></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Confirm bank execution</h3><p>Check bank status and statement evidence before assuming the payment failed.</p><strong>If bank execution is unknown, do not resend.</strong></article>
      <article><span>2</span><h3>Confirm statement import</h3><p>Did the correct bank account and statement reach SAP? Was the file imported without errors?</p><strong>Integration evidence first.</strong></article>
      <article><span>3</span><h3>Check transaction mapping</h3><p>External transaction, posting rule, and account symbol point to the intended bank-clearing account?</p><strong>Configuration decides the posting path.</strong></article>
      <article><span>4</span><h3>Check matching fields</h3><p>Payment reference, amount, currency, and value date align with the open clearing item?</p><strong>Good posting can still fail to clear.</strong></article>
      <article><span>5</span><h3>Reprocess with evidence</h3><p>Use F1520 or the relevant classic post-processing tool. Create a reusable rule only for a repeatable pattern.</p><strong>One-off repair is not always a configuration change.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">60-second answer</p><h2>“Why is the bank-clearing account still open?”</h2></header>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span><p>First I confirm whether the supplier invoice was already cleared by the payment run. Then I check whether the bank executed the payment and whether the correct bank statement reached SAP. If cash moved but the clearing account is still open, I inspect the EBS transaction mapping and the matching reference, amount, currency, and value date. I only reverse the supplier payment if the bank did not execute it and the accounting state must be reopened.</p><a href="/labs/assessment/">Practice more <span class="material-symbols-outlined" aria-hidden="true">school</span></a></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Primary references</p><h2>Current SAP Help baseline.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/PRODUCT_ID/3cb1182b4a184bdd93f8d62e3f1f0741/a1597b757dfd404283a050ab12585e5a.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Incoming Payment Files</strong><small>Import bank statements, payment rejections, and related payment files.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/PRODUCT_ID/3cb1182b4a184bdd93f8d62e3f1f0741/bc1fe656fe590950e10000000a44147b.html" target="_blank" rel="noopener"><span>SAP</span><strong>Reprocess Bank Statement Items</strong><small>Manual and rule-based recovery for items not posted or cleared automatically.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/039683576ea1a96be10000000a4450e5.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Payment Media</strong><small>Payment-medium operations and status.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
