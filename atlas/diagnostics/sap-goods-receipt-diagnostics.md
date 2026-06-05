---

title: SAP Goods Receipt Diagnostics
layout: default
description: A practical support diagnostic guide for SAP goods receipt issues.
permalink: /atlas/diagnostics/sap-goods-receipt-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: MM inventory management
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-05-06

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - procurement
related: 
  - "/atlas/maps/procure-to-pay-map/"
  - "/atlas/sap/gr-ir-clearing-explained/"
source_files: 
  - "private-source/kb-drafts/sap-domain-atlas/domains/logistics/concepts/warehouse/goods-receipt.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/inventory-management/goods-receipt.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/troubleshooting/goods-receipt-blocked.md"
robots: noindex,follow
short_title: Goods Receipt Diagnostics
h1: SAP goods receipt diagnostics
subtitle: Goods receipt is where physical delivery becomes system evidence. Mistakes ripple into stock, invoice matching, and finance.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">Goods Receipt Diagnostics</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP goods receipt diagnostics</h1>

<p class="note-subtitle">Goods receipt is where physical delivery becomes system evidence. Mistakes ripple into stock, invoice matching, and finance.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP AMS</dd></div><div><dt>Type</dt><dd>diagnostic guide</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Goods receipt sits at the boundary of inbound logistics, inventory management, invoice verification, and accounting.</p>

<h2>Common issues</h2>

<ul>

<li>The purchase order is closed, blocked, wrong, or no longer matches the physical delivery.</li>

<li>The material, batch, serial number, storage location, or quality status prevents normal posting.</li>

<li>A receipt was posted too early, too late, with the wrong quantity, or against the wrong reference.</li>

</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>What was physically received, and what document is the system expecting?</li>

<li>Is the error about quantity, status, account assignment, quality inspection, batch/serial data, or authorization?</li>

<li>What changed after the receipt: stock, purchase order history, inspection status, and invoice matching?</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>

<li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
