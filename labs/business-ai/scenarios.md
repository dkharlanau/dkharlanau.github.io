---
layout: default
title: "Business AI Scenarios — Successes, Mixed Results, Failures"
description: "Enterprise AI scenarios compared by process, technology, controls, outcomes, failure modes, evidence quality, and reusable lessons."
permalink: /labs/business-ai/scenarios/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - enterprise-ai
  - case-studies
  - failures
  - architecture
---

{% assign library = site.data.labs.business_ai.scenario_library %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Scenarios</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / scenario outcomes</p>
      <h1>Study what worked.<br />Study what broke.</h1>
      <p>A useful AI catalog needs failed pilots, mixed results, legal problems, biased decisions, and bad economics as much as successful customer stories. This page compares the whole operating pattern.</p>
      <a class="research-canvas__button" href="#scenario-list">Open scenarios <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Scenario set</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ library.scenarios | where: "status", "strong_pattern" | size }}</strong><small>Strong patterns</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ library.scenarios | where: "status", "mixed_result" | size }}</strong><small>Mixed results</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ library.scenarios | where: "status", "failure" | size }}</strong><small>Failures</small></div>
      <em>Failure is evidence too. It often tells us which control the success story forgot to mention.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Problem:</strong> public AI material is biased toward successful launches, while failed pilots and weak controls are harder to find.</p>
    <p><strong>Context:</strong> scenarios are classified by business process, operating boundary, evidence quality, failure mode, and lesson. A stopped pilot is not automatically a bad project; sometimes stopping is the correct control.</p>
    <a href="/labs/business-ai/practices/">Open the best-practice rules <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="scenario-list" data-reveal>
    <header><p class="research-canvas__eyebrow">Strong patterns</p><h2>Useful because the process boundary is clear.</h2><p>These are still public company or provider stories, so the evidence grade stays visible.</p></header>
    <div class="research-route-list">
      {% for item in library.scenarios %}{% if item.status == "strong_pattern" %}
      <a href="#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.process }}</strong><small>{{ item.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      {% endif %}{% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Mixed results</p><h2>The technology may work while the operating model needs correction.</h2><p>This is often more useful than a clean success story because trade-offs are visible.</p></header>
    <div class="research-route-list">
      {% for item in library.scenarios %}{% if item.status == "mixed_result" %}
      <a href="#{{ item.id }}"><span>MIX</span><strong>{{ item.company }} · {{ item.process }}</strong><small>{{ item.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      {% endif %}{% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Failures and anti-patterns</p><h2>Do not hide the expensive lessons.</h2><p>The question is not only “which model failed?” It is “which decision, control, rollout, policy, or economic assumption was wrong?”</p></header>
    <div class="research-route-list">
      {% for item in library.scenarios %}{% if item.status == "failure" %}
      <a href="#{{ item.id }}"><span>!</span><strong>{{ item.company }} · {{ item.process }}</strong><small>{{ item.failure_mode }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endif %}{% endfor %}
    </div>
  </section>

  {% for item in library.scenarios %}
  <section class="research-canvas__inventory" id="{{ item.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">{{ item.status }} / evidence {{ item.evidence_grade }}</p>
      <h2>{{ item.company }} · {{ item.process }}</h2>
      <p>{{ item.domain }}</p>
    </header>
    <div class="research-route-list">
      {% if item.what_worked %}<a href="#{{ item.id }}"><span>+</span><strong>What worked</strong><small>{{ item.what_worked }}</small><i class="material-symbols-outlined" aria-hidden="true">done</i></a>{% endif %}
      {% if item.what_changed %}<a href="#{{ item.id }}"><span>Δ</span><strong>What changed</strong><small>{{ item.what_changed }}</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>{% endif %}
      {% if item.what_failed %}<a href="#{{ item.id }}"><span>!</span><strong>What failed</strong><small>{{ item.what_failed }}</small><i class="material-symbols-outlined" aria-hidden="true">error</i></a>{% endif %}
      {% if item.what_happened %}<a href="#{{ item.id }}"><span>OBS</span><strong>What happened</strong><small>{{ item.what_happened }}</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>{% endif %}
      {% if item.reported_results %}<a href="#{{ item.id }}"><span>KPI</span><strong>Reported results</strong><small>{{ item.reported_results | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>{% endif %}
      {% if item.good_controls %}<a href="#{{ item.id }}"><span>CTRL</span><strong>Controls that helped</strong><small>{{ item.good_controls | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>{% endif %}
      {% if item.failure_mode %}<a href="#{{ item.id }}"><span>FAIL</span><strong>Failure mode</strong><small>{{ item.failure_mode }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>{% endif %}
      {% if item.missing_controls %}<a href="#{{ item.id }}"><span>MISS</span><strong>Missing controls</strong><small>{{ item.missing_controls | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>{% endif %}
      {% if item.limits %}<a href="#{{ item.id }}"><span>LIM</span><strong>Evidence limits</strong><small>{{ item.limits | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">info</i></a>{% endif %}
      <a href="#{{ item.id }}"><span>MEM</span><strong>Lesson</strong><small>{{ item.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Failure-pattern index</p><h2>Failures repeat more often than company names do.</h2><p>These patterns are meant for design reviews and assessment answers.</p></header>
    <div class="research-route-list">
      {% for item in library.failure_patterns %}
      <a href="/labs/business-ai/practices/#{{ item.id }}"><span>!</span><strong>{{ item.title }}</strong><small>{{ item.signal }} · Controls: {{ item.controls | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
