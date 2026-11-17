---
layout: default
title: "Decorator Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Decorator programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/decorator/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Decorator</li></ol>
</nav>

# Decorator

*GoF / structural* — **Add logging, metrics or policy around a service without rewriting it.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A working outbound gateway needs correlation tracing and duration measurement. Adding tracing code to every business method risks changing the result contract.

## Classes and responsibilities

- ZIF_BP_GATEWAY — the common wrapped and wrapper interface.
- ZCL_BP_API_GATEWAY — the real read/write implementation.
- ZCL_TRACING_BP_GATEWAY — receives a gateway in its constructor and delegates.
- ZIF_TRACE_SINK — accepts redacted technical metadata.

## Apply it in four steps

1. Preserve the exact interface of the wrapped object.
2. Delegate to the original method once and propagate its result/errors.
3. Record only permitted diagnostic metadata and timing.
4. Specify decoration order and what happens if telemetry fails.

## Illustrative implementation

```text
ZCL_BP_APPLICATION_SERVICE
  -> ZCL_TRACING_BP_GATEWAY (ZIF_BP_GATEWAY)
     -> ZCL_BP_API_GATEWAY (ZIF_BP_GATEWAY)

READ(key):
  start timer
  delegate READ(key)
  record duration and outcome
  return the original result or exception
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Decorator | Interface: ZIF_BP_GATEWAY | Wrapped service: immutable dependency | Extra behavior: redacted tracing | Errors: preserved | Transaction: unchanged.

**Where it fits:** ABAP: one wrapper per cross-cutting concern, injected around the gateway. RAP/CAP: keep framework transaction and error semantics intact; do not use a decorator as a secret second writer.

**Where it fails:** Avoid wrapping every class solely for aesthetics; use platform observability when it already solves the need.

## Acceptance tests

- [ ] The underlying call executes exactly once.
- [ ] Exceptions propagate unchanged.
- [ ] Trace failures follow a documented policy.
- [ ] Sensitive payload values are not logged.

## Distinguish it from similar patterns

Decorator adds behavior without changing the interface; Adapter changes the interface.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
