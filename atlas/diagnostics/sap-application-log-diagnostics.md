---
layout: default
title: SAP Application Log Diagnostics
description: A practical guide to choosing SAP application logs, dumps, job logs, system logs, and traces from the incident evidence instead of searching everything at once.
permalink: /atlas/diagnostics/sap-application-log-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: Application logs / SLG1 / SM21
business_process: SAP AMS support
status: reviewed
verified: true
level: 2
last_reviewed: '2026-06-13'
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
robots: index,follow
sitemap: true
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
    <p class="note-subtitle">The right log is the one closest to the failed business step. Searching every technical monitor usually creates more noise than evidence.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>Application logs / runtime evidence</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Start from the failure, then choose the evidence source</h2>
    <p>SAP has many logs because different layers fail in different ways. A background job, an application validation, an ABAP dump, an RFC problem, and a system-level event should not begin in the same monitor.</p>
    <p>Before opening a log transaction, capture the exact time window, user or technical user, business object, program or interface if known, and what the user expected to happen. These details are the search key. Without them, “check the logs” becomes an expensive form of scrolling.</p>

    <h2>Which evidence is closest to the symptom?</h2>
    <div class="decision-table"><table><thead><tr><th>Symptom</th><th>Useful starting evidence</th><th>Why</th></tr></thead><tbody>
      <tr><td>Application step reports a business or processing error</td><td>Application log where the application writes one, often visible through SLG1.</td><td>It can contain object-specific messages and processing context that the UI does not show.</td></tr>
      <tr><td>ABAP runtime terminates</td><td>ST22 short dump for the matching user, program, and time.</td><td>The dump gives exception, program context, and call information for the termination.</td></tr>
      <tr><td>Background processing fails</td><td>Job status and job log first; spool or application log next when relevant.</td><td>The job itself tells you which step/program failed and under which user.</td></tr>
      <tr><td>Broad technical or system event is suspected</td><td>SM21 system log and Basis monitoring appropriate to the time window.</td><td>The problem may sit below one business application.</td></tr>
      <tr><td>Interface message fails</td><td>The message-specific monitor first: IDoc, AIF, RFC, queue, middleware, or API evidence used by that interface.</td><td>A generic system log rarely explains a business-message failure as well as the message trace itself.</td></tr>
      <tr><td>Issue is reproducible but normal evidence is not enough</td><td>A controlled trace such as authorization, SQL, or runtime trace chosen for the hypothesis.</td><td>Traces can be expensive and noisy, so they should answer a specific question.</td></tr>
    </tbody></table></div>

    <h2>Using the application log well</h2>
    <p>SLG1 is valuable when the application uses the SAP Application Log. Search with the narrowest useful combination of object, subobject, external ID, user, and time. The exact object names are application-specific, so a known working case or technical documentation is often useful.</p>
    <p>An empty SLG1 result does not prove that “SAP has no error.” The application may log elsewhere, the selection may be wrong, or the failure may happen before the logging point. Move to another evidence source only when the process path justifies it.</p>

    <h2>A diagnostic sequence</h2>
    <ol>
      <li><strong>Pin down the event.</strong> Exact timestamp or narrow window, user, system/client, business object, and failed action.</li>
      <li><strong>Choose the nearest log.</strong> Application log for application processing, job log for jobs, dump for runtime termination, message monitor for interfaces.</li>
      <li><strong>Find the first useful error.</strong> Later messages often describe consequences. The earlier message may show the rejected value, missing object, failed call, or exception.</li>
      <li><strong>Correlate across layers only when needed.</strong> If an application error calls an RFC, then follow the RFC. If a job step dumps, then open the dump. Build a chain instead of a pile of screenshots.</li>
      <li><strong>Compare with a working case.</strong> Same program, object type, user group, or interface in a nearby time window can show what normal evidence looks like.</li>
      <li><strong>Record the finding in business terms.</strong> State which processing step failed and what the log proves.</li>
    </ol>

    <h2>Traces are not the first reflex</h2>
    <p>Tools such as ST05, SAT, authorization traces, and other low-level diagnostics can be extremely useful, but they should have a question behind them. “Maybe the database is slow” is not enough. Define the transaction, user, time, reproduction step, and expected signal before tracing, and follow local rules for production use.</p>

    <h2>A few common mistakes</h2>
    <ul>
      <li>Searching a whole day when the failure time is known to the minute.</li>
      <li>Looking only at the latest error instead of the first meaningful failure in the chain.</li>
      <li>Using a generic system log for a message-specific integration problem.</li>
      <li>Changing log configuration during an incident without understanding retention, volume, or production impact.</li>
      <li>Collecting technical screenshots without linking them to the failed business object or process step.</li>
    </ul>

    <h2>What belongs in the escalation</h2>
    <p>Include system/client, time window, user or technical user, transaction/program/interface, business object, exact symptom, the relevant log or dump identifier, and the first useful error message. Add the path you already checked. This saves the next team from repeating the same search with the same incomplete information.</p>

    <h2>The useful outcome</h2>
    <p>Log analysis is complete when the evidence narrows the failure to a component or process step and gives the next owner a testable question. A 30-line copy of SLG1 is not a diagnosis. It is a souvenir.</p>
  </div>
</article>
