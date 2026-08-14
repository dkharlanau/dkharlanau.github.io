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
{% assign sales_landscape = site.data.labs.enterprise_context.topics.sales_application_landscape %}

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
      <p class="research-canvas__eyebrow">Research topics</p>
      <h2>Depth comes before coverage.</h2>
      <p>Each topic passes the same seven gates so research status is explicit rather than represented by a decorative percentage.</p>
    </header>

    <div class="research-route-list">
      {% for topic_entry in site.data.labs.enterprise_context.topics %}
      {% assign topic = topic_entry[1] %}
      <a href="/labs/enterprise-context/model/#topic-lifecycle"><span>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</span><strong>{{ topic.title }}</strong><small>{{ topic.business_question }}</small><i class="material-symbols-outlined" aria-hidden="true">query_stats</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-application-landscape" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Application landscape</p>
      <h2>{{ sales_landscape.title }}</h2>
      <p>The components below are not eight competing versions of SD. Each owns a different architectural responsibility across CRM, quoting, commerce, ERP execution, orchestration, sourcing, and service.</p>
    </header>
    <div class="research-route-list">
      {% for app in sales_landscape.applications %}
      <a href="{{ app.official_docs_url }}" target="_blank" rel="noopener"><span>APP</span><strong>{{ app.title }}</strong><small><b>{{ app.architecture_role }}</b> · {{ app.description }} Best fit: {{ app.best_fit }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Choose by responsibility, not by product-name similarity.</h2>
      <p>Start with the business responsibility that needs an owner. Then decide whether the component is a system of engagement, system of record, commerce channel, quote engine, orchestration layer, or sourcing service.</p>
    </header>
    <div class="research-route-list">
      {% for decision in sales_landscape.decision_guide %}
      {% assign selected = nil %}
      {% for app in sales_landscape.applications %}{% if app.id == decision.primary_choice %}{% assign selected = app %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}Primary: {{ selected.title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Licensing signals</p>
      <h2>Architecture has a commercial boundary too.</h2>
      <p>These are public licensing signals, not a substitute for the customer contract. SAP product use rights, editions, packages, add-ons, digital access, region, and commercial agreements can change the exact entitlement.</p>
    </header>
    <div class="research-route-list">
      {% for app in sales_landscape.applications %}
      <a href="{{ app.official_commercial_url }}" target="_blank" rel="noopener"><span>LIC</span><strong>{{ app.title }}</strong><small>{{ app.licensing.commercial_model }}{% if app.licensing.metric %} · Metric: {{ app.licensing.metric }}{% endif %}{% if app.licensing.purchase_unit %} · {{ app.licensing.purchase_unit }}{% endif %}{% if app.licensing.minimum_quantity %} · Minimum: {{ app.licensing.minimum_quantity }}{% endif %}{% if app.licensing.note %} · {{ app.licensing.note }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Key boundaries</p>
      <h2>What each component should not silently become.</h2>
      <p>Most architecture mistakes happen when a product is technically capable of doing something and is therefore promoted to owning the entire process. The graph keeps the principal boundary explicit.</p>
    </header>
    <div class="research-route-list">
      {% for app in sales_landscape.applications %}
      <a href="{{ app.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ app.title }}</strong><small>{{ app.not_for }}{% if app.limitations and app.limitations.size > 0 %} Key limitation: {{ app.limitations[0] }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference patterns</p>
      <h2>Typical combinations, not mandatory blueprints.</h2>
      <p>The same products can be combined differently. These paths exist to make the architectural separation memorable before deeper integration modeling starts.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in sales_landscape.architecture_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · {{ pattern.fit }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
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
