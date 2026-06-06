---
layout: default
title: "SAP MM Sourcing Overview"
description: "How sourcing works in SAP MM: info records, source lists, quota arrangements, outline agreements, and common sourcing failures."
permalink: /atlas/sap/sap-mm-sourcing-overview/
atlas_section: sap
domain: SAP operations
subdomain: Procurement and sourcing
concept_type: SAP concept
sap_area: MM purchasing / sourcing
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - sourcing
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-incompletion-procedure-diagnostics/
  - /atlas/sap/gr-ir-clearing-explained/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP MM Sourcing Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP MM sourcing overview</h1>
    <p class="note-subtitle">How SAP decides which supplier to use, and why that decision sometimes fails.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing / sourcing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Sourcing in SAP MM is the set of rules and master data that determines which supplier fulfills a procurement need. It is not just about picking a vendor; it is about ensuring the chosen supplier is valid for the material, plant, and purchasing organization, and that the price and terms are agreed in advance. When sourcing fails, the symptom is usually a blocked purchase requisition or a PO that cannot be created. The root cause is almost always a gap in master data or an expired rule.</p>

    <h2>Key sections</h2>

    <h3>Info records</h3>
    <p>An info record links a material, a supplier, and a purchasing organization. It stores the last price, planned delivery time, and terms. It is optional for manual PO creation but often required for automatic sourcing.</p>
    <ul>
      <li><strong>ME11</strong> — create info record.</li>
      <li><strong>ME12</strong> — change info record.</li>
      <li><strong>ME13</strong> — display info record.</li>
      <li><strong>ME1N</strong> — list info records by material or supplier.</li>
    </ul>
    <p>Common issue: the info record exists but is not marked as <em>standard</em> or <em>pipeline</em>, or the purchasing organization in the info record does not match the PR.</p>

    <h3>Source lists</h3>
    <p>A source list defines which suppliers are valid for a material in a specific plant during a specific time period. It can be mandatory or optional depending on plant configuration.</p>
    <ul>
      <li><strong>ME01</strong> — create source list.</li>
      <li><strong>ME03</strong> — display source list.</li>
      <li><strong>ME05</strong> — generate source list from info records and outline agreements.</li>
    </ul>
    <p>Common issue: the source list has expired (valid-to date in the past), or the supplier is blocked in the source list, or no source list exists and the plant requires one.</p>

    <h3>Quota arrangements</h3>
    <p>A quota arrangement splits procurement across multiple suppliers by percentage. It is used when no single supplier should receive all the volume.</p>
    <ul>
      <li><strong>MEQ1</strong> — maintain quota arrangement.</li>
      <li><strong>MEQ4</strong> — display quota arrangement.</li>
    </ul>
    <p>Common issue: the quota arrangement does not add up to 100 percent, or one supplier has reached their quota and the system cannot assign the remainder, or the quota arrangement is not released.</p>

    <h3>Outline agreements and contracts</h3>
    <p>An outline agreement is a long-term arrangement with a supplier. A contract is a legal agreement without delivery schedules; a scheduling agreement includes delivery dates.</p>
    <ul>
      <li><strong>ME31K</strong> — create contract.</li>
      <li><strong>ME32K</strong> — change contract.</li>
      <li><strong>ME33K</strong> — display contract.</li>
      <li><strong>ME38</strong> — maintain scheduling agreement delivery schedule.</li>
    </ul>
    <p>Common issue: the contract is expired, the target quantity is exhausted, or the contract is not released. A PO referencing an invalid contract will fail or fall back to manual sourcing.</p>

    <h3>Automatic vs manual sourcing</h3>
    <p>Automatic sourcing is triggered during PR-to-PO conversion or MRP. The system searches in this order: quota arrangement, source list, info record, outline agreement. If nothing is found, the PR remains without a source or the PO must be created manually. Manual sourcing means the user selects the supplier directly in <strong>ME21N</strong> or <strong>ME51N</strong>.</p>

    <h3>Common sourcing failures</h3>
    <ul>
      <li><strong>Missing info record</strong> — the material has never been purchased from this supplier, or the info record was deleted.</li>
      <li><strong>Expired source list</strong> — the valid-to date passed and no new source list was created.</li>
      <li><strong>Blocked supplier</strong> — the supplier master has a blocking flag for the purchasing organization or company code.</li>
      <li><strong>Quota arrangement mismatch</strong> — the quota is not released, or the assigned supplier is blocked, or the quota percentages do not cover the requirement.</li>
      <li><strong>Organizational mismatch</strong> — the purchasing organization or plant in the PR does not match the sourcing master data.</li>
    </ul>

    <h3>Diagnostic questions</h3>
    <ul>
      <li>Does the material have a valid source list for this plant and time period?</li>
      <li>Is there an info record for the intended supplier and purchasing organization?</li>
      <li>Is the supplier blocked in the master data or in the source list?</li>
      <li>Does a quota arrangement exist, and is it released and valid?</li>
      <li>Is the plant configured to require a source list?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Most sourcing failures are master data issues, not system bugs. Before escalating a sourcing problem, verify the source list validity period, the info record purchasing organization, and the supplier blocking status. A quick check in <strong>ME03</strong> and <strong>ME13</strong> resolves the majority of cases.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers standard MM sourcing. It does not cover SRM supplier management, Ariba sourcing, or vendor evaluation scoring. It does not detail MRP sourcing logic or batch-specific material determination.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
