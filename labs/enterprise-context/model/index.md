---
layout: default
title: "Enterprise Context Lab — Model and Authoring Contract"
description: "The authoring contract for adding enterprise process, data, rule, integration, failure, KPI, test, source, and expert-reasoning knowledge to the Enterprise Context Lab."
permalink: /labs/enterprise-context/model/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
---

{% assign lab = site.data.labs.enterprise_context.manifest %}
{% assign schema = site.data.labs.enterprise_context.schema %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Model</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Model / authoring contract</p>
      <h1>One topic in.<br />Reusable context out.</h1>
      <p>This contract defines how a research topic becomes structured enterprise knowledge with stable identifiers, dates, evidence states, typed relationships, expert reasoning, synthetic examples, and AI-evaluation targets.</p>
      <a class="research-canvas__button" href="#topic-lifecycle">Open the topic lifecycle <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Model inventory">
      <p>Schema v{{ schema.version }}</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ schema.node_types | size }}</strong><small>Node types</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ schema.edge_types | size }}</strong><small>Edge types</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ schema.evidence_types | size }}</strong><small>Evidence states</small></div>
      <em>Updated {{ schema.updated_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Author once, project many times.</strong> Structured files are the working contract. Human pages, JSON endpoints, progress views, graph projections, and later AI tools should derive from the same facts instead of maintaining parallel copies.</p>
    <a href="/labs/enterprise-context/data/schema.json">Open schema JSON <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="topic-lifecycle" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Topic lifecycle</p>
      <h2>Seven gates, each with a definition of done.</h2>
      <p>The completion count is derived from explicit gates. A topic that has been read but not modeled and tested remains incomplete.</p>
    </header>
    <div class="research-route-list">
      {% for gate in lab.maturity_gates %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>0{{ gate.order }}</span><strong>{{ gate.label }}</strong><small>{{ gate.done_definition }}</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Core entity families</p>
      <h2>Model the context, not just the document.</h2>
      <p>Stable node types make it possible to ask the same dependency and impact questions across processes, data, integration, operations, and AI evaluation.</p>
    </header>
    <div class="research-route-list">
      {% for node in schema.node_types %}
      <a href="/labs/enterprise-context/data/schema.json"><span>{{ node.prefix }}</span><strong>{{ node.label }}</strong><small>Stable prefix: {{ node.prefix }}</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Relationship vocabulary</p>
      <h2>Every edge should answer a real question.</h2>
      <p>Edges are typed so an AI tool can distinguish containment, dependency, determination, impact, validation, integration, evidence, and test relationships.</p>
    </header>
    <div class="research-route-list">
      {% for edge in schema.edge_types %}
      <a href="/labs/enterprise-context/data/schema.json"><span>→</span><strong>{{ edge }}</strong><small>Typed relationship in schema {{ schema.version }}.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_right_alt</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence and freshness</p>
      <h2>Dates are part of the knowledge model.</h2>
      <p>A relationship that was true for a specific product release three years ago should not silently masquerade as current truth. Verification and source-access dates remain explicit.</p>
    </header>
    <div class="research-route-list">
      {% for evidence in schema.evidence_types %}
      <a href="/labs/enterprise-context/data/schema.json"><span>E</span><strong>{{ evidence }}</strong><small>Evidence type used to separate documentation, expert judgment, inference, synthetic assumptions, and observed examples.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Adding a study topic</p>
      <h2>The minimum topic record.</h2>
      <p>Create one topic record first. Expand stable concepts into reusable graph entities only when the research actually supports them.</p>
    </header>
    <pre><code>id: TOPIC-O2C-SALES-ORDER-CREATION
type: research_topic
title: Order-to-Cash — Sales Order Creation
domain: SAP S/4HANA Logistics
status: researching
created_at: 2026-08-14
updated_at: 2026-08-14
verified_at: null

business_question: &gt;-
  What dependencies are required to create a valid sales order,
  and what should be inspected before recommending a change?

maturity:
  gates_complete: 1
  gates_total: 7
  gates:
    scope: done
    sources: in_progress
    model: planned
    relationships: planned
    expert_reasoning: planned
    synthetic_example: planned
    ai_evaluation: planned

source_refs: []</code></pre>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">When a fact becomes an assertion</p>
      <h2>Separate the relationship from its evidence.</h2>
      <p>The same subject-predicate-object pattern can carry different evidence states without pretending expert judgment is vendor documentation.</p>
    </header>
    <pre><code>subject: OBJ-SD-SALES-ORDER
predicate: references
object: MD-BP-CUSTOMER

evidence_type: documented_fact
source_refs:
  - SRC-...
confidence: high
verified_at: 2026-08-14
scope:
  product: S4HANA
  release: to-be-verified</code></pre>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Expert knowledge</p>
      <h2>Capture how a consultant investigates, not only what the system contains.</h2>
      <p>Heuristics live separately from factual relationships so they can be tested, refined, challenged, and later used as benchmark expectations.</p>
    </header>
    <pre><code>id: HEUR-O2C-SCOPE-BEFORE-CONFIG
context: sales-order creation failure
statement: &gt;-
  Establish whether the failure is customer-, material-, plant-,
  channel-, or time-specific before assuming a configuration defect.
confidence: medium
questions:
  - What changed immediately before the failures started?
  - Do successful and failed orders share a master-data pattern?
anti_patterns:
  - jump directly to configuration</code></pre>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Storage rule</p><h2>Keep the model maintainable as it grows.</h2></div>
    <ol>
      <li><span>01</span><strong>Topic file</strong><p>One study topic per structured file under the lab data tree.</p></li>
      <li><span>02</span><strong>Reusable entities</strong><p>Promote recurring processes, objects, terms, rules, and failures to stable IDs instead of duplicating them.</p></li>
      <li><span>03</span><strong>Source registry</strong><p>Register evidence once, then reference the source ID from assertions and topics.</p></li>
      <li><span>04</span><strong>Generated views</strong><p>Human pages and machine JSON should be projections of the same structured model.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
