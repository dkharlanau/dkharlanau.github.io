---
layout: default
title: "Enterprise Context Lab — Process, Data, Rules and AI Reasoning"
description: "A source-tracked enterprise context graph connecting SAP processes, data, rules, integrations, failures, KPIs, tests, and architecture reasoning."
permalink: /labs/enterprise-context/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - enterprise-architecture
  - logistics
  - integration
  - business-ai
---

{% assign lab = site.data.labs.enterprise_context.manifest %}
{% assign schema = site.data.labs.enterprise_context.schema %}
{% assign sales_landscape = site.data.labs.enterprise_context.topics.sales_application_landscape %}
{% assign supply_chain_landscape = site.data.labs.enterprise_context.topics.supply_chain_logistics_landscape %}

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
      <em>Last reviewed together {{ lab.last_reviewed_together_at }} · updated {{ lab.updated_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Problem:</strong> SAP knowledge is usually scattered across processes, data, products, integrations, and operational evidence.</p>
    <p><strong>Pages are projections, structured data is the contract.</strong> The lab separates business domains, industries, deployment models, applications, AI components, facts, judgment, and evidence.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare Public, Private, and On-Premise <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="lab-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Context model</p>
      <h2>Connect the business question to the evidence path.</h2>
      <p>The target is not a catalogue of SAP terms. The target is a typed path from business capability and process to data, rules, integrations, operational failure, business impact, and tests.</p>
    </header>

    <div class="research-route-list">
      <a href="/labs/enterprise-context/domains/"><span>01</span><strong>Business Domain → Industry → Deployment</strong><small>Who owns the outcome, what industry changes, and which S/4HANA operating model constrains the design.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/model/"><span>02</span><strong>Capability → Process → Step</strong><small>Where the activity sits in the business flow and which process variant is in scope.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/model/"><span>03</span><strong>Object → Attribute → Rule</strong><small>Which business objects and data concepts participate, and which determination or validation logic uses them.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/model/"><span>04</span><strong>Integration → Failure → KPI → Test</strong><small>How a dependency crosses systems, how it can fail, what outcome it affects, and how the relationship is tested.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
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
      <a href="{% if topic.page_url %}{{ topic.page_url }}{% else %}/labs/enterprise-context/model/#topic-lifecycle{% endif %}"><span>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</span><strong>{{ topic.title }}</strong><small>{{ topic.business_question }}</small><i class="material-symbols-outlined" aria-hidden="true">query_stats</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-application-landscape" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales application landscape</p>
      <h2>{{ sales_landscape.title }}</h2>
      <p>The components below are not competing versions of SD. Each owns a different architectural responsibility across CRM, quoting, commerce, ERP execution, orchestration, sourcing, and service.</p>
    </header>
    <div class="research-route-list">
      {% for app in sales_landscape.applications %}
      <a href="{{ app.official_docs_url }}" target="_blank" rel="noopener"><span>APP</span><strong>{{ app.title }}</strong><small><b>{{ app.architecture_role }}</b> · {{ app.description }} Best fit: {{ app.best_fit }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales decision guide</p>
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
      <p class="research-canvas__eyebrow">Sales licensing signals</p>
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
      <p class="research-canvas__eyebrow">Sales key boundaries</p>
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
      <p class="research-canvas__eyebrow">Sales reference patterns</p>
      <h2>Typical combinations, not mandatory blueprints.</h2>
      <p>The same products can be combined differently. These paths exist to make the architectural separation memorable before deeper integration modeling starts.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in sales_landscape.architecture_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · {{ pattern.fit }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="supply-chain-domain-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain domain map</p>
      <h2>{{ supply_chain_landscape.title }}</h2>
      <p>Start with business domains before product names. The same SAP product can participate in several domains, but each responsibility still needs a clear architectural owner.</p>
      <p><strong>Last reviewed together:</strong> {{ supply_chain_landscape.reviewed_together_at }} · {{ supply_chain_landscape.review_note }}</p>
    </header>
    <div class="research-route-list">
      {% for domain in supply_chain_landscape.domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>DOM</span><strong>{{ domain.title }}</strong><small>{{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="supply-chain-applications" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain application landscape</p>
      <h2>ERP core, advanced execution, planning, and network products.</h2>
      <p>The list separates classic module names such as MM, PP, QM, EWM and TM from adjacent cloud products such as Ariba, IBP, Digital Manufacturing, Business Network, Logistics Management, and GTS.</p>
    </header>
    <div class="research-route-list">
      {% for app in supply_chain_landscape.applications %}
      <a href="{{ app.official_docs_url }}" target="_blank" rel="noopener"><span>APP</span><strong>{{ app.title }}</strong><small><b>{{ app.architecture_role }}</b> · {{ app.description }} Best fit: {{ app.best_fit }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain decision guide</p>
      <h2>Choose the system by the decision or execution responsibility it must own.</h2>
      <p>Do not start with “Which module contains this transaction?” Start with “Who owns this business decision, posting, optimization, collaboration, or execution step?”</p>
    </header>
    <div class="research-route-list">
      {% for decision in supply_chain_landscape.decision_guide %}
      {% assign selected = nil %}
      {% for app in supply_chain_landscape.applications %}{% if app.id == decision.primary_choice %}{% assign selected = app %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}Primary: {{ selected.title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain licensing signals</p>
      <h2>Know which boundary is functional and which one is commercial.</h2>
      <p>Metrics below are taken from reviewed public SAP sources where available. They are architecture signals, not contractual advice. Exact rights depend on edition, package, deployment, add-ons, use rights, country, and the signed agreement.</p>
    </header>
    <div class="research-route-list">
      {% for app in supply_chain_landscape.applications %}
      <a href="{{ app.official_commercial_url }}" target="_blank" rel="noopener"><span>LIC</span><strong>{{ app.title }}</strong><small>{{ app.licensing.commercial_model }}{% if app.licensing.metric %} · Metric: {{ app.licensing.metric }}{% endif %}{% if app.licensing.purchase_unit %} · {{ app.licensing.purchase_unit }}{% endif %}{% if app.licensing.note %} · {{ app.licensing.note }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain key boundaries</p>
      <h2>Use the lightest component that owns the required responsibility.</h2>
      <p>More advanced does not automatically mean more appropriate. EWM is not a better MM-IM, PP/DS is not a better MRP for every material, Digital Manufacturing is not a better production order, and a business network is not a better ERP.</p>
    </header>
    <div class="research-route-list">
      {% for app in supply_chain_landscape.applications %}
      <a href="{{ app.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ app.title }}</strong><small>{{ app.not_for }}{% if app.limitations and app.limitations.size > 0 %} Key limitation: {{ app.limitations[0] }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supply chain reference patterns</p>
      <h2>Typical end-to-end combinations.</h2>
      <p>These are reference paths to explain ownership and integration. They are not mandatory SAP blueprints and should be validated against process complexity, edition, deployment, licensing, integration, and operational constraints.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in supply_chain_landscape.architecture_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · {{ pattern.fit }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>