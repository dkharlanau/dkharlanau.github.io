---
layout: default
title: "API Integration Working Skill"
description: "Choose protocols, define contracts, and design resilient synchronous integrations for REST, OData, SOAP, and SAP services."
permalink: /skill-hub/integration-architecture/api-integration-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">API Integration</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>API Integration Working Skill</h1>
  <p class="lead">Choose the right protocol, define the contract, handle auth and versioning, and design error behavior so the integration works under real load and real failure conditions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you decide which protocol to use for a given integration need, define the API contract with version and error semantics, design authentication and rate-limiting, and document the integration so it can be operated without guessing.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new system needs to exchange data with SAP or another enterprise system.</li>
      <li>You are replacing a legacy point-to-point integration with a standardized API.</li>
      <li>An existing API is breaking consumers due to unannounced schema changes.</li>
      <li>You need to choose between REST, OData, SOAP, or IDoc for a specific flow.</li>
      <li>Authentication credentials are expiring and the rotation process is undefined.</li>
      <li>Consumers report timeouts or rate-limit errors under production load.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: New CRM needs customer data from SAP S/4</h3>
    <p>The CRM team requests "an API" for customer master. The integration team must decide whether to expose OData from S/4, build a middleware REST API, or use an existing IDoc. The wrong choice creates coupling, performance issues, or data lag.</p>
    <h3>Situation 2: Legacy SOAP service failing under load</h3>
    <p>A SOAP service built five years ago is timing out during month-end. The team wants to modernize but does not know whether to migrate to REST, OData, or an event-driven pattern. The decision affects consumer rework, middleware config, and monitoring.</p>
    <h3>Situation 3: API contract mismatch causing order creation failures</h3>
    <p>A downstream system sends orders via REST API. After a middleware update, the JSON schema changes slightly. Orders fail with 400 errors. There is no versioning strategy, so both sides blame each other.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Integration requirement: data entities, direction, frequency, volume.</li>
      <li>Existing interface inventory (to avoid duplication).</li>
      <li>System landscape: SAP version, middleware, consumer platforms.</li>
      <li>Authentication mechanisms available (basic, OAuth, certificate, SAP principal).</li>
      <li>SLA requirements: availability, latency, throughput.</li>
      <li>Non-functional requirements: security, compliance, payload limits.</li>
      <li>Consumer capabilities: what protocols and auth they support.</li>
      <li>Failure history of similar integrations (optional but valuable).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the data volume per call and per day?</li>
      <li>Does the consumer need the data in real time, near real time, or batch?</li>
      <li>Who owns the API contract, and who approves changes to it?</li>
      <li>What happens to the business process when the API is unavailable for 1 minute? 1 hour?</li>
      <li>How should the consumer behave on timeout, 500 error, 400 error, 429 error?</li>
      <li>What is the maximum acceptable payload size?</li>
      <li>How are breaking changes communicated to consumers?</li>
      <li>Is the consumer internal or external, trusted or untrusted?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Map the need to a pattern.</strong> Document the business process, data entities, direction, frequency, and consumer count. Classify as read, write, or bidirectional.</li>
      <li><strong>Choose the protocol.</strong> Compare REST, OData, SOAP, IDoc, and file based on consumer needs, SAP capabilities, and team skills. Record the decision in an ADR.</li>
      <li><strong>Define the contract.</strong> Specify endpoint, methods, request/response schema, error schema, content type, and charset. Include example payloads.</li>
      <li><strong>Design authentication.</strong> Choose mechanism, define credential lifecycle (creation, rotation, revocation), and document how consumers obtain access.</li>
      <li><strong>Define SLA and limits.</strong> State availability target, max latency, rate limit, and payload size limit. Document what happens when limits are exceeded.</li>
      <li><strong>Design error handling.</strong> Define error codes, retryability, and consumer behavior per status code. Link to the Integration Error Handling skill.</li>
      <li><strong>Plan versioning.</strong> Choose URL versioning, header versioning, or content negotiation. Define deprecation policy and communication lead time.</li>
      <li><strong>Document operational details.</strong> Write runbook entries for: how to check health, how to diagnose failure, how to rotate credentials, who to page.</li>
      <li><strong>Validate with consumer test.</strong> Run a structured test with the consumer using realistic data and failure injection. Fix contract gaps before go-live.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the consumer is a user-facing application needing real-time data, use REST or OData.</li>
      <li>If the integration is bulk transactional with SAP as the source or target, evaluate IDoc or OData batch before REST.</li>
      <li>If the external system is a SaaS platform with complex query needs, use OData.</li>
      <li>If authentication uses tokens, define a rotation process with a grace period; never hardcode credentials.</li>
      <li>If the payload exceeds 1 MB, use an asynchronous pattern or chunked transfer; do not force synchronous.</li>
      <li>If there are more than 5 consumers for the same data, prefer a middleware layer or event bus over direct API calls.</li>
      <li>If the consumer is external or untrusted, enforce schema validation and rate limiting at the entry point.</li>
      <li>If backward compatibility cannot be maintained, increment the version and support the old version for at least 90 days.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>API Contract Document</strong> — Endpoint, schema, examples, error codes, version.</li>
      <li><strong>Architecture Decision Record</strong> — Why this protocol was chosen. Link to <a href="/skill-hub/artifact-templates/">ADR template</a>.</li>
      <li><strong>Interface Ownership Matrix entry</strong> — Owners, SLA, status. Link to <a href="/skill-hub/artifact-templates/">Interface Ownership Matrix template</a>.</li>
      <li><strong>Operational Runbook excerpt</strong> — Health check, failure diagnosis, credential rotation.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>API Contract Brief</h3>
    <pre><code>---
