---
layout: default
title: "SAP MDG Data Model Anatomy — Enterprise Context Lab"
description: "Problem-first SAP MDG data modeling: roots, entity types, keys, staging, active areas, Material structure, and extension decisions."
permalink: /labs/enterprise-context/mdg/data-model/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - mdg
  - data-model
  - master-data
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_data_model_anatomy %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Data Model</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / Data Model Anatomy</p>
      <h1>Model the object before the screen.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#layers">Trace the model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Data model memory">
      <p>Memory model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Root</strong><small>What is governed?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Entity</strong><small>Where does the data belong?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>State</strong><small>Staging → active</small></div>
      <em>{{ topic.memory_model.phrase }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Design rule:</strong> {{ topic.memory_model.design_rule }}</p>
  </section>

  <section class="research-canvas__inventory" id="layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Six questions</p>
      <h2>A data model is a sequence of design decisions.</h2>
      <p>Do not begin with a custom field. First decide the governed root, entity boundary, key, relationship, processing state, and active storage.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.modeling_layers %}
      <a href="#entity-types"><span>{{ layer.order }}</span><strong>{{ layer.title }}</strong><small><b>{{ layer.question }}</b> {{ layer.example }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="entity-types" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Classic MDG Application Framework</p>
      <h2>Storage and use types tell you what an entity can do.</h2>
      <p>The numbers are not trivia. They tell you whether the entity is independently governed, dependent, reference-only, and whether MDG generates storage for it.</p>
    </header>
    <div class="research-route-list">
      {% for entity in topic.storage_and_use_types %}
      <a href="#active-area"><span>{{ forloop.index }}</span><strong>{{ entity.title }}</strong><small>{{ entity.meaning }} <b>Use:</b> {{ entity.design_use }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="active-area" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Active state</p>
      <h2>MDG active area or reuse active area?</h2>
      <p>{{ topic.active_area_decision.question }}</p>
    </header>
    <div class="research-route-list">
      {% for option in topic.active_area_decision.options %}
      <a href="#material"><span>DEC</span><strong>{{ option.option }}</strong><small><b>Fit:</b> {{ option.fit }} <b>Consequence:</b> {{ option.consequence }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="material" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Material example</p>
      <h2>One Material ID, many data slices.</h2>
      <p>The delivered MM model makes the architecture visible: basic data, plant data, sales, purchasing, valuation, units, and classification do not have the same organizational scope or consumers.</p>
    </header>
    <div class="research-route-list">
      {% for slice in topic.material_anatomy.slices %}
      <a href="/labs/enterprise-context/mdg/impact/"><span>MD</span><strong>{{ slice.title }}</strong><small>{{ slice.scope }} <b>Examples:</b> {{ slice.examples | join: ", " }}. <b>Consumers:</b> {{ slice.consumers | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extension reasoning</p>
      <h2>A new field is never only a new field.</h2>
      <p>Walk through these checks before deciding how to extend the model.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.extension_reasoning.path %}
      <a href="/labs/enterprise-context/mdg/extensions/"><span>{{ item.step }}</span><strong>{{ item.question }}</strong><small><b>Weak:</b> {{ item.weak_answer }} <b>Lead signal:</b> {{ item.lead_signal }}</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">science</span>
    <p><strong>Synthetic case:</strong> {{ topic.synthetic_case.title }}. {{ topic.synthetic_case.request }}</p>
    <p><strong>Proof:</strong> {{ topic.synthetic_case.proof | join: " · " }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment checks</p>
      <h2>Explain the model, then use it.</h2>
    </header>
    <div class="research-route-list">
      {% for test in topic.assessment_cases %}
      <a href="/labs/enterprise-context/mdg/reasoning/"><span>Q</span><strong>{{ test.prompt }}</strong><small><b>Expected path:</b> {{ test.answer_shape | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
