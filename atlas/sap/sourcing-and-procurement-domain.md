---
layout: default
title: "Sourcing and Procurement — SAP S/4HANA Domain"
description: "Analytical overview of the Sourcing and Procurement domain in SAP S/4HANA: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sourcing-and-procurement-domain/
atlas_section: sap
domain: SAP operations
subdomain: Procurement
concept_type: domain
sap_area: "MM"
business_process: "Procure to pay"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-mm
  - procurement
  - procure-to-pay
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/sap/sap-ariba/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/diagnostics/sap-incompletion-procedure-diagnostics/
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
    <p class="note-subtitle">Purchasing, contracts, supplier management, goods receipt, and invoice verification.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>The Sourcing and Procurement domain in S/4HANA covers the supply side: purchasing, supplier management, contracts, request for quotation, purchase orders, goods receipt, invoice verification, and GR/IR clearing. It is the supply-side anchor of the procure-to-pay process.</p>

    <h2>Business purpose</h2>
    <p>Source materials and services, negotiate and manage contracts, create purchase orders, receive goods, verify invoices, and clear liabilities. The domain ensures the right material arrives at the right time, quantity, and price.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Upstream: demand from production (component requirements), MRP, or manual requisitions. Downstream: warehousing (goods receipt), finance (invoice posting, GR/IR clearing), and quality (inspection). Cross-domain: sales (third-party orders, drop-ship), project systems (project procurement).</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Vendor master / business partner (ordering address, invoicing party).</li>
      <li>Material master (purchasing views, valuation, source list).</li>
      <li>Purchasing documents: requisition, RFQ, quotation, purchase order, contract, scheduling agreement.</li>
      <li>Goods receipt: material document, stock update, quality inspection lot.</li>
      <li>Invoice receipt: invoice document, GR/IR posting, tax.</li>
      <li>GR/IR clearing: matching goods receipt to invoice, clearing differences.</li>
      <li>Source list, quota arrangement, info record, outline agreement.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>PP/PM: component demand, maintenance spare parts.</li>
      <li>WM/EWM: goods receipt putaway, warehouse tasks.</li>
      <li>QM: inspection on receipt, usage decision.</li>
      <li>FI: invoice posting, GR/IR account, tax, payment.</li>
      <li>External: Ariba (sourcing, supplier collaboration), EDI (ORDERS, INVOIC).</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>BAdIs in purchase order processing and release strategy.</li>
      <li>Custom source determination logic.</li>
      <li>RAP extensions for purchasing objects.</li>
      <li>Side-by-side supplier collaboration apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>GR/IR clearing account balance — open items and aging.</li>
      <li>Purchase order acknowledgment tracking — expected vs. confirmed delivery.</li>
      <li>Invoice verification backlog — parked, blocked, or unprocessed invoices.</li>
      <li>Source list and quota arrangement validity.</li>
      <li>Vendor evaluation scores and delivery performance.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Deep integration between purchasing, inventory, and finance.</li>
      <li>Flexible procurement types: standard, subcontracting, consignment, pipeline.</li>
      <li>GR/IR clearing provides a clear audit trail for received-not-invoiced.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>GR/IR clearing errors are persistent and hard to resolve at scale.</li>
      <li>Release strategy and approval workflows are release-specific.</li>
      <li>Invoice verification with multiple account assignments is error-prone.</li>
      <li>Vendor master data quality directly impacts procurement accuracy.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>GR/IR mismatch — quantity or price difference between receipt and invoice.</li>
      <li>Purchase order blocked — release strategy, budget, or incompletion.</li>
      <li>Wrong vendor selected — source list, info record, or quota arrangement.</li>
      <li>Goods receipt blocked — inspection lot or warehouse task issue.</li>
      <li>Invoice parked — tax code, account assignment, or PO reference mismatch.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Object names, transaction codes, and configuration paths may vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
