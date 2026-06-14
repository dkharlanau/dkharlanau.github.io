---
layout: default
title: "SAP Bank Account Determination Diagnostics"
description: "A conservative diagnostic frame for house bank, payment method, and bank account determination issues in SAP."
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
    <p class="note-subtitle">A first-pass structure for finding why SAP does not select the expected house bank, payment method, or bank account.</p>
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
    <p>SAP selects a house bank and bank account for outgoing payments based on payment methods, amount groups, currencies, and ranking orders. For incoming payments, customer bank details drive automatic payment matching. A wrong selection can send a payment from the wrong account or fail to produce a payment medium. The diagnostic task is to trace the determination sequence from the payment method through the ranking order to the house bank account.</p>
    <p>This guide covers bank account determination for payment transactions, not cash management or liquidity planning.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Payment proposal selects a house bank the user did not expect.</li>
      <li>Payment method is not determined for a vendor or customer.</li>
      <li>Bank account is missing in the payment medium even though the house bank exists.</li>
      <li>Customer incoming payment does not match the open item because bank details differ.</li>
      <li>Payment run fails with "No house bank/bank account could be determined."</li>
      <li>Electronic bank statement posting fails due to missing house bank account.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing payment method:</strong> the vendor/customer master does not have a payment method for the company code.</li>
      <li><strong>Ranking order issue:</strong> the ranking order for payment methods or house banks points to an inactive entry.</li>
      <li><strong>Bank account not configured:</strong> the house bank account is missing in FBZP or FI12.</li>
      <li><strong>Amount or currency mismatch:</strong> the payment amount or currency is outside the permitted range for the bank account.</li>
      <li><strong>House bank inactive:</strong> the house bank is blocked for the payment program.</li>
      <li><strong>Master data mismatch:</strong> vendor/customer bank details differ from the bank statement or payment file.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>FBZP</strong> — payment program configuration: company code, paying company code, payment methods, bank determination.</li>
      <li><strong>FI12</strong> — house bank and bank account master data.</li>
      <li><strong>FK03 / FD03</strong> — vendor/customer master bank details and payment methods.</li>
      <li><strong>F110</strong> — payment run proposal and log.</li>
      <li><strong>FLB2</strong> — electronic bank statement posting.</li>
      <li><strong>SE16 / BNKA</strong> — bank master data.</li>
      <li><strong>SE16 / T012 / T012K</strong> — house bank and house bank account tables.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>T012</strong> — house bank master.</li>
      <li><strong>T012K</strong> — house bank accounts.</li>
      <li><strong>BNKA</strong> — bank master data.</li>
      <li><strong>LFBK / LFB1</strong> — vendor bank details and company code data.</li>
      <li><strong>KNBK / KNB1</strong> — customer bank details and company code data.</li>
      <li><strong>REGUH / REGUP</strong> — payment proposal and payment run header/items.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the company code, payment method, amount, currency, and vendor/customer from the payment proposal.</li>
      <li>Check FBZP for payment method configuration by country and company code.</li>
      <li>Review the bank determination ranking order in FBZP for the payment method and currency.</li>
      <li>Open FI12 and confirm the house bank and bank account exist and are active.</li>
      <li>Verify vendor/customer master payment method and bank details in FK03/FD03.</li>
      <li>Run the payment proposal in F110 and read the detailed proposal log.</li>
      <li>For bank statement issues, compare the external bank account with T012K entries.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Assign the correct payment method to the vendor or customer master.</li>
      <li>Adjust the ranking order in FBZP so the intended house bank is selected.</li>
      <li>Create or activate the missing house bank account in FI12.</li>
      <li>Extend amount group or currency settings to include the payment amount.</li>
      <li>Correct vendor/customer bank details to match the bank statement or payment file.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the company code, payment method, house bank, bank account, currency, amount, vendor/customer number, exact error or selection result, and whether the issue occurs in payment proposal, payment run, or bank statement processing.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Payment proposals select the wrong house bank for many vendors.</li>
      <li>Bank statement posting fails for an entire house bank account.</li>
      <li>Payment method configuration is missing for a country or payment medium.</li>
      <li>Bank account master changes are needed outside normal maintenance windows.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for bank account determination in payment processing, not a guide to treasury, cash management, or payment medium format development. It does not cover SWIFT or multi-bank connectivity setup.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
