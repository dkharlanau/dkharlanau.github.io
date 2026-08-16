---
layout: default
title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
description: "Architect-level SAP development guide: RAP vs CAP, ABAP Cloud, classic ABAP, CDS, BTP runtimes, side-by-side design and clean-core trade-offs."
permalink: /labs/enterprise-context/development/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-16
hide_global_cta: true
tags:
  - sap
  - abap
  - rap
  - cap
  - cds
  - btp
  - clean-core
  - architecture
last_reviewed: 2026-08-16
publication_wave: "lead-architecture-search-wave-03"
review_method: "primary sources + factual review + page-level editorial review"
search_intent: "SAP clean core development with ABAP Cloud, RAP, CAP and BTP"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-s4hana"
ai_sidecar: "/ai/pages/labs--enterprise-context--development.json"
semantic_links:
  - type: "Related topic"
    title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
    url: "/labs/enterprise-context/business-ai/"
  - type: "Same domain"
    title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "Related topic"
    title: "Enterprise Agent Architecture — Tools, Identity, Autonomy and Governance"
    url: "/labs/enterprise-context/business-ai/agents/"
  - type: "Related topic"
    title: "SAP EWM — Deployment & Warehouse Execution Map"
    url: "/labs/enterprise-context/ewm/"
  - type: "Same domain"
    title: "FI/CO for Logistics — Enterprise Context Lab"
    url: "/labs/enterprise-context/finance-logistics/"
  - type: "Same domain"
    title: "Cross-Process Logistics Capabilities — Enterprise Context Lab"
    url: "/labs/enterprise-context/logistics-capabilities/"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.development_architecture %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Development Architecture</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Development architecture</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#decision-matrix">Start with the decision <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Development architecture research status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.building_blocks | size }}</strong><small>Core building blocks</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.decision_matrix | size }}</strong><small>Decision scenarios</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>First rule:</strong> RAP, CAP, CDS, ABAP Objects, BTP and Cloud Foundry are not alternatives at the same level. One is a programming model, another a data model, another a runtime, another a deployment target.</p>
    <p><strong>Architecture starts with coupling:</strong> where is the transaction, where is the data, who owns the lifecycle, and what happens when the network is down?</p>
    <a href="/labs/enterprise-context/data/development.json">Open the AI-readable model <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture thesis</p>
      <h2>Build close to the business boundary, not close to the current fashion.</h2>
      <p>These are working architecture rules, not SAP product slogans.</p>
    </header>
    <div class="research-route-list">
      {% for principle in topic.architecture_thesis %}
      <a href="/labs/enterprise-context/data/development.json"><span>{{ forloop.index }}</span><strong>Decision rule</strong><small>{{ principle }}</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>Separate language, data model, programming model, UI, runtime and tooling.</h2>
      <p>This removes most false comparisons before the architecture discussion even starts.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.concept_layers %}
      <a href="/labs/enterprise-context/data/development.json"><span>LAY</span><strong>{{ layer.title }}</strong><small>{{ layer.examples | join: " · " }} — {{ layer.architect_note }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technology map</p>
      <h2>What each building block actually owns.</h2>
      <p>A technology earns a place when its responsibility is clear.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.building_blocks %}
      <a href="/labs/enterprise-context/data/development.json"><span>DEV</span><strong>{{ item.title }}</strong><small><b>{{ item.role }}</b> Best fit: {{ item.best_fit }} Architect view: {{ item.architect_view }}</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="decision-matrix" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision matrix</p>
      <h2>If I need to build something, where do I start?</h2>
      <p>Prefer the smallest architecture that keeps the correct transaction and lifecycle boundary.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_matrix %}
      <a href="/labs/enterprise-context/data/development.json"><span>→</span><strong>{{ decision.need }}</strong><small><b>Prefer:</b> {{ decision.preferred }} · <b>Fallback:</b> {{ decision.fallback }} · <b>Avoid:</b> {{ decision.avoid }} · {{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extensibility</p>
      <h2>Key user, ABAP Cloud, classic ABAP and side-by-side are different coupling choices.</h2>
      <p>Clean core does not require one answer for every requirement.</p>
    </header>
    <div class="research-route-list">
      {% for model in topic.extension_models %}
      <a href="/labs/enterprise-context/data/development.json"><span>EXT</span><strong>{{ model.title }}</strong><small><b>{{ model.coupling }}</b> · Choose when: {{ model.choose_when }} Lead rule: {{ model.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Runtime choice</p>
      <h2>On-stack, Cloud Foundry, Kyma or BTP ABAP Environment?</h2>
      <p>The runtime changes networking, operations, scaling and lifecycle. This is where side-by-side architecture becomes real rather than decorative.</p>
    </header>
    <div class="research-route-list">
      {% for runtime in topic.runtime_decisions %}
      <a href="/labs/enterprise-context/data/development.json"><span>RUN</span><strong>{{ runtime.title }}</strong><small><b>Default:</b> {{ runtime.default_stack }} · Best for: {{ runtime.best_for }} · Cost signal: {{ runtime.costs[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Clean core, without religion</p>
      <h2>{{ topic.clean_core_reality.definition }}</h2>
      <p>{{ topic.clean_core_reality.sap_reality_check }}</p>
    </header>
    <div class="research-route-list">
      {% for rule in topic.clean_core_reality.practical_rules %}
      <a href="/labs/enterprise-context/data/development.json"><span>CORE</span><strong>Practical rule</strong><small>{{ rule }}</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Clean code</p>
      <h2>Readable code and upgrade-stable core are separate engineering goals.</h2>
      <p>{{ topic.clean_code_reality.definition }} {{ topic.clean_code_reality.caution }}</p>
    </header>
    <div class="research-route-list">
      {% for practice in topic.clean_code_reality.practices %}
      <a href="/labs/enterprise-context/data/development.json"><span>CODE</span><strong>Engineering practice</strong><small>{{ practice }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Side-by-side cost model</p>
      <h2>Independence is useful. It is not free.</h2>
      <p>{{ topic.side_by_side_cost_model.architect_rule }}</p>
    </header>
    <div class="research-route-list">
      {% for cost in topic.side_by_side_cost_model.hidden_costs %}
      <a href="/labs/enterprise-context/data/development.json"><span>$</span><strong>Hidden distributed-systems cost</strong><small>{{ cost }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Toolchain and languages</p>
      <h2>Know enough to choose and challenge a design.</h2>
      <p>A Lead does not need to be the best developer in every stack. A Lead does need to understand what skills, runtime and lifecycle the choice creates.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.language_map %}
      <a href="/labs/enterprise-context/data/development.json"><span>{{ item.priority_for_sap_lead }}</span><strong>{{ item.language }}</strong><small>{{ item.learn_for }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture smells</p>
      <h2>Patterns that look modern and age badly.</h2>
      <p>Most bad architecture is not technically impossible. That is the problem.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.anti_patterns %}
      <a href="/labs/enterprise-context/data/development.json"><span>!</span><strong>{{ item.name }}</strong><small>{{ item.smell }} Correction: {{ item.correction }}</small><i class="material-symbols-outlined" aria-hidden="true">report_problem</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Answers should expose the trade-off, not recite the product catalog.</h2>
      <p>These are compact interview answers. The reasoning behind them is in the model above.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.lead_assessment_answers %}
      <a href="/labs/enterprise-context/data/development.json"><span>Q</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
