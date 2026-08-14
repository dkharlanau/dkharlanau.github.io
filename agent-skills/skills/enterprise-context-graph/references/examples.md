# Enterprise Context Graph Modeling — Examples

All examples below are generic or synthetic. They illustrate modeling choices, not project history.

## Good example: Sales-order creation as a dependency graph

Question: What dependencies should be checked before changing configuration when a sales order cannot be created correctly?

Useful entities:

- `PROC-O2C-CREATE-SALES-ORDER` — process step.
- `OBJ-SD-SALES-ORDER` — business object.
- `MD-BP-CUSTOMER` — master-data object.
- `MD-MM-PRODUCT` — master-data object.
- `RULE-SD-PARTNER-DETERMINATION` — rule.
- `FAIL-O2C-ORDER-CREATION` — failure mode.
- `TEST-O2C-STANDARD-ORDER` — test case.

Useful relations:

```yaml
- from: PROC-O2C-CREATE-SALES-ORDER
  type: creates
  to: OBJ-SD-SALES-ORDER
  evidence_type: documented_fact
  confidence: high
  source_refs: [SRC-REGISTERED-O2C-SOURCE]

- from: PROC-O2C-CREATE-SALES-ORDER
  type: reads
  to: MD-BP-CUSTOMER
  evidence_type: reasoned_interpretation
  confidence: high

- from: RULE-SD-PARTNER-DETERMINATION
  type: determines
  to: OBJ-SD-SALES-ORDER
  evidence_type: documented_fact
  confidence: medium
  source_refs: [SRC-REGISTERED-PARTNER-SOURCE]

- from: PROC-O2C-CREATE-SALES-ORDER
  type: can_fail_as
  to: FAIL-O2C-ORDER-CREATION
  evidence_type: expert_heuristic
  confidence: high

- from: PROC-O2C-CREATE-SALES-ORDER
  type: tested_by
  to: TEST-O2C-STANDARD-ORDER
  evidence_type: expert_heuristic
  confidence: high
```

Why this is good: the graph supports process explanation, dependency tracing, diagnosis, and test design. The entities are reusable in later ATP, pricing, integration, and master-data topics.

## Bad example: A sales topic as a product list

```yaml
products:
  - SAP S/4HANA
  - SAP Sales Cloud
  - SAP CPQ
  - SAP Commerce Cloud
  - SAP Integration Suite
```

Why this is weak: it says what products exist but not which system owns which decision, which objects move between them, which process step uses them, or where failures can occur. A slide can survive on such a list. A knowledge graph should demand more from life.

## Good example: Integration boundary instead of protocol soup

Question: How should a customer order move from an external channel to ERP execution?

Model separately:

- order-capture application;
- integration boundary;
- message/API/event contract;
- ERP sales application;
- business object created or updated;
- failure modes such as mapping rejection, duplicate message, or missing master data.

Example relations:

```yaml
- from: APP-COMMERCE-CLOUD
  type: integrates_with
  to: APP-S4HANA-SALES
  evidence_type: documented_fact
  confidence: medium
  source_refs: [SRC-REGISTERED-INTEGRATION-SOURCE]

- from: INT-O2C-INBOUND-ORDER
  type: consumed_via
  to: MSG-O2C-CUSTOMER-ORDER
  evidence_type: reasoned_interpretation
  confidence: medium

- from: FAIL-O2C-MAPPING-REJECTION
  type: impacts
  to: PROC-O2C-CREATE-SALES-ORDER
  evidence_type: expert_heuristic
  confidence: high
```

Why this is good: protocol, business contract, application ownership, and operational failure are separate concepts. They can change independently without renaming everything.

## Bad example: One node per sentence

A topic creates separate nodes named:

- “SAP S/4HANA receives orders”
- “Orders arrive through API”
- “API can fail”
- “Failed API blocks order creation”

Why this is weak: sentences have been mistaken for entities. The durable entities are S/4HANA Sales, the integration, the message/API, the failure mode, and the process. The verbs belong in typed relations.

## Good example: Master-data governance reasoning

Question: Why can a logistics process fail even when the transaction configuration is correct?

Useful graph path:

```text
Master Data Object
  -> governed_by -> Governance Process / Control
  -> replicated_via or integrated_via -> Integration
  -> read_by -> Logistics Process
  -> can_fail_as -> Operational Failure
  -> measured_by -> Data Quality / Process KPI
```

If `replicated_via` is not in the controlled edge vocabulary, do not casually add it because the phrase feels nice. Check whether `integrated_via`, `writes`, `updates`, `triggers`, or another existing edge captures the durable meaning. Extend the vocabulary only when the distinction will be reused.

## Good example: Synthetic automotive JIT scenario

A fictional automotive supplier can be used to instantiate:

- JIT call as a message/business object;
- inbound or outbound JIT process;
- call-control rule;
- production or delivery requirement;
- integration channel;
- sequence or timing constraint;
- failure mode such as invalid call status or missing reference data;
- test cases for duplicate, changed, and cancelled calls.

Mark the enterprise and transactions as synthetic. Product facts can still be separately source-backed.

Why this is useful: the model can show industry reasoning and SAP-specific process structure without exposing any real customer or employer data.

## Identity conflict example

Topic A defines:

```yaml
id: APP-S4HANA-SALES
type: application_component
title: "SAP S/4HANA Sales"
```

Topic B needs the same component but prefers the display label “SD core”.

Good choice: reuse `APP-S4HANA-SALES` and use an alias or topic-specific description.

Bad choice: create `APP-SD-CORE` as a second canonical node unless it truly represents a different semantic component.

The graph becomes useful when repeated concepts connect topics. Duplicating them removes precisely the connectivity we wanted to build.
