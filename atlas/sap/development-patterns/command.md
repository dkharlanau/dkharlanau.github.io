---
layout: default
title: "Command Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Command programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/command/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Command</li></ol>
</nav>

# Command

*GoF / behavioral* — **Represent an operation as an object with one execution contract.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

One inbound message can express create, change, replace or wait. Parsing the message and doing all updates inside one CASE statement mixes classification, business execution, error reporting and retry semantics.

## Classes and responsibilities

- ZIF_BP_COMMAND — EXECUTE(intent) returning a typed result.
- ZCL_CREATE_BP_COMMAND / ZCL_CHANGE_BP_COMMAND / ZCL_SKIP_BP_COMMAND — operation implementations.
- ZCL_BP_COMMAND_FACTORY — resolves a normalized operation to one command.
- ZCL_BP_INBOUND_PROCESSOR — orchestrates classification, rule evaluation and execution.

## Apply it in four steps

1. Read relevant message function and segment semantics, then normalize them into a supported operation.
2. Resolve a command; reject unknown operations instead of defaulting to create.
3. Execute using one clearly identified transaction-owning application boundary.
4. Preserve correlation ID, result and duplicate processing policy.

## Illustrative implementation

```abap
INTERFACE zif_bp_command PUBLIC.
  METHODS execute
    IMPORTING is_intent TYPE zbp_s_intent
    RETURNING VALUE(rs_result) TYPE zbp_s_result
    RAISING zcx_bp_processing.
ENDINTERFACE.

DATA(command) = command_factory->create_for(
  iv_operation = is_intent-operation ).
DATA(result) = command->execute( is_intent ).
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Command | Input: normalized operation+intent | Dispatcher: ZCL_BP_COMMAND_FACTORY | Command: ZIF_BP_COMMAND~EXECUTE | Transaction: application/framework owned | Unsupported mode: reject.

**Where it fits:** Classic ABAP: implementations can call an approved application service or BAPI through a gateway. RAP: use a behavior action when a consumer explicitly requests an operation; never insert COMMIT inside RAP handlers. CAP: custom on handlers can delegate to a command service.

**Where it fails:** Avoid Command when a direct method call is already sufficient and no selection, tracing, deferred execution or common dispatch is needed.

## Acceptance tests

- [ ] Every supported operation is dispatched correctly.
- [ ] A wait/no-op operation does not write.
- [ ] An unsupported function code reports an error.
- [ ] Duplicate delivery follows an explicit idempotency contract.

## Distinguish it from similar patterns

Command describes *what operation to execute*; Strategy swaps *the algorithm used*; State controls *when an operation is allowed*.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
