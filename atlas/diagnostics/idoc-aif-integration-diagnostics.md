---
layout: default
title: "IDoc and AIF Integration Diagnostics"
description: "Diagnose IDoc and SAP AIF integration failures by separating IDoc runtime, AIF monitoring, middleware evidence, and the receiver's business outcome."
permalink: /atlas/diagnostics/idoc-aif-integration-diagnostics/
last_modified_at: 2026-09-24
atlas_section: diagnostics
domain: SAP operations
subdomain: Integration diagnostics
concept_type: diagnostic guide
sap_area: IDoc / AIF / integration
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-09-24
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
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
  - /atlas/diagnostics/sap-qrfc-trfc-diagnostics/
  - /atlas/diagnostics/sap-inbound-processing-diagnostics/
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
    <p class="note-subtitle">First determine who processed the message, who only monitored it, and where the business outcome stopped.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>IDoc / AIF / integration</dd></div>
      <div><dt>Indexing</dt><dd>Noindex pending human verification.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>An integration incident becomes confusing when every monitor is treated as another copy of the same truth. An IDoc record, an SAP Application Interface Framework (AIF) message, a middleware execution, and the final business object describe different parts of the route. A green middleware message can coexist with an inbound IDoc error. An IDoc can also be visible in AIF even when AIF did not process it.</p>

    <p>The first question is therefore not “Which monitor is red?” It is <strong>which component actually owned this step of execution?</strong> Once that is clear, each monitor has a precise job.</p>

    {% include article-visual.html %}

    <h2>Draw the execution path before opening more monitors</h2>
    <p>A useful trace starts with the configured route, not with a standard list of SAP transactions. Depending on the landscape, a business message may move directly through the IDoc runtime, pass through SAP Integration Suite or another middleware product, be monitored by AIF, be processed by AIF, or use several of those components.</p>

    <p>Do not draw AIF as a mandatory layer between an IDoc and the application. SAP supports several AIF IDoc scenarios. In one common scenario, the standard ALE runtime processes an existing IDoc while AIF provides Monitoring and Error Handling on top of it. In other scenarios, the IDoc is passed into the AIF runtime, where mappings, checks, value mappings, and actions can participate in processing. The same product name therefore represents two very different diagnostic roles.</p>

    <p>That distinction changes the next step. If ALE processed the IDoc and AIF only monitors it, the IDoc status history remains the primary runtime evidence. If AIF processed the message, its interface configuration and runtime log can be part of the failing execution itself.</p>

    <h2>Give each evidence source one job</h2>
    <table>
      <thead>
        <tr><th>Evidence</th><th>What it can establish</th><th>What it does not establish alone</th></tr>
      </thead>
      <tbody>
        <tr><td>WE02 / WE05</td><td>An IDoc exists in this SAP system, with a direction, control record, payload, status history, and timestamps.</td><td>That a middleware hop completed or that the final business result is correct.</td></tr>
        <tr><td>AIF Monitoring and Error Handling</td><td>The configured AIF interface can select and display the message, with the keys, logs, and actions supported by that interface technology and engine setup.</td><td>That AIF necessarily processed the message. AIF can monitor IDocs processed by the standard IDoc runtime.</td></tr>
        <tr><td>Cloud Integration message monitor</td><td>A particular integration-flow execution reached the status shown by that runtime, with its message-processing details and identifiers.</td><td>That the receiving SAP application posted the intended business object.</td></tr>
        <tr><td>Receiver application evidence</td><td>The actual business outcome: for example, the created document, application status, or application log entry.</td><td>How an earlier transport or monitoring layer behaved unless the records are correlated.</td></tr>
      </tbody>
    </table>

    <p>Legacy PI/PO or another integration platform follows the same principle: use its monitor only if that runtime is actually on the route. A landscape diagram and one successful reference message are often more useful than opening every available monitor.</p>

    <h2>AIF visibility depends on the AIF scenario</h2>
    <p>SAP's current AIF documentation explicitly supports monitoring interfaces that are not processed by the AIF runtime. For existing IDocs, AIF can use IDoc-specific engines to read control records, data records, and status information from the standard IDoc runtime. The interface still needs the relevant AIF definition and technology setup so that AIF knows which IDocs belong to it.</p>

    <p>This makes an empty AIF result ambiguous. It can mean that no matching message is available, but it can also mean that the wrong namespace, interface, version, status, date range, or IDoc assignment was selected, or that this IDoc route was never configured for AIF monitoring. “Not found in AIF” is therefore not equivalent to “not created in SAP.” Check the IDoc runtime directly when the route uses IDocs.</p>

    <p>The reverse is also important. When the design deliberately processes an IDoc through AIF, AIF is no longer just a viewing layer. A failure may come from interface determination, mapping, checks, value mapping, or an action before the final application result is produced. The diagnostic path must follow that configured runtime instead of assuming standard ALE processing.</p>

    <h2>Correlate the message before comparing statuses</h2>
    <p>One business transaction can have several technical identifiers as it crosses systems. Do not assume that an outbound IDoc number in one SAP system will equal an inbound IDoc number in another system, or that a middleware message ID will equal either of them.</p>

    <p>Build the correlation from several pieces of evidence: sender and receiver, direction, message type and basic type, business key, timestamps with time zone, and any middleware message, correlation, or application identifier. SAP Cloud Integration can expose Message ID, Correlation ID, and Application ID in its message-processing logs, and custom header properties can be used for additional business-oriented search keys when the integration flow is designed to write them.</p>

    <p>The goal is not to collect every identifier. It is to prove that the records belong to the same business message. Only then does a sequence such as “middleware completed → inbound IDoc created → application posting failed” become an evidence chain rather than a guess.</p>

    <h2>Read success at the boundary where it occurred</h2>
    <p>A successful status is local to the component that reports it. If Cloud Integration shows a message as Completed, that establishes the result of that integration-flow execution. It does not prove that the receiver created the expected sales order, supplier invoice, delivery, or master-data object.</p>

    <p>The same rule applies inside the IDoc runtime. Standard inbound processing uses status records to describe its own progress. For example, SAP documents status 51 as an application document that was not posted and status 53 as an application document that was posted. Those statuses are much stronger receiver-side evidence than a successful upstream transport status, but even a posted IDoc should be followed to the referenced business object when a user reports the wrong business outcome.</p>

    <p>This boundary is the reason to stop reading from left to right once the first failed or unproven step is found. If an inbound IDoc already exists and has an application error, another sender-side resend usually adds noise. The useful evidence is now in the receiver's IDoc status and application context.</p>

    <h2>A concrete trace: middleware completed, IDoc failed, AIF is empty</h2>
    <p>Consider a message for which Cloud Integration shows <strong>Completed</strong>, the receiving SAP system contains an inbound IDoc in status <strong>51</strong>, and an AIF search returns no result.</p>

    <p>The three observations do not conflict. The middleware execution completed at its boundary. The correlated inbound IDoc reached the receiver but the application document was not posted. The empty AIF search says only that the current AIF selection did not return the message; it does not overturn the IDoc evidence.</p>

    <p>At this point, read the full IDoc status text and the application evidence behind it. Determine whether the cause is business data, master data, configuration, or application logic. In parallel, establish how AIF is configured for this interface. If AIF is only meant to monitor existing IDocs, fix the AIF selection or interface definition separately from the posting error. If AIF is the runtime for this route, its own processing log becomes part of the root-cause analysis.</p>

    <p>This is a better diagnostic result than “AIF is broken” or “Cloud Integration says success.” It identifies two different questions: why the business posting failed, and why the monitoring view did not show the same technical message.</p>

    <h2>Recover from the first failed boundary, not from the source by default</h2>
    <p>Before any retry, establish what already exists. Check whether the receiver has an IDoc, whether an application object was partly or fully created, whether ordering matters, and whether a retry can create a duplicate. Then use the recovery function supported by that interface technology and status.</p>

    <p>AIF restart and cancel functions depend on the interface technology and configured engines; they are not universal controls for every message shown in AIF. IDoc recovery is likewise status- and scenario-specific. The <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">IDoc Status Diagnostics</a> page covers the standard status boundary in more detail.</p>

    <p>If no receiver-side record exists, move one hop upstream and prove the hand-off from middleware or the sending IDoc runtime. If the receiver already contains the failed message, prefer correcting the failing receiver-side condition over creating another copy from the source unless the process design explicitly requires a resend.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Application Interface Framework 2025 FPS01 — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/34a0e9694fce4beaa5a20765b93a1a52.html">Technology Support</a>.</li>
      <li>SAP Application Interface Framework 2025 FPS01 — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/25ab6783bdd04abd912d5cf398a8b4ac.html">Monitor Existing IDocs in Monitoring and Error Handling</a>.</li>
      <li>SAP Application Interface Framework 2025 FPS01 — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/95ac643f35a149b285a6c4117cc61401.html">IDoc Structure Generation and Interface Definition</a>.</li>
      <li>SAP IDoc Interface/ALE 2025 FPS01 — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/8f3819b0c24149b5959ab31070b64058/4b4c3bba3b71265ce10000000a421937.html">Testing Inbound Processing</a>.</li>
      <li>SAP Cloud Integration — <a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/monitor-message-processing">Monitor Message Processing</a>.</li>
      <li>SAP Integration Suite — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/use-custom-header-properties-to-search-for-message-processing-logs">Use Custom Header Properties to Search for Message Processing Logs</a>.</li>
    </ul>
    <p>Sources were checked on 24 September 2026. Exact AIF engines, recovery actions, middleware monitors, and IDoc processing modes remain release- and landscape-dependent. The page remains noindex until human verification.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains how to separate runtime and monitoring evidence across an IDoc/AIF integration path. It is not a partner-profile configuration guide, an AIF implementation guide, or a catalogue of IDoc status codes. For a broad monitoring design, use <a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">Interface Monitoring Diagnostics</a>; for status-specific IDoc analysis, use <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">IDoc Status Diagnostics</a>.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC and tRFC Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
