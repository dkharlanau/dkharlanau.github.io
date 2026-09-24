---
layout: default
title: "SAP Integration Suite"
description: "SAP Integration Suite explained: Cloud Integration, API Management, events, B2B integration, connectivity, and where each capability fits."
permalink: /atlas/sap/sap-integration-suite/
atlas_section: sap
domain: SAP operations
subdomain: Integration middleware
concept_type: product
sap_area: "Integration Suite"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-integration-suite
  - middleware
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/business-events/
  - /atlas/sap/idoc/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/idempotency/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Integration Suite</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Integration Suite</h1>
    <p class="note-subtitle">SAP BTP integration capabilities for process integration, APIs, events, B2B exchange, and hybrid runtime needs.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>Integration Suite</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Integration Suite is SAP's modular integration platform on SAP BTP. The important point is that it is not one middleware runtime with several names. Its capabilities solve different integration problems: Cloud Integration processes messages, API Management governs APIs, event capabilities broker asynchronous communication, Integration Advisor and Trading Partner Management support B2B work, and other capabilities cover areas such as non-SAP connectivity, data spaces, migration assessment, and private runtime requirements.</p>

    <p>A useful design starts with the interaction we need rather than with the product menu. Are we moving a message between two applications, exposing a stable API to many consumers, distributing an event without waiting for a response, or managing partner-specific B2B agreements? Those choices lead to different artifacts, runtime behavior, and operational evidence.</p>

    <h2>Cloud Integration processes message flows</h2>
    <p>Cloud Integration is the message-processing capability. An integration flow receives a message through a sender adapter, applies steps such as routing, mapping, transformation, or calls to other systems, and sends the result through one or more receiver adapters. SAP provides adapters for SAP and non-SAP protocols and applications, while message monitoring records how deployed flows behave at runtime.</p>

    <p>The integration flow can decouple systems technically, but it does not remove the business contract between them. We still need to know which system owns each field, which identifier makes a message unique, whether the exchange is synchronous or asynchronous, what a retry is allowed to repeat, and how a failed message is reconciled with the business object.</p>

    <p>For example, a customer update from a CRM system to SAP S/4HANA may need mapping and routing in Cloud Integration. The flow can transform the payload and handle transport errors, but SAP S/4HANA still decides whether the requested business change is valid. A technically successful integration message and a correct business result are therefore related but not identical facts.</p>

    <h2>API Management governs a consumer-facing API</h2>
    <p>API Management addresses a different boundary. It can place a managed API in front of an existing backend service or integration endpoint and apply policies for concerns such as authentication, authorization, traffic control, monitoring, and selected transformations. API products, subscriptions, analytics, and Developer Hub capabilities support the producer-consumer lifecycle around that endpoint.</p>

    <p>This does not move the business operation into the gateway. A proxy can authenticate a caller and control traffic before forwarding the request, while the provider still owns the business semantics and the authorization required to execute the operation. Keeping that boundary clear makes it much easier to understand whether a failure belongs to the consumer, API policy, connectivity, integration logic, or backend application.</p>

    <p><strong>API Composition</strong> is another current Integration Suite capability and should not be reduced to an API proxy. SAP documents it as a way to expose semantically connected business data through a business data graph and an OData V4 API. That is a data-access composition model, whereas classic API Management is primarily about managing and governing APIs that already have a provider contract.</p>

    <h2>Events change the interaction model</h2>
    <p>For event-driven integration, SAP Integration Suite includes event-broker capabilities, including Advanced Event Mesh. Here a producer publishes an event and consumers react through brokered subscriptions instead of holding a synchronous request open for a response. This is useful when several consumers should react independently or when the producer should not know every downstream process.</p>

    <p>The broker does not define the business meaning of the event for us. Event name, payload, versioning, delivery expectations, duplicate handling, ordering requirements, and consumer recovery still need explicit design. Those details matter more than whether the initial event left the source system successfully.</p>

    <h2>B2B integration has partner-specific design objects</h2>
    <p>B2B integration adds another layer of variability because the same business transaction can use different message standards, mappings, identifiers, certificates, and communication agreements for different partners. Integration Advisor supports interface and mapping design with artifacts such as Message Implementation Guidelines and Mapping Guidelines. Trading Partner Management keeps partner profiles and agreements that describe how a company exchanges B2B messages with each partner.</p>

    <p>These capabilities complement Cloud Integration rather than replace it. The design-time artifacts and partner agreements help define the exchange; runtime integration content still has to receive, transform, route, send, and monitor the actual messages. This separation is important when troubleshooting: a mapping defect, an expired partner certificate, and a failed runtime delivery are three different problems even if they affect the same purchase order or invoice.</p>

    <h2>Specialized capabilities should stay specialized</h2>
    <p>Open Connectors provides prebuilt connectivity to supported non-SAP cloud applications. Data Space Integration is for offering, consuming, and maintaining assets in a data space. Prepackaged integration content can accelerate common scenarios. These capabilities can reduce implementation effort, but they do not remove the need to understand data ownership, security, retries, monitoring, or release dependencies in the target landscape.</p>

    <p>The same rule applies to prebuilt integration packages: they are implementation assets, not proof that the local architecture is correct. Before adopting one, we still need to understand its message contract, dependencies, extension points, operational model, and what happens when either endpoint changes.</p>

    <h2>Cloud and edge are runtime choices</h2>
    <p>In the standard deployment model, integration content runs in SAP-managed cloud runtimes on SAP BTP. SAP also provides <strong>Edge Integration Cell</strong> as a hybrid runtime for supported integration flows and API artifacts in a customer-managed private landscape. SAP documents the model as cloud-based design and monitoring with execution in the customer's Kubernetes environment.</p>

    <p>That is different from SAP Cloud Connector. Cloud Connector provides controlled connectivity from SAP BTP services to resources in a private network; it is not a private Integration Suite runtime. A standard cloud integration may use Cloud Connector for supported on-premise communication, while an Edge Integration Cell actually executes supported integration content inside the private landscape. The runtime choice therefore changes the operational boundary, not just the network route.</p>

    <h2>PI/PO migration is an assessment and redesign exercise</h2>
    <p>SAP provides Migration Assessment to analyze supported SAP Process Integration and SAP Process Orchestration scenarios, and Migration Tooling can convert supported objects through pattern-based migration into Integration Suite artifacts. Neither capability means that an entire PI/PO estate can be renamed and moved unchanged.</p>

    <p>SAP documents important assessment limits, including areas where custom adapters, custom code dependencies, BPM logic, or cross-interface dependencies need additional analysis. A sensible modernization therefore separates interfaces that can be migrated with limited change from interfaces that should be redesigned around APIs, events, B2B capabilities, or a different runtime model.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite">SAP Integration Suite documentation and current capability scope</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/runtimes">Deployment Options and Runtimes</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/graph-odata-v4-api">API Composition OData V4 API</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/what-is-migration-tooling">Migration Tooling</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf">SAP BTP Connectivity documentation</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP changes Integration Suite capabilities, service plans, regional availability, quotas, runtime profiles, and feature scope over time. Verify the exact service plan and runtime used in the target landscape before turning these architectural boundaries into a detailed solution design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/business-events/">Business Events</a></li>
      <li><a href="/atlas/sap/idoc/">IDoc</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
