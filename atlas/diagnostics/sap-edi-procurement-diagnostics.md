---
layout: default
title: "SAP EDI Procurement Diagnostics"
description: "A diagnostic frame for EDI message failures in SAP procurement: orders, confirmations, shipping notices, and invoices."
permalink: /atlas/diagnostics/sap-edi-procurement-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement integration
concept_type: diagnostic guide
sap_area: "MM EDI"
business_process: Procure to pay
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - edi
  - procurement
  - integration
  - diagnostics
related:
  - /atlas/diagnostics/sap-idoc-diagnostics/
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/diagnostics/sap-vendor-confirmation-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP EDI Procurement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP EDI procurement diagnostics</h1>
    <p class="note-subtitle">Trace EDI procurement failures from partner profile to IDoc status and business document.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM EDI</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>EDI in procurement moves purchase orders, order confirmations, shipping notices, and invoices between SAP and supplier systems. Failures usually appear as a missing business document, but the root cause is often earlier: partner profile, port definition, message control, or IDoc mapping. The diagnostic goal is to follow the message path from outbound generation to inbound posting.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Purchase order was not sent to the supplier.</li>
      <li>Supplier shipping notice arrived but no inbound delivery was created.</li>
      <li>Supplier invoice posted via EDI is blocked or missing.</li>
      <li>IDoc status is 51 or 56 and the message did not reach the application.</li>
      <li>EDI messages arrive but reference wrong PO numbers or quantities.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Partner profile missing:</strong> vendor is not set up with the correct partner function and message type.</li>
      <li><strong>Message control not triggered:</strong> output condition record or dispatch time is not configured.</li>
      <li><strong>Port or RFC issue:</strong> EDI subsystem or file port is unreachable.</li>
      <li><strong>IDoc segment error:</strong> mandatory segment missing or value format is invalid.</li>
      <li><strong>Mapping mismatch:</strong> supplier format differs from the expected IDoc version or message variant.</li>
      <li><strong>Document reference error:</strong> inbound message references a PO that does not exist or is closed.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WE20 — partner profiles for vendor and message types.</li>
      <li>WE21 — port definitions.</li>
      <li>NACE / condition technique — output determination for EDI messages.</li>
      <li>WE02 / WE05 — IDoc status monitor.</li>
      <li>SOST — send requests and transmission status.</li>
      <li>BD87 — IDoc reprocessing.</li>
      <li>ME23N / MIGO / MIRO — downstream business documents.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC / EDIDD / EDIDS</strong> — IDoc control, data, and status records.</li>
      <li><strong>EDP13 / EDP21</strong> — partner profile message control.</li>
      <li><strong>TEDELS / TEDE1</strong> — port and IDoc type references.</li>
      <li><strong>NAST</strong> — output messages.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the missing or failed business document and its expected EDI message type.</li>
      <li>Check the output message or IDoc control record for the partner and message type.</li>
      <li>Review IDoc status history to find the first error status.</li>
      <li>Validate partner profile, port, and message control configuration.</li>
      <li>Compare the IDoc segment values with the referenced PO, delivery, or invoice.</li>
      <li>Reprocess or correct the IDoc after fixing the root cause.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Maintain the missing partner profile or port for the vendor.</li>
      <li>Adjust output condition records or dispatch time.</li>
      <li>Correct mapping in the EDI subsystem or SAP extension.</li>
      <li>Fix document references in the inbound message or master data.</li>
      <li>Reprocess failed IDocs through BD87 after validation.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>EDI procurement failures are integration failures first and procurement failures second. Always trace the message from partner profile to IDoc status before assuming the supplier or the business document is wrong.</p>

    <h2>Related diagnostics</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-diagnostics/">SAP IDoc Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-output-message-control-diagnostics/">SAP Output Message Control Diagnostics</a></li>
    </ul>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
