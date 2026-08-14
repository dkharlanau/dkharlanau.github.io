---
layout: default
title: "SAP Business AI & AI Platform Landscape — Enterprise Context Lab"
description: "A decision-oriented map of SAP Business AI, Joule, agents, Joule Studio, AI Foundation, AI Core, AI Launchpad, generative AI hub, business grounding, and AI governance."
permalink: /labs/enterprise-context/business-ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
---

{% assign topic = site.data.labs.enterprise_context.topics.business_ai_platform_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Business AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Business AI</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#ai-layers">Explore the architecture <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Review status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.layers | size }}</strong><small>Architecture layers</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.components | size }}</strong><small>Modeled components</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Architecture boundary.</strong> SAP Business AI is a portfolio and platform landscape, not one product. User experience, agents, development, runtime, model access, grounding, and governance are modeled as separate responsibilities.</p>
    <a href="/labs/enterprise-context/domains/">Open enterprise domain taxonomy <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="ai-layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture layers</p>
      <h2>Separate the responsibility before choosing the component.</h2>
      <p>Most poor AI architecture starts by treating every SAP AI name as interchangeable. The layer model keeps user experience, business agents, build tools, runtime, grounding, and governance distinct.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.layers %}
      <a href="#components"><span>AI</span><strong>{{ layer.title }}</strong><small>{{ layer.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="components" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP Business AI components</p>
      <h2>Choose by architecture role, not by brand proximity.</h2>
      <p>Each component below has a different responsibility. The official SAP source is linked directly from the component card.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>{% if component.type == 'ai_asset' %}AI{% else %}PLT{% endif %}</span><strong>{{ component.title }}</strong><small><b>{{ component.architecture_role }}</b> · {{ component.description }} Best fit: {{ component.best_fit }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Start with the responsibility that needs an owner.</h2>
      <p>The same business scenario can use several AI components. This guide identifies the primary component for the responsibility, not the only technology in the end-to-end solution.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      {% assign selected = nil %}
      {% for component in topic.components %}{% if component.id == decision.primary_choice %}{% assign selected = component %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}Primary: {{ selected.title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Licensing signals</p>
      <h2>AI architecture has a consumption model.</h2>
      <p>These are public commercial signals, not contract advice. Base AI, Premium AI, AI Units, SAP Build entitlements, BTP service plans, model tokens, data-platform subscriptions, and downstream application rights can all participate in one solution.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_commercial_url }}" target="_blank" rel="noopener"><span>LIC</span><strong>{{ component.title }}</strong><small>{{ component.licensing.commercial_model }}{% if component.licensing.metric %} · Metric: {{ component.licensing.metric }}{% endif %}{% if component.licensing.note %} · {{ component.licensing.note }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Key boundaries</p>
      <h2>Do not promote one component into the whole AI stack.</h2>
      <p>The boundary is as important as the capability. A conversational experience is not a runtime; a runtime is not a grounding layer; an agent builder is not an enterprise integration platform.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ component.title }}</strong><small>{{ component.not_for }}{% if component.limitations and component.limitations.size > 0 %} Key limitation: {{ component.limitations[0] }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference patterns</p>
      <h2>Typical combinations, not mandatory blueprints.</h2>
      <p>Patterns make ownership visible before deeper API, authorization, grounding, observability, and evaluation design begins.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.reference_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · {{ pattern.fit }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
