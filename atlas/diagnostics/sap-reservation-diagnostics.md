---
layout: default
title: "SAP Reservation Diagnostics"
description: "A conservative diagnostic frame for reservation issues in SAP inventory management."
permalink: /atlas/diagnostics/sap-reservation-diagnostics/
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
    <li aria-current="page">SAP Reservation Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP reservation diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a reservation cannot be created, consumes wrong stock, or blocks MRP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory / Logistics</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until reservation behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Reservations in SAP hold stock for a specific purpose — production, maintenance, sales, or transfer. When a reservation cannot be created, does not consume the expected stock, or creates MRP noise, the support goal is to identify whether the issue is in the reservation type, movement allowed settings, account assignment, or stock availability.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>MB25 or MB1A fails to create a reservation due to missing data or authorization.</li>
      <li>Reservation was created but goods issue against it fails with 'no stock available'.</li>
      <li>MRP shows reserved stock that does not match the actual reservation.</li>
      <li>Reservation was deleted but stock remains reserved in MRP.</li>
      <li>Wrong movement type or account assignment is used when posting against a reservation.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Wrong reservation type:</strong> the reservation type does not allow the intended movement or account assignment.</li>
      <li><strong>Movement not allowed:</strong> the reservation type restricts which movement types can be posted against it.</li>
      <li><strong>Stock not available:</strong> the reserved material is not in unrestricted stock or is already consumed by another reservation.</li>
      <li><strong>Account assignment mismatch:</strong> the reservation account assignment differs from the goods issue or receiving document.</li>
      <li><strong>Plant / storage location mismatch:</strong> the reservation was created for one location but the goods issue is attempted from another.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MB25 — reservation display.</li>
      <li>MB1A — goods issue with reference to reservation.</li>
      <li>MMBE — stock overview across plants and storage locations.</li>
      <li>MD04 / MD05 — MRP list to see reservation impact on planning.</li>
      <li>MB51 — material documents posted against the reservation.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>RESB</strong> — reservation items.</li>
      <li><strong>RKPF</strong> — reservation header.</li>
      <li><strong>MARD</strong> — storage location stock.</li>
      <li><strong>MKPF / MSEG</strong> — material documents.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the reservation number and the exact error during creation or goods issue.</li>
      <li>Check MB25 for reservation details: material, plant, storage location, quantity, movement allowed, and account assignment.</li>
      <li>Verify stock availability in MMBE or MB52 for the reserved material and location.</li>
      <li>Check if the movement type used in goods issue is allowed for the reservation type.</li>
      <li>Compare account assignment between reservation and goods issue document.</li>
      <li>Check MD04 to see if the reservation is correctly reflected in MRP.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create the reservation with the correct type that allows the intended movement.</li>
      <li>Transfer stock to the correct storage location if the reservation was created for the wrong location.</li>
      <li>Adjust the reservation quantity if the original request was overstated.</li>
      <li>Delete and recreate the reservation if it was created with wrong parameters and no goods movements were posted.</li>
      <li>If MRP shows stale reservation data, run MRP refresh or check for orphaned reservation records.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Reservation issues are usually master data or stock availability problems. A useful ticket should include: reservation number, material, plant, storage location, expected quantity, available stock, movement type, and the exact error message.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a reservation configuration guide. It does not cover reservation type setup, WM reservation integration, or batch reservation logic. It does not replace SAP's inventory management documentation.</p>

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
