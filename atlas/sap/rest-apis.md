---
layout: default
title: "REST APIs"
description: "REST APIs in SAP landscapes explained: HTTP semantics, resource contracts, retries, OpenAPI, CAP, API Management, and the boundary with OData."
permalink: /atlas/sap/rest-apis/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "REST APIs"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
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
    <p class="note-subtitle">HTTP APIs built around resources and clear request semantics, with the business contract still owned by the application behind them.</p>
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
    <p>REST is an architectural style, not a SAP protocol and not a synonym for JSON. In practice, a REST API usually uses HTTP resources, standard request methods, status codes, headers, and representations such as JSON. The important part is the contract: what a resource means, which operations are allowed, and what a client can safely conclude from the response.</p>

    <h2>HTTP semantics are part of the API design</h2>
    <p>HTTP already gives request methods defined behavior. <code>GET</code> is safe: a client does not ask the server to change application state. <code>PUT</code>, <code>DELETE</code>, and the safe methods are idempotent at the HTTP-semantics level, which means repeating the same request is intended to have the same effect as sending it once. <code>POST</code> does not have that guarantee by default.</p>

    <p>This matters during failures. If a client sends a create request and loses the connection before receiving the response, it may not know whether the backend committed the change. Retrying a non-idempotent operation blindly can create duplicates. Some APIs solve this with a business key, request token, or explicit idempotency mechanism, but that is an API-specific contract rather than a universal REST feature.</p>

    <h2>JSON and OpenAPI are useful, but neither defines REST</h2>
    <p>JSON is common because it is easy to process in web and cloud applications, but HTTP can carry other representations. OpenAPI is also separate from REST itself. It can describe paths, operations, request and response schemas, authentication schemes, and other parts of an HTTP API in a machine-readable form.</p>

    <p>An OpenAPI document improves discoverability and tooling only when it matches the runtime behavior. A generated client is not protected from a backend that changes field meaning, error behavior, authorization rules, or retry semantics without updating the contract.</p>

    <h2>In SAP, name the actual interface instead of calling everything REST</h2>
    <p>SAP landscapes contain several HTTP-based API styles. OData is RESTful, but it is a defined protocol with its own metadata, query options, entity model, and version-specific behavior. Current RAP service bindings expose Web APIs through supported protocols such as OData; an OData Web API should therefore be described as OData rather than flattened into the vague label “REST API.”</p>

    <p>CAP has a different boundary. CAP services can be exposed through more than one protocol, including OData V4 and a REST protocol adapter. The same business service can therefore have different protocol endpoints while the domain logic remains in the CAP service implementation. This is a useful reminder that protocol choice and business behavior are related but separate design decisions.</p>

    <h2>API Management governs exposure; it does not own the business transaction</h2>
    <p>SAP Integration Suite API Management can place an API proxy in front of an existing backend service and apply policies for concerns such as authentication, authorization, traffic control, threat protection, monitoring, and selected transformations. It can also work with OpenAPI definitions.</p>

    <p>The proxy is still not the system of record for the business operation. If a consumer creates an order through a managed endpoint, the backend application decides whether that order is valid, how it is saved, and which business side effects occur. Keeping business logic out of a growing policy layer makes ownership and incident analysis much clearer.</p>

    <h2>A small example shows where the real design work is</h2>
    <p>Suppose a BTP extension exposes a plain REST endpoint for a partner to request a return. The API can define a resource-oriented contract, validate authentication at the managed edge, and pass the request to application logic that checks the business rules. If the partner retries after a timeout, the API needs an explicit rule for duplicate detection or idempotent processing. HTTP alone cannot decide whether two return requests represent one business action or two.</p>

    <p>Now compare that with an SAP S/4HANA OData service. The transport is still HTTP, but the client also relies on OData metadata, entity semantics, protocol rules, and the operations released by that particular service. Treating both interfaces as “just REST” hides information that matters to implementation and support.</p>

    <h2>Diagnose the request path, not only the status code</h2>
    <p>An HTTP response narrows the problem but rarely identifies the full cause. A <code>401</code> or <code>403</code> can come from the exposure layer or the backend authorization path. A <code>5xx</code> can originate in the application, a proxy policy, an integration component, or a downstream dependency. A timeout does not tell us whether the request reached the business application or whether the business transaction committed.</p>

    <p>For support, the useful evidence is the complete path: consumer request, gateway or proxy trace, correlation identifier, backend log, and resulting business object. This is especially important before retrying a write operation.</p>

    <h2>Evolve the contract deliberately</h2>
    <p>Breaking changes are not limited to changing a URL. Making a property mandatory, changing the meaning of a field, narrowing an authorization scope, changing error semantics, or altering retry behavior can break a consumer even when the endpoint path stays the same. Versioning is one tool, but compatibility discipline is the larger requirement.</p>

    <p>A good REST API is therefore less about fashionable endpoint shapes and more about predictable semantics. Consumers should know what they can request, what success means, what can be retried safely, and which system remains authoritative for the business state.</p>

    <h2>Source references</h2>
    <ul>
      <li>IETF — <a href="https://www.rfc-editor.org/rfc/rfc9110.html">RFC 9110: HTTP Semantics</a>.</li>
      <li>OpenAPI Initiative — <a href="https://spec.openapis.org/oas/latest.html">OpenAPI Specification</a>.</li>
      <li>SAP CAP — <a href="https://cap.cloud.sap/docs/guides/protocols/">Service Protocols in CAP</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-rap/service-binding">RAP Service Binding</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/1b17d18006d2472e81aa2f7af066a1b2.html">Classic API Management</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/openapi-specification-3-0">OpenAPI Specification 3.0 in SAP Integration Suite</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Protocol support, API Management policies, CAP adapters, authentication options, and released SAP APIs change by product and release. Verify the concrete API contract and runtime path for the target landscape before implementation.</p>
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
