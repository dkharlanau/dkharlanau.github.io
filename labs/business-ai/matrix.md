---
layout: default
title: "Business AI Assessment Matrix — Process, Autonomy, Risk, KPI"
description: "Lead-level Business AI decision matrix linking process, AI job, reusable pattern, autonomy, risk, KPI, controls, failure patterns, and public evidence."
permalink: /labs/business-ai/matrix/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
last_reviewed: 2026-09-22
hide_global_cta: true
tags:
  - business-ai
  - assessment
  - architecture
  - autonomy
  - risk
---

{% assign matrix = site.data.labs.business_ai.assessment_matrix %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Assessment Matrix</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / assessment matrix</p>
      <h1>Capability is only<br />one part of the answer.</h1>
      <p>An AI system may be able to summarize, classify, negotiate, recommend, or act. That still does not tell us whether it should have authority inside a business process. The matrix connects technical capability with the process, system ownership, business risk, controls, and result we expect to improve.</p>
      <a class="research-canvas__button" href="#profiles">Open the matrix <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Decision framework</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ matrix.profiles | size }}</strong><small>Scenario profiles</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ matrix.autonomy_levels | size }}</strong><small>Autonomy levels</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ matrix.decision_rules | size }}</strong><small>Architecture rules</small></div>
      <em>Model capability is not the same thing as business authority.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>The matrix is a comparison tool, not a scoring engine.</strong> It helps us make the hidden assumptions in an AI proposal visible: what process step is changing, what the model is expected to do, what can go wrong, which system remains authoritative, and how much autonomy is justified.</p>
      <p>{{ matrix.reading_rule }}</p>
      <p>Two solutions can use similar models and still need very different operating boundaries. Drafting a reply for an employee is not the same kind of action as changing a contract, posting an accounting document, or sending a supplier commitment.</p>
    </div>
    <a href="/labs/business-ai/scenarios/">Compare with scenario evidence <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="autonomy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Autonomy scale</p>
      <h2>Autonomy describes where human or system authority enters the flow.</h2>
      <p>Terms such as “human in the loop” can hide important differences. A system that drafts a proposal, one that executes after explicit approval, and one that acts within predefined limits are not equivalent even if a person can eventually intervene in all three.</p>
    </header>
    <div class="research-route-list">
      {% for level in matrix.autonomy_levels %}
      <a href="#autonomy"><span>{{ level.id }}</span><strong>{{ level.label }}</strong><small>{{ level.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">What changes the answer</p><h2>The autonomy level depends on the business situation around the model.</h2></div>
    <ol>
      {% for item in matrix.decision_rules %}
      <li><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>{{ item.id | replace: 'dr-', '' | replace: '-', ' ' | capitalize }}</strong><p>{{ item.rule }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__inventory" id="profiles" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scenario matrix</p>
      <h2>{{ matrix.profiles | size }} examples of the same capability meeting different business conditions.</h2>
      <p>Each profile keeps the process, AI job, autonomy, risk, KPI, authority, controls, likely failure patterns, and available evidence together. The point is to compare the whole operating context rather than judge the model in isolation.</p>
    </header>
    <div class="research-route-list">
      {% for item in matrix.profiles %}
      <a href="#{{ item.id }}"><span>{{ item.recommended_autonomy }}</span><strong>{{ item.process }} · {{ item.ai_job }}</strong><small>Risk: {{ item.risk_class }} · KPI: {{ item.primary_kpis | first }} · Max before extra controls: {{ item.maximum_autonomy_before_extra_controls }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for item in matrix.profiles %}
  <section class="research-canvas__inventory" id="{{ item.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">{{ item.process }} / risk {{ item.risk_class }}</p>
      <h2>{{ item.ai_job }}</h2>
      <p>Recommended autonomy: <strong>{{ item.recommended_autonomy }}</strong>. Maximum before extra controls: <strong>{{ item.maximum_autonomy_before_extra_controls }}</strong>.</p>
    </header>
    <div class="research-route-list">
      <a href="#{{ item.id }}"><span>PAT</span><strong>Reusable pattern</strong><small>{{ item.pattern_ids | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#{{ item.id }}"><span>KPI</span><strong>Business scorecard</strong><small>{{ item.primary_kpis | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#{{ item.id }}"><span>AUTH</span><strong>System authority</strong><small>{{ item.system_authority }}</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="#{{ item.id }}"><span>CTRL</span><strong>Required controls</strong><small>{{ item.required_controls | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="#{{ item.id }}"><span>FAIL</span><strong>Failure patterns to test</strong><small>{{ item.failure_pattern_ids | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#{{ item.id }}"><span>CASE</span><strong>Evidence joins</strong><small>{{ item.scenario_ids | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#{{ item.id }}"><span>Q</span><strong>Assessment question</strong><small>{{ item.assessment_prompt }}</small><i class="material-symbols-outlined" aria-hidden="true">quiz</i></a>
      <a href="#{{ item.id }}"><span>LEAD</span><strong>Lead answer shape</strong><small>{{ item.lead_answer }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Using the matrix in discussion</p><h2>A good answer explains the business boundary before the product.</h2></div>
    <ol>
      {% for item in matrix.assessment_answer_pattern %}
      <li><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>Step {{ forloop.index }}</strong><p>{{ item }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <div>
      <p>A question such as “Can we automate supplier negotiation?” is incomplete until the scope becomes concrete. Tail-spend negotiation inside predefined commercial ranges is a very different design problem from allowing a model to create unrestricted commercial commitments.</p>
      <p>The same distinction matters elsewhere. Autonomy that is reasonable for a reversible recommendation may be inappropriate for employment decisions, safety controls, contract interpretation, or destructive security actions.</p>
    </div>
    <a href="/labs/business-ai/data/matrix.json">Open machine-readable matrix <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
