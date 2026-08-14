---
layout: default
title: "SAP Automotive JIT / JIS Lab"
description: "Architecture notes, graph data, fictional scenarios, and agent rules for SAP Automotive JIT and JIS assessment preparation."
permalink: /datasets/automotive-jit/
verified: false
status: needs_verification
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14T17:30:00+00:00
data_catalog_page: true
hide_global_cta: true
---

<div class="dataset-canvas">
  <header class="dataset-canvas__hero" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">Assessment Lab · SAP Automotive</p>
      <h1>JIT is not one interface.<br />It is a controlled physical promise.</h1>
      <p>Use this lab to reason about SAP Automotive JIT and JIS from demand signal to line-side delivery. The focus is not transaction memory. It is the architecture: business identity, call structure, status and action control, sequence, supplier forwarding, physical execution, integration, recovery, and clean extensions.</p>
      <div class="dataset-canvas__actions">
        <a class="dataset-canvas__button" href="/datasets/automotive-jit/manifest.json">Open machine manifest <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
        <a class="dataset-canvas__text-link" href="/datasets/">All datasets <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="dataset-canvas__inventory" aria-label="JIT lab inventory">
      <div><dt>4</dt><dd>Core artifacts</dd><small>Model, graph, scenarios, agent rules</small></div>
      <div><dt>6</dt><dd>Training scenarios</dd><small>JIS, summarized JIT, Tier-2, exceptions</small></div>
      <div><dt>2</dt><dd>SAP generations</dd><small>Classic and Next Generation JIT</small></div>
    </dl>
  </header>

  <section class="dataset-canvas__access" data-reveal aria-label="Core mental model">
    <div>
      <p class="dataset-canvas__eyebrow">The mental model</p>
      <h2>Follow the state, then follow the material.</h2>
      <p>A good JIT design answers five questions in order: what signal arrived, what SAP object represents it, what controls the next action, what changed physically, and how recovery works if the chain breaks.</p>
    </div>
    <nav aria-label="JIT process chain">
      <a href="#inbound"><span>01</span><strong>Receive</strong><small>Identity, partner, type, destination</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#control"><span>02</span><strong>Control</strong><small>Status + action, not status decoration</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#execute"><span>03</span><strong>Execute</strong><small>Produce, pack, deliver, transport</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#recover"><span>04</span><strong>Recover</strong><small>Reconcile logical and physical state</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </nav>
  </section>

  <section class="dataset-canvas__collections" data-reveal>
    <header>
      <p class="dataset-canvas__eyebrow">Machine-readable layer</p>
      <h2>Four artifacts, four jobs.</h2>
      <p>The files are small enough for direct retrieval and structured enough for graph or agent workflows. They contain no client names or proprietary project data.</p>
    </header>
    <div class="dataset-route-list">
      <a href="/datasets/automotive-jit/domain-model.json"><span>01</span><strong>Domain model</strong><small>Classic JIT vs Next Generation JIT, objects, terminology, decisions, design principles, and classic transaction orientation.</small><em>JSON</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/datasets/automotive-jit/knowledge-graph.json"><span>02</span><strong>Knowledge graph</strong><small>Actors, calls, master data, messages, controls, failure modes, KPIs, extension points, and typed edges.</small><em>JSON</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>03</span><strong>Scenario pack</strong><small>Fictional OEM, Tier-1, and Tier-2 flows with JIS, summarized JIT, forwarding, resequencing, duplicates, and master-data failures.</small><em>JSON</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/datasets/automotive-jit/agent-rules.json"><span>04</span><strong>Agent rules</strong><small>Architecture review algorithm, specification gates, incident reasoning, extension strategy, and Lead-level questions.</small><em>JSON</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section id="inbound" class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">01 · Inbound</p>
      <h2>First decide what kind of promise the customer is making you keep.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p><strong>Summarized JIT:</strong> mainly date + quantity. It is short-horizon execution demand, but it does not require a vehicle production sequence.</p>
      <p><strong>Sequenced JIT / JIS:</strong> the demand is tied to an order or vehicle context and the sequence matters. A sequence error is therefore not only a document error. It can put the wrong physical component at the line.</p>
      <p><strong>Classic SAP Automotive:</strong> think JIT Inbound with call header → component groups → call components. The component group is central for processing control.</p>
      <p><strong>Next Generation JIT:</strong> think Supply to Customer (S2C) and Supply to Production (S2P), with newer Fiori applications, released extensibility, and stronger E2E integration into handling units, EWM, TM, and modern service interfaces.</p>
    </div>
  </section>

  <section id="control" class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">02 · Call Control</p>
      <h2>A status without an action model is just a coloured label.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p>Classic JIT Call Control is best understood as a state/action engine. A processing status allows or triggers an action; successful action execution moves the component group into a new processing status.</p>
      <p>For a Lead design, separate <strong>external production status</strong> from <strong>internal execution status</strong>. The OEM can tell you that a vehicle reached a production point. That does not automatically mean your material is produced, packed, loaded, or safe to resequence.</p>
      <p>A useful state model always defines duplicate behavior, change/cancel behavior, automatic versus manual transitions, partial-action recovery, and the point where the call becomes delivery-relevant.</p>
    </div>
  </section>

  <section id="execute" class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">03 · Physical execution</p>
      <h2>The database is not the factory.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p>For JIS, follow the chain through production or staging, sequence-controlled packing, handling units, delivery, warehouse execution, loading, transportation, goods issue, and customer confirmation.</p>
      <p>The later the physical process has moved, the more dangerous a simple electronic update becomes. Before production, resequencing may be cheap. After packing it can require HU reconciliation. After loading or shipping, silent resequencing is usually the wrong idea; the process needs an exception path.</p>
      <p>This is also why EWM and TM matter in current S/4HANA JIS designs. The JIT call cannot be treated as an isolated LE object when warehouse and transportation execution already carry the physical truth.</p>
    </div>
  </section>

  <section class="dataset-canvas__collections" data-reveal>
    <header>
      <p class="dataset-canvas__eyebrow">Tier-1 → Tier-2</p>
      <h2>Forward the requirement, not your confusion.</h2>
      <p>A system supplier often has to convert an OEM call into supplier demand. The mapping is not a blind copy because Tier-1 still needs time to produce, assemble, pack, and transport.</p>
    </header>
    <div class="dataset-route-list">
      <a href="/datasets/automotive-jit/scenarios.json"><span>A</span><strong>Preserve traceability</strong><small>Keep stable OEM business references while defining the Tier-2 business key explicitly.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>B</span><strong>Transform time</strong><small>Tier-2 required time normally needs lead-time logic; copying the OEM line-arrival time is not a design.</small><em>Scheduling</em><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>C</span><strong>Propagate change safely</strong><small>Define what happens when OEM resequences or cancels after the supplier call is already in flight.</small><em>Control</em><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
    </div>
  </section>

  <section id="recover" class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">04 · Integration & recovery</p>
      <h2>Exactly-once business effect matters more than a green message monitor.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p>Classic Automotive JIT commonly uses EDI through IDoc. Current Next Generation JIT also provides modern service patterns; SAP documents the SOAP service <code>JITCallRequest_In</code> for inbound customer JIT calls in S/4HANA Cloud scenarios.</p>
      <p>Transport retries can create duplicates even when every technical component behaves correctly. The business contract therefore needs stable identity, version/change logic, idempotent actions, correlation, ordering expectations, and safe reprocessing.</p>
      <p>Before reprocessing a failed call, check downstream side effects: supplier call, delivery, HU, goods movement, transportation object, and confirmation. Reprocessing first and investigating later is how one incident applies for a management position.</p>
    </div>
  </section>

  <section class="dataset-canvas__collections" data-reveal>
    <header>
      <p class="dataset-canvas__eyebrow">Extensibility</p>
      <h2>Keep custom logic close to the decision it owns.</h2>
      <p>Start with configuration. Then use released key-user/developer extensibility or BAdIs. Keep protocol conversion in the integration layer and keep the JIT business lifecycle inside the domain unless there is a strong reason to split it.</p>
    </header>
    <div class="dataset-route-list">
      <a href="/datasets/automotive-jit/knowledge-graph.json"><span>01</span><strong>BADI_NJIT_COMPONENT_GRP_DET</strong><small>Example Next Generation extension for component-group determination.</small><em>Determination</em><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="/datasets/automotive-jit/knowledge-graph.json"><span>02</span><strong>BADI_NJIT_CREATE_HU_SEQJC</strong><small>Example extension to influence HU creation for sequenced JIT calls.</small><em>Execution</em><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/datasets/automotive-jit/knowledge-graph.json"><span>03</span><strong>NJIT_CALL_CMAT_S2P</strong><small>Custom Fields and Logic context at S2P JIT call component-material level.</small><em>Clean core</em><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
    </div>
    <p><strong>Release rule:</strong> every extension object must be verified against the exact S/4HANA product, deployment model, and release before it enters a real specification.</p>
  </section>

  <section class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">Assessment lens</p>
      <h2>What a Lead answer should sound like.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p><strong>Weak:</strong> “JIT comes by IDoc, then we use JITM and create delivery.”</p>
      <p><strong>Better:</strong> “First I separate forecast from execution demand and identify summarized versus sequenced call. Then I define call identity, partner/destination/component determination, external-to-internal state mapping, Call Control actions, delivery relevance, physical sequence cut-offs, downstream Tier-2 propagation, and safe recovery. Only after that do I choose the interface and extension technology for the target S/4HANA release.”</p>
      <p>The second answer is longer because factories have stubbornly refused to become dropdown menus.</p>
    </div>
  </section>

  <section class="dataset-canvas__collections" data-reveal>
    <header>
      <p class="dataset-canvas__eyebrow">Fictional training company</p>
      <h2>FalkenWerk → MainLink → ElbeTrim</h2>
      <p>The scenarios use a fictional German automotive chain so requirements and incidents can be discussed like a real project without publishing real customer information.</p>
    </header>
    <div class="dataset-route-list">
      <a href="/datasets/automotive-jit/scenarios.json"><span>01</span><strong>Inbound JIS</strong><small>Vehicle V000471 needs a configured door module in production sequence.</small><em>OEM → Tier-1</em><i class="material-symbols-outlined" aria-hidden="true">directions_car</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>02</span><strong>Forwarded JIS</strong><small>Tier-1 derives beige trim and premium speaker demand for the Tier-2 supplier.</small><em>Tier-1 → Tier-2</em><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>03</span><strong>Late resequence</strong><small>OEM changes sequence after packing has started. Logical and physical truth must be reconciled.</small><em>Exception</em><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="/datasets/automotive-jit/scenarios.json"><span>04</span><strong>Duplicate retry</strong><small>Network retry sends the same business call twice. Business idempotency prevents double demand.</small><em>Integration</em><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
    </div>
  </section>

  <section class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">Terminology guardrail</p>
      <h2>JIS is canonical here. “JIC” needs a project definition.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p>SAP documentation consistently uses <strong>JIS / Just-In-Sequence</strong> for sequence-specific JIT processing. This lab does not treat <strong>JIC</strong> as a standard SAP Automotive term. If a project uses JIC as local shorthand, define it in the project glossary before mapping it to SAP objects or processes.</p>
      <p>This small rule matters for AI use. Acronyms are cheap; wrong architecture built on a guessed acronym is less cheap.</p>
    </div>
  </section>

  <section class="dataset-canvas__citation" data-reveal>
    <div>
      <p class="dataset-canvas__eyebrow">Source boundary</p>
      <h2>Grounded in SAP documentation, still awaiting human review.</h2>
    </div>
    <div class="dataset-canvas__citation-copy">
      <p>Core facts are based on SAP Help documentation for classic JIT Inbound/Outbound and SAP S/4HANA 2025 FPS01 / current Cloud documentation for Next Generation JIT, JIS integration, APIs, and extensibility.</p>
      <p>The architecture comments, fictional examples, failure models, and assessment framing are synthesis. They are intentionally separated from client-specific experience and should be adapted to the actual project release and partner contract.</p>
      <p><strong>Status:</strong> review candidate. This page stays noindex until it is reviewed under the repository verification policy.</p>
    </div>
  </section>
</div>
