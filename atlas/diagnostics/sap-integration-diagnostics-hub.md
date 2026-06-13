---
layout: default
title: "SAP Integration Diagnostics Hub"
description: "A review-candidate hub mapping IDoc, AIF, qRFC, tRFC, RFC destination, and interface monitoring symptoms to SAP checks."
permalink: /atlas/diagnostics/sap-integration-diagnostics-hub/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: "IDoc / AIF / RFC / ALE"
business_process: "Integration operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - integration
  - idoc
  - qrfc
related:
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
  - /atlas/diagnostics/sap-rfc-destination-diagnostics/
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/maps/integration-monitoring-reliability-map/
**Practical implication:** Use status codes and queue states first; most integration failures separate cleanly into partner-profile, master-data, timing, or RFC-destination categories.
**Tags:** sap-ams, integration, idoc, qrfc

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Integration Diagnostics Hub</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic Hub</p>
    <h1>SAP Integration Diagnostics Hub</h1>
    <p class="note-subtitle">A first-pass workflow for IDoc, AIF, qRFC/tRFC, RFC destination, ALE, and interface monitoring failures.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration operations</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / AIF / RFC / ALE</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Integration failures in SAP-heavy landscapes usually present as one of a few patterns: an IDoc stops with a status code, a qRFC queue is stuck, an RFC destination returns an error, an ALE distribution model misses a target, or monitoring does not alert on a real failure. This hub maps each symptom to the first transaction or monitor to open.</p>

    <h2>Symptom-to-check matrix</h2>
    <table>
      <thead>
        <tr><th>Symptom</th><th>First check</th><th>Typical SAP touchpoints</th></tr>
      </thead>
      <tbody>
        <tr><td>IDoc failed or stuck in error status</td><td>IDoc status and error text</td><td>WE02, WE05, BD87, IDoc status records</td></tr>
        <tr><td>Outbound IDoc never reached partner</td><td>Partner profile and port</td><td>WE20, WE21, tRFC/BGRFC queue</td></tr>
        <tr><td>Inbound IDoc posted wrong data</td><td>Segment processing and mapping</td><td>WE19, BD87, target application log</td></tr>
        <tr><td>qRFC/tRFC queue is stuck</td><td>Queue status and locked entries</td><td>SM58, SMQ1, SMQ2, QRFC monitor</td></tr>
        <tr><td>Cross-system call fails</td><td>RFC destination and authorization</td><td>SM59, connection test, authorization log</td></tr>
        <tr><td>Master data not distributed to target</td><td>ALE distribution model and filter</td><td>BD64, BD50, WE02 on target side</td></tr>
        <tr><td>Monitoring misses failures or over-alerts</td><td>Alert configuration and coverage</td><td>SXMB_MONI, AIF monitoring, custom monitors</td></tr>
        <tr><td>Document output never reached recipient</td><td>Message determination and spool</td><td>NACE, SOST, spool request, condition records</td></tr>
      </tbody>
    </table>

    <h2>Evidence to collect</h2>
    <ul>
      <li>IDoc number, message type, partner, and status history.</li>
      <li>Queue name and LUW count for qRFC/tRFC issues.</li>
      <li>RFC destination name and connection-test result.</li>
      <li>ALE distribution model and message type for master-data distribution.</li>
      <li>Target application document number or error log reference.</li>
      <li>Timestamp of failure and any related batch job or middleware log (without system IDs).</li>
    </ul>

    <h2>Related diagnostics</h2>
    <div class="atlas-card-grid">
      <a class="atlas-card" href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">
        <h2>IDoc and AIF Integration</h2>
        <p>Partner profiles, segments, master data, and timing failures.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">
        <h2>qRFC and tRFC</h2>
        <p>Queues stuck or executing out of order.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-idoc-status-diagnostics/">
        <h2>IDoc Status Codes</h2>
        <p>Interpret status codes and decide next action.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-rfc-destination-diagnostics/">
        <h2>RFC Destination</h2>
        <p>Cross-system call failures and queue issues.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-ale-distribution-model-diagnostics/">
        <h2>ALE Distribution Model</h2>
        <p>Master data not distributed or duplicated.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">
        <h2>Interface Monitoring</h2>
        <p>Missed failures and false alerts.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">
        <h2>Inbound Processing</h2>
        <p>Message not received or posted incorrectly.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">
        <h2>Outbound Processing</h2>
        <p>Message not created, not sent, or corrupted.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
    </div>

    <h2>Related maps and concepts</h2>
    <ul>
      <li><a href="/atlas/maps/integration-monitoring-reliability-map/">Integration Monitoring and Reliability Map</a> — review candidate.</li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a> — review candidate.</li>
    </ul>

    <h2>Boundaries and escalation</h2>
    <p>This hub covers diagnostic triage only. Structural IDoc changes, partner profile reconfiguration, ALE model changes, and retry of mass failed documents require change control, functional review, and careful testing. Escalate when a retry could create duplicate follow-on documents or when the failure affects period-end processes.</p>

    <h2>Safe automation opportunity</h2>
    <p>A support agent can classify IDoc status codes, summarize queue depth, and cross-reference partner profiles to reduce initial triage time. It should not retry documents or change configuration.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
