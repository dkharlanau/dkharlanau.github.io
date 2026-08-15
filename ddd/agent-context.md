# DDD for Acting Systems — agent context

Status: `working-framework`  
Version: `0.3.0`  
Verification: `needs_verification`  
Canonical model: `https://dkharlanau.github.io/ddd/framework.json`  
Decision schema: `https://dkharlanau.github.io/ddd/decision.schema.json`  
Reference cases: `https://dkharlanau.github.io/ddd/examples.json`  
Decision Canvas: `https://dkharlanau.github.io/ddd/decision-canvas/`  
Human-readable page: `https://dkharlanau.github.io/ddd/`

## Role

Use this framework when a business or software domain includes people, deterministic applications, integrations, AI models, agents, delegated tasks, or autonomous actions.

The framework keeps the practical DDD base: domain language, bounded contexts, invariants, context mapping, events, and anti-corruption layers. It adds explicit models for decision, commitment, authority, evidence, time, evaluation, and controlled learning.

It is a personal working synthesis, not an official DDD standard.

## Core formula

**Meaning -> Decision -> Commitment -> Evidence -> Learning**

A bounded context asks: **where is this business meaning valid?**

A decision boundary asks: **what should happen, from which evidence, and which part may use judgment?**

A commitment boundary asks: **who may make the result real and create a durable business effect?**

A learning boundary asks: **what production evidence is strong enough to change future behavior, policy, tools, models, or autonomy?**

Do not collapse these questions into one prompt or one agent.

## Three planes

### Domain Plane

Protect meaning and ownership:

- bounded contexts;
- ubiquitous language;
- capabilities and owners;
- invariants;
- contracts and anti-corruption layers.

### Action Plane

Control judgment and real business effects:

- decisions;
- actors;
- authority envelopes;
- domain tools or commands;
- commitments.

### Learning Plane

Improve behavior without uncontrolled self-modification:

- events;
- evidence;
- evaluations;
- change proposals;
- promotion gates.

## Eight design units

1. **Context — semantic integrity.** Where one model and language are coherent.
2. **Capability — value ownership.** A business ability with an accountable owner and outcome.
3. **Contract — boundary crossing.** What may cross between contexts, systems, or agents.
4. **Decision — judgment.** A choice with inputs, invariants, uncertainty, authority, and consequences.
5. **Commitment — business effect.** A promise, transaction, reservation, approval, or durable state change.
6. **Event — temporal memory.** A durable statement that something relevant happened.
7. **Evidence — trust.** Traceable information that explains or reconstructs a decision and action.
8. **Evaluation — learning.** A controlled test used to decide whether behavior should change.

## Non-negotiable rules

- Start with domain language, business outcome, and ownership. Do not start with agents, microservices, databases, or vendor products.
- Keep deterministic invariants deterministic.
- An AI answer is not a source of record.
- A recommendation is not a commitment.
- A discovered capability is not business authority.
- A tool call is not automatically a valid business action.
- A vector store or knowledge graph is semantic memory, not transactional truth.
- Important evidence should carry source context, observation time, and state version or freshness information when available.
- Place an agent inside the bounded context whose language and decisions it uses. Do not create an `AI context` by default.
- Expose narrow domain tools. Avoid generic mutation access as a business interface.
- Crossing a bounded context requires an explicit contract and semantic translation.
- Delegation must not amplify authority. A child task receives equal or narrower authority than its parent actor.
- Autonomy belongs to a decision and action, not to an agent personality.
- Material commitments need evidence, authority, a transaction path, and a reversal or compensation rule.
- Production feedback may create a change proposal. It must not silently rewrite business policy, permissions, invariants, or autonomy.
- Increase autonomy only after evaluation shows that the action is reliable enough and economically useful.
- If a machine or agent will consume an architecture artifact, prefer a typed machine-readable contract over free prose.

## Analysis procedure

Run the analysis in this order:

1. **Explore** business outcomes, language, events, decisions, and commitments.
2. **Bound** the model into bounded contexts and assign capability ownership.
3. **Contract** relationships between contexts, systems, tools, events, and agent tasks.
4. **Decide** which choices are deterministic, advisory, bounded judgment, or cross-context. Evaluate decision economics.
5. **Commit** by defining who may turn a decision into a durable business effect, through which command, transaction, approval, and compensation path.
6. **Observe** domain events, state versions, execution telemetry, evidence, and exceptions.
7. **Learn** by converting evidence into evaluation cases and controlled change proposals.

## Decision Card

For each important decision produce a Decision Card compatible with:

`https://dkharlanau.github.io/ddd/decision.schema.json`

The interactive reference tool is:

`https://dkharlanau.github.io/ddd/decision-canvas/`

A Decision Card contains:

- `decision_id`;
- business outcome;
- home bounded context;
- decision type;
- authoritative inputs;
- contextual inputs;
- freshness or state-version rule;
- deterministic invariants;
- allowed and forbidden judgment;
- design posture;
- authority envelope and autonomy level;
- commitment owner and command;
- decision economics;
- evidence to retain;
- evaluation cases and promotion gate.

Classify the decision as one of:

- `deterministic-invariant`;
- `bounded-judgment`;
- `advisory`;
- `cross-context`.

Use one of these design postures when useful:

- `prefer-deterministic`;
- `advisory-ai`;
- `prepare-with-review`;
- `bounded-execution-candidate`.

The posture is an architecture heuristic, not a probability score.

## Commitment boundary

A commitment is the point where analysis becomes a business effect.

