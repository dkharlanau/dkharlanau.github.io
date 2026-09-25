---
layout: default
title: "Sourcing and Procurement — SAP S/4HANA Domain"
description: "A clear overview of SAP S/4HANA Sourcing and Procurement: requirements, sources of supply, purchasing documents, receipt, invoice verification, and the link to Finance."
permalink: /atlas/sap/sourcing-and-procurement-domain/
atlas_section: sap
domain: SAP operations
subdomain: Procurement
concept_type: domain
sap_area: "MM"
business_process: "Procure to pay"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - sap-mm
  - procurement
  - procure-to-pay
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/sap/sap-mm-sourcing-overview/
  - /atlas/sap/sap-ariba/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Sourcing and Procurement Domain</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Domain</p>
    <h1>Sourcing and procurement — SAP S/4HANA domain</h1>
    <p class="note-subtitle">From an internal requirement to a supplier order, receipt, invoice, and financial handoff.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / Sourcing and Procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Procurement starts with a requirement</h2>
    <p>SAP S/4HANA Sourcing and Procurement covers the process of turning a business requirement into an order with a supplier and then recording what was received and invoiced. The familiar procure-to-pay chain often contains a purchase requisition, source-of-supply decision, purchase order, goods receipt or service entry, and supplier invoice. Payment itself belongs to Finance, but procurement supplies much of the document history and accounting context behind it.</p>

    <p>The process is deliberately document-based. A purchase requisition describes what the organization needs. A purchase order creates the purchasing commitment to the supplier. Receipt documents record that goods arrived or services were accepted. Invoice verification checks the supplier invoice against the purchasing history before the financial liability continues through Accounts Payable.</p>

    <h2>Sourcing and purchasing are related, but not the same</h2>
    <p><strong>Sourcing</strong> answers the question “where should we buy this from?” A source can come from purchasing master data and agreements such as purchasing info records, source lists, contracts, scheduling agreements, and quota arrangements. Depending on the process and configuration, SAP can propose or determine a source for a purchase requisition.</p>

    <p><strong>Purchasing</strong> turns the requirement and chosen source into a purchasing document. Not every purchase requisition has to begin with a material master, and not every purchase order follows the same path. Stock materials, consumable materials, external services, subcontracting, consignment, and stock transfers use different combinations of item categories, account assignments, receipt logic, and follow-on documents.</p>

    <h2>The main data behind the process</h2>
    <p>The supplier is represented through the Business Partner model and supplier roles. Material or product data provides purchasing and plant-specific attributes where a material master is used. Purchasing info records can hold supplier-material purchasing data and conditions. Source lists describe permitted or preferred sources for a material and plant over a validity period. Quota arrangements can distribute requirements among several sources. Contracts and scheduling agreements provide longer-term commercial frameworks.</p>

    <p>Organizational data matters just as much. Company code, plant, purchasing organization, and purchasing group describe different responsibilities in the process. A source or purchasing condition that exists in one organizational context does not automatically apply in another.</p>

    <h2>Receipt changes the process from commitment to execution</h2>
    <p>For material procurement, a goods receipt records that the ordered quantity has physically arrived and updates the relevant inventory or consumption postings. For service procurement, the process can use a service entry sheet to record and accept performed services. Quality Management or warehouse processing may add further steps when those functions are active.</p>

    <p>This is also where procurement and accounting become visibly connected. Depending on the scenario, the goods receipt can create accounting entries before the supplier invoice arrives. The GR/IR clearing account is the familiar bridge between those two events for goods-receipt-based processes.</p>

    <h2>Invoice verification closes the purchasing history, not the payment</h2>
    <p>Supplier invoice processing uses the purchase order and, where relevant, the goods receipt or service entry as references. SAP checks quantities, values, taxes, and configured tolerances. A difference does not always mean the invoice cannot be posted; depending on the tolerance and process, the invoice may be blocked for payment and require later clarification.</p>

    <p>Once the supplier invoice is posted, the procurement part of the chain has largely done its job. The payable, payment terms, and eventual payment continue in Financial Accounting. This separation is useful because “the supplier was not paid” can originate in procurement, invoice verification, workflow, master data, or payment processing — not in one single MM setting.</p>

    <h2>How the domain connects to other SAP areas</h2>
    <p>Procurement receives demand from many places: MRP, production, maintenance, projects, sales scenarios, and manual requests. It connects to Inventory Management for goods movements, EWM for warehouse execution, QM for inspections, and Finance for accounting and supplier liabilities. SAP Ariba and SAP Business Network can extend parts of sourcing, buying, supplier collaboration, and document exchange, but they are not required for the core S/4HANA purchasing process.</p>

    <h2>Where to go deeper</h2>
    <p>This page is the domain map. The detailed mechanics belong on focused pages: operational procurement, source determination, purchasing info records, quota arrangements, invoice verification, movement types, GR/IR, stock transfers, services, and SAP Ariba integration. Keeping those topics separate makes the procurement model easier to understand and keeps this overview from becoming a list of configuration objects.</p>

    <h2>Sources</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-and-procurement/outlining-a-general-procurement-process_dfbc33f8-72f1-4d30-a4cd-bd63d48d7a70">Outlining a General Procurement Process</a>.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/exploring-operational-procurement-in-sap-s-4hana/outlining-purchase-order-processing-in-sap-s-4hana">Outlining Purchase Order Processing in SAP S/4HANA</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/57c7e45776bddf12e10000000a4450e5.html">Manage Sources of Supply</a>.</li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/sap/sap-mm-sourcing-overview/">SAP MM Sourcing Overview</a></li>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
