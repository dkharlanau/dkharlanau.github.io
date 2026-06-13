---
layout: default
title: "SAP Spool and Print Output Diagnostics"
description: "Diagnostic guide for SAP spool request failures, print output errors, and message control issues in transaction SP01, SP02, and related output management."
permalink: /atlas/diagnostics/sap-spool-output-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Basis and output management
concept_type: diagnostic guide
sap_area: "Basis / SPAD / output control"
business_process: System operations
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - spool
  - print-output
  - sap-basis
  - diagnostics
  - output-management
related:
  - /atlas/diagnostics/sap-output-message-control-diagnostics/
  - /atlas/diagnostics/sap-background-job-diagnostics/
  - /atlas/sap/output-control/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Spool and Print Output Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP spool and print output diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a spool request failed, why print output was not generated, or why a document output never reached the printer or recipient.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System operations</dd></div>
      <div><dt>SAP area</dt><dd>Basis / SPAD / output control</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until spool behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP generates spool requests for printed documents, reports, and form outputs. The spool request passes through the SAP spool system, an output device (printer), or an external output management system. When output fails, the issue can be in the spool request itself, the output device configuration, the access method, the host spool system, or the form/layout. The diagnostic task is to trace the spool request from creation to the final destination.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Spool request is created but status remains "In process" or "-" and never prints.</li>
      <li>Spool request shows status "Error" or "Compl." with errors in the spool log.</li>
      <li>Document output (e.g., invoice, purchase order) is not generated after saving or posting.</li>
      <li>Print output is generated but sent to the wrong printer or recipient.</li>
      <li>Background job produces spool output but the spool request is deleted or not found.</li>
      <li>Form output shows garbled characters, missing fields, or wrong layout.</li>
      <li>Multiple spool requests are created for a single document, causing duplicate prints.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Output device misconfiguration:</strong> the printer (output device) in SPAD has the wrong device type, access method, or host printer name.</li>
      <li><strong>Access method failure:</strong> the access method (C = direct operating system call, L = print locally, U = print via SAPSprint) does not match the infrastructure.</li>
      <li><strong>Host spool system error:</strong> the operating system spooler (Windows print spooler, CUPS, etc.) is stopped or the printer queue is full.</li>
      <li><strong>Form or Smart Form issue:</strong> the form (SAPscript, Smart Form, Adobe Form) is corrupted, has a version mismatch, or references missing resources.</li>
      <li><strong>Message control configuration:</strong> the output type (e.g., RD00, NEU) is not configured for the document type, or the condition record is missing.</li>
      <li><strong>Communication user issue:</strong> the user assigned to the output device or RFC destination lacks authorization.</li>
      <li><strong>Spool request deletion:</strong> the spool request was deleted by a cleanup job or retention policy before printing.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SP01 / SP02</strong> — spool request administration and user spool list; check status, output device, and spool log.</li>
      <li><strong>SPAD</strong> — output device configuration; check device type, access method, host printer, and device attributes.</li>
      <li><strong>NACE / SPRO</strong> — message control and output type configuration for application documents.</li>
      <li><strong>VF31 / ME9F</strong> — output processing for billing documents and purchase orders; check condition records and processing status.</li>
      <li><strong>SOST</strong> — send requests (for email/fax output); check transmission status.</li>
      <li><strong>SM13</strong> — update records; check if the update that creates the spool request failed.</li>
      <li><strong>SM21</strong> — system log; check for spool work process or host spool errors.</li>
      <li><strong>SM50 / SM66</strong> — work process overview; check if spool work processes are available.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>TSP01 / TSP02</strong> — spool request header and line items.</li>
      <li><strong>TSP03</strong> — output device definitions.</li>
      <li><strong>TNAPR</strong> — output program and form assignment for message control.</li>
      <li><strong>NAST</strong> — message status table for application outputs.</li>
      <li><strong>T001P</strong> — printer determination and user-parameter assignment.</li>
      <li><strong>SP01 spool log</strong> — detailed error text for each spool request.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the spool request number or the document number for which output is missing.</li>
      <li>Check SP01/SP02 for the spool request status, output device, and error log.</li>
      <li>If no spool request exists, check NAST for the output type and message status.</li>
      <li>Check the output device in SPAD: is the device type correct? Is the access method valid?</li>
      <li>Test the output device in SPAD using the test print function.</li>
      <li>Check the host spool system (operating system level) for printer queue status and errors.</li>
      <li>Check SM13 for failed update records that may have prevented spool creation.</li>
      <li>Check SM50/SM66 for spool work process availability.</li>
      <li>If the form output is garbled, verify the form version and device type compatibility.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the output device configuration in SPAD (host printer name, access method, device type).</li>
      <li>Restart the host spooler service or clear the printer queue if it is stuck.</li>
      <li>Reprocess the output in VF31, ME9F, or the relevant output processing transaction.</li>
      <li>Create or update the message condition record in NACE if the output type is missing.</li>
      <li>Regenerate the form (Smart Form or Adobe Form) if the layout is corrupted or version-mismatched.</li>
      <li>Adjust spool retention settings if spool requests are deleted too quickly.</li>
      <li>Escalate to the Basis team if the issue is spool work process shortage or host spool system failure.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Spool and print output failures are usually device configuration, host spool, or message control issues. A useful ticket should include: spool request number, output device, document number, exact error message from SP01, and whether the issue affects one printer or all printers.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a spool or output device configuration guide. It does not cover SAP Print Service, SAP Cloud Print Manager, or mobile device printing. It does not replace SAP's output management documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-output-message-control-diagnostics/">SAP Output and Message Control Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Failure Diagnostics</a></li>
      <li><a href="/atlas/sap/output-control/">SAP Output Control</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
