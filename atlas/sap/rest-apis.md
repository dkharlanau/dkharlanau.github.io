---
layout: default
title: "REST APIs"
description: "Analytical overview of REST APIs in SAP: what they are, where they sit, and how they break."
permalink: /atlas/sap/rest-apis/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "REST APIs"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - rest-api
  - openapi
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/odata/
  - /atlas/sap/soap/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">REST APIs</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>REST APIs</h1>
    <p class="note-subtitle">HTTP-based integration standard for lightweight, stateless service communication in SAP landscapes.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>REST APIs</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>REST (Representational State Transfer) is the dominant architectural style for modern API design. It uses standard HTTP methods (GET, POST, PUT, PATCH, DELETE), JSON payloads, and resource-oriented URLs. OpenAPI (formerly Swagger) provides a machine-readable contract for discovery and code generation.</p>

    <h2>Business purpose</h2>
    <p>Enable lightweight, scalable integration between SAP systems, cloud services, and external applications. Support mobile and web frontends, microservice architectures, and third-party developer ecosystems.</p>

    <h2>Where it sits in the landscape</h2>
    <p>REST APIs are the preferred interface layer for new development. In SAP, they are exposed via CAP services, BTP API Management, Integration Suite, and custom microservices. They coexist with OData (which is REST-like but protocol-specific) and legacy SOAP services.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Resource endpoint: URL representing a business entity.</li>
      <li>HTTP method: operation semantics (GET for read, POST for create, etc.).</li>
      <li>JSON payload: request and response body format.</li>
      <li>OpenAPI spec: contract describing paths, schemas, and security.</li>
      <li>Authentication token: OAuth2, API key, or mutual TLS.</li>
      <li>Idempotency key: client-generated token for safe retries.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: custom REST services, CDS-based exposure.</li>
      <li>BTP: CAP services, API Management, Kyma microservices.</li>
      <li>Integration Suite: REST adapter, API proxying.</li>
      <li>External: mobile apps, web frontends, partner APIs, cloud services.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom REST services in ABAP or CAP.</li>
      <li>API gateway policies: rate limiting, transformation, caching.</li>
      <li>OpenAPI generation from CDS or manual authoring.</li>
      <li>Side-by-side microservices on BTP or Kyma.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>HTTP status codes: 4xx client errors, 5xx server errors.</li>
      <li>Response time and throughput: latency percentiles, RPS.</li>
      <li>API gateway logs: request/response tracing, policy violations.</li>
      <li>Authentication failures: token expiry, scope mismatch.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Simple, widely understood, and tooling-rich.</li>
      <li>Statelessness enables horizontal scaling.</li>
      <li>JSON is compact and human-readable.</li>
      <li>OpenAPI enables automated client generation and documentation.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>No built-in transactionality across distributed calls.</li>
      <li>Over-fetching or under-fetching compared to OData or GraphQL.</li>
      <li>Security: exposed endpoints require rigorous authentication and input validation.</li>
      <li>Versioning: breaking changes affect all consumers.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>401/403 errors — token expiry, misconfigured OAuth, or scope issue.</li>
      <li>500 errors — unhandled exception in custom service logic.</li>
      <li>Timeout — downstream system slow or unreachable.</li>
      <li>Rate limiting — consumer exceeds quota or burst threshold.</li>
      <li>Payload mismatch — schema change without consumer update.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
      <li><a href="/atlas/sap/soap/">SOAP</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP BTP API Management — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management">SAP Help Portal</a>.</li>
      <li>SAP CAP REST Services — <a href="https://cap.cloud.sap/docs/">CAP Documentation</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. REST API availability, gateway features, and security policies vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
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
