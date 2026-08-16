---
name: business-rule-ownership-analysis
description: Use this skill when an enterprise business rule has unclear ownership, inconsistent implementation, exceptions, or cross-system impact. Identify the rule meaning, source, business owner, data dependencies, enforcement points, conflicts, exceptions, evidence, and controlled change path.
---

# Business Rule Ownership Analysis

## Purpose
Make an important business rule explicit and traceable across people, data, systems, controls, and changes. Separate ownership of rule meaning from technical implementation ownership.

## Use when
- Process behaviour differs across systems, channels, regions, or products.
- A configuration or logic change has no clear business owner.
- The same rule exists in several technologies.
- Exceptions and overrides have become common.
- A migration, redesign, integration, or AI workflow needs a reliable rule catalog.

## Do not use when
- The problem is only technical configuration drift between environments.
- The rule meaning is already clear and only implementation debugging is needed.
- Legal interpretation is required; route that decision to qualified legal ownership.

## Required inputs
- Rule statement or observed behaviour.
- Business process and scope.
- Known policies, contracts, standards, decisions, or configuration.
- Relevant systems and data fields.
- Stakeholders and known owners.
- Example transactions, documents, or cases where available.

## Workflow
1. State the rule in business language without system-specific implementation detail.
2. Define scope: organization, country, product, party, channel, document, process step, or other context.
3. Identify the authoritative source: policy, contract, regulation, approved design, master-data standard, or formal decision.
4. Identify the business owner who can decide what the rule means.
5. Identify required data and its owner.
6. Map every enforcement point: UI, workflow, configuration, code, integration, API policy, master data, batch logic, or manual control.
7. Compare implementations and identify conflicts or duplicated logic.
8. Record exceptions, override authority, duration, and visibility.
9. Collect evidence from representative process cases and implementation points.
10. Define the rule-change path: request, approve, implement, test, deploy, communicate, monitor, review.

## Decision rules
- Do not assume the application team owns the business meaning of a rule.
- If multiple systems enforce the same rule, treat them as separate implementation points until equivalence is proven.
- An exception without an approver, scope, and expiry is uncontrolled rule drift.
- If the authoritative source is unknown, mark the rule unresolved instead of inventing ownership.
- A rule change is incomplete until downstream implementations and tests are identified.
- Distinguish business owner, data owner, application owner, control owner, and change coordinator where they differ.

## Output format
Produce a **Business Rule Ownership Record** containing:
- rule ID, statement, purpose, and scope;
- authoritative source;
- business owner and data owner;
- required data;
- enforcement-point map and technical owners;
- known exceptions and approvers;
- conflicting implementations;
- evidence;
- change path, test requirement, monitoring, and review trigger.

## Quality gates
- Rule meaning is understandable without opening a technical configuration screen.
- Business ownership is separate from implementation ownership.
- All known enforcement points are listed.
- Exceptions and overrides are explicit.
- Conflicting implementations are visible.
- Change path includes impact analysis, testing, deployment, and communication.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
