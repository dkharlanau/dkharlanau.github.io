---
layout: default
title: "Event-Driven Architecture Working Skill"
description: "Decide whether an event should exist, who owns it, what its contract is, and how failures are monitored and handled."
permalink: /skill-hub/integration-architecture/event-driven-architecture-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">Event-Driven Architecture</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Event-Driven Architecture Working Skill</h1>
  <p class="lead">Turn business facts into well-owned, well-contracted events that decouple systems without creating invisible dependencies or silent failures.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you identify which business facts should become events, confirm the authoritative source, define the event contract and schema, choose delivery semantics, design failure handling, and maintain an event catalog that consumers can trust.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You need to decouple a source system from multiple downstream consumers.</li>
      <li>A polling integration is causing performance issues on the source system.</li>
      <li>You are implementing the output of an event storming workshop.</li>
      <li>A new downstream system needs to react to state changes in SAP or another platform.</li>
      <li>Consumers are receiving duplicate or out-of-order events.</li>
      <li>An event was added without schema governance and is now breaking consumers.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: Order status changes trigger four downstream systems</h3>
    <p>When an order is confirmed in SAP S/4, the warehouse system, billing system, customer notification service, and analytics platform all need to react. Point-to-point API calls create tight coupling and retry complexity. Events are proposed but no one owns the event definition.</p>
    <h3>Situation 2: Polling integration causing SAP performance issues</h3>
    <p>A logistics platform polls SAP every five minutes for delivery status updates. During peak periods, the polling volume impacts SAP application server performance. The team wants to replace polling with events but does not know how to guarantee delivery or handle failures.</p>
    <h3>Situation 3: Duplicate events during retries</h3>
    <p>A consumer receives order confirmation events multiple times because the producer retries on timeout. The consumer processes each duplicate as a new order, creating duplicate shipments. There is no idempotency key or deduplication logic.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Business process map showing state changes and triggers.</li>
      <li>List of current and potential consumers with their data needs.</li>
      <li>Existing event catalog (if any).</li>
      <li>SLA requirements: delivery latency, ordering, durability.</li>
      <li>Retry and error handling policies from the organization.</li>
      <li>Middleware or broker capabilities (topics, partitions, retention, schema registry).</li>
      <li>SAP event enablement status (SAP Event Mesh, CDC, custom outbound).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business fact occurred, and who is the authoritative source?</li>
      <li>How many consumers need to know about this fact today? How many in two years?</li>
      <li>What happens if the event is lost? What happens if it is duplicated?</li>
      <li>Does the consumer need strict ordering, or can events be processed out of order?</li>
      <li>What is the maximum acceptable delay between the business fact and consumer receipt?</li>
      <li>How will schema changes be communicated and versioned?</li>
      <li>What is the retention policy for this event, and who decides it?</li>
      <li>How will a consumer prove it is compatible before subscribing?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the business event.</strong> Name it after the business fact, not the technical trigger. Example: <code>OrderConfirmed</code>, not <code>SAPTableUpdated</code>.</li>
      <li><strong>Confirm the authoritative source.</strong> Only one system publishes this event. Document why it is authoritative.</li>
      <li><strong>Define the event contract.</strong> Specify event name, schema, version, payload example, and metadata fields (timestamp, correlation ID, source).</li>
      <li><strong>List consumers and their needs.</strong> For each consumer, document what fields they use, their latency requirement, and their ordering requirement.</li>
      <li><strong>Choose broker and topic strategy.</strong> Decide topic naming, partitioning key (if ordering matters), and retention. Record in an ADR.</li>
      <li><strong>Define delivery semantics.</strong> Choose at-least-once, at-most-once, or exactly-once. Document the trade-off and implementation.</li>
      <li><strong>Design failure handling.</strong> Define retry policy, dead letter criteria, and escalation path. Link to Integration Error Handling skill.</li>
      <li><strong>Add to event catalog.</strong> Register the event, schema, owner, consumers, and SLA in the central event catalog.</li>
      <li><strong>Validate with consumer test.</strong> Have a consumer subscribe using the contract. Inject failures and verify retry, ordering, and idempotency behavior.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If more than three consumers need the same business fact, use an event instead of API polling.</li>
      <li>If strict ordering matters, use a partition key and ordered delivery; otherwise, allow parallel processing.</li>
      <li>If exactly-once processing is required, implement idempotency in the consumer; do not rely on broker guarantees alone.</li>
      <li>If event loss is unacceptable, use a persistent queue with acknowledgment and retry.</li>
      <li>If the consumer is external or untrusted, enforce schema validation at the consumer edge.</li>
      <li>If no event catalog exists, create one before adding new events.</li>
      <li>If the event payload exceeds 100 KB, evaluate whether a reference plus lookup pattern is better than a fat event.</li>
      <li>If SAP is the source, verify whether SAP Event Mesh, CDC, or custom outbound is the right emission mechanism.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Event Contract</strong> — Name, schema, version, example, metadata. See template below.</li>
      <li><strong>Event Catalog Entry</strong> — Owner, consumers, SLA, broker, topic.</li>
      <li><strong>Consumer Compatibility Matrix</strong> — Which consumers use which fields and versions.</li>
      <li><strong>Architecture Decision Record</strong> — Broker choice, delivery semantics, partitioning. Link to <a href="/skill-hub/artifact-templates/">ADR template</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Event Contract Brief</h3>
    <pre><code>---
