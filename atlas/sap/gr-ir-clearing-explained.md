---
title: SAP GR/IR Clearing Explained
layout: default
description: A clear explanation of why the GR/IR clearing account exists, what an open balance means, and how procurement and finance reconcile it.
permalink: /atlas/sap/gr-ir-clearing-explained/
atlas_section: sap
domain: SAP operations
subdomain: Procurement finance
concept_type: SAP concept
sap_area: MM / FI / invoice verification
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-09-22
tags:
  - procure-to-pay
  - sap-mm
  - procurement
related:
  - "/atlas/maps/procure-to-pay-map/"
  - "/atlas/diagnostics/sap-goods-receipt-diagnostics/"
  - "/atlas/diagnostics/sap-three-way-match-diagnostics/"
  - "/atlas/sap/sap-mm-procurement-overview/"
robots: noindex,follow
short_title: GR/IR Clearing Explained
h1: SAP GR/IR clearing explained
subtitle: GR/IR connects the physical receipt of goods with the supplier invoice when those events happen at different times.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li><li aria-current="page">GR/IR Clearing Explained</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
<p class="eyebrow">Knowledge Atlas</p>
<h1>SAP GR/IR clearing explained</h1>
<p class="note-subtitle">GR/IR connects the physical receipt of goods with the supplier invoice when those events happen at different times.</p>
<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>SAP concept</dd></div><div><dt>Reviewed</dt><dd>2026-09-22</dd></div></dl></aside>

<div class="note-body">
<h2>Why GR/IR exists</h2>
<p>Procurement creates two independent facts. The first is operational: goods or services were received. The second is financial: the supplier sent an invoice that creates a payable. Those events rarely happen at exactly the same moment. SAP uses the goods receipt/invoice receipt clearing account, usually shortened to <strong>GR/IR</strong>, to bridge the gap.</p>

<p>For a typical valuated goods receipt, the receipt updates inventory or consumption and creates the corresponding GR/IR posting. When the supplier invoice is posted, the invoice creates the vendor liability and the matching posting against GR/IR. The exact accounting depends on the purchasing and valuation scenario, but the idea stays the same: GR/IR temporarily holds the difference between what the business says it received and what the supplier says it invoiced.</p>

<h2>An open balance is a message about process state</h2>
<p>If receipt and invoice quantities and values align, the related GR/IR items can be cleared. If they do not, the open balance tells us that the purchasing story is not complete yet. SAP documentation gives the cleanest examples: when the invoiced quantity is higher than the received quantity, the system expects further goods receipts; when the received quantity is higher, it expects further invoices.</p>

<p>This is why GR/IR is more useful when read by purchase-order item than as one large account balance. A total of zero can hide many old unmatched items, while a non-zero total can include perfectly legitimate timing differences. We need the document relationship, not just the account total.</p>

<h2>Most differences fall into a few patterns</h2>
<p>The simplest case is timing: the warehouse posted the receipt today and the invoice will arrive next week. Quantity differences are similar but need more attention because they may represent partial deliveries, returns, over-invoicing, or an incomplete receipt. Price differences can remain when the invoice and purchasing documents do not value the same quantity in the same way. Delivery costs and corrections can add another layer.</p>

<p>Before treating an old balance as a cleanup item, we ask whether another business document is still expected. If the purchase-order item is genuinely complete and no more goods or invoices will arrive, the remaining balance needs reconciliation. Current S/4HANA documentation provides the <strong>Clear GR/IR Clearing Account</strong> function (app ID <strong>MR11</strong>) for this purpose, and the <strong>Reconcile GR/IR Accounts</strong> app brings procurement and accounting information together for exception handling.</p>

<h2>Reconciliation starts from the purchase-order history</h2>
<p>A useful investigation follows one purchase-order item from order to receipt to invoice. We compare what was ordered, what was received, what was invoiced, and what was reversed or corrected. That sequence usually explains the balance more reliably than starting from a G/L line-item list and guessing backwards.</p>

<p>The result should be a business explanation: “20 pieces were received but not yet invoiced,” “the invoice was posted for a higher quantity than the receipt,” or “no further documents are expected and the residual difference is ready for approved clearing.” Those statements are actionable because they describe what is missing.</p>

<h2>GR/IR is part of period close, but it is not only a finance problem</h2>
<p>Finance sees the open account, but the cause can sit in purchasing, receiving, invoice processing, or document reversal. Good GR/IR reconciliation therefore crosses team boundaries. The account is a financial representation of a logistics process, and cleaning it without understanding that process can hide the same error until the next period.</p>

<h2>Sources</h2>
<ul>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/72256b54f94c8f4ce10000000a4450e5.html">SAP Help: Clear GR/IR Clearing Account</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/17f3a45189524e78b4a80bf51ff2b741.html">SAP Help: Reconcile GR/IR Accounts</a></li>
</ul>
</div>

<section class="atlas-related"><h2>Related pages</h2><ul>
<li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
<li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods Receipt Diagnostics</a></li>
<li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">Three-Way Match Diagnostics</a></li>
<li><a href="/atlas/sap/sap-mm-procurement-overview/">MM Procurement Overview</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
