---
layout: default
title: SAP qRFC and tRFC Diagnostics
description: A conservative diagnostic frame for queued and transactional RFC issues
  in SAP integration.
permalink: /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
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
    <p class="note-subtitle">A first-pass structure for finding why RFC calls are stuck, failing, or executing out of order.</p>
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
    <p>Transactional RFC (tRFC) and queued RFC (qRFC) are the transport layers for many SAP integrations including ALE, IDoc, and custom interfaces. When RFC calls are stuck in a queue, fail with connection errors, or execute in the wrong order, the support goal is to identify whether the issue is in the RFC destination, the queue configuration, the executing function module, or the target system availability.</p>
    <p>Always test the RFC destination in SM59 before reprocessing entries in SM58 or SMQ1/SMQ2. Reprocessing a queue against a broken destination just creates the same failure again.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>SM58 shows multiple tRFC entries in error status.</li>
      <li>SMQ1 or SMQ2 shows queues with status SYSFAIL or MANUAL.</li>
      <li>IDoc status 03 but partner reports the document never arrived.</li>
      <li>RFC destination test (SM59) fails with connection or authorization error.</li>
      <li>Queue scheduler is not running or queues are not being processed.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>RFC destination unreachable:</strong> the target system is down, network path is broken, or the gateway is not responding.</li>
      <li><strong>Authorization failure:</strong> the RFC user lacks the required authorization in the target system.</li>
      <li><strong>Queue blocked:</strong> a previous failed entry is blocking the entire queue (serialization).</li>
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
      <li>Identify the RFC destination, function module, and the error symptom (stuck, failed, out of order).</li>
      <li>Test the RFC destination in SM59 to confirm basic connectivity.</li>
      <li>Check SM58 for tRFC errors and read the error text for each failed entry.</li>
      <li>Check SMQ1 / SMQ2 for queue status. Look for the first failed entry that may be blocking the queue.</li>
      <li>Verify the RFC user authorization in the target system if the error is authorization-related.</li>
      <li>Check if the queue scheduler is running and if the queue is registered for scheduling.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Restart or correct the failed RFC entry in SM58 after fixing the underlying issue.</li>
      <li>Unblock the queue in SMQ1 / SMQ2 by deleting or moving the failed entry if it is blocking subsequent calls.</li>
      <li>Fix the RFC destination configuration if SM59 test fails.</li>
      <li>Update the RFC user authorization in the target system.</li>
      <li>Restart the queue scheduler if it is not running.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>qRFC and tRFC issues are usually connectivity, authorization, or queue blocking problems. Capture: RFC destination, function module, queue name (if qRFC), error text, SM58 or SMQ1/SMQ2 status, and whether the issue is isolated or affecting multiple interfaces.</p>

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

- [ ] Check SMQ1/SMQ2 for SYSFAIL or MANUAL status and identify the first blocking entry.

- [ ] Verify the RFC user authorization in the target system if authorization is suspected.

- [ ] Confirm the queue scheduler is running and the queue is registered for scheduling.

- [ ] Safety limit: do not delete or move a failed queue entry until the underlying cause is documented.
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
