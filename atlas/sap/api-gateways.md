---
layout: default
title: "API Gateways"
description: "Analytical overview of API Gateways in SAP: what they are, where they sit, and how they break."
permalink: /atlas/sap/api-gateways/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "API Gateways"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - api-gateway
  - api-management
  - microservices
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/rest-apis/
  - /atlas/sap/odata/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">API Gateways</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>API Gateways</h1>
    <p class="note-subtitle">Traffic management, security, and analytics layer for API exposure in SAP and hybrid landscapes.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>API Gateways</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>An API gateway is a reverse proxy that sits between API consumers and backend services. It handles request routing, authentication, rate limiting, caching, transformation, and analytics. In SAP landscapes, it centralizes control over OData, REST, and SOAP service exposure.</p>

    <h2>Business purpose</h2>
    <p>Protect backend services from direct exposure. Enforce consistent security policies, throttle traffic, and provide usage analytics. Enable developer portals for internal and external API consumers.</p>

    <h2>Where it sits in the landscape</h2>
    <p>API gateways sit at the edge of the integration layer, fronting S/4HANA OData services, BTP microservices, and third-party APIs. SAP API Management on BTP is the native option; third-party gateways (Kong, Apigee, AWS API Gateway) are common in multi-cloud setups.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>API proxy: gateway representation of a backend service.</li>
      <li>Policy: rate limit, quota, caching, transformation rules.</li>
      <li>Product: bundled APIs with usage plans.</li>
      <li>Developer portal: consumer onboarding and documentation.</li>
      <li>Analytics: call volume, latency, error rate, consumer identity.</li>
      <li>Key/credential: API key, OAuth client, or certificate.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData service exposure with policy enforcement.</li>
      <li>BTP: API Management, Integration Suite API policies.</li>
      <li>Kyma: Istio ingress gateway for microservice fronting.</li>
      <li>External: third-party gateways, cloud provider API services.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom policies: JavaScript, XSLT, or plugin-based.</li>
      <li>Developer portal branding and documentation.</li>
      <li>Analytics export to external monitoring systems.</li>
      <li>Multi-gateway federation across cloud and on-premise.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Gateway logs: request/response tracing, policy execution.</li>
      <li>Latency percentiles: p50, p95, p99 per API.</li>
      <li>Error rate: 4xx/5xx breakdown by consumer and API.</li>
      <li>Quota exhaustion: rate limit and throttle events.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Centralized security and traffic control.</li>
      <li>Decouples consumers from backend changes.</li>
      <li>Rich analytics for usage and performance insights.</li>
      <li>Developer portal improves API discoverability.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Additional latency from proxy hop.</li>
      <li>Single point of failure if not clustered.</li>
      <li>Policy complexity can obscure root cause during incidents.</li>
      <li>License and infrastructure cost for high-throughput scenarios.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>429 errors — consumer exceeds rate limit or quota.</li>
      <li>502/504 errors — backend down or gateway timeout.</li>
      <li>Authentication failure — expired key, revoked credential.</li>
      <li>Policy misconfiguration — wrong transformation or routing rule.</li>
      <li>Analytics gap — logging disabled or misrouted.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/rest-apis/">REST APIs</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP BTP API Management — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management">SAP Help Portal</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. API gateway features, policy types, and integration mechanisms vary by release and must be verified against the customer's system.</p>

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
