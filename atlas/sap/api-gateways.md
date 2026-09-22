---
layout: default
title: "API Gateways"
description: "API gateways in SAP landscapes explained: API proxies, policies, products, Developer Hub, and the role of SAP Integration Suite API Management."
permalink: /atlas/sap/api-gateways/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "API Gateways"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
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
    <p class="note-subtitle">A controlled layer between API consumers and backend services for security, traffic policies, lifecycle management, and observability.</p>
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
    <h2>The gateway sits between a consumer and an API</h2>
    <p>An API gateway is an intermediary that receives API calls before they reach the backend service. Instead of exposing every backend endpoint directly, the gateway can present a managed endpoint and apply common controls around it. Typical responsibilities include authentication and authorization, traffic policies, routing, monitoring, and lifecycle management.</p>

    <p>The gateway does not replace the business API. The backend still owns the actual business operation and data. The gateway controls how that API is exposed and consumed.</p>

    <h2>SAP API Management uses API proxies</h2>
    <p>In SAP Integration Suite, API Management represents a managed API through an <strong>API proxy</strong>. The proxy becomes the endpoint through which consumers call the service. Policies can be applied around that proxy to enforce security and traffic rules or to transform aspects of the interaction.</p>

    <p>This indirection is useful because the consumer does not need to know every backend detail. A backend host can change while the managed API contract remains stable, provided the proxy and API design preserve the external interface.</p>

    <h2>Management is broader than request routing</h2>
    <p>API Management is not only a reverse-proxy hop. SAP describes a broader lifecycle that includes API design, proxies, products, applications, analytics, and a Developer Hub. APIs can be grouped into products and published so developers can discover and consume them through a controlled catalog.</p>

    <p>This matters in larger landscapes. Without a management layer, teams may know that an OData or REST endpoint exists but still lack a clear answer to who may use it, which version is current, how usage is monitored, or how consumers discover the contract.</p>

    <h2>Policies should protect the contract, not hide a weak design</h2>
    <p>Gateway policies are useful for cross-cutting concerns such as authentication, quotas, traffic control, and selected transformations. They are less useful when they become a second application layer full of business logic. The more behavior is hidden in proxy configuration, the harder it becomes to understand where a response was changed or why two consumers see different behavior.</p>

    <p>We usually want the backend to remain responsible for business semantics and the gateway to remain responsible for exposure policy. That boundary makes incidents easier to reason about.</p>

    <h2>API gateway is not SAP Gateway</h2>
    <p>The terminology is easy to confuse. <strong>SAP Gateway</strong> in the ABAP stack is associated with exposing and consuming OData services in SAP systems. An <strong>API gateway</strong> or SAP Integration Suite API Management sits in front of APIs as a management and policy layer. One can expose an OData service and the other can manage how consumers reach it; they are not the same product or architectural role.</p>

    <h2>Where it helps in a hybrid landscape</h2>
    <p>A managed API layer is useful when several consumers need controlled access to SAP S/4HANA services, integration flows, BTP applications, or other enterprise APIs. It gives one place to apply exposure policies and observe usage without forcing every backend team to implement the same gateway concerns independently.</p>

    <p>It does add another runtime dependency. If a managed API is unavailable, we need to distinguish whether the problem is in the consumer, the proxy and its policies, network connectivity, or the backend service. Good observability should preserve that chain instead of reducing every failure to a generic gateway error.</p>

    <h2>Developer Hub makes APIs a consumable product</h2>
    <p>SAP Integration Suite includes Developer Hub as part of its API Management capabilities. Organizations can publish API products to a catalog where application developers can discover APIs and consume them through subscriptions. That moves API management beyond technical routing toward a governed producer-consumer relationship.</p>

    <p>The practical value is simple: an API is easier to reuse when its contract, lifecycle, access path, and ownership are visible. A gateway cannot create a good API by itself, but it can make a good API safer and easier to consume consistently.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/working-with-api-management">Working with API Management</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/api-proxy-states">API Proxy States</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/discover-and-publish-apis-from-integration-suite-on-developer-hub">Discover and Publish APIs From Integration Suite on Developer Hub</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Available policy types, limits, API lifecycle functions, runtime options, and Developer Hub behavior can change with SAP Integration Suite updates. Verify the exact capability and service plan used in the target tenant.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
