---
layout: default
title: SAP Application Log Diagnostics
description: A source-backed guide to choosing SAP application logs, ABAP short dumps, system logs, job logs, and traces from the failed processing step instead of searching every monitor.
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
last_reviewed: '2026-09-24'
last_modified_at: 2026-09-24
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
    <p class="note-subtitle">Start from the failed processing step, then choose the evidence source that can actually explain it.</p>
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
    <h2>There is no single SAP log for an incident</h2>
    <p>An SAP incident can cross several technical layers before the business symptom becomes visible. The application may reject a document, an ABAP program may terminate, a background job may cancel, an interface may stop in its own monitor, or the ABAP system itself may report a technical event. Those failures do not belong in one universal log.</p>

    <p>The useful starting point is therefore not “check SLG1” or “check SM21.” First identify the processing step that should have produced the missing result. Capture the narrowest useful time window, user or technical user, system and client, business object, program or interface if known, and the expected outcome. Those facts tell us which evidence source is closest to the failure.</p>

    <div class="decision-table"><table><thead><tr><th>Observed symptom</th><th>Start here</th><th>What this evidence can prove</th></tr></thead><tbody>
      <tr><td>An application step reports a business or processing error</td><td>The application-specific log, often the SAP Application Log displayed with SLG1 when that application writes there.</td><td>Which application object was processed, which message was raised, and often the processing context around it.</td></tr>
      <tr><td>An ABAP program terminates</td><td>ST22 / ABAP Runtime Error analysis for the matching user, program, client, and time.</td><td>The runtime error, termination context, source position, call information, and other dump details available for that failure.</td></tr>
      <tr><td>A background job cancels or finishes with the wrong result</td><td>The exact job run and job log first; then follow the failing program into its own application log, dump, spool, or interface evidence.</td><td>Which job step ran, under which user and parameters, and where the background process stopped or diverged.</td></tr>
      <tr><td>A broad ABAP system event is suspected</td><td>SM21 system log for the relevant time and application server scope.</td><td>System messages, warnings, and errors written by the ABAP instances.</td></tr>
      <tr><td>An interface message fails</td><td>The message-specific monitor: IDoc, AIF, RFC/qRFC, middleware, API, or application monitor used by that flow.</td><td>The state of the message or hand-off itself, which a generic system log often cannot explain.</td></tr>
    </tbody></table></div>

    <h2>SLG1 shows application-owned evidence</h2>
    <p>The SAP Application Log is structured by the application that writes it. Logs are commonly classified with an <strong>object</strong> and <strong>subobject</strong>; applications can also use an <strong>external ID</strong> to make one processing instance easier to find. SAP documentation for current S/4HANA scenarios still uses SLG1 in this way, for example to inspect Business Partner and SAP Gateway processing logs.</p>

    <p>That structure is the reason SLG1 works best when we already know something about the process. Search by the known object or subobject, external ID when available, user, and a narrow time window. A broad search usually produces unrelated messages and makes the real sequence harder to see.</p>

    <p>An empty SLG1 result does not prove that no error occurred. It proves only that the current selection found no matching application-log entry. The application may use a dedicated monitor, the selection may be wrong, the log may already have been removed according to its retention rules, or the failure may have occurred before that application wrote an entry. The next step should follow the process path, not assume that every application writes the same evidence.</p>

    <h2>ST22 and SM21 answer different questions</h2>
    <p>ST22 is for ABAP runtime errors. SAP documents a short dump as the record created when an ABAP program terminates because of a runtime error. The dump can include the error description, likely cause, source position, call information, and runtime context. If a user says that a transaction “just stopped,” matching the exact time, user, program, and client in ST22 can quickly separate an ABAP termination from an application-level rejection.</p>

    <p>SM21 is different. The ABAP system log records system messages, warnings, and errors for the SAP system; each instance writes a local log, and SM21 can read the relevant instance logs. This is useful when the evidence points below one business application—for example, when a dump or repeated application failures coincide with a wider system event. It is not a substitute for an application log or message-specific monitor.</p>

    <h2>Build one evidence chain</h2>
    <p>The investigation becomes much faster when each piece of evidence leads to the next layer. Suppose a nightly job cancels while posting business documents. The job log identifies the failing step. That step produces an ABAP dump. The dump points to a call that was processing one business object. If that application also writes an application log, the corresponding entry can explain which value or business rule caused the failure. Four monitors are useful here because they form one chain, not because we searched all four at random.</p>

    <p>Read the sequence from the first meaningful deviation, not only from the final red status. A later message often describes a consequence: “document not created,” “step cancelled,” or “processing terminated.” The earlier application message, dump, failed call, or missing dependency usually tells us why.</p>

    <p>Comparison with a nearby successful case is often more useful than collecting more logs. The same program, application object, interface, or job under a similar selection can show which messages are normal and which state transition is missing in the failed run.</p>

    <h2>Use traces only when ordinary evidence leaves a specific question</h2>
    <p>SQL traces, ABAP runtime traces, authorization traces, and other low-level tools can add detail that normal logs do not capture. They also add volume and can affect production operation if used carelessly. Before tracing, define the exact user or process, reproduction step, time window, and the signal you expect to confirm or reject. “Maybe the database is slow” is not a useful trace question; “which SQL statement dominates this reproducible step?” is.</p>

    <h2>A good escalation explains the boundary of the failure</h2>
    <p>An escalation should let the next owner continue the investigation instead of reconstructing it. Include the system and client, time window, user or technical user, business object, program/job/interface, expected result, the first meaningful error, and the evidence chain already checked. State what the evidence proves and what remains uncertain.</p>

    <p>The end product of log analysis is not a screenshot collection. It is a narrow statement such as: “The background job started correctly, step 2 terminated with an ABAP runtime error while processing document X, and the application log shows the rejected value immediately before the dump.” That statement gives the next team a component, a point in time, and a testable cause.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/05a5505cc81943fb9d01e84cb2e135ef/10a73b543e98843ae10000000a44538d.html">SAP S/4HANA 2025 FPS01: application logging example with SLG1</a></li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/a7b390faab1140c087b8926571e942b7/d13ca7548c124e8986df37c0821a9ce5.html">SAP ABAP Platform: SAP Gateway logs and SLG1 selection fields</a></li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/491807a9005338a1e10000000a421937.html">SAP ABAP Platform 2025 FPS01: runtime error long text and ST22</a></li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/76e99b1bf8b24e45933247ac04764749.html">SAP ABAP Platform 2025 FPS01: system logging with SM21</a></li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains how to choose and correlate evidence in ABAP-based SAP systems. Exact application-log objects, dedicated monitors, retention settings, authorizations, cloud tooling, and trace procedures vary by product, release, and landscape. Use the relevant SAP product documentation and local production rules before changing log settings or enabling traces.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Failure Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
