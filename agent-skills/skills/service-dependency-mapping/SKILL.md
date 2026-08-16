---
name: service-dependency-mapping
description: Use when a business capability depends on several services, APIs, queues, data stores, identity providers, jobs, platforms, or third parties and the team needs a runtime dependency map with ownership, failure impact, and health evidence. Produces a Service Dependency Map Record. Do not use for a generic landscape inventory that is not tied to a business outcome.
---

# Service Dependency Mapping

## Purpose

Map the runtime dependencies required for one business outcome, including direction, dependency type, failure effect, ownership, and the signal that proves each critical dependency is healthy.

## Use when

- A business flow crosses several technical components.
- Incident routing is slow because dependency and ownership boundaries are unclear.
- A release or change needs blast-radius understanding.
- Component monitoring exists but business impact of dependency failure is unclear.

## Do not use when

- The goal is only a generic application inventory.
- One concrete failed transaction needs tracing. Use `end-to-end-flow-trace`.
- You only need organizational ownership without runtime dependency analysis.

## Required inputs

- Business capability or critical user journey.
- Known systems, services, interfaces, jobs, stores, platforms, and third parties.
- Owners or support teams where known.
- Runtime traces, architecture diagrams, interface catalogs, or monitoring evidence where available.

## Workflow

1. Define the business outcome and actor or process that depends on it.
2. Map the entry point: UI, API, event, file, job, or manual action.
3. Trace direct runtime dependencies such as services, databases, queues, identity, configuration, storage, networks, and third parties.
4. Trace asynchronous and hidden dependencies such as jobs, retries, consumers, caches, and reference-data refreshes.
5. Type each dependency as hard runtime, soft/degraded, asynchronous, data freshness, security, operational, or human.
6. Record failure effect: blocked, delayed, stale, partial, duplicate, degraded, or invisible.
7. Record provider owner, consumer owner, and escalation boundary.
8. Define the health evidence that proves each critical dependency works for this business path.
9. Identify shared dependencies, single points, high-blast-radius nodes, and ownership gaps.
10. Validate the map with one known-good runtime trace.
11. Connect the map to observability, incident routing, change impact, and release readiness.

## Decision rules

- Add a component only when the selected business outcome depends on it.
- Separate runtime dependency from administrative grouping or deployment ownership.
- A technically available dependency can still fail through stale or semantically wrong data.
- Unknown ownership on a critical boundary is an operational risk.
- Architecture diagrams are hypotheses until runtime evidence validates the critical path.

## Output format

Produce a **Service Dependency Map Record**:

```markdown
## Business outcome
Capability / journey:
Actor:
Entry point:

## Dependencies
| From | To | Type | Failure effect | Provider owner | Consumer owner | Health evidence |
|---|---|---|---|---|---|---|

## Critical and shared dependencies

## Single points / high blast radius

## Ownership gaps

## Observability gaps

## Known-good trace validation
Trace object:
Result:
Map changes after trace:

## Operational actions
```

## Quality gates

- [ ] The map begins with a business outcome.
- [ ] Dependencies are directional and typed.
- [ ] Failure effect is stated for critical boundaries.
- [ ] Provider and consumer ownership is visible.
- [ ] Critical dependencies have health evidence or an explicit observability gap.
- [ ] Shared and high-blast-radius dependencies are identified.
- [ ] A real trace validates the important path.

## References

- `references/method.md` — Dependency typing, failure-impact, and validation model.
- `references/templates.md` — Dependency map and operational-gap templates.
- `references/examples.md` — Synthetic checkout, integration, data freshness, and shared-identity cases.
