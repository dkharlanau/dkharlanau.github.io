---
title: "Domain Research: Event-Driven Architecture"
robots: noindex
sitemap: false
---

# Event-Driven Architecture

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from event-driven patterns, schema registries, and message contract governance?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [AsyncAPI Specification](https://www.asyncapi.com/) (src-302) | 1 | Open standard for event-driven APIs | Event contracts, schema registry, code generation |
| [Martin Fowler EDA](https://martinfowler.com/articles/201701-event-driven.html) (src-306) | 2 | Taxonomy of four EDA patterns | Pattern selection, semantic clarity |
| [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/develop/api.html) (src-004) | 1 | API and compatibility mechanics for schema-based data contracts | Compatibility modes, ruleSet attachments |
| [Data Contracts Guide](https://datadef.io/guides/en/data-contracts) (src-309) | 3 | Practical implementable breakdown of data contracts | Semantic versioning, expand-then-contract migration |
| [Netflix Tech Blog](https://netflixtechblog.com/) (src-307) | 2 | Mature distributed systems operational practices | Chaos engineering, regional resilience |

## Key practical patterns

- Event Notification for loose coupling and dependency inversion.
- Event-Carried State Transfer for consumer autonomy (with eventual consistency).
- Event Sourcing for auditability and state reconstruction.
- AsyncAPI as the contract standard for event-driven systems.
- Schema registry with compatibility modes (BACKWARD, FORWARD, FULL).
- Semantic versioning for data contracts (MAJOR.MINOR.PATCH).
- Dead letter queues for invalid records in stream processing.

## Artifacts found

- AsyncAPI specifications defining channels, messages, and bindings
- Event catalogs with producer/consumer mappings
- Schema registry configurations and compatibility policies
- Event flow / topology diagrams
- Runbooks for event replay and dead-letter queue handling

## Decision rules found

- If a system needs loose coupling, use Event Notification rather than direct calls.
- If consumers need data without querying the source, accept eventual consistency and use Event-Carried State Transfer.
- If auditability is required, use Event Sourcing with an append-only log.
- If using Kafka/RabbitMQ, define protocol bindings in AsyncAPI.
- If an event schema changes, validate compatibility against the registry before deployment.

## Quality gates found

- AsyncAPI spec validation in CI/CD
- Schema registry compatibility checks
- Cross-reference analysis to detect unintended event chains
- Consumer contract tests for message handling
- Documentation of event semantics (events vs. commands)

## Common failure modes

- Treating events as commands (naming and semantic confusion)
- Schema drift between producers and consumers
- Missing documentation causing "no statement of overall behavior"
- Eventual consistency bugs when consumers assume immediate consistency
- CQRS implemented without sufficient operational maturity

## Candidate skills

- `asyncapi-contract-design`
- `event-driven-pattern-selection`
- `schema-registry-governance`
- `event-sourcing-operations`
- `dead-letter-queue-management`

## Source-backed notes

- AsyncAPI provides protocol-agnostic event contract specification with publish/subscribe semantics and code generation (src-302).
- Martin Fowler defines four EDA patterns and warns that CQRS is complex and often implemented incorrectly (src-306).
- Confluent Schema Registry defines compatibility modes (BACKWARD, FORWARD, FULL, TRANSITIVE) and ruleSet attachments (src-004).

## Gaps / further research needed

- Real-world production data contracts with schemas, SLAs, and enforcement logic are scarce.
- Event-driven postmortems explicitly dissecting message-level failures are fewer than infrastructure postmortems.