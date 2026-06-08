---
layout: default
title: "Why invoice verification delays increase procurement support cost"
description: "Price, quantity, and tax mismatches between PO, GR, and invoice create blocked invoices in MIRO, driving manual reconciliation, late payment penalties, and month-end close delays."
permalink: /scenarios/invoice-verification-three-way-match-delays/
scenario_cluster: Process Execution Pain
domain: SAP AMS
subdomain: Procurement finance control
concept_type: business scenario
sap_area: "MM invoice verification / three-way match"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - invoice-verification
  - diagnostics
related:
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/diagnostics/sap-three-way-match-diagnostics/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/scenarios/">Scenarios</a></li>
    <li aria-current="page">Why invoice verification delays increase procurement support cost</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Scenario — Process Execution Pain</p>
    <h1>Why invoice verification delays increase procurement support cost</h1>
    <p class="note-subtitle">Price, quantity, and tax mismatches between PO, GR, and invoice create blocked invoices in MIRO, driving manual reconciliation, late payment penalties, and month-end close delays.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM invoice verification / three-way match</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until scenario claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Business pain</h2>
    <p>Invoices sit in blocked status for days or weeks because the three-way match between purchase order, goods receipt, and invoice fails. Accounts payable cannot post the invoice, the supplier does not get paid on time, and procurement spends hours reconciling line-item differences manually. Month-end close is delayed because open GR/IR items cannot be cleared.</p>

    <h2>Process context</h2>
    <p>The three-way match is the core control in SAP procure-to-pay. When the invoice arrives via MIRO, SAP compares quantities and prices against the PO and GR. If any variance exceeds tolerance limits, or if the GR is missing, the invoice is blocked for payment. The block may be automatic (tolerance, quantity variance) or manual (price discrepancy, tax mismatch). Each blocked invoice becomes a support ticket, an email chain, or a spreadsheet tracker.</p>

    <h2>Typical symptoms</h2>
    <ul>
      <li>High volume of invoices in blocked status (RBKP_BLOCKED, BSEG with payment block).</li>
      <li>Repeated MIRO error messages referencing tolerance limits or quantity variance.</li>
      <li>GR/IR clearing account growing month over month with unreconciled items.</li>
      <li>Suppliers escalating late payments despite goods having been received.</li>
      <li>Month-end accrual adjustments because GR/IR cannot be cleared in time.</li>
    </ul>

    <h2>SAP touchpoints</h2>
    <ul>
      <li><strong>MIRO</strong> — invoice entry and variance checking.</li>
      <li><strong>ME23N / ME2N</strong> — PO history and three-way match visibility.</li>
      <li><strong>MIR4 / MIR5</strong> — invoice document display and lists.</li>
      <li><strong>GR/IR clearing account</strong> — FBL3N for open item analysis.</li>
      <li><strong>Tolerance keys</strong> — AN, AP, BD, BR, BW, DO, DW, KW, LA, LD, PE, PS, SE, ST, VP.</li>
      <li><strong>Payment blocks</strong> — R (invoice verification difference), A (manual block), G (GR-based invoice verification).</li>
      <li><strong>OBY6 / company code settings</strong> — GR/IR account maintenance and posting period control.</li>
    </ul>

    <h2>Master data / configuration / integration touchpoints</h2>
    <ul>
      <li><strong>Vendor master</strong> — incorrect tax codes, payment terms, or reconciliation accounts.</li>
      <li><strong>Material master / info record</strong> — outdated prices or order unit mismatches.</li>
      <li><strong>Purchase order</strong> — partial deliveries, changed quantities, or price adjustments after GR.</li>
      <li><strong>Goods receipt</strong> — over-delivery, under-delivery, or GR posted to wrong storage location.</li>
      <li><strong>Tax configuration</strong> — tax code mismatches between PO and invoice, especially in cross-border scenarios.</li>
      <li><strong>Tolerance configuration</strong> — tolerance groups (OMR6) set too tight or too loose for the business reality.</li>
      <li><strong>IDoc / EDI interfaces</strong> — invoice data arriving with wrong currency, quantity unit, or tax indicator.</li>
    </ul>

    <h2>Cost drivers</h2>
    <ul>
      <li><strong>Manual reconciliation time</strong> — each blocked invoice often requires 15–60 minutes of consultant or clerk time to trace PO history, compare GR quantities, and confirm price validity.</li>
      <li><strong>Late payment penalties</strong> — blocked invoices delay payment runs; early-payment discounts may be lost.</li>
      <li><strong>Supplier disputes</strong> — repeated blocks damage supplier relationships and may trigger renegotiation or supply risk.</li>
      <li><strong>Month-end close delays</strong> — uncleared GR/IR items prevent clean financial close and may require manual accrual postings.</li>
      <li><strong>Audit findings</strong> — persistent GR/IR imbalances often attract auditor attention as a control weakness.</li>
    </ul>

    <h2>Root cause patterns</h2>
    <ul>
      <li><strong>Tolerance misalignment</strong> — tolerance limits do not reflect actual supplier behavior or material price volatility.</li>
      <li><strong>GR timing gaps</strong> — invoice arrives before GR is posted, especially in drop-ship or third-party scenarios.</li>
      <li><strong>Price changes after GR</strong> — retroactive price adjustments or contract renegotiations create invoice-PO mismatches.</li>
      <li><strong>Unit of measure conversion errors</strong> — ordering in cases, receiving in pallets, invoicing in kilograms.</li>
      <li><strong>Tax configuration drift</strong> — tax code changes in the vendor master or country-specific rules not reflected in PO.</li>
      <li><strong>Interface mapping errors</strong> — EDI or IDoc fields mapped incorrectly, especially for quantity, price, and tax.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <p>A practical first-pass diagnostic for blocked invoices:</p>
    <ol>
      <li><strong>Identify the block reason</strong> — in MIR4 or RBKP_BLOCKED, check the payment block code and tolerance message.</li>
      <li><strong>Compare PO, GR, and invoice line items</strong> — use ME23N PO history to confirm quantity, price, and unit alignment.</li>
      <li><strong>Check tolerance settings</strong> — in OMR6, verify whether the variance falls within the configured tolerance key.</li>
      <li><strong>Review GR/IR account</strong> — in FBL3N, check whether the GR was posted and whether the clearing item exists.</li>
      <li><strong>Validate tax codes</strong> — compare tax code on PO, GR, and invoice; check FTXP for validity.</li>
      <li><strong>Inspect interface data</strong> — if the invoice arrived via IDoc, review WE02/WE05 for segment-level errors.</li>
      <li><strong>Confirm vendor master consistency</strong> — check XK03 for payment terms, tax category, and reconciliation account.</li>
    </ol>

    <h2>Solution patterns</h2>
    <ul>
      <li><strong>Align tolerance configuration with business reality</strong> — review OMR6 settings quarterly against actual variance distributions.</li>
      <li><strong>Enforce GR-before-invoice discipline</strong> — for GR-based invoice verification, configure message control to prevent invoice entry before GR.</li>
      <li><strong>Standardize units of measure</strong> — lock order unit and price unit in info records; avoid ad-hoc conversions.</li>
      <li><strong>Automate GR/IR clearing</strong> — schedule F.13 or use background jobs with clear selection criteria.</li>
      <li><strong>Fix interface mappings</strong> — validate EDI/IDoc field mappings for quantity, price, and tax during onboarding.</li>
      <li><strong>Proactive vendor communication</strong> — notify vendors of blocked invoices via automated output rather than reactive email.</li>
    </ul>

    <h2>AI / automation / workflow opportunity</h2>
    <p>Structured diagnostic knowledge can reduce the time per blocked-invoice ticket significantly. A support knowledge system that maps block reason codes to the exact PO/GR/invoice comparison steps can guide junior consultants through reconciliation without escalating to senior staff. Automated monitoring of GR/IR account growth, tolerance key hit rates, and vendor-specific block frequency can flag configuration drift before it becomes a month-end crisis. Natural-language query interfaces over PO history and invoice status can help process owners self-serve status updates instead of opening AMS tickets.</p>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a> — step-by-step MIRO error analysis and block reason decoding.</li>
      <li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">SAP Three-Way Match Diagnostics</a> — PO/GR/invoice alignment checks and tolerance key reference.</li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a> — GR timing, quantity variance, and storage location issues.</li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a> — account mechanics, clearing transactions, and month-end handling.</li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a> — procurement process structure and key objects.</li>
    </ul>

    <h2>Public references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b481d23b7654d3d901b0b324668d8d7/4b85a7f5e9d74fd4a6c5e6e5e5e5e5e5.html">SAP Help — Invoice Verification</a> — official SAP documentation on MIRO and variance handling.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b481d23b7654d3d901b0b324668d8d7/4b85a7f5e9d74fd4a6c5e6e5e5e5e5e5.html">SAP Help — Tolerance Groups</a> — configuration reference for tolerance keys in invoice verification.</li>
    </ul>

    <h2>Verification status and limitations</h2>
    <p>This scenario is a structured working hypothesis based on operational patterns observed in SAP AMS support. Specific cost figures, transaction behavior, and configuration details vary by SAP release, industry solution, and custom enhancement. Validate in your own landscape and official SAP documentation before acting on diagnostic recommendations.</p>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
