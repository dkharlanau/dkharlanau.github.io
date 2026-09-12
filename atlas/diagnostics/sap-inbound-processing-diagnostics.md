---
layout: default
title: SAP Inbound Processing Diagnostics
description: A conservative diagnostic frame for inbound IDoc and ALE processing issues
  in SAP.
permalink: /atlas/diagnostics/sap-inbound-processing-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: IDoc / ALE / inbound
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
last_modified_at: 2026-09-12
article_visual: inbound-search-evidence
og_image: /assets/img/articles/inbound-search-evidence.webp
og_image_width: 1536
og_image_height: 1024
og_image_alt: "An inbound search branches into checking search scope when no match exists and checking status and application evidence when a match is found."
tags:
- integration
- sap-ale
- diagnostics
- inbound
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-integration-error-handling-diagnostics/
robots: index,follow,max-image-preview:large
sitemap: true
level: 2
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Inbound Processing Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP inbound processing diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why an inbound message was not received, not posted, or created wrong data.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / ALE / inbound</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Inbound processing is the path from an external system into SAP. When an inbound IDoc or message is missing, stuck in status, or posts wrong data, the support goal is to trace the path from receipt through syntax check, partner profile validation, and application posting to identify where it failed and why.</p>

    {% include article-visual.html %}

    <h2>Common symptoms</h2>
    <ul>
      <li>Partner reports a message was sent but no IDoc exists in SAP.</li>
      <li>Inbound IDoc exists but is stuck in status 64 or 51.</li>
      <li>IDoc posted successfully but the business document has wrong data.</li>
      <li>Inbound IDoc creates duplicate business documents.</li>
      <li>Inbound processing is slow and messages accumulate in the queue.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Receipt failure:</strong> transport evidence identifies a failed hand-off. An empty receiver search alone does not establish this cause.</li>
      <li><strong>Syntax error:</strong> the IDoc structure does not match the expected segment definition.</li>
      <li><strong>Partner profile mismatch:</strong> the sender partner or message type is not configured in the inbound partner profile.</li>
      <li><strong>Application error:</strong> the IDoc passed syntax and profile checks but failed during posting due to master data or business rules.</li>
      <li><strong>Queue bottleneck:</strong> a failed unit, dependency, deliberate stop, or resource constraint prevents progress. Queue depth alone does not distinguish these causes.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE02 / WE05 — IDoc list filtered by direction 2 (inbound) and partner.</li>
      <li>SM58 — inspect failed tRFC calls in the sending RFC system, when this interface actually uses tRFC. It is not a generic receiver-side inbound message log.</li>
      <li>SMQ2 — inbound qRFC queue status.</li>
      <li>SM21 — system log for gateway or connection errors.</li>
      <li>SLG1 — application log where the receiving application records posting details; start with the IDoc status long text and its referenced object.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC / EDIDS</strong> — IDoc control and status.</li>
      <li><strong>TRFCQIN</strong> — inbound qRFC queue.</li>
      <li><strong>ARFCSSTATE</strong> — tRFC status.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the receiving system and client, sender, message type, business key, and time window with its time zone. Capture the sender's correlation reference.</li>
      <li>Search WE02 / WE05 with direction 2 (inbound). Check restrictive partner, date, and status selections before concluding that no matching IDoc exists. Direction 1 denotes outbound processing.</li>
      <li>If no match remains, trace the actual transport path. Inspect middleware delivery evidence and, for a tRFC sender, failed calls in that sending system's SM58. Do not assume sender and receiver IDoc numbers are identical.</li>
      <li>If the IDoc exists, read its status history and detailed message. For status 51, inspect the application error and relevant application log where available. For a successful posting, inspect the referenced business object and expected state.</li>
      <li>For an inbound qRFC delay, inspect SMQ2 and the blocking unit or dependency. Record whether the queue is stopped intentionally before proposing recovery.</li>
      <li>Choose one testable next action and define its expected evidence: a located message, an explained failure, or the correct application state.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the search scope or correlation first if receipt is still uncertain.</li>
      <li>Correct a proven structure or mapping defect with the interface owner; validate a representative payload before replay.</li>
      <li>Change a partner profile only when the intended sender, message type, and processing design justify it.</li>
      <li>Resolve the specific master-data or business-rule failure before controlled reprocessing of affected status 51 IDocs.</li>
      <li>Request a resend only after checking the original outcome, duplicate handling, and replay scope. A missing search result is insufficient authorization for replay.</li>
      <li>Consider capacity or scheduler changes only after identifying a resource constraint. A serialized application error needs a different remedy.</li>
    </ul>

    <h2>Interview exercise: the empty receiver list</h2>
    <p><strong>Synthetic case.</strong> A sender reports successful dispatch at 23:58. The receiver search returns no IDoc. The search uses today's date, one partner, and direction 1. A colleague proposes an immediate resend.</p>
    <ol>
      <li>Name the selection error and two other facts to verify before interpreting the empty list.</li>
      <li>Explain which evidence would connect the sender's message to the receiver.</li>
      <li>State what you need to know before a resend is safe.</li>
    </ol>
    <details class="study-review">
      <summary>Review the diagnostic reasoning</summary>
      <p>Use direction 2 for inbound processing. Confirm the receiving system and client, then check the date boundary, time zone, and partner selection. The sender's message reference, business key, and transport trace should establish correlation; a dispatch statement alone does not establish posting.</p>
      <p>Before replay, determine whether the original message or business object already exists, how duplicates are handled, and which exact message is in scope. The useful answer narrows uncertainty before choosing recovery.</p>
      <p><strong>Transfer question:</strong> if the corrected search finds status 53, what changes? Inspect the referenced application object and expected state; the next step is no longer an investigation of an absent IDoc.</p>
    </details>

    <h2>Source checks</h2>
    <p>SAP documents direction 2 for inbound processing in <a href="https://help.sap.com/saphelp_em900/helpdata/en/4b/4c76174a712597e10000000a42189b/content.htm">Assigning a Function Module (Direct Inbound Processing)</a>. Its <a href="https://help.sap.com/saphelp_em700_ehp01/helpdata/en/0b/2a66bc507d11d18ee90000e8366fc2/content.htm">tRFC status check</a> describes investigating an outbound IDoc that has not reached the receiver. These checks were consulted on 12 September 2026; screen details and recovery procedures remain release- and landscape-dependent.</p>

    <h2>Support takeaway</h2>
    <p>Inbound issues are usually receipt, syntax, or application posting problems. A useful ticket should include: sender partner, message type, IDoc number if it exists, expected business document, actual result, and any error text from WE02, SM58, or SLG1.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an inbound processing configuration guide. It does not cover IDoc segment design, partner profile setup, or gateway configuration. It does not replace SAP's IDoc documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP Idoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
