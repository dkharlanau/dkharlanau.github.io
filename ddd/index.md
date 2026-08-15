---
layout: default
title: "Domain-Driven Design for Acting Systems"
description: "A working Domain-Driven Design framework for systems where people, deterministic software, AI models, and agents can all make or execute decisions."
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
      <p class="ddd-kicker">Working framework · v0.1</p>
      <h1 id="ddd-title">Domain-Driven Design for acting systems.</h1>
      <p class="ddd-hero__lead">DDD gives us a strong way to protect business meaning. I want to keep that. But once software can retrieve context, make a recommendation, call a tool, and change a real business object, the old architecture picture is missing one important boundary: the right to decide.</p>
    </div>
    <aside class="ddd-hero__aside" aria-label="Framework thesis">
      <p class="ddd-label">Core proposition</p>
      <strong>Domain boundaries are no longer enough. We also need decision boundaries.</strong>
      <p>A context says where meaning is valid. A decision boundary says who may decide, from which evidence, under which rules, and how far the action may go.</p>
      <div class="ddd-machine-links" aria-label="Machine-readable framework files">
        <a href="/ddd/framework.json">framework.json</a>
        <a href="/ddd/agent-context.md">agent-context.md</a>
      </div>
    </aside>
  </header>

  <section class="ddd-section" aria-labelledby="ddd-why">
    <div class="ddd-section__head">
      <div><p class="ddd-label">01 · Why rethink it</p><h2 id="ddd-why">DDD still works. The actors changed.</h2></div>
      <div>
        <p>I do not think AI makes Domain-Driven Design obsolete. I think it makes the strategic part more important. A model can now be used not only by developers and services, but by models and agents that interpret language, retrieve documents, choose tools, and sometimes act.</p>
      </div>
    </div>

    <div class="ddd-note">
      <p>The problem is no longer only “where should this logic live?” It is also “what is allowed to make this decision, what can it trust, and what can it change?”</p>
    </div>

    <div class="ddd-compare" style="margin-top:2.5rem">
      <article><h3>I keep ubiquitous language.</h3><p>Humans, code, events, prompts, and tools should use the same domain terms inside one bounded context. Language drift becomes behavior drift when an agent is involved.</p></article>
      <article><h3>I add an evidence model.</h3><p>A retrieved paragraph, an event, and the current SAP document are not equal. Architecture should say which source is authoritative and which source is only context.</p></article>
      <article><h3>I keep bounded contexts.</h3><p>The same word may have different meaning in Sales, Logistics, Finance, or Master Data. That is still normal. Translation across the boundary must stay explicit.</p></article>
      <article><h3>I add decision boundaries.</h3><p>For each important decision, define authority, invariants, allowed judgment, autonomy, approval, evidence, and a reversal or compensation path.</p></article>
      <article><h3>I keep aggregates and invariants.</h3><p>If a rule must always hold, it should remain deterministic. An LLM may explain the rule, but it should not become the rule.</p></article>
      <article><h3>I add agent contracts.</h3><p>An agent needs a role inside the domain, allowed tools, readable data, forbidden actions, autonomy level, escalation, and evaluation cases.</p></article>
      <article><h3>I keep context maps and anti-corruption layers.</h3><p>External models still need translation before they enter the local model. Now “external” can also mean generated or retrieved AI context.</p></article>
      <article><h3>I add observable autonomy.</h3><p>Tool calls, approvals, decision inputs, and outcomes should leave evidence. A system that can act but cannot explain its operating trail is hard to govern.</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-units">
    <div class="ddd-section__head">
      <div><p class="ddd-label">02 · Design units</p><h2 id="ddd-units">Six things I want to see on the map.</h2></div>
      <p>Traditional diagrams often jump from business capabilities to services and databases. I would stop in the middle and model the pieces that control meaning, decision, memory, and trust.</p>
    </div>

    <div class="ddd-units">
      <article class="ddd-unit"><span class="ddd-unit__number">01</span><div><h3>Context</h3><p>Unit of autonomy.</p></div><div><p>A semantic boundary where one domain model and language are coherent.</p><p class="ddd-unit__question">Question: inside which boundary can this meaning stay valid?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">02</span><div><h3>Capability</h3><p>Unit of ownership.</p></div><div><p>A business ability with an accountable owner and a stable outcome.</p><p class="ddd-unit__question">Question: who owns this ability and its result?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">03</span><div><h3>Contract</h3><p>Unit of integration.</p></div><div><p>The explicit interface through which contexts, systems, or agents exchange intent and facts.</p><p class="ddd-unit__question">Question: what may cross the boundary without leaking internal semantics?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">04</span><div><h3>Decision</h3><p>Unit of intelligence.</p></div><div><p>A business choice with inputs, rules, judgment, authority, outcome, and risk.</p><p class="ddd-unit__question">Question: what must be decided, and which part may be probabilistic?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">05</span><div><h3>Event</h3><p>Unit of memory.</p></div><div><p>A durable statement that something relevant happened in the domain.</p><p class="ddd-unit__question">Question: which fact should remain observable after the action?</p></div></article>
      <article class="ddd-unit"><span class="ddd-unit__number">06</span><div><h3>Evidence</h3><p>Unit of trust.</p></div><div><p>Traceable information used to justify, review, or reconstruct a decision and action.</p><p class="ddd-unit__question">Question: what proves why this result was accepted?</p></div></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-decision">
    <div class="ddd-section__head">
      <div><p class="ddd-label">03 · Decision boundary</p><h2 id="ddd-decision">Put a boundary around the judgment, not only around the data.</h2></div>
      <p>I would model every important business decision as a small contract. It should be possible to point at the decision and answer five basic questions without opening a prompt, a workflow, and six source files.</p>
    </div>

    <div class="ddd-decision-grid" aria-label="Decision boundary sequence">
      <div class="ddd-decision-step"><span>01</span><strong>Truth</strong><p>Which system or domain object is authoritative for the current state?</p></div>
      <div class="ddd-decision-step"><span>02</span><strong>Evidence</strong><p>Which facts, events, documents, and observations may support the decision?</p></div>
      <div class="ddd-decision-step"><span>03</span><strong>Judgment</strong><p>Which part is deterministic, and where is bounded interpretation acceptable?</p></div>
      <div class="ddd-decision-step"><span>04</span><strong>Action</strong><p>Who may act, through which domain tool, with which approval or policy?</p></div>
      <div class="ddd-decision-step"><span>05</span><strong>Observation</strong><p>What event and evidence show what actually happened after the action?</p></div>
    </div>

    <div class="ddd-note" style="margin-top:2.5rem">
      <p>My default split is simple: deterministic software protects invariants; AI handles bounded interpretation; policy and people control material authority.</p>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-agent">
    <div class="ddd-section__head">
      <div><p class="ddd-label">04 · Agent placement</p><h2 id="ddd-agent">An agent is a domain actor, not a new domain by default.</h2></div>
      <p>I would not create an “AI bounded context” just because an LLM exists. If an agent talks about order fulfillment, reads order data, and proposes fulfillment actions, it belongs inside that business context and must use its language and contracts.</p>
    </div>

    <div class="ddd-system-map" aria-label="Agent placement inside a domain context">
      <div class="ddd-system-map__node"><p class="ddd-label">Business context</p><strong>Bounded context</strong><p>Owns language, capabilities, invariants, and business meaning.</p></div>
      <div class="ddd-system-map__node ddd-system-map__node--decision"><p class="ddd-label">Control</p><strong>Decision contract</strong><p>Separates authoritative inputs, deterministic rules, allowed judgment, and approval.</p></div>
      <div class="ddd-system-map__node"><p class="ddd-label">Actors</p><strong>Human · service · agent</strong><p>Different actors may support the same decision, but each receives explicit authority.</p></div>
      <div class="ddd-system-map__node"><p class="ddd-label">Execution</p><strong>Domain tools</strong><p>Narrow operations call systems of record. Generic “do anything” access is not a domain contract.</p></div>
    </div>

    <p style="max-width:48rem;margin-top:1.75rem">Crossing a bounded context should feel like crossing it with any other integration: name the contract, preserve the source context, and translate meaning. RAG does not cancel context mapping. It can actually make semantic mixing easier because everything arrives as apparently friendly text.</p>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-autonomy">
    <div class="ddd-section__head">
      <div><p class="ddd-label">05 · Autonomy</p><h2 id="ddd-autonomy">Autonomy should be a domain setting.</h2></div>
      <p>“The agent can use tools” is not an operating model. I prefer a small ladder that can be attached to each agent and, more importantly, to each decision or action.</p>
    </div>

    <div class="ddd-autonomy">
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A0</span><strong>Read</strong><p>Retrieve, explain, summarize.</p><small>Human owns every decision and action.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A1</span><strong>Recommend</strong><p>Evaluate bounded options and recommend.</p><small>Human chooses and executes.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A2</span><strong>Prepare</strong><p>Prepare a transaction, message, or change without committing it.</p><small>Human reviews and submits.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A3</span><strong>Execute with approval</strong><p>Run a defined action after an explicit approval checkpoint.</p><small>Human approves material action.</small></div>
      <div class="ddd-autonomy__row"><span class="ddd-autonomy__level">A4</span><strong>Bounded execution</strong><p>Act inside narrow value, time, scope, and policy limits.</p><small>Use for low-risk, observable, preferably reversible work.</small></div>
    </div>

    <p style="max-width:48rem;margin-top:1.75rem">The level is not a badge for the whole agent. One agent may be A0 for pricing rules, A1 for delivery alternatives, and A3 for sending a low-risk notification. Authority belongs to the decision and action, not to the personality of the bot.</p>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-memory">
    <div class="ddd-section__head">
      <div><p class="ddd-label">06 · Truth and memory</p><h2 id="ddd-memory">Do not put every kind of knowledge in one bucket.</h2></div>
      <p>AI architecture often uses the word “memory” too freely. For enterprise systems I want four layers because they answer different questions and carry very different authority.</p>
    </div>

    <div class="ddd-memory">
      <article><strong>System of Record</strong><p>Transactional truth. The current business object, approved master data, or policy state used for material decisions.</p><p class="ddd-memory__warning">May authorize state</p></article>
      <article><strong>Event Memory</strong><p>What happened. Domain or business events provide time, sequence, and observable facts when their semantics are clear.</p><p class="ddd-memory__warning">Check freshness and meaning</p></article>
      <article><strong>Semantic Memory</strong><p>What may be relevant. Documents, embeddings, vector indexes, and knowledge graphs help retrieval and interpretation.</p><p class="ddd-memory__warning">Never truth by itself</p></article>
      <article><strong>Evidence Store</strong><p>Why the system acted. Sources, tool calls, approvals, evaluation results, and outcomes support review and governance.</p><p class="ddd-memory__warning">Trace, do not invent</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-method">
    <div class="ddd-section__head">
      <div><p class="ddd-label">07 · Method</p><h2 id="ddd-method">A seven-step design loop.</h2></div>
      <p>This is not meant to become another ceremony. It is a sequence for keeping the discussion in the right order. If we start with “which agent framework?” we have already skipped several decisions that matter more.</p>
    </div>

    <div class="ddd-loop" aria-label="Framework lifecycle">
      <div><span>01</span><strong>Explore</strong></div>
      <div><span>02</span><strong>Bound</strong></div>
      <div><span>03</span><strong>Contract</strong></div>
      <div><span>04</span><strong>Decide</strong></div>
      <div><span>05</span><strong>Act</strong></div>
      <div><span>06</span><strong>Observe</strong></div>
      <div><span>07</span><strong>Learn</strong></div>
    </div>

    <div class="ddd-artifacts" style="margin-top:2.5rem">
      <article class="ddd-artifact"><h3>Context Card</h3><p>Scope, language, owners, systems of record, inbound and outbound relationships.</p></article>
      <article class="ddd-artifact"><h3>Capability Map</h3><p>Business abilities, accountable ownership, and the systems that currently support them.</p></article>
      <article class="ddd-artifact"><h3>Decision Map</h3><p>Important choices, invariants, authority, risk, allowed judgment, and autonomy.</p></article>
      <article class="ddd-artifact"><h3>Tool Contract</h3><p>One narrow executable domain operation with preconditions, permissions, effects, and failures.</p></article>
      <article class="ddd-artifact"><h3>Event Contract</h3><p>A stable business fact with owner, schema, version, and consumer expectations.</p></article>
      <article class="ddd-artifact"><h3>Agent Contract</h3><p>Role, context, tools, readable data, forbidden actions, escalation, evidence, and evaluation.</p></article>
      <article class="ddd-artifact"><h3>Trust Policy</h3><p>Source authority, freshness, sensitivity, and what each type of information may be used to decide.</p></article>
      <article class="ddd-artifact"><h3>Evaluation Set</h3><p>Representative domain cases, edge cases, and known failures used before autonomy increases.</p></article>
      <article class="ddd-artifact"><h3>Anti-Corruption Map</h3><p>Where external system semantics or model-generated assumptions must be translated.</p></article>
      <article class="ddd-artifact"><h3>Evidence Record</h3><p>Decision inputs, sources, approvals, tool results, events, and the observed business outcome.</p></article>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-sap">
    <div class="ddd-section__head">
      <div><p class="ddd-label">08 · SAP example</p><h2 id="ddd-sap">Order Fulfillment with a Delivery Risk Advisor.</h2></div>
      <p>SAP logistics is a useful test because the difference between “helpful context” and “business truth” is not theoretical. A plausible explanation cannot create stock, change ATP, or silently become a customer promise.</p>
    </div>

    <div class="ddd-case">
      <div class="ddd-case__facts">
        <dl>
          <div><dt>Bounded context</dt><dd>Order Fulfillment</dd></div>
          <div><dt>Decision</dt><dd>Can we keep the requested delivery promise, and what should we do if risk appears?</dd></div>
          <div><dt>Systems of record</dt><dd>SAP S/4HANA sales order, ATP/aATP result, delivery state, approved master data.</dd></div>
          <div><dt>Agent</dt><dd>Delivery Risk Advisor</dd></div>
          <div><dt>Default autonomy</dt><dd>A1 · Recommend</dd></div>
          <div><dt>Key boundary</dt><dd>AI may explain and rank valid alternatives. It does not override availability truth or business authority.</dd></div>
        </dl>
      </div>

      <div class="ddd-flow">
        <ol>
          <li><span class="ddd-flow__n">01</span><div><strong>Read authoritative state.</strong><p>Resolve the sales order, current availability result, delivery milestones, and approved master data.</p></div></li>
          <li><span class="ddd-flow__n">02</span><div><strong>Detect the risk deterministically where possible.</strong><p>Use valid status, schedule, ATP, interface, and policy signals before asking a model to interpret the situation.</p></div></li>
          <li><span class="ddd-flow__n">03</span><div><strong>Build bounded context.</strong><p>Retrieve only relevant operating knowledge and preserve its source, date, and bounded context.</p></div></li>
          <li><span class="ddd-flow__n">04</span><div><strong>Use AI for judgment, not truth.</strong><p>Explain the trade-off and rank permitted alternatives such as a supported alternative date or plant.</p></div></li>
          <li><span class="ddd-flow__n">05</span><div><strong>Apply authority.</strong><p>A material promise change requires the defined human approval or a narrow policy that explicitly permits bounded execution.</p></div></li>
          <li><span class="ddd-flow__n">06</span><div><strong>Execute through a domain tool.</strong><p>The tool validates authorization, current state, invariants, and transaction result before committing anything.</p></div></li>
          <li><span class="ddd-flow__n">07</span><div><strong>Leave evidence.</strong><p>Record the sources, recommendation, approval or policy, tool result, and resulting event such as <code>PromiseDateChanged</code>.</p></div></li>
        </ol>
      </div>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-anti">
    <div class="ddd-section__head">
      <div><p class="ddd-label">09 · Anti-patterns</p><h2 id="ddd-anti">Things I would stop early.</h2></div>
      <p>Most of these patterns look convenient during a prototype. They become expensive when the system touches real process state, several domains, or regulated decisions.</p>
    </div>

    <ul class="ddd-anti">
      <li><strong>Agent as integration layer.</strong> One general agent translates and coordinates every system instead of using stable contracts.</li>
      <li><strong>Vector store as source of truth.</strong> Retrieved text is treated as current transactional state.</li>
      <li><strong>LLM as invariant engine.</strong> A probabilistic answer is expected to enforce a rule that must always hold.</li>
      <li><strong>Super-agent with access everywhere.</strong> One actor can silently mix semantics and authority across bounded contexts.</li>
      <li><strong>Prompt as undocumented process.</strong> Critical workflow, approval, and policy exist only inside a long instruction.</li>
      <li><strong>Events without ownership.</strong> Technical notifications are published without stable business meaning or schema evolution.</li>
      <li><strong>Cross-context RAG without translation.</strong> Retrieval merges several meanings of the same term and presents them as one truth.</li>
      <li><strong>Autonomy without reversal.</strong> The system can act, but there is no compensation, escalation, or reliable operating trail.</li>
      <li><strong>Agent per microservice.</strong> Technical deployment boundaries are mistaken for domain roles.</li>
      <li><strong>AI before domain cleanup.</strong> Weak ownership, unclear terms, and bad master data are hidden behind a more fluent interface.</li>
    </ul>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-signals">
    <div class="ddd-section__head">
      <div><p class="ddd-label">10 · Signals behind the rethink</p><h2 id="ddd-signals">Standards are moving toward explicit tools, agents, events, and observability.</h2></div>
      <p>This framework is my synthesis, not a wrapper around one standard. Still, several current technical directions make the same architectural pressure visible: agents need bounded tools and resources, agents need interoperable capabilities, events need common structure, and AI execution needs observable traces and risk controls.</p>
    </div>

    <div class="ddd-source-list">
      <a href="https://www.domainlanguage.com/ddd/reference/" rel="noopener"><strong>DDD Reference · Eric Evans</strong><span>The original strategic and tactical vocabulary I am extending, not replacing.</span><i>↗</i></a>
      <a href="https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/" rel="noopener"><strong>Context Mapping with an AI-based Component · Eric Evans</strong><span>A 2026 primary discussion of placing probabilistic AI inside a structured deterministic system.</span><i>↗</i></a>
      <a href="https://modelcontextprotocol.io/specification/2025-11-25/server/index" rel="noopener"><strong>Model Context Protocol</strong><span>Explicit resources, prompts, and executable tools for AI clients. Useful infrastructure, but domain authority still needs its own model.</span><i>↗</i></a>
      <a href="https://a2a-protocol.org/dev/specification/" rel="noopener"><strong>Agent2Agent Protocol</strong><span>Agent discovery, capability communication, and collaborative tasks make agent boundaries an architecture concern rather than a library detail.</span><i>↗</i></a>
      <a href="https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/" rel="noopener"><strong>OpenTelemetry GenAI semantic conventions</strong><span>Agent, retrieval, and tool execution are becoming observable operations with common semantic attributes.</span><i>↗</i></a>
      <a href="https://github.com/cloudevents/spec" rel="noopener"><strong>CloudEvents</strong><span>A vendor-neutral event format reinforces the idea that events need durable metadata and interoperable contracts.</span><i>↗</i></a>
      <a href="https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence" rel="noopener"><strong>NIST AI RMF · Generative AI Profile</strong><span>Risk, evaluation, governance, and trust need to be designed across the AI lifecycle, not added after deployment.</span><i>↗</i></a>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-machine">
    <div class="ddd-machine-panel">
      <div>
        <p class="ddd-label">11 · For agents and tools</p>
        <h2 id="ddd-machine">The prose is not the source model.</h2>
        <p>The canonical machine file contains the framework units, graph relations, autonomy levels, method, anti-patterns, SAP example, source metadata, and an expected agent output structure.</p>
        <div class="ddd-machine-links">
          <a href="/ddd/framework.json">Open framework.json</a>
          <a href="/ddd/agent-context.md">Open agent-context.md</a>
        </div>
        <p class="ddd-status-line">Current repository state: needs_verification · direct grounding only · not yet in global verified retrieval indexes</p>
      </div>
      <pre aria-label="Example framework relation graph">context ──owns────────▶ capability
capability ─contains──▶ decision
decision ──uses───────▶ evidence
decision ──constrained▶ policy
agent ─────acts_inside▶ context
agent ─────invokes────▶ tool
tool ──────implements─▶ contract
semantic memory ─────▶ context only
semantic memory ──X──▶ source of record</pre>
    </div>
  </section>

  <section class="ddd-section" aria-labelledby="ddd-close">
    <div class="ddd-section__head">
      <div><p class="ddd-label">12 · Working conclusion</p><h2 id="ddd-close">Design the right to act.</h2></div>
      <div>
        <p>The part of DDD I value most is not the folder structure or the list of tactical patterns. It is the discipline of making business meaning explicit before technical convenience takes over.</p>
        <p>In systems with agents, I would extend the same discipline to decisions. Name the truth. Name the judgment. Name the actor. Name the boundary. Name the evidence. Then decide how much autonomy is actually useful.</p>
        <p>That is the framework for now. It should evolve through real cases, not through adding more boxes to the diagram.</p>
      </div>
    </div>
  </section>
</div>
