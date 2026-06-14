---
layout: default
title: "SAP Payment Run and Dunning Diagnostics"
description: "A conservative diagnostic frame for payment proposals, exceptions, dunning notices, and blocked items in SAP."
permalink: /atlas/diagnostics/sap-payment-run-dunning-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP operations
concept_type: diagnostic guide
sap_area: "FI-AP / FI-AR"
business_process: Payment processing
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - payment-run
related:
  - /atlas/diagnostics/sap-bank-account-determination-diagnostics/
  - /atlas/diagnostics/sap-background-job-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Payment Run and Dunning Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP payment run and dunning diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why payment proposals, dunning runs, or payment exceptions do not match expectations.</p>
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
    <h2>Core idea</h2>
    <p>Payment runs and dunning runs are periodic mass processes that select open items, propose payments or notices, and generate output. Failures appear as excluded items, wrong amounts, blocked documents, or missing payment media. The diagnostic task is to read the proposal log, identify the exception reason for each item, and trace it back to master data, document status, or configuration.</p>
    <p>This guide covers AP/AR payment and dunning execution, not payment format development or collections management.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Expected invoice is missing from the payment proposal.</li>
      <li>Payment proposal lists an item as blocked or not due.</li>
      <li>Dunning run does not generate a notice for an overdue customer.</li>
      <li>Payment amount is split into multiple payments unexpectedly.</li>
      <li>Payment run job fails or cancels in SM37.</li>
      <li>Dunning level does not increase even though the item is overdue.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Document blocked:</strong> the invoice is blocked for payment by reason code, amount, or manual block.</li>
      <li><strong>Payment method issue:</strong> vendor/customer master lacks a valid payment method for the amount or currency.</li>
      <li><strong>Payment term mismatch:</strong> the due date calculation places the item outside the run date.</li>
      <li><strong>House bank not determined:</strong> ranking order or bank account configuration is missing.</li>
      <li><strong>Dunning configuration gap:</strong> dunning area, dunning procedure, or dunning level settings exclude the item.</li>
      <li><strong>Selection criteria too narrow:</strong> the payment or dunning run variant excludes the company code or document type.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>F110</strong> — payment run: parameters, proposal, edit proposal, payment run log.</li>
      <li><strong>F150</strong> — dunning run: parameters, proposal, print.</li>
      <li><strong>FB02 / FB03</strong> — document change/display to check payment block and payment method.</li>
      <li><strong>FK03 / FD03</strong> — vendor/customer master payment data.</li>
      <li><strong>FBZP</strong> — payment program configuration.</li>
      <li><strong>SM37</strong> — background job status for payment or dunning runs.</li>
      <li><strong>SP01 / SP02</strong> — spool requests for payment media and dunning notices.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>REGUH</strong> — payment run header.</li>
      <li><strong>REGUP</strong> — payment run item.</li>
      <li><strong>BSIK / BSAK</strong> — vendor open and cleared items.</li>
      <li><strong>BSID / BSAD</strong> — customer open and cleared items.</li>
      <li><strong>T042 / T042Z</strong> — payment program and payment method settings.</li>
      <li><strong>T047</strong> — dunning procedure settings.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Open the payment or dunning run in F110/F150 and review the parameters and run date.</li>
      <li>Display the proposal log and note the exception reason for the missing or blocked item.</li>
      <li>Open the document in FB03 and check payment block, payment method, due date, and document type.</li>
      <li>Verify vendor/customer master payment settings in FK03/FD03.</li>
      <li>Check FBZP for payment method and bank determination if the item is excluded due to bank selection.</li>
      <li>For dunning, verify the dunning procedure, dunning area, and last dunning date in the customer master.</li>
      <li>Check SM37 and spool requests if the run itself failed or produced no output.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Remove the payment block from the document if it was set in error.</li>
      <li>Assign or correct the payment method in the vendor/customer master.</li>
      <li>Adjust the run date or due date selection to include the item.</li>
      <li>Correct house bank ranking or bank account configuration in FBZP.</li>
      <li>Update dunning procedure or dunning level settings for the customer.</li>
      <li>Restart the failed background job after correcting the underlying error.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the run ID, run date, company code, payment method, dunning procedure, vendor/customer number, document number, line item, exception reason from the proposal log, and exact symptom.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Payment run fails for an entire company code or payment method.</li>
      <li>Dunning notices are not printed for many customers.</li>
      <li>Payment media files are generated with wrong totals or missing records.</li>
      <li>Bank statement reconciliation shows payments not matching the proposal.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for payment and dunning run execution, not a guide to payment format programming, bank communication, or credit management. It does not cover lockbox processing or collections workflow.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
