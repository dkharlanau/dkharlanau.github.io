---
layout: default
title: SAP IDoc Diagnostics
description: Diagnose SAP IDoc failures by tracing the message from business trigger through IDoc status, transport, and application posting.
permalink: /atlas/diagnostics/sap-idoc-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: diagnostic guide
sap_area: IDoc / ALE
business_process: Cross-system integration
status: reviewed
verified: true
level: 2
expert_context:
  enabled: true
  domain: sap-integration
  topics:
    - IDoc diagnostics
    - partner profiles
    - integration incident resolution
  service_url: /services/sap-integration-reliability-assessment/
  evidence_urls:
    - /atlas/diagnostics/sap-idoc-status-diagnostics/
    - /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
    - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
last_reviewed: '2026-06-13'
last_modified_at: 2026-09-05
author: Dzmitryi Kharlanau
tags:
- sap-ams
- idoc
- ale
- integration
- diagnostics
related:
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
- /atlas/diagnostics/sap-inbound-processing-diagnostics/
- /atlas/diagnostics/sap-outbound-processing-diagnostics/
- /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP IDoc Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP IDoc diagnostics</h1>
    <p class="note-subtitle">Treat the IDoc as a message journey. Find the last step that worked, then investigate the first step that did not.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-system integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Do not start with the status code alone</h2>
    <p>An IDoc status is evidence, but it is not the whole incident. First define the business message: what should have left the source system, where should it have gone, and which business document or update should have appeared in the target?</p>
    <p>Then trace the message through the actual landscape. The failure can happen before an IDoc is created, during dispatch, in RFC or queue processing, after the target receives the IDoc, or inside the target application. The same user symptom can therefore belong to very different owners.</p>

    {% include atlas/expert-context.html %}

    <h2>Split the problem by the last confirmed step</h2>
    <div class="decision-table"><table><thead><tr><th>Evidence</th><th>What it tells you</th><th>Next place to look</th></tr></thead><tbody>
      <tr><td>No expected outbound IDoc exists</td><td>The problem may be in the business trigger, output/change logic, distribution model, or selection before IDoc creation.</td><td>Source document, trigger logic, change pointers or application-specific generation path.</td></tr>
      <tr><td>IDoc exists but was not transferred as expected</td><td>The message was created, so move downstream to partner, port, RFC, queue, or scheduling evidence.</td><td>IDoc status history, partner profile, port, RFC/tRFC/qRFC evidence.</td></tr>
      <tr><td>Target received the IDoc but no business document was posted</td><td>Transport worked far enough for application processing to begin.</td><td>Inbound status text, segment values, master data, mapping, application validation.</td></tr>
      <tr><td>IDoc reached a success status but the business result is still wrong</td><td>The technical message path may be healthy while the application result or follow-on process is not.</td><td>Created business document, application log, follow-on status, business rules.</td></tr>
      <tr><td>The same business message appears more than once</td><td>Do not assume “duplicate IDoc” is the cause. Find whether the source sent twice, middleware retried, or the target processed twice.</td><td>Message identifiers, timestamps, source trigger, middleware/retry history, target document references.</td></tr>
    </tbody></table></div>

    <h2>A useful diagnostic path</h2>
    <ol>
      <li><strong>Capture the business context.</strong> Source and target systems, direction, message type, business object, expected result, time window, and one concrete example.</li>
      <li><strong>Find the IDoc and read its status history.</strong> Use the sequence and timestamps, not only the latest status. The first meaningful error often explains more than later reprocessing statuses.</li>
      <li><strong>Check the control record.</strong> Confirm sender/receiver partner information, message type, IDoc type, and basic routing context.</li>
      <li><strong>Inspect the failed layer.</strong> For transport problems, follow partner, port, RFC, tRFC, or qRFC evidence as used in this landscape. For application errors, read the target error text and the relevant segment values.</li>
      <li><strong>Compare with a successful message.</strong> A working IDoc of the same business scenario gives you routing, segment, and timing evidence without guessing.</li>
      <li><strong>Correct the cause before reprocessing.</strong> Reprocessing is a recovery step, not a diagnosis.</li>
      <li><strong>Confirm the business result.</strong> The incident is closed when the expected target document or update exists and the integration path is stable again.</li>
    </ol>

    <h2>Useful SAP tools</h2>
    <p>The exact tool set depends on direction and architecture. Common starting points in classic IDoc/ALE landscapes include:</p>
    <ul>
      <li><strong>WE02 / WE05</strong> for IDoc content and status history.</li>
      <li><strong>WE20</strong> for partner-profile context.</li>
      <li><strong>WE21</strong> for port definitions.</li>
      <li><strong>BD87</strong> for controlled IDoc reprocessing where applicable.</li>
      <li><strong>SM58</strong> when transactional RFC processing is part of the failed path.</li>
      <li><strong>SMQ1 / SMQ2</strong> when qRFC queues are part of the integration design.</li>
    </ul>
    <p>Do not open every monitor because an IDoc failed. Use the IDoc history to decide which layer deserves attention.</p>

    <h2>What to capture before escalation</h2>
    <ul>
      <li>IDoc number, direction, message type, sender and receiver.</li>
      <li>Business document or object reference and expected target result.</li>
      <li>Status sequence with the first relevant error text and timestamp.</li>
      <li>Relevant segment/value that failed application validation, if known.</li>
      <li>RFC or queue evidence only when that layer is part of the failure.</li>
      <li>A successful comparison message when available.</li>
    </ul>

    <h2>Reprocessing needs a business check</h2>
    <p>Before reprocessing, confirm whether the message is safe to repeat. Some inbound processes have duplicate protection; others can create a second business effect if the original result already exists outside the status you are looking at. Check the target business object and the landscape's restart design before pressing the convenient button humans invented for making yesterday's problem happen twice.</p>

    <h2>The end of the diagnosis</h2>
    <p>A strong IDoc incident says where the chain broke: generation, routing, transport, queue, mapping/data, or application posting. “Status 51 fixed” is not enough. The status is the symptom. The reusable knowledge is why the application rejected the message and what control prevents the same failure next time.</p>

    <h2>Official references and scope</h2>
    <p>Use these SAP references to check the monitoring and partner-profile behavior behind this guide. The sequence of investigation and escalation checklist above are the author's diagnostic synthesis; the references do not establish a cause or approve reprocessing in your system.</p>
    <ul>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/8f3819b0c24149b5959ab31070b64058/4b4c790e4a712597e10000000a42189b.html?locale=en-US&amp;version=LATEST">SAP Help: IDoc Monitoring</a> — ABAP Platform, 2025 FPS01 documentation at the time of the source check. Describes the available monitoring views and distinguishes IDoc display, status processing, and queues. Use it to select the monitor for the failed layer.</li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/8f3819b0c24149b5959ab31070b64058/4ab7c1736dbe6d8be10000000a42189c.html?locale=en-US&amp;state=PRODUCTION&amp;version=202310.latest">SAP Help: Status Monitor for ALE Messages</a> — ABAP Platform 2023 documentation. Covers BD87, status long text, linked objects, and manual processing after correcting the problem. This supports reading the error and target context before recovery.</li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/8f3819b0c24149b5959ab31070b64058/4ab38cc3549a6d8ce10000000a42189c.html">SAP Help: Check/Generate Partner Profiles</a> — ABAP Platform, 2025 FPS01 documentation at the time of the source check. Identifies WE20 and the distribution-model and RFC prerequisites. Use it to investigate routing configuration, not as an instruction to regenerate profiles during an incident.</li>
    </ul>
    <p><strong>Source check:</strong> 5 September 2026. Confidence is high for the documentation topics mapped above. This guide concerns classic IDoc/ALE landscapes; check your release, integration design, permissions, and restart behavior before applying a step. A source check is not a new review of the entire article or a live SAP test.</p>

    <h2>Related diagnostics</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-ale-distribution-model-diagnostics/">SAP ALE Distribution Model Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC / tRFC Diagnostics</a></li>
    </ul>
  </div>
</article>

{% include atlas/expert-cta.html %}
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
