---
layout: default
title: "SAP Short Dump Diagnostics"
description: "Conservative diagnostic frame for ABAP runtime errors and short dumps in SAP systems."
permalink: /atlas/diagnostics/sap-short-dump-diagnostics/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: "ABAP runtime errors / ST22"
business_process: "SAP AMS support"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - abap
  - st22
  - runtime-error
  - diagnostics
related:
  - /atlas/diagnostics/sap-application-log-diagnostics/
  - /atlas/diagnostics/sap-update-termination-diagnostics/
  - /atlas/diagnostics/sap-background-job-diagnostics/
  - /atlas/diagnostics/sap-lock-enqueue-diagnostics/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/diagnostics/sap-application-log-diagnostics/
**Practical implication:** Use the dump type, program name, source line, and active calls to decide whether the cause is code, data, authorization, or resource limits before escalating.
**Tags:** sap-ams, abap, st22, runtime-error, diagnostics

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Short Dump Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP short dump diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why an ABAP program terminates with a runtime error in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>ABAP runtime errors / ST22</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>A short dump is an ABAP runtime error that terminates the program and writes detailed diagnostic information to the system. The support task is to extract the dump type, the exact statement, the active call stack, and the data values that triggered it, then decide whether the fix is in the data, the code, the configuration, or the environment.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A dialog transaction ends with a runtime error screen or a system message that refers to ST22.</li>
      <li>A background job is cancelled and the job log points to a short dump.</li>
      <li>ST22 shows one or more new dumps for the same program, user, or transaction.</li>
      <li>A custom program or enhancement starts dumping after a recent transport or support package.</li>
      <li>An intermittent failure only reproduces under specific data conditions.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Programming error:</strong> null object reference, division by zero, type conversion failure, or uncaught exception in custom code.</li>
      <li><strong>Data inconsistency:</strong> the program encounters a record state that it does not expect, such as a missing dependent object.</li>
      <li><strong>Resource limit:</strong> timeout, memory limit, or too many nested calls.</li>
      <li><strong>Authorization check in runtime:</strong> a missing authorization object causes a message-type dump.</li>
      <li><strong>Version mismatch:</strong> a transport moved code and data models out of sync.</li>
      <li><strong>External call failure:</strong> an RFC, HTTP, or database call returns an unhandled error.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ST22</strong> — short dump analysis: dump type, error message, source line, active calls, variable contents.</li>
      <li><strong>SM21</strong> — system log for operating-system or kernel-level errors around the failure time.</li>
      <li><strong>SLG1</strong> — application log for the affected component.</li>
      <li><strong>SM50 / SM66</strong> — work process overview if the dump is related to a dialog or background process.</li>
      <li><strong>SM37</strong> — background job log for job-related dumps.</li>
      <li><strong>SM13</strong> — update terminations if the dump occurred in an update work process.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SNAP</strong> — short dump header data.</li>
      <li><strong>ST22</strong> — short dump analysis tool.</li>
      <li><strong>TRDIR / TADIR</strong> — program and object directory entries.</li>
      <li><strong>SM21</strong> — system log.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Record the exact time, user, transaction, program, and dump type from the error.</li>
      <li>Open ST22, locate the dump, and read the short text and error information.</li>
      <li>Identify the source line and active calls to see which program and routine failed.</li>
      <li>Check the variable contents and the internal table state at the point of failure.</li>
      <li>Correlate the dump with SM21 system log entries and any application logs in SLG1.</li>
      <li>Determine whether the dump is isolated to one user, one object, or one program version.</li>
      <li>Decide whether the fix is a data correction, a code correction, or an environment change.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the master data or transactional data that triggers the dump, if the cause is data.</li>
      <li>Apply the relevant SAP note or implement a code fix for identified program errors.</li>
      <li>Adjust timeouts, memory limits, or job scheduling if the dump is resource-related.</li>
      <li>Re-run a failed background job after the root cause is removed.</li>
      <li>Escalate to development if the fix requires ABAP code changes.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful short dump ticket includes the dump type, program name, source line, user, transaction, time, and whether the failure is reproducible. Without this information, development cannot act quickly.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a triage guide, not an ABAP debugging or development manual. It does not cover detailed static analysis, code walkthroughs, or transport strategy.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-application-log-diagnostics/">SAP Application Log Diagnostics</a> — if the dump context is unclear and logs may contain earlier warnings.</li>
      <li><a href="/atlas/diagnostics/sap-update-termination-diagnostics/">SAP Update Termination Diagnostics</a> — if the dump appears in an update work process.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Failure Diagnostics</a> — if the dump cancelled a background job.</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-application-log-diagnostics/">SAP Application Log Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-incident-triage-diagnostics/">SAP Incident Triage Diagnostics</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
