---
layout: default
title: "SAP API Management: Proxies, Products, Security and Cost"
description: "Learn SAP API Management with step-by-step proxy setup, API Products, consumer Applications, REST/OData/SOAP, security policies and pricing."
permalink: /labs/enterprise-context/integrations/api-management/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-03
last_reviewed: 2026-11-03
review_method: "Current SAP Help, SAP Developer tutorials and public SAP pricing reviewed; human and tenant validation pending"
content_model: technical_guide
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-cleancore
tags:
  - sap
  - integration-suite
  - api-management
  - sap-btp
  - odata
  - rest
  - soap
  - api-security
structured_data:
  type: TechArticle
  primary_topic: "sap-integration"
semantic_links:
  - type: part_of
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: related_topic
    title: "SAP Business Partner API"
    url: "/labs/enterprise-context/integrations/business-partner-api/"
  - type: related_topic
    title: "Integration Operations & Recovery"
    url: "/labs/enterprise-context/integration-operations/"
  - type: related_topic
    title: "SAP Development Architecture and Clean Core"
    url: "/labs/enterprise-context/development/"
source_links:
  - title: "SAP Integration Suite — API Management architecture"
    url: "https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/api-management"
  - title: "Important Concepts of API Management"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/important-concepts-of-api-management"
  - title: "SAP Integration Suite pricing"
    url: "https://www.sap.com/products/technology-platform/integration-suite/pricing.html"
  - title: "Set Up API Management from SAP Integration Suite"
    url: "https://developers.sap.com/tutorials/api-mgmt-isuite-initial-setup"
  - title: "Get Started with API Management — tutorials"
    url: "https://developers.sap.com/tutorials/group-get-started-with-api-management"
  - title: "APIs on SAP Business Accelerator Hub"
    url: "https://help.sap.com/docs/btp/best-practices/apis"
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">SAP Enterprise</a></li>
    <li><a href="/labs/enterprise-context/integrations/">Integrations</a></li>
    <li aria-current="page">API Management</li>
  </ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / BTP / Integration Architecture</p>
      <h1>SAP API Management: from a backend service to a controlled API</h1>
      <p>An S/4HANA service already has a URL. Why put another service in front of it? Because making an API available and managing who may use it, at what rate, under which contract, are different responsibilities.</p>
      <a class="research-canvas__button" href="#mental-model">Follow an API call <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="The four things to remember">
      <p>Four objects to remember</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Provider</strong><small>Backend connection</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Proxy</strong><small>Managed endpoint</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Product</strong><small>Publish a bundle</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Application</strong><small>Registered consumer</small></div>
      <em>Current SAP cloud documentation reviewed: 3 November 2026. Product availability and contract terms must be checked per tenant.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">security</span>
    <p><strong>One-sentence answer:</strong> API Management puts a governed entry point in front of APIs so consumers get a stable contract and the provider controls access, traffic, visibility and change.</p>
    <p><strong>Important boundary:</strong> an API proxy does not create a missing S/4HANA business function, replace ERP authorization, or guarantee that the business transaction succeeded.</p>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">01 / See the system</p>
      <h2>Two flows: what the administrator configures, and what the consumer calls.</h2>
      <p>The Product and Application are part of onboarding and access management. They are not additional runtime hops for every HTTP request.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Design time · API team</h3><p>Choose a real backend service → configure an <strong>API Provider</strong> → create an <strong>API Proxy</strong> → attach security/traffic policies → deploy → group proxies into an <strong>API Product</strong> → publish to <strong>Developer Hub</strong>.</p></div>
      <div><h3>Onboarding · Consumer team</h3><p>Find the Product in Developer Hub → read its contract → create an <strong>Application</strong> → add or subscribe to the Product → obtain the applicable application credentials and access approval.</p></div>
      <div><h3>Runtime · One request</h3><p>Consumer software → <strong>API proxy URL</strong> → identity and traffic policies → backend S/4HANA service or Cloud Integration iFlow → response through the proxy → API analytics.</p></div>
    </div>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="Which part of the API Management architecture is used at runtime">
      <table class="study-table__table">
        <thead><tr><th scope="col">Question</th><th scope="col">Answer</th></tr></thead>
        <tbody>
          <tr><th scope="row">Which URL does the partner call?</th><td>The deployed API proxy endpoint, not the Product page and not the public SAP catalog.</td></tr>
          <tr><th scope="row">Where is the business logic?</th><td>Usually in S/4HANA or a service/iFlow behind the proxy. API-centric integration runtimes can also embed supported integration processing in API artifacts.</td></tr>
          <tr><th scope="row">Where is the right to change the sales order checked?</th><td>At the service/backend authorization boundary, in addition to gateway identity and access controls.</td></tr>
          <tr><th scope="row">What proves that the order changed?</th><td>The backend response and an appropriate follow-up business-state check, not merely an HTTP call recorded by API Management.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="why-use-it" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">02 / Business value</p>
      <h2>When a managed entry point pays for itself.</h2>
      <p><strong>Problem:</strong> exposing S/4HANA services directly to several distributors couples consumers to backend endpoints and makes access, traffic limits and changes harder to govern consistently. A managed API layer can reduce these dependencies.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Control access</h3><p>Apply consumer-facing policies, credential validation and approved access rules before requests reach ERP. Still enforce object and business authorization in the backend.</p></div>
      <div><h3>Protect capacity</h3><p>Use quota and spike controls to reduce unexpected traffic. A limit can prevent overload; it can also reject legitimate peak demand, so choose numbers from measurements.</p></div>
      <div><h3>Hide landscape changes</h3><p>Expose a stable managed path while changing internal hostnames or selected backends. A proxy cannot hide incompatible business-contract changes automatically.</p></div>
      <div><h3>Onboard partners</h3><p>Publish documented API Products for teams and partners. Applications make consumption and credentials traceable by consumer.</p></div>
      <div><h3>Observe usage</h3><p>Measure traffic, failures, response times and consumer usage. Combine gateway evidence with backend and business-process monitoring.</p></div>
      <div><h3>Govern changes</h3><p>Version and retire interfaces deliberately. Require ownership, testing and notice before a breaking change reaches a consuming application.</p></div>
    </div>
    <p class="ecg-caption"><strong>Counterpoint:</strong> for one internal, low-risk interface with adequate existing authentication, monitoring and connectivity, direct consumption of a released SAP API may be simpler and cheaper. Do not add a gateway solely because the landscape contains APIs.</p>
  </section>

  <section class="research-canvas__inventory" id="terminology" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">03 / Vocabulary</p>
      <h2>Provider, proxy, product and application are not synonyms.</h2>
      <p>Use this table in design workshops. Each term belongs to a different responsibility, even when the SAP screens show them together.</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="API Management terms and examples">
      <table class="study-table__table">
        <thead><tr><th scope="col">Term</th><th scope="col">What it really means</th><th scope="col">Example / common mistake</th></tr></thead>
        <tbody>
          <tr><th scope="row">Backend service / API</th><td>The real functionality: read an order, update a record, or start a business operation.</td><td>A released S/4HANA Sales Order API. A catalog entry does not mean it is active in your tenant.</td></tr>
          <tr><th scope="row">API Provider</th><td>Reusable connection definition for a target system, including supported host, authentication or connectivity settings.</td><td>“S4-ERP-QA”. It describes how to reach a backend; it is not the external partner.</td></tr>
          <tr><th scope="row">API Proxy</th><td>The managed API-facing endpoint with routing, security, traffic and optional transformation policies.</td><td>“PartnerOrderRead-v1”. Calls go to its managed URL.</td></tr>
          <tr><th scope="row">API policy</th><td>A runtime rule attached to an API flow, such as API-key verification, OAuth/JWT validation, quota or spike protection.</td><td>Publishing a Product does not, by itself, enforce an API key. Configure and test the policy.</td></tr>
          <tr><th scope="row">API Product</th><td>A logical, publishable bundle of one or more APIs, with documentation and access/subscription context.</td><td>“Partner Order Visibility” contains order and delivery read APIs. Not an SAP material/product master.</td></tr>
          <tr><th scope="row">Developer</th><td>A person or team with access to discover and consume published APIs.</td><td>A partner developer may register an Application to use an approved Product.</td></tr>
          <tr><th scope="row">Application</th><td>A registered API consumer, associated with Products and credentials in the relevant consumption model.</td><td>“Distributor Portal — Production” is a consumer registration. It is not the frontend source code itself.</td></tr>
          <tr><th scope="row">App key / secret</th><td>Credentials linked to an Application; their use depends on the selected policies and authentication scheme.</td><td>A valid key identifies the registered consumer but is not proof of ERP business authorization.</td></tr>
          <tr><th scope="row">API subscription</th><td>An approved relationship allowing an Application or developer to consume selected Product APIs, subject to configuration.</td><td>Production and test consumers should not silently share credentials.</td></tr>
          <tr><th scope="row">API Portal / design UI</th><td>Provider/admin workspace where APIs, proxies, Products, policies and analytics are managed.</td><td>Typically reached through Integration Suite’s API Management experience; older guides use “API Portal”.</td></tr>
          <tr><th scope="row">Developer Hub</th><td>Customer-facing internal/partner API catalog for discovery, documentation, testing and subscriptions.</td><td>Previously called API Business Hub Enterprise; not the global public SAP catalog.</td></tr>
          <tr><th scope="row">API analytics</th><td>Traffic and consumer-level observations from the managed API layer.</td><td>HTTP 200 does not prove delivery posted, invoice created, or business processing completed.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="hubs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">04 / Three different portals</p>
      <h2>API Business Hub, Business Accelerator Hub, API Portal and Enterprise Hub: which one?</h2>
      <p>The naming changed over time. A public SAP discovery catalog and your company's API catalog have different owners and purposes.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>SAP Business Accelerator Hub</h3><p><strong>Public SAP catalog.</strong> Formerly <em>SAP API Business Hub</em>. Browse SAP and selected partner APIs, specifications and sample/mock testing where offered. It does not deploy, activate or grant access to a customer's S/4HANA tenant.</p><p><a href="https://api.sap.com/" target="_blank" rel="noopener">Browse api.sap.com</a></p></div>
      <div><h3>API Portal / API design and management</h3><p><strong>Your API provider/admin workspace.</strong> Create an API Provider, build and deploy API proxies, attach policies, create API Products and analyze traffic. UI labels depend on the SAP Integration Suite experience and release.</p><p><a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/working-with-api-management" target="_blank" rel="noopener">SAP management concepts</a></p></div>
      <div><h3>Developer Hub</h3><p><strong>Your organization's consumer catalog.</strong> The earlier name <em>API Business Hub Enterprise (ABHE)</em> refers to this type of enterprise developer portal. Developers discover published APIs, subscribe and manage Applications.</p><p><a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/api-management" target="_blank" rel="noopener">SAP Developer Hub architecture</a></p></div>
    </div>
    <p class="ecg-caption"><strong>Memory rule:</strong> <em>Accelerator Hub = discover what SAP offers.</em> <em>API Portal = manage what your organization exposes.</em> <em>Developer Hub = let approved consumers find and use those APIs.</em></p>
  </section>

  <section class="research-canvas__inventory" id="protocols" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">05 / Protocol choices</p>
      <h2>REST vs OData vs SOAP: compare the contract, not the acronym.</h2>
      <p>All three can be exposed as managed APIs in supported SAP API Management scenarios. None should be selected merely because it sounds more modern.</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="REST OData and SOAP comparison">
      <table class="study-table__table">
        <thead><tr><th scope="col">Aspect</th><th scope="col">REST-style HTTP API</th><th scope="col">OData</th><th scope="col">SOAP</th></tr></thead>
        <tbody>
          <tr><th scope="row">Nature</th><td>Architectural style, commonly JSON over HTTP.</td><td>Standardized REST-based protocol with an entity/data model.</td><td>XML-based messaging protocol with an explicit service contract.</td></tr>
          <tr><th scope="row">Contract</th><td>Often OpenAPI, plus provider-specific semantics.</td><td>Service metadata, entity sets, navigation and query rules.</td><td>Typically WSDL and XSD; may include WS-* standards.</td></tr>
          <tr><th scope="row">Typical operations</th><td>GET, POST, PATCH, PUT, DELETE as supported by the API.</td><td>HTTP operations plus model-aware queries such as <code>$filter</code>, <code>$select</code> and <code>$expand</code> when supported.</td><td>Named service operations with an XML SOAP envelope.</td></tr>
          <tr><th scope="row">SAP example</th><td>Custom/released REST service, depending on product.</td><td>Many released S/4HANA business-object APIs; OData V2 and V4 depend on the API.</td><td>Existing enterprise service or asynchronous master-data replication contract.</td></tr>
          <tr><th scope="row">Useful when</th><td>Simple consumer-facing resources and commands with a clear contract.</td><td>Structured SAP business entities, relationships and standardized query access.</td><td>A WSDL service already exists or contractual/enterprise messaging requires it.</td></tr>
          <tr><th scope="row">Main risk</th><td>Loose conventions or inconsistent semantics between endpoints.</td><td>Expensive queries, deep expansions, authorization complexity and version-specific behavior.</td><td>Heavier schemas, tooling and operational complexity.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">info</span>
      <p><strong>OData is not the opposite of REST.</strong> OData is a specific REST-based protocol. SOAP is a different messaging protocol. A proxy can expose an existing service without changing that service's protocol. Any protocol conversion or payload reshaping must be explicitly designed and tested.</p>
    </div>
    <p><strong>Illustrative OData V2 read, not a ready-to-use tenant URL:</strong></p>
    <pre><code>GET /sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner?$top=5
