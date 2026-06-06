---
layout: default
title: "SAP Procurement KPIs"
description: "Practical procurement KPIs that can be measured from SAP MM data, including where to find the data and common measurement pitfalls."
permalink: /atlas/sap/sap-procurement-kpis/
atlas_section: sap
domain: SAP operations
subdomain: Procurement analytics
concept_type: SAP concept
sap_area: MM / analytics
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - analytics
  - kpis
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-invoice-split-analysis/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Procurement KPIs</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP procurement KPIs</h1>
    <p class="note-subtitle">What procurement performance looks like in SAP data, where to measure it, and what to watch out for.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / analytics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Procurement KPIs in SAP are not just dashboard numbers. They reflect process discipline, master data quality, and supplier performance. The challenge is that raw SAP tables contain every document state, including drafts, reversals, and test data. A meaningful KPI requires filtering by document status, organizational scope, and time window. This page describes practical KPIs that an AMS operator or consultant can calculate from standard MM tables without custom extractors.</p>

    <h2>Key sections</h2>

    <h3>Purchase order cycle time</h3>
    <p>The time from purchase requisition creation to purchase order creation, or from PO creation to goods receipt. Measured in days or hours.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>EKKO</strong> (PO header: creation date, change date), <strong>EKPO</strong> (PO item), <strong>EBAN</strong> (PR header).</li>
      <li><strong>Pitfall</strong> — PRs converted to POs in bulk or via MRP have artificially short cycle times. Manual PRs with long approval workflows skew the average. Filter by creation type and document category.</li>
    </ul>

    <h3>Supplier on-time delivery rate</h3>
    <p>The percentage of PO lines where the goods receipt date is on or before the PO delivery date.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>EKET</strong> (delivery schedule), <strong>EKPO</strong> (PO item delivery date), <strong>MSEG</strong> (GR posting date).</li>
      <li><strong>Pitfall</strong> — The PO delivery date may have been changed after the fact, making a late delivery appear on time. Check the PO change history in <strong>CDPOS</strong> for date modifications.</li>
    </ul>

    <h3>Invoice accuracy rate</h3>
    <p>The percentage of invoices posted in MIRO that are not blocked for price or quantity variance.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>RBKP</strong> (invoice header: block status), <strong>RSEG</strong> (invoice item), linked to PO in <strong>EKPO</strong>.</li>
      <li><strong>Pitfall</strong> — Some invoices are blocked for manual review even when the variance is within tolerance, due to release strategy or user error. Distinguish between system-blocked and manually blocked.</li>
    </ul>

    <h3>GR/IR aging</h3>
    <p>The age of open GR/IR items where goods have been received but no invoice has been posted, or vice versa.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>BSIS</strong> / <strong>BSAK</strong> (G/L line items on the GR/IR reconciliation account), filtered by open item indicator. Cross-reference with <strong>MSEG</strong> for GR date and <strong>RBKP</strong> for invoice date.</li>
      <li><strong>Pitfall</strong> — Old open items may be legitimate (long payment terms, consignment) or may be cleanup items from incomplete reversals. Do not treat all old items as errors.</li>
    </ul>

    <h3>Procurement spend under contract</h3>
    <p>The percentage of PO value that references an outline agreement or contract.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>EKPO</strong> (contract or scheduling agreement reference in <code>KONNR</code> or <code>ABRNG</code>).</li>
      <li><strong>Pitfall</strong> — Framework agreements may be referenced loosely or not at all. A PO without a contract reference does not always mean maverick buying; some categories are intentionally non-contracted.</li>
    </ul>

    <h3>Maverick buying rate</h3>
    <p>The percentage of PO value or count created without a purchase requisition, without a contract, or outside the preferred supplier list.</p>
    <ul>
      <li><strong>Where to find it</strong> — <strong>EKKO</strong> (creation indicator: <code>FRGGR</code>, <code>FRGSX</code>), <strong>EKPO</strong> (PR reference, contract reference, info record reference).</li>
      <li><strong>Pitfall</strong> — Emergency purchases, low-value orders, and recurring operational buys are often legitimately created without a PR. Define the scope before measuring.</li>
    </ul>

    <h3>Common measurement pitfalls</h3>
    <ul>
      <li><strong>Test data</strong> — development and quality assurance systems often contain unrealistic dates and quantities. Always filter by real company codes and plants.</li>
      <li><strong>Document status</strong> — deleted or held documents should be excluded. Check <code>LOEKZ</code> (deletion indicator) and <code>STATU</code> (status).</li>
      <li><strong>Currency</strong> — PO values may be in document currency, local currency, or group currency. Be consistent.</li>
      <li><strong>Partial deliveries</strong> — a single PO item with multiple GRs and invoices creates multiple rows. Aggregating at PO header level can hide item-level problems.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Before building any procurement KPI report, define the exact business question and the organizational scope. A KPI that mixes MRP-generated POs with manual emergency buys is meaningless. Start with one plant, one material group, and one time window. Validate the numbers against a known document in <strong>ME23N</strong> before publishing the report.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page describes KPIs based on standard MM tables. It does not cover S/4HANA embedded analytics, SAP Ariba spend metrics, or BW/4HANA procurement cubes. It does not provide SQL or ABAP code for extraction.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-invoice-split-analysis/">SAP Invoice Split Analysis</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