artifact: API Contract Brief
id: API-001
status: draft | reviewed | approved
---

## Interface
<!-- Source system → Target system, direction -->

## Endpoint
<!-- URL, method, content-type -->

## Request schema
<!-- JSON schema or field list with types and constraints -->

## Response schema
<!-- Success and error response structures -->

## Example payload
<!-- Realistic example with comments -->

## Error codes
| Code | Condition | Retryable | Consumer action |
|------|-----------|-----------|-----------------|
| 400  | Schema validation failed | No | Fix payload |
| 401  | Authentication expired | Yes | Refresh token and retry |
| 429  | Rate limit exceeded | Yes | Backoff and retry |
| 500  | Internal server error | Yes | Retry with backoff |
| 503  | Service unavailable | Yes | Retry with backoff |

## Version
<!-- Current version and deprecation policy -->

## Rate limit
<!-- Requests per second/minute per consumer -->

## Payload limit
<!-- Maximum size in MB -->

## Auth mechanism
<!-- OAuth 2.0 / Basic / Certificate / SAP Principal -->

## Owner
<!-- Business owner + technical owner -->

## SLA
<!-- Availability %, max latency p99 -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Contract has a version number and a deprecation policy.</li>
      <li>Every error code states whether the consumer should retry.</li>
      <li>Authentication mechanism is documented with rotation steps.</li>
      <li>Rate limits and payload size limits are specified.</li>
      <li>Backward compatibility rule is stated explicitly.</li>
      <li>At least one realistic example payload is included.</li>
      <li>Operational owner is named.</li>
      <li>Health check endpoint is defined.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Skipping error code design. <strong>Consequence:</strong> Consumers guess whether to retry, causing duplicate data or thundering herds.</li>
      <li><strong>Mistake:</strong> Hardcoding endpoint URLs or credentials in consumer code. <strong>Consequence:</strong> Every environment change or credential rotation requires a code deployment.</li>
      <li><strong>Mistake:</strong> No versioning strategy. <strong>Consequence:</strong> Schema changes break all consumers simultaneously.</li>
      <li><strong>Mistake:</strong> Ignoring payload size limits until production. <strong>Consequence:</strong> Timeouts and memory issues under real data volumes.</li>
      <li><strong>Mistake:</strong> Designing the API for a single consumer without considering future consumers. <strong>Consequence:</strong> The API becomes a point-to-point integration with a misleading name.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Gather context first:</strong> Collect integration requirements, existing interface inventory, system landscape, and NFRs before proposing a protocol.</li>
      <li><strong>Separate facts from assumptions:</strong> Do not assume the consumer supports OAuth, JSON, or webhooks. Verify their capabilities explicitly.</li>
      <li><strong>Produce artifacts:</strong> Generate an API Contract Brief and an Architecture Decision Record. Do not stop at a recommendation.</li>
      <li><strong>Avoid generic language:</strong> Do not write "REST is modern and flexible." Write "Use OData if the consumer needs filtered queries over SAP entities."</li>
      <li><strong>Handle missing information:</strong> If SLA or auth requirements are missing, list them as open questions and block the design until answered.</li>
      <li><strong>Link to Atlas diagnostics:</strong> If the integration involves SAP, reference <a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">outbound processing</a> and <a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">inbound processing</a> diagnostics for failure patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> — When synchronous APIs are not the right pattern.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Assign owners before finalizing the contract.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Design retry and failure behavior.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Monitor the API after go-live.</li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a> — Record the protocol choice.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — Conceptual foundation for contract design.</li>
      <li><a href="/atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/">REST vs OData vs SOAP vs IDoc vs Events</a> — Protocol comparison.</li>
      <li><a href="/atlas/concepts/synchronous-vs-asynchronous-integration/">Synchronous vs Asynchronous Integration</a> — When to avoid APIs.</li>
      <li><a href="/atlas/concepts/integration-pattern-decision-matrix/">Integration Pattern Decision Matrix</a> — Structured protocol selection.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of API integration practice. It is not official SAP, OpenAPI, or vendor documentation. SAP-specific guidance is aligned with S/4HANA OData and common IDoc patterns but may need adaptation for custom landscapes or older releases. Always validate protocol choices against the specific SAP release and middleware in use.</p>
  </section>
</article>