Examples:

- change a customer promise date;
- reserve inventory;
- release a purchase order;
- approve credit;
- activate master data;
- post a financial document;
- send an externally binding confirmation.

For each commitment record:

- owning bounded context;
- authorized actor;
- preconditions;
- domain command or tool;
- transactional system;
- duplicate or idempotency control when relevant;
- reversal or compensation;
- resulting business event.

Never treat an LLM recommendation, an A2A task result, successful MCP tool discovery, or a technically successful tool call as a commitment by itself.

## Authority envelope

Authority should be explicit and narrow. Record:

- `scope`: objects, customers, plants, company codes, warehouses, process types, or similar domain scope;
- `value`: financial, quantity, or impact limits;
- `frequency`: allowed number or rate of actions;
- `time`: validity window;
- `reversibility`: whether the action is safely reversible or compensatable;
- `approval`: required human or policy gate.

Rules:

- delegation may preserve or reduce authority but never increase it;
- model confidence can affect routing or review but does not grant authority;
- tool availability does not imply permission to use the tool for a material business effect.

## Decision economics

Do not add AI only because a decision contains words.

Evaluate:

- ambiguity;
- decision volume;
- cost of delay;
- cost of error;
- reversibility;
- evidence quality;
- human review cost.

Useful heuristics:

- low ambiguity often means deterministic logic is the better design;
- high error cost plus low reversibility normally means advisory AI and human commitment;
- high ambiguity plus high reversibility can be a good AI-assistance candidate;
- material commitments with weak evidence normally stay in recommendation or preparation mode;
- bounded execution should start lower and earn promotion through evaluation.

## Truth and time

Keep these layers separate:

- **System of Record**: authoritative transactional state. Prefer object identity, state version, and observation time for material decisions.
- **Event Memory**: what happened. Preserve event time, producer context, and schema semantics.
- **Semantic Memory**: documents, embeddings, knowledge graphs, and retrieval candidates that may help interpretation. Preserve source context and source date.
- **Evidence Store**: sources, tool calls, approvals, evaluations, and action outcomes used for review.

Never silently promote semantic memory into transactional truth.

For material commitments, re-read current authoritative state when stale evidence could change the result.

## Integration contract types

Use the right contract for the crossing:

- `data-contract`: stable facts or snapshots;
- `event-contract`: durable business facts with producer context and time semantics;
- `command-tool-contract`: one narrow action with preconditions, authority, and effects;
- `agent-task-contract`: delegated goal with source context, authority envelope, expected artifact, and lifecycle;
- `evidence-contract`: provenance and decision evidence that must remain distinct from domain truth.

Protocol-level capability discovery and transport are infrastructure. Domain authority remains a business concern.

## Agent contract

An agent contract should state at least:

- home bounded context;
- role and business purpose;
- decisions it may support;
- allowed reads;
- allowed tools;
- forbidden actions;
- authority envelope;
- autonomy level;
- delegation rules;
- approval or policy gates;
- evidence requirements;
- escalation route;
- reversal or compensation route;
- evaluation set.

## Learning boundary

Production execution may produce evidence. Evidence may produce a change proposal. A change proposal is not a production change.

Default promotion flow:

`observe -> curate evidence -> add evaluation case -> propose change -> test -> review -> promote -> monitor`

Version and review changes to:

- domain model;
- prompts or system instructions;
- model configuration;
- retrieval policy;
- tool schema;
- authority policy;
- evaluation set.

Runtime behavior must not silently increase autonomy, widen permissions, change deterministic invariants, or turn retrieved text into business policy.

## Reference cases

Use `https://dkharlanau.github.io/ddd/examples.json` for concrete patterns. The current catalog contains:

- Sales delivery-risk response;
- Procurement source-selection exception;
- Credit-block response;
- Material-master change proposal;
- EWM warehouse-exception response.

Use these as analysis shapes, not as product configuration instructions. Preserve each case's distinction between authoritative state, AI judgment, authority, and commitment.

## Expected output

When applying the framework, return these sections when relevant:

1. `domain_scope`
2. `ubiquitous_language`
3. `bounded_contexts`
4. `capabilities`
5. `context_relationships`
6. `decision_map`
7. `commitment_map`
8. `truth_and_time`
9. `agent_contracts`
10. `authority_and_autonomy`
11. `events_and_evidence`
12. `learning_boundary`
13. `anti_patterns_or_risks`
14. `open_questions`

For each material decision, also return a `decision_card` object that validates against `decision.schema.json` whenever enough input is available.

Prefer graph-like facts, explicit owners, source context, and relationships over long generic prose.

## SAP logistics interpretation

Do not treat SAP modules as bounded contexts automatically. Start with business meaning, then map the SAP implementation.

Examples:

- `Customer Order` owns the customer promise while `Availability` owns ATP or aATP meaning.
- `Operational Procurement` owns the purchasing commitment while sourcing evidence may come from several data and supplier contexts.
- `Credit Management` owns credit-release authority even when Sales provides urgency and customer context.
- `Product Master Data` owns activation of approved master data; extracted document text is contextual evidence until validated.
- `Warehouse Execution` owns executable warehouse state; historical exception patterns do not replace current EWM stock, HU, or task state.

Use the reference catalog for full Decision Cards.

## Retrieval policy

This material is currently `needs_verification`. It may be used when a task explicitly points to it, but it should not be treated as externally validated evidence or as an official DDD extension. Do not add it to sitewide verified retrieval indexes until human review promotes it under the repository policy.
