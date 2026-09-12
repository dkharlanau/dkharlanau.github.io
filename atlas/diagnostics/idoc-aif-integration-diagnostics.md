---
layout: default
title: "IDoc and AIF Integration Diagnostics"
description: "A landscape-aware diagnostic guide for separating IDoc, SAP AIF, on-premise integration, Cloud Integration, and application evidence."
permalink: /atlas/diagnostics/idoc-aif-integration-diagnostics/
last_modified_at: 2026-09-12
atlas_section: diagnostics
domain: SAP operations
subdomain: Integration diagnostics
concept_type: diagnostic guide
sap_area: IDoc / AIF / integration
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
article_visual: integration-monitor-boundaries
og_image: /assets/img/articles/integration-monitor-boundaries.webp
og_image_width: 1536
og_image_height: 1024
og_image_alt: "One business message crosses IDoc, optional AIF or middleware monitoring, and application-outcome evidence; each monitor proves only its own checkpoint."
tags:
  - diagnostics
  - integration
  - idoc
  - aif
  - sap-ams
related:
  - /atlas/diagnostics/sap-process-audit/
  - /atlas/automation/mini-apps-for-sap-operations/
  - /atlas/concepts/composable-erp-for-sap-operations/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
robots: noindex,follow
sitemap: false
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
    <p class="note-subtitle">Choose the monitor from the actual message path, correlate the records, and test the business outcome before recovery.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / AIF / integration</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>IDoc, SAP Application Interface Framework (AIF), an integration platform, and the receiving application can describe different checkpoints of the same business message. They are not interchangeable logs. Start by drawing the actual message path, then choose the monitor that owns each hop and correlate its record to the next one.</p>
    <p>SAP AIF supports several interface technologies with different scopes. Depending on configuration, it can monitor an IDoc or another technology, and it can also display messages that were not processed by the AIF runtime. Therefore, “not visible in AIF” does not by itself prove that an IDoc was never created or transported.</p>

    {% include article-visual.html %}

    <h2>What each evidence source can prove</h2>
    <table>
      <thead>
        <tr><th>Evidence source</th><th>Useful evidence</th><th>Boundary</th></tr>
      </thead>
      <tbody>
        <tr><td>WE02 / WE05</td><td>IDoc control record, data records, direction, status history, timestamps.</td><td>An IDoc status does not automatically prove the next platform or expected business state.</td></tr>
        <tr><td>AIF Monitoring and Error Handling</td><td>Configured interface view, indexed keys, application messages, and supported actions.</td><td>Visibility and restart capability depend on the interface technology, engines, and configuration.</td></tr>
        <tr><td>SXI_MONITOR / SXMB_MONI</td><td>On-premise XI / PI Integration Engine message evidence where that runtime is part of the path.</td><td>These transactions are not the Cloud Integration tenant monitor.</td></tr>
        <tr><td>Cloud Integration — Monitor Message Processing</td><td>Integration-flow execution, message processing log, identifiers, and step-level error context.</td><td>A completed flow does not prove that the receiver created the expected business object.</td></tr>
        <tr><td>IDoc status detail, SLG1, or business object</td><td>Application error, referenced object, and expected-versus-actual business state.</td><td>The relevant application log and object vary by scenario.</td></tr>
      </tbody>
    </table>

    <h2>First-pass diagnostic path</h2>
    <ol>
      <li>Record the source and receiver system and client, direction, message type, business key, time window with time zone, and available message or correlation ID.</li>
      <li>Sketch the configured route: direct IDoc, AIF-supported interface, on-premise PI/PO, Cloud Integration, or a combination. Do not add a monitor simply because it exists in the landscape.</li>
      <li>Search the monitor for each actual hop. Correlate records with documented identifiers, business keys, partners, and timestamps rather than assuming equal message numbers.</li>
      <li>For an IDoc, inspect the control record separately from the data records. Sender, receiver, message type, and direction belong to the control record; business payload fields belong to data segments.</li>
      <li>Read the detailed error at the first unproven or failed checkpoint. Compare affected and successful messages to identify partner, plant, payload, interface, or time-window patterns.</li>
      <li>Define one recovery action and one outcome check. Reprocessing is useful only after the cause, original outcome, scope, ordering, and duplicate risk are understood.</li>
    </ol>

    <h2>Common failure patterns</h2>
    <h3>IDoc configuration and data</h3>
    <ul>
      <li>The message type or direction does not match the intended partner-profile entry.</li>
      <li>The control record points to an unexpected sender, receiver, message type, or basic type.</li>
      <li>A mandatory segment, qualifier, or business field is missing or invalid for the receiving process.</li>
      <li>The application rejects otherwise valid transport data because required master data or a business rule is missing.</li>
    </ul>

    <h3>AIF scope and interface configuration</h3>
    <ul>
      <li>The selected namespace, interface, version, date range, status, or key excludes the message being investigated.</li>
      <li>The interface technology uses AIF for monitoring, runtime processing, or both; the available functions differ by the configured engines and technology.</li>
      <li>Interface determination, mapping, checks, value mapping, or actions route the message differently from the expected design.</li>
      <li>Indexing or key configuration makes correlation difficult even though another technical record exists.</li>
    </ul>

    <h3>Middleware and sequencing</h3>
    <ul>
      <li>A mapping or routing error occurs in the actual PI/PO or Cloud Integration runtime.</li>
      <li>A message reaches a technical receiver while the receiving application rejects it later.</li>
      <li>A dependent master-data message has not been applied, or serialized messages arrive or process in an unexpected order.</li>
      <li>A “successful” monitor status belongs to one hop and is interpreted as end-to-end success.</li>
    </ul>

    <h2>Choose the right monitor</h2>
    <ul>
      <li><strong>WE02 / WE05</strong> — IDoc control, data, and status records.</li>
      <li><strong>WE20</strong> — partner-profile context; inspect before proposing a configuration change.</li>
      <li><strong>BD87</strong> — IDoc status monitoring and controlled reprocessing where applicable.</li>
      <li><strong>AIF Monitoring and Error Handling</strong> — use the AIF application configured for the interface and release; `/AIF/ERR` is common in SAP GUI landscapes.</li>
      <li><strong>SXI_MONITOR / SXMB_MONI</strong> — on-premise XI / PI Integration Engine message monitoring.</li>
      <li><strong>Monitor Message Processing</strong> — SAP Cloud Integration runtime messages and message processing logs.</li>
      <li><strong>SLG1 or the application object</strong> — application evidence where the relevant process records it.</li>
    </ul>

    <h2>Interview exercise: three monitors, one message</h2>
    <p><strong>Synthetic case.</strong> Cloud Integration reports a completed message. WE02 shows an inbound IDoc in status 51. An AIF search returns no result because it is filtered to a different interface version. The user reports that no order exists.</p>
    <ol>
      <li>State what each observation proves and what remains unproven.</li>
      <li>Name the evidence needed to show that the three records refer to the same business message.</li>
      <li>Choose the next diagnostic action and explain why an immediate resend is unsafe.</li>
    </ol>
    <details class="study-review">
      <summary>Review the evidence boundaries</summary>
      <p>The completed Cloud Integration message proves that its configured flow completed according to that monitor; it does not prove application posting. Inbound IDoc status 51 is application-error evidence in the receiver. The empty AIF result is explained by the current selection and says nothing yet about whether the interface is otherwise visible in AIF.</p>
      <p>Correlate the records with the available message or correlation identifiers, business key, sender and receiver, message type, and timestamps. Then read the full status 51 message and the relevant application evidence. Check whether any business object was created before deciding on correction and controlled reprocessing.</p>
      <p><strong>Change the condition:</strong> if WE02 has no matching IDoc after correcting the receiver search, move the next check back to the preceding hop and receiver hand-off evidence. The same recovery answer no longer follows.</p>
    </details>

    <h2>Source checks</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/34a0e9694fce4beaa5a20765b93a1a52.html?locale=en-US&amp;state=PRODUCTION&amp;version=202310.001">SAP AIF: Technology Support</a> — supported technologies have different monitoring and runtime scopes.</li>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/xi/3362976904.html">SAP: Important Transaction Codes in XI</a> — identifies SXI_MONITOR as XI message monitoring and SXMB_MONI as Integration Engine monitoring.</li>
      <li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/monitor-message-processing?locale=en-US">SAP Cloud Integration: Monitor Message Processing</a> — describes the Cloud Integration operations view and message processing details.</li>
    </ul>
    <p>Sources were checked on 12 September 2026. Exact applications, transaction availability, and recovery functions remain release- and landscape-dependent. The page stays noindex until human verification.</p>

    <h2>Support takeaway</h2>
    <p>A useful handover names the failing checkpoint, the evidence source, the correlation method, and the expected business outcome. Include system and client, direction, interface or message type, partner, timestamps and time zone, record identifiers, complete error text, affected business key, original outcome, and whether the issue repeats. “Fix the IDoc” or “AIF is empty” is not yet a diagnosis.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a transaction-by-transaction configuration guide. It does not claim that every landscape uses AIF, PI/PO, Cloud Integration, identical partner profiles, or the same recovery functions. Validate the actual route and release documentation before changing configuration or replaying messages.</p>

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

- [ ] Check WE02/WE05 for the control record, data records, status history, and full error text.

- [ ] Review partner profile (WE20), port, and process code for the message type.

- [ ] Use AIF Monitoring and Error Handling only when AIF is configured for the interface; use SXI_MONITOR/SXMB_MONI for the relevant on-premise XI/PI path, or Monitor Message Processing for Cloud Integration.

- [ ] Confirm whether the failure is isolated to one partner, plant, message type, or time window.

- [ ] Document recent changes: transports, master data updates, partner profiles, or network.

- [ ] Safety limit: do not mass-reprocess until the failing checkpoint, original outcome, scope, order, and duplicate risk are known.
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
