---
layout: default
title: "Domain-Driven Design for Acting Systems"
description: "A working DDD framework for systems where people, deterministic software, AI models, and agents can decide, delegate, commit, and learn."
permalink: /ddd/
last_modified_at: 2026-08-15
status: needs_verification
verified: false
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
hide_global_cta: true
ddd_framework: true
---

<div class="ddd-canvas">
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <ol><li><a href="/">Home</a></li><li aria-current="page">DDD for Acting Systems</li></ol>
  </nav>

  <header class="ddd-hero" aria-labelledby="ddd-title">
    <div>
      <p class="ddd-kicker">Working framework · v0.3</p>
      <h1 id="ddd-title">Domain-Driven Design for acting systems.</h1>
      <p class="ddd-hero__lead">DDD protects business meaning. I keep that discipline, but extend it for software that can interpret context, make a choice, delegate work, call a tool, change business state, and learn from the result.</p>
    </div>
    <aside class="ddd-hero__aside" aria-label="Framework thesis">
      <p class="ddd-label">Core proposition</p>
      <strong>Meaning is only the first boundary. Acting systems also need boundaries for decisions, commitments, authority, and learning.</strong>
      <p>My working formula is: Meaning → Decision → Commitment → Evidence → Learning.</p>
      <div class="ddd-machine-links" aria-label="Framework files and tools">
        <a href="/ddd/decision-canvas/">Decision Canvas</a>
        <a href="/ddd/framework.json">framework.json</a>
        <a href="/ddd/decision.schema.json">decision.schema.json</a>
        <a href="/ddd/examples.json">SAP examples</a>
        <a href="/ddd/agent-context.md">agent-context.md</a>
      </div>
    </aside>
  </header>

  <section class="ddd-section" aria-labelledby="ddd-why">
    <div class="ddd-section__head">
      <div><p class="ddd-label">01 · The rethink</p><h2 id="ddd-why">DDD still works. The missing part is the right to make something real.</h2></div>
      <div>
        <p>I do not see AI as a reason to abandon bounded contexts or ubiquitous language. It is almost the opposite. Once a model can read business language and choose an action, a semantic mistake can become an operational mistake.</p>
        <p>The architecture question is no longer only “where does this logic live?” It is also “who may decide, who may commit, what is trusted, and what is allowed to change after we learn from production?”</p>
      </div>
    </div>

    <div class="ddd-note">
      <p>A fluent answer is cheap. A valid business commitment is not. The framework should make the distance between the two explicit.</p>
    </div>

    <div class="ddd-compare" style="margin-top:2.5rem">
      <article><h3>I keep bounded contexts.</h3><p>A model is valid inside a semantic boundary. Sales, Availability, Delivery, Finance, Master Data, and Warehouse Execution may use the same word differently.</p></article>
      <article><h3>I add decision boundaries.</h3><p>An important choice needs an owner, authoritative inputs, invariants, allowed judgment, and an authority rule.</p></article>
      <article><h3>I keep invariants.</h3><p>If a rule must always hold, deterministic logic should protect it. AI may explain the rule, not become the rule.</p></article>
      <article><h3>I add commitment boundaries.</h3><p>A recommendation becomes business reality only when an authorized actor creates a promise, transaction, approval, reservation, or state change.</p></article>
      <article><h3>I keep context maps.</h3><p>Crossing a context still needs a contract and semantic translation. RAG and agent-to-agent calls do not remove that requirement.</p></article>
      <article><h3>I add authority envelopes.</h3><p>Authority has scope, value, frequency, time, approval, and reversibility limits. It belongs to an action, not to an agent personality.</p></article>
      <article><h3>I keep domain events.</h3><p>Events are not only integration messages. They are also temporal memory that tells us what really happened.</p></article>
      <article><h3>I add learning boundaries.</h3><p>Production feedback can propose a change. It should not silently rewrite policy, permissions, prompts, invariants, or autonomy.</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-planes">
    <div class="ddd-section__head">
      <div><p class="ddd-label">02 · Three planes</p><h2 id="ddd-planes">Separate meaning, action, and learning.</h2></div>
      <p>I find this split more useful than putting every new concept into one giant architecture diagram. Each plane answers a different kind of question.</p>
    </div>

    <div class="ddd-system-map" aria-label="Three framework planes">
      <div class="ddd-system-map__node"><p class="ddd-label">Domain Plane</p><strong>What does the business mean?</strong><p>Context, language, capability, ownership, invariant, contract.</p></div>
      <div class="ddd-system-map__node ddd-system-map__node--decision"><p class="ddd-label">Action Plane</p><strong>What may happen?</strong><p>Decision, actor, authority envelope, tool, commitment.</p></div>
      <div class="ddd-system-map__node"><p class="ddd-label">Learning Plane</p><strong>What may change next?</strong><p>Event, evidence, evaluation, change proposal, promotion gate.</p></div>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-units">
    <div class="ddd-section__head">
      <div><p class="ddd-label">03 · Design units</p><h2 id="ddd-units">Eight things I want to see on the map.</h2></div>
      <p>Context is a unit of semantic integrity. Autonomy belongs in the action plane. That distinction matters once software can act.</p>
    </div>

    <div class="ddd-units">
      <article class="ddd-unit"><span class="ddd-unit__number">01</span><div><h3>Context</h3><p>Semantic integrity.</p></div><div><p>A boundary where one domain model and language are coherent.</p><p class="ddd-unit__question">Where is this meaning valid?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">02</span><div><h3>Capability</h3><p>Value ownership.</p></div><div><p>A business ability with an accountable owner and outcome.</p><p class="ddd-unit__question">Who owns this ability?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">03</span><div><h3>Contract</h3><p>Boundary crossing.</p></div><div><p>An explicit interface for facts, events, commands, tools, or delegated tasks.</p><p class="ddd-unit__question">What may cross the boundary?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">04</span><div><h3>Decision</h3><p>Judgment.</p></div><div><p>A choice with evidence, rules, uncertainty, authority, and consequences.</p><p class="ddd-unit__question">What is being decided?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">05</span><div><h3>Commitment</h3><p>Business effect.</p></div><div><p>A durable promise, transaction, approval, reservation, or state change.</p><p class="ddd-unit__question">Who may make the result real?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">06</span><div><h3>Event</h3><p>Temporal memory.</p></div><div><p>A durable statement that something relevant happened.</p><p class="ddd-unit__question">What should remain observable?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">07</span><div><h3>Evidence</h3><p>Trust.</p></div><div><p>Traceable information used to justify or reconstruct a decision and action.</p><p class="ddd-unit__question">Why was this accepted?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">08</span><div><h3>Evaluation</h3><p>Learning.</p></div><div><p>A controlled test of behavior against real domain cases and failure modes.</p><p class="ddd-unit__question">What evidence is enough to change behavior?</p></div></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-decision">
    <div class="ddd-section__head">
      <div><p class="ddd-label">04 · Decision and commitment</p><h2 id="ddd-decision">Do not stop at “the agent decided”.</h2></div>
      <p>An acting system has at least six steps. I want each material decision to make them visible.</p>
    </div>

    <div class="ddd-decision-grid" aria-label="Decision to commitment sequence">
      <div class="ddd-decision-step"><span>01</span><strong>Truth</strong><p>Which business object or system is authoritative for current state?</p></div>
      <div class="ddd-decision-step"><span>02</span><strong>Evidence</strong><p>Which facts, events, documents, and observations may support the choice?</p></div>
      <div class="ddd-decision-step"><span>03</span><strong>Judgment</strong><p>What is deterministic, and where is bounded interpretation useful?</p></div>
      <div class="ddd-decision-step"><span>04</span><strong>Authority</strong><p>Which actor may perform which action inside which limits?</p></div>
      <div class="ddd-decision-step"><span>05</span><strong>Commitment</strong><p>Which command creates the durable business effect?</p></div>
      <div class="ddd-decision-step"><span>06</span><strong>Observation</strong><p>Which event and evidence prove what actually happened?</p></div>
    </div>

    <div class="ddd-note" style="margin-top:2.5rem">
      <p>Recommendation ≠ commitment. Capability ≠ authority. Tool success ≠ valid business state.</p>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-authority">
    <div class="ddd-section__head">
      <div><p class="ddd-label">05 · Authority envelope</p><h2 id="ddd-authority">Autonomy needs shape, not a badge.</h2></div>
      <p>A0 to A4 is useful, but one number is not enough. A material action also needs a narrow authority envelope.</p>
    </div>

    <div class="ddd-compare">
      <article><h3>Scope</h3><p>Which customers, plants, company codes, warehouses, materials, document types, or process variants are in scope?</p></article>
      <article><h3>Value</h3><p>What quantity, financial, margin, credit, or business-impact limit applies?</p></article>
      <article><h3>Frequency</h3><p>How many actions may happen before review or rate control applies?</p></article>
      <article><h3>Time</h3><p>During which period is the authority valid, and when does it expire?</p></article>
      <article><h3>Reversibility</h3><p>Can the result be undone or compensated without creating a second problem?</p></article>
      <article><h3>Approval</h3><p>Which action still needs an explicit human or policy checkpoint?</p></article>
    </div>

    <div class="ddd-note" style="margin-top:2.5rem">
      <p>Delegation may preserve or reduce authority. It must never amplify it. A child agent or remote task cannot receive more business authority than the actor that delegated the work.</p>
    </div>

    <div class="ddd-autonomy" style="margin-top:2.5rem">
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A0</span><strong>Read</strong><p>Retrieve, explain, summarize.</p><small>Human owns decision and action.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A1</span><strong>Recommend</strong><p>Evaluate bounded options and recommend.</p><small>Human chooses and executes.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A2</span><strong>Prepare</strong><p>Prepare a transaction, message, or change without committing it.</p><small>Human reviews and submits.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A3</span><strong>Execute with approval</strong><p>Run one defined action after an explicit approval checkpoint.</p><small>Human approves material commitment.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A4</span><strong>Bounded execution</strong><p>Act without per-action approval inside a narrow authority envelope.</p><small>Only after evaluation earns it.</small></div>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-economics">
    <div class="ddd-section__head">
      <div><p class="ddd-label">06 · Decision economics</p><h2 id="ddd-economics">Not every judgment deserves an agent.</h2></div>
      <p>AI adds uncertainty, latency, cost, evaluation work, and governance. It should earn its place in the process.</p>
    </div>

    <div class="ddd-compare">
      <article><h3>Prefer deterministic</h3><p>Ambiguity is low or a stable rule already gives the right answer.</p></article>
      <article><h3>Advisory AI</h3><p>Error cost is high and the outcome is hard to reverse. AI explains; an authorized actor commits.</p></article>
      <article><h3>Prepare with review</h3><p>Judgment is useful, but a material commitment still needs an explicit review before execution.</p></article>
      <article><h3>Bounded execution candidate</h3><p>Evidence is strong, the action is reversible, and deterministic guardrails are available. Start lower and promote through evaluation.</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-truth">
    <div class="ddd-section__head">
      <div><p class="ddd-label">07 · Truth and time</p><h2 id="ddd-truth">Correct data can still be wrong if it is old.</h2></div>
      <p>Agentic systems make stale truth more dangerous because a model can build a convincing explanation around it. For material actions I want source context and time to be part of the evidence model.</p>
    </div>

    <div class="ddd-memory">
      <article><strong>System of Record</strong><p>Transactional truth. Prefer object identity, state version, and observation time for material decisions.</p><p class="ddd-memory__warning">May authorize current state</p></article>
      <article><strong>Event Memory</strong><p>What happened. Preserve event time, producer context, ordering assumptions, and schema meaning.</p><p class="ddd-memory__warning">Temporal fact</p></article>
      <article><strong>Semantic Memory</strong><p>What may be relevant. Documents, embeddings, knowledge graphs, and retrieved context help interpretation.</p><p class="ddd-memory__warning">Context, not transaction truth</p></article>
      <article><strong>Evidence Store</strong><p>Why the system acted. Sources, approvals, tool results, model output, and outcomes support review.</p><p class="ddd-memory__warning">Trace the decision</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-agents">
    <div class="ddd-section__head">
      <div><p class="ddd-label">08 · Agents and contracts</p><h2 id="ddd-agents">Protocols solve connectivity. They do not solve domain authority.</h2></div>
      <p>MCP can expose tools and resources. A2A can describe agents, tasks, and artifacts. Useful infrastructure still needs a business contract around meaning, authority, commitment, and evidence.</p>
    </div>

    <div class="ddd-artifacts">
      <article class="ddd-artifact"><h3>Data Contract</h3><p>Stable facts or state snapshots with owner, semantics, and version expectations.</p></article>
      <article class="ddd-artifact"><h3>Event Contract</h3><p>A durable business fact with producer context, schema, and time semantics.</p></article>
      <article class="ddd-artifact"><h3>Command / Tool Contract</h3><p>One narrow action with preconditions, authority, effects, failures, and compensation.</p></article>
      <article class="ddd-artifact"><h3>Agent Task Contract</h3><p>A delegated goal with source context, authority envelope, expected artifact, and lifecycle.</p></article>
      <article class="ddd-artifact"><h3>Evidence Contract</h3><p>Provenance and decision evidence that crosses a boundary without pretending to be domain truth.</p></article>
      <article class="ddd-artifact"><h3>Anti-Corruption Rule</h3><p>Translation that protects local language from foreign system, model, or agent semantics.</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-learning">
    <div class="ddd-section__head">
      <div><p class="ddd-label">09 · Learning boundary</p><h2 id="ddd-learning">Learning is a promotion process, not self-editing.</h2></div>
      <p>I want production systems to learn from evidence, but I do not want a production agent to quietly rewrite the rules that control its own behavior.</p>
    </div>

    <div class="ddd-loop" aria-label="Learning promotion flow">
      <div><span>01</span><strong>Observe</strong></div>
      <div><span>02</span><strong>Curate</strong></div>
      <div><span>03</span><strong>Evaluate</strong></div>
      <div><span>04</span><strong>Propose</strong></div>
      <div><span>05</span><strong>Test</strong></div>
      <div><span>06</span><strong>Review</strong></div>
      <div><span>07</span><strong>Promote</strong></div>
      <div><span>08</span><strong>Monitor</strong></div>
    </div>

    <div class="ddd-note" style="margin-top:2.5rem">
      <p>Production evidence may suggest a better prompt, model, retrieval rule, tool schema, authority policy, or even domain model. It does not get to promote that change by itself.</p>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-practical">
    <div class="ddd-section__head">
      <div><p class="ddd-label">10 · Practical layer</p><h2 id="ddd-practical">Turn the framework into a contract.</h2></div>
      <p>Architecture prose is useful for thinking, but it is weak as an interface between people and agents. v0.3 adds a typed Decision Card and an interactive canvas.</p>
    </div>

    <div class="ddd-case">
      <div class="ddd-case__facts">
        <dl>
          <div><dt>Human tool</dt><dd><a href="/ddd/decision-canvas/">Decision Canvas</a></dd></div>
          <div><dt>Machine contract</dt><dd><a href="/ddd/decision.schema.json">decision.schema.json</a></dd></div>
          <div><dt>Reference cases</dt><dd><a href="/ddd/examples.json">examples.json</a></dd></div>
          <div><dt>Agent instructions</dt><dd><a href="/ddd/agent-context.md">agent-context.md</a></dd></div>
        </dl>
      </div>
      <div>
        <h3>Design one decision before designing one agent.</h3>
        <p>The canvas asks for business outcome, bounded context, authoritative truth, freshness, invariants, allowed judgment, decision economics, authority envelope, commitment, evidence, and evaluation cases.</p>
        <p>It produces JSON that follows the Decision Card schema. The goal is not bureaucracy. The goal is to expose missing authority or truth before those gaps become hidden inside orchestration code.</p>
        <div class="ddd-machine-links"><a href="/ddd/decision-canvas/">Open Decision Canvas →</a></div>
      </div>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-cases">
    <div class="ddd-section__head">
      <div><p class="ddd-label">11 · SAP reference cases</p><h2 id="ddd-cases">The same model should survive different domains.</h2></div>
      <p>I use several SAP-heavy cases because they force the framework to deal with different kinds of truth, risk, ownership, and commitment. If the model only works for a chatbot, it is not much of an enterprise model.</p>
    </div>

    <div class="ddd-artifacts">
      <article class="ddd-artifact"><h3>Sales · Delivery risk</h3><p>ATP or aATP remains authoritative. AI can explain risk and prepare a response. Changing the customer promise is a separate commitment.</p></article>
      <article class="ddd-artifact"><h3>Procurement · Source selection</h3><p>AI can rank valid suppliers and explain trade-offs. Creating or releasing a PO remains a purchasing commitment with its own authority.</p></article>
      <article class="ddd-artifact"><h3>Credit · Block response</h3><p>AI can assemble evidence and recommend. Credit exposure, policy, and release authority remain explicit and current.</p></article>
      <article class="ddd-artifact"><h3>Master Data · Change proposal</h3><p>AI can extract and compare candidate values. Activation through governance is the commitment that creates enterprise truth.</p></article>
      <article class="ddd-artifact"><h3>EWM · Warehouse exception</h3><p>AI can classify and rank recovery actions. Current task, HU, and stock state remain authoritative before an execution command.</p></article>
      <article class="ddd-artifact"><h3>Why five cases?</h3><p>Sales tests promises, Procurement tests financial commitment, Credit tests authority, Master Data tests truth creation, and EWM tests fast reversible execution.</p></article>
    </div>

    <div class="ddd-machine-links"><a href="/ddd/examples.json">Open all machine-readable cases →</a></div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-method">
    <div class="ddd-section__head">
      <div><p class="ddd-label">12 · Working method</p><h2 id="ddd-method">Explore → Bound → Contract → Decide → Commit → Observe → Learn.</h2></div>
      <p>The order matters. If the first workshop question is “which agent framework should we use?”, we have skipped the business architecture and moved directly to plumbing.</p>
    </div>

    <div class="ddd-loop" aria-label="Framework lifecycle">
      <div><span>01</span><strong>Explore</strong></div>
      <div><span>02</span><strong>Bound</strong></div>
      <div><span>03</span><strong>Contract</strong></div>
      <div><span>04</span><strong>Decide</strong></div>
      <div><span>05</span><strong>Commit</strong></div>
      <div><span>06</span><strong>Observe</strong></div>
      <div><span>07</span><strong>Learn</strong></div>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-antipatterns">
    <div class="ddd-section__head">
      <div><p class="ddd-label">13 · Anti-patterns</p><h2 id="ddd-antipatterns">Where this usually goes wrong.</h2></div>
      <p>Most failures I worry about are not model failures. They are architecture failures that the model makes easier to hide.</p>
    </div>

    <ul class="ddd-anti">
      <li><strong>Super Agent.</strong> One agent sees every context and receives broad mutation access.</li>
      <li><strong>Capability equals authority.</strong> A discovered tool or remote skill is treated as permission to use it.</li>
      <li><strong>Delegation amplification.</strong> A child task receives more rights than its parent actor.</li>
      <li><strong>Vector Store as Truth.</strong> Retrieved text is treated as current transactional state.</li>
      <li><strong>Stale Truth.</strong> A correct value is used after the business state has already changed.</li>
      <li><strong>LLM Enforces the Invariant.</strong> A probabilistic answer protects a rule that must always hold.</li>
      <li><strong>Prompt as Process.</strong> A critical workflow exists only inside a long system instruction.</li>
      <li><strong>Cross-Context RAG.</strong> Retrieval merges different domain meanings into one friendly-looking text block.</li>
      <li><strong>Self-Learning Policy.</strong> Production feedback directly changes permissions, prompts, autonomy, or business rules.</li>
      <li><strong>Untyped Agent Output.</strong> Architecture prose becomes an automation input without a stable schema.</li>
      <li><strong>AI Before Domain Cleanup.</strong> Weak ownership and poor master data are hidden behind a fluent interface.</li>
    </ul>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-signals">
    <div class="ddd-section__head">
      <div><p class="ddd-label">14 · Signals behind the rethink</p><h2 id="ddd-signals">The technical standards are becoming more explicit. The domain model should do the same.</h2></div>
      <p>This framework is my synthesis, not a wrapper around one protocol. I use current standards as signals for where architecture needs clearer contracts.</p>
    </div>

    <div class="ddd-source-list">
      <a href="https://www.domainlanguage.com/ddd/reference/" rel="noopener"><strong>DDD Reference · Eric Evans</strong><span>The original strategic and tactical vocabulary I keep as the base.</span><i>↗</i></a>
      <a href="https://www.domainlanguage.com/articles/ai-components-deterministic-system/" rel="noopener"><strong>AI Components for a Deterministic System · Eric Evans</strong><span>A useful separation between probabilistic classification and deliberate domain modeling.</span><i>↗</i></a>
      <a href="https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/" rel="noopener"><strong>Context Mapping with an AI-based Component · Eric Evans</strong><span>A current discussion of placing a probabilistic component inside a structured deterministic system.</span><i>↗</i></a>
      <a href="https://modelcontextprotocol.io/specification/draft/server/tools" rel="noopener"><strong>Model Context Protocol</strong><span>Tools and resources are explicit technical capabilities. I keep business authority as a separate domain concern.</span><i>↗</i></a>
      <a href="https://a2a-protocol.org/dev/specification/" rel="noopener"><strong>Agent2Agent Protocol</strong><span>Tasks, artifacts, discovery, and remote execution make delegation a real architecture boundary.</span><i>↗</i></a>
      <a href="https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/" rel="noopener"><strong>OpenTelemetry GenAI semantic conventions</strong><span>Model, retrieval, agent, and tool execution are becoming observable operations.</span><i>↗</i></a>
      <a href="https://json-schema.org/draft/2020-12" rel="noopener"><strong>JSON Schema · Draft 2020-12</strong><span>The Decision Card uses a machine-validatable contract instead of relying only on prose.</span><i>↗</i></a>
      <a href="https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence" rel="noopener"><strong>NIST AI RMF · Generative AI Profile</strong><span>Risk and evaluation belong across the lifecycle, not only at deployment time.</span><i>↗</i></a>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-machine">
    <div class="ddd-machine-panel">
      <div>
        <p class="ddd-label">15 · For agents and tools</p>
        <h2 id="ddd-machine">The machine model is stricter than the prose.</h2>
        <p>The canonical files contain the three planes, design units, decision and commitment boundaries, authority envelopes, decision economics, integration contracts, learning rules, reference cases, and a typed Decision Card schema.</p>
        <div class="ddd-machine-links">
          <a href="/ddd/framework.json">framework.json</a>
          <a href="/ddd/decision.schema.json">decision.schema.json</a>
          <a href="/ddd/examples.json">examples.json</a>
          <a href="/ddd/agent-context.md">agent-context.md</a>
        </div>
        <p class="ddd-status-line">Current repository state: needs_verification · direct grounding only · not yet in global verified retrieval indexes</p>
      </div>
      <pre aria-label="Example framework relation graph">context ──owns──────────▶ capability
capability ─contains────▶ decision
decision ──authorized───▶ authority envelope
decision ──may produce──▶ commitment
commitment ─recorded in─▶ system of record
commitment ─emits────────▶ event
evidence ──feeds─────────▶ evaluation
evaluation ─may support──▶ change proposal
change proposal ──X──────▶ direct policy rewrite</pre>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-close">
    <div class="ddd-section__head">
      <div><p class="ddd-label">16 · Working conclusion</p><h2 id="ddd-close">Design meaning. Design judgment. Design the right to commit.</h2></div>
      <div>
        <p>The part of DDD I value most is the discipline of making business meaning explicit before technical convenience takes over.</p>
        <p>For acting systems I extend the same discipline one step further. Make the decision explicit. Separate it from the commitment. Limit authority. Keep evidence with time and source context. Let production teach us, but make learning pass through a controlled boundary.</p>
        <p>v0.3 adds the practical test: if the decision cannot be expressed as a clear Decision Card, it is probably too early to give an agent authority over it.</p>
      </div>
    </div>
  </section>
</div>
