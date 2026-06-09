---
layout: default
title: "SAP RFC Destination Diagnostics"
description: "Diagnostic guide for SAP RFC destination failures, connection errors, and remote function call issues in distributed system landscapes."
permalink: /atlas/diagnostics/sap-rfc-destination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and RFC
concept_type: diagnostic guide
sap_area: "Basis / ALE / RFC"
business_process: Integration
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - rfc
  - integration
  - sap-basis
  - diagnostics
  - distributed-systems
related:
  - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
  - /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP RFC Destination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP RFC destination diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why an RFC destination fails, why tRFC or qRFC queues are stuck, or why cross-system calls return errors.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>Basis / ALE / RFC</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until RFC behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>RFC destinations in SAP define how one system calls another. When an RFC fails, the impact can be stuck IDocs, failed master data replication, missing transactional data, or batch job cancellations. The diagnostic task is to isolate whether the failure is in the network layer, the destination configuration, the target system availability, the user credentials, or the called function module.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>RFC destination test in SM59 returns "Connection refused," "Name or password incorrect," or "Program not registered."</li>
      <li>tRFC or qRFC queue in SM58 or SMQ1/SMQ2 shows repeated errors for a specific destination.</li>
      <li>IDoc is stuck in status 03 (data passed to port) but never arrives at the target system.</li>
      <li>Master data replication shows success in the source but the object is missing in the target.</li>
      <li>Background job fails with RFC-related short dump (CALL_FUNCTION_REMOTE_ERROR).</li>
      <li>Cross-system transaction fails with COMMIT_FAILURE or ROLLBACK_FAILURE.</li>
      <li>RFC performance is slow, causing timeouts in calling programs.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Network or firewall:</strong> the target system is unreachable due to network changes, firewall rules, or DNS resolution failure.</li>
      <li><strong>Target system down:</strong> the target application server, message server, or gateway is not running.</li>
      <li><strong>User credentials:</strong> the user in the RFC destination is locked, expired, or has incorrect password.</li>
      <li><strong>Program not registered:</strong> for TCP/IP RFC destinations (e.g., PI/PO, external programs), the registered program is not running.</li>
      <li><strong>Gateway or message server issue:</strong> the SAP gateway (sapgwXX) or message server is not responding.</li>
      <li><strong>Load balancing misconfiguration:</strong> the logon group or message server parameters are incorrect.</li>
      <li><strong>Function module error:</strong> the RFC reaches the target system but the called function module fails due to data or authorization issues.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SM59</strong> — RFC destination administration; test connection, Unicode test, and authorization test.</li>
      <li><strong>SM58</strong> — tRFC error log; check failed RFC calls and error texts.</li>
      <li><strong>SMQ1 / SMQ2</strong> — qRFC queue monitor; check outbound and inbound queues.</li>
      <li><strong>SMGW</strong> — gateway monitor; check registered programs and active connections.</li>
      <li><strong>SMLG</strong> — logon group load balancing; check group assignment and server availability.</li>
      <li><strong>SM21</strong> — system log; check for gateway or work process errors.</li>
      <li><strong>ST22</strong> — short dump analysis; check for RFC-related dumps in the calling or target system.</li>
      <li><strong>AL11</strong> — directory listing; check gateway trace files (dev_rd) if needed.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>RFCDES / RFCDOC</strong> — RFC destination definitions.</li>
      <li><strong>ARFCSDATA / ARFCSSTATE</strong> — tRFC execution data and status.</li>
      <li><strong>TRFCQOUT / TRFCQIN</strong> — tRFC queue tables.</li>
      <li><strong>SMQ1 / SMQ2</strong> — qRFC queue monitor transactions.</li>
      <li><strong>GWY_CONN</strong> — gateway connection table (via SMGW).</li>
      <li><strong>USR02</strong> — user master; check if the RFC user is locked or expired.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the RFC destination name and the exact error message from SM59, SM58, or the application log.</li>
      <li>Test the connection in SM59: connection test, Unicode test, and authorization test.</li>
      <li>If the connection test fails, check network connectivity (ping, telnet to gateway port) from the Basis team.</li>
      <li>If the authorization test fails, check the user in USR02 for lock status, password expiry, or missing authorizations.</li>
      <li>Check SMGW for registered programs if the destination uses a registered RFC server program.</li>
      <li>Check SM58 for tRFC errors: note the transaction ID, error text, and retry count.</li>
      <li>Check SMQ1/SMQ2 for qRFC queue status if the destination uses queued RFC.</li>
      <li>Check ST22 in both source and target systems for RFC-related short dumps.</li>
      <li>If the connection succeeds but the function fails, check the target system application log (SLG1) for function module errors.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the RFC destination host name, IP address, or gateway service if network details changed.</li>
      <li>Unlock or reset the password for the RFC user in SU01.</li>
      <li>Restart the registered RFC program or server if it is not running.</li>
      <li>Restart the SAP gateway service (sapgwXX) if it is not responding.</li>
      <li>Reprocess tRFC errors in SM58 after fixing the underlying issue.</li>
      <li>Clear or restart qRFC queues in SMQ1/SMQ2 if they are stuck.</li>
      <li>Adjust the RFC timeout or retry settings if the issue is intermittent network latency.</li>
      <li>Escalate to the network or Basis team if the issue is infrastructure-related.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>RFC destination failures are usually network, configuration, or credential issues. A useful ticket should include: RFC destination name, source system, target system, exact error message, SM59 test results, and whether the issue is isolated to one destination or affects multiple.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an RFC configuration guide. It does not cover RFC destination creation, SNC/SSL setup, or PI/PO adapter configuration. It does not replace SAP's RFC and integration documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC and tRFC Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-ale-distribution-model-diagnostics/">SAP ALE Distribution Model Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
