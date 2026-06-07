---
layout: default
title: "SAP BTP"
description: "Analytical overview of SAP BTP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-btp/
atlas_section: sap
domain: SAP operations
subdomain: Business Technology Platform
concept_type: product
sap_area: "BTP"
business_process: "Platform and integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-btp
  - cloud-platform
  - extensions
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/cap/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/ai-ready-data-layer/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP BTP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP BTP</h1>
    <p class="note-subtitle">SAP's Business Technology Platform for extensions, integration, analytics, and AI.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Platform and integration</dd></div>
      <div><dt>SAP area</dt><dd>BTP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP BTP (Business Technology Platform) is SAP's cloud platform for extending SAP applications, integrating systems, running analytics, and building custom applications. It hosts side-by-side extensions that keep the S/4HANA core clean.</p>

    <h2>Business purpose</h2>
    <p>Extend SAP functionality without modifying the core. Integrate SAP with non-SAP systems. Run analytics, AI, and IoT workloads adjacent to the ERP. Provide a unified development and runtime environment.</p>

    <h2>Where it sits in the landscape</h2>
    <p>BTP sits alongside S/4HANA as the extension and integration layer. It connects to satellite products (Datasphere, Analytics Cloud, Integration Suite) and external systems. It is the platform for CAP, Kyma, Fiori, and SAP Build.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Subaccounts: organizational and operational boundaries.</li>
      <li>Spaces: development and deployment environments.</li>
      <li>Services: HANA Cloud, Integration Suite, Data Intelligence, AI Core.</li>
      <li>Applications: CAP apps, Fiori apps, SAP Build apps.</li>
      <li>Destinations: connectivity to S/4HANA and external systems.</li>
      <li>Cloud Foundry / Kyma: container runtime.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData, RFC, business events, cloud connector.</li>
      <li>Satellite products: Datasphere, Analytics Cloud, Integration Suite.</li>
      <li>External: REST, SOAP, OData, event mesh.</li>
      <li>Identity: SAP Cloud Identity, SAML, OAuth.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>CAP applications for business logic.</li>
      <li>Kyma for Kubernetes-native extensions.</li>
      <li>SAP Build for low-code apps and workflows.</li>
      <li>Fiori for user experience.</li>
      <li>AI Core for machine learning scenarios.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>BTP cockpit: service health, quota usage, application logs.</li>
      <li>Cloud Foundry: app logs, metrics, scaling events.</li>
      <li>Integration Suite: message monitoring, API health.</li>
      <li>HANA Cloud: performance, memory, connection status.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Keeps S/4HANA core clean via side-by-side extensions.</li>
      <li>Unified platform for development, integration, and analytics.</li>
      <li>Cloud-native runtime with elastic scaling.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Multiple subaccounts and services increase operational complexity.</li>
      <li>Cloud connector and network configuration are common failure points.</li>
      <li>Licensing and entitlement tracking across services.</li>
      <li>Latency between BTP and on-premise S/4HANA.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Cloud connector down — BTP cannot reach on-premise S/4HANA.</li>
      <li>Destination error — certificate, authentication, or network.</li>
      <li>Service quota exceeded — memory, disk, or API calls.</li>
      <li>Application crash — memory limit, dependency failure.</li>
      <li>Integration flow error — mapping, connection, or payload.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. BTP service availability, pricing, and feature scope vary by region and must be verified against SAP's current documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
