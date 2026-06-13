---
layout: default
title: "SAP Application Log Diagnostics"
description: "Conservative diagnostic frame for SAP application logs, system logs, and developer traces in support incidents."
permalink: /atlas/diagnostics/sap-application-log-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: "Application logs / SLG1 / SM21"
business_process: "SAP AMS support"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - application-logs
  - slg1
  - sm21
  - diagnostics
related:
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
  - /atlas/diagnostics/sap-background-job-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Application Log Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP application log diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding incident evidence in SAP application logs, system logs, and developer traces.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>Application logs / SLG1 / SM21</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Application logs are often the fastest way to narrow an incident to a component, user, or transaction. When the symptom is vague, the goal is to move from the business report to the concrete log object, time window, and error text.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A process failed but no application error message is visible to the user.</li>
      <li>The support team needs to prove whether an error originated in SAP or in a connected system.</li>
      <li>An interface or batch job failed and the job log is too short to explain why.</li>
      <li>A user reports intermittent failures that are hard to reproduce.</li>
      <li>A custom program or enhancement behaves unexpectedly after a transport.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Log object not activated:</strong> the application writes to a log object that is not active in SLG0/SLG2.</li>
      <li><strong>Wrong log level:</strong> the log is configured for errors only and omits the warning that explains the root cause.</li>
      <li><strong>Time-window mismatch:</strong> the log is searched outside the actual failure window.</li>
      <li><strong>Object overwritten:</strong> old log entries were deleted by housekeeping before the incident was reported.</li>
      <li><strong>Trace not collected:</strong> a short dump or SQL trace was not captured at the moment of failure.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>SLG1 — application log: filter by log object, sub-object, external ID, or time.</li>
      <li>SM21 — system log: check for operating-system level or kernel errors around the failure time.</li>
      <li>ST22 — short dump analysis for ABAP runtime errors.</li>
      <li>ST05 / SQL trace — capture database activity if the issue is reproducible.</li>
      <li>SM50 / SM66 — work process overview for stuck or failed dialogs.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SLG1 / SLG2</strong> — application log entries and display.</li>
      <li><strong>SNAP</strong> — short dump header data.</li>
      <li><strong>TBPROF / TSP02</strong> — spool and print request tables.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the exact time, user, transaction, and business object involved in the incident.</li>
      <li>Open SLG1 and filter by the relevant log object/sub-object or external ID.</li>
      <li>If SLG1 is empty, check SM21 for system-level errors in the same time window.</li>
      <li>For ABAP dumps, open ST22 and search by date/user/transaction.</li>
      <li>If the failure is reproducible, run ST05 or SAT to capture SQL or runtime trace.</li>
      <li>Document the log object, message ID, and timestamp; correlate with business process step.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Activate or extend the relevant log object in SLG0 if logging is missing.</li>
      <li>Adjust log retention or archive strategy so recent incidents are still available.</li>
      <li>Add explicit error handling and logging in custom code.</li>
      <li>Route critical log objects to alerting or incident workflow.</li>
      <li>Escalate to development or basis if the trace points to a program or kernel issue.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful log investigation ticket includes: time window, user/background user, transaction or program name, business object ID, and the exact symptom. Without this context, log searches become slow and inconclusive.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a configuration guide for SAP Log Management or SAP Cloud ALM. It does not cover detailed trace interpretation or code debugging.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>
</article>
