---
layout: default
title: SAP ALE Distribution Model Diagnostics
description: A conservative diagnostic frame for ALE distribution model issues in
  SAP master data replication.
permalink: /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: ALE / master data distribution
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- integration
- sap-ale
- diagnostics
- master-data
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-key-mapping-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP ALE Distribution Model Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP ALE distribution model diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why master data is not distributed, arrives at the wrong target, or creates duplicate objects.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>ALE / master data distribution</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>ALE distribution models define which master data changes are sent to which target systems. When master data is not replicated, arrives at the wrong system, or creates duplicates, the support goal is to identify whether the issue is in the distribution model, change pointers, filter objects, partner profiles, or the target system's handling of the received data.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Master data change in source system is not reflected in target system.</li>
      <li>Change pointer exists but no IDoc was generated.</li>
      <li>IDoc was sent to wrong target system or multiple systems unexpectedly.</li>
      <li>Target system creates duplicate master data objects instead of updating existing ones.</li>
      <li>Distribution model shows active but no messages for the object type.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing distribution model entry:</strong> the object type or message type is not included in the active distribution model.</li>
      <li><strong>Change pointer not created:</strong> change documents were not written or the change pointer job (BD21) did not process them.</li>
      <li><strong>Filter object mismatch:</strong> the filter object excludes the specific plant, company code, or sales organization from distribution.</li>
      <li><strong>Partner profile issue:</strong> the receiver partner profile does not support the message type or the outbound parameter is missing.</li>
      <li><strong>Target system key mapping:</strong> the target system does not recognize the source key and creates a new object instead of updating.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>BD64 — distribution model display.</li>
      <li>BD22 — change pointer overview.</li>
      <li>BD21 — change pointer processing log.</li>
      <li>WE20 — partner profile outbound parameters.</li>
      <li>WE02 — generated IDocs for the message type.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>BDCP / BDCPS</strong> — change pointers.</li>
      <li><strong>EDIDC / EDIDS</strong> — IDoc control and status.</li>
      <li><strong>TBD22 / TBD23</strong> — distribution model tables.</li>
      <li><strong>TBDBE</strong> — filter objects.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the master data object, message type, source system, and expected target system.</li>
      <li>Check BD64 for the distribution model: is the object/message type included and active?</li>
      <li>Check BD22 for change pointers: was a change pointer created for the object change?</li>
      <li>Run or check BD21 to see if change pointers were processed into IDocs.</li>
      <li>Check WE20 for the receiver partner profile: does it have the outbound parameter for this message type?</li>
      <li>Check WE02 for generated IDocs and their status.</li>
      <li>On the target system, check if the IDoc was received and whether it created or updated the object.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Add the missing object type or message type to the distribution model.</li>
      <li>Process change pointers with BD21 if they were not automatically processed.</li>
      <li>Adjust filter objects if the distribution scope is too narrow.</li>
      <li>Update the partner profile to include the missing outbound parameter.</li>
      <li>Fix key mapping on the target system if duplicates are being created.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>ALE distribution issues are usually model or profile configuration gaps. A useful ticket should include: object type, message type, source system, target system, change document number, distribution model name, and whether the issue is new or recurring.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an ALE configuration guide. It does not cover distribution model design, filter object setup, or target system key mapping configuration. It does not replace SAP's ALE documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP Idoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
