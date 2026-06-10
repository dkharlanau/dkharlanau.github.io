---
title: "Domain Research: API Design"
robots: noindex
sitemap: false
---

# API Design

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from REST API design, versioning, and governance?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [Google AIPs](https://google.aip.dev/) (src-301) | 1 | Google's public API design standards | Resource-oriented design, versioning, field behavior |
| [AsyncAPI Specification](https://www.asyncapi.com/) (src-302) | 1 | Open standard for event-driven APIs | Event contracts, schema registry, code generation |
| [Stripe Idempotency](https://stripe.com/docs/api/idempotent_requests) (src-305) | 2 | Industry reference for safe retries | Idempotency keys, state machines |
| [Treblle API Governance](https://treblle.com/blog/api-governance-best-practices) (src-312) | 3 | Practical checklist-oriented synthesis | OpenAPI-first, Spectral linting, breaking-change detection |
| [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) (src-304) | 1 | Cloud-vetted API deployment practices | Canary analysis, Blue/Green deployment |

## Key practical patterns

- Resource-oriented naming (nouns, not verbs) with hierarchical collections.
- Standard methods (List, Get, Create, Update, Delete) with consistent HTTP mapping.
- Major-only versioning (`v1`, not `v1.0.1`) with deprecation periods.
- Field behavior annotations (REQUIRED, OUTPUT_ONLY, IMMUTABLE).
- OpenAPI spec as source of truth; linting in CI/CD via Spectral.
- Breaking-change detection with OpenAPI diff tools (oasdiff).
- Uniform error models and pagination across the API surface.

## Artifacts found

- OpenAPI/AsyncAPI specifications in version control
- API style guide (enforceable ruleset)
- Mock server configuration
- Changelog and migration guide
- API catalog / inventory with ownership metadata
- Breaking-change detection CI job

## Decision rules found

- If an API exposes a collection, it must use a standard List method with pagination.
- If a field is user-settable at creation but immutable afterward, mark it `IMMUTABLE`.
- If an API violates a standard, it must include a justification comment.
- If a breaking change is required, provide at least one major version deprecation cycle.
- If an API has no OpenAPI spec, it is not published.

## Quality gates found

- OpenAPI linting passes in CI/CD
- Breaking-change detection on PR blocks merge if breaking
- Design review with stakeholders before coding
- Contract tests validate implementation against spec
- Runtime validation of request/response against published schema

## Common failure modes

- APIs modeled as database schemas (tight coupling anti-pattern)
- Inconsistent naming and error shapes across teams
- Breaking changes deployed without consumer notification
- Missing pagination causing performance degradation at scale
- Manual governance that does not scale

## Candidate skills

- `openapi-design-first`
- `api-style-guide-enforcement`
- `breaking-change-detection`
- `api-versioning-and-deprecation`
- `contract-testing-rest`

## Source-backed notes

- Google AIPs define resource-oriented design, standard methods, and field behavior annotations (src-301).
- Treblle recommends OpenAPI-first with Spectral linting and oasdiff for breaking-change detection (src-312).
- AWS Well-Architected recommends canary analysis and Blue/Green deployment for API changes (src-304).

## Gaps / further research needed

- Azure REST API guidelines would add a third major cloud perspective.
- Public API product management case studies linking organizational structure to API ownership outcomes are limited.