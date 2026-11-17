---
layout: default
title: "Thin RAP Handler Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Thin RAP Handler programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/thin-rap-handler/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Thin RAP Handler</li></ol>
</nav>

# Thin RAP Handler

*SAP / framework idiom* — **Keep behavior handlers about framework contracts; delegate pure business rules.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A RAP validation method reads data, calculates policy, performs remote calls, modifies another BO and commits. Most of these activities should not be in the validation, and some are prohibited.

## Classes and responsibilities

- RAP behavior pool — gets keys and returns FAILED/REPORTED messages.
- ZIF_VALIDATION_POLICY — pure CHECK(candidate) result.
- ZCL_VALIDATION_POLICY — ABAP Unit tested implementation.
- Supported read adapter — retrieves only required BO fields.

## Apply it in four steps

1. Read only the fields required by the validation using supported RAP behavior operations.
2. Call a pure policy class for the business question.
3. Map violations to RAP FAILED/REPORTED with typed messages.
4. Let RAP save sequence own the transaction; use supported auxiliary classes for reusable logic where appropriate.

## Illustrative implementation

```text
RAP validation:
  READ ENTITIES ... IN LOCAL MODE
  LOOP AT instances
    result = validation_policy->check( instance )
    if not valid:
      append key to FAILED
      append message to REPORTED
  ENDLOOP

Do not use EML MODIFY inside a RAP validation.
Do not COMMIT WORK in a RAP behavior handler.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Thin RAP Handler | Entry: behavior pool | Delegate: testable pure policy | Failure: FAILED/REPORTED | Transaction owner: RAP | Forbidden operations: no EML MODIFY in validation, no COMMIT in handler.

**Where it fits:** SAP provides RAP behavior contracts and ABP auxiliary classes for appropriate reuse. The exact available implementation types and support vary by edition/release. CAP hooks have different execution semantics and must not be treated as identical to RAP determinations and validations.

**Where it fails:** Avoid creating one forwarding class for every two-line RAP method. Extract logic where it has a stable rule, tests or reuse value.

## Acceptance tests

- [ ] Rule classes pass ABAP Unit independently of RAP.
- [ ] Failed instances map to correct keys and messages.
- [ ] No handler performs a forbidden commit.
- [ ] No unintended dependency on order between determinations.

## Distinguish it from similar patterns

This is an SAP realization of Separation of Concerns and Dependency Injection, not an additional GoF pattern.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
