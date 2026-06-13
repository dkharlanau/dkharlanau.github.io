---
layout: default
title: "SAP Cloud Connector Diagnostics"
description: "Conservative diagnostic frame for SAP BTP Cloud Connector connectivity, tunnel, and destination issues."
permalink: /atlas/diagnostics/sap-cloud-connector-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: "Cloud Connector / BTP connectivity"
business_process: "Integration operations"
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - cloud-connector
  - btp
  - connectivity
  - integration
related:
  - /atlas/sap/cloud-connector/
  - /atlas/diagnostics/sap-rest-api-diagnostics/
  - /atlas/diagnostics/sap-rfc-destination-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Cloud Connector Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP cloud connector diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for SAP BTP Cloud Connector connectivity and tunnel issues.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration operations</dd></div>
      <div><dt>SAP area</dt><dd>Cloud Connector / BTP connectivity</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>The SAP BTP Cloud Connector bridges on-premise SAP systems and cloud services. Failures usually sit in the tunnel state, the access-control configuration, the destination, or the on-premise service availability.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Cloud application cannot reach the on-premise SAP system.</li>
      <li>Cloud Connector shows a disconnected or unhealthy tunnel.</li>
      <li>Destination test in BTP fails with connectivity or authorization errors.</li>
      <li>Some on-premise systems are reachable while others are not.</li>
      <li>Performance through the Cloud Connector is inconsistent.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Tunnel down:</strong> Cloud Connector cannot connect to the BTP subaccount.</li>
      <li><strong>Missing access control:</strong> the resource is not exposed for the cloud application.</li>
      <li><strong>Destination misconfiguration:</strong> wrong URL, authentication, or location ID.</li>
      <li><strong>On-premise service down:</strong> the target RFC/HTTP service is not active.</li>
      <li><strong>Network or firewall change:</strong> outbound connectivity to BTP is blocked.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>Cloud Connector admin UI — tunnel state, subaccount connection, and logs.</li>
      <li>BTP cockpit — destination configuration and connection test.</li>
      <li>SM59 / SICF — verify the on-premise RFC or HTTP service is active.</li>
      <li>On-premise network trace — confirm outbound connectivity to BTP endpoints.</li>
      <li>Application log on BTP and on-premise side for the same time window.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>Cloud Connector logs</strong> — tunnel and request logs (file-based, not SAP tables).</li>
      <li><strong>SM59</strong> — RFC destination test results.</li>
      <li><strong>SICF</strong> — HTTP service activation.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the affected subaccount, Cloud Connector instance, and target on-premise system.</li>
      <li>Check the Cloud Connector tunnel state and admin UI health indicators.</li>
      <li>Test the destination from BTP and capture the exact error.</li>
      <li>Verify access-control entries for the target resource.</li>
      <li>Check the on-premise service (SM59/SICF) and network path.</li>
      <li>Review both sides' logs for the failure window and correlate timestamps.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Restart or reconnect the Cloud Connector to the subaccount.</li>
      <li>Add or correct the access-control entry for the missing resource.</li>
      <li>Correct destination URL, authentication, or location ID.</li>
      <li>Activate or fix the on-premise RFC/HTTP service.</li>
      <li>Update firewall or proxy allow-lists for BTP endpoints.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Cloud Connector tickets are useful when they include the subaccount, Cloud Connector version, destination name, target system, and whether the issue is tunnel, access control, or service side.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a Cloud Connector installation or BTP security configuration guide. It does not cover detailed certificate or SAML setup.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>
</article>
