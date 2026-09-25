---
layout: default
title: "Integration Monitoring"
description: "SAP integration monitoring explained: how to follow messages across source, middleware, receiver, and business outcome using local evidence and SAP Cloud ALM."
permalink: /atlas/sap/integration-monitoring/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "Integration Monitoring"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - monitoring
  - integration-health
  - observability
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/idoc/
  - /atlas/sap/odata/
  - /atlas/sap/business-events/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Integration Monitoring</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>Integration Monitoring</h1>
    <p class="note-subtitle">Following one business exchange through source application, transport, receiver, and business posting.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>Integration Monitoring</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>Integration monitoring is not one dashboard. It is the work of reconstructing an exchange across several ownership boundaries and proving how far the business message actually travelled. A useful trace connects the source business event, the transport or middleware run, the receiver's technical acceptance, and the final business result.</p>

    <p>This distinction matters because each component can be healthy while the end-to-end process is still incomplete. A middleware flow can finish its own processing successfully even though a later asynchronous step fails. An HTTP request can return a technically valid response while the expected business object is still rejected, delayed, or processed elsewhere. Monitoring becomes useful when it separates those facts instead of reducing them to one red or green status.</p>

    <h2>Follow the exchange through ownership boundaries</h2>
    <p>For most incidents, the fastest question is not “Which monitoring tool should we open?” but “What is the last handoff we can prove?” A typical path may look like this:</p>

    <ol>
      <li>The source application creates or changes a business object and triggers an outbound exchange.</li>
      <li>A protocol, queue, adapter, or middleware runtime accepts the message.</li>
      <li>Integration logic may map, route, enrich, split, or call another endpoint.</li>
      <li>The receiving technical interface accepts or rejects the request.</li>
      <li>The target application turns that request into a business result.</li>
    </ol>

    <p>Each step leaves different evidence. An IDoc has its own status history. An OData call has an HTTP response and backend application behavior. SAP Integration Suite has message processing logs for Cloud Integration. The target application may have a business document, application log, workflow state, or another processing queue. These records complement each other; none of them automatically proves every other step.</p>

    <h2>Cloud Integration records what its runtime did</h2>
    <p>For Cloud Integration, the message processing log (MPL) is the main runtime record. SAP documents MPL data for messages processed on a tenant together with information about individual processing steps. The detailed log can show the integration flow, processing status, duration, run steps, properties, and error information.</p>

    <p>The amount of evidence depends on configuration. In particular, SAP states that message content can be reviewed only when the log level is set to <strong>Trace</strong>. We should therefore not assume that a failed production message always has a stored payload snapshot. Trace data is useful for a focused investigation, but monitoring design should not depend on permanently retaining detailed payloads.</p>

    <p>An MPL also describes the middleware boundary, not the whole business process. If the flow sends a request to another system, we still need to establish what the receiver accepted and what the target application did with it. A completed middleware run is evidence that the runtime completed its work; it is not, by itself, proof that the downstream business outcome is correct.</p>

    <h2>Correlation works only when identifiers survive the path</h2>
    <p>One of the hardest parts of integration support is finding the same business exchange in several systems. Cloud Integration provides several identifiers for different purposes. A <strong>Message ID</strong> identifies a message processing log. A <strong>Correlation ID</strong> can connect messages that are processed together in an integration scenario. An <strong>Application Message ID</strong> can be supplied through the <code>SAP_ApplicationID</code> header, and a <strong>Predecessor ID</strong> can link supported chains of integration-flow calls.</p>

    <p>These identifiers do not create universal end-to-end tracing automatically. SAP explicitly documents, for example, that HTTP inbound and outbound processing logs need the correlation ID to be passed through the flow when we want to correlate them. Predecessor links also have adapter and flow-pattern restrictions. For many business interfaces, the most useful operational key is therefore a deliberately preserved business identifier such as an order number, IDoc number, application message ID, or another stable reference.</p>

    <p>The identifier should be chosen before an incident occurs. If every component invents a new unrelated technical ID, support teams are forced to correlate by time, payload, and guesswork. If the same business key can be searched safely at important boundaries, the investigation becomes much faster without requiring the full business payload to be copied into every log.</p>

    <h2>SAP Cloud ALM can add a cross-system view</h2>
    <p>SAP Cloud ALM provides <strong>Integration &amp; Exception Monitoring</strong> for supported systems, services, and integration scenarios. SAP describes it as a way to collect integration artifacts, monitor messages and exceptions, correlate supported end-to-end message flows, and combine monitoring with alerting and analysis.</p>

    <p>The word <em>supported</em> is important. Coverage is not automatic for every interface in a landscape. SAP Cloud ALM requires managed components and data collection to be configured, and the available message categories and monitoring detail depend on the product and scenario. A central view therefore complements the local monitor; it does not make component-level evidence unnecessary.</p>

    <p>This gives us two useful levels of observation. The central monitor helps answer “Where in the end-to-end flow is the problem visible?” The local component monitor answers “What exactly did this runtime or application do?” Strong operations use both levels instead of forcing every diagnosis into one tool.</p>

    <h2>Diagnose from the last confirmed handoff</h2>
    <p>Consider an outbound customer update that should pass through Cloud Integration into SAP S/4HANA. If the source confirms that the outbound message was created but there is no matching MPL, investigate the handoff into the integration runtime. If the MPL exists and fails during mapping or the receiver call, the middleware record gives the next technical boundary. If the MPL completes but SAP S/4HANA has no expected business change, move the investigation to the receiver response, inbound processing, and target business state rather than repeatedly restarting the integration flow.</p>

    <p>This order keeps diagnosis evidence-based. We first prove that an object or message existed, then prove each handoff, and only then analyze the failing component. It also reduces unsafe reprocessing. Retrying an exchange before we know whether the receiver already committed the business change can create duplicates or conflicting state in interfaces that are not designed for replay.</p>

    <h2>Monitoring data needs its own operating rules</h2>
    <p>Operational evidence has a lifecycle. Log level, retention, access permissions, data collection, and storage settings affect what will still be available when an incident is investigated. Payloads and business identifiers may also contain sensitive information, so more logging is not automatically better monitoring.</p>

    <p>A practical monitoring design keeps enough identifiers and status evidence to reconstruct the path, captures detailed payload data only when justified, and knows which component is authoritative for each step. That is more durable than a large dashboard whose metrics cannot be connected back to a real business exchange.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/message-processing-logs">Cloud Integration: Message Processing Logs</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/using-ids-to-filter-messages?locale=en-US&amp;version=LATEST">Cloud Integration: Using IDs to Filter Messages</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/cloud-alm/applicationhelp/configuring-integration-monitoring">SAP Cloud ALM: Configuring Integration &amp; Exception Monitoring</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/sap-btp-guidance-framework/integration-architecture-guide/end-to-end-integration-monitoring">Integration Architecture Guide: End-to-End Integration Monitoring</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Supported monitoring objects, correlation behavior, collected fields, retention, alerting, and setup steps vary by SAP product, runtime, tenant configuration, and release. Verify the actual managed component and interface scenario before treating a central monitor as complete end-to-end coverage.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
