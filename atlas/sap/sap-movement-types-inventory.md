---
layout: default
title: "SAP Movement Types and Inventory"
description: "A practical guide to SAP movement types, how they control stock direction and account determination, and diagnostic questions for inventory mismatches."
permalink: /atlas/sap/sap-movement-types-inventory/
atlas_section: sap
domain: SAP operations
subdomain: Inventory management
concept_type: SAP concept
sap_area: MM inventory management / WM
business_process: Procure to pay / Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - inventory
  - movement-types
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/maps/procure-to-pay-map/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Movement Types and Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP movement types and inventory</h1>
    <p class="note-subtitle">How movement types direct stock, what the common ones mean, and where inventory mismatches start.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay / Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management / WM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>A movement type in SAP is a three-character code that tells the system what kind of goods movement is happening, which stock direction applies, and which general ledger accounts to update. It controls whether stock increases or decreases, whether the movement is valuated, and whether it creates a purchase order reference. Getting the movement type wrong is a common cause of inventory mismatches, incorrect account postings, and failed period-end close.</p>

    <h2>Key sections</h2>

    <h3>Common movement types and what they do</h3>
    <ul>
      <li><strong>101</strong> — Goods receipt for purchase order into unrestricted stock. Increases valuated stock and posts to GR/IR.</li>
      <li><strong>102</strong> — Reversal of 101. Use when a 101 was posted incorrectly; it reverses both stock and accounting.</li>
      <li><strong>103</strong> — Goods receipt for purchase order into GR blocked stock. Stock is visible but not yet valuated or available for consumption.</li>
      <li><strong>104</strong> — Reversal of 103. Removes the GR blocked stock without creating an accounting document.</li>
      <li><strong>105</strong> — Release from GR blocked stock to unrestricted. The valuated receipt happens here, not in 103.</li>
      <li><strong>261</strong> — Goods issue for order (production). Consumes stock and posts to work-in-process.</li>
      <li><strong>262</strong> — Reversal of 261. Returns stock from production order to storage.</li>
      <li><strong>301</strong> — Transfer posting plant to plant in one step. Stock leaves the issuing plant and arrives at the receiving plant in a single document.</li>
      <li><strong>303</strong> — Transfer posting plant to plant: removal from issuing plant (two-step).</li>
      <li><strong>305</strong> — Transfer posting plant to plant: receipt at receiving plant (two-step).</li>
      <li><strong>311</strong> — Transfer posting storage location to storage location within the same plant.</li>
      <li><strong>501</strong> — Receipt without purchase order. Used for initial stock load or unplanned receipts; requires careful account assignment.</li>
      <li><strong>502</strong> — Reversal of 501.</li>
    </ul>

    <h3>Account determination</h3>
    <p>Each movement type is linked to a transaction/event key (such as BSX, WRX, GBB) that drives account determination. The final G/L account depends on the valuation class, chart of accounts, and account grouping. If an account determination error appears during goods movement, check <strong>OMJJ</strong> (movement type configuration) and <strong>OBYC</strong> (account determination).</p>

    <h3>Common confusion areas</h3>
    <ul>
      <li><strong>101 vs 103+105</strong> — A user posts 103 thinking the stock is available, but it is blocked. The actual valuated receipt is 105. This creates a timing mismatch between physical stock and accounting.</li>
      <li><strong>102 vs 122</strong> — 102 reverses a 101. 122 is a return to vendor, which also reduces stock but uses a different account logic and may require a returns delivery.</li>
      <li><strong>301 vs 303+305</strong> — 301 is one-step; the stock disappears from the issuing plant immediately. 303+305 is two-step; the stock sits in transit between 303 and 305, which affects availability and reconciliation.</li>
      <li><strong>261 without production order</strong> — Posting 261 requires a valid production order. If the order is missing or closed, the goods issue fails.</li>
    </ul>

    <h3>Tables and transactions</h3>
    <ul>
      <li><strong>MSEG</strong> — material document items, including movement type, quantity, and PO reference.</li>
      <li><strong>MKPF</strong> — material document header.</li>
      <li><strong>MARD</strong> — storage location stock.</li>
      <li><strong>MB51</strong> — material document overview, the best starting point for any stock investigation.</li>
      <li><strong>MMBE</strong> — stock overview across hierarchy levels.</li>
      <li><strong>OMJJ</strong> — movement type configuration.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>When investigating an inventory mismatch, always check the movement type in <strong>MB51</strong> first. Ask: was the movement a receipt or issue, was it valuated, was it reversed, and does the PO or order reference match? Do not assume a quantity difference is a system error; it is often a process issue where the wrong movement type was selected or a two-step transfer was not completed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers standard MM movement types. It does not cover WM transfer requirements, handling unit movements, or special stock types (consignment, subcontracting, pipeline). It does not replace SAP's inventory management configuration guide.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