Accept: application/json

# Confirm the released service, target edition, authorization and
# communication setup before trying this against a real system.</code></pre>
    <p>For state-changing OData V2 requests, also check the service's CSRF-token and ETag/concurrency behavior. An API proxy must not accidentally strip required headers, query parameters or batch boundaries.</p>
    <p><a href="/labs/enterprise-context/integrations/business-partner-api/">See the Business Partner API's entity hierarchy and write/recovery considerations</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="setup" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">06 / Hands-on setup</p>
      <h2>A practical first implementation: publish an existing read-only SAP service.</h2>
      <p>This is a reproducible design sequence, not a claim that every tenant uses identical menu labels. Start with a permitted non-production environment and a real released API for its SAP product and edition.</p>
    </header>
    <div class="research-route-list">
      <a href="https://developers.sap.com/tutorials/api-mgmt-isuite-initial-setup" target="_blank" rel="noopener"><span>01</span><strong>Check entitlement and activate the capability</strong><small>Provision SAP Integration Suite and the required roles in a BTP subaccount. In Integration Suite, add the <b>Manage APIs</b> capability; enable Developer Hub if the scenario needs a consumer portal. Verify the actual subscribed plan first.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://api.sap.com/" target="_blank" rel="noopener"><span>02</span><strong>Select a real backend API and its contract</strong><small>Find a suitable SAP API in Business Accelerator Hub. Verify Public Cloud vs Private Cloud/on-premise edition, API version, available operations, communication scenario, roles, business permissions and activation requirements.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.sap.com/tutorials/hcp-apim-create-provider" target="_blank" rel="noopener"><span>03</span><strong>Configure an API Provider or supported target connection</strong><small>Define the backend target, correct HTTPS/trust and authentication, and required connectivity. For private/on-premise hosts, evaluate SAP Cloud Connector/private connectivity as supported. Test the target without exposing credentials.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.sap.com/tutorials/hcp-apim-create-api" target="_blank" rel="noopener"><span>04</span><strong>Create an API Proxy</strong><small>Use the API Provider or suitable target URL to create a managed external base path, configure routing, inspect the imported service contract and deploy. Start with a harmless GET before adding writes.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.sap.com/tutorials/hcp-apim-verify-api" target="_blank" rel="noopener"><span>05</span><strong>Add and test policies</strong><small>Apply the appropriate client authentication/verification policy, then quota, spike protection and safe logging as needed. Test anonymous, expired, unauthorized and over-limit calls. An API key alone is rarely sufficient for sensitive business writes.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.sap.com/tutorials/hcp-apim-create-product" target="_blank" rel="noopener"><span>06</span><strong>Create and publish an API Product</strong><small>Group the proxy with a meaningful business name, description, owner and version. Publish it for the right audience in Developer Hub. A Product groups access; it is not an executable intermediary.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/important-concepts-of-api-management" target="_blank" rel="noopener"><span>07</span><strong>Register a consumer Application</strong><small>In the applicable Developer Hub flow, create an Application, associate/subscribe to the Product and obtain the permitted credentials. Store secrets outside browser code and source control. Confirm the access and approval model.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#verification" ><span>08</span><strong>Prove the outcome and prepare operations</strong><small>Call the proxy with a controlled test client. Confirm routing, response, analytics, backend authorization, trace ID, quota behavior, failure handling and the real ERP read result. Repeat in QA before production promotion.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
    <p><strong>Illustrative managed call:</strong> host, path and credential header depend on the deployed proxy and its policy. In a directory outside source control, prepare <code>test-api-headers.txt</code> with the configured header name (often <code>APIKey</code>) and a short-lived QA credential; restrict file permissions. Never commit or log the file.</p>
    <pre><code>curl --request GET \
  'https://api.example.invalid/partner-orders/v1/orders/demo-100' \
  --header @./test-api-headers.txt \
  --header 'Accept: application/json'

