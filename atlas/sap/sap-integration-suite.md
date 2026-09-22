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
last_reviewed: 2026-09-22
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
    <p class="note-subtitle">SAP BTP integration capabilities for process integration, APIs, events, B2B exchange, and hybrid connectivity.</p>
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
    <p>SAP Integration Suite is SAP's integration platform on SAP BTP. It is better understood as a set of related integration capabilities than as one universal middleware runtime. An integration architect chooses the capability that matches the interaction: process messages, govern APIs, exchange business events, connect trading partners, or reach non-SAP applications.</p>

    <h2>Cloud Integration handles message-based process integration</h2>
    <p>Cloud Integration is the part most people mean when they talk about integration flows. An integration flow can receive a message, route it, transform or map the payload, call one or more systems, and apply error-handling logic. Adapters provide connectivity for different protocols and applications.</p>

    <p>This makes Cloud Integration useful when the systems on both sides should remain decoupled from each other's technical details. It can connect SAP and non-SAP applications across cloud and on-premise landscapes, but the integration flow still needs an explicit contract: payload, identifiers, security, retry behavior, and ownership do not disappear because a managed integration service sits in the middle.</p>

    <h2>API Management solves a different problem</h2>
    <p>API Management is about exposing and governing APIs. Policies can control access, traffic, and other API behavior while developer-facing artifacts make APIs easier to discover and consume. It does not replace the business logic of the backend and it does not automatically turn every integration flow into a good public API.</p>

    <p>When an integration needs both mediation and API governance, the capabilities can work together. The architectural value comes from keeping the concerns visible: the backend implements business behavior, the integration layer mediates where necessary, and the API layer governs the consumer-facing contract.</p>

    <h2>Events, B2B, and connectors extend the platform beyond request-response flows</h2>
    <p>Integration Suite includes event capabilities for publishing and consuming business events, as well as capabilities for B2B integration such as Integration Advisor and Trading Partner Management. Open Connectors provides prebuilt connectivity to many non-SAP cloud applications. These are not interchangeable features; each addresses a different integration problem.</p>

    <p>SAP also provides Migration Assessment for assessing SAP Process Orchestration scenarios and Edge Integration Cell for selected customer-managed runtime requirements. This is a more useful way to think about modernization than saying that Integration Suite simply “replaces PI/PO.” A migration can preserve some interface contracts, redesign others, and use different Integration Suite capabilities depending on the scenario.</p>

    <h2>Prebuilt content is an accelerator, not the architecture</h2>
    <p>Integration packages and predefined content can shorten implementation time because common mappings, flows, and connectivity patterns do not always need to start from an empty canvas. But prebuilt content still runs inside a real landscape with local master data, extensions, security rules, error ownership, and release dependencies.</p>

    <p>We therefore treat prebuilt content as a starting point to understand and govern, not as a reason to skip interface design. The durable questions remain the same: what business event or message starts the flow, which system owns each field, how duplicates are prevented, what happens after a timeout, and how operations can trace a failed exchange.</p>

    <h2>Hybrid connectivity is part of the design</h2>
    <p>Cloud applications often need to reach systems inside a private network. SAP Cloud Connector is one option for controlled cloud-to-on-premise access, depending on the integration capability and protocol. Other deployment and connectivity options also exist, including Edge Integration Cell for supported scenarios. The network path should therefore be designed explicitly instead of assuming that every Integration Suite flow uses the same tunnel.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite">SAP Integration Suite documentation</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf">SAP BTP Connectivity documentation</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP changes Integration Suite capabilities, service plans, regional availability, quotas, and runtime options over time. Verify the current documentation and commercial entitlement for the exact capability before using this page for a solution design.</p>
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
