# Enterprise Context Graph Modeling — Templates

These fragments are starting patterns, not a second schema. Always check `_data/labs/enterprise_context/schema.yml` and existing topics before using them.

## Topic skeleton

```yaml
id: TOPIC-<DOMAIN>-<STABLE-NAME>
type: research_topic
title: "<Human title>"
summary: >-
  <What this topic explains and why it matters.>
domain: "<Business / SAP domain>"
process_family: "<Optional process family>"
status: researching
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
verified_at: null

business_question: >-
  <One bounded question the graph must answer.>

scope:
  include:
    - "<included boundary>"
  exclude_for_now:
    - "<explicit exclusion>"

maturity:
  gates_complete: 1
  gates_total: 7
  gates:
    scope: done
    sources: planned
    model: planned
    relationships: planned
    expert_reasoning: planned
    synthetic_example: planned
    ai_evaluation: planned

entities: []
relations: []
source_refs: []
tags:
  - <tag>
```

## Canonical entity pattern

```yaml
- id: OBJ-SD-SALES-ORDER
  type: business_object
  title: "Sales Order"
  summary: >-
    <Short semantic definition, not page marketing copy.>
  status: researching
  source_refs:
    - SRC-<REGISTERED-SOURCE>
```

Only add fields that carry reusable meaning. Topic-specific prose can live elsewhere in the topic without redefining the entity identity.

## Typed relation pattern

```yaml
- from: PROC-O2C-CREATE-SALES-ORDER
  type: creates
  to: OBJ-SD-SALES-ORDER
  evidence_type: documented_fact
  confidence: high
  source_refs:
    - SRC-<REGISTERED-SOURCE>
  rationale: >-
    <Optional explanation when the relation is conditional or not obvious.>
  scope: "<Optional product/release/scenario boundary>"
  status: source_verified
  verified_at: "YYYY-MM-DD"
```

## Failure and root-cause pattern

```yaml
failure_modes:
  - id: FAIL-O2C-ORDER-CREATION
    type: failure_mode
    title: "Sales order cannot be created"
    summary: "<Observable failure, not the presumed cause.>"

root_causes:
  - id: CAUSE-O2C-MISSING-SALES-AREA
    type: root_cause
    title: "Missing customer sales-area data"
    summary: "<Underlying condition.>"

relations:
  - from: CAUSE-O2C-MISSING-SALES-AREA
    type: can_cause
    to: FAIL-O2C-ORDER-CREATION
    evidence_type: expert_heuristic
    confidence: high
    rationale: >-
      <Why this cause should be checked in this failure context.>
```

## Rule / determination pattern

```yaml
rules:
  - id: RULE-SD-PARTNER-DETERMINATION
    type: rule
    title: "Partner Determination"
    summary: "<What decision or derivation this rule controls.>"

relations:
  - from: RULE-SD-PARTNER-DETERMINATION
    type: determines
    to: <TARGET-ID>
    evidence_type: documented_fact
    confidence: high
    source_refs:
      - SRC-<REGISTERED-SOURCE>
```

## Integration pattern

```yaml
integrations:
  - id: INT-O2C-INBOUND-ORDER
    type: integration
    title: "Inbound Sales Order Integration"
    summary: "<Business boundary and responsibility.>"

messages:
  - id: MSG-O2C-CUSTOMER-ORDER
    type: message
    title: "Customer Order Message"
    summary: "<Semantic message/API/event role.>"

relations:
  - from: INT-O2C-INBOUND-ORDER
    type: consumed_via
    to: MSG-O2C-CUSTOMER-ORDER
    evidence_type: reasoned_interpretation
    confidence: medium
    rationale: >-
      <Why this message is modeled as the integration contract.>
```

## Expert heuristic pattern

```yaml
expert_heuristics:
  - id: HEUR-O2C-CHECK-MASTER-DATA-FIRST
    type: expert_heuristic
    title: "Check master-data scope before changing configuration"
    context: "Sales-order creation fails only for one customer/product combination."
    statement: >-
      Verify organizational and master-data completeness before changing determination logic.
    confidence: high
    questions:
      - "Does the customer have the required sales-area data?"
      - "Is the material extended to the relevant sales/plant context?"
    checks:
      - "Compare a working and failing business object at the same organizational scope."
    anti_patterns:
      - "Changing customizing before isolating a master-data difference."
    related_nodes:
      - <RELATED-ID>
```

## Source registry pattern

```yaml
sources:
  - id: SRC-<PUBLISHER>-<STABLE-NAME>
    publisher: <Publisher>
    source_type: official_help
    title: "<Source title>"
    url: "<Public source URL>"
    accessed_at: "YYYY-MM-DD"
    verified_at: "YYYY-MM-DD"
    product_scope: "<Product / release / capability>"
    status: source_verified
```

Store metadata and scope, not copied source prose.
