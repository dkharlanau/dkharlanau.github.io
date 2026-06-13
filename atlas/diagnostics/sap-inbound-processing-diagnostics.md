---
layout: default
title: SAP Inbound Processing Diagnostics
description: A conservative diagnostic frame for inbound IDoc and ALE processing issues
  in SAP.
permalink: /atlas/diagnostics/sap-inbound-processing-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: IDoc / ALE / inbound
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- integration
- sap-ale
- diagnostics
- inbound
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-integration-error-handling-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Inbound Processing Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP inbound processing diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why an inbound message was not received, not posted, or created wrong data.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE / inbound</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Inbound processing is the path from an external system into SAP. When an inbound IDoc or message is missing, stuck in status, or posts wrong data, the support goal is to trace the path from receipt through syntax check, partner profile validation, and application posting to identify where it failed and why.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Partner reports a message was sent but no IDoc exists in SAP.</li>
      <li>Inbound IDoc exists but is stuck in status 64 or 51.</li>
      <li>IDoc posted successfully but the business document has wrong data.</li>
      <li>Inbound IDoc creates duplicate business documents.</li>
      <li>Inbound processing is slow and messages accumulate in the queue.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Receipt failure:</strong> the IDoc never arrived due to network, RFC, or gateway issues.</li>
      <li><strong>Syntax error:</strong> the IDoc structure does not match the expected segment definition.</li>
      <li><strong>Partner profile mismatch:</strong> the sender partner or message type is not configured in the inbound partner profile.</li>
      <li><strong>Application error:</strong> the IDoc passed syntax and profile checks but failed during posting due to master data or business rules.</li>
      <li><strong>Queue bottleneck:</strong> inbound qRFC queues are not processing fast enough.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE02 / WE05 — IDoc list filtered by direction 1 (inbound) and partner.</li>
      <li>SM58 — tRFC error log for inbound RFC failures.</li>
      <li>SMQ2 — inbound qRFC queue status.</li>
      <li>SM21 — system log for gateway or connection errors.</li>
      <li>SLG1 — application log for posting errors.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC / EDIDS</strong> — IDoc control and status.</li>
      <li><strong>TRFCQIN</strong> — inbound qRFC queue.</li>
      <li><strong>ARFCSSTATE</strong> — tRFC status.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the partner sent the message and capture the message ID or timestamp.</li>
      <li>Check WE02 for the IDoc with direction 1 (inbound) and the sender partner.</li>
      <li>If the IDoc does not exist, check SM21 for gateway errors and SM58 for RFC failures.</li>
      <li>If the IDoc exists, check its status and status history for the failure layer.</li>
      <li>For status 51, check SLG1 for the application error details.</li>
      <li>For queue delays, check SMQ2 for queue depth and processing status.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Request a resend from the partner if the IDoc never arrived.</li>
      <li>Fix syntax errors by correcting the segment data or updating the partner's mapping.</li>
      <li>Update the inbound partner profile to accept the message type and sender.</li>
      <li>Fix master data or business rule issues before reprocessing status 51 IDocs.</li>
      <li>Increase queue processing capacity or tune the queue scheduler if messages accumulate.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Inbound issues are usually receipt, syntax, or application posting problems. A useful ticket should include: sender partner, message type, IDoc number if it exists, expected business document, actual result, and any error text from WE02, SM58, or SLG1.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an inbound processing configuration guide. It does not cover IDoc segment design, partner profile setup, or gateway configuration. It does not replace SAP's IDoc documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP Idoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
