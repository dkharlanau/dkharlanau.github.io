---
layout: default
title: "Chain of Responsibility Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Chain of Responsibility programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/chain-of-responsibility/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Chain of Responsibility</li></ol>
</nav>

# Chain of Responsibility

*GoF / behavioral* — **Try a defined sequence of handlers until one can answer.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A mapping lookup checks a source-specific exception, then a normal organization mapping. New exceptions are added frequently, and each one changes the precedence logic of a nested CASE.

## Classes and responsibilities

- ZIF_MAPPING_RESOLVER — TRY_RESOLVE(context) returns matched/value.
- ZCL_SPECIAL_SOURCE_RESOLVER — checks approved exceptions.
- ZCL_DEFAULT_ORG_RESOLVER — checks standard value mapping.
- ZCL_RESOLVER_CHAIN — enforces order and final failure.

## Apply it in four steps

1. Document resolution precedence as part of the business contract.
2. Let each handler return match/no match, never a hidden default.
3. Stop at the first match and record the matched rule for support.
4. If no handler matches, fail visibly before the write phase.

## Illustrative implementation

```text
INPUT: source system + source org + target scope
  -> Source-specific exception resolver
     -> matched? return mapping
     -> no match? Standard mapping resolver
        -> matched? return mapping
        -> no match? Raise missing-mapping error

Resolutions are pure. The application service writes later.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Chain of Responsibility | Handler: TRY_RESOLVE | Order: exception -> standard -> reject | Output: match + target + rule ID | Side effects: forbidden.

**Where it fits:** ABAP: compose handlers as injected classes. RAP: this is one controlled algorithm; do not split it into unrelated determinations and assume their execution order. CAP: separate explicitly ordered handlers from framework before handlers, which may run concurrently.

**Where it fails:** Avoid this chain when all stages must always run; use a Pipeline. For one simple keyed lookup, use a table.

## Acceptance tests

- [ ] Specific exception wins over normal mapping.
- [ ] No-match flows to the next resolver.
- [ ] A resolution does not invoke later handlers.
- [ ] No-match yields a controlled diagnostic.

## Distinguish it from similar patterns

Strategy selects one known algorithm; Chain of Responsibility discovers the first handler that can resolve a request.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
