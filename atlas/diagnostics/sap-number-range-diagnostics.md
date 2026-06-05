---
layout: default
title: "SAP Number Range Diagnostics"
description: "A conservative diagnostic frame for number range issues in SAP document and master data creation."
permalink: /atlas/diagnostics/sap-number-range-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "Number ranges / document creation"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-basis
  - diagnostics
  - number-ranges
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
  - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Number Range Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP number range diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a document or master data object cannot be created due to number range problems.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Number ranges / document creation</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until number range behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Number ranges in SAP control how documents and master data objects are numbered. When a number range is exhausted, misconfigured, or conflicts with another system, creation fails or produces duplicates. The support goal is to identify which number range object is affected, whether the issue is exhaustion, overlap, external vs. internal numbering mismatch, or transport-related misconfiguration.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Document or master data creation fails with 'number range exceeded' or similar error.</li>
      <li>Object is created with a number that does not match the expected range or format.</li>
      <li>Number range status shows the current number is at or above the maximum.</li>
      <li>Different systems use overlapping number ranges, causing duplicates in consolidation.</li>
      <li>Transport of number range configuration creates inconsistency between systems.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Range exhausted:</strong> the current number has reached the maximum defined for the range.</li>
      <li><strong>External vs. internal mismatch:</strong> the number range is set to external but the program tries to assign internal numbers, or vice versa.</li>
      <li><strong>Overlapping ranges:</strong> two number range intervals cover the same numbers, causing collisions.</li>
      <li><strong>Transport inconsistency:</strong> the number range was changed in development but the transport did not update the current number in production correctly.</li>
      <li><strong>Buffering issue:</strong> buffered number ranges in a multi-application-server landscape may skip numbers or cause gaps.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>SNRO — number range object display and status.</li>
      <li>SNUM — number range maintenance (if authorized).</li>
      <li>SPRO — number range configuration for the specific application area.</li>
      <li>SE16 — NRIV table for number range interval details.</li>
      <li>ST22 — short dumps if number range errors cause program termination.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>NRIV</strong> — number range intervals.</li>
      <li><strong>NRLOAD</strong> — number range buffering status.</li>
      <li><strong>TNRO</strong> — number range object definitions.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the document type, object type, or transaction where the number range error occurs.</li>
      <li>Check the error message for the number range object name (e.g., RF_BELEG, KUNNR, LIFNR).</li>
      <li>Check SNRO or NRIV for the current number and the interval maximum.</li>
      <li>Verify if the range is internal or external and if the creation program matches.</li>
      <li>Check for overlapping intervals or multiple intervals for the same object.</li>
      <li>If the issue appeared after a transport, compare number range configuration across systems.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Extend the number range interval if it is exhausted.</li>
      <li>Switch the range to external or internal to match the creation program's expectation.</li>
      <li>Remove or adjust overlapping intervals.</li>
      <li>If duplicates exist due to overlap, evaluate renumbering or consolidation with master data governance.</li>
      <li>Adjust buffering settings if gaps or skips are unacceptable.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Number range issues are usually configuration or exhaustion problems. A useful ticket should include: number range object name, document type or object type, error message, current number, interval maximum, and whether the issue is new or recurring after a transport.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a number range configuration guide. It does not cover number range design, buffering strategy, or transport management. It does not replace SAP's number range documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
