---
layout: default
title: "SAP MDG Assessment Reasoning — Enterprise Context Lab"
description: "Problem-based SAP MDG assessment practice: Explain, Compare, Design, and Diagnose with evidence paths and Lead-level scoring."
permalink: /labs/enterprise-context/mdg/reasoning/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - mdg
  - assessment
  - reasoning
  - diagnostics
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_assessment_reasoning %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Reasoning</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / Assessment Reasoning</p>
      <h1>Facts are the input. The assessment tests the decision.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#cases">Open the cases <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Reasoning memory">
      <p>Answer path</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Boundary</strong><small>What is the real scope?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Decision</strong><small>Why this pattern?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Proof</strong><small>What evidence closes it?</small></div>
      <em>{{ topic.memory_model.phrase }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Evaluation rule:</strong> {{ topic.memory_model.evaluation_rule }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Question types</p>
      <h2>Four modes test different kinds of understanding.</h2>
    </header>
    <div class="research-route-list">
      {% for type in topic.question_types %}
      <a href="#cases"><span>{{ forloop.index }}</span><strong>{{ type.title }}</strong><small>{{ type.purpose }} <b>Score:</b> {{ type.scoring_focus | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Answer contract</p>
      <h2>A useful Lead answer has a visible structure.</h2>
    </header>
    <div class="research-route-list">
      {% for step in topic.answer_contract.strong_answer_sequence %}
      <a href="#cases"><span>{{ forloop.index }}</span><strong>{{ step }}</strong><small>Keep the reasoning short enough to follow, but explicit enough to defend.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="cases" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reasoning cases</p>
      <h2>Answer first. Then compare with the expected path.</h2>
      <p>The weak answer is included because it exposes the common shortcut. The Lead signal shows what the answer should add.</p>
    </header>
    <div class="research-route-list">
      {% for case in topic.cases %}
      <a href="#score"><span>{{ case.mode | upcase }}</span><strong>{{ case.prompt }}</strong><small><b>Path:</b> {{ case.reasoning_path | join: " → " }}. <b>Weak:</b> {{ case.weak_answer }} <b>Lead signal:</b> {{ case.lead_signal }}</small><i class="material-symbols-outlined" aria-hidden="true">quiz</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="score" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scoring</p>
      <h2>Score reasoning, not vocabulary.</h2>
    </header>
    <div class="research-route-list">
      {% for dimension in topic.scoring_model.dimensions %}
      <a href="/labs/enterprise-context/mdg/"><span>{{ dimension.weight }}%</span><strong>{{ dimension.id | replace: "_", " " | capitalize }}</strong><small>{{ dimension.strong }}</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Weak-answer pattern:</strong> {{ topic.answer_contract.weak_patterns | join: " · " }}</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
