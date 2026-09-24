---
layout: default
title: "Event-Driven Architecture"
description: "Event-driven architecture coordinates systems through asynchronous facts about business changes, while keeping event semantics, delivery guarantees, and consumer behavior explicit."
tags:
  - concept
  - sap-mm
  - sap-wm
  - sap-s4hana
  - sap-integration
  - ai-operations
  - automation
permalink: /atlas/concepts/event-driven-architecture/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
last_reviewed: 2026-09-24
last_modified_at: 2026-09-24
related:
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/event-catalog/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---

# Event-Driven Architecture

> **Status**: Under review.  
> **Scope**: Event-driven patterns, contracts, and operational concerns for enterprise landscapes.

Event-driven architecture (EDA) lets a producer publish a fact about a change without waiting for every interested consumer to complete its reaction. A sales order can change in the source system, an event can announce that change, and several consumers can react independently.

EDA does **not** replace synchronous APIs. Most enterprise landscapes need both. A synchronous request is useful when the caller needs an immediate answer before it can continue. An event is useful when something has already happened and other systems may react afterward.

## An event is a fact, not a remote procedure call

It helps to separate three message intentions:

- a **query** asks for information;
- a **command** asks another component to perform an action;
- an **event** states that something happened.

The distinction changes the coupling between systems. If an order application calls five downstream systems before it can commit an order, its runtime depends on all five. If it commits the order and then publishes an event, downstream consumers can process the change on their own timelines.

That freedom has a cost: the producer and consumers are no longer guaranteed to hold the same state at the same moment.

## Follow the event through the whole path

A useful event flow is more than producer → broker → consumer:

**Business change → event creation → publication → broker or messaging service → subscription or queue → consumer processing → downstream business state**

Each boundary can succeed while a later one fails. A producer can publish successfully while a consumer is offline. A broker can deliver a message while the consumer rejects the payload. The consumer can finish technically while its business update is rejected by the target system.

This is why “the event was sent” is weak evidence. For an important flow, we need to know what state was committed at each boundary.

## One flow contains several contracts

An event-driven design usually depends on three different contracts.

The **business contract** explains what the event means. It identifies the event type, business object, identifiers, important payload fields, and any versioning rules. A name such as `OrderChanged` is not enough if consumers cannot tell which change it represents or what they may safely infer from it.

The **delivery contract** belongs to the messaging technology and configuration. It covers routing, acknowledgements, retries, ordering, retention, replay, and failure handling. These properties are not universal features of “EDA”; they depend on the broker, protocol, service plan, topology, and consumer design.

The **processing contract** belongs to the consumer. It defines what the consumer does, how it handles repeated or delayed messages, how it correlates the event with business data, and how it proves the final result.

Keeping these contracts separate prevents a common design error: treating a reliable broker as proof that the business process is reliable.

## Decide how much state belongs in the event

Not every event needs the full business object. Two common shapes are useful:

**Event notification.** The event carries enough information to identify what changed. The consumer retrieves current state from an API or another authoritative source when it needs more detail. This keeps the event small and leaves the source of truth in one place, but it adds a follow-up dependency.

**Event-carried state.** The event includes the state that consumers need for their reaction. This can reduce follow-up reads and preserve the state as it was when the event was emitted, but the contract becomes larger and harder to evolve.

Neither shape is automatically better. The right choice depends on what the consumer must know, whether historical state matters, payload sensitivity, volume, and the cost of another read.

Event sourcing is a separate architectural decision. In event sourcing, the event log itself represents the authoritative history from which state can be rebuilt. A system can use ordinary business events without using event sourcing at all.

## Asynchrony changes consistency and recovery

Once processing is asynchronous, temporary inconsistency is normal. The source may have committed a change while a consumer is still waiting, retrying, or offline. Architecture must therefore answer two questions that synchronous designs can often hide: **how stale may the consumer be, and how will we recover when it falls behind?**

Duplicate delivery, delayed delivery, and ordering also need explicit treatment when the chosen transport can produce them. A consumer should be able to recognize whether repeating work is safe, whether it needs an idempotency key or state comparison, and what to do with a message that cannot be processed automatically.

A dead-letter queue can isolate failed messages in systems that provide one, but it is not a recovery strategy by itself. Someone or something still needs to classify the failure, correct the cause, and decide whether replay is safe.

## When EDA is a good fit

EDA is useful when several independent consumers need to react to the same business occurrence, when the producer should not know all of those consumers, or when the reaction can happen after the source transaction commits. It is also useful when absorbing short differences in processing speed is better than holding the producer open.

A synchronous call is usually clearer when the source needs an immediate decision before it can continue—for example, a blocking validation or calculation that belongs inside the transaction. Batch integration may also be the simpler choice when timeliness is not important and a scheduled transfer already meets the business requirement.

The choice is therefore not “modern events versus old APIs.” It is a question of timing, ownership, failure isolation, and consistency.

## A SAP example: notification first, state second

SAP business events illustrate the distinction well. SAP S/4HANA can publish events that notify consumers that a business object changed. The event contract can contain identifiers and selected data rather than a complete copy of the object. The consumer may then use an API to retrieve the current state that it needs.

For example, SAP documents supplier-invoice events whose payload identifies the supplier invoice and fiscal year. A consumer that needs invoice items, amounts, or approval context must obtain that information from an appropriate business interface rather than assuming the event contains the full invoice.

This pattern can be effective because the event answers **when should I react?** while the API answers **what is the current authoritative state?** The two interfaces solve different problems.

## Standards help at different layers

[CloudEvents](https://cloudevents.io/) standardizes common event metadata such as an event identifier, source, type, and specification version. It does not define the business meaning of an order or invoice event.

[AsyncAPI](https://www.asyncapi.com/docs/concepts/asyncapi-document) can describe asynchronous interfaces, including channels, operations, and messages. The document becomes part of the communication contract between senders and receivers, but it does not replace business ownership or runtime monitoring.

[OpenTelemetry messaging semantic conventions](https://opentelemetry.io/docs/specs/semconv/messaging/) provide a common vocabulary for messaging telemetry. Those messaging conventions are still marked as development, so implementations should verify the conventions and instrumentation version they actually use.

## Related Atlas pages

- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Event Contracts](/atlas/concepts/event-contracts/)
- [Idempotency](/atlas/concepts/idempotency/)
- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/)
- [Business Events](/atlas/sap/business-events/)
- [Event-Driven Architecture Map](/atlas/maps/event-driven-architecture-map/)

## Source references

- CloudEvents — [Specification and project documentation](https://cloudevents.io/)
- AsyncAPI Initiative — [AsyncAPI document concepts](https://www.asyncapi.com/docs/concepts/asyncapi-document)
- OpenTelemetry — [Semantic conventions for messaging systems](https://opentelemetry.io/docs/specs/semconv/messaging/)
- SAP Help Portal — [Business Events on SAP Business Accelerator Hub](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/8cbf952e55364254be2da77aa1342aa5.html)
- SAP Help Portal — [Supplier Invoice Events](https://help.sap.com/docs/SAP_S4HANA_CLOUD/bb9f1469daf04bd894ab2167f8132a1a/3f383669990a4957b0b58eae7d8b67b4.html)

## Verification limitations

Delivery guarantees, ordering, replay, retention, payload size, and operational controls depend on the selected broker and configuration. Product-specific behavior should be verified for the target landscape rather than inferred from the general EDA pattern.
