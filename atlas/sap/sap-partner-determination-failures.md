---
title: SAP Partner Determination in Sales
layout: default
description: How SAP Sales partner determination connects partner functions, customer master data, document procedures, and header or item partners.
permalink: /atlas/sap/sap-partner-determination-failures/
atlas_section: sap
domain: SAP operations
subdomain: Sales master data
concept_type: SAP concept
sap_area: SD partner determination
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-09-22
tags:
  - order-to-cash
  - sap-sd
  - master-data
  - diagnostics
related:
  - "/atlas/concepts/order-to-cash/"
  - "/atlas/diagnostics/sap-sales-order-block-diagnosis/"
  - "/atlas/diagnostics/sap-bp-relationship-diagnostics/"
  - "/atlas/diagnostics/sap-customer-master-replication-diagnostics/"
robots: noindex,follow
short_title: Partner Determination in Sales
h1: SAP partner determination in Sales
subtitle: Sold-to, ship-to, bill-to, and payer are document roles. Partner determination decides which roles are required and where their partners come from.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li><li aria-current="page">Partner Determination in Sales</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
<p class="eyebrow">Knowledge Atlas</p>
<h1>SAP partner determination in Sales</h1>
<p class="note-subtitle">Sold-to, ship-to, bill-to, and payer are document roles. Partner determination decides which roles are required and where their partners come from.</p>
<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>SAP concept</dd></div><div><dt>Reviewed</dt><dd>2026-09-22</dd></div></dl></aside>

<div class="note-body">
<h2>A partner function is a role in the transaction</h2>
<p>One customer can play several roles in a sales process, or several business partners can divide those roles between them. The party that orders the goods can be different from the party that receives them, receives the invoice, or pays it. SAP represents those responsibilities through <strong>partner functions</strong> such as sold-to, ship-to, bill-to, and payer.</p>

<p>This distinction is more than naming. The ship-to partner can influence delivery address and logistics data; the payer matters for payment-related processing; the bill-to party is relevant to invoicing. A missing or unexpected partner can therefore surface later as a delivery, billing, output, pricing, or credit-processing problem even though the original cause is partner data.</p>

<h2>The procedure defines which roles belong in the document</h2>
<p>A <strong>partner determination procedure</strong> groups the partner functions that are relevant for a business object. In Sales, procedures can be assigned to contexts such as customer master records, sales document types, billing documents, or item categories. The procedure can define whether a partner function is mandatory and whether users are allowed to change it in the document.</p>

<p>So when a partner is missing, we separate two questions. First: should this partner function exist in this document at all? That is a procedure/configuration question. Second: if the function belongs here, which partner should fill it? That is usually a master-data and determination question.</p>

<h2>Customer master data supplies the normal relationship</h2>
<p>SAP documentation describes partner relationships as being maintained in customer master data and then proposed into sales documents. In the common case, the sold-to party has the related ship-to, bill-to, and payer partners maintained for the relevant sales context. When the sales document is created, those relationships are copied into the document header according to partner determination.</p>

<p>The document can then have its own partner state. Depending on configuration, a user may change a proposed partner, and partners can also exist at item level. This is why checking only today's master data does not always explain an old sales order: the document contains the partner data that was determined or changed in its own processing history.</p>

<h2>Do not confuse SD partner functions with every BP relationship</h2>
<p>In S/4HANA, Business Partner is the central master-data object, but a generic BP relationship is not automatically the same thing as an SD partner function in a sales document. The Sales process still needs the relevant customer/sales-area data and partner-determination setup. A BP can exist and still fail to appear as the expected ship-to or payer if the Sales-specific partner data does not support that role.</p>

<p>This distinction is especially useful in replication and migration issues. “The BP exists” proves identity, not that the full Sales relationship needed by the document was maintained correctly.</p>

<h2>Read a failure from the role backwards</h2>
<p>When a sales document contains the wrong partner, we begin with the affected function: ship-to, payer, bill-to, or another role. Then we check whether that function is expected in the document procedure, whether the intended partner is valid for that role and sales context, and whether the document inherited, copied, or manually changed the value.</p>

<p>A good explanation sounds like this: “The order requires a ship-to partner, but the sold-to customer did not provide the expected ship-to relationship for this sales area,” or “The correct payer exists in master data, but the document already contains a manually changed payer.” That tells us which layer owns the correction.</p>

<h2>Sources</h2>
<ul>
  <li><a href="https://help.sap.com/docs/SAP_ERP/72b431fb78a649da9c8b46951e64fb88/0271bd534f22b44ce10000000a174cb4.html">SAP Help: Partner Determination in Sales and Distribution</a></li>
  <li><a href="https://help.sap.com/docs/SAP_ERP_SPV/a428aae377ba4a1199c3ecc8b7f5f33d/0e71bd534f22b44ce10000000a174cb4.html">SAP Help: Partner Determination Procedure</a></li>
  <li><a href="https://help.sap.com/docs/SAP_ERP/248c3cdd7e6548999a7f5b95118f4522/806fbd534f22b44ce10000000a174cb4.html">SAP Help: Partner Functions</a></li>
</ul>
</div>

<section class="atlas-related"><h2>Related pages</h2><ul>
<li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
<li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">Sales Order Block Diagnosis</a></li>
<li><a href="/atlas/diagnostics/sap-bp-relationship-diagnostics/">SAP BP Relationship Diagnostics</a></li>
<li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
