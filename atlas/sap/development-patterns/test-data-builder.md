---
layout: default
title: "Test Data Builder Pattern for ABAP, RAP and CAP | Implementation Guide"
description: "Test Data Builder programming pattern with an SAP case, interface/class contract, clear method responsibilities, code sketch, test checks and trade-offs."
permalink: /atlas/sap/development-patterns/test-data-builder/
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
  <ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Test Data Builder</li></ol>
</nav>

# Test Data Builder

*Testing / construction* — **Make tests show the business difference, not 40 fields of fixture setup.**

[← Return to the 153-pattern catalog](/atlas/sap/development-patterns/)

## The situation

Each ABAP Unit test initializes a large synthetic BP record by hand. A changed structure makes unrelated tests fail, and it becomes unclear which field causes the expected rejection.

## Classes and responsibilities

- ZCL_BP_TEST_DATA_BUILDER — creates valid synthetic defaults.
- WITH_ORG / MARK_DELETED — intentional test-specific variations.
- BUILD — produces a fresh independent candidate.
- ABAP Unit test class — asserts business behavior.

## Apply it in four steps

1. Start with one explicitly synthetic valid object.
2. Override only the fields relevant to the test.
3. Build fresh values so tests cannot share hidden state.
4. Keep separate negative builders for invalid-data cases.

## Illustrative implementation

```text
given = ZCL_BP_TEST_DATA_BUILDER=>valid_candidate( )
given-deleted = abap_true

result = specification->is_satisfied_by( given )

assert result = abap_false

Never copy real customer data into public fixtures.
```

`Z*` objects and data types are illustrative placeholders; this is a pattern sketch, not a copy-paste production implementation. Confirm syntax, available released APIs and runtime contracts in your target system.

## Short technical specification

> Pattern: Test Data Builder | Default: valid synthetic object | Overrides: named and minimal | Output: independent value | Sensitive input: prohibited.

**Where it fits:** Use with ABAP Unit and pure policy classes. For RAP, unit-test delegated domain logic separately from behavior pool integration. In CAP, create similarly focused test fixtures for service hooks and contract tests.

**Where it fails:** Avoid an elaborate builder when simple VALUE #( ) initialization is already clear.

## Acceptance tests

- [ ] Two builds do not share mutable data.
- [ ] Default fixture satisfies its documented invariants.
- [ ] One override changes exactly one business condition.
- [ ] Test data contains no real customer or project identifiers.

## Distinguish it from similar patterns

A Builder creates test values. A Fake implements a test dependency. A Stub returns controlled responses.

## Sources and constraints

- [${sourceLabel(u)}](${u})
- [${sourceLabel(u)}](${u})

This independent educational example uses synthetic scenarios and does not claim official SAP endorsement. The page is pending editorial and release-specific review.

[Back to the pattern library](/atlas/sap/development-patterns/)
