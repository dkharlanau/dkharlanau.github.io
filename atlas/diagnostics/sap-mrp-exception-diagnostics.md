---
layout: default
title: "SAP MRP Exception Diagnostics"
description: "Diagnostic guide for SAP MRP exception messages, planning run failures, and material availability issues in production and procurement planning."
permalink: /atlas/diagnostics/sap-mrp-exception-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Planning and MRP
concept_type: diagnostic guide
sap_area: "MM / PP MRP"
business_process: Material requirements planning
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - mrp
  - sap-mm
  - sap-pp
  - planning
  - diagnostics
related:
  - /atlas/diagnostics/sap-purchase-requisition-diagnostics/
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-reservation-diagnostics/
  - /atlas/diagnostics/sap-stock-transfer-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP MRP Exception Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP MRP exception diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why MRP produces exception messages, why planned orders or purchase requisitions are not created, or why a material appears overstocked or short.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Material requirements planning</dd></div>
      <div><dt>SAP area</dt><dd>MM / PP MRP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until MRP behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>MRP in SAP calculates material requirements based on demand, supply, lot size, and planning parameters. Exception messages indicate where the plan deviates from the target stock level or where action is required. When MRP produces unexpected results — no planned order, excessive order quantity, or incorrect timing — the issue is usually in the material master planning data, batch size, procurement type, or BOM/routing data. The diagnostic task is to map the exception message to the planning parameter that caused it.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>MRP exception message 07, 10, or 20: material is short, but no planned order or PR was created.</li>
      <li>MRP exception message 01, 02, or 03: new planned order or PR created, but quantity or date seems wrong.</li>
      <li>MRP exception message 25 or 30: excess stock or order start date in the past.</li>
      <li>MRP list (MD05) shows no exceptions, but the material is clearly out of stock.</li>
      <li>Planned order exists but cannot be converted to a production order or purchase requisition.</li>
      <li>MRP run completes with errors for specific materials or plants.</li>
      <li>Procurement proposal is created with a vendor or plant that is incorrect or blocked.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>MRP type misconfiguration:</strong> the material has MRP type ND (no planning), PD (MRP), or VB (manual reorder point) that does not match the business process.</li>
      <li><strong>Lot size setting:</strong> lot size EX (lot-for-lot), FX (fixed lot size), or WB (weekly lot size) produces quantities that do not match demand patterns.</li>
      <li><strong>Procurement type mismatch:</strong> procurement type E (in-house production) vs. F (external procurement) determines whether MRP creates a planned order or a purchase requisition.</li>
      <li><strong>BOM or routing issue:</strong> for in-house production, missing or incorrect BOM/routing stops planned order creation or causes quantity errors.</li>
      <li><strong>Planning time fence:</strong> the requirement date falls within the planning time fence, so MRP does not create a proposal.</li>
      <li><strong>Batch input or selection issue:</strong> the MRP run was executed with a variant that excluded the material or plant.</li>
      <li><strong>Special procurement type:</strong> consignment, subcontracting, or pipeline material requires a special procurement type that is missing or incorrect.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>MD04 / MD05 / MD06 / MD07</strong> — MRP list and stock/requirements list; check exception messages and planning results.</li>
      <li><strong>MD61 / MD62 / MD63</strong> — planned independent requirements; verify demand inputs to MRP.</li>
      <li><strong>MD02 / MD03</strong> — single-item MRP run; execute interactively to see live error messages.</li>
      <li><strong>MM03</strong> — material master, MRP views (1, 2, 3, 4); check MRP type, lot size, procurement type, planning time fence, safety stock.</li>
      <li><strong>CS03</strong> — BOM display; verify component assignment and quantities for in-house production.</li>
      <li><strong>CA03</strong> — routing display; verify operation sequences and work centers.</li>
      <li><strong>ME53N</strong> — purchase requisition details if MRP created a PR.</li>
      <li><strong>MD14 / MD15</strong> — planned order details; check conversion status and error messages.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>MARC</strong> — plant-specific material data (MRP type, lot size, procurement type, special procurement).</li>
      <li><strong>MDKP / MDVM / MDVL</strong> — MRP header and item data for planned orders and purchase requisitions.</li>
      <li><strong>RESB</strong> — reservation/dependent requirements from BOM explosion.</li>
      <li><strong>PLAF</strong> — planned orders.</li>
      <li><strong>EBAN</strong> — purchase requisitions created by MRP.</li>
      <li><strong>T438A / T438B</strong> — MRP exception message definitions and groupings.</li>
      <li><strong>STKO / STPO</strong> — BOM header and items.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material, plant, and MRP area from the exception message or user report.</li>
      <li>Check MD04/MD05 for the exception message text and the supply/demand situation.</li>
      <li>Verify the material master MRP views in MM03: MRP type, lot size, procurement type, safety stock, reorder point.</li>
      <li>If the material is in-house produced, check CS03 for BOM validity and CA03 for routing validity.</li>
      <li>Check if the requirement date falls within the planning time fence (MRP view 3).</li>
      <li>Run MD02 for the single material to capture any live error messages during planning.</li>
      <li>Check MD14/ME53N for existing planned orders or PRs that may be blocking new proposals.</li>
      <li>Verify the MRP run variant and selection criteria if the issue affects multiple materials.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Change the MRP type from ND to PD or VB if the material should be planned.</li>
      <li>Adjust the lot size or rounding value to better match demand and supply constraints.</li>
      <li>Correct the procurement type (E vs. F) or special procurement type in the material master.</li>
      <li>Update or create the BOM and routing for in-house production materials.</li>
      <li>Reduce the planning time fence if urgent requirements are being excluded.</li>
      <li>Convert planned orders to production orders (CO40) or purchase requisitions (ME59N) as appropriate.</li>
      <li>Escalate to the planning or production team if the issue is demand forecast accuracy or capacity constraints.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>MRP exceptions are planning parameter issues, not system bugs. A useful ticket should include: material number, plant, MRP area, exception message number, expected versus actual planning result, and confirmation that the material master MRP views are maintained.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an MRP configuration guide. It does not cover capacity planning, S&OP, IBP integration, or detailed BOM/routing design. It does not replace SAP's MRP documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-requisition-diagnostics/">SAP Purchase Requisition Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-reservation-diagnostics/">SAP Reservation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">SAP Stock Transfer Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
