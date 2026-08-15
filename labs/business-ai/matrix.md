---
layout: default
title: "Business AI Assessment Matrix — Process, Autonomy, Risk, KPI"
description: "Lead-level Business AI decision matrix linking process, AI job, reusable pattern, autonomy, risk, KPI, controls, failure patterns, and public evidence."
permalink: /labs/business-ai/matrix/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
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
      <p class="research-canvas__eyebrow">Business AI / lead assessment matrix</p>
      <h1>Do not ask only<br />“Can AI do it?”</h1>
      <p>Ask what the process is, what can go wrong, who owns the business truth, how much autonomy is acceptable, and which KPI proves value. This matrix turns those questions into a repeatable architecture method.</p>
      <a class="research-canvas__button" href="#profiles">Open the matrix <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Decision framework</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ matrix.profiles | size }}</strong><small>Scenario profiles</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ matrix.autonomy_levels | size }}</strong><small>Autonomy levels</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ matrix.decision_rules | size }}</strong><small>Architecture rules</small></div>
      <em>Model capability is not business authority.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Problem:</strong> AI discussions often jump from a possible capability to automation without stating the consequence of a wrong action, the business authority boundary, or the KPI that should improve.</p>
    <p><strong>Context:</strong> the same model can be safe as an assistant in one process and unsafe as an autonomous actor in another. This matrix compares decisions by process, autonomy, risk, authority, controls, evidence, and business result.</p>
    <p><strong>Working rule:</strong> {{ matrix.reading_rule }}</p>
    <p><strong>Assessment use:</strong> start from a process step, choose the AI job, then explain autonomy, risk, KPI, system authority, controls, and evidence. A product name comes after that.</p>
    <p><strong>Lead signal:</strong> a strong answer can explain why two technically similar AI solutions need different autonomy because the cost of a wrong action is different.</p>
    <a href="/labs/business-ai/scenarios/">Compare with scenario evidence <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="autonomy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Autonomy scale</p>
      <h2>Separate assistance from authority.</h2>
      <p>“Human in the loop” is too vague. Use a concrete autonomy level and name the control boundary.</p>
    </header>
    <div class="research-route-list">
      {% for level in matrix.autonomy_levels %}
      <a href="#autonomy"><span>{{ level.id }}</span><strong>{{ level.label }}</strong><small>{{ level.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Decision rules</p><h2>Eight rules before choosing autonomy.</h2></div>
    <ol>
      {% for item in matrix.decision_rules %}
      <li><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>{{ item.id | replace: 'dr-', '' | replace: '-', ' ' | capitalize }}</strong><p>{{ item.rule }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__inventory" id="profiles" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scenario matrix</p>
      <h2>{{ matrix.profiles | size }} decision profiles.</h2>
      <p>Each profile is a compact assessment answer: process → AI job → autonomy → risk → KPI → authority → controls → failure pattern → evidence.</p>
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
    <div><p class="research-canvas__eyebrow">Assessment answer pattern</p><h2>A seven-step answer that works across domains.</h2></div>
    <ol>
      {% for item in matrix.assessment_answer_pattern %}
      <li><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>Step {{ forloop.index }}</strong><p>{{ item }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Example:</strong> “Can we automate supplier negotiation?” is not yet an architecture question. A stronger answer is: tail-spend negotiation, predefined commercial ranges, L4 guardrailed autonomy, procurement system as authority, supplier and out-of-policy KPIs, audit plus escalation, and Walmart/Pactum as directional evidence.</p>
    <p><strong>Counter-example:</strong> the same L4 autonomy would be a poor default for employment decisions, safety rules, contract interpretation, or security actions with destructive side effects.</p>
    <a href="/labs/business-ai/data/matrix.json">Open machine-readable matrix <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
