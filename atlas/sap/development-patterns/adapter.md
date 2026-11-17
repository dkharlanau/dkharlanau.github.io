---
layout: default
title: "Adapter Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Adapter programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/adapter/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Adapter</li></ol>
</nav>

# Adapter

*GoF / structural* — **Provide one business-facing interface over incompatible provider contracts.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A service needs to read customer details. A legacy implementation exposes a function module and a newer one exposes a released API. Callers should not depend on those incompatible signatures.

## Classes and responsibilities

- ZIF_BP_GATEWAY — the consumer-owned read contract.
- ZCL_LEGACY_BP_ADAPTER — translates an approved legacy interface.
- ZCL_RELEASED_BP_ADAPTER — uses a supported released contract.
- ZCL_BP_APPLICATION_SERVICE — depends only on ZIF_BP_GATEWAY.

## Apply it in four steps

1. Specify the consumer's business-facing operation first.
2. Translate source types, result codes and exceptions inside the adapter.
3. Preserve authorization and transaction semantics; no hidden commits.
4. Inject the adapter and test against a fake.

## Illustrative implementation

```abap
INTERFACE zif_bp_gateway PUBLIC.
  METHODS read
    IMPORTING iv_key TYPE zbp_key
    RETURNING VALUE(rs_bp) TYPE zbp_s_partner
    RAISING zcx_bp_access.
ENDINTERFACE.

"Both ZCL_LEGACY_BP_ADAPTER and ZCL_RELEASED_BP_ADAPTER
"implement ZIF_BP_GATEWAY without changing its contract.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Adapter | Port: ZIF_BP_GATEWAY | Provider: legacy FM OR released API | Input/Output: stable DTO | Failures: mapped explicitly | Transaction: provider-owned.

**Where it fits:** ABAP Cloud: a wrapper does not magically make an unreleased SAP object permitted. Verify released APIs and the deployment model. RAP: use EML for supported BO consumption rather than bypassing behavior with SQL.

**Where it fails:** Avoid Adapter if you can simply call an already stable, approved interface directly.

## Acceptance tests

- [ ] Both adapters follow the same consumer contract.
- [ ] Missing object and missing authorization remain different errors.
- [ ] Provider-specific data types never leak to business classes.
- [ ] No implicit COMMIT occurs.

## Distinguish it from similar patterns

Adapter changes an interface. Decorator preserves the interface and adds behavior. Anti-Corruption Layer also translates meaning.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
