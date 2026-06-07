---
layout: default
title: "Enterprise Integration Architecture Watchlist"
description: "Tracking SAP Integration Suite, event mesh, API management, cloud-to-on-premise connectivity, and integration standards."
type: watchlist
status: draft
date: 2026-06-07
updated: 2026-06-07
robots: noindex,follow
sitemap: false
evidence_level: high
topics:
  - sap-integration-suite
  - event-mesh
  - api-management
  - cloud-connector
source_count: 5
related_atlas:
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
  - /atlas/sap/business-events/
related_research:
  - /research/comparisons/sap-integration-suite-vs-eda/
  - /research/briefs/event-driven-integration-for-sap-landscapes/
next_actions:
  - Verify Event Mesh in Integration Suite (EMIS) vs standalone Event Mesh service roadmap
  - Track SAP's PI/PO migration tooling maturity
  - Monitor AsyncAPI and CloudEvents adoption in SAP partner ecosystem
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/research/">Research</a></li>
    <li aria-current="page">Enterprise Integration Architecture Watchlist</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Research Watchlist</p>
    <h1>Enterprise Integration Architecture Watchlist</h1>
    <p class="note-subtitle">SAP Integration Suite, event mesh, API management, and integration standards.</p>
  </header>

  <div class="note-body">

## Research question

What is the current state of SAP's integration platform, how do Event Mesh and API management fit into the landscape, and what migration paths exist from legacy middleware?

## Short answer

SAP Integration Suite is the cloud-native iPaaS on BTP, replacing or complementing on-premise PI/PO. It includes Cloud Integration (CPI), API Management, Integration Advisor, Event Mesh, and Open Connectors. Event Mesh is now available both as a standalone BTP service and as Event Mesh in Integration Suite (EMIS). S/4HANA can emit business events directly to Event Mesh via channel configuration. For AMS teams, the key shift is from batch-oriented, file-based integration to real-time, API- and event-driven patterns—requiring new monitoring, error handling, and security models.

## What changed

