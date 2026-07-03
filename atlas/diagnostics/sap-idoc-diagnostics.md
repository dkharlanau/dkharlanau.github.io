---
layout: default
title: SAP IDoc Diagnostics
description: Diagnose SAP IDoc failures through status history, partner profiles,
  ports, segments, application validation, and RFC queue evidence.
permalink: /atlas/diagnostics/sap-idoc-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: IDoc / ALE
business_process: Cross-system integration
status: reviewed
verified: true
level: 2
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- sap-ams
- idoc
- ale
- integration
- diagnostics
related:
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
- /atlas/diagnostics/sap-inbound-processing-diagnostics/
- /atlas/diagnostics/sap-outbound-processing-diagnostics/
- /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP IDoc Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP IDoc diagnostics</h1>
    <p class="note-subtitle">Trace IDoc failures from creation through partner profile to final posting status.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-system integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
          <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>IDocs fail at four points: creation, dispatch, receipt, and application posting. The status monitor shows the last failure, but the first error status in the history usually points to the real cause. The diagnostic job is to read the history from oldest to newest and trace the first error to partner profile, port, segment, or application validation.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Expected business document was not created from an inbound IDoc.</li>
      <li>Outbound IDoc was not sent to the partner system.</li>
      <li>IDoc shows status 51, 56, or 62 in the status monitor.</li>
      <li>IDoc was sent but the receiving system reports a format error.</li>
      <li>Duplicate IDocs create duplicate business documents.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Partner profile missing:</strong> the logical system or partner is not configured for the message type.</li>
      <li><strong>Port issue:</strong> RFC or file port used by the IDoc is unavailable.</li>
      <li><strong>Segment error:</strong> mandatory segment is missing or a value violates the IDoc type definition.</li>
      <li><strong>Application posting error:</strong> the IDoc arrived correctly but the business document failed validation.</li>
      <li><strong>Queue issue:</strong> qRFC queue is stuck and prevents sequential processing.</li>
      <li><strong>Duplicate IDoc:</strong> same message was resent and processed twice.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE02 / WE05 — IDoc status monitor.</li>
      <li>WE20 — partner profiles.</li>
      <li>WE21 — port definitions.</li>
      <li>BD87 — IDoc reprocessing.</li>
      <li>SM58 — asynchronous RFC errors.</li>
      <li>SMQ1 / SMQ2 — qRFC outbound and inbound queues.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC</strong> — IDoc control record.</li>
      <li><strong>EDIDD</strong> — IDoc data segments.</li>
      <li><strong>EDIDS</strong> — IDoc status records.</li>
      <li><strong>EDPP1 / EDP13</strong> — partner profile message control.</li>
      <li><strong>TBDLS</strong> — logical systems.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Find the IDoc number from the business document reference or message trace.</li>
      <li>Open WE02/WE05 and review the status history from creation to final status.</li>
      <li>Identify the first error status and its text.</li>
      <li>For outbound errors, check partner profile, port, and RFC destination.</li>
      <li>For inbound errors, check segment data, business document validation, and queue status.</li>
      <li>Fix the root cause before reprocessing.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Maintain the missing partner profile or message type assignment.</li>
      <li>Restore the RFC or file port used for transmission.</li>
      <li>Correct segment values or mapping in the sending system.</li>
      <li>Fix the underlying business document validation error and reprocess.</li>
      <li>Clear the qRFC queue and reprocess in correct sequence.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Before routing the issue, capture: IDoc number, direction, message type, partner, first error status, and error text. Reprocessing without fixing the cause produces more failed IDocs and makes the original failure harder to read.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an IDoc configuration guide. It does not cover partner profile setup, port or RFC destination configuration, IDoc segment design, or AIF mapping. It does not replace SAP's IDoc and ALE documentation.</p>

    <p>This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Related diagnostics</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-ale-distribution-model-diagnostics/">SAP ALE Distribution Model Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC / tRFC Diagnostics</a></li>
    </ul>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
