---
layout: default
title: "SAP Lead Evidence Bank — Project Story Coverage"
description: "Check the evidence problem behind SAP Lead claims through decisions, trade-offs, results, lessons, and project coverage."
permalink: /labs/interview-readiness/evidence-bank/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-19
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-evidence
  - lead-decision
  - lead-stakeholders
  - integration-ownership
tags:
  - sap
  - interview
  - evidence
  - leadership
  - project-stories
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li><a href="/labs/interview-readiness/drills/">Drills</a></li><li aria-current="page">Evidence Bank</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lead drills / Evidence Bank</p>
      <h1>A strong claim<br />needs a real story.</h1>
      <p>This page reads only the project stories already stored in your browser. It checks structural coverage, not truth. A complete story can still be unsupported, and a short story can still be well proven.</p>
      <a class="research-canvas__button" href="#coverage">Check coverage <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Lead drills"><a href="/labs/interview-readiness/stories/">Story Bank</a><a href="/labs/interview-readiness/drills/">Drills</a><a href="/labs/interview-readiness/boss-battles/">Boss Battles</a><a href="/labs/assessment/evidence-coverage/">Assessment Evidence</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Evidence structure">
      <p>Story evidence</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Role</strong><small>What you actually owned</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Decision</strong><small>What changed because of you</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Trade-off</strong><small>What cost or risk was accepted</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Result</strong><small>What outcome changed</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
    <p><strong>Evidence levels:</strong> source fact = directly visible material; supported inference = conclusion from facts; runtime proof = observed approved runtime evidence; unsupported claim = statement beyond evidence; proof gap = something still unproven.</p>
    <p><strong>Important:</strong> this page never upgrades a story to “proof” automatically. It only shows whether the story has the fields and range needed for a useful interview answer.</p>
  </section>

  <section class="research-canvas__inventory" id="coverage" data-reveal>
    <header><p class="research-canvas__eyebrow">Coverage dashboard</p><h2>Can your stories support the role you claim?</h2><p id="eb-summary">Reading browser-local stories…</p></header>
    <div class="ir-grid" id="eb-metrics"></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Capability range</p><h2>Do not make every leadership answer about the same incident.</h2><p>Coverage is inferred only from the tags you chose in Story Bank. Add clear tags such as Sales, Procurement, Integration, Architecture, Incident, Stakeholder, Leadership, AI, or Delivery.</p></header>
    <div class="ir-grid" id="eb-capabilities"></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Story review</p><h2>Find the weak evidence shape before the interview does.</h2><p>Completeness means the story has enough structure to test. It does not mean the claim is verified.</p></header>
    <div class="ir-story-list" id="eb-stories"></div>
    <div class="ir-toolbar"><a class="ir-button ir-button--primary" href="/labs/interview-readiness/stories/">Add or edit stories</a><a class="ir-button" href="/labs/assessment/evidence-coverage/">Run formal evidence review</a></div>
  </section>
</div>

