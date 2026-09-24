---
layout: default
title: "Event-Driven Architecture Map"
description: "A practical map of event-driven architecture in SAP landscapes, connecting business events, channels, brokers, subscriptions, consumers, reliability controls, and business outcomes."
tags:
  - landscape-map
  - sap-btp
  - sap-s4hana
  - sap-integration
  - data-quality
  - ai-operations
  - integration
permalink: /atlas/maps/event-driven-architecture-map/
nav_order: 11
parent: Maps
robots: noindex, follow
sitemap: false
verified: false
last_reviewed: 2026-09-24
last_modified_at: 2026-09-24
related:
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/event-catalog/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/business-events/
  - /atlas/sap/odata/
  - /atlas/sap/rest-apis/
  - /atlas/sap/api-gateways/
  - /atlas/sap/cloud-connector/
  - /atlas/sap/integration-monitoring/
---

# Event-Driven Architecture Map

> **Status**: Under review.  
> **Scope**: The event path from SAP business change to downstream business outcome.

This map is for one practical job: locating responsibility in an event-driven flow. Instead of treating “event integration” as one box, follow the event through the boundaries that can fail independently.

## The event path

**1. Business change**  
A source application changes business state: an order is created, an invoice is posted, a master-data object changes.

↓

**2. Event definition**  
The producer emits an event with a defined type, identity, and payload. The [event contract](/atlas/concepts/event-contracts/) explains what consumers may infer from it.

↓

**3. Publication channel**  
The event is allowed onto an outbound channel or equivalent publication path. In supported SAP S/4HANA and ABAP scenarios, Enterprise Event Enablement manages channels and topic bindings.

↓

**4. Broker and routing**  
An event broker accepts the message and routes it according to topics, queues, subscriptions, and access rules. [SAP Event Mesh](/atlas/sap/business-events/) is one SAP messaging option; SAP Integration Suite also provides event capabilities for broader EDA scenarios.

↓

**5. Consumer delivery**  
A consumer receives the message according to the delivery semantics of the selected broker and subscription. This is where retry, acknowledgement, duplicate delivery, ordering, retention, and dead-letter behavior become concrete configuration questions rather than generic EDA concepts.

↓

**6. Consumer processing**  
The application interprets the event. It may act directly on the payload or use an [OData](/atlas/sap/odata/) or [REST API](/atlas/sap/rest-apis/) to retrieve current authoritative state.

↓

**7. Business outcome**  
The consumer creates or changes something that matters: a workflow starts, a downstream object changes, a notification is recorded, or another business process advances. This final state is separate from successful message delivery.

## Read the map in both directions

For support, move forward from the last proven fact. If the source committed a change but no event exists, stay at the producer. If the event left the producer but no consumer has it, move to the broker. If the consumer received it but the business object is wrong, leave broker diagnostics and inspect application processing.

For change impact, move backward from the consumer. Ask which event contract it relies on, which topic or queue delivers that event, which producer owns the event, and which business change creates it. That path shows where a seemingly small producer change can affect downstream behavior.

## What each layer owns

| Layer | Owns | Does not prove |
|---|---|---|
| Business application | The committed business change and event trigger | That the event reached a broker |
| Event definition | Meaning, identifiers, payload, version | Delivery or consumer success |
| Publication channel | Which events can leave through the configured path | Broker routing or final business state |
| Broker | Routing, buffering, subscription/queue behavior available in that service | Correct consumer logic |
| Consumer | Interpretation, deduplication/state checks, follow-up calls | That its downstream update succeeded unless it verifies it |
| Target business system | Final validation and persisted business state | Why an upstream message was delayed or duplicated |

The table is deliberately strict. Most event incidents take longer when evidence from one row is used to make claims about another.

## Use the symptom to choose the next boundary

**The source object changed, but no event is visible.** Confirm that the event exists for that object and scenario, then inspect the source event mechanism. Do not start with broker queues when there is no evidence that publication began.

**The producer shows a published event, but the expected queue or subscription is empty.** Compare the actual event type and topic with broker routing and access rules. A valid event can still have no matching route.

**The queue grows while the source continues normally.** The producer and broker may be healthy. Focus on consumer availability, throughput, acknowledgement behavior, and downstream latency.

**The consumer reports success, but the business result is missing.** Reconcile the target object or transaction. Message consumption proves that application code received the event; it does not prove that downstream business validation accepted the requested change.

**The same business effect happens twice.** Establish whether the message was redelivered or whether two different events represented the same business state. Then inspect [idempotency](/atlas/concepts/idempotency/) at the consumer rather than assuming the broker must suppress every repeat.

**The consumer needs fields that the event does not contain.** Decide whether the event is a notification contract. If it is, retrieve current state from the authoritative interface instead of expanding every event by default.

## SAP product placement

In an SAP S/4HANA event flow, the business application owns the business change. Business Event Handling and Enterprise Event Enablement provide event and channel capabilities for supported scenarios. SAP Event Mesh or event capabilities in SAP Integration Suite can provide the messaging layer. Consumer applications may run on SAP BTP or elsewhere and may use SAP APIs for follow-up reads or business actions.

Cloud Integration can also participate when transformation or orchestration is required, but an event-driven design does not require every message to pass through an integration flow. Add that layer when it performs a real integration job, not merely to make the architecture diagram look complete.

## Contract and reliability links

- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/) — the coordination model and its consistency trade-offs.
- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/) — SAP-specific event publication and consumption path.
- [Event Contracts](/atlas/concepts/event-contracts/) — event meaning, payload, and compatibility.
- [Idempotency](/atlas/concepts/idempotency/) — safe repeated processing.
- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/) — recovery without uncontrolled duplication.
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/) — isolation of messages that cannot be processed automatically.
- [Integration Monitoring and Reliability Map](/atlas/maps/integration-monitoring-reliability-map/) — operational evidence across integration layers.

## Source references

- SAP Help Portal — [Business Events on SAP Business Accelerator Hub](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/8cbf952e55364254be2da77aa1342aa5.html)
- SAP Help Portal — [Maintain Outbound Event Topics](https://help.sap.com/docs/abap-cloud/abap-integration-connectivity/maintain-outbound-event-topics)
- SAP Help Portal — [What Is SAP Event Mesh?](https://help.sap.com/docs/event-mesh/event-mesh/set-up-sap-event-mesh-in-btp-cockpit)
- SAP Integration Architecture Guide — [Use SAP Integration Suite to Explore EDA in the Enterprise](https://help.sap.com/docs/sap-btp-guidance-framework/integration-architecture-guide/use-sap-integration-suite-to-explore-eda-in-enterprise)
- CloudEvents — [Specification and project documentation](https://cloudevents.io/)
- AsyncAPI Initiative — [AsyncAPI document concepts](https://www.asyncapi.com/docs/concepts/asyncapi-document)

## Verification limitations

This map describes responsibilities and investigation boundaries, not one mandatory SAP topology. Event availability, channel configuration, broker capabilities, delivery semantics, and API behavior vary by SAP product, release, service plan, and landscape design.
