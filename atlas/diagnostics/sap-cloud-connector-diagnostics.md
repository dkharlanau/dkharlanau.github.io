---
layout: default
title: "SAP Cloud Connector Diagnostics"
description: "A practical diagnostic for BTP-to-on-premise connectivity across tunnel state, resource exposure, destination setup, identity, and target health."
permalink: /atlas/diagnostics/sap-cloud-connector-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: "Cloud Connector / BTP connectivity"
business_process: "Integration operations"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
last_modified_at: 2026-08-15
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
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">SAP Cloud Connector Diagnostics</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
  <p class="eyebrow">Atlas Diagnostic</p>
  <h1>SAP Cloud Connector diagnostics</h1>
  <p class="note-subtitle">A green tunnel does not prove that an application can reach the right on-premise resource. Trace the complete path.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl><div><dt>Process</dt><dd>Integration operations</dd></div><div><dt>SAP area</dt><dd>Cloud Connector / BTP connectivity</dd></div><div><dt>Indexing</dt><dd>Noindex until product-specific claims are verified.</dd></div></dl></aside>

<div class="note-body">
  <h2>The problem is an end-to-end connectivity break</h2>
  <p>SAP Cloud Connector is one part of the path between a BTP workload and an on-premise resource. A connection can fail because the subaccount tunnel is unavailable, the resource is not exposed, a location or destination points to the wrong connector, identity propagation is wrong, or the target service itself is unavailable.</p>
  <p>That means “Cloud Connector is connected” and “the application can use the backend” are different statements. Diagnose the path stage by stage.</p>

  <h2>Separate the layers</h2>
  <div class="decision-table"><table><thead><tr><th>Layer</th><th>Question</th><th>Evidence</th></tr></thead><tbody>
    <tr><td>BTP application</td><td>Which destination or connectivity configuration is the application actually using?</td><td>Application/subaccount, destination name, region, location context, timestamp.</td></tr>
    <tr><td>Subaccount tunnel</td><td>Is the expected Cloud Connector connected to the correct subaccount?</td><td>Connector status, subaccount mapping, recent disconnects, certificate/connection events.</td></tr>
    <tr><td>Resource exposure</td><td>Is the exact internal host, protocol, port, and path/resource allowed?</td><td>Virtual-to-internal mapping and exposed-resource rules.</td></tr>
    <tr><td>Identity</td><td>Does the target receive the identity or technical credential expected by this scenario?</td><td>Authentication mode, principal propagation context where used, target authorization error.</td></tr>
    <tr><td>On-premise target</td><td>Is the backend service reachable and healthy from the connector host/network?</td><td>Target service status, DNS/network evidence, backend log and response.</td></tr>
  </tbody></table></div>

  <h2>A practical diagnostic workflow</h2>
  <ol>
    <li><strong>Start from the failing application call.</strong> Capture the BTP application, subaccount, destination, timestamp, target business service, and exact error.</li>
    <li><strong>Confirm the intended connector path.</strong> In landscapes with more than one connector or location, verify that the destination resolves through the expected instance rather than a different healthy connector.</li>
    <li><strong>Check tunnel state around the failure time.</strong> Current green status can hide a short disconnect that occurred during the incident.</li>
    <li><strong>Check resource exposure precisely.</strong> Compare the requested host, protocol, port, and path with what is exposed. “The system is exposed” is too broad.</li>
    <li><strong>Check authentication separately from connectivity.</strong> A reachable backend can still reject the propagated or technical identity. Keep network and authorization evidence distinct.</li>
    <li><strong>Check the backend itself.</strong> Confirm that the target service was available and that its own logs show either the request or the absence of one.</li>
    <li><strong>Compare with a working route.</strong> Another destination to the same backend or another backend through the same connector can help isolate destination, connector, network, or service ownership.</li>
  </ol>

  <h2>Do not restart first</h2>
  <p>Restarting a connector may restore service, but it also removes evidence and can hide a certificate, network, proxy, resource-mapping, or capacity problem that will return. Preserve the failure window and logs first. Restart only when the operational runbook and impact justify it.</p>

  <h2>Useful next actions</h2>
  <ul>
    <li>Correct the destination or location reference when the BTP workload uses the wrong path.</li>
    <li>Correct resource exposure when the exact backend host or path is outside the allowed mapping.</li>
    <li>Repair subaccount connectivity, certificates, proxy, or outbound network access when the tunnel itself is unstable.</li>
    <li>Correct the target authentication or identity propagation setup when connectivity succeeds but authorization fails.</li>
    <li>Route backend availability or service errors to the owning application/Basis team with connector evidence attached.</li>
  </ul>

  <h2>What to capture first</h2>
  <p>Record the BTP subaccount and region, application, destination, location identifier if used, Cloud Connector instance, virtual and internal target, resource path, authentication mode, failure timestamp, exact error, tunnel state at that time, and whether the backend saw the request.</p>

  <h2>Limitations and boundaries</h2>
  <p>This page is a diagnostic structure, not an installation or security guide. Cloud Connector capabilities and administration details evolve, and identity propagation, certificates, high availability, proxying, and destination behavior depend on the landscape. Verify the current SAP product documentation before changing security-sensitive connectivity configuration.</p>
</div>

<section class="atlas-related"><h2>Related Atlas Pages</h2><ul>
  <li><a href="/atlas/sap/cloud-connector/">SAP Cloud Connector</a></li>
  <li><a href="/atlas/diagnostics/sap-rest-api-diagnostics/">SAP REST API Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-rfc-destination-diagnostics/">SAP RFC Destination Diagnostics</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