<script src="/assets/js/interview-readiness.js"></script>
<script>
(() => {
  'use strict';
  const IR = window.InterviewReadiness;
  if (!IR) return;
  const stories = IR.storyBank();
  const metrics = document.getElementById('eb-metrics');
  const capabilities = document.getElementById('eb-capabilities');
  const storyList = document.getElementById('eb-stories');
  const summary = document.getElementById('eb-summary');
  const fields = ['context','role','decision','tradeoff','result','lesson'];
  const requiredForLead = ['role','decision','tradeoff','result','lesson'];
  const capabilityMap = [
    ['Sales',['sales','o2c','order','pricing','billing','atp']],
    ['Procurement',['procurement','p2p','purchasing','supplier','mm']],
    ['Integration',['integration','api','idoc','interface','event','middleware']],
    ['Architecture',['architecture','design','boundary','clean core','ewm','tm']],
    ['Incident',['incident','failure','outage','production','support','recovery']],
    ['Stakeholder',['stakeholder','conflict','business','alignment','workshop']],
    ['Leadership',['leadership','lead','mentoring','team','decision']],
    ['AI',['ai','agent','rag','automation','llm']],
    ['Delivery',['delivery','testing','release','cutover','migration','hypercare']]
  ];

  function metric(label,value,note) {
    const card = document.createElement('article'); card.className = 'ir-card';
    const kicker = document.createElement('p'); kicker.className = 'ir-kicker'; kicker.textContent = label;
    const number = document.createElement('p'); number.className = 'ir-metric'; number.textContent = value;
    const copy = document.createElement('p'); copy.className = 'ir-muted'; copy.textContent = note;
    card.append(kicker,number,copy); return card;
  }

  function has(story,field) { return Boolean(String(story[field] || '').trim()); }
  function completeness(story) { return Math.round(requiredForLead.filter(field => has(story,field)).length / requiredForLead.length * 100); }
  function tags(story) { return String(story.tags || '').toLowerCase(); }

  function renderMetrics() {
    if (!stories.length) {
      summary.textContent = 'No browser-local stories are saved yet. Start with one incident, one architecture decision, and one stakeholder conflict.';
      metrics.replaceChildren(metric('Stories','0','No project evidence stored in this browser.'),metric('Lead-complete','0%','No story can be checked yet.'),metric('Trade-offs','0','Explicit trade-offs prevent success-only stories.'),metric('Lessons','0','Lessons show how experience changed later decisions.'));
      return;
    }
    const complete = stories.filter(story => completeness(story) === 100).length;
    const tradeoffs = stories.filter(story => has(story,'tradeoff')).length;
    const lessons = stories.filter(story => has(story,'lesson')).length;
    const results = stories.filter(story => has(story,'result')).length;
    summary.textContent = `${stories.length} stories are stored in this browser. ${complete} contain role, decision, trade-off, result, and lesson.`;
    metrics.replaceChildren(
      metric('Stories',String(stories.length),'Range matters as much as depth.'),
      metric('Lead-complete',`${Math.round(complete / stories.length * 100)}%`,'Structural completeness only, not proof strength.'),
      metric('Trade-offs',`${tradeoffs}/${stories.length}`,'A decision without a cost is usually only a description.'),
      metric('Results',`${results}/${stories.length}`,'Use measured outcomes only when you can support them.'),
      metric('Lessons',`${lessons}/${stories.length}`,'Show what changed in your later behaviour.')
    );
  }

  function renderCapabilities() {
    capabilities.replaceChildren();
    capabilityMap.forEach(([label,signals]) => {
      const count = stories.filter(story => signals.some(signal => tags(story).includes(signal))).length;
      const card = document.createElement('article'); card.className = 'ir-card';
      const kicker = document.createElement('p'); kicker.className = 'ir-kicker'; kicker.textContent = label;
      const value = document.createElement('p'); value.className = 'ir-metric'; value.textContent = String(count);
      const note = document.createElement('p'); note.className = 'ir-muted'; note.textContent = count ? 'Tagged project stories available.' : 'No tagged story supports this area yet.';
      card.append(kicker,value,note); capabilities.appendChild(card);
    });
  }

  function renderStories() {
    storyList.replaceChildren();
    if (!stories.length) { const empty = document.createElement('p'); empty.className = 'ir-empty'; empty.textContent = 'No stories to review. Add stories in the browser-local Story Bank.'; storyList.appendChild(empty); return; }
    stories.forEach(story => {
      const card = document.createElement('article'); card.className = 'ir-story';
      const head = document.createElement('div'); head.className = 'ir-story__head';
      const wrap = document.createElement('div');
      const title = document.createElement('h3'); title.textContent = story.title || 'Untitled story';
      const tagLine = document.createElement('p'); tagLine.className = 'ir-muted'; tagLine.textContent = story.tags || 'No capability tags';
      wrap.append(title,tagLine);
      const score = document.createElement('span'); score.className = 'ir-pill'; score.textContent = `${completeness(story)}% structure`;
      head.append(wrap,score);
      const dl = document.createElement('dl');
      fields.forEach(field => {
        const dt = document.createElement('dt'); dt.textContent = field === 'tradeoff' ? 'Trade-off' : field.charAt(0).toUpperCase() + field.slice(1);
        const dd = document.createElement('dd'); dd.textContent = has(story,field) ? 'Present' : 'Proof gap in story structure';
        dl.append(dt,dd);
      });
      const note = document.createElement('p'); note.className = 'ir-muted';
      const missing = requiredForLead.filter(field => !has(story,field));
      note.textContent = missing.length ? `Next improvement: add ${missing.join(', ')}.` : 'Structure is complete. Next check whether each claim is supported by evidence you can discuss safely.';
      card.append(head,dl,note); storyList.appendChild(card);
    });
  }

  renderMetrics(); renderCapabilities(); renderStories();
})();
</script>
