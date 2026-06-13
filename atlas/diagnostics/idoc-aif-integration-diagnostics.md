---
layout: default
title: "IDoc and AIF Integration Diagnostics"
description: "A support diagnostic frame for investigating IDoc and AIF integration failures in SAP landscapes without assuming identical partner profiles or landscape setups."
permalink: /atlas/diagnostics/idoc-aif-integration-diagnostics/
atlas_section: diagnostics
domain: SAP operations
subdomain: Integration diagnostics
concept_type: diagnostic guide
sap_area: IDoc / AIF / integration
business_process: Cross-process operations
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - integration
  - idoc
  - aif
  - sap-ams
related:
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
  - /atlas/diagnostics/sap-idoc-diagnostics/
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
  - /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">IDoc and AIF Integration Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostics</p>
    <h1>IDoc and AIF integration diagnostics</h1>
    <p class="note-subtitle">Trace where interface failures originate, why they repeat, and what evidence to collect before escalating.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / AIF / integration</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>IDoc and AIF failures are rarely random. They cluster around specific partners, message types, process steps, or master data gaps. A useful diagnostic does not guess the root cause from the error text alone. It maps the failure to the landscape layer — partner profile, port, process code, mapping, or master data — and collects evidence that narrows the search.</p>

    <h2>First-pass diagnostic path</h2>
    <ul>
      <li>Confirm the message type, partner number, and direction (inbound or outbound).</li>
      <li>Check the IDoc status and whether the failure is at transmission, syntax, or processing stage.</li>
      <li>Review the partner profile and port settings for the affected message type.</li>
      <li>Inspect the IDoc segments for missing or unexpected values, especially control record fields.</li>
      <li>Check whether the failure is isolated to one partner, one plant, one message type, or one time window.</li>
      <li>Look for recent changes: transport releases, master data updates, partner profile edits, or network changes.</li>
    </ul>

    <h2>Common failure patterns</h2>

    <h3>Partner profile mismatches</h3>
    <p>A partner profile defines which message types a partner can send or receive, and how they are processed. Common issues:</p>
    <ul>
      <li>Message type not defined in the partner profile for the given partner and direction.</li>
      <li>Process code missing or pointing to a deactivated function module.</li>
      <li>Port definition changed but not propagated to all affected partners.</li>
    </ul>

    <h3>Segment and field-level errors</h3>
    <p>IDoc segments must match the expected structure for the message type. Issues include:</p>
    <ul>
      <li>Mandatory segments missing or in wrong order.</li>
      <li>Field lengths exceeded or invalid characters in key fields.</li>
      <li>Qualifier values that do not match the partner agreement.</li>
      <li>Control record fields (sender, receiver, message type) that do not match the payload.</li>
    </ul>

    <h3>Master data gaps</h3>
    <p>Many IDoc failures are actually master data failures in disguise:</p>
    <ul>
      <li>Material number does not exist or is not extended to the receiving plant.</li>
      <li>Customer or supplier master missing required roles or tax data.</li>
      <li>Plant, storage location, or purchasing organization not valid for the document type.</li>
    </ul>

    <h3>AIF-specific patterns</h3>
    <p>AIF adds a processing and monitoring layer on top of IDoc. When AIF is involved:</p>
    <ul>
      <li>Check the AIF interface determination — is the correct interface and variant selected?</li>
      <li>Review AIF structure mappings for field conversions and lookups.</li>
      <li>Inspect AIF index tables for missing or duplicate index values.</li>
      <li>Check AIF monitoring for error handling and restart capabilities.</li>
    </ul>

    <h3>Timing and sequencing</h3>
    <ul>
      <li>IDoc arrives before the referenced master data is replicated.</li>
      <li>Multiple IDocs for the same document arrive out of order.</li>
      <li>Batch job or workflow step that processes the IDoc is delayed or failed.</li>
    </ul>

    <h2>Diagnostic toolkit</h2>
    <ul>
      <li><strong>WE02 / WE05</strong> — IDoc list and detailed display.</li>
      <li><strong>WE20</strong> — partner profile overview.</li>
      <li><strong>BD87</strong> — status monitor for application errors.</li>
      <li><strong>/AIF/ERR</strong> — AIF error handling and monitoring.</li>
      <li><strong>SXI_MONITOR</strong> — PI/PO or Integration Suite message monitoring.</li>
      <li><strong>Application logs (SLG1)</strong> — custom or standard logging around interface processing.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful IDoc or AIF ticket should include: message type, partner number, direction, IDoc number, status, error text, affected document or material, and whether the failure is recurring. Avoid asking the integration team to "fix IDocs" without showing which layer failed and what changed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not provide transaction-by-transaction instructions. It does not claim that every SAP landscape uses the same partner profile setup or the same AIF configuration. It does not replace SAP's own IDoc and AIF documentation.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — use this when multiple interfaces are affected and you need a monitoring lens.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — go here to interpret status codes and identify the processing stage.</li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC and tRFC Diagnostics</a> — check this when IDoc processing depends on RFC queues.</li>
      <li><a href="/atlas/diagnostics/sap-output-message-control-diagnostics/">SAP Output and Message Control Diagnostics</a> — use this if the failing message is an output IDoc.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect message type, partner number, direction, IDoc number, and status. **Synthetic example:** IDoc 1234567890, message type ORDERS, outbound, partner TEST_CUST_01.

- [ ] Check WE02/WE05 for IDoc status and segment-level error text.

- [ ] Review partner profile (WE20), port, and process code for the message type.

- [ ] Inspect /AIF/ERR or SXI_MONITOR if AIF/PI/PO/Integration Suite is involved.

- [ ] Confirm whether the failure is isolated to one partner, plant, message type, or time window.

- [ ] Document recent changes: transports, master data updates, partner profiles, or network.

- [ ] Safety limit: do not mass-reprocess IDocs until the root layer (partner, mapping, or master data) is identified.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a></li>
      <li><a href="/atlas/automation/mini-apps-for-sap-operations/">Mini Apps and Prototypes for SAP Operations</a></li>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
