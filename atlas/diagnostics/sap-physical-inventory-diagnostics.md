---
layout: default
title: "SAP Physical Inventory Diagnostics"
description: "A conservative diagnostic frame for physical inventory count and adjustment issues in SAP."
permalink: /atlas/diagnostics/sap-physical-inventory-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory management
concept_type: diagnostic guide
sap_area: "MM inventory management"
business_process: Inventory / Logistics
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - inventory-management
related:
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/diagnostics/sap-movement-types-diagnostics/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Physical Inventory Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP physical inventory diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a physical count does not match system stock or why an inventory difference cannot be posted.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory / Logistics</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until physical inventory behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Physical inventory reconciles system stock with actual stock on hand. When counts do not match, differences cannot be posted, or adjustments create unexpected accounting entries, the support goal is to identify whether the issue is in the count document, the difference list, the posting period, or the stock status at the time of count.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>MI20 difference list shows items that cannot be cleared or posted.</li>
      <li>Physical count quantity differs significantly from system stock without obvious reason.</li>
      <li>Inventory difference posting fails due to period closure or authorization.</li>
      <li>Count document was created for wrong storage location or material.</li>
      <li>Adjustment posted to wrong GL account or cost center.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Movement during count:</strong> goods were received or issued after the count was entered but before the difference was posted.</li>
      <li><strong>Wrong count document:</strong> the physical inventory document was created for the wrong plant, storage location, or batch.</li>
      <li><strong>Period closed:</strong> the posting period for inventory differences is closed in MM or FI.</li>
      <li><strong>Stock status mismatch:</strong> the count included restricted or blocked stock that the system treats separately.</li>
      <li><strong>Authorization issue:</strong> the user lacks authorization to post inventory differences for the material or plant.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MI20 — difference list for the physical inventory document.</li>
      <li>MI20N — physical inventory document display.</li>
      <li>MB52 — stock overview at the time of count versus current stock.</li>
      <li>MB51 — material documents between count entry and difference posting.</li>
      <li>MMRV — posting period status.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>IKPF / ISEG</strong> — physical inventory document header and items.</li>
      <li><strong>MARD</strong> — storage location stock.</li>
      <li><strong>MKPF / MSEG</strong> — material documents.</li>
      <li><strong>BKPF / BSEG</strong> — accounting documents for inventory adjustments.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the physical inventory document number and the material with the difference.</li>
      <li>Check MI20 for the difference quantity and any blocking reason.</li>
      <li>Verify the count document was created for the correct plant, storage location, and batch.</li>
      <li>Check MB51 for any movements between count entry and difference posting.</li>
      <li>Verify the posting period is open in both MM and FI.</li>
      <li>Check the stock status (unrestricted, restricted, blocked) at the time of count.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Recount the material if movements occurred during the count process.</li>
      <li>Open the posting period temporarily if authorized, or post in the current period.</li>
      <li>Correct the count document if it was created for the wrong location or batch.</li>
      <li>Post the difference with documented approval and business justification.</li>
      <li>Investigate large unexplained differences as potential process or control issues.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Physical inventory issues are usually process timing or count accuracy problems. A useful ticket should include: inventory document number, material, plant, storage location, system stock, physical count, difference, and any movements that occurred during the count.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a physical inventory configuration guide. It does not cover cycle counting setup, WM inventory procedures, or RFID integration. It does not replace SAP's inventory management documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
