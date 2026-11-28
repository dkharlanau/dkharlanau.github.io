---
layout: default
title: "Specification Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Specification programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/specification/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Specification</li></ol>
</nav>

# Specification

*DDD / behavioral decision* — **Turn a business eligibility rule into a reusable yes/no question.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

A partner can be replicated only when it is active, not marked for deletion and has a permitted target organization. The same check is needed before inbound processing, in a RAP validation and in a background reconciliation job.

## Classes and responsibilities

- ZIF_BP_SPECIFICATION — IS_SATISFIED_BY(candidate) returns ABAP_BOOL.
- ZCL_BP_ACTIVE_SPEC / ZCL_BP_ORG_SPEC — implement single predicates.
- ZCL_BP_AND_SPEC — composes two specifications without side effects.
- ZCL_BP_PROCESSOR — decides how to handle a failed predicate.

## Apply it in four steps

1. Normalize the business candidate before evaluation.
2. Evaluate pure, named predicates with no persistence or remote calls.
3. Compose AND/OR rules only when independent rules must genuinely be reused.
4. Keep error-message construction outside the predicate unless you deliberately adopt a richer result object.

## Illustrative implementation

```abap
INTERFACE zif_bp_specification PUBLIC.
  METHODS is_satisfied_by
    IMPORTING is_partner TYPE zbp_s_candidate
    RETURNING VALUE(rv_match) TYPE abap_bool.
ENDINTERFACE.

"Inside ZCL_BP_ACTIVE_SPEC (illustrative)
METHOD zif_bp_specification~is_satisfied_by.
  rv_match = xsdbool(
    is_partner-active = abap_true
    AND is_partner-deleted = abap_false ).
ENDMETHOD.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Specification | Entry: normalized BP candidate | Interface: ZIF_BP_SPECIFICATION~IS_SATISFIED_BY | Side effects: none | Result: eligible/ineligible | Caller owns rejection message.

**Where it fits:** ABAP: delegate to a class that can be tested by ABAP Unit. RAP: use the predicate from a validation or feature-control implementation, but report failure through RAP's own structures. CAP: invoke an equivalent pure function in a before handler.

**Where it fails:** Avoid Specification when the 'rule' is actually an ordered update workflow. Use Command or a domain service for execution.

## Acceptance tests

- [ ] Two identical candidates return identical answers.
- [ ] Changed status and deletion flag are independently covered.
- [ ] AND/OR composition has a truth-table test.
- [ ] No write or network call occurs in the predicate.

## Distinguish it from similar patterns

Specification answers *may this happen?* Strategy answers *how?* Command performs *do it*.

## Sources and constraints

- [Patterns of Enterprise Application Architecture — Martin Fowler](https://martinfowler.com/eaaCatalog/)
- [SAP Clean ABAP — writing testable business rules](https://github.com/SAP/styleguides/blob/main/clean-abap/CleanABAP.md)

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
