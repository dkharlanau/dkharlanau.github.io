---
title: SAP GR/IR Clearing Explained
layout: default
description: A conservative explanation of GR/IR clearing in procurement and invoice verification.
permalink: /atlas/sap/gr-ir-clearing-explained/
atlas_section: sap
domain: SAP operations
subdomain: Procurement finance
concept_type: SAP concept
sap_area: MM / FI / invoice verification
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-05-06
related: 
  - "/atlas/maps/procure-to-pay-map/"
  - "/atlas/diagnostics/sap-goods-receipt-diagnostics/"
source_files: 
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/invoice-verification/gr-ir-clearing.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/troubleshooting/gr-ir-mismatch.md"
robots: noindex,follow
short_title: GR/IR Clearing Explained
h1: SAP GR/IR clearing explained
subtitle: GR/IR is the accounting bridge between received goods and supplier invoices. Mismatches are process evidence, not just finance noise.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/sap/">Sap</a></li><li aria-current="page">GR/IR Clearing Explained</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP GR/IR clearing explained</h1>

<p class="note-subtitle">GR/IR is the accounting bridge between received goods and supplier invoices. Mismatches are process evidence, not just finance noise.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>SAP concept</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>GR/IR sits between goods receipt and invoice verification. It helps separate the physical receipt event from the supplier invoice event.</p>

<h2>Common issues</h2>

<ul>

<li>Goods are received but the invoice has not arrived or cannot be matched.</li>

<li>Invoice quantity, price, tax, or purchase order reference differs from the receipt evidence.</li>

<li>Old balances remain because reversals, returns, cancellations, or invoice corrections were not handled consistently.</li>

</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>Which purchase order, goods receipt, and invoice documents are involved?</li>

<li>Is the mismatch quantity-based, price-based, tax-related, timing-related, or reversal-related?</li>

<li>Does the open item represent a real business mismatch or a cleanup item?</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>

<li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods Receipt Diagnostics</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
