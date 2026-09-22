---
layout: default
title: "IDoc"
description: "SAP IDoc explained: message types, basic types, segments, inbound and outbound processing, status history, and ALE/EDI use."
permalink: /atlas/sap/idoc/
atlas_section: sap
domain: SAP operations
subdomain: Document integration
concept_type: integration
sap_area: "IDoc"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - idoc
  - edi
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
  - /atlas/concepts/retry-and-error-handling/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">IDoc</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>IDoc</h1>
    <p class="note-subtitle">A durable SAP message container for asynchronous application-to-application data exchange.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>An IDoc, or Intermediate Document, is a structured SAP message used to move business data between application processes. The format is deliberately separate from the way the application stores the same data internally. That makes an IDoc useful as an interface contract: the sender prepares a message in a known structure, the receiver processes that structure, and both sides can track what happened to the message.</p>

    <h2>Business meaning and technical structure are separate</h2>
    <p>Two terms are easy to mix up. The <strong>message type</strong> describes the business meaning of the exchange. The <strong>basic type</strong> describes the technical IDoc structure used to carry it. A basic type is built from segments, and each segment contains fields for part of the business data.</p>

    <p>An individual IDoc is an instance of that structure. It contains a control record with routing and technical information, one or more data records that contain the segment data, and status records that document processing steps. The status history is one reason IDocs remain useful in operational support: we can see that a message was created, transferred, accepted, rejected, or posted without treating integration as a single opaque call.</p>

    <h2>Outbound and inbound processing form two halves of the exchange</h2>
    <p>In outbound processing, an SAP application prepares the data, creates an IDoc, and dispatches it according to the configured distribution and partner settings. In inbound processing, the receiving SAP system stores the IDoc and then invokes application processing to turn the message into the corresponding business result.</p>

    <p>This is normally an asynchronous model. The sending business process does not need to behave like a synchronous API call that waits for the remote application to complete all of its work. ALE uses this model for distribution between logical systems, while EDI scenarios use the IDoc interface as a boundary between SAP application data and messages exchanged with external partners or subsystems.</p>

    <h2>Configuration tells SAP where a message belongs</h2>
    <p>The structure alone is not enough. Partner profiles describe how a particular sender or receiver participates in the exchange. Ports describe the communication endpoint or medium. Distribution settings and, in ALE scenarios, message types and filters determine which data should be sent to which logical system.</p>

    <p>That is why an apparently simple question such as “Why was no IDoc created?” can belong to several layers. The application may not have triggered the interface, the distribution rule may not select the receiver, or the outbound configuration may be incomplete. Once the IDoc exists, a different set of questions starts: was it dispatched, received, and posted successfully?</p>

    <h2>Status history is part of the interface, not an afterthought</h2>
    <p>IDoc processing records technical and application progress as statuses. A status should therefore be read in context rather than memorized as a universal error code list. Some statuses describe outbound processing, others inbound processing, and the useful next step depends on where the message currently is in the flow.</p>

    <p>For support work, the practical advantage is traceability. We can follow one document from creation through transport into application processing, then separate a communication problem from a business-data or posting problem. Reprocessing should follow that diagnosis; repeatedly restarting a failed IDoc without understanding the failed layer can simply reproduce the same error.</p>

    <h2>IDoc still has a clear place beside APIs and events</h2>
    <p>IDoc is not a lower layer underneath OData, SOAP, or business events, and those technologies do not automatically replace it. They are different interface styles. IDocs remain relevant where an established SAP business interface, asynchronous distribution, EDI exchange, or durable message-level processing fits the process. A new integration should choose its interface deliberately rather than treating age alone as an architectural decision.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/4ab38761549a6d8ce10000000a42189c.html">Message Distribution (IDoc Interface/ALE)</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_ERP_SPV/a428aae377ba4a1199c3ecc8b7f5f33d/3854b753128eb44ce10000000a174cb4.html">Electronic Data Interchange / IDoc Interface</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Exact message types, basic types, ports, triggering mechanisms, middleware paths, and reprocessing procedures depend on the business interface and SAP release. This page explains the durable IDoc model rather than a configuration recipe for one scenario.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
