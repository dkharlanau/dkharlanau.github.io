---
title: SAP Stock Exists but Is Not Promisable
layout: default
description: Why SAP stock visibility can differ from what can be promised to a customer or channel.
permalink: /atlas/concepts/sap-stock-exists-not-promisable/
atlas_section: concepts
domain: SAP operations
subdomain: Availability and fulfillment
concept_type: business concept
sap_area: ATP / availability / stock status
business_process: Order to cash
status: reviewed
verified: true
last_reviewed: 2026-05-06
related: 
  - "/atlas/concepts/sap-atp-is-not-inventory/"
  - "/atlas/concepts/order-to-cash/"
  - "/atlas/diagnostics/sap-sales-order-block-diagnosis/"
source_files: 
  - "private-source/kb-drafts/sap-domain-atlas/domains/retail/troubleshooting/stock-exists-but-not-promisable.md"
  - "private-source/kb-drafts/sap-domain-atlas/domains/sales/concepts/atp.md"
robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1
short_title: Stock Exists but Is Not Promisable
h1: SAP stock exists, but it is not always promisable
subtitle: A practical explanation of why visible stock can still fail availability, ATP, allocation, or channel commitment checks.
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/concepts/">Concepts</a></li><li aria-current="page">Stock Exists but Is Not Promisable</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP stock exists, but it is not always promisable</h1>

<p class="note-subtitle">A practical explanation of why visible stock can still fail availability, ATP, allocation, or channel commitment checks.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>business concept</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>This page sits between inventory reporting and customer commitment. It is useful when business users say stock is visible in one place, but an order, store channel, or online promise still cannot use it.</p>

<h2>Common issues</h2>

<ul>

<li>Stock is in the wrong plant, storage location, channel, or stock type for the process being checked.</li>

<li>Stock is physically present but already committed, reserved, blocked, or not included in the relevant availability logic.</li>

<li>Retail, e-commerce, and distribution channels may apply allocation or promise rules that differ from simple unrestricted stock visibility.</li>

</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>Which stock figure is the user looking at, and which process is trying to consume or promise it?</li>

<li>Is the stock unrestricted, relevant to the checked location, and available on the requested date?</li>

<li>Is another document, allocation rule, or protection rule already consuming the quantity?</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>

<li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>

<li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">Sales Order Block Diagnosis</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
