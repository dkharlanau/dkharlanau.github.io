---
layout: default
title: "SAP Quality Management Inspection Diagnostics"
description: "A conservative diagnostic frame for inspection lots, usage decisions, and results recording in SAP QM."
permalink: /atlas/diagnostics/sap-quality-management-inspection-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "QM"
business_process: Quality management
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - quality-management
related:
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Quality Management Inspection Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP quality management inspection diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why inspection lots are missing, results cannot be recorded, or usage decisions are blocked.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Quality management</dd></div>
      <div><dt>SAP area</dt><dd>QM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP Quality Management creates inspection lots from goods receipts, production orders, or manual triggers. Each lot follows a plan with characteristics, sample sizes, and inspection points. Problems usually appear as a missing lot, incomplete results, or a usage decision that cannot be posted. The diagnostic task is to trace the lot origin, the inspection plan assignment, and the stock impact.</p>
    <p>This guide covers inspection lot processing, not quality planning or quality notifications.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Goods receipt does not create an inspection lot even though quality management is active.</li>
      <li>Inspection lot is created but cannot be released for results recording.</li>
      <li>Results recording shows missing inspection characteristics or wrong sample sizes.</li>
      <li>Usage decision fails because results are incomplete or the lot is still in process.</li>
      <li>Stock remains in quality inspection status after usage decision is posted.</li>
      <li>Inspection type is not determined for the material and plant combination.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing inspection setup:</strong> the material master QM view does not have the inspection type active for the transaction.</li>
      <li><strong>Missing or incorrect inspection plan:</strong> no valid plan exists for the material and lot creation date.</li>
      <li><strong>Status mismatch:</strong> the inspection lot is not released (REL) or has an error status.</li>
      <li><strong>Incomplete results:</strong> mandatory characteristics are not valuated or the sample quantity is insufficient.</li>
      <li><strong>Stock posting block:</strong> the usage decision movement type is not allowed for the storage location or material.</li>
      <li><strong>Batch requirement:</strong> the material requires batch management but no batch was entered.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>QA03 / QA33</strong> — display inspection lots and status.</li>
      <li><strong>QE51N</strong> — results recording for inspection characteristics.</li>
      <li><strong>QA11</strong> — record usage decision and post stock.</li>
      <li><strong>MM03</strong> — material master QM view; check inspection types and settings.</li>
      <li><strong>QP03 / QP43</strong> — display inspection plan / reference operation set.</li>
      <li><strong>MMBE / MB52</strong> — stock overview including quality inspection stock.</li>
      <li><strong>MSC3N</strong> — batch master if the material is batch-managed.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>QALS</strong> — inspection lot header.</li>
      <li><strong>QAVE</strong> — usage decision data.</li>
      <li><strong>QAMR / QASR</strong> — recorded results for quantitative and qualitative characteristics.</li>
      <li><strong>PLKO / PLPO</strong> — inspection plan header and operations.</li>
      <li><strong>TQ80</strong> — inspection types per material and plant.</li>
      <li><strong>MCHA / MCHB</strong> — batch master and stock by batch.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Find the inspection lot in QA03/QA33 using the material, batch, or originating document.</li>
      <li>Check the lot status and the originating document (goods receipt or production order).</li>
      <li>Review the material master QM view in MM03 to confirm the inspection type is active.</li>
      <li>Open QP03 and verify that a valid inspection plan exists for the lot start date.</li>
      <li>Check QE51N for recorded results and any missing mandatory characteristics.</li>
      <li>Attempt QA11 and read the exact error if the usage decision fails.</li>
      <li>Check MMBE/MB52 for quality inspection stock movement after usage decision.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Activate the correct inspection type in the material master QM view.</li>
      <li>Create or extend the inspection plan to cover the lot creation period.</li>
      <li>Release the inspection lot if it is stuck in a non-released status.</li>
      <li>Record missing results in QE51N and confirm sample sizes.</li>
      <li>Post the usage decision in QA11 and verify stock movement.</li>
      <li>Enter or correct the batch number if the material is batch-managed.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the inspection lot number, material, plant, batch, inspection type, originating document, current lot status, exact error message, and whether quality inspection stock exists.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Inspection lots are not created for many materials after a goods receipt.</li>
      <li>Usage decisions fail for an entire inspection type or plant.</li>
      <li>Stock remains stuck in quality inspection and blocks goods issue or production.</li>
      <li>Inspection plan assignment is inconsistent across plants.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for inspection lot processing, not a guide to quality planning, calibration, or quality notifications. It does not cover external quality systems or LIMS integration.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
