---
layout: default
title: SAP IDoc Status Diagnostics
description: A source-backed SAP IDoc guide for statuses 51, 53, 56, 64, 75, 02, and 03, with safe checks before reprocessing.
permalink: /atlas/diagnostics/sap-idoc-status-diagnostics/
last_modified_at: 2026-08-11
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: IDoc / ALE / EDI
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- integration
- sap-ale
- diagnostics
- idoc
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-inbound-processing-diagnostics/
- /atlas/diagnostics/sap-outbound-processing-diagnostics/
- /atlas/diagnostics/sap-idoc-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

**Sources:** [SAP inbound IDoc status records](https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079745.html), [SAP IDoc Channel monitoring guidance](https://support.sap.com/en/alm/solution-manager/expert-portal/monitoring-of-integration-scenarios/idoc-channel.html), and the [SAP ALE troubleshooting guide](https://help.sap.com/docs/SUPPORT_CONTENT/techtsg/3362710617.html).
**Date checked:** 2026-08-11
**Confidence:** high for standard status meanings; medium for landscape-specific routing and custom status handling.
**Related page/topic:** /atlas/diagnostics/idoc-aif-integration-diagnostics/
**Practical implication:** Treat the latest status as a processing checkpoint, then confirm the direction, full status history, and business outcome before retrying the IDoc.
**Tags:** integration, sap-ale, diagnostics, idoc

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP IDoc Status Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP IDoc status diagnostics</h1>
    <p class="note-subtitle">A status-led workflow for locating an IDoc failure without confusing transport success with application success.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE / EDI</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>An IDoc status is a checkpoint in either the inbound or outbound flow. It does not, by itself, prove that the intended business document exists in the receiving application. Start with direction and full status history, use the current status to select the next monitor, and reprocess only after the underlying cause is understood.</p>

    <h2>What the common IDoc statuses mean</h2>
    <table>
      <thead>
        <tr><th>Status</th><th>Direction and meaning</th><th>First evidence to check</th></tr>
      </thead>
      <tbody>
        <tr><td>51</td><td>Inbound: application document was not posted.</td><td>Read the detailed status text and application log; correct the data, configuration, or business-rule failure before using BD87.</td></tr>
        <tr><td>53</td><td>Inbound: application document was posted.</td><td>Open the referenced business object and review status history if the expected result still appears missing.</td></tr>
        <tr><td>56</td><td>Inbound: IDoc was added with errors, often during partner or profile checks.</td><td>Read the exact status message, then check the partner profile and control-record values.</td></tr>
        <tr><td>64</td><td>Inbound: IDoc is ready to be passed to the application.</td><td>Check the WE20 processing mode and, for background processing, the RBDAPP01 job, variant, and authorization in SM37.</td></tr>
        <tr><td>75</td><td>Inbound: IDoc is in an inbound qRFC queue.</td><td>Inspect the related inbound queue in SMQ2 before treating it as an IDoc control-record problem.</td></tr>
        <tr><td>02</td><td>Outbound: error while passing data to the port.</td><td>Check the port, RFC destination, connection, and status message.</td></tr>
        <tr><td>03</td><td>Outbound: data was passed to the port successfully.</td><td>If the receiver has no message, use the TID and SM58 or the relevant downstream monitor; status 03 is not receiver-side posting confirmation.</td></tr>
      </tbody>
    </table>

    <h2>Common symptoms</h2>
    <ul>
      <li>IDoc stuck in status 64 and not processed.</li>
      <li>IDoc in status 51 with application error text that is not immediately clear.</li>
      <li>IDoc in status 56 after a partner or profile check fails.</li>
      <li>Inbound IDoc in status 53 but the business document was not created.</li>
      <li>Outbound IDoc in status 03 but the partner reports it never arrived.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Application or data failure:</strong> status 51 points to inbound application posting, so the detailed status message is more useful than the numeric code alone.</li>
      <li><strong>Partner or profile mismatch:</strong> status 56 can result when the inbound partner, message type, or process code cannot be resolved as configured.</li>
      <li><strong>Processing backlog:</strong> status 64 can remain when background collection is configured but RBDAPP01 is missing, delayed, incorrectly filtered, or unauthorized.</li>
      <li><strong>Queued inbound processing:</strong> status 75 means the IDoc is waiting in an inbound qRFC path; the blocking evidence is normally in SMQ2.</li>
      <li><strong>Outbound transport failure:</strong> status 02 points to the port or its underlying technical connection. Status 03 means the port handoff succeeded, not that the receiver posted the business object.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE02 / WE05 — IDoc list and detailed display with status history.</li>
      <li>BD87 — IDoc reprocessing and status change.</li>
      <li>SM58 — tRFC error log if the IDoc uses RFC.</li>
      <li>SMQ1 / SMQ2 — qRFC queues if queued RFC is involved.</li>
      <li>SLG1 — application log for detailed error messages.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC</strong> — IDoc control record.</li>
      <li><strong>EDIDS</strong> — IDoc status records.</li>
      <li><strong>EDID4 / EDID3</strong> — IDoc data records (version-dependent).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the IDoc number and the current status from WE02 or WE05.</li>
      <li>Read the status text and any error messages in the status history.</li>
      <li>Confirm whether the IDoc is inbound or outbound; the same diagnostic language cannot be applied safely across both directions.</li>
      <li>Map the current status to one layer: inbound partner/profile, inbound application, background or qRFC backlog, or outbound port and transport.</li>
      <li>For status 51, use the detailed status message and the relevant application log to identify the data, configuration, or business-rule failure.</li>
      <li>For status 64, compare the WE20 processing mode with the RBDAPP01 schedule, selection variant, job log, and authorization.</li>
      <li>For status 75, inspect the inbound qRFC queue in SMQ2 and identify the first blocking entry.</li>
      <li>For status 02, check the port and underlying destination. For status 03 with a missing receiver message, trace the TID through SM58 or the applicable middleware and receiver monitor.</li>
      <li>Confirm the business result before closing the incident: document number, application log, receiver acknowledgement, or another system-specific proof.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Reprocess the IDoc with BD87 after correcting the underlying master data or configuration issue.</li>
      <li>Correct the RBDAPP01 schedule, variant, or authorization when background processing is configured and status 64 accumulates.</li>
      <li>Correct the partner profile or port configuration if the IDoc fails at the profile layer.</li>
      <li>Resolve the first failed qRFC unit before retrying an IDoc that remains in status 75.</li>
      <li>If the IDoc is corrupted and cannot be reprocessed, request a resend from the partner system.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Before routing the issue, capture the IDoc number, direction, message type, sender and receiver partner, timestamps, current status, full status history, and exact error text. Record whether the failure is isolated or part of a backlog. For status 03, include the transaction ID when available; for status 53, include the referenced application document.</p>

    <h2>Safe reprocessing boundary</h2>
    <p>Do not use BD87, restart an RFC entry, or request a resend merely to see whether the error clears. First establish whether the original message already produced a business object, whether sequencing matters, and which team owns the failing layer. This avoids duplicate documents and hides fewer intermittent failures.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079745.html">SAP: inbound data flow in ALE and inbound IDoc status records</a></li>
      <li><a href="https://support.sap.com/en/alm/solution-manager/expert-portal/monitoring-of-integration-scenarios/idoc-channel.html">SAP: IDoc Channel monitoring guidance</a></li>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/techtsg/3362710617.html">SAP: ALE troubleshooting guide</a></li>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/techtsg/3362709543.html">SAP: IDocs that remain in status 64</a></li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an IDoc configuration guide. It does not cover partner profile setup, port configuration, or AIF mapping. It does not replace SAP's IDoc documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
