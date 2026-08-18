---
layout: default
title: "SAP Lead Interview Roadmap — Sales, Logistics, Integration, AI"
description: "A browser-local SAP Lead interview roadmap for Sales, Procurement and Logistics, Integration and Architecture, AI and Data, and Lead judgment."
permalink: /labs/interview-readiness/roadmap/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-18
hide_global_cta: true
tags:
  - sap
  - interview
  - roadmap
  - sap-lead
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li aria-current="page">Roadmap</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Interview Readiness / Roadmap</p>
      <h1>Track depth,<br />not page views.</h1>
      <p>Use the roadmap to record the level you can actually demonstrate. Reading a page is useful. Explaining it without notes is better. Defending the design when somebody disagrees is the Lead test.</p>
      <a class="research-canvas__button" href="#roadmap">Open roadmap <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Interview Readiness sections"><a href="/labs/interview-readiness/">Dashboard</a><a href="/labs/interview-readiness/questions/">Questions</a><a href="/labs/interview-readiness/stories/">Stories</a><a href="/labs/interview-readiness/practice/">Practice</a><a href="/labs/interview-readiness/progress/">Progress</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Roadmap states">
      <p>Topic states</p>
      <div class="research-canvas__signal-line"><span>0</span><strong>Not reviewed</strong><small>No recent confidence</small></div>
      <div class="research-canvas__signal-line"><span>1</span><strong>Refreshed</strong><small>Model rebuilt</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Can explain</strong><small>Clear answer without notes</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Can defend</strong><small>Trade-offs and follow-ups</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">touch_app</span>
    <p><strong>How to use it:</strong> click a status to move the topic to the next level. Open the source when the model is weak. The state stays in localStorage in this browser.</p>
    <p><strong>Do not game the percentage.</strong> Mark “Can defend” only if you can answer the obvious follow-up: why this design, what can fail, and what would you challenge?</p>
  </section>

  <section class="research-canvas__inventory" id="roadmap" data-reveal>
    <header><p class="research-canvas__eyebrow">Roadmap</p><h2 id="ir-roadmap-title">Five tracks. One preparation map.</h2><p>Filter by track or status when you need a focused review session.</p></header>
    <div class="ir-toolbar">
      <div class="ir-filter" id="ir-track-filter" aria-label="Filter by track"></div>
      <button type="button" id="ir-reset">Reset local roadmap</button>
    </div>
    <div class="ir-grid" id="ir-roadmap-summary" aria-label="Roadmap summary"></div>
  </section>

  <div id="ir-track-sections"></div>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Next step</p><h2>Turn a green topic into an answer under pressure.</h2><p>The roadmap measures self-reported depth. Use questions and mock practice to find out whether that confidence survives follow-up pressure.</p></header>
    <div class="research-route-list">
      <a href="/labs/interview-readiness/questions/"><span>Q</span><strong>Question Bank</strong><small>Explain, trace, diagnose, design, and challenge across the five tracks.</small><i class="material-symbols-outlined" aria-hidden="true">quiz</i></a>
      <a href="/labs/interview-readiness/practice/"><span>30</span><strong>Interview Mode</strong><small>A balanced session with ten questions and a simple self-rating.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="/labs/assessment/practice-engine/"><span>ADAPT</span><strong>Adaptive Assessment Practice</strong><small>Use the existing assessment engine when you want case scoring across reasoning dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
    </div>
  </section>
</div>

<script src="/assets/js/interview-readiness.js"></script>
<script>
(() => {
  'use strict';
  const IR = window.InterviewReadiness;
  if (!IR) return;
  const filters = document.getElementById('ir-track-filter');
  const sections = document.getElementById('ir-track-sections');
  const summary = document.getElementById('ir-roadmap-summary');
  const reset = document.getElementById('ir-reset');
  let activeTrack = 'all';

  function makeFilter(id,label) {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = label;
    button.dataset.track = id;
    button.setAttribute('aria-pressed', id === activeTrack ? 'true' : 'false');
    button.addEventListener('click', () => { activeTrack = id; render(); });
    return button;
  }

  function renderFilters() {
    filters.replaceChildren();
    filters.appendChild(makeFilter('all','All tracks'));
    Object.entries(IR.TRACKS).forEach(([id,label]) => filters.appendChild(makeFilter(id,label)));
  }

  function renderSummary() {
    summary.replaceChildren();
    const data = IR.summary();
    const overall = document.createElement('article');
    overall.className = 'ir-card';
    overall.innerHTML = `<p class="ir-kicker">Overall</p><p class="ir-metric">${data.overall}%</p><p class="ir-muted">Weighted by topic depth.</p>`;
    summary.appendChild(overall);
    Object.entries(data.tracks).forEach(([id,track]) => {
      if (activeTrack !== 'all' && activeTrack !== id) return;
      const card = document.createElement('article');
      card.className = 'ir-card ir-track';
      card.innerHTML = `<div class="ir-track__head"><strong>${track.label}</strong><span>${track.readiness}%</span></div><div class="ir-track__bar"><span style="width:${track.readiness}%"></span></div><small>${track.count} topics</small>`;
      summary.appendChild(card);
    });
  }

  function renderSections() {
    sections.replaceChildren();
    Object.entries(IR.TRACKS).forEach(([trackId,label]) => {
      if (activeTrack !== 'all' && activeTrack !== trackId) return;
      const wrapper = document.createElement('section');
      wrapper.className = 'research-canvas__inventory';
      wrapper.id = trackId;
      wrapper.dataset.reveal = '';
      const items = IR.TOPICS.filter(topic => topic.track === trackId);
      wrapper.innerHTML = `<header><p class="research-canvas__eyebrow">${label}</p><h2>${label}</h2><p>${items.length} interview topics. Open the source only when you need it; the goal is a usable answer, not ceremonial browsing.</p></header>`;
      const list = document.createElement('div');
      list.className = 'ir-topic-list';
      items.forEach(topic => {
        const status = IR.statusObject(topic.id);
        const row = document.createElement('article');
        row.className = 'ir-topic';
        row.dataset.topic = topic.id;
        row.innerHTML = `<div class="ir-topic__copy"><strong>${topic.title}</strong><small>${topic.why}</small></div><div class="ir-topic__actions"><button class="ir-status" type="button" data-topic="${topic.id}" data-level="${status.score}" aria-label="Change status for ${topic.title}">${status.label}</button><a class="ir-link" href="${topic.href}">Source <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a></div>`;
        list.appendChild(row);
      });
      wrapper.appendChild(list);
      sections.appendChild(wrapper);
    });
    sections.querySelectorAll('.ir-status').forEach(button => button.addEventListener('click', () => { IR.cycleStatus(button.dataset.topic); renderSummary(); renderSections(); }));
  }

  function render() { renderFilters(); renderSummary(); renderSections(); }
  reset.addEventListener('click', () => {
    if (window.confirm('Reset all Interview Readiness topic states in this browser?')) IR.resetReadiness();
  });
  window.addEventListener('interview-readiness-change', render);
  render();
})();
</script>
