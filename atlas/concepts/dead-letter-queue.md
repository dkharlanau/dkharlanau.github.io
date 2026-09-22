---
layout: default
title: "Dead Letter Queue"
description: "A dead-letter or dead-message queue isolates messages that cannot be processed normally so they can be investigated without blocking healthy traffic."
tags:
  - concept
  - sap-sd
  - ai-operations
  - integration
  - data-architecture
permalink: /atlas/concepts/dead-letter-queue/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
last_reviewed: 2026-09-23
related:
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/business-events/
---

# Dead Letter Queue

> **Status**: Under review.  
> **Scope**: Dead-letter and dead-message queue patterns for SAP messaging integrations.

A dead-letter queue is a holding area for messages that the normal consumer path cannot process safely. The exact name and trigger vary by broker. SAP Event Mesh documentation uses the term **dead message queue**; other platforms commonly use **dead-letter queue (DLQ)**.

The important idea is not the label. A failed message should stop cycling through the normal path when further automatic redelivery is unlikely to help, while healthy messages continue to move.

## Retry and dead-letter handling solve different problems

A retry is appropriate when failure may be temporary: a receiver is unavailable, a network call times out, or a dependent service is overloaded. A dead-message queue is for the point where the broker or integration design decides that normal redelivery should stop.

That boundary must be explicit. If every error is retried forever, one bad message can waste capacity or repeatedly block ordered processing. If messages are moved aside too quickly, temporary outages become manual incidents.

There is no useful universal rule such as “retry three times.” The right policy depends on business urgency, expected outage duration, message ordering, idempotency, and the broker's own delivery semantics.

## SAP Event Mesh

In SAP Event Mesh, a queue can be configured with a **Max Redelivery Count** and a **Dead Message Queue**. When a message reaches the configured redelivery limit, Event Mesh can move the undelivered message to that dead message queue instead of purging it. A message can also move there when it reaches the queue's maximum time-to-live, if a dead message queue is configured.

This is a broker-level mechanism. It does not repair the message and it does not tell us why processing failed. Operations still need the original message, delivery information, correlation identifiers where available, and the consumer-side error that caused the rejection or missing acknowledgement.

A practical support sequence is therefore:

1. identify whether the failure is transient or deterministic;
2. inspect the consumer error and message content without changing production data;
3. fix the consumer, configuration, authorization, or payload problem;
4. confirm that replay is safe, especially if the consumer may already have produced a side effect;
5. redeliver or recreate the message using the mechanism supported by the broker and application.

The idempotency check in step four is critical. A message can look “failed” from the broker's point of view even when a downstream system completed part of the work before the acknowledgement was lost.

## Cloud Integration JMS is a different case

SAP Cloud Integration also has a setting named **Dead-Letter Queue** in the JMS sender adapter, but it should not be treated as a general-purpose business-error DLQ. Current SAP documentation states that this option is used to take a message out of processing when repeated processing causes worker-node crashes; related adapter documentation describes scenarios such as repeated out-of-memory failures. SAP explicitly notes that this mechanism does not handle normal integration errors in the same way.

For ordinary temporary processing failures, the JMS retry pattern keeps the message in queue storage and retries it according to the configured interval, exponential backoff, and maximum retry interval. This is why we need to distinguish the Event Mesh dead-message-queue pattern from Cloud Integration's special JMS dead-letter setting even though the names sound similar.

## What good operations look like

A DLQ is useful only if somebody owns it. We want monitoring for message count and age, enough retained context to diagnose the failure, and a documented decision for replay versus discard. The queue should not become a second backlog that everyone assumes another team is watching.

For a production integration, ownership normally sits with the team responsible for the consuming process, while the messaging platform team maintains broker configuration and observability. The producer still owns payload correctness and contract changes. These boundaries are more useful than a generic “integration team owns everything” model.

A growing DLQ is a symptom, not a KPI to optimize in isolation. We check what changed before the growth started: a deployment, schema change, authorization change, receiver outage, or new payload pattern. The goal is to remove the cause, then recover messages safely.

## Related Atlas pages

- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Idempotency](/atlas/concepts/idempotency/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [Integration Monitoring and Reliability Map](/atlas/maps/integration-monitoring-reliability-map/)

## Source references

- SAP Help Portal — [Create a Queue in SAP Event Mesh](https://help.sap.com/docs/integration-suite/sap-integration-suite/create-queue)
- SAP Help Portal — [Queues and Queue Subscriptions](https://help.sap.com/docs/integration-suite/sap-integration-suite/queues-and-queue-subscriptions)
- SAP Help Portal — [Apply the Retry Pattern with JMS Queue](https://help.sap.com/docs/integration-suite/sap-integration-suite/apply-retry-pattern-with-jms-queue)
- SAP Help Portal — [Configure the XI Receiver Adapter](https://help.sap.com/docs/SAP_INTEGRATION_SUITE/51ab953548be4459bfe8539ecaeee98d/configure-xi-receiver-adapter)

## Verification limitations

Dead-letter behavior depends on the broker, adapter, retry configuration, acknowledgement model, and product edition. This page deliberately avoids assuming that SAP Event Mesh, Advanced Event Mesh, Cloud Integration JMS, and third-party brokers implement one identical DLQ mechanism.
