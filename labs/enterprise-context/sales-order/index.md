---
layout: default
title: "Sales Order Determination Graph — Enterprise Context Lab"
description: "A source-tracked causal model of SAP S/4HANA sales-order determinations: inputs, rules, outputs, dependencies, impact traces, and expert reasoning."
permalink: /labs/enterprise-context/sales-order/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
enterprise_context_graph: true
---

{% assign graph = site.data.labs.enterprise_context.graphs.sales_order %}
{% assign evidence = site.data.labs.enterprise_context.sources.sales_order_determinations %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Sales Order Graph</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Deep vertical / Order-to-Cash</p>
      <h1>A sales order is a small decision engine.</h1>
      <p>{{ graph.summary }} Most process maps stop at “Create Sales Order”. That is exactly where the interesting part starts.</p>
      <a class="research-canvas__button" href="#dependency-engine">Open the dependency engine <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Graph inventory">
      <p>Working graph</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ graph.determinations | size }}</strong><small>Determinations</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ graph.causal_edges | size }}</strong><small>Causal edges</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ evidence.sources | size }}</strong><small>Official sources</small></div>
      <em>Draft model · source-tracked · client data excluded</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>A field is boring until it becomes somebody else’s input.</strong> The graph therefore models determinations as first-class objects: inputs → mechanism → output → downstream consequences.</p>
    <a href="/labs/enterprise-context/data/sales-order-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three projections</p>
      <h2>One model, three ways to think.</h2>
      <p>Process flow is useful, but it is only one projection. The same structured model should also explain the document and answer the consultant’s favorite question: “why did SAP do that?”</p>
    </header>

    <div class="ecg-view-grid">
      {% for view in graph.views %}
      <article class="ecg-view-card">
        <span>0{{ forloop.index }}</span>
        <h3>{{ view.title }}</h3>
        <p class="ecg-question">{{ view.question }}</p>
        <p>{{ view.projection }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="dependency-engine" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Dependency engine</p>
      <h2>The order item is where several worlds collide.</h2>
      <p>Customer context, material data, organizational design, configuration, calendars, availability, and commercial rules meet inside a document that still manages to look like a form.</p>
    </header>

    <div class="ecg-rail" aria-label="Simplified sales-order dependency chain">
      <div class="ecg-rail__branch">
        <span class="ecg-node ecg-node--input">Material + Customer</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Plant proposal</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Plant</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Shipping point</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Shipping Point</span>
      </div>
      <div class="ecg-rail__branch">
        <span class="ecg-node ecg-node--input">Zones + Shipping Condition + Transport Group</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Route determination</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Route</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Scheduling</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Material Availability Date</span>
      </div>
      <div class="ecg-rail__branch">
        <span class="ecg-node ecg-node--input">Date + Quantity + Plant + Supply</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Availability</span>
        <span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Confirmed Qty / Date</span>
      </div>
    </div>

    <p class="ecg-caption">Simplified reasoning projection, not an execution trace. The exact path depends on release, configuration, activated capabilities, and design choices.</p>
  </section>

  <section class="ecg-anatomy" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">Determination anatomy</p>
      <h2>Do not store “Plant Determination” as a paragraph.</h2>
      <p>Store a small machine. Then a human can read it, a graph can traverse it, and an AI system can explain it without pretending that keyword similarity is reasoning.</p>
    </div>
    <ol>
      <li><span>01</span><strong>Inputs</strong><p>Master data, document data, organizational context, previous outputs.</p></li>
      <li><span>02</span><strong>Mechanism</strong><p>Lookup, procedure, condition technique, calculation, search strategy, availability check.</p></li>
      <li><span>03</span><strong>Output</strong><p>The value or decision written back into the business object.</p></li>
      <li><span>04</span><strong>Consequences</strong><p>Which later determinations, controls, integrations, or process steps consume it.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Determination catalogue</p>
      <h2>Ten decisions worth tracing.</h2>
      <p>These are intentionally modeled as decision nodes rather than a flat list of configuration tables. The important unit is the path from input to consequence.</p>
    </header>

    <div class="ecg-determination-grid">
      {% for determination in graph.determinations %}
      <article class="ecg-determination">
        <header>
          <span>DET {{ forloop.index }}</span>
          <small>{{ determination.level | replace: "_", " " }}</small>
        </header>
        <h3>{{ determination.title }}</h3>
        <p class="ecg-question">{{ determination.question }}</p>
        <dl>
          <div><dt>Mechanism</dt><dd>{{ determination.mechanism | replace: "_", " " }}</dd></div>
          <div><dt>Inputs</dt><dd>{{ determination.inputs | size }}</dd></div>
          <div><dt>Outputs</dt><dd>{{ determination.output | size }}</dd></div>
        </dl>
        <p class="ecg-lead-lens">{{ determination.lead_lens }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Impact traces</p>
      <h2>Forward for impact. Backward for explanation.</h2>
      <p>This is where a graph starts earning its keep. A consultant can move downstream from a proposed change or walk upstream from a suspicious value.</p>
    </header>

    <div class="ecg-traces">
      {% for trace in graph.impact_traces %}
      <article class="ecg-trace">
        <div class="ecg-trace__head">
          <span>{{ trace.id }}</span>
          <h3>{{ trace.title }}</h3>
        </div>
        <div class="ecg-trace__path">
          {% for step in trace.path %}
          <span>{{ step }}</span>{% unless forloop.last %}<i aria-hidden="true">→</i>{% endunless %}
          {% endfor %}
        </div>
        <p>{{ trace.caveat }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Experience layer</p>
      <h2>Documentation says what exists. Investigation needs another layer.</h2>
      <p>Project knowledge is stored separately from documented behavior. That keeps a useful heuristic useful without quietly promoting it to vendor fact.</p>
    </header>

    <div class="research-route-list">
      {% for pattern in graph.experience_patterns %}
      <a href="/labs/enterprise-context/model/"><span>EXP</span><strong>{{ pattern.title }}</strong><small>{{ pattern.statement }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence</p>
      <h2>Every interesting edge eventually needs a source.</h2>
      <p>The first graph uses official SAP Help as the factual baseline. Release scope stays attached because “SAP works like this” is usually where future archaeology begins.</p>
    </header>

    <div class="research-route-list">
      {% for source in evidence.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.title }}</strong><small>{{ source.product_scope }} · {{ source.release_scope }} · accessed {{ source.accessed_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="ecg-machine" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">For tools and AI</p>
      <h2>The page is a projection. The graph is the asset.</h2>
      <p>The same determinations, edges, traces, and evidence references are exposed as JSON. Later experiments can render different views, create synthetic scenarios, or benchmark whether an AI answer follows the dependency path instead of improvising one.</p>
    </div>
    <a class="research-canvas__button" href="/labs/enterprise-context/data/sales-order-graph.json">Open sales-order graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
