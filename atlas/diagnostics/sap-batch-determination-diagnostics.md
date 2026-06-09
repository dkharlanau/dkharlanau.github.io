---
layout: default
title: "SAP Batch Determination Diagnostics"
description: "Diagnostic guide for SAP batch determination failures, batch search strategy issues, and batch status blockers in MM, SD, and WM."
permalink: /atlas/diagnostics/sap-batch-determination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory and batch management
concept_type: diagnostic guide
sap_area: "MM / SD / WM batch management"
business_process: Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - batch-management
  - sap-mm
  - sap-sd
  - sap-wm
  - diagnostics
  - inventory
related:
  - /atlas/diagnostics/sap-movement-types-diagnostics/
  - /atlas/diagnostics/sap-stock-transfer-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/diagnostics/sap-physical-inventory-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Batch Determination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP batch determination diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why batch determination fails, returns the wrong batch, or cannot find a valid batch in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / SD / WM batch management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until batch determination behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Batch determination in SAP selects a batch based on classification, shelf-life expiration date (SLED), stock status, and search strategy. When batch determination fails, the issue is usually in the batch search procedure, the batch classification, the stock availability, or the material master batch settings. The diagnostic task is to isolate whether the problem is configuration, master data, stock data, or classification.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>System message "No batch could be determined" during goods issue, sales order, or delivery.</li>
      <li>Batch determination finds a batch, but it is the wrong one (not FIFO, not the oldest, not the required quality grade).</li>
      <li>Batch is determined in the sales order but not in the delivery, or vice versa.</li>
      <li>Batch determination works in one plant but fails in another for the same material.</li>
      <li>Batch status is restricted or blocked, preventing selection even though stock exists.</li>
      <li>SLED or expiration date is past due, and the batch is excluded from selection.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing batch search procedure:</strong> the material does not have a valid batch search procedure assigned, or the procedure has no condition table entries.</li>
      <li><strong>Classification mismatch:</strong> the batch class or characteristic values do not match the selection criteria in the batch search strategy.</li>
      <li><strong>Stock type or status block:</strong> the batch is in quality inspection, blocked, or restricted status and cannot be selected for the movement type.</li>
      <li><strong>SLED / expiration date exclusion:</strong> the batch is past its expiration date or the remaining shelf life does not meet the minimum requirement.</li>
      <li><strong>Plant or storage location mismatch:</strong> the batch exists but not in the required plant or storage location.</li>
      <li><strong>Batch management not active:</strong> the material master does not have batch management enabled at the required level (plant, client).</li>
      <li><strong>Search strategy sort rule:</strong> the sort rule in the search procedure does not match the intended selection logic (e.g., FIFO vs. LIFO).</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>MM03</strong> — material master, "Plant data / stor. 1" and "Plant data / stor. 2" views: check batch management indicator and batch search procedure.</li>
      <li><strong>MSC1N / MSC2N / MSC3N</strong> — batch master data; check batch status, SLED, classification, and stock overview.</li>
      <li><strong>MMBE</strong> — stock overview by batch, plant, and storage location.</li>
      <li><strong>CL30N</strong> — batch classification display; verify characteristic values and class assignment.</li>
      <li><strong>CT04</strong> — characteristic definitions; check value types and allowed values.</li>
      <li><strong>VCH1 / VCH2</strong> — batch search strategy (condition records); verify the strategy type, sort sequence, and selection criteria.</li>
      <li><strong>CO09</strong> — stock availability overview; check whether the batch is available or reserved.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>MCHA / MCHB</strong> — batch stocks at plant and storage location level.</li>
      <li><strong>KSSK / AUSP</strong> — classification and characteristic values for batches.</li>
      <li><strong>T156</strong> — movement types; check if the movement type allows batch determination.</li>
      <li><strong>T459A / T459B / T459C</strong> — batch search procedure and strategy tables.</li>
      <li><strong>MARA-XCHPF</strong> — batch management indicator in material master.</li>
      <li><strong>CHV1 / CHV2 / CHV3</strong> — batch search strategy condition tables.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the material has batch management active in MM03 (plant level or client level, depending on configuration).</li>
      <li>Check the batch search procedure assigned to the material and the movement type.</li>
      <li>Verify that a batch search strategy (condition record) exists in VCH1 for the relevant combination (material, plant, movement type).</li>
      <li>Check batch stock in MMBE or MSC3N: does a valid batch exist in the required plant and storage location?</li>
      <li>Check batch status in MSC3N: is the batch restricted, in quality inspection, or blocked?</li>
      <li>Check SLED and expiration dates: is the batch still within the required shelf-life window?</li>
      <li>Check batch classification in CL30N: do the characteristic values match the search strategy selection criteria?</li>
      <li>If the wrong batch is selected, review the sort rule and selection class in the search strategy.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or update the batch search strategy (condition record) in VCH1 for the material and plant.</li>
      <li>Correct batch classification values (characteristics) in MSC2N or CL20N to match the selection criteria.</li>
      <li>Change batch status from restricted to unrestricted in MSC2N if quality inspection is complete.</li>
      <li>Extend the material master batch management indicator to the plant if missing.</li>
      <li>Adjust the sort rule in the batch search procedure to match business requirements (FIFO, FEFO, etc.).</li>
      <li>If the batch is expired, initiate goods movement to scrap or blocked stock, or update SLED if the date was entered incorrectly.</li>
      <li>Escalate to the warehouse or quality team if batch status decisions are business-driven, not master data issues.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Batch determination failures are usually master data or configuration issues, not system errors. A useful ticket should include: material number, plant, storage location, movement type, exact error message, whether batch management is active, and the expected versus actual batch selection.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a batch management configuration guide. It does not cover batch-specific unit of measure, batch where-used lists, or hazardous material batch management. It does not replace SAP's batch management documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">SAP Stock Transfer Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-physical-inventory-diagnostics/">SAP Physical Inventory Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
