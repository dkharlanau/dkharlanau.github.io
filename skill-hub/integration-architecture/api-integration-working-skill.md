---
layout: default
title: "API Integration Working Skill"
description: "Choose protocols, define contracts, and design resilient synchronous integrations for REST, OData, SOAP, and SAP services."
permalink: /skill-hub/integration-architecture/api-integration-working-skill/
last_modified_at: 2026-09-26
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
    <p>This skill helps you decide which protocol to use for a given integration need, <mark class="key-idea">define the API contract with version and error semantics</mark>, design authentication and rate-limiting, and document the integration so it can be operated without guessing.</p>
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
      <li><a href="/skill-hub/integration-architecture/integration-sla-working-skill/">SLA and SLO requirements</a>: availability, latency, throughput, and freshness where the API serves replicated or cached data.</li>
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
      <li><strong>Choose the protocol.</strong> Compare REST, OData, SOAP, IDoc, and file based on consumer needs, SAP capabilities, and team skills. <mark class="key-idea">Record the decision in an ADR.</mark></li>
      <li><strong>Define the contract.</strong> Specify endpoint, methods, request/response schema, error schema, content type, and charset. Include example payloads.</li>
      <li><strong>Design authentication.</strong> Choose mechanism, define credential lifecycle (creation, rotation, revocation), and document how consumers obtain access.</li>
      <li><strong>Define SLA and limits.</strong> Use <a href="/skill-hub/integration-architecture/integration-sla-working-skill/">Integration SLA and SLO Design</a> to state the availability target, latency percentile, sustainable throughput, measurement window, and freshness objective where relevant. Then define rate and payload limits.</li>
      <li><strong>Design error handling.</strong> Define error codes, retryability, and consumer behavior per status code. Link to the Integration Error Handling skill.</li>
      <li><strong>Plan versioning.</strong> Choose URL versioning, header versioning, or content negotiation. Define deprecation policy and communication lead time.</li>
      <li><strong>Document operational details.</strong> Write runbook entries for: how to check health, how to diagnose failure, how to rotate credentials, who to page.</li>
      <li><strong>Validate with consumer test.</strong> Run a structured test with the consumer using realistic data and failure injection. Fix contract gaps before go-live.</li>
    </ol>
  </section>

  <section>
    <p class="eyebrow">Decision model</p>
    <h2>Choose the interaction first. Choose the protocol second.</h2>
    <p>A Lead-level integration decision does not start with REST, OData, IDoc, or Event Mesh. Start with the business interaction and the failure model. The same business object can need different patterns for different interactions: a UI may query an order synchronously, a warehouse may receive an order asynchronously, and analytics may consume an event or batch extract.</p>
    <p><mark class="key-idea">The protocol is an implementation consequence of the interaction semantics, NFRs, platform constraints, and recovery model.</mark></p>

    <h3>Decision tree</h3>
    <ol>
      <li>
        <strong>What is the interaction?</strong>
        <ul>
          <li><strong>Query:</strong> the consumer asks for current data and needs a response now → evaluate REST or OData.</li>
          <li><strong>Command:</strong> the consumer asks the target to perform a business action → evaluate a synchronous API only if the caller truly needs the outcome immediately; otherwise evaluate an asynchronous command/message pattern.</li>
          <li><strong>Business fact:</strong> something already happened and independent consumers need to know → evaluate events.</li>
          <li><strong>Bulk transfer or scheduled synchronization:</strong> large sets move on a cadence and immediate response is not required → evaluate IDoc, batch API, file, CDC, or another asynchronous bulk mechanism.</li>
        </ul>
      </li>
      <li>
        <strong>Does the caller need the business result before it can continue?</strong>
        <ul>
          <li><strong>Yes:</strong> synchronous API is a candidate. Define timeout, latency percentile, availability dependency, and what the caller does when the response is unknown.</li>
          <li><strong>No:</strong> prefer decoupling. Evaluate event, queue, IDoc, or batch rather than holding two systems in one availability chain.</li>
        </ul>
      </li>
      <li>
        <strong>What consistency and freshness are actually required?</strong>
        <ul>
          <li>Current authoritative state on demand → API/query pattern.</li>
          <li>State change must be propagated quickly but temporary lag is acceptable → event/message pattern.</li>
          <li>Periodic convergence is sufficient → batch/file/replication can be simpler and cheaper.</li>
        </ul>
      </li>
      <li>
        <strong>What are the load and payload characteristics?</strong>
        <ul>
          <li>Small, bounded request/response payloads with predictable concurrency → synchronous API fits well.</li>
          <li>Large payloads, bursts, long-running processing, or expensive SAP transactions → asynchronous processing, batching, pagination, or job-based APIs deserve priority.</li>
          <li>Do not use a universal payload-size threshold. Measure serialization cost, network time, backend processing time, concurrency, memory, and gateway limits in the actual landscape.</li>
        </ul>
      </li>
      <li>
        <strong>What delivery behavior matters?</strong>
        <ul>
          <li>If duplicates can cause business damage, define an idempotency key or business deduplication rule.</li>
          <li>If ordering matters, define the ordering scope: global, per customer, per order, per material, or another business key. Global ordering is rarely necessary and reduces scalability.</li>
          <li>If a timeout leaves the result unknown, provide a status lookup, correlation ID, reconciliation process, or safe retry rule.</li>
        </ul>
      </li>
      <li>
        <strong>How many consumers exist, and who controls them?</strong>
        <ul>
          <li>One known consumer with a request/response need → direct API can be reasonable.</li>
          <li>Several independent consumers reacting to the same fact → publish/subscribe becomes stronger because the producer should not orchestrate every consumer.</li>
          <li>External partners or SaaS consumers → contract stability, throttling, authentication, network boundary, audit, and partner-supported standards may dominate the choice.</li>
        </ul>
      </li>
      <li>
        <strong>What does SAP and the surrounding platform support cleanly?</strong>
        <ul>
          <li>Prefer a released standard SAP API, event, IDoc, or supported integration capability over a custom extraction from internal tables.</li>
          <li>Check the exact S/4HANA release, deployment model, API availability, business object coverage, extensibility, middleware, and partner constraints.</li>
          <li>If the standard contract does not cover the business need, document the gap before designing a custom interface.</li>
        </ul>
      </li>
      <li>
        <strong>Can operations recover it at 03:00?</strong>
        <ul>
          <li>Define monitoring, correlation, retry ownership, replay, dead-letter handling where relevant, reconciliation, and business proof of completion.</li>
          <li>If the design cannot explain how an operator detects and safely recovers a failed transaction, the integration decision is not finished.</li>
        </ul>
      </li>
    </ol>

    <h3>Pattern comparison</h3>
    <table>
      <thead>
        <tr>
          <th>Pattern</th>
          <th>Strong fit</th>
          <th>Watch for</th>
          <th>Typical SAP context</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>REST API</strong></td>
          <td>Simple resource or command interactions, broad consumer compatibility, synchronous request/response.</td>
          <td>Tight runtime dependency, chatty calls, unclear retry semantics, custom pagination/filtering conventions.</td>
          <td>Released SAP APIs, middleware façades, side-by-side applications.</td>
        </tr>
        <tr>
          <td><strong>OData</strong></td>
          <td>Entity-oriented access where filtering, projection, navigation, metadata, and standard query semantics are valuable.</td>
          <td>Consumers coupling to a broad data model, expensive queries, unrestricted navigation, using query flexibility where a bounded business API would be clearer.</td>
          <td>S/4HANA and Fiori-oriented services, SAP business object access where a released OData service exists.</td>
        </tr>
        <tr>
          <td><strong>SOAP</strong></td>
          <td>Existing enterprise contracts, WSDL-based tooling, partner ecosystems, or SAP services where SOAP is the supported contract.</td>
          <td>Replacing it only for fashion, complex WS-* dependencies, large synchronous payloads, consumer migration cost.</td>
          <td>Established SAP enterprise services and legacy/partner integrations.</td>
        </tr>
        <tr>
          <td><strong>IDoc</strong></td>
          <td>Asynchronous SAP-centric business document exchange, established ALE/EDI flows, durable transactional distribution.</td>
          <td>Assuming technical status equals business completion, partner-profile complexity, reprocessing ownership, semantic mapping outside SAP.</td>
          <td>Orders, deliveries, invoices, master data, B2B/EDI and legacy SAP integration landscapes.</td>
        </tr>
        <tr>
          <td><strong>Event</strong></td>
          <td>A business fact should reach independent consumers without the producer controlling their process.</td>
          <td>Using events as hidden commands, missing idempotency, ordering assumptions, schema evolution, replay and reconciliation.</td>
          <td>Business-event distribution, decoupled extensions, SAP Event Mesh or other broker-based landscapes.</td>
        </tr>
        <tr>
          <td><strong>File / batch</strong></td>
          <td>Large periodic transfers, partner constraints, simple bulk exchange, non-urgent synchronization.</td>
          <td>Weak validation, partial files, duplicate delivery, poor lineage, manual recovery, unclear cut-off times.</td>
          <td>Legacy interfaces, bank/partner exchange, migration, large extracts and scheduled reconciliation.</td>
        </tr>
      </tbody>
    </table>

    <h3>Hard gates before selecting a synchronous API</h3>
    <ul>
      <li><strong>Availability gate:</strong> Can the business process tolerate the caller becoming dependent on the target's runtime availability?</li>
      <li><strong>Latency gate:</strong> Is the end-to-end latency target realistic at peak load, including SAP processing and middleware hops?</li>
      <li><strong>Timeout gate:</strong> Is the business outcome known after a timeout, or can the caller safely determine whether the action happened?</li>
      <li><strong>Throughput gate:</strong> Can the target sustain peak and burst load without turning the API into a remote batch processor?</li>
      <li><strong>Recovery gate:</strong> Is there a controlled way to retry, reconcile, and prove the final business state?</li>
    </ul>
    <p>For measurable availability, latency, throughput, recovery, and other quality attributes, use the <a href="/skill-hub/architecture/non-functional-requirements-working-skill/">Non-Functional Requirements</a> skill rather than vague labels such as “real time” or “high performance”.</p>

    <h3>Decision rules</h3>
    <ul>
      <li>If the user or calling process must receive current data before continuing, evaluate REST or OData first, then verify latency and availability dependencies.</li>
      <li>If the producer is announcing a completed business fact to independent consumers, evaluate an event before adding more point-to-point API calls.</li>
      <li>If the target can process work later, do not create synchronous coupling merely because an HTTP endpoint is easy to expose.</li>
      <li>If data transfer is high-volume or long-running, evaluate batching, asynchronous jobs, IDoc, file, CDC, or event streaming rather than one large synchronous request.</li>
      <li>If the consumer needs flexible entity queries and the SAP service safely supports them, OData can be a strong fit; if the interaction is a bounded business command, a narrower API contract may be clearer.</li>
      <li>If a standard SAP contract already exists and meets the need, prefer it over a custom protocol wrapper unless a documented constraint justifies the extra layer.</li>
      <li>If an external partner mandates a contract such as SOAP, EDI/IDoc, or file exchange, treat that as a real architecture constraint and design security, validation, monitoring, and recovery around it.</li>
      <li>If duplicates are possible, make idempotency explicit. If ordering is required, define the business key and scope of ordering rather than saying only “messages must be ordered”.</li>
      <li>If backward compatibility cannot be maintained, version the contract and define a migration/deprecation window based on consumer criticality and release cadence; do not apply one universal number.</li>
      <li>If the interface cannot be monitored, correlated, replayed or safely reconciled where needed, it is not production-ready regardless of protocol.</li>
    </ul>

    <h3>When to change the default</h3>
    <p>Change the initial pattern when one constraint dominates the rest: strict ordering, very large payloads, a legal acknowledgement requirement, an external B2B standard, an existing platform mandate, offline operation, a receiving application with only one supported contract, or a recovery model that the preferred technology cannot satisfy. Record the reason in an <a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a>.</p>

    <h3>Three examples</h3>
    <table>
      <thead>
        <tr>
          <th>Situation</th>
          <th>Reasoning</th>
          <th>Likely direction</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>CRM user opens a customer and needs current credit-relevant information immediately.</td>
          <td>The UI cannot continue without current state; payload is bounded; a response is required.</td>
          <td>Released synchronous API/OData service, with timeout and fallback behavior defined.</td>
        </tr>
        <tr>
          <td>An order is confirmed in S/4 and warehouse, notification, analytics, and another service must react independently.</td>
          <td>The business fact already happened; consumers should not extend the order-save transaction or depend on each other.</td>
          <td>Business event / publish-subscribe, with idempotency, ordering scope, replay, and schema ownership.</td>
        </tr>
        <tr>
          <td>Millions of master-data records must be synchronized overnight to a legacy partner.</td>
          <td>Immediate response is unnecessary; throughput, restartability, reconciliation, and partner capability dominate.</td>
          <td>Bulk asynchronous pattern such as file, IDoc, replication, or batch API depending on supported contracts.</td>
        </tr>
      </tbody>
    </table>

    <p><strong>Lead answer frame:</strong> “I would not choose the protocol first. I would classify the interaction as query, command, event, or bulk transfer; confirm whether an immediate business result is required; quantify freshness, latency, volume, ordering, and availability; check standard SAP capabilities and partner constraints; then choose the simplest pattern whose failure and recovery model we can operate.”</p>
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
<!-- Availability target, p95/p99 latency, sustainable throughput, freshness if applicable, measurement window -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Contract has a version number and a deprecation policy.</li>
      <li><mark class="key-idea">Every error code states whether the consumer should retry.</mark></li>
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
      <li><strong>Handle missing information:</strong> If <a href="/skill-hub/integration-architecture/integration-sla-working-skill/">SLA/SLO</a> or auth requirements are missing, list them as open questions and block the design until answered.</li>
      <li><strong>Link to Atlas diagnostics:</strong> If the integration involves SAP, reference <a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">outbound processing</a> and <a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">inbound processing</a> diagnostics for failure patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/integration-sla-working-skill/">SLA &amp; SLO Design</a> — Define measurable availability, latency, throughput, and freshness targets before finalizing the API contract.</li>
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
