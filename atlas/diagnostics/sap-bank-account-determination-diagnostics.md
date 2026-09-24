---
layout: default
title: "SAP Bank Account Determination Diagnostics"
description: "Diagnose SAP automatic-payment bank selection by separating payment-method eligibility, house-bank ranking, account selection, available amounts, and partner bank details."
permalink: /atlas/diagnostics/sap-bank-account-determination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data governance
concept_type: diagnostic guide
sap_area: "FI-AP / FI-AR"
business_process: Payment processing
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - bank-account
related:
  - /atlas/diagnostics/sap-payment-run-dunning-diagnostics/
  - /atlas/diagnostics/sap-company-code-data-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Bank Account Determination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP bank account determination diagnostics</h1>
    <p class="note-subtitle">Trace an unexpected outgoing-payment bank from the payment method to the house bank, account ID, available amount, and posting account.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Payment processing</dd></div>
      <div><dt>SAP area</dt><dd>FI-AP / FI-AR</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>When an automatic payment uses the wrong bank account, it is tempting to start with the house bank master. That is often too late in the decision chain. SAP first has to decide that an item is payable and which payment method applies. Only then can it choose the company bank and the account from which the payment should be made.</p>

    <p>A useful working model is:</p>

    <p><strong>eligible open item → payment method → partner bank details, when required → house-bank ranking → house-bank account → available amount and value-date checks → payment posting and payment medium</strong></p>

    <p>Each arrow is a different configuration or data boundary. If we identify the first wrong decision, the incident usually becomes much smaller.</p>

    <aside class="callout">
      <strong>Scope:</strong> this page focuses on bank selection for automatic outgoing payments. Electronic bank statement processing, cash management, payment-format development, and bank communication are later or separate processes.
    </aside>

    <h2>First decide whether bank determination has actually started</h2>
    <p>A missing payment is not automatically a bank-selection problem. If the open item is excluded because it is not due, is blocked, or has no usable payment method, there is no house bank to diagnose yet. Start with the payment proposal and its exception evidence.</p>

    <p>Current SAP S/4HANA provides proposal review through the automatic-payment process, including exception analysis. The useful evidence is the paying company code, business partner, open item, payment method, amount, currency, and the exact proposal result. If the item never reaches bank selection, keep the investigation in item, payment-method, or master-data determination.</p>

    <h2>The payment method sets the bank-selection context</h2>
    <p>The payment method describes how the payment is to be made, for example by transfer or check. SAP defines payment methods at country or region level and then for the company code. A method can come from business-partner master data or from the open item; when a payment method is specified on the open item, SAP documents that it takes precedence over the master-record proposal.</p>

    <p>This distinction matters because bank determination is configured by payment method. If the program has selected a different method from the one the support team expected, changing house-bank ranking will not correct the real cause.</p>

    <h2>Ranking order chooses the house-bank candidate</h2>
    <p>For automatic outgoing payments, the bank-selection configuration is maintained for the paying company code. The ranking order associates a payment method, optionally a currency, with house banks in a defined sequence. SAP evaluates that sequence when choosing the bank from which the payment should be made.</p>

    <p>Consider a company code with two EUR transfer banks:</p>

    <table>
      <thead>
        <tr><th>Payment method</th><th>Currency</th><th>Rank</th><th>House bank</th></tr>
      </thead>
      <tbody>
        <tr><td>Transfer</td><td>EUR</td><td>1</td><td>HB01</td></tr>
        <tr><td>Transfer</td><td>EUR</td><td>2</td><td>HB02</td></tr>
      </tbody>
    </table>

    <p>If the program uses HB02, “ranking order is wrong” is only one hypothesis. HB01 may be unavailable for that payment because the relevant account entry, amount, currency, or another bank-selection condition is not satisfied. Diagnose why the first candidate was rejected before changing the sequence.</p>

    <h2>The house bank and the account ID are separate decisions</h2>
    <p>A house bank represents a bank used by the company. In current SAP S/4HANA documentation it is identified together with the company code, and the company can maintain several house banks. The account ID identifies the account used under that house bank for payment processing.</p>

    <p>Bank determination therefore does not stop when the correct house bank is found. The bank-account settings connect the house bank, payment method, currency, and account ID. In current S/4HANA configurations, the posting side can also use the bank-reconciliation-account model, where the bank subaccount or clearing account is derived for the payment method rather than maintained as an isolated hard-coded account.</p>

    <p>Keep bank master maintenance separate from payment-program configuration. Current SAP S/4HANA supports house-bank maintenance through the Manage Banks app and <code>FI12_HBANK</code>; bank accounts can also be managed through Bank Account Management. Those objects must exist and be connected correctly, but their existence alone does not define the ranking used by the automatic payment program.</p>

    <h2>Available amounts can move the payment to the next bank</h2>
    <p>The payment program can check the available amount configured for a bank account. For outgoing payments, this setting limits how much can be paid from the account for the relevant value-date context. If one candidate cannot cover the payment, SAP can continue with another bank account.</p>

    <p>This is an important diagnostic detail because SAP documents that the payment program does not split one payment across several accounts merely to satisfy the available-amount limit. If no candidate can cover the entire payment, the payment is not executed from a partially available account.</p>

    <p>For an unexpected second-choice bank, compare the payment amount and currency with the available-amount settings before concluding that ranking order was ignored.</p>

    <h2>Partner bank details belong to the other side of the payment</h2>
    <p>The company’s house bank answers <em>where the money comes from</em>. The customer or supplier bank details answer <em>where the money goes</em>. They are related in the payment run but are not the same determination.</p>

    <p>If a payment method requires business-partner bank details, SAP selects bank details that satisfy the method’s requirements. That can include restrictions such as permitted bank country or collection authorization. A wrong beneficiary account therefore points first to partner bank selection, not to house-bank ranking.</p>

    <p>This separation also prevents a common support mistake: changing the company bank configuration to fix a problem that actually sits in the business partner’s bank data.</p>

    <h2>Read the symptom against the decision boundary</h2>
    <table>
      <thead>
        <tr><th>Symptom</th><th>First boundary to inspect</th><th>Useful evidence</th></tr>
      </thead>
      <tbody>
        <tr><td>Item is missing from the proposal</td><td>Eligibility / payment method</td><td>Proposal exception, due date, payment block, payment method</td></tr>
        <tr><td>Unexpected house bank</td><td>Ranking order and candidate validity</td><td>Paying company code, method, currency, ranking entries, available amounts</td></tr>
        <tr><td>Correct house bank, wrong account</td><td>Bank-account determination</td><td>House bank, account ID, currency, payment method, posting account</td></tr>
        <tr><td>Correct company bank, wrong beneficiary bank</td><td>Partner bank selection</td><td>Business-partner bank details and payment-method requirements</td></tr>
        <tr><td>Payment posted but no usable bank file</td><td>Payment-medium processing</td><td>Payment result, medium status, format and downstream handoff</td></tr>
        <tr><td>Bank statement does not post or clear</td><td>Bank-statement processing</td><td>Statement item, interpretation/processing rule, posting and clearing result</td></tr>
      </tbody>
    </table>

    <h2>A compact diagnostic sequence</h2>
    <ol>
      <li><strong>Open the exact payment proposal or payment run.</strong> Confirm that the item was selected and record the exception if it was not.</li>
      <li><strong>Confirm the effective payment method.</strong> Do not assume the method from the business-partner master if the open item specifies another one.</li>
      <li><strong>Record the bank-selection inputs.</strong> Paying company code, payment method, currency, amount, expected house bank, and expected account ID.</li>
      <li><strong>Read the ranking order.</strong> Check which house bank should be tried first for that method and currency.</li>
      <li><strong>Check the account entry for the candidate bank.</strong> Verify house bank, account ID, currency, payment method, and the relevant posting-account setup.</li>
      <li><strong>Check available amounts when the program skipped a preferred bank.</strong> Compare the full payment amount with the configured capacity for the account and value date.</li>
      <li><strong>Separate partner-bank problems.</strong> If the company account is correct but the recipient account is wrong or missing, inspect business-partner bank details instead.</li>
      <li><strong>Retest through the proposal before executing money movement.</strong> A corrected proposal is safer evidence than changing several bank settings and immediately running the final payment.</li>
    </ol>

    <p>The objective is not to make the payment program choose a particular bank at any cost. It is to prove why the configured decision chain produced its result, then change only the layer that is actually wrong.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/0804c5536a51204be10000000a174cb4.html">Customizing of the Payment Program</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/39ebd353ca9f4408e10000000a174cb4.html">Procedure for Controlling Bank Selection</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/ebead353ca9f4408e10000000a174cb4.html">Available Amounts</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ac319d8fa4ea4624b40a58d23e3c4627/4460d353c6244308e10000000a174cb4.html">Defining House Banks</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/848f8ce21bcd4f67bce77494799e2257/1204c55368511d4be10000000a174cb4.html">Selecting the Bank Details of a Business Partner</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3eb1567cf97543c08087efb0936964e6/45698054f87c033de10000000a441470.html">Manage Automatic Payments</a> and <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/de567c542889063de10000000a441470.html">Revise Payment Proposals</a>.</li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
