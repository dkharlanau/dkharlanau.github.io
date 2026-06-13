---
layout: default
title: "SAP Background Job Failure Diagnostics"
description: "Diagnostic guide for SAP background job failures, scheduling issues, and job log analysis in transaction SM37 and related monitoring."
permalink: /atlas/diagnostics/sap-background-job-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Basis and system operations
concept_type: diagnostic guide
sap_area: "Basis / CCMS"
business_process: System operations
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - basis
  - background-jobs
  - sap-operations
  - diagnostics
  - system-monitoring
related:
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
  - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/sap/job-monitoring/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Background Job Failure Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP background job failure diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a background job failed, was cancelled, did not start, or produced incorrect results in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System operations</dd></div>
      <div><dt>SAP area</dt><dd>Basis / CCMS</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until background job behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Background jobs in SAP execute periodic or long-running tasks: MRP runs, IDoc processing, billing, payment runs, data archiving, and interface monitoring. When a job fails, the impact can be delayed invoices, stuck IDocs, or missing master data updates. The diagnostic task is to identify whether the failure is in the job definition, the program logic, the data, the authorization, or the system resources.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Job status in SM37 shows "Cancelled" or "Finished" with errors in the job log.</li>
      <li>Job is scheduled but never starts; status remains "Released" or "Ready."</li>
      <li>Job runs but produces no output, or the output is incomplete.</li>
      <li>Job runs longer than expected and is cancelled by the system due to maximum runtime.</li>
      <li>Job fails with a short dump (ST22) that is not visible in the job log.</li>
      <li>Job fails with authorization errors or missing variant errors.</li>
      <li>Job runs successfully in test but fails in production with the same variant.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Program or variant issue:</strong> the ABAP program has a bug, or the variant selects too much data, or a required parameter is missing.</li>
      <li><strong>Authorization failure:</strong> the user assigned to the job does not have the required authorization for the program, table, or transaction.</li>
      <li><strong>Data lock or enqueue:</strong> another process has locked the data the job needs, causing a timeout or dump.</li>
      <li><strong>Resource exhaustion:</strong> the job exceeds available memory, work processes, or database time.</li>
      <li><strong>Scheduling conflict:</strong> the job is scheduled to run when a dependent job is still running, or when the system is in maintenance mode.</li>
      <li><strong>Target server or work process unavailable:</strong> the job is assigned to a specific application server that is down or has no free work processes.</li>
      <li><strong>External command or program failure:</strong> the job calls an external program or RFC that fails.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SM37</strong> — job overview; check status, start time, end time, and job log.</li>
      <li><strong>SM35</strong> — batch input session log if the job processes a batch input.</li>
      <li><strong>ST22</strong> — short dump analysis; check for runtime errors at the same time as the job.</li>
      <li><strong>SM21</strong> — system log; check for system-level errors, work process restarts, or database issues.</li>
      <li><strong>SM12</strong> — enqueue lock overview; check if locks are held by other users or jobs.</li>
      <li><strong>ST03 / ST03N</strong> — workload analysis; check resource consumption and response times.</li>
      <li><strong>SM50 / SM66</strong> — work process overview; check if work processes are available and what they are running.</li>
      <li><strong>SM59</strong> — RFC destination test if the job calls external systems.</li>
      <li><strong>SP01 / SP02</strong> — spool request overview if the job produces print output.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>TBTCO</strong> — job status overview table.</li>
      <li><strong>TBTCP</strong> — job step details.</li>
      <li><strong>TBTCO-STATUS</strong> — job status codes (P = scheduled, S = released, R = ready, A = cancelled, F = finished).</li>
      <li><strong>TRBAT / TRJOB</strong> — transport-related job tables (if job is transport-related).</li>
      <li><strong>SNAP</strong> — short dump header table (links to ST22).</li>
      <li><strong>USR02</strong> — user master data; check if the job user is locked or expired.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the job name, job count, and the time of failure in SM37.</li>
      <li>Read the job log in SM37 for the exact error message or cancellation reason.</li>
      <li>Check ST22 for any short dumps at the same time with the same user or program.</li>
      <li>Check SM21 for system-level errors (database, work process, memory) at the same time.</li>
      <li>Verify the job variant: are the selection parameters reasonable? Does the variant exist?</li>
      <li>Check SM12 for enqueue locks on the tables or documents the job processes.</li>
      <li>Check SM50/SM66 for work process availability and load at the scheduled time.</li>
      <li>Test the program with the same variant in dialog mode (if safe) to reproduce the error.</li>
      <li>If the job calls an RFC, test the RFC destination in SM59.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the program variant to reduce data volume or fix missing parameters.</li>
      <li>Assign the correct authorizations to the job user or use a service user with the required roles.</li>
      <li>Reschedule the job to avoid conflicts with other jobs or maintenance windows.</li>
      <li>Release enqueue locks in SM12 if they are stale (with caution and approval).</li>
      <li>Increase the maximum runtime or memory allocation if the job is legitimately large.</li>
      <li>Restart the job in SM37 after fixing the underlying issue.</li>
      <li>Escalate to the development team if the program has a bug that requires code correction.</li>
      <li>Escalate to the Basis team if the issue is system resources, database performance, or work process shortage.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Background job failures are usually program, data, or resource issues. A useful ticket should include: job name, job count, scheduled time, actual start/end time, status, exact error message from the job log, program name, variant name, and whether the issue is isolated or recurring.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a job scheduling or Basis administration guide. It does not cover job definition creation, SM36 scheduling, or CCMS monitoring setup. It does not replace SAP's Basis documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC and tRFC Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/sap/job-monitoring/">SAP Job Monitoring</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
