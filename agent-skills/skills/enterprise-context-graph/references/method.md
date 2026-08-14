# Enterprise Context Graph Modeling — Detailed Method

## 1. Start from the question, not from SAP product names

A useful graph begins with a decision, dependency, diagnostic, or process question. Product lists are secondary.

Examples of good starting questions:

- What must be true before a sales order can be confirmed?
- Which master-data objects control a procurement process and where can bad data break it?
- How should an inbound customer order move through channel, integration, ERP, availability, and fulfillment layers?
- Which system should own a business decision and which systems merely consume the result?

Write explicit exclusions. A narrow graph with meaningful relationships is more useful than an encyclopedic topic whose edges mean nothing.

## 2. Resolve identity before adding nodes

Search all topic files for the concept and common aliases before creating a new ID.

Treat these as the same identity when they describe the same durable concept:

- a product with a shortened display name and its full product name;
- a process reused by several industry scenarios;
- the same business object appearing in sales, integration, and diagnostics topics.

Treat them as different identities when the distinction changes architecture or reasoning, for example:

- Sales Order versus Sales Order Item;
- Business Partner versus Customer role/context;
- SAP Event Mesh versus a generic business event/message;
- process versus process step;
- application component versus integration interface.

Use `synonym_of` for true aliases when separate term nodes are useful. Do not create parallel canonical IDs merely because two pages use different wording.

## 3. Choose the narrowest useful type

Use the node vocabulary in `schema.yml`. The type should answer what the thing *is*, not where it happens to appear.

Common distinctions:

- `process` / `process_step`: business flow and its steps.
- `business_object`: transactional or semantic business object.
- `master_data_object`: governed reusable master data.
- `rule`: determination, validation, or decision logic.
- `application_component`: application capability or product component.
- `platform_component`: technical platform capability.
- `integration`: interface or integration boundary.
- `message`: API payload, event, IDoc/message concept.
- `failure_mode` and `root_cause`: symptom/failure versus underlying cause.
- `control`, `test_case`, `kpi`: governance and validation mechanisms.
- `expert_heuristic`: reusable diagnostic or design judgment.

If no existing type fits, first ask whether the concept is actually an attribute or explanation rather than a first-class node. Add a node type only when the distinction will be reused.

## 4. Model edges as questions

Every edge should answer a meaningful question. Read it as a sentence:

`A -> relation -> B`

Examples:

- Sales Order `reads` Customer Master.
- Partner Determination `determines` Partner Functions.
- Inbound Order Interface `integrates_with` SAP S/4HANA Sales.
- Missing Sales Area Data `can_cause` Sales Order Creation Failure.
- Sales Order Creation `tested_by` Standard Order Creation Test.

Direction matters. Avoid symmetric-looking edges unless the semantics truly are symmetric.

Prefer explicit edges for important dependencies instead of hiding them inside description fields. Use `rationale` when the relationship is conditional, non-obvious, or architectural rather than directly structural.

## 5. Separate facts from judgment

Use evidence classes deliberately:

- `documented_fact`: externally verifiable and source-backed.
- `professional_experience`: practical observation, only when genuinely supportable.
- `expert_heuristic`: reusable design or diagnostic rule.
- `reasoned_inference`: conclusion derived from facts and assumptions.
- `reasoned_interpretation`: interpretation of documented scope or behavior.
- `synthetic_assumption` / `synthetic_example`: fictional material for learning or evaluation.

Do not use a vendor source to make a heuristic look like a documented product fact. Conversely, do not present a documented prerequisite as mere personal preference.

## 6. Attach sources at the claim boundary

Register sources under `sources/` first. Then attach `source_refs` as close as practical to the entity or relationship being supported.

For time-sensitive claims, capture:

- product/release scope;
- access date;
- verification date;
- relevant limitation or prerequisite.

A topic-level source list is useful for discovery, but it does not replace evidence on material relationships when the graph is meant to support grounded reasoning.

## 7. Add reasoning depth

For lead-level material, a topic should normally contain more than the happy path. Consider modeling:

- determination rules;
- ownership boundaries;
- failure modes and root causes;
- integration boundaries and message semantics;
- controls and tests;
- KPIs and operational consequences;
- architecture trade-offs;
- diagnostic questions and expert heuristics.

Do not force every node type into every topic. Add only what improves the reasoning path.

## 8. Validate before presentation

Run:

```sh
python3 scripts/validate_enterprise_context.py
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_enterprise_context_model.py
```

Fix hard integrity errors before modifying presentation. Warnings should be reviewed, not automatically ignored.

The presentation layer may group, filter, or simplify the graph for a reader, but it must not create a second set of contradictory identities or relationships.

## Common failure patterns

1. **Product catalogue instead of graph.** Many products, few meaningful edges, no decision value.
2. **Duplicate identity.** The same SAP concept receives a new ID in every topic.
3. **Prose-only dependency.** A critical prerequisite appears only in a paragraph, so graph traversal cannot find it.
4. **Everything is a documented fact.** Interpretation and heuristics are incorrectly made to look vendor-certified.
5. **One giant topic.** Sales, procurement, manufacturing, MDG, integration, and AI are placed in one YAML because files are apparently scarce resources.
6. **UI owns semantics.** A page-specific data structure becomes the real ontology and the canonical graph drifts behind it.
7. **Synthetic history presented as experience.** Fictional examples are useful, but they must stay visibly fictional.