artifact: Event Contract Brief
id: EVT-001
status: draft | reviewed | approved
---

## Event name
<!-- Business-fact name: OrderConfirmed, DeliveryShipped -->

## Source system
<!-- Authoritative publisher -->

## Schema version
<!-- SemVer or integer -->

## Payload schema
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| orderId | string | yes | Unique order identifier | ORD-2026-0042 |
| confirmedAt | ISO-8601 | yes | Timestamp of confirmation | 2026-06-09T14:30:00Z |
| customerId | string | yes | Customer reference | C-8821 |
| totalAmount | decimal | no | Confirmed total | 1250.00 |

## Metadata
| Field | Description | Example |
|-------|-------------|---------|
| eventId | Unique event identifier for idempotency | evt-uuid |
| correlationId | Trace identifier across services | corr-uuid |
| source | System that emitted the event | sap-s4-prod |
| emittedAt | Event emission timestamp | 2026-06-09T14:30:01Z |

## Example payload
```json
{
  "orderId": "ORD-2026-0042",
  "confirmedAt": "2026-06-09T14:30:00Z",
  "customerId": "C-8821",
  "totalAmount": 1250.00
}
```

## Delivery semantics
<!-- at-least-once | at-most-once | exactly-once -->
<!-- Implementation: idempotency key, deduplication window -->

## Ordering requirement
<!-- Strict by orderId | None -->

## Consumer list
| Consumer | Fields used | Latency req | Ordering req | Contact |
|----------|-------------|-------------|--------------|---------|
| Warehouse | orderId, confirmedAt | < 30s | No | Team A |
| Billing | orderId, totalAmount | < 5 min | No | Team B |

## Topic / queue
<!-- Name, broker, retention -->

## Owner
<!-- Business owner + technical owner -->

## SLA
<!-- Max latency, durability guarantee -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Event has a unique business-fact name, not a technical trigger name.</li>
      <li>Schema is versioned and includes metadata (eventId, correlationId, source, emittedAt).</li>
      <li>Authoritative source system is identified and documented.</li>
      <li>Consumer list is complete with latency and ordering requirements.</li>
      <li>Delivery semantics are defined and implemented.</li>
      <li>Idempotency mechanism is documented.</li>
      <li>Failure path (retry, dead letter, escalation) is documented.</li>
      <li>Event is registered in the event catalog.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Events without schema governance. <strong>Consequence:</strong> Producers change fields silently, breaking consumers.</li>
      <li><strong>Mistake:</strong> Missing dead letter handling. <strong>Consequence:</strong> Failed events accumulate in queues, causing backpressure or data loss.</li>
      <li><strong>Mistake:</strong> Assuming ordered delivery without explicit configuration. <strong>Consequence:</strong> Consumers process events out of order and produce incorrect state.</li>
      <li><strong>Mistake:</strong> No consumer onboarding process. <strong>Consequence:</strong> New consumers subscribe to production topics without compatibility checks.</li>
      <li><strong>Mistake:</strong> Fat events with entire entity state. <strong>Consequence:</strong> Payload bloat, serialization cost, and leakage of fields consumers should not see.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Gather context first:</strong> Collect the business process map, consumer list, existing event catalog, and broker capabilities before designing events.</li>
      <li><strong>Name events by business fact:</strong> Do not use table names or technical triggers as event names.</li>
      <li><strong>Define contract before implementation:</strong> Produce an Event Contract Brief and get consumer sign-off before coding.</li>
      <li><strong>Ensure idempotency:</strong> Always include <code>eventId</code> and document the consumer deduplication strategy.</li>
      <li><strong>Avoid generic language:</strong> Do not write "events provide loose coupling." Write "Use an event when three consumers need the same OrderConfirmed fact."</li>
      <li><strong>Link to Atlas diagnostics:</strong> For SAP event emission, reference <a href="/atlas/concepts/sap-event-driven-architecture/">SAP Event-Driven Architecture</a> and <a href="/atlas/concepts/cdc-change-data-capture/">CDC</a> for mechanism selection.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — When events are not the right pattern.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Monitor event flows and consumer lag.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Design retry and dead letter behavior.</li>
      <li><a href="/skill-hub/integration-architecture/data-mesh-working-skill/">Data Mesh</a> — Events as output ports for domain data products.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> — Conceptual foundation.</li>
      <li><a href="/atlas/concepts/sap-event-driven-architecture/">SAP Event-Driven Architecture</a> — SAP-specific mechanisms.</li>
      <li><a href="/atlas/concepts/event-contracts/">Event Contracts</a> — Contract design principles.</li>
      <li><a href="/atlas/concepts/event-catalog/">Event Catalog</a> — Governance and discovery.</li>
      <li><a href="/atlas/concepts/idempotency/">Idempotency</a> — Exactly-once processing.</li>
      <li><a href="/atlas/concepts/dead-letter-queue/">Dead Letter Queue</a> — Failure handling.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of event-driven architecture practice. It is not official SAP, Confluent, or vendor documentation. SAP-specific guidance references SAP Event Mesh and CDC patterns available in recent S/4HANA releases but may not apply to all landscapes. Always verify broker capabilities and SAP release notes before committing to an event strategy.</p>
  </section>
</article>
