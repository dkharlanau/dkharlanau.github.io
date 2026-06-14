---

title: Store Receiving in SAP Retail
layout: default
description: A practical explanation of store receiving as the point where retail logistics becomes sellable inventory.
permalink: /atlas/concepts/store-receiving-sap-retail/
atlas_section: concepts
domain: Retail operations
subdomain: Store operations
concept_type: business concept
sap_area: Retail / inventory management
business_process: Retail replenishment
status: reviewed
verified: true
level: 2
last_reviewed: 2026-05-06

tags:
  - retail
  - sap-sd
  - order-to-cash
related: 
  - "/atlas/diagnostics/pos-sales-not-reflected-in-sap/"
  - "/atlas/concepts/sap-stock-exists-not-promisable/"
  - "/atlas/maps/order-to-cash-map/"
  - "/atlas/data-quality/sap-master-data-quality/"
robots: index,follow
sitemap: true
short_title: Store Receiving in SAP Retail
h1: Store receiving in SAP Retail
subtitle: Store receiving is not only a goods receipt posting. It is the handoff from supply chain execution to sales-floor availability.
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/concepts/">Concepts</a></li><li aria-current="page">Store Receiving in SAP Retail</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>Store receiving in SAP Retail</h1>

<p class="note-subtitle">Store receiving is not only a goods receipt posting. It is the handoff from supply chain execution to sales-floor availability.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>Retail operations</dd></div><div><dt>Type</dt><dd>business concept</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Store receiving is the point where distribution-center or supplier delivery becomes store stock that can be counted, replenished, sold, and audited.</p>

<h2>Common issues</h2>

<ul>

<li>Goods arrive physically but are not posted in time, creating visibility gaps for replenishment and availability.</li>

<li>Discrepancies are handled informally instead of being recorded as structured evidence.</li>

<li>Store staff may receive during peak operational pressure, which increases errors and delays.</li>

</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>Has the delivery physically arrived, and is there proof of delivery?</li>

<li>Has system receipt been posted against the expected reference?</li>

<li>Were shortages, damages, overages, or wrong-store deliveries recorded in a way finance and supply chain can use?</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
<li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a></li>
<li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
