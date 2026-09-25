---
layout: default
title: "SAP Concur"
description: "SAP Concur explained: Expense, Travel, Invoice, how employee spend becomes an approved accounting document, and where ERP integration begins."
permalink: /atlas/sap/sap-concur/
atlas_section: sap
domain: SAP operations
subdomain: Travel and expense
concept_type: product
sap_area: "Concur"
business_process: "Travel and expense"
status: needs_verification
verified: false
last_synced: 2026-07-14
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-concur
  - travel-expense
  - employee-spend
related:
  - /atlas/sap/sap-product-portfolio/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Concur</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Concur</h1>
    <p class="note-subtitle">Cloud applications for employee expenses, business travel, and accounts-payable invoice processing.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Travel and expense</dd></div>
      <div><dt>SAP area</dt><dd>Concur</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Concur is better understood as a family of cloud spend applications than as one workflow. <strong>Concur Expense</strong> manages employee expense reports, <strong>Concur Travel</strong> manages business-trip booking and itinerary information, and <strong>Concur Invoice</strong> supports accounts-payable invoice processing. They can share data and user experience, but their business objects and accounting paths are different.</p>

    <h2>Expense turns evidence of spend into an approved report</h2>
    <p>An expense process usually starts before there is an accounting document. Concur Expense can collect items that are ready to become expense entries, such as company-card transactions, e-receipts, travel segments, mobile entries, and ExpenseIt results. Employees can also add out-of-pocket expenses. Which sources are available depends on company configuration.</p>

    <p>Those inputs are assembled into an expense report. Receipts may be attached at expense or report level, policy rules can require evidence or flag exceptions, and approval happens before the financial posting step. This distinction matters because a card transaction, a receipt image, an expense entry, and an approved report are related records, not four names for the same thing.</p>

    <h2>A travel booking is not yet an expense</h2>
    <p>Concur Travel can provide itinerary segments to Concur Expense, but a booked flight or hotel is still a plan for travel, not proof of the final amount charged. SAP's current Travel and Expense integration documentation shows itinerary items alongside card transactions and e-receipts in Available Expenses. The actual expense process reconciles those sources into the report that the employee submits.</p>

    <p>This is why an itinerary total can differ from the amount that eventually reaches accounting. Taxes, fees, changed bookings, cancellations, card settlements, and personal out-of-pocket items can change the final expense picture. The useful question is not simply whether Travel and Expense are “integrated,” but which source supplied each amount and how it was matched.</p>

    <h2>Concur Invoice is an accounts-payable process</h2>
    <p>Concur Invoice handles vendor invoices and credit memos rather than employee expense reports. Current SAP documentation describes both paper and electronic invoice intake, supporting documents, invoice processing, and approval. Invoice Capture can add OCR-based capture where that feature is licensed and configured.</p>

    <p>Keeping this boundary visible prevents a common design mistake. An employee reimbursement and a supplier invoice may both end in Financial Accounting, but they start from different business evidence, follow different approvals, and should not be modelled as one generic “Concur document.”</p>

    <h2>The ERP boundary begins with an explicit financial integration</h2>
    <p>SAP provides standard integration between SAP Concur solutions and SAP S/4HANA for supported scenarios. In SAP S/4HANA 2025 FPS01, SAP documents bidirectional communication that can export master data such as cost objects and import Concur financial documents. For SAP S/4HANA Cloud, the current integration guide covers Concur Expense and Concur Invoice and returns posting feedback to the Concur workflow.</p>

    <p>That is more precise than saying that Concur simply “feeds the ERP.” The integration needs agreed company identifiers, cost objects, G/L mapping, tax and payment settings, employee or vendor context, and an error-handling path. In a configured Expense flow, an approved report enters a financial posting queue; a posting failure can then be returned to Concur for correction and resubmission.</p>

    <h2>Trace a mismatch through the document states</h2>
    <p>When a number is wrong, we follow the spend from its source rather than starting at the final journal entry. Was the amount imported from a card, created from a receipt, or entered manually? Was it attached to the correct report and allocation? Did policy or approval change the report state? Did the financial integration accept it, and did S/4HANA post the expected accounting document?</p>

    <p>This sequence separates user-entry problems from policy configuration, integration mapping, and ERP posting. It also avoids assuming that a report marked approved in Concur must already exist as a successful financial posting.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/concur-expense/concur-expense-professional-edition-end-user-help/available-expenses-overview">Concur Expense: Available Expenses - Overview</a> (2026_07).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_CONCUR/a759a183cd9d49e3bd0edf8493d12578/d19deb4c6ddd1014b625a44135d32877.html">Concur Travel Integration Using Normal Expense Report Process</a> (2026_07).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/CONCUR_INVOICE/5d4d01ab28704a4fbfa543f20b66966c/1470d2befcc64d258d613c89ef413226.html">Concur Invoice Professional Edition: Overview</a> (2026_07).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/c682b0c107a5447fa2c0885134ad5f8c.html">SAP S/4HANA: Integration with SAP Concur</a> (2025 FPS01).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_CONCUR/20a0937ba80e46f4b7f15f6fd3114ef0/1884e43e6f091014a8d9dcf340b5a74a.html">SAP Integration with Concur Solutions for SAP S/4HANA Cloud Setup Guide</a> (2026_07).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP Concur editions, optional services, country capabilities, card and travel integrations, and supported ERP scenarios change over time. Verify the exact Concur edition, S/4HANA deployment, integration package, and company configuration before using this page as an implementation design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-product-portfolio/">SAP Product Portfolio</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
