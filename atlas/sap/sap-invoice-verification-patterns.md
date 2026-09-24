---
layout: default
title: "SAP Invoice Verification Patterns"
description: "How SAP invoice verification compares supplier invoices with purchasing history, why invoices are blocked, and how to read a variance before correcting it."
permalink: /atlas/sap/sap-invoice-verification-patterns/
atlas_section: sap
domain: SAP operations
subdomain: Procurement finance
concept_type: SAP concept
sap_area: MM / FI / invoice verification
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - invoice-verification
related:
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Invoice Verification Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP invoice verification patterns</h1>
    <p class="note-subtitle">An invoice can be posted and still be wrong for payment. Invoice verification is where SAP separates those two questions.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / FI / invoice verification</dd></div>
      <div><dt>Reviewed</dt><dd>2026-09-22</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Invoice verification is a consistency check</h2>
    <p>A supplier invoice arrives late in the procurement process, after SAP may already know the purchase order, the expected price, and one or more goods receipts. Invoice verification brings those facts together. The important question is not simply whether the invoice can be entered. It is whether the invoice is consistent enough with the purchasing history to be paid without further review.</p>

    <p>When we enter an invoice with purchase-order reference, SAP proposes expected values from the purchasing documents. Depending on the scenario, goods-receipt information can also be part of that reference. The invoice brings the supplier's actual quantity and amount. SAP compares the two and applies configured tolerance rules. Small differences can be accepted; larger differences can make the invoice unsuitable for payment until somebody resolves the cause.</p>

    <h2>A payment block is not the same as a posting error</h2>
    <p>This distinction explains many confusing support cases. SAP can allow an invoice to be posted while automatically blocking it for payment because a tolerance limit was exceeded. The accounting document therefore exists, but Financial Accounting cannot pay the supplier line until the block is released. A block can also be set manually, and other blocking reasons exist in standard invoice verification.</p>

    <p>That means the presence of an accounting document does not prove that the invoice passed every business check. Conversely, a blocked invoice is not automatically a bad invoice. It may be a valid invoice that arrived before the remaining goods, a price change that procurement has not reflected in the order, or simply a difference that requires confirmation.</p>

    <h2>Read the variance in business context</h2>
    <p>Quantity and price are the two patterns we meet most often. If the supplier invoices more than has been received in a goods-receipt-based process, the system may be waiting for another receipt. If the price differs from the purchase order, the question is whether the supplier is wrong or the order is outdated. Schedule and quality-related checks can also matter in specific configurations.</p>

    <p>We therefore start with the document history rather than with tolerance configuration. Which purchase-order item is involved? What has actually been received? What quantity and price did the supplier invoice? Was the order changed? Is another delivery still expected? Once those facts are clear, the block usually becomes easier to interpret.</p>

    <h2>Fix the business mismatch before releasing the block</h2>
    <p>A blocked invoice can become valid later. For example, missing goods can arrive or the purchase-order price can be corrected after agreement with the supplier. SAP documentation makes an important point here: when the original blocking reason is no longer valid, the invoice can still remain blocked until the block is explicitly released. In classic SAP terminology, blocked invoices can be reviewed and released with the <strong>Release Blocked Invoices</strong> function (app ID <strong>MRBR</strong> in current S/4HANA documentation).</p>

    <p>If the invoice itself is wrong, release is not the answer. The document may need to be reversed or corrected according to the process. The goal is to make the procurement evidence and the supplier claim agree, not to make the red status disappear.</p>

    <h2>A useful way to explain an invoice issue</h2>
    <p>For support, we try to describe one variance in one sentence: “PO item 10 was ordered for 100 pieces, 80 have been received, and the supplier invoiced 100.” That is more useful than “MIRO is blocked.” The first description exposes the process state; the second only names the symptom.</p>

    <p>Once the mismatch is explicit, responsibility also becomes clearer. Purchasing owns an outdated price agreement, goods receiving owns a missing or incorrect receipt, Accounts Payable owns invoice-entry mistakes, and the supplier owns a genuinely incorrect invoice. SAP is the place where those facts meet.</p>

    <h2>Sources</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/7870b6531de6b64ce10000000a174cb4.html">SAP Help: Blocking Invoices</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/74497657a11a0522e10000000a44147b.html">SAP Help: Release Blocked Invoices</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
