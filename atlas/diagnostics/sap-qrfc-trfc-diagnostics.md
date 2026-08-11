---
layout: default
title: SAP qRFC and tRFC Diagnostics
description: A source-backed SAP qRFC and tRFC guide for blocked SMQ1, SMQ2, and SM58 entries, with safe recovery boundaries.
permalink: /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
last_modified_at: 2026-08-11
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: RFC / ALE / integration
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- integration
- sap-ale
- diagnostics
- rfc
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-interface-monitoring-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

**Sources:** [SAP guidance for SMQ1 and SMQ2](https://help.sap.com/saphelp_snc70/helpdata/EN/76/e12041c877f623e10000000a155106/content.htm?no_cache=true), [SAP qRFC queue status guidance](https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/48c1642f425831ebe10000000a42189b.html), and the [SAP ALE troubleshooting guide](https://help.sap.com/docs/SUPPORT_CONTENT/techtsg/3362710617.html).
**Date checked:** 2026-08-11
**Confidence:** high for monitor purpose and recovery boundaries; medium for status handling that depends on the application and release.
**Related page/topic:** /atlas/diagnostics/sap-rfc-destination-diagnostics/
**Practical implication:** Identify direction and the first blocking unit before restarting anything; a healthy destination does not rule out an application or serialization failure.
**Tags:** integration, sap-ale, diagnostics, rfc, qrfc, trfc

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP qRFC and tRFC Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP qRFC and tRFC diagnostics</h1>
    <p class="note-subtitle">A direction-first workflow for blocked transactional and queued RFC calls in SM58, SMQ1, and SMQ2.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>RFC / ALE / integration</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Transactional RFC (tRFC) and queued RFC (qRFC) carry many ALE, IDoc, and custom integration calls. qRFC adds queue-based serialization, so an earlier failed unit can hold later work in the same queue. The diagnostic task is to identify the direction, the first blocking unit, and whether the failure belongs to connectivity, authorization, scheduling, serialization, or the target application.</p>
    <p>Use SM59 when an outbound destination or connection is involved, but do not treat a successful destination test as proof that the queued function will execute successfully. Application data, authorization, locks, and queue state can still block the call.</p>

    <h2>Choose the monitor by processing path</h2>
    <table>
      <thead>
        <tr><th>Evidence location</th><th>What it tells you</th><th>First diagnostic question</th></tr>
      </thead>
      <tbody>
        <tr><td>SM58</td><td>Transactional RFC units waiting or in error.</td><td>What does the exact error text say, and is the destination currently reachable?</td></tr>
        <tr><td>SMQ1</td><td>Outbound qRFC queues in the sending system.</td><td>Which first unit is blocking the queue, and which destination owns the next step?</td></tr>
        <tr><td>SMQ2</td><td>Inbound qRFC queues in the receiving system.</td><td>Did the called application fail, or is processing deliberately stopped or waiting?</td></tr>
        <tr><td>SM59</td><td>RFC destination definition and technical tests.</td><td>Does connection and logon work with the configured destination and user?</td></tr>
        <tr><td>Queue scheduler</td><td>Whether eligible queues are registered and processed automatically.</td><td>Is the queue registered, active, and within the intended scheduling scope?</td></tr>
      </tbody>
    </table>

    <h2>Common symptoms</h2>
    <ul>
      <li>SM58 shows multiple tRFC entries in error status.</li>
      <li>SMQ1 or SMQ2 shows a persistent error, waiting, or manually stopped state.</li>
      <li>IDoc status 03 but partner reports the document never arrived.</li>
      <li>RFC destination test (SM59) fails with connection or authorization error.</li>
      <li>Queue scheduler is not running or queues are not being processed.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>RFC destination unreachable:</strong> the target system is down, network path is broken, or the gateway is not responding.</li>
      <li><strong>Authorization failure:</strong> the RFC user lacks the required authorization in the target system.</li>
      <li><strong>Queue blocked:</strong> an earlier failed unit is holding later calls in the same serialized queue.</li>
      <li><strong>Function module error:</strong> the called function module fails in the target system due to data or application errors.</li>
      <li><strong>Queue scheduler not running:</strong> the qRFC scheduler (QOUT scheduler or QIN scheduler) is not active.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>SM59 — RFC destination configuration and connection test.</li>
      <li>SM58 — tRFC monitor and error log.</li>
      <li>SMQ1 — outbound qRFC queue status.</li>
      <li>SMQ2 — inbound qRFC queue status.</li>
      <li>SM50 / SM66 — work process status if RFC is executing synchronously.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>ARFCSDATA / ARFCSSTATE</strong> — tRFC data and status.</li>
      <li><strong>TRFCQOUT / TRFCQIN</strong> — qRFC queue tables.</li>
      <li><strong>RFCDES</strong> — RFC destination definitions.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify whether the evidence belongs to tRFC, outbound qRFC, or inbound qRFC. Capture the destination, function module, queue name, timestamps, and business key.</li>
      <li>For an outbound path, test the RFC destination in SM59 to separate basic connection and logon problems from queue or application failures.</li>
      <li>Check SM58 for tRFC errors and read the exact message on the oldest relevant failed entry.</li>
      <li>Check SMQ1 or SMQ2 according to direction. Inspect the first failed unit in the queue rather than a later symptom.</li>
      <li>Verify the RFC user authorization in the target system if the error is authorization-related.</li>
      <li>Check if the queue scheduler is running and if the queue is registered for scheduling.</li>
      <li>Confirm whether the target application already committed a business result before repeating the call.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Repeat the failed tRFC unit only after connectivity, authorization, or application data has been corrected and duplicate-processing risk is understood.</li>
      <li>For qRFC, fix the first failed unit and use the release-appropriate repeat or activation action with the application owner.</li>
      <li>Do not delete or move a queue entry as a routine unblock step. That can break sequence, lose the only recoverable unit, or make later business state inconsistent.</li>
      <li>Fix the RFC destination configuration if SM59 test fails.</li>
      <li>Update the RFC user authorization in the target system.</li>
      <li>Restart the queue scheduler if it is not running.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the RFC destination, sending and receiving systems, function module, queue name, first failing unit, exact error text, timestamps, business key, and whether other queues or interfaces are affected. For serialized flows, note the oldest blocked unit and queue depth; for authorization errors, record the target-side evidence without exposing credentials.</p>

    <h2>Safe recovery boundary</h2>
    <p>A restart is justified only when the failure cause is corrected, the original execution outcome is known, and the relevant application owner agrees with the replay path. Deletion requires an explicit recovery and reconciliation decision; it is not a diagnostic shortcut.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/saphelp_snc70/helpdata/EN/76/e12041c877f623e10000000a155106/content.htm?no_cache=true">SAP: SMQ1 and SMQ2</a></li>
      <li><a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/48c1642f425831ebe10000000a42189b.html">SAP: queue status in SMQ1</a></li>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/techtsg/3362710617.html">SAP: ALE troubleshooting guide</a></li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an RFC configuration guide. It does not cover RFC destination setup, SNC configuration, or load balancing. It does not replace SAP's RFC documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-rfc-destination-diagnostics/">SAP RFC Destination Diagnostics</a> — test connectivity and authorization for the RFC destination.</li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a> — go here when RFC errors appear together with IDoc failures.</li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — use this when multiple interfaces are affected at the same time.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect RFC destination, function module, queue name, and SM58/SMQ1/SMQ2 status. **Synthetic example:** destination TEST_DEST_01, queue Q_1234567890.

- [ ] Test the RFC destination in SM59 and capture the connection or authorization error.

- [ ] Check SM58 for failed tRFC entries and read the error text before restarting.

- [ ] Check SMQ1/SMQ2 for a persistent error, waiting, or manually stopped state and identify the first blocking unit.

- [ ] Verify the RFC user authorization in the target system if authorization is suspected.

- [ ] Confirm the queue scheduler is running and the queue is registered for scheduling.

- [ ] Safety limit: do not repeat, delete, or move a failed unit until the underlying cause, original outcome, and recovery owner are documented.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP Idoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-rfc-destination-diagnostics/">SAP RFC Destination Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