# Run from the directory containing the private header file.
# The .invalid host is synthetic; use an authorized QA proxy URL.
# For OAuth security, use the required Authorization header instead.</code></pre>
    <p class="ecg-caption"><strong>Connection distinction:</strong> an <em>API Provider</em> is the API Management target-system abstraction. A <em>BTP Destination</em> is a different reusable connection concept, typically used by applications and integrations. Do not assume creating one automatically configures the other. Choose the supported connectivity mechanism for the selected runtime and backend.</p>
  </section>

  <section class="research-canvas__inventory" id="security" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">07 / Security and traffic</p>
      <h2>What a policy can protect—and what it cannot.</h2>
      <p>Place access checks early in the request flow so denied traffic does not unnecessarily reach ERP. Select the exact policy types and order for the runtime in use.</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="Common API security and traffic policies">
      <table class="study-table__table">
        <thead><tr><th scope="col">Control</th><th scope="col">Why use it?</th><th scope="col">What still needs design?</th></tr></thead>
        <tbody>
          <tr><th scope="row">Verify API Key</th><td>Identify an approved consuming Application where the policy is configured.</td><td>Key storage, rotation, revocation and finer-grained user/business authorization.</td></tr>
          <tr><th scope="row">OAuth 2.0 / JWT validation</th><td>Validate supported token-based caller identity/claims.</td><td>Trust, token audience, scopes, user propagation and backend authorization.</td></tr>
          <tr><th scope="row">Quota</th><td>Limit requests over a configured period.</td><td>Expected volume, fair allocation across consumers and response on limit exhaustion.</td></tr>
          <tr><th scope="row">Spike Arrest</th><td>Reduce short traffic bursts reaching the backend.</td><td>Real peak patterns: a limit can reject legitimate concurrent work.</td></tr>
          <tr><th scope="row">Threat protection / validation</th><td>Reject selected malformed or suspicious payloads.</td><td>Payload limits, protocol compatibility, schema changes and false positives.</td></tr>
          <tr><th scope="row">Logging / analytics</th><td>See calls, latency, consumer and technical error patterns.</td><td>PII/secrets redaction, retention, tracing, alert owner and backend correlation.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="ecg-caption"><strong>Security principle:</strong> do not publish a broad S/4HANA API and rely only on client keys. Review the least-privilege backend role and whether a partner can see other partners' orders. A gateway policy cannot correct an overly broad ERP authorization model.</p>
  </section>

  <section class="research-canvas__inventory" id="architecture-choices" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">08 / Choose the right architecture</p>
      <h2>API Management is not Cloud Integration—and neither replaces the ERP.</h2>
      <p>Keep the component that owns business processing separate from the component that owns API exposure and consumption.</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="Architecture option comparison">
      <table class="study-table__table">
        <thead><tr><th scope="col">Scenario</th><th scope="col">Useful first design</th><th scope="col">Main trade-off</th></tr></thead>
        <tbody>
          <tr><th scope="row">One trusted internal app reads stock</th><td>Consume the released S/4HANA API directly if existing security/connectivity/governance are sufficient.</td><td>Simple and low overhead, but consumer coupling remains.</td></tr>
          <tr><th scope="row">Several partners use the same API</th><td>Place a managed API Proxy in front of the released ERP service; publish a Product and manage Applications.</td><td>Better shared control, additional cost and an extra runtime dependency.</td></tr>
          <tr><th scope="row">Consumer and ERP structures differ</th><td>Use Cloud Integration/iFlow for mapping/orchestration; API Management for exposure and policy.</td><td>Two responsibilities to operate. Some supported newer API-centric runtimes can combine these.</td></tr>
          <tr><th scope="row">Master data distributed asynchronously</th><td>Select an asynchronous/event/DRF pattern as business semantics require, not an HTTP proxy by default.</td><td>Requires reconciliation, retry, sequencing and owner of eventual completion.</td></tr>
          <tr><th scope="row">Partner must submit business-critical writes</th><td>Govern API access, limit write operations and preserve backend business authorization, idempotency and audit.</td><td>Timeouts create unknown outcomes. API Management does not make a write exactly-once.</td></tr>
          <tr><th scope="row">AI agent invokes ERP functions</th><td>Expose a narrow approved set of APIs/tools with caller identity, policy, confirmation for risky actions and audit.</td><td>Tool discovery is not action authorization. Validate the supported MCP gateway capability separately.</td></tr>
        </tbody>
      </table>
    </div>
    <p>Current SAP Integration Suite API Management documentation distinguishes <strong>Classic API Management</strong> (managed proxy runtime), <strong>Integration Cell</strong> (managed API-centric integration runtime), and <strong>Edge Integration Cell</strong> (customer-managed runtime for supported private/on-premise scenarios). Support, availability and allowed policies differ. Do not treat a classic-proxy tutorial as proof that every runtime behaves the same.</p>
    <p><a href="/labs/enterprise-context/integrations/">Compare APIs with IDocs, events, queues and files in the Integration Architecture map</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="costs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">09 / Commercial reality</p>
      <h2>How much does SAP API Management cost?</h2>
      <p>SAP publishes indicative US-dollar monthly prices for Integration Suite editions. These are platform offer prices, <strong>not</strong> an isolated price per API Proxy or per API Product. As of 3 November 2026, the public SAP pricing page shows:</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="SAP Integration Suite public monthly pricing snapshot on 3 November 2026">
      <table class="study-table__table">
        <thead><tr><th scope="col">Integration Suite edition</th><th scope="col">Published USD/month</th><th scope="col">API Management?</th><th scope="col">Commercial reading</th></tr></thead>
        <tbody>
          <tr><th scope="row">Starter</th><td><strong>$1,728</strong></td><td>Not included in the public edition comparison.</td><td>Good for limited integration flow use cases, not a substitute for full API lifecycle management.</td></tr>
          <tr><th scope="row">Standard</th><td><strong>$5,339</strong></td><td>Included in the published comparison.</td><td>Starting reference for API lifecycle management and related integration capabilities.</td></tr>
          <tr><th scope="row">Enhanced</th><td><strong>$7,688</strong></td><td>Included.</td><td>More capabilities and different included allowances; justify each extra capability.</td></tr>
        </tbody>
      </table>
    </div>
    <p><a href="https://www.sap.com/products/technology-platform/integration-suite/pricing.html" target="_blank" rel="noopener">Check the current official SAP Integration Suite pricing and edition matrix</a>. Displayed prices may change by region, buying model, tax treatment, commitments, contract and negotiated discounts. A separate standalone API Management offering or existing enterprise entitlement may change the comparison; request a quote for the actual commercial structure.</p>
    <div class="ecg-decision-columns">
      <div><h3>Platform entitlement</h3><p>Which SAP BTP commercial agreement and service plan exist already? Does it include full API Management, Developer Hub and the selected runtime?</p></div>
      <div><h3>Metering and capacity</h3><p>Check included messages, metering definition, API request volumes, data sizes, throughput and extra usage charges. Do not assume “API request” always equals one billable message.</p></div>
      <div><h3>Hidden project cost</h3><p>Budget for onboarding, Cloud Connector/connectivity, certificates, identity integration, key rotation, testing, transports, monitoring and incident ownership.</p></div>
      <div><h3>Business value</h3><p>Estimate avoided duplicate partner integrations, reduced exposure risk, faster onboarding, better operational evidence and change isolation. Compare this with direct integration and alternative gateways.</p></div>
    </div>
    <p class="ecg-caption"><strong>Architecture decision:</strong> the business case is strongest when several consumers share a managed interface portfolio. Do not multiply the public monthly price by “number of APIs”; SAP's published edition prices are not per-proxy list prices. Validate actual overage and service use rights before committing to a budget.</p>
  </section>

  <section class="research-canvas__inventory" id="verification" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">10 / Prove it works</p>
      <h2>How to test a managed API without confusing gateway success with business success.</h2>
      <p>Before production, record the exact consumer, key/token type, API Product, Proxy revision, target system, backend business user and a safe request ID.</p>
    </header>
    <div class="research-route-list">
      <a href="#security"><span>401</span><strong>Authentication fails</strong><small>Check the header/token, API policy placement, signature/audience/expiry, API key association and credentials. Distinguish gateway denial from backend 401.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#security"><span>403</span><strong>Caller is known but not allowed</strong><small>Check Product/Application access, scopes and backend business authorization. A gateway success does not prove permission to view a particular customer's order.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="#setup"><span>404</span><strong>Wrong managed path or backend route</strong><small>Compare deployed Proxy base path, target endpoint, API version and service activation. Use the actual published URL, not the SAP catalog URL.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#security"><span>429</span><strong>Traffic policy rejected requests</strong><small>Check quota versus spike controls, application usage and expected peaks. Increasing the limit without checking ERP capacity may move the outage downstream.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>5xx</span><strong>Gateway, network or backend failure</strong><small>Correlate gateway logs with connectivity, target response, iFlow traces where used, and ERP application logs. For writes, never retry blindly after a timeout.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="/labs/enterprise-context/integrations/business-partner-api/"><span>200</span><strong>Technically successful—but is the business result correct?</strong><small>For reads, verify the expected object and authorization. For writes, verify the updated business state, business errors and duplicate controls.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
    <p class="ecg-caption"><strong>Release checklist:</strong> approved API contract, valid consumer permissions, least-privilege ERP authorization, masked logs, measured traffic, error ownership, correlation, QA evidence, version/rollback plan and documented cutover. Run negative tests as well as one happy-path call.</p>
  </section>

  <section class="research-canvas__inventory" id="interview" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">11 / Explain and challenge</p>
      <h2>The SAP Lead answer in 30 seconds.</h2>
      <p>“SAP API Management is the governance and protection layer for APIs. We can expose an existing S/4HANA or Cloud Integration service through an API Proxy, apply security and traffic policies, publish it in an API Product and let registered consumer Applications access it through Developer Hub. I would use it when several consumers need a stable, monitored contract. I would still keep business authorization and transaction logic in the owning backend, and I would verify licensing and traffic before recommending it.”</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Architecture follow-up</h3><p>Three partners need Sales Order data, but one may only see its own customers. Which part should enforce consumer identity, and which part should enforce business-data authorization?</p></div>
      <div><h3>Cost follow-up</h3><p>Would you add SAP API Management for one internal reporting application? What existing controls and costs would you inspect before deciding?</p></div>
      <div><h3>Reliability follow-up</h3><p>A partner's API call timed out after creating an order in S/4HANA. What evidence would you collect before allowing a retry?</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">References / scope</p>
      <h2>Primary references and what they establish.</h2>
      <p>The sources below support SAP's named capabilities, object terminology, tutorials and list prices. Architecture patterns, cautions and synthetic examples are independent learning guidance, not an implementation test or a vendor certification.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/api-management" target="_blank" rel="noopener"><span>SAP</span><strong>API Management architecture and runtime options</strong><small>Classic runtime, Integration Cell, Edge Integration Cell, Developer Hub and security/governance capabilities.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/important-concepts-of-api-management" target="_blank" rel="noopener"><span>SAP</span><strong>Important Concepts of API Management</strong><small>Provider, API, Product, Developer, Application and application key.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/btp/best-practices/apis" target="_blank" rel="noopener"><span>SAP</span><strong>API offerings on SAP BTP</strong><small>The public Business Accelerator Hub is a discovery source; API Management manages customer-facing interfaces.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.sap.com/tutorials/group-get-started-with-api-management" target="_blank" rel="noopener"><span>LAB</span><strong>SAP Developer API Management tutorial sequence</strong><small>Set up, API Provider, Proxy, Product and API key verification.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://www.sap.com/products/technology-platform/integration-suite/pricing.html" target="_blank" rel="noopener"><span>USD</span><strong>SAP Integration Suite public pricing</strong><small>Published Starter, Standard and Enhanced monthly prices. Commercial snapshot: 3 November 2026; confirm live pricing.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/security-aspects-of-data-data-flow-for-api-management" target="_blank" rel="noopener"><span>SEC</span><strong>API Management security and traffic policies</strong><small>Authentication, access policies, threat protection, quota and spike controls.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
