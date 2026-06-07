---
layout: default
title: "SAP Integration Suite"
description: "Analytical overview of SAP Integration Suite: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-integration-suite/
atlas_section: sap
domain: SAP operations
subdomain: Integration middleware
concept_type: product
sap_area: "Integration Suite"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
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
    <p class="note-subtitle">Cloud integration platform for APIs, events, and prebuilt integrations.</p>
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
    <h2>What it is</h2>
    <p>SAP Integration Suite is a cloud-based integration platform that provides API management, integration flows, event mesh, data integration, and prebuilt integration content. It connects S/4HANA to SAP and non-SAP systems.</p>

    <h2>Business purpose</h2>
    <p>Reduce custom middleware by providing prebuilt integrations, standard protocols, and managed connectivity. Enable real-time and batch integration between cloud and on-premise systems.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Integration Suite runs on SAP BTP. It sits between S/4HANA and satellite products (Ariba, EWM, TM, etc.), as well as external systems. It replaces or complements on-premise middleware like SAP PI/PO.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Integration flow: message routing, transformation, mapping.</li>
      <li>API: REST, OData, SOAP exposure and management.</li>
      <li>Event mesh: topic, subscription, event producer/consumer.</li>
      <li>Prebuilt package: integration content for specific scenarios.</li>
      <li>Connection: adapter, credential, endpoint.</li>
      <li>Monitoring dashboard: message status, error, retry.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData, RFC, IDoc, business events.</li>
      <li>Satellite products: Ariba, EWM, TM, IBP, Datasphere.</li>
      <li>Non-SAP: REST, SOAP, JDBC, file, cloud storage.</li>
      <li>Event mesh: SAP and third-party event producers.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom integration flows and mappings.</li>
      <li>Custom API policies and rate limiting.</li>
      <li>Event mesh topic extensions.</li>
      <li>Side-by-side integration monitoring apps.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Message monitoring: processed, failed, retrying.</li>
      <li>API health: latency, error rate, throughput.</li>
      <li>Event mesh: topic lag, consumer health.</li>
      <li>Integration content: version, update, deprecation.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Prebuilt integration content reduces development time.</li>
      <li>Managed service reduces infrastructure overhead.</li>
      <li>Unified platform for API, event, and data integration.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Cloud-to-on-premise connectivity depends on cloud connector.</li>
      <li>Prebuilt content may not cover custom scenarios.</li>
      <li>Message volume and complexity affect pricing.</li>
      <li>Error handling and retry logic require careful design.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Integration flow failed — mapping, connection, or payload.</li>
      <li>API timeout — backend slow or network issue.</li>
      <li>Event not delivered — topic misconfiguration or consumer down.</li>
      <li>Cloud connector down — on-premise system unreachable.</li>
      <li>Certificate expired — SSL handshake failure.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/business-events/">Business Events</a></li>
      <li><a href="/atlas/sap/idoc/">IDoc</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Integration Suite features, prebuilt content, and pricing vary by release and must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/business-events/">Business Events</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
