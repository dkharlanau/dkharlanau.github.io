---
layout: default
title: "SAP Movement Types Diagnostics"
description: "A conservative diagnostic frame for movement type issues in SAP inventory management."
permalink: /atlas/diagnostics/sap-movement-types-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory management
concept_type: diagnostic guide
sap_area: "MM inventory management"
business_process: Procure to pay / Inventory
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
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Movement Types Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP movement types diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a goods movement posts to the wrong stock type, account, or status.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay / Inventory</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until movement type behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Movement types in SAP define the direction, stock type, and accounting impact of every goods movement. A wrong movement type does not just misclassify stock — it can post to the wrong account, trigger wrong valuation, create incorrect GR/IR records, or leave inventory in an unusable status. The support goal is to identify which movement type was used, whether it matches the business intent, and what correction is needed.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Goods receipt posted stock to quality inspection instead of unrestricted.</li>
      <li>Transfer posting created an unexpected accounting entry.</li>
      <li>Return to vendor did not reduce GR/IR or created a wrong reversal.</li>
      <li>Movement type is not allowed for the material type or plant.</li>
      <li>Inventory count adjustment posted to a consumption account instead of inventory.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Wrong movement type selected:</strong> user chose 101 instead of 103, or 311 instead of 301, changing stock type or valuation.</li>
      <li><strong>Movement type not configured for material type:</strong> the material type restricts which movements are allowed.</li>
      <li><strong>Account modification mismatch:</strong> the movement type posts to a G/L account that does not match the material's valuation class.</li>
      <li><strong>Stock type confusion:</strong> unrestricted, quality inspection, blocked, or in transit were not distinguished correctly.</li>
      <li><strong>Custom movement type:</strong> a landscape-specific movement type behaves differently from standard and is not documented.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MIGO — display the material document and check the movement type on each item.</li>
      <li>MB51 — material documents list, filter by movement type and material.</li>
      <li>OMJJ — movement type configuration (transaction-dependent, view-only in production).</li>
      <li>MB52 — stock overview showing stock types per storage location.</li>
      <li>Material master — check material type and valuation class.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>T156</strong> — movement types.</li>
      <li><strong>T156T</strong> — movement type texts.</li>
      <li><strong>MKPF</strong> — material document header.</li>
      <li><strong>MSEG</strong> — material document items.</li>
      <li><strong>MBEW</strong> — material valuation.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the material document number and item from the user report or error.</li>
      <li>Check MIGO or MB51 for the movement type used and compare with the business intent.</li>
      <li>Verify the stock type before and after the movement in MB52.</li>
      <li>Check if the movement type is allowed for the material type and plant.</li>
      <li>Review the accounting document (FI) to see if the G/L accounts match expectations.</li>
      <li>Determine if the movement should be reversed and re-posted with the correct type.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Reverse the incorrect movement with the reversal movement type and re-post correctly.</li>
      <li>Update user training or MIGO defaults to prevent repeated wrong selection.</li>
      <li>If the movement type configuration is wrong, escalate to the configuration team with documented evidence.</li>
      <li>For stock type issues, perform a transfer posting to move stock to the correct status.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Movement type errors are often user selection issues, not system bugs. Before escalating, collect the material document number, the movement type used, the expected movement type, the material, plant, and storage location. A useful movement type ticket should show the business intent and the system result.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a movement type configuration guide. It does not cover custom movement type design, WM movement types, or EWM-specific logic. It does not replace SAP's inventory management documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-batch-determination-diagnostics/">SAP Batch Determination Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
