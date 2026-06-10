---
title: "Domain Research: Integration Architecture"
robots: noindex
sitemap: false
---

# Integration Architecture

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from integration design, failure handling, and observability patterns?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [Google AIPs](https://google.aip.dev/) (src-301) | 1 | Google's public API design standards | Resource-oriented design, versioning, field behavior |
| [AsyncAPI Specification](https://www.asyncapi.com/) (src-302) | 1 | Open standard for event-driven APIs | Event contracts, schema registry, code generation |
| [OpenTelemetry Documentation](https://opentelemetry.io/docs/what-is-opentelemetry/) (src-303) | 1 | CNCF-backed open standard for unified telemetry | Distributed tracing, metrics, logs |
| [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) (src-304) | 1 | Six-pillar framework with integration reliability guidance | Deployment guardrails, canary analysis |
| [Stripe Idempotency](https://stripe.com/docs/api/idempotent_requests) (src-305) | 2 | Industry reference for safe retries in payment APIs | Idempotency keys, state machines, hash validation |
| [Martin Fowler EDA](https://martinfowler.com/articles/201701-event-driven.html) (src-306) | 2 | Taxonomy of four EDA patterns | Event Notification, ECST, Event Sourcing, CQRS |
| [Netflix Tech Blog](https://netflixtechblog.com/) (src-307) | 2 | Mature public examples of distributed API operations | Chaos engineering, regional deploys, canary analysis |
| [DORA 2024 Report](https://dora.dev/) (src-308) | 2 | Largest longitudinal study of software delivery performance | Four key metrics, platform engineering |

## Key practical patterns

- Resource-oriented naming (nouns, hierarchical collections) over action-oriented endpoints.
- Standard HTTP methods with consistent request/response shapes.
- Major-only versioning (`v1`, `v2`) with explicit deprecation windows.
- OpenAPI/AsyncAPI as contract-first design artifacts.
- Uniform error models and pagination conventions across the API surface.
- Idempotency keys for safe retries of non-idempotent operations.
- Exponential backoff with jitter to prevent thundering herds.
- Circuit breakers to fail fast and protect downstream services.
- Distributed tracing with context propagation across all service boundaries.

## Artifacts found

- OpenAPI/AsyncAPI specifications under version control
- API style guides (enforceable via linting rulesets)
- Mock servers generated from specs for early consumer feedback
- Changelogs and migration guides for version transitions
- API catalogs / inventories with ownership metadata
- Idempotency key database schemas and TTL policies
- Retry policy configuration (backoff strategy, max attempts, jitter)
- Circuit breaker threshold and timeout settings
- OpenTelemetry instrumentation configuration
- SLO definitions and error budget policies

## Decision rules found

- If an endpoint represents a collection, it must support standard List with pagination.
- If a field behavior changes (immutable → mutable), bump the major version.
- If a new API is proposed without an OpenAPI spec, block publication until the spec is provided.
- If a POST operation has side effects, require an idempotency key.
- If a failure is transient, retry with capped exponential backoff and jitter.
- If a service is consistently failing, open the circuit breaker and fail fast.
- If a request crosses a service boundary, propagate trace context.

## Quality gates found

- OpenAPI linting passes in CI/CD (Spectral or equivalent)
- Breaking-change detection on PR (oasdiff or equivalent)
- Design review with stakeholders before coding begins
- Contract tests validate implementation against spec
- Idempotency key collision detection and request hash validation
- Circuit breaker monitoring (error rate, open-state duration)
- Auto-instrumentation coverage for all services
- Context propagation validated through service mesh / proxy layers

## Common failure modes

- APIs modeled as database schemas (tight coupling to storage)
- Inconsistent naming and error shapes across teams
- Breaking changes deployed without consumer notification
- Missing pagination causing performance degradation at scale
- Retry storms overwhelming a recovering service
- Double-charging due to partial failure mid-handler
- Broken trace context at load balancers or proxies causing fragmented traces

## Candidate skills

- `openapi-design-first`
- `api-style-guide-enforcement`
- `breaking-change-detection`
- `api-versioning-and-deprecation`
- `contract-testing-rest`
- `idempotency-key-design`
- `retry-and-backoff-strategy`
- `circuit-breaker-implementation`
- `opentelemetry-instrumentation`
- `distributed-tracing-propagation`

## Source-backed notes

- Google AIPs require resource-oriented design, standard methods, and field behavior annotations (src-301).
- AsyncAPI provides protocol-agnostic event contract specification with publish/subscribe semantics (src-302).
- OpenTelemetry replaces OpenTracing and OpenCensus with unified traces, metrics, and logs (src-303).
- Stripe's idempotency pattern uses a state machine (NEW → IN_PROGRESS → COMPLETED) with request hash validation (src-305).
- Martin Fowler defines four EDA patterns: Event Notification, Event-Carried State Transfer, Event Sourcing, CQRS (src-306).
- DORA identifies four key metrics: Deployment Frequency, Lead Time, Change Failure Rate, Failed Deployment Recovery Time (src-308).

## Gaps / further research needed

- Azure API design guidance would provide a useful third-cloud perspective.
- Real-world data contract public examples with schemas, SLAs, and enforcement logic are scarce.
- Interface ownership organizational patterns (Team Topologies) exist but public case studies linking org structure to API ownership outcomes are thinner.
- IETF idempotency keys draft is promising but not yet finalized.