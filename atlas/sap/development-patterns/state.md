---
layout: default
title: "State Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "State programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/state/
author: "Dzmitryi Kharlanau"
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-17
hide_global_cta: true
tags: [sap, abap, rap, cap, design-patterns, software-architecture]
related:
  - /atlas/sap/development-patterns/
  - /labs/enterprise-context/development/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">State</li></ol>
</nav>

# State

*GoF / behavioral* — **Model legal behavior and transitions around lifecycle state.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

An approval request moves between DRAFT, READY, APPROVED and CANCELLED. A late update must not reopen an approved request, and UI action availability is not a sufficient security control.

## Classes and responsibilities

- ZIF_REQUEST_STATE — state-dependent operations and guards.
- ZCL_DRAFT_STATE / ZCL_READY_STATE / ZCL_APPROVED_STATE — legal transition behavior.
- ZCL_REQUEST_WORKFLOW — owns persisted state and transition.
- ZIF_AUTHORIZATION_POLICY — separate permission rule.

## Apply it in four steps

1. Write the state transition table before implementing code.
2. Keep guards and invalid-transition errors explicit.
3. Persist state and business data through the correct transaction boundary.
4. Express available actions in RAP feature control, but enforce authorization separately.

## Illustrative implementation

```text
DRAFT --submit--> READY --approve--> APPROVED
   |                 |
   +--cancel------> CANCELLED
   READY --cancel-> CANCELLED

approve(DRAFT) -> invalid transition
approve(READY) -> APPROVED
approve(APPROVED) -> reject or idempotent result by policy
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: State | State: persisted | Events: submit/approve/cancel | Guards: invariants+permissions | Invalid transition: typed failure | Concurrency: checked.

**Where it fits:** ABAP: state classes or a guarded transition table are both valid implementations. RAP: expose explicit actions and feature control, and separately enforce authorization. CAP: validate transitions in a domain service invoked from an on handler.

**Where it fails:** Avoid class-per-state machinery for a trivial display status without behavioral variation.

## Acceptance tests

- [ ] Every permitted transition succeeds.
- [ ] Every forbidden transition is rejected.
- [ ] Parallel or stale updates cannot overwrite later states.
- [ ] Feature availability and backend authorization are tested separately.

## Distinguish it from similar patterns

Strategy varies algorithm by selection; State varies behavior because the object changes lifecycle state.

## Sources and constraints

- [State — Refactoring.Guru](https://refactoring.guru/design-patterns/state)
- [RAP BO operations — SAP Help (transaction-specific actions)](https://help.sap.com/docs/abap-cloud/abap-rap/operations)

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