- **Event Mesh in Integration Suite (EMIS).** SAP consolidated Event Mesh as a capability within Integration Suite, enabling direct S/4HANA-to-EMIS connectivity without a standalone Event Mesh subscription. [SAP Community: SAP S/4HANA direct connectivity with Event Mesh in Integration Suite](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-s-4hana-direct-connectivity-with-event-mesh-in-integration-suite/ba-p/13752534)
- **S/4HANA direct event publishing.** S/4HANA 2023 FPS01 and later support direct channel configuration to Advanced Event Mesh (AEM) and EMIS, using SM59 destinations and OAuth 2.0 or certificate-based authentication. [SAP Community: SAP S/4HANA integration with SAP Integration Suite, Advanced Event Mesh](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-integration-with-sap-integration-suite-advanced-event-mesh/ba-p/13577271)
- **PI/PO migration path.** SAP provides a structured migration assessment tool and partner-supported migration methodology for moving from SAP Process Orchestration to Integration Suite. [SAP-Press: Complete Guide to SAP Integration Suite](https://blog.sap-press.com/complete-guide-to-sap-integration-suite)
- **API Management on Cloud Foundry.** SAP API Management is a standalone service within Integration Suite for publishing, promoting, and overseeing APIs in a secure, scalable environment. [GitHub: SAP-docs/btp-integration-suite](https://github.com/SAP-docs/btp-integration-suite)
- **CloudEvents and AsyncAPI momentum.** The event-driven architecture ecosystem is standardizing around CloudEvents (CNCF graduated project) for event envelopes and AsyncAPI (Linux Foundation) for event API contracts. Both are relevant to SAP's event mesh strategy. [The New Stack: CNCF CloudEvents](https://thenewstack.io/cncf-cloudevents-a-lil-message-envelope-that-travels-far/), [AsyncAPI Initiative](https://www.asyncapi.com/en)

## Evidence

| Signal | Source | Confidence |
|--------|--------|------------|
| Event Mesh in Integration Suite GA | SAP official community blog | High |
| S/4HANA direct connectivity to AEM/EMIS | SAP official community blog | High |
| PI/PO migration tooling | SAP-Press / SAP partner documentation | Medium |
| API Management Cloud Foundry | SAP GitHub docs repository | High |
| CloudEvents graduated CNCF project | CNCF / The New Stack | High |

## Why it matters

Integration is the backbone of SAP AMS. When integrations fail—IDoc errors, API timeouts, cloud connector outages, certificate expirations—business processes stop. The shift to cloud-native integration changes the failure modes: instead of file system or RFC errors, teams now see OAuth token failures, message queue backlogs, and event mesh topic misconfigurations. AMS teams need to build new diagnostic playbooks for these patterns.

## Practical implications

- **Monitoring shift.** Cloud Integration monitoring tracks message status, error rates, and retry counts. API Management monitors latency, throughput, and policy violations. Event Mesh monitors topic lag and consumer health. These are different metrics from traditional SM58/SM59 RFC monitoring.
- **Security model.** Cloud-to-on-premise connectivity depends on SAP Cloud Connector and OAuth 2.0 or certificate-based authentication. Certificate expiry is a recurring AMS incident pattern. Automate certificate renewal monitoring.
- **Event-driven extensibility.** S/4HANA business events (sales order created, purchase order changed, billing block status changed) can trigger BTP-side extensions without modifying the core. This is the clean-core pattern: keep S/4HANA standard, build extensions on BTP.
- **Migration planning.** Organizations still on PI/PO should assess Integration Suite readiness. The migration is not just technical—it involves rethinking integration design from file-based batch to API/event-based real-time.

## Risks and unknowns

- **EMIS vs standalone Event Mesh.** SAP has both EMIS (Integration Suite-embedded) and standalone Event Mesh. The long-term roadmap for standalone Event Mesh is unclear; EMIS appears to be the strategic path.
- **Cloud Connector dependency.** Any cloud-to-on-premise integration requires Cloud Connector. If the Cloud Connector node fails, all cloud integrations to on-premise systems stop. High-availability Cloud Connector setups are essential.
- **Event volume and cost.** Event Mesh pricing depends on message volume. High-frequency business events (e.g., every inventory movement) can generate significant cost. Plan event filtering and batching strategies.
- **AsyncAPI/CloudEvents SAP native support.** While SAP Event Mesh supports standard protocols (AMQP, MQTT), native CloudEvents envelope handling and AsyncAPI documentation generation are not first-class features as of 2026.

## Related Atlas links

- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)
- [SAP BTP](/atlas/sap/sap-btp/)
- [Business Events](/atlas/sap/business-events/)

## Next actions

- [ ] Audit current PI/PO landscape and identify candidates for Integration Suite migration.
- [ ] Test S/4HANA business event publishing to Event Mesh in a development environment.
- [ ] Review Cloud Connector high-availability setup and certificate renewal process.
- [ ] Evaluate CloudEvents as an event envelope standard for custom extensions.

## Sources

1. [SAP S/4HANA direct connectivity with Event Mesh in Integration Suite](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-s-4hana-direct-connectivity-with-event-mesh-in-integration-suite/ba-p/13752534)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: EMIS configuration, S/4HANA channel setup, OAuth 2.0 authentication

2. [SAP S/4HANA integration with SAP Integration Suite, Advanced Event Mesh](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-integration-with-sap-integration-suite-advanced-event-mesh/ba-p/13577271)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: S/4HANA 2023 FPS01 AEM connectivity, certificate-based authentication

3. [The Complete Guide to SAP Integration Suite](https://blog.sap-press.com/complete-guide-to-sap-integration-suite)
   - type: article
   - accessed: 2026-06-07
   - confidence: medium
   - used for: Integration Suite capabilities overview and certification objectives

4. [SAP-docs/btp-integration-suite — GitHub](https://github.com/SAP-docs/btp-integration-suite)
   - type: repository
   - accessed: 2026-06-07
   - confidence: high
   - used for: API Management, Cloud Integration, Integration Advisor documentation

5. [CNCF CloudEvents: A Li'l Message Envelope That Travels Far](https://thenewstack.io/cncf-cloudevents-a-lil-message-envelope-that-travels-far/)
   - type: article
   - accessed: 2026-06-07
   - confidence: high
   - used for: CloudEvents specification status, industry adoption, Microsoft/Azure usage

  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
