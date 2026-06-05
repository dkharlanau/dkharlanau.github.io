---

title: Procure to Pay Map
layout: default
description: A concise map of the procure-to-pay operating chain from demand to invoice and clearing.
permalink: /atlas/maps/procure-to-pay-map/
atlas_section: maps
domain: Business operations
subdomain: Procurement
concept_type: process map
sap_area: MM / FI integration
business_process: Procure to pay
status: reviewed
verified: true
last_reviewed: 2026-05-06

tags:
  - procure-to-pay
  - sap-mm
  - procurement
related: 
  - "/atlas/sap/gr-ir-clearing-explained/"
  - "/atlas/diagnostics/sap-goods-receipt-diagnostics/"
source_files: 
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/purchasing/procure-to-pay.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/mm-procurement/process-map.md"
robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1
short_title: Procure to Pay Map
h1: Procure to pay map
subtitle: A practical map for connecting procurement demand, purchasing documents, goods receipt, invoice verification, and financial clearing.
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/maps/">Maps</a></li><li aria-current="page">Procure to Pay Map</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>Procure to pay map</h1>

<p class="note-subtitle">A practical map for connecting procurement demand, purchasing documents, goods receipt, invoice verification, and financial clearing.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>Business operations</dd></div><div><dt>Type</dt><dd>process map</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Procure to pay connects business demand with supplier commitment, physical receipt, invoice verification, and payment readiness.</p>

<h2>Core flow</h2>

<ul>

<li>Demand is captured as a purchase requisition, MRP proposal, service request, or manual procurement need.</li>

<li>The purchasing process turns that demand into a purchase order or another purchasing document.</li>

<li>Goods receipt or service acceptance confirms that the supplier delivered what the business can recognize.</li>

<li>Invoice verification compares commercial, receipt, and invoice evidence before finance clears or blocks payment.</li>

</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>Where did the chain stop: requisition, order, receipt, invoice, clearing, or payment?</li>

<li>Is the issue caused by document status, master data, tolerance, approval, or finance integration?</li>

<li>Which team owns the failed control?</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a></li>

<li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods Receipt Diagnostics</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
