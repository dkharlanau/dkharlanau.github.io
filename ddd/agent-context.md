# DDD for Acting Systems — agent context

Status: `working-framework`  
Verification: `needs_verification`  
Canonical model: `https://dkharlanau.github.io/ddd/framework.json`  
Human-readable page: `https://dkharlanau.github.io/ddd/`

## Role

Use this framework when you need to structure a business or software domain that includes deterministic applications, integrations, people, AI models, or agents.

The framework extends practical Domain-Driven Design with explicit decision, evidence, memory, tool, and autonomy boundaries. It is a personal working synthesis, not an official DDD standard.

## Core idea

A bounded context answers: **where is this business meaning valid?**

A decision boundary adds: **who may decide, from which evidence, under which rules, and how far may the action go?**

Treat both as first-class architecture.

## Six design units

1. **Context — unit of autonomy.** A semantic boundary where one model and language are coherent.
2. **Capability — unit of ownership.** A business ability with an accountable owner and outcome.
3. **Contract — unit of integration.** An explicit interface for intent or facts crossing a boundary.
4. **Decision — unit of intelligence.** A business choice with inputs, invariants, judgment, authority, and risk.
5. **Event — unit of memory.** A durable statement that something relevant happened.
6. **Evidence — unit of trust.** Traceable information that justifies or reconstructs a decision and action.

## Non-negotiable rules

- Start with domain language and ownership, not microservices, agents, databases, or vendor products.
- Keep deterministic invariants deterministic.
- An AI answer is not a source of record.
- A vector store or knowledge graph is semantic memory, not transactional truth.
- Place an agent inside the bounded context whose language and decisions it uses. Do not create an `AI context` by default.
- Expose narrow domain tools. Avoid generic mutation access as a business interface.
- Crossing a bounded context requires an explicit contract and semantic translation.
- Autonomy must be explicit. Use A0 to A4 from the canonical model.
- Material actions need evidence, a clear approval or policy basis, and a reversal or compensation path.
- Increase autonomy only after evaluation against representative domain cases and known failure cases.

## Analysis procedure

Run the analysis in this order:

1. **Explore** the business outcome, language, events, problems, and important decisions.
2. **Bound** the model into bounded contexts and assign capability ownership.
3. **Contract** the relationships between contexts, systems, and tools.
4. **Decide** which decisions are deterministic, advisory, bounded judgment, or cross-context.
5. **Act** by defining allowed actors, tools, approvals, autonomy, and reversible operations.
6. **Observe** domain events, execution telemetry, evidence, and exception routes.
7. **Learn** by converting failures into evaluation cases, policy changes, and domain-model feedback.

## Decision classification

For each important decision, classify it as one of:

- `deterministic-invariant`: a rule that must always hold;
- `bounded-judgment`: several valid options exist and AI may rank or propose inside constraints;
- `advisory`: AI may interpret or recommend but does not hold final authority;
- `cross-context`: the decision depends on facts or commitments owned by multiple contexts.

Then record:

- domain owner;
- authoritative inputs;
- contextual inputs;
- invariants;
- allowed judgment;
- actor and autonomy level;
- approval rule;
- permitted actions;
- reversal or compensation;
- evidence to retain;
- evaluation cases.

## Truth and memory

Keep these layers separate:

- **System of Record**: authoritative transactional state.
- **Event Memory**: what happened, with defined semantics and time.
- **Semantic Memory**: documents, embeddings, knowledge graphs, and retrieval candidates that may help interpretation.
- **Evidence Store**: sources, tool calls, approvals, evaluation results, and action outcomes used for review.

Never silently promote semantic memory into transactional truth.

## Agent contract

An agent contract should state at least:

- bounded context;
- role and business purpose;
- allowed reads;
- allowed tools;
- forbidden actions;
- decisions it may support;
- autonomy level;
- approval or policy gates;
- evidence requirements;
- escalation route;
- reversal or compensation route;
- evaluation set.

## Expected output

When applying the framework, return these sections when relevant:

1. `domain_scope`
2. `ubiquitous_language`
3. `bounded_contexts`
4. `capabilities`
5. `context_relationships`
6. `decision_map`
7. `truth_and_memory`
8. `agent_contracts`
9. `autonomy`
10. `events_and_evidence`
11. `anti_patterns_or_risks`
12. `open_questions`

Prefer graph-like facts and explicit relationships over long generic prose.

## SAP logistics interpretation

For SAP-heavy domains, separate business meaning from the SAP implementation while still naming the system truth precisely.

Example: in Order Fulfillment, a sales order, ATP/aATP result, delivery state, master data, and business events can be authoritative inputs. An AI agent may explain delivery risk or rank valid alternatives, but it must not invent availability or override a deterministic ATP result. A material promise change remains subject to the defined business authority and autonomy policy.

Use the `sap_example` object in `framework.json` as the reference shape.

## Retrieval policy

This material is currently `needs_verification`. It may be used when a task explicitly points to it, but it should not be treated as externally validated evidence or as an official DDD extension. Do not add it to sitewide verified retrieval indexes until human review promotes it under the repository policy.
