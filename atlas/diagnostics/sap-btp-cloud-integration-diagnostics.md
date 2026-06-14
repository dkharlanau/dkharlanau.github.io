---
layout: default
title: "SAP BTP Cloud Integration Diagnostics"
description: "Conservative diagnostic frame for SAP BTP Cloud Integration (CPI) integration flow and message processing failures."
permalink: /atlas/diagnostics/sap-btp-cloud-integration-diagnostics/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: "SAP BTP Cloud Integration"
business_process: "Integration operations"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - btp
  - cloud-integration
  - cpi
  - integration
related:
  - /atlas/diagnostics/sap-cloud-connector-diagnostics/
  - /atlas/diagnostics/sap-integration-error-handling-diagnostics/
  - /atlas/diagnostics/sap-rest-api-diagnostics/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/sap/sap-integration-suite/
**Practical implication:** Use the integration flow name, message processing log, and the failing step to separate adapter, mapping, connectivity, and credential problems before retrying a message.
**Tags:** sap-ams, btp, cloud-integration, cpi, integration

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP BTP Cloud Integration Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP BTP Cloud Integration diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why an integration flow on SAP BTP Cloud Integration fails or does not deliver a message.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP BTP Cloud Integration</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP BTP Cloud Integration moves messages between cloud applications, on-premise SAP systems, and third-party endpoints. Failures usually surface in the message processing log as adapter errors, mapping exceptions, routing mismatches, or connectivity problems. The diagnostic goal is to locate the failing integration flow step, inspect the payload at that point, and determine whether the fix is in configuration, credentials, mapping, or the connected system.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A message shows status Failed, Escalated, or Retry in the Cloud Integration monitoring view.</li>
      <li>The receiver system does not receive a message that Cloud Integration reports as processed.</li>
      <li>The sender system cannot connect to Cloud Integration.</li>
      <li>A mapping step fails with a field or structure mismatch.</li>
      <li>A message is routed to the wrong receiver or split incorrectly.</li>
      <li>Authentication or certificate errors appear on the sender or receiver adapter.</li>
      <li>Large payloads cause timeouts or memory-related failures.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Adapter misconfiguration:</strong> wrong endpoint, credentials, certificate, or authentication method on sender or receiver.</li>
      <li><strong>Mapping exception:</strong> source and target structures differ, a mandatory field is missing, or an XSLT/Groovy script fails.</li>
      <li><strong>Routing error:</strong> a router, filter, or content modifier sends the message to the wrong branch.</li>
      <li><strong>Connectivity issue:</strong> Cloud Connector tunnel to on-premise is down, or a cloud endpoint is unreachable.</li>
      <li><strong>Credential or certificate expiry:</strong> OAuth token, client certificate, or keystore entry has expired.</li>
      <li><strong>Payload issue:</strong> the message is too large, malformed, or contains unsupported characters.</li>
      <li><strong>Deployment/version drift:</strong> the integration flow version on the tenant does not match the design-time version.</li>
    </ul>

    <h2>Where to check</h2>
    <ul>
      <li><strong>Cloud Integration Message Processing Log (MPL)</strong> — status, error step, and payload at each step.</li>
      <li><strong>Cloud Integration Operations view</strong> — tenant health, queue depth, and trace.</li>
      <li><strong>Cloud Connector logs / BTP Connectivity</strong> — tunnel and destination status for on-premise calls.</li>
      <li><strong>BTP subaccount / Destinations</strong> — destination configuration and credentials.</li>
      <li><strong>Sender and receiver system logs</strong> — whether the message was sent or received.</li>
      <li><strong>HTTP client or curl/Postman</strong> — reproduce the endpoint call outside the flow.</li>
    </ul>

    <h2>Key objects / artifacts</h2>
    <ul>
      <li><strong>Integration flow (IFlow)</strong> — the deployed integration artifact.</li>
      <li><strong>Message Processing Log (MPL)</strong> — per-message execution trace.</li>
      <li><strong>Cloud Connector</strong> — on-premise connectivity tunnel.</li>
      <li><strong>BTP destination / security material</strong> — credentials and certificates.</li>
      <li><strong>Keystore / client certificates</strong> — used for TLS and signing.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the integration flow name, message ID, and the time of failure.</li>
      <li>Open the Message Processing Log and locate the first failed step.</li>
      <li>Inspect the payload and headers before and after the failing step.</li>
      <li>Check the adapter configuration for endpoint, credentials, and certificates.</li>
      <li>Test connectivity from Cloud Integration to the receiver endpoint.</li>
      <li>If on-premise systems are involved, check the Cloud Connector tunnel and destination.</li>
      <li>Classify the cause as adapter, mapping, routing, connectivity, or credential.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the adapter endpoint, credentials, or authentication method.</li>
      <li>Fix the mapping or add null handling for missing fields.</li>
      <li>Adjust the router/filter conditions to route the message correctly.</li>
      <li>Renew or redeploy expired certificates, OAuth tokens, or keystore entries.</li>
      <li>Restore or restart the Cloud Connector tunnel if it is down.</li>
      <li>Redeploy the integration flow if version drift is suspected.</li>
      <li>Resubmit the message after correction; avoid mass resubmission until the root cause is fixed.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Cloud Integration tickets move fastest when they include the integration flow name, message ID, MPL error text, the failing step, and whether the issue is isolated to one sender, receiver, or message pattern.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a Cloud Integration development or BTP tenant administration guide. It does not cover detailed Groovy/XSLT scripting or BTP security configuration.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-cloud-connector-diagnostics/">SAP Cloud Connector Diagnostics</a> — if the flow reaches an on-premise system.</li>
      <li><a href="/atlas/diagnostics/sap-rest-api-diagnostics/">SAP REST API Diagnostics</a> — if the failing endpoint is HTTP/REST.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — for retry versus escalation decisions.</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/diagnostics/sap-integration-diagnostics-hub/">SAP Integration Diagnostics Hub</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
