---
layout: default
title: "SAP Lead Contrast Lab — Distinguish the Right Boundary"
description: "Objective SAP Lead practice for confusable process, integration and AI boundaries, with confidence and explanatory feedback."
permalink: /labs/interview-readiness/contrast/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-26
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-answer
  - delivery-memory
  - delivery-testing
tags:
  - sap-lead
  - interview-readiness
  - interleaving
  - discrimination
  - learning-science
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />
<link rel="stylesheet" href="/assets/css/contrast-lab.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li aria-current="page">Contrast Lab</li></ol></nav>

<div class="research-canvas ir-shell contrast-lab" id="contrast-lab">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Interview Readiness / Contrast Engine</p>
      <h1>Similar words.<br />Different decision.</h1>
      <p>Lead-level mistakes often come from choosing the wrong model too early. This Lab mixes boundaries that look related and asks one objective question: which model should lead the next decision?</p>
      <a class="research-canvas__button" href="#contrast-session">Start contrast session <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Learning system sections"><a href="/labs/interview-readiness/today/">Mastery Today</a><a href="/labs/interview-readiness/memory-atlas/">Memory Atlas</a><a href="/labs/interview-readiness/learning-science/">Learning Science</a><a href="/labs/assessment/practice-engine/">Assessment Practice</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Contrast loop">
      <p>Contrast loop</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Classify</strong><small>Choose the model before feedback</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Calibrate</strong><small>Commit confidence with the choice</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Explain</strong><small>Read why the boundary matters</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Interleave</strong><small>Switch to another confusable pair</small></div>
      <em>Answers are scored automatically. History stays in this browser.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span>
    <p><strong>Context:</strong> use this after basic recall. Interleaving is most useful here because the task is to discriminate between related models, not to make random practice feel difficult.</p>
    <p><strong>Evidence:</strong> the system stores choice correctness, confidence, pair and timestamp. It does not store free-text answers because this mode does not need them.</p>
  </section>

  <section class="research-canvas__inventory" id="contrast-position" data-reveal>
    <header><p class="research-canvas__eyebrow">Discrimination position</p><h2>Measure wrong-boundary risk directly.</h2><p>Accuracy shows whether the distinction is understood. Calibration shows whether confidence matches the objective result.</p></header>
    <div class="contrast-metrics" id="ct-metrics" aria-label="Contrast metrics"></div>
    <div class="contrast-pairs" id="ct-pair-summary" aria-label="Contrast pair results"></div>
  </section>

  <section class="research-canvas__inventory" id="contrast-session" data-reveal>
    <header><p class="research-canvas__eyebrow">Blind classification</p><h2 id="ct-title">Choose a contrast item.</h2><p id="ct-meta">Unseen and weak pairs are rotated without repeating the same pair back-to-back.</p></header>
    <article class="contrast-card" id="ct-card" hidden>
      <p class="contrast-prompt" id="ct-prompt"></p>

      <div class="contrast-confidence">
        <div><p class="ir-kicker">Confidence</p><strong id="ct-confidence-value">50%</strong></div>
        <label for="ct-confidence">How sure are you about the boundary?</label>
        <input id="ct-confidence" type="range" min="0" max="100" step="5" value="50" />
      </div>

      <div class="contrast-choice-grid" id="ct-choices"></div>

      <div class="contrast-feedback" id="ct-feedback" hidden aria-live="polite">
        <p class="ir-kicker" id="ct-result-label"></p>
        <h3 id="ct-result-title"></h3>
        <p id="ct-explanation"></p>
        <p><strong>Discriminator:</strong> <span id="ct-discriminator"></span></p>
        <p><strong>If confused:</strong> <span id="ct-failure"></span></p>
        <div class="contrast-source-links" id="ct-sources"></div>
        <button type="button" class="ir-button ir-button--primary" id="ct-next">Next contrast</button>
      </div>
    </article>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Pair bank</p><h2>What the engine deliberately mixes.</h2><p>These are decision boundaries, not vocabulary pairs. Each pair links back to the Career skills and source Labs that explain the models.</p></header>
    <div class="ir-grid">
      {% for pair in site.data.career.contrast.pairs %}
      <article class="ir-card"><p class="ir-kicker">{{ pair.left.label }} / {{ pair.right.label }}</p><h3>{{ pair.title }}</h3><p>{{ pair.discriminator }}</p><p class="contrast-pair-links"><a href="{{ pair.left.source }}">{{ pair.left.skill_id }}</a><span aria-hidden="true">·</span><a href="{{ pair.right.source }}">{{ pair.right.skill_id }}</a></p></article>
      {% endfor %}
    </div>
  </section>
</div>

<script id="contrast-data" type="application/json">{{ site.data.career.contrast | jsonify }}</script>
<script src="/assets/js/contrast-lab.js"></script>
