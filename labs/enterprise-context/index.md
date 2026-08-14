---
layout: default
title: "Enterprise Context Lab — Process, Data, Rules and AI Reasoning"
description: "A working lab for a source-tracked enterprise context graph connecting processes, business objects, attributes, rules, integrations, failures, KPIs, tests, and expert reasoning."
permalink: /labs/enterprise-context/
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
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">Enterprise Context</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / {{ lab.version }}</p>
      <h1>{{ lab.model_name }}</h1>
      <p>{{ lab.purpose }}</p>
      <a class="research-canvas__button" href="#lab-model">See the working model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Lab status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ lab.first_vertical.gates_complete }}/{{ lab.first_vertical.gates_total }}</strong><small>First-topic gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ schema.node_types | size }}</strong><small>Node types</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ schema.edge_types | size }}</strong><small>Edge types</small></div>
      <em>Started {{ lab.started_at }} · updated {{ lab.updated_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Pages are projections, structured data is the contract.</strong> The lab separates documented facts, expert judgment, inference, and synthetic assumptions so a later AI system can inspect both the relationship and its evidence state.</p>
    <a href="/labs/enterprise-context/model/">Open the authoring contract <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="lab-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Context model</p>
      <h2>Connect the business question to the evidence path.</h2>
      <p>The target is not a catalogue of SAP terms. The target is a typed path from business capability and process to data, rules, integrations, operational failure, business impact, and tests.</p>
    </header>

    <div class="research-route-list">
      <a href="/labs/enterprise-context/model/"><span>01</span><strong>Capability → Process → Step</strong><small>Where the activity sits in the business flow and which process variant is in scope.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/model/"><span>02</span><strong>Object → Attribute → Rule</strong><small>Which business objects and data concepts participate, and which determination or validation logic uses them.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/model/"><span>03</span><strong>Integration → Failure → KPI → Test</strong><small>How a dependency crosses systems, how it can fail, what outcome it affects, and how the relationship is tested.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">First deep vertical</p>
      <h2>{{ lab.first_vertical.title }}</h2>
      <p>Depth comes before coverage. Each topic passes the same seven gates so research status is explicit rather than represented by a decorative percentage.</p>
    </header>

    <div class="research-route-list">
      {% for topic_entry in site.data.labs.enterprise_context.topics %}
      {% assign topic = topic_entry[1] %}
      <a href="/labs/enterprise-context/model/#topic-lifecycle"><span>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</span><strong>{{ topic.title }}</strong><small>{{ topic.business_question }}</small><i class="material-symbols-outlined" aria-hidden="true">query_stats</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__method" id="topic-lifecycle" data-reveal>
    <div><p class="research-canvas__eyebrow">Seven maturity gates</p><h2>Every topic follows the same completion contract.</h2></div>
    <ol>
      {% for gate in lab.maturity_gates %}
      <li><span>0{{ gate.order }}</span><strong>{{ gate.label }}</strong><p>{{ gate.done_definition }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference enterprise</p>
      <h2>{{ lab.reference_enterprise.title }}</h2>
      <p>{{ lab.reference_enterprise.description }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/model/"><span>GT</span><strong>Synthetic enterprise, not client data</strong><small>The reference company will provide organization, master data, processes, transactions, interfaces, injected failures, and benchmark scenarios.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">For tools and AI</p>
      <h2>Machine-readable endpoints</h2>
      <p>The same project metadata exposed on this page is also available as generated JSON.</p>
    </header>
    <div class="research-route-list">
      <a href="{{ lab.machine_endpoints.catalog }}"><span>01</span><strong>Catalog JSON</strong><small>Project manifest plus pointers to schema, topics, and sources.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="{{ lab.machine_endpoints.schema }}"><span>02</span><strong>Schema JSON</strong><small>Node types, edge types, evidence states, stable-ID rules, and date fields.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="{{ lab.machine_endpoints.topics }}"><span>03</span><strong>Topics JSON</strong><small>Current research topics, scope, maturity gates, and planned evaluation targets.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="{{ lab.machine_endpoints.sources }}"><span>04</span><strong>Sources JSON</strong><small>Source registry and provenance policy without bulk copying source material.</small><i class="material-symbols-outlined" aria-hidden="true">source</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
