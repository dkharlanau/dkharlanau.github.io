---
title: "Composable ERP — Philosophy & Playbook"
description: "Composable ERP strategy to keep clean core S/4HANA, protect SAP order-to-cash, and run event-driven integrations on portable tech with cost guardrails."
eyebrow: "Opinionated essay"
subtitle: "S/4HANA as the core. Best‑of‑breed at the edges. Open contracts. Zero drama."
tags:
  - ERP
  - Architecture
  - Clean Core
  - Best of Breed
  - Composable Enterprise
further_reading:
  - label: "Cut MTTR with the SAP AMS order-to-cash stabilisation approach"
    url: "/notes/ams/"
  - label: "Deploy AI/ML sidecars that respect clean core S/4HANA boundaries"
    url: "/notes/ai-ml/"
  - label: "Govern SAP integration architecture for event-driven resilience"
    url: "/notes/system-architecture/"
---

> I like S/4HANA as the backbone for finance and logistics. I don’t love platform decisions made because a slide says “use only SAP‑branded everything.” Capability first. Open technology. No avoidable lock‑in.

## What “composable” means to me

Composable ERP is capability‑driven, not vendor‑driven. The S/4 core remains the source of record for postings, document flow, inventory, and compliance. Everything else lives at the edges as small, replaceable services speaking versioned **APIs**, clear **events**, and curated **data products**. If a tool becomes too slow, too expensive, or too opinionated, we can replace it without touching the core.

## Principles

1. **Clean core S/4** for legal truth, audit, performance.
2. **Best‑of‑breed by default** at the edges; suite only when it’s clearly superior.
3. **Open interfaces first**: OData v2/v4, REST, AsyncAPI events, IDoc/AIF when needed.
4. **Portability**: run on standard runtimes (containers/Kubernetes/serverless) and keep brokers swappable.
5. **Cost clarity**: predict 3‑year TCO, not just month‑1 licensing.
6. **Observability outside‑in**: logs, metrics, and traces leave the garden.
7. **Small, reversible steps**: prototypes that can be thrown away without regret.
8. **Decision transparency**: ADRs and runbooks, not folklore.

> Composable enterprise is not new. It’s a disciplined way of designing around business capabilities (popularized by Gartner) so teams can ship faster without breaking the backbone.

## Best‑of‑breed vs suite: how I choose

| Choose SAP‑native | Choose best‑of‑breed/open |
|---|---|
| Tight coupling to S/4 authorizations and document flow | Loose coupling, clear contracts, and frequent change |
| Compliance logic that must execute in‑core | Exploratory logic (pricing sims, validations, reconciliation) |
| Unique capabilities that are actually best in class | Commodity capabilities available across ecosystems |
| Operational simplicity matters more than flexibility | Portability, cost control, and speed matter more |

**Rule of thumb:** if a capability can live on portable runtimes with portable contracts, I keep it outside the core and outside any single vendor’s walled garden.

## Boundaries of the S/4 core

Keep **inside S/4**: postings, document flow, inventory, BP master data consistency, legal compliance, credit control gating.

Push **to the edges**: pricing exploration and what‑ifs, pre‑posting validation (BP/CVI, addresses, duplicates), reconciliations across SAP/partners, operational analytics and dashboards, integration adapters, orchestration and automation.

## Lock‑in tests I run

- **API portability test:** can this interface run on two runtimes with no code change?
- **90‑day exit test:** can we move this capability in under 90 days without breaking the core?
- **Shadow deployment test:** can we run an alternative side‑by‑side and switch by config?
- **Price predictability test:** do we understand per‑message, per‑connection, and egress costs at peak?

If any test fails, we rethink the platform choice.

## On BTP vs open runtimes

I will use BTP when it is clearly the best fit for a specific capability and when exit costs are acceptable. Otherwise I prefer standard runtimes (containers/serverless), open brokers, and observability that the enterprise already owns. Platform is a tool, not a doctrine.

## AI layer: how I pick and why I stay decoupled

Different teams will prefer different AI stacks. My selection criteria:

- **Capability:** reasoning quality, tool/agent APIs, function calling.
- **Safety & controls:** policy enforcement, red‑teaming, auditability.
- **Enterprise fit:** deployment options, data retention, fine‑grained access.
- **Ecosystem velocity:** SDKs, community, integrations, roadmap pace.
- **Cost/performance:** tokens per dollar, throughput, latency under load.

**Joule vs OpenAI vs Anthropic (high‑level view):**
- *Joule* aligns tightly with SAP context and workflows inside the suite. Good for embedded SAP tasks, less portable by design.
- *OpenAI* offers broad developer tooling and rapid ecosystem velocity; strong for general prototyping and agent patterns.
- *Anthropic* emphasizes safety controls and constitutional approaches; strong fit where risk tolerance is low and policy clarity is required.

**My stance:** keep an **LLM gateway** in front (your API), so you can route traffic to whichever provider fits a given task, and switch without refactoring products.

## Contracts that last

**APIs**
```http
GET /v1/business-partners/{id}?expand=roles,addresses
Accept: application/json
```
- Version in the path; never silently break. Pagination and filtering explicit.

**Events** (AsyncAPI sketch)
```yaml
asyncapi: 2.6.0
info: { title: bp-events, version: 1.0.0 }
channels:
  bp.changed.v1:
    subscribe:
      message:
        name: BpChanged
        payload:
          type: object
          properties:
            bpId: { type: string }
            changed: { type: array, items: { type: string } }
```
- Stable topics, schema-versioned payloads, idempotent consumers.
- Treat SAP Integration Suite Event Mesh (sap integration suite event mesh) as just another broker: same contracts, runtime exit tests, and observability you control.

**Data products**
- Curated views for O2C and MDG quality with owners, SLAs, lineage, and access policy.

## Cost model I use

- Traffic profile: peak RPS, messages/day, payload sizes.
- Variable vs fixed: broker egress, runtime minutes, storage IO, observability.
- 3‑year TCO: licenses + infra + ops + support + change.
- Exit cost and time: how hard is a platform move if economics change?

## Operating model

- Two‑week capability probes with ADRs for each decision.
- Contract tests in CI; schema registries for events and APIs.
- Shared observability (logs/metrics/traces) independent of any one platform.

## Anti‑patterns

- “Everything with the vendor label” as a starting point.
- Customizing the S/4 core to get short‑term velocity.
- Locking into a single broker or closed observability.
- Shadow Excel solutions with no contracts or lineage.

## What good looks like

- Faster change cycles without fear of breaking the core.
- Fewer incidents from custom code in the wrong place.
- Predictable costs and the freedom to swap an edge service without a program.

---

If you share the goal — stable S/4 core, fast edges, zero lock‑in — this is the path I follow.
