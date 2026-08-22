---
layout: default
title: "SAP Lead Interview Progress — Readiness and Weak Areas"
description: "Track SAP Lead interview problems in context with roadmap depth, track coverage, recent practice, weak areas, and project story evidence."
permalink: /labs/interview-readiness/progress/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-18
hide_global_cta: true
tags:
  - sap
  - interview
  - progress
  - sap-lead
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li aria-current="page">Progress</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Interview Readiness / Progress</p>
      <h1>See the gap.<br />Change the next session.</h1>
      <p>Progress is useful when it changes your preparation. This view combines roadmap depth with recent Interview Mode sessions and shows where confidence is still thin.</p>
      <a class="research-canvas__button" href="#progress-summary">Open progress <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Interview Readiness sections"><a href="/labs/interview-readiness/">Dashboard</a><a href="/labs/interview-readiness/roadmap/">Roadmap</a><a href="/labs/interview-readiness/questions/">Questions</a><a href="/labs/interview-readiness/stories/">Stories</a><a href="/labs/interview-readiness/practice/">Practice</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Progress model">
      <p>Two signals</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Roadmap</strong><small>What depth you report by topic</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Practice</strong><small>How mixed interview answers went</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Stories</strong><small>Whether evidence is ready</small></div>
      <em>All three stay local to this browser.</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="progress-summary" data-reveal>
    <header><p class="research-canvas__eyebrow">Summary</p><h2>Readiness is depth plus coverage.</h2><p>One strong topic cannot compensate for an untouched track when the role crosses Sales, Logistics, Integration, AI, and leadership decisions.</p></header>
    <div class="ir-grid" id="ir-progress-summary"></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Track coverage</p><h2>Where the roadmap is solid, and where it is mostly optimism.</h2><p>Readiness is weighted from Not reviewed to Can defend. “Can explain” is useful. “Can defend” is the stronger Lead signal.</p></header>
    <div style="overflow-x:auto"><table class="ir-progress-table"><thead><tr><th>Track</th><th>Readiness</th><th>Not reviewed</th><th>Refreshed</th><th>Can explain</th><th>Can defend</th></tr></thead><tbody id="ir-track-table"></tbody></table></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Weakest topics</p><h2>Review the first five before polishing what is already comfortable.</h2><p>Weak areas are sorted by roadmap depth. Use the source link, then answer one question out loud before changing the status.</p></header>
    <div class="ir-topic-list" id="ir-weak-topics"></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Recent Interview Mode</p><h2>Mixed practice should expose cross-track weakness.</h2><p>This is a self-rating, not a certification. Use it as a signal for what to review next.</p></header>
    <div id="ir-practice-history"></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Assessment connection</p><h2>Use the right progress view for the right question.</h2><p>Interview Readiness tracks recall, explanation, defence, and interview stories. The Assessment Lab tracks scored reasoning dimensions and case attempts.</p></header>
    <div class="research-route-list">
      <a href="/labs/assessment/progress/"><span>ASSESS</span><strong>Assessment Progress</strong><small>Reasoning dimensions, track coverage, scored attempts, and portable history.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>
      <a href="/labs/assessment/review/"><span>REVIEW</span><strong>Assessment Review Queue</strong><small>Turn weak dimensions and weak tracks into focused study routes.</small><i class="material-symbols-outlined" aria-hidden="true">target</i></a>
      <a href="/labs/interview-readiness/stories/"><span>STORY</span><strong>Interview Story Bank</strong><small>Prepare the project evidence that a score cannot provide.</small><i class="material-symbols-outlined" aria-hidden="true">history_edu</i></a>
    </div>
  </section>
</div>

<script src="/assets/js/interview-readiness.js?v={{ site.time | date: '%s' }}"></script>
<script>
(() => {
  'use strict';
  const IR = window.InterviewReadiness;
  if (!IR) return;
  const summaryEl = document.getElementById('ir-progress-summary');
  const table = document.getElementById('ir-track-table');
  const weak = document.getElementById('ir-weak-topics');
  const historyEl = document.getElementById('ir-practice-history');

  function render() {
    const data = IR.summary();
    const practice = IR.practiceHistory();
    const stories = IR.storyBank();
    const latest = practice[0];
    summaryEl.replaceChildren();
    [
      ['Roadmap readiness',data.overall + '%',`${IR.TOPICS.length - data.statuses['not-reviewed']} of ${IR.TOPICS.length} topics touched`],
      ['Interview sessions',String(practice.length),latest ? `Latest: ${latest.percent}%` : 'No mixed session saved yet'],
      ['Prepared stories',String(stories.length),stories.length ? 'Browser-local story evidence' : 'Add incident, decision, and conflict stories']
    ].forEach(([label,value,detail]) => {
      const card = document.createElement('article'); card.className = 'ir-card';
      card.innerHTML = `<p class="ir-kicker">${label}</p><p class="ir-metric">${value}</p><p class="ir-muted">${detail}</p>`;
      summaryEl.appendChild(card);
    });

    table.replaceChildren();
    Object.entries(IR.TRACKS).forEach(([track,label]) => {
      const items = IR.TOPICS.filter(topic => topic.track === track);
      const counts = Object.fromEntries(IR.STATUSES.map(status => [status.id,items.filter(topic => IR.getStatus(topic.id) === status.id).length]));
      const tr = document.createElement('tr');
      [label,IR.readinessFor(items)+'%',counts['not-reviewed'],counts['refreshed'],counts['explain'],counts['defend']].forEach(value => { const td = document.createElement('td'); td.textContent = value; tr.appendChild(td); });
      table.appendChild(tr);
    });

    weak.replaceChildren();
    data.weak.slice(0,7).forEach(topic => {
      const status = IR.statusObject(topic.id);
      const row = document.createElement('article'); row.className = 'ir-topic';
      row.innerHTML = `<div class="ir-topic__copy"><strong>${topic.title}</strong><small>${IR.TRACKS[topic.track]} · ${topic.why}</small></div><div class="ir-topic__actions"><span class="ir-pill">${status.label}</span><a class="ir-link" href="${topic.href}">Review <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a></div>`;
      weak.appendChild(row);
    });

    historyEl.replaceChildren();
    if (!practice.length) {
      const empty = document.createElement('p'); empty.className = 'ir-empty'; empty.innerHTML = 'No Interview Mode sessions saved yet. <a href="/labs/interview-readiness/practice/">Run a balanced session</a>.'; historyEl.appendChild(empty);
      return;
    }
    const wrap = document.createElement('div'); wrap.style.overflowX = 'auto';
    const t = document.createElement('table'); t.className = 'ir-progress-table';
    t.innerHTML = '<thead><tr><th>Date</th><th>Overall</th><th>Sales</th><th>Logistics</th><th>Integration</th><th>AI</th><th>Lead</th></tr></thead>';
    const body = document.createElement('tbody');
    practice.slice(0,10).forEach(row => {
      const tr = document.createElement('tr');
      const date = new Date(row.attempted_at);
      const values = [Number.isNaN(date.getTime()) ? 'Unknown' : date.toLocaleDateString(),row.percent+'%'];
      ['sales','logistics','integration','ai','leadership'].forEach(track => { const value = row.track_scores && row.track_scores[track]; values.push(value == null ? '—' : Math.round(value/2*100)+'%'); });
      values.forEach(value => { const td = document.createElement('td'); td.textContent = value; tr.appendChild(td); });
      body.appendChild(tr);
    });
    t.appendChild(body); wrap.appendChild(t); historyEl.appendChild(wrap);
  }

  render();
  window.addEventListener('interview-readiness-change', render);
})();
</script>
