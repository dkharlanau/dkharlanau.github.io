---
layout: default
title: "TRIZ SAP Lead Drill"
description: "A 90-second assessment drill for SAP Sales, Procurement, Logistics, Integration, Master Data, and AI using contradiction-driven reasoning."
permalink: /triz/drill/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, sap, assessment, lead, sales, procurement, logistics, integration, master-data, ai]
---

<link rel="stylesheet" href="/assets/triz-drill.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">SAP Lead Drill</li></ol>
</nav>

<div class="triz-drill" data-triz-drill>
  <header class="triz-drill__hero">
    <div class="triz-drill__hero-copy">
      <p class="triz-drill__eyebrow">TRIZ / SAP Lead assessment drill</p>
      <h1>Think like a Lead.<br />Before the timer wins.</h1>
      <p>Take one synthetic enterprise problem and answer it in 60–90 seconds. The drill rewards business framing, contradictions, different system shapes, ownership, evidence, and a testable recommendation. Product names alone earn very little sympathy.</p>
    </div>
    <aside class="triz-drill__hero-note">
      <p class="triz-drill__eyebrow">Practice boundary</p>
      <p><strong>18 synthetic cases.</strong> Sales, Procurement, Logistics, Integration, Master Data, and AI. The page does not call an AI model and does not submit your answer to this site.</p>
      <p>Do not paste client names, internal IDs, proprietary configuration, credentials, or confidential process details.</p>
    </aside>
  </header>

  <section class="triz-drill__controls" aria-label="Drill filters">
    <div class="triz-drill__controls-grid">
      <div class="triz-drill__field">
        <label for="drill-domain">Domain</label>
        <select id="drill-domain" data-drill-domain>
          <option value="">All domains</option>
          <option value="sales">Sales</option>
          <option value="procurement">Procurement</option>
          <option value="logistics">Logistics</option>
          <option value="integration">Integration</option>
          <option value="master_data">Master Data</option>
          <option value="ai">AI / Agents</option>
        </select>
      </div>
      <div class="triz-drill__field">
        <label for="drill-difficulty">Difficulty</label>
        <select id="drill-difficulty" data-drill-difficulty>
          <option value="">All levels</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
      </div>
      <button class="triz-drill__button" type="button" data-drill-new>New case</button>
    </div>
    <p class="triz-drill__meta" data-drill-status aria-live="polite">Loading assessment data…</p>
  </section>

  <section class="triz-drill__stage" aria-labelledby="drill-case-title">
    <article class="triz-drill__case">
      <header class="triz-drill__case-head">
        <div>
          <p class="triz-drill__eyebrow">Current case</p>
          <h2 id="drill-case-title" data-drill-title>Loading case…</h2>
        </div>
        <div class="triz-drill__case-tags" data-drill-meta></div>
      </header>

      <p class="triz-drill__prompt" data-drill-prompt>The case dataset is loading.</p>

      <div class="triz-drill__pressure" data-drill-pressure hidden>
        <strong>Interviewer pressure</strong>
        <div data-drill-pressure-list></div>
      </div>

      <div class="triz-drill__actions">
        <button class="triz-drill__button triz-drill__button--secondary" type="button" data-drill-pressure-button>Show interviewer pressure</button>
      </div>

      <div class="triz-drill__answer">
        <div class="triz-drill__answer-head">
          <div>
            <p class="triz-drill__eyebrow">Your answer</p>
            <strong>Use the Lead spine, not a feature list.</strong>
          </div>
          <small data-drill-count>0 characters</small>
        </div>
        <textarea data-drill-answer aria-label="Your 60 to 90 second Lead answer" placeholder="I would first frame the useful function and the evidence. The contradiction is…"></textarea>
        <div class="triz-drill__actions">
          <button class="triz-drill__button" type="button" data-drill-reveal>Reveal debrief</button>
        </div>
      </div>
    </article>

    <aside class="triz-drill__timer" aria-label="90 second practice timer">
      <p class="triz-drill__timer-label">Assessment clock</p>
      <div class="triz-drill__clock" data-drill-timer>1:30</div>
      <p>A useful answer usually fits one spine: problem → contradiction → separation → options → ownership → evidence and experiment.</p>
      <div class="triz-drill__timer-actions">
        <button class="triz-drill__button" type="button" data-drill-timer-start>Start</button>
        <button class="triz-drill__button triz-drill__button--secondary" type="button" data-drill-timer-reset>Reset</button>
      </div>
    </aside>
  </section>

  <section class="triz-drill__debrief" data-drill-debrief hidden aria-labelledby="drill-debrief-title">
    <header>
      <div>
        <p class="triz-drill__eyebrow">Debrief</p>
        <h2 id="drill-debrief-title">Compare the reasoning, not the wording.</h2>
      </div>
      <p>A strong answer does not need to copy this outline. It should show the same kinds of judgment: protect the useful function, expose both useful sides of the conflict, create design distance, allocate authority, and name evidence that could prove you wrong.</p>
    </header>
    <div class="triz-drill__debrief-grid" data-drill-debrief-grid></div>
  </section>

  <section class="triz-drill__rubric" data-drill-rubric hidden aria-labelledby="drill-rubric-title">
    <header>
      <div>
        <p class="triz-drill__eyebrow">Lead rubric</p>
        <h2 id="drill-rubric-title">Score the answer you actually gave.</h2>
      </div>
      <p>Six dimensions, four points each. The score is deliberately about reasoning and communication, not whether you guessed the same product choice as the reference case.</p>
    </header>

    <div class="triz-drill__rubric-grid" data-drill-rubric-grid></div>

    <div class="triz-drill__score">
      <div>
        <p class="triz-drill__score-label">Self score</p>
        <div class="triz-drill__score-value" data-drill-score>0/24</div>
      </div>
      <div class="triz-drill__score-copy">
        <h3 data-drill-band>Narrow solution answer</h3>
        <p data-drill-band-copy>Score the rubric to see the current band.</p>
      </div>
    </div>

    <div class="triz-drill__machine">
      <p class="triz-drill__eyebrow">Agent evaluation payload</p>
      <h3>Same case. Same rubric. Less self-deception.</h3>
      <p>Copy this JSON into the assessment agent. It contains the case, your answer, the rubric, your self-score, and the expected evaluator output. The evaluator should judge reasoning, not keyword overlap.</p>
      <div class="triz-drill__actions">
        <button class="triz-drill__button" type="button" data-drill-copy-payload>Copy agent evaluation payload</button>
      </div>
      <pre data-drill-payload tabindex="0" aria-label="Agent evaluation payload"></pre>
    </div>
  </section>

  <section class="triz-drill__debrief" aria-labelledby="drill-method-title">
    <header>
      <div>
        <p class="triz-drill__eyebrow">Answer spine</p>
        <h2 id="drill-method-title">Six moves are enough for most questions.</h2>
      </div>
      <p>The goal is not to force TRIZ vocabulary into an interview. Use normal architecture language. The framework is underneath the answer, doing the less glamorous work of keeping the reasoning coherent.</p>
    </header>
    <div class="triz-drill__debrief-grid">
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">01</p><h3>Frame</h3><p>What happens, which business object matters, who owns the outcome, and what evidence exists?</p></article>
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">02</p><h3>Contradiction</h3><p>Which useful property improves, and which other useful property becomes worse?</p></article>
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">03</p><h3>Separate</h3><p>Can the conflict change by time, condition, context, system level, authority, or representation?</p></article>
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">04</p><h3>Options</h3><p>Compare simplification, deterministic redesign, and uncertainty-assisted design when they are genuinely different.</p></article>
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">05</p><h3>Authority</h3><p>Who may read, propose, validate, approve, and execute? Capability is not authorization.</p></article>
      <article class="triz-drill__debrief-card"><p class="triz-drill__eyebrow">06</p><h3>Prove it</h3><p>Name evidence, primary metric, counter-metric, bounded scope, and what would change your recommendation.</p></article>
    </div>
  </section>

  <section class="triz-drill__debrief" aria-labelledby="drill-data-title">
    <header>
      <div>
        <p class="triz-drill__eyebrow">Machine layer</p>
        <h2 id="drill-data-title">The drill is a dataset too.</h2>
      </div>
      <p>The browser UI and the assessment agent use the same case data and the same scoring rubric. That makes the exercise reusable for regression checks instead of relying on whatever mood the evaluator woke up in.</p>
    </header>
    <div class="research-route-list">
      <a href="/datasets/triz-digital-framework/drill-cases.json"><span>18</span><strong>Drill cases</strong><small>Sales, Procurement, Logistics, Integration, Master Data, and AI cases with expected reasoning signals.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/datasets/triz-digital-framework/lead-rubric.json"><span>24</span><strong>Lead rubric</strong><small>Six scoring dimensions, performance bands, hard-fail signals, and the answer spine.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/triz/workbench/"><span>WB</span><strong>TRIZ Workbench</strong><small>Use the full contradiction workflow when a case needs deeper design exploration.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>
</div>

<div class="research-canvas">
  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>

<script src="/assets/triz-drill.js" defer></script>
