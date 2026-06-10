---
title: "Domain Research: Observability and SRE"
robots: noindex
sitemap: false
---

# Observability and SRE

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from observability design, SLO management, and reliability engineering?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [OpenTelemetry Documentation](https://opentelemetry.io/docs/what-is-opentelemetry/) (src-303) | 1 | CNCF-backed open standard for unified telemetry | Distributed tracing, metrics, logs |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) (src-403) | 1 | Foundational SRE text with public chapters | Emergency response, incident management, postmortems |
| [Google SRE Workbook — Postmortem Culture](https://sre.google/workbook/postmortem-culture/) (src-402) | 1 | Definitive public chapter on blameless postmortems | Postmortem templates, action item tracking |
| [DORA 2024 Report](https://dora.dev/) (src-308) | 2 | Largest longitudinal study of software delivery | Four key metrics, platform engineering |
| [Netflix Tech Blog](https://netflixtechblog.com/) (src-307) | 2 | Mature public examples of chaos engineering | Chaos Monkey, regional deploys, canary analysis |

## Key practical patterns

- Distributed tracing with context propagation across all service boundaries.
- Structured logging with trace/span IDs for correlation.
- Metrics aligned to user experience (SLOs, error budgets).
- OpenTelemetry as the vendor-neutral instrumentation standard.
- Sampling strategies to manage telemetry volume and cost.
- Blameless postmortems focus on systemic failures, not individual errors.
- Error budget policies: if budget is exhausted, halt feature work.

## Artifacts found

- OpenTelemetry instrumentation configuration
- Trace context propagation maps (W3C, B3, Jaeger)
- SLO definitions and error budget policies
- Dashboards linking latency, errors, and saturation (USE/RED methods)
- Runbooks correlating traces to known failure signatures
- Postmortem template (bad vs. good examples)
- Action item tracker with owners and due dates

## Decision rules found

- If a request crosses a service boundary, propagate trace context.
- If telemetry volume is too high, implement sampling rather than disabling instrumentation.
- If using multiple observability backends, export via OTLP.
- If an alert fires, it must be actionable and tied to an SLO.
- If a service is critical, define RED metrics (Rate, Errors, Duration) per endpoint.
- If SLO is missed and toil is high, offload toil and fix the product.

## Quality gates found

- Auto-instrumentation coverage for all services
- Context propagation validated through service mesh / proxy layers
- SLO review meetings with error budget burn rate tracking
- Alert fatigue audits (remove non-actionable alerts)
- Trace-to-log correlation tested in incident drills
- Postmortems must be blameless and reviewed for judgmental language
- Action items must be specific, assigned, and tracked to completion

## Common failure modes

- Broken trace context at load balancers or proxies causing fragmented traces
- Over-sampling saturating telemetry backends
- Metrics without SLOs leading to alert fatigue
- Missing custom spans for business-critical operations
- Observability treated as "logging everything" without queryability
- Postmortems that assign individual blame, preventing honest reporting
- Action items filed and forgotten without tracking

## Candidate skills

- `opentelemetry-instrumentation`
- `distributed-tracing-propagation`
- `slo-and-error-budget-design`
- `observability-driven-debugging`
- `telemetry-sampling-and-cost`
- `blameless-postmortem-writing`
- `action-item-tracking`

## Source-backed notes

- OpenTelemetry provides auto-instrumentation agents, context propagation, and the Collector as a processing pipeline (src-303).
- Google SRE Book defines the distinction between incident management (restore service) and problem management (prevent recurrence) (src-403).
- Google SRE Workbook provides a side-by-side case study of a "bad" vs. "good" postmortem (src-402).
- DORA identifies four key metrics: Deployment Frequency, Lead Time, Change Failure Rate, Failed Deployment Recovery Time (src-308).

## Gaps / further research needed

- Vendor-neutral observability trace format standards are still emerging.
- Real-world cost and latency benchmarks for multi-agent workflows with reflection loops are scarce.