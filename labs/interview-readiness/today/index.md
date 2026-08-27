---
layout: default
title: "SAP Lead Mastery Today — Recall, Apply, Retain"
description: "A retrieval-first SAP Lead practice session for Sales, Logistics, Integration and AI, focused on recall, application, defence and delayed retention."
permalink: /labs/interview-readiness/today/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-20
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-answer
  - delivery-memory
  - delivery-testing
tags:
  - sap
  - sap-lead
  - interview-readiness
  - retrieval-practice
  - mastery
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />
<link rel="stylesheet" href="/assets/css/mastery-today.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li aria-current="page">Mastery Today</li></ol></nav>

<div class="research-canvas ir-shell mastery-today" id="mastery-today">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Interview Readiness / Mastery Loop</p>
      <h1>Close the notes.<br />Build the answer.</h1>
      <p>Reading creates familiarity. This session checks whether the useful model can be rebuilt from memory, connected to neighbouring processes, applied to a new case, and defended under challenge.</p>
      <a class="research-canvas__button" href="#session">Start today's session <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Interview Readiness sections"><a href="/labs/interview-readiness/">Dashboard</a><a href="/labs/interview-readiness/contrast/">Contrast Lab</a><a href="/labs/interview-readiness/memory-atlas/">Memory Atlas</a><a href="/labs/interview-readiness/learning-science/">Learning Science</a><a href="/labs/interview-readiness/roadmap/">Career Roadmap</a><a href="/labs/assessment/practice-engine/">Assessment Practice</a><a href="/labs/assessment/progress/">Assessment Progress</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Mastery loop">
      <p>Mastery loop</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Recall</strong><small>Rebuild the Five-Link model</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Connect</strong><small>Place it in the wider process</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Apply</strong><small>Use it in a new scenario</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Defend</strong><small>Handle a Lead-level challenge</small></div>
      <div class="research-canvas__signal-line"><span>05</span><strong>Retain</strong><small>Retrieve it again after time</small></div>
      <em>Progress stays in this browser.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology_alt</span>
    <p><strong>Context:</strong> use this after studying a Lab or roadmap skill, when you need to test retrieval instead of rereading.</p>
    <p><strong>Rule:</strong> answer and commit confidence before you reveal the reference. Familiarity is not evidence that you can retrieve the model in an assessment.</p>
    <p><strong>Scheduler:</strong> same-session success can repair fluency but does not advance the spacing stage. A stage grows only after a successful retrieval separated by a real delay.</p>
    <p><strong>Scoring:</strong> self-score is a practice signal, not certification. Use Contrast Lab, Assessment Practice and human review when you need stronger evidence.</p>
  </section>

  <section class="research-canvas__inventory" id="position" data-reveal>
    <header><p class="research-canvas__eyebrow">Learning position</p><h2>Track retrieval, retention and calibration.</h2><p>The learning state is separate from the professional capability target in the Career Roadmap. Confidence is also separate from performance.</p></header>
    <div class="mastery-metrics" id="mt-metrics" aria-label="Mastery metrics"></div>
    <div class="mastery-state-strip" id="mt-state-strip" aria-label="Mastery states"></div>
  </section>

  <section class="research-canvas__inventory" id="session" data-reveal>
    <header><p class="research-canvas__eyebrow">Today</p><h2>Five useful retrievals. Due work first.</h2><p>The selector prioritises overdue reviews, weak results, new coverage, and track diversity. A weak or high-mismatch answer returns after intervening items instead of repeating immediately.</p></header>
    <div class="mastery-session" id="mt-session"></div>
  </section>

  <section class="research-canvas__inventory" id="practice" data-reveal>
    <header><p class="research-canvas__eyebrow">Cold recall</p><h2 id="mt-title">Choose a session item.</h2><p id="mt-meta">Your prompt will appear here.</p></header>
    <article class="mastery-practice-card" id="mt-card" hidden>
      <div class="mastery-practice-card__top"><span id="mt-track"></span><span id="mt-mode"></span><span id="mt-state"></span></div>
      <h3 id="mt-prompt-title">Your task</h3>
      <p class="mastery-prompt" id="mt-prompt"></p>
      <label class="mastery-answer">Build the answer before reveal
        <textarea id="mt-answer" rows="7" maxlength="6000" placeholder="Use short notes. The text is not saved to history."></textarea>
      </label>

      <div class="mastery-confidence">
        <div><p class="ir-kicker">Confidence before feedback</p><strong id="mt-confidence-value">50%</strong></div>
        <label for="mt-confidence">How likely is your answer to survive the reference?</label>
        <input id="mt-confidence" type="range" min="0" max="100" step="5" value="50" />
        <small>Set this before reveal. The value is stored with the score so calibration can be measured later.</small>
      </div>

      <div class="mastery-actions"><button class="ir-button ir-button--primary" type="button" id="mt-reveal">Commit confidence and reveal</button><a class="ir-button" id="mt-source" href="#" hidden>Open source</a></div>
      <div class="mastery-reference" id="mt-reference" hidden>
        <div class="mastery-five-link" id="mt-five-link"></div>

        <div class="mastery-repair">
          <div><p class="ir-kicker">Mismatch repair</p><h3>What changed in your model?</h3><p>Do not only notice that the answer was different. Name the missing rule, boundary, owner, evidence or decision.</p></div>
          <label for="mt-mismatch">Mismatch strength
            <select id="mt-mismatch">
              <option value="0">Expected — the reference matched my model</option>
              <option value="1">Some mismatch — one useful part was missing</option>
              <option value="2">Major mismatch — an important rule or boundary was wrong</option>
            </select>
          </label>
          <label class="mastery-answer" for="mt-repair-note">Explain the mismatch
            <textarea id="mt-repair-note" rows="3" maxlength="1200" placeholder="One short explanation. This text is not saved to history."></textarea>
          </label>
          <p class="mastery-repair-status" id="mt-repair-status" aria-live="polite"></p>
        </div>

        <div class="mastery-score-panel">
          <div><p class="ir-kicker">Self-score</p><h3>How much existed before reveal?</h3><p>Score the answer you produced, not how familiar the reference looks now. A weak or major-mismatch attempt enters delayed repair.</p></div>
          <div class="mastery-score-buttons" id="mt-score-buttons"></div>
        </div>
      </div>
    </article>
  </section>

  <section class="research-canvas__inventory" id="profile" data-reveal>
    <header><p class="research-canvas__eyebrow">Retention evidence</p><h2>Let old knowledge become due again.</h2><p>Retained means successful defence or review retrievals across time after the most recent lapse. A new lapse removes retained status until delayed retrieval rebuilds the evidence. Calibration remains a separate signal.</p></header>
    <div class="mastery-profile" id="mt-profile"></div>
    <div class="mastery-actions"><button type="button" class="ir-button" id="mt-export">Export mastery history</button><button type="button" class="ir-button" id="mt-clear">Clear mastery history</button></div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Discrimination:</strong> the <a href="/labs/interview-readiness/contrast/">Contrast Lab</a> tests whether you can choose between confusable models such as stock versus ATP availability or retrieval failure versus evaluation failure.</p>
    <p><strong>Process reconstruction:</strong> Five-Link recall tests one skill. The <a href="/labs/interview-readiness/memory-atlas/">Memory Atlas</a> tests whether you can rebuild the O2C, P2P, and integration spine and explain the ownership hand-offs between nodes.</p>
    <p><strong>Research contract:</strong> the <a href="/labs/interview-readiness/learning-science/">Learning Science Lab</a> records which learning mechanics are supported, where evidence is conditional, and which claims we deliberately avoid.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">How the memory card works</p><h2>Compress a topic into five links.</h2><p>The five links are small enough to rebuild from memory but rich enough to support diagnosis and Lead-level discussion.</p></header>
    <div class="ir-grid">
      <article class="ir-card"><p class="ir-kicker">01 / Trigger</p><h3>Why does this mechanism exist?</h3><p>Start with the business job, not the SAP object.</p></article>
      <article class="ir-card"><p class="ir-kicker">02 / Flow</p><h3>What state changes next?</h3><p>Keep the main process or architecture sequence visible.</p></article>
      <article class="ir-card"><p class="ir-kicker">03 / Objects & rules</p><h3>What controls the decision?</h3><p>Name only the objects and rules that explain behaviour.</p></article>
      <article class="ir-card"><p class="ir-kicker">04 / Failure boundary</p><h3>Where can expected state diverge?</h3><p>Separate symptoms from the first useful diagnostic boundary.</p></article>
      <article class="ir-card"><p class="ir-kicker">05 / Lead decision</p><h3>What should a Lead decide?</h3><p>Finish with ownership, evidence, trade-off, recovery, or change.</p></article>
    </div>
  </section>
</div>

<script id="mastery-data" type="application/json">{{ site.data.career.mastery | jsonify }}</script>
<script id="scheduler-data" type="application/json">{{ site.data.career.scheduler | jsonify }}</script>
<script src="/assets/js/mastery-today.js"></script>