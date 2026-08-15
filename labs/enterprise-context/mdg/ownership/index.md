---
layout: default
title: "MDG Ownership and Federation — Enterprise Context Lab"
description: "Separate core Business Partner ownership from Sales, Procurement, and Finance application data, and understand the current federated MDG process boundary."
permalink: /labs/enterprise-context/mdg/ownership/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - mdg
  - federated-mdg
  - ownership
  - business-partner
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_ownership_federation %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Ownership</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / Ownership and Federation</p>
      <h1>Central system does not mean central ownership of every field.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#owners">Map the owners <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Ownership memory">
      <p>Ownership model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Core</strong><small>Shared identity</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Application</strong><small>Business-specific attributes</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Orchestrate</strong><small>One controlled object</small></div>
      <em>{{ topic.memory_model.phrase }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Design rule:</strong> {{ topic.memory_model.design_rule }}</p>
    <p><strong>Product boundary:</strong> {{ topic.current_product_boundary.documented_scope }}</p>
  </section>

  <section class="research-canvas__inventory" id="owners" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Federated concepts</p>
      <h2>Who owns what?</h2>
      <p>Federation is useful because one Business Partner contains shared identity and application-specific responsibilities. Those responsibilities do not have to live under one decision owner.</p>
    </header>
    <div class="research-route-list">
      {% for concept in topic.concepts %}
      <a href="#layers"><span>{{ forloop.index }}</span><strong>{{ concept.title }}</strong><small>{{ concept.definition }}{% if concept.current_boundary %} <b>Boundary:</b> {{ concept.current_boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Ownership layers</p>
      <h2>Classify the data before assigning an approver.</h2>
    </header>
    <div class="research-route-list">
      {% for layer in topic.ownership_layers %}
      <a href="#bp-example"><span>{{ forloop.index }}</span><strong>{{ layer.layer }}</strong><small><b>{{ layer.question }}</b> {{ layer.examples | join: ", " }}. <b>Pattern:</b> {{ layer.owner_pattern }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="bp-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business Partner example</p>
      <h2>One identity, several application responsibilities.</h2>
      <p>The exact ownership split is an enterprise design decision. The useful question is not “who owns BP?” but “who owns this attribute group for this business purpose?”</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/impact/"><span>CORE</span><strong>{{ topic.bp_ownership_example.core_owner.title }}</strong><small>{{ topic.bp_ownership_example.core_owner.attribute_groups | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/mdg/impact/"><span>SD</span><strong>{{ topic.bp_ownership_example.sales_owner.title }}</strong><small>{{ topic.bp_ownership_example.sales_owner.attribute_groups | join: ", " }}. <b>Proof:</b> {{ topic.bp_ownership_example.sales_owner.business_proof }}</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="/labs/enterprise-context/mdg/impact/"><span>MM</span><strong>{{ topic.bp_ownership_example.procurement_owner.title }}</strong><small>{{ topic.bp_ownership_example.procurement_owner.attribute_groups | join: ", " }}. <b>Proof:</b> {{ topic.bp_ownership_example.procurement_owner.business_proof }}</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/mdg/impact/"><span>FI</span><strong>{{ topic.bp_ownership_example.finance_owner.title }}</strong><small>{{ topic.bp_ownership_example.finance_owner.attribute_groups | join: ", " }}. <b>Proof:</b> {{ topic.bp_ownership_example.finance_owner.business_proof }}</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Federation flow</p>
      <h2>Ownership becomes a runtime process.</h2>
    </header>
    <div class="research-route-list">
      {% for step in topic.federation_flow %}
      <a href="#anti-patterns"><span>{{ step.order }}</span><strong>{{ step.title }}</strong><small><b>Owner:</b> {{ step.owner }}. {{ step.result }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="anti-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure modes</p>
      <h2>Most ownership problems look like workflow or integration problems later.</h2>
    </header>
    <div class="research-route-list">
      {% for failure in topic.anti_patterns %}
      <a href="/labs/enterprise-context/mdg/reasoning/"><span>FAIL</span><strong>{{ failure.title }}</strong><small><b>Symptom:</b> {{ failure.symptom }} <b>Correction:</b> {{ failure.correction }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">science</span>
    <p><strong>Synthetic case:</strong> {{ topic.synthetic_case.title }}. {{ topic.synthetic_case.business_goal }}</p>
    <p><strong>Injected failure:</strong> {{ topic.synthetic_case.injected_failure.symptom }} {{ topic.synthetic_case.injected_failure.likely_branch }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment</p>
      <h2>Workflow follows ownership. It does not create ownership.</h2>
    </header>
    <div class="research-route-list">
      {% for test in topic.assessment_cases %}
      <a href="/labs/enterprise-context/mdg/reasoning/"><span>Q</span><strong>{{ test.prompt }}</strong><small>{{ test.answer_shape | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
