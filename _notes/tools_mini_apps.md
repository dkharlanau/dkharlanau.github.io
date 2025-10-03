---
title: "Mini Apps & Prototypes"
eyebrow: "Services"
subtitle: "I design and build small utilities and prototypes that unblock delivery without touching the SAP core."
tags:
  - Automation
  - UX
  - Prototyping
---

## What I build

Small, outcome‑focused tools that remove tedious manual work or unblock analysis fast. Typical shapes:

- **Exception handlers** that enrich and retry failed IDocs or AIF messages with one click.
- **One‑click reconciliations** that stitch SAP + spreadsheets + partner APIs and flag deltas.
- **Operational dashboards** that show the next best action, not a 40‑field SAP screen.
- **BP/CVI validators** for MDG rules, duplicate checks, postal/format fixes before posting.
- **Cutover simulators** that dry‑run steps, validate prerequisites, and produce ready checklists.
- **OData inspectors** to explore v2/v4 services, filter/expand, and generate example payloads.
- **BRFplus helpers** for decision table edits with guardrails, audit, and export.
- **Event‑first monitors** that correlate events (Kafka/Event Mesh) with interface health.

## Why teams use this

- Fast wins to keep sponsors confident and unblock delivery.
- Clean core stays intact — utilities sit on the edge, portable and well‑documented.
- Bespoke UX for ops — explain the next action and automate the boring steps.

## Delivery options

- **5‑Day Prototype**
  - Scope a single pain point, ship a working prototype (clickable UI or service).
  - Includes README, demo video, backlog, and effort to productionise.

- **10–20 Day Mini App**
  - Production‑ready edge service or UI with observability, auth, and handover docs.
  - Integration with AIF/IDoc/OData as needed; deployable on‑prem or cloud.

## Tech stack

- **Runtime:** FastAPI or Spring Boot for services.
- **Frontend:** React/Next.js or SAP UI5 when needed.
- **Integration:** OData v2/v4, IDoc/AIF, REST, EDI.
- **Data:** Feature views and curated tables behind one API; avoid one‑off SQL.
- **Automation:** Temporal or Airflow for orchestrations; observable jobs by default.
- **Hosting:** Docker/Kubernetes, or serverless if it fits the use case.
- **Security:** SSO via the enterprise IdP, OPA policies, auditable logs.

## Reference mini apps (examples)

- AIF reprocessing assistant with safe enrichment and bulk retry.
- IDoc retry tool with partner‑profile awareness and queue visibility.
- BP/CVI pre‑check for addresses, roles, and mapping before posting to S/4.
- O2C event‑first monitor that reduces diagnosis time from hours to minutes.
- Cutover simulator producing a step‑by‑step runbook and risk checks.
- OData service explorer with saved queries and exportable examples.
- BRFplus decision‑table editor with diff, audit trail, and export.
- Reconciliation toolkit for pricing, deliveries, and billing deltas.

## How I work

1. Catalogue recurring manual steps causing friction (with concrete examples).
2. Prototype the smallest tool that removes the pain, ship to one pilot team.
3. Measure the impact (time saved, errors removed), then productionise where it pays back.

## Outcomes to track

- Fewer manual retries and rework.
- Lower MTTR for incidents and interface issues.
- Faster reconciliations and cutovers.
- Clear audit trail and handover‑ready documentation.

## Request a prototype

If you have a specific pain point (IDoc chaos, BP/CVI noise, fragile cutovers), I can develop a small mini app or prototype to solve it. Prefer fixed‑scope, short‑cycle engagements.

_This page will keep expanding as reference implementations solidify._
