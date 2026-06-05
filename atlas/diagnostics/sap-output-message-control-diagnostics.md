---
layout: default
title: "SAP Output and Message Control Diagnostics"
description: "A conservative diagnostic frame for output determination and message control issues in SAP."
permalink: /atlas/diagnostics/sap-output-message-control-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: "Output determination / NAST"
business_process: Integration
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - integration
  - sap-sd
  - diagnostics
  - output-determination
related:
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/diagnostics/sap-inbound-processing-diagnostics/
  - /atlas/diagnostics/sap-outbound-processing-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Output and Message Control Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP output and message control diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a document output (print, email, IDoc, fax) was not created, not sent, or sent to the wrong recipient.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>Output determination / NAST</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until output determination behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Output determination controls how SAP documents communicate with external systems and users — via print, email, fax, EDI, or IDoc. When an expected output is missing, sent to the wrong address, or fails with a processing error, the support goal is to identify whether the issue is in the condition technique, output type, partner function, medium, or processing program.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Expected printout, email, or IDoc was not generated for a sales or purchase document.</li>
      <li>Output was created but remains in status 'not processed' or 'error'.</li>
      <li>Email was sent to the wrong address or with wrong attachment.</li>
      <li>IDoc output was generated but the partner reports it never arrived.</li>
      <li>Multiple outputs were created for the same document unexpectedly.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Condition not met:</strong> the output condition record does not match the document characteristics (partner, document type, sales area).</li>
      <li><strong>Output type disabled:</strong> the output type is not active for the document type or has been deactivated.</li>
      <li><strong>Wrong partner function:</strong> the output is determined for a partner function that is missing or has wrong address data.</li>
      <li><strong>Processing program error:</strong> the program or form assigned to the output type fails during execution.</li>
      <li><strong>Communication method issue:</strong> the email server, fax gateway, or printer is unreachable or misconfigured.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>NACE — condition technique for output determination.</li>
      <li>VV33 / VV23 — output condition records for sales / purchasing.</li>
      <li>SP01 / SOST — spool and send requests.</li>
      <li>SOST — email send status and error details.</li>
      <li>WE02 — IDoc output status if the output medium is IDoc.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>NAST</strong> — output messages.</li>
      <li><strong>TNAPR</strong> — output programs and forms.</li>
      <li><strong>TVARVC</strong> — variant variables (if used in output programs).</li>
      <li><strong>SOOD / SOFM</strong> — SAPoffice documents and send requests.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the document number, output type, and the expected output medium.</li>
      <li>Check the document output screen (e.g., VF03 for billing, ME23N for PO) to see if the output was determined.</li>
      <li>If not determined, check the condition technique (NACE) and condition records (VV33/VV23).</li>
      <li>If determined but not processed, check NAST for status and error text.</li>
      <li>For email, check SOST for send status and recipient address.</li>
      <li>For print, check SP01 for spool requests and printer status.</li>
      <li>For IDoc, check WE02 for generated IDoc and its status.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or update the output condition record to match the document characteristics.</li>
      <li>Activate the output type if it was disabled.</li>
      <li>Correct the partner function or address data if the output is sent to the wrong recipient.</li>
      <li>Fix the processing program or form if it fails during execution.</li>
      <li>Resolve communication method issues (email server, printer, fax gateway) with the infrastructure team.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Output issues are usually condition technique or communication method problems. A useful ticket should include: document number, output type, expected medium, actual result, NAST status, error text, and whether the issue is isolated or recurring.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an output determination configuration guide. It does not cover Smart Forms, Adobe Forms, or condition technique design. It does not replace SAP's output management documentation.</p>

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
