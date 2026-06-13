---
layout: default
title: "SAP IDoc Status Diagnostics"
description: "A conservative diagnostic frame for IDoc status code issues and status-driven troubleshooting in SAP."
permalink: /atlas/diagnostics/sap-idoc-status-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: "IDoc / ALE / EDI"
business_process: Integration
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau

tags:
  - integration
  - sap-ale
  - diagnostics
  - idoc
related:
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/diagnostics/sap-inbound-processing-diagnostics/
  - /atlas/diagnostics/sap-outbound-processing-diagnostics/
  - /atlas/diagnostics/sap-idoc-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP IDoc Status Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP IDoc status diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for interpreting IDoc status codes and deciding the next action based on status.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE / EDI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until IDoc status behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>IDoc status codes tell you where an interface document failed and what layer is responsible. Status 51 means application error, 56 means IDoc missing, 64 means ready for dispatch, 75 means control record error. The support goal is to map the status to the right layer — syntax, partner profile, application, or workflow — and collect the evidence needed before escalating.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>IDoc stuck in status 64 and not processed.</li>
      <li>IDoc in status 51 with application error text that is not immediately clear.</li>
      <li>IDoc in status 56 with 'IDoc added' but no further processing.</li>
      <li>Inbound IDoc in status 53 but the business document was not created.</li>
      <li>Outbound IDoc in status 03 but the partner reports it never arrived.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Status 51 — application error:</strong> the IDoc passed syntax and partner checks but failed during application posting. Often master data or business rule issue.</li>
      <li><strong>Status 56 — IDoc missing:</strong> the IDoc was added to the system but the processing function could not be found or is not assigned.</li>
      <li><strong>Status 64 — not processed:</strong> the IDoc is waiting for a background job or manual trigger to process.</li>
      <li><strong>Status 75 — control record error:</strong> the control record contains invalid partner, message type, or port information.</li>
      <li><strong>Status 02 — error passing data to port:</strong> the port or RFC destination is misconfigured or unreachable.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE02 / WE05 — IDoc list and detailed display with status history.</li>
      <li>BD87 — IDoc reprocessing and status change.</li>
      <li>SM58 — tRFC error log if the IDoc uses RFC.</li>
      <li>SMQ1 / SMQ2 — qRFC queues if queued RFC is involved.</li>
      <li>SLG1 — application log for detailed error messages.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC</strong> — IDoc control record.</li>
      <li><strong>EDIDS</strong> — IDoc status records.</li>
      <li><strong>EDID4 / EDID3</strong> — IDoc data records (version-dependent).</li>
      <li><strong>TBD41 / TBD42</strong> — status code definitions.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the IDoc number and the current status from WE02 or WE05.</li>
      <li>Read the status text and any error messages in the status history.</li>
      <li>Map the status to the layer: syntax (status 60+), partner/profile (status 56, 75), application (status 51), or transmission (status 02, 03).</li>
      <li>For status 51, check the application log (SLG1) and the specific error text for master data or business rule issues.</li>
      <li>For status 64, check if the background job (RBDAPP01) is scheduled and running.</li>
      <li>For status 02 or 03, check the port, RFC destination, and partner profile.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Reprocess the IDoc with BD87 after correcting the underlying master data or configuration issue.</li>
      <li>Trigger the background job (RBDAPP01) if IDocs are stuck in status 64.</li>
      <li>Correct the partner profile or port configuration if the IDoc fails at the profile layer.</li>
      <li>Fix the control record data if status 75 indicates invalid partner or message type.</li>
      <li>If the IDoc is corrupted and cannot be reprocessed, request a resend from the partner system.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>IDoc status is the primary diagnostic signal. A useful ticket should include: IDoc number, direction, message type, partner, current status, status history, error text, and whether the issue is isolated or批量. Do not reprocess IDocs without understanding why they failed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an IDoc configuration guide. It does not cover partner profile setup, port configuration, or AIF mapping. It does not replace SAP's IDoc documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
