---
layout: default
title: "Unit of Work Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Unit of Work programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/unit-of-work/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Unit of Work</li></ol>
</nav>

# Unit of Work

*PoEAA / transaction management* — **Coordinate one logical change set at its legitimate transaction boundary.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A developer wants one transaction across changes, so they place COMMIT WORK in a RAP validation. This conflicts with RAP's save protocol and may produce failures that are hard to recover from.

## Classes and responsibilities

- Application service — states the intended operations.
- Persistence adapter — stages writes through supported APIs.
- Transaction owner — classic application LUW or framework-managed transaction.
- RAP runtime — owns its behavior/save sequence.

## Apply it in four steps

1. Name the actual owner of the transaction before coding.
2. In a classic custom service, stage and commit at the documented application boundary when permitted.
3. In RAP, use EML and behavior operations without manual COMMIT/ROLLBACK in handlers.
4. For cross-system work use compensation or messaging patterns; one local transaction cannot make remote services atomic.

## Illustrative implementation

```text
Classic custom application:
  collect changes -> validate -> persist through allowed APIs
  -> commit ONCE at the owning application boundary

RAP behavior handler:
  framework keys -> supported EML/behavior operations
  -> RAP save sequence owns commit / rollback

Never put COMMIT WORK or COMMIT ENTITIES inside RAP handlers.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Unit of Work | Scope: one local transaction | Coordinator: named runtime owner | Failure atomicity: documented | RAP: no manual commit in handler | Cross-system: not atomic.

**Where it fits:** RAP's BO implementation contract forbids COMMIT WORK, ROLLBACK WORK, EML COMMIT ENTITIES and EML ROLLBACK ENTITIES in handler methods. CAP also manages request transactions; use its transaction facilities rather than ad hoc nested commits.

**Where it fails:** Avoid implementing a new transaction coordinator when SAP's framework already owns the unit of work.

## Acceptance tests

- [ ] A local transaction either succeeds or follows the documented rollback behavior.
- [ ] No lower-layer method hides its own commit.
- [ ] RAP handler code contains no prohibited statements.
- [ ] External failure is not misrepresented as a local rollback.

## Distinguish it from similar patterns

Unit of Work coordinates local state. Outbox protects event intent across publication. Saga coordinates business steps across independent transactions.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
