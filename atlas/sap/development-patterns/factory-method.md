---
layout: default
title: "Factory Method Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Factory Method programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/factory-method/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Factory Method</li></ol>
</nav>

# Factory Method

*GoF / creational* — **Centralize creation of interchangeable implementations.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

An inbound processor instantiates concrete CreatePartnerCommand and ChangePartnerCommand classes in several code branches. A new operation forces the caller to know even more implementation details.

## Classes and responsibilities

- ZIF_BP_COMMAND — shared executable contract.
- ZCL_BP_COMMAND_FACTORY — named creation operation.
- ZCL_CREATE_BP_COMMAND / ZCL_CHANGE_BP_COMMAND — concrete classes.
- ZCL_BP_INBOUND_PROCESSOR — only knows the interface.

## Apply it in four steps

1. Normalize the requested operation before construction.
2. Resolve from an allowlisted mapping rather than arbitrary class names in customizing.
3. Inject dependencies into the returned implementation.
4. Unknown modes must produce an explicit error; factory construction never writes data.

## Illustrative implementation

```abap
DATA(command) = command_factory->create_for(
  iv_operation = is_intent-operation ).

DATA(result) = command->execute( is_intent ).

"Factory returns REF TO ZIF_BP_COMMAND.
"The factory creates; the command executes.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Factory Method | Factory: CREATE_FOR(operation) | Output: REF TO ZIF_BP_COMMAND | Unknown operation: error | Construction side effects: none.

**Where it fits:** Works well in ABAP OO. RAP implementations must still obey framework transaction constraints. CAP can map service actions to injected implementation classes/functions without making a framework hook itself a factory.

**Where it fails:** Avoid an elaborate factory hierarchy if one stable concrete class exists.

## Acceptance tests

- [ ] Every supported operation resolves deterministically.
- [ ] Unsupported operation is rejected.
- [ ] Injected dependencies are supplied to new instances.
- [ ] Factory creation is free of business updates.

## Distinguish it from similar patterns

Factory Method constructs one implementation. Abstract Factory constructs a family of related implementations.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
