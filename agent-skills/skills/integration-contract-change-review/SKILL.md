---
name: integration-contract-change-review
description: Use this skill when an API, message, event, file, mapping, endpoint, identity, retry, or semantic integration contract changes. Review producers, consumers, compatibility, mixed-version behaviour, rollout order, tests, observability, rollback, and retirement criteria before release.
---

# Integration Contract Change Review

## Purpose
Review integration changes as changes to a business contract across producers and consumers, not only as schema edits.

## Use when
- API, event, message, file, or mapping fields change.
- Field meaning, type, format, mandatory status, or allowed values change.
- Endpoint, authentication, routing, retry, error, ordering, or timing behaviour changes.
- New producers or consumers join an integration.
- Version transition or backward-compatible rollout is required.

## Do not use when
- The contract is unchanged and a runtime failure needs troubleshooting.
- Only local implementation code changes with no externally visible contract effect.
- Producer and consumer inventory is unknown and must first be discovered through dependency or interface mapping.

## Required inputs
- Current and proposed contract.
- Business reason for change.
- Known producers and consumers.
- Schema, semantic, transport, identity, retry, and error behaviour where relevant.
- Existing versions and rollout constraints.
- Test and monitoring capabilities.

## Workflow
1. State the business reason and expected outcome change.
2. Define all affected contract surfaces: schema, semantics, values, identity, endpoint, headers, ordering, timing, errors, retries, idempotency, and service expectations.
3. Map direct and indirect producers and consumers.
4. Classify the change as additive, conditionally compatible, breaking, or semantically breaking.
5. Review semantic changes independently from schema compatibility.
6. Select a transition strategy: tolerant reader, dual-read, dual-write, versioning, feature flag, bridge mapping, staged rollout, or coordinated cutover.
7. Define mixed-version behaviour and rollout order.
8. Define contract, negative, retry, idempotency, and business-result tests.
9. Define observability, rollback, and owner during transition.
10. Define retirement criteria for old versions or compatibility paths.

## Decision rules
- Same field name and type does not imply same semantic contract.
- Do not assume consumers tolerate unknown fields or values; prove it.
- Making a field mandatory is breaking for any producer that cannot supply it.
- Retry or ordering changes require side-effect and idempotency review.
- Mixed-version operation must be understood before staggered rollout.
- Retire old behaviour only after usage evidence shows it is no longer required.

## Output format
Produce an **Integration Contract Change Review** containing:
- change ID and business reason;
- current and proposed contract;
- affected contract surfaces;
- producer/consumer inventory;
- compatibility classification;
- semantic changes;
- transition strategy and rollout order;
- mixed-version behaviour;
- tests and business validation;
- observability, rollback, retirement criteria, and owner.

## Quality gates
- Producers, consumers, and unknowns are explicit.
- Schema and semantic compatibility are both assessed.
- Error, retry, ordering, identity, and idempotency are included where relevant.
- Mixed-version behaviour is defined.
- Tests validate business result, not only parsing.
- Old behaviour has evidence-based retirement criteria.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
