---
layout: default
title: "TRIZ Digital Workbench"
description: "A browser-based contradiction workbench for IT, SAP, business-process, integration, data, and AI design."
permalink: /triz/workbench/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, workshop, problem-solving, architecture, sap, business-processes, ai]
---

<link rel="stylesheet" href="/assets/triz-workbench.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Workbench</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / interactive workbench</p>
      <h1>Frame the contradiction.<br />Then force different system shapes.</h1>
      <p>This workbench turns a problem into a structured design draft. It does not call an AI model. The routing is deterministic, so the framework itself has to do useful work before we add probabilistic reasoning.</p>
      <a class="research-canvas__button" href="#workbench">Start with a problem <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Workbench behavior">
      <p>Workbench</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>6</strong><small>Separation operators checked</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>3</strong><small>Different system shapes</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>1</strong><small>Machine-readable draft</small></div>
      <em>No model call. No server-side form submission.</em>
    </div>
  </header>
</div>

<section class="triz-workbench-shell" id="workbench" data-triz-workbench>
  <div class="triz-workbench__notice">
    <span class="material-symbols-outlined" aria-hidden="true">privacy_tip</span>
    <p><strong>Public-site rule.</strong> The workbench runs in the browser and does not submit the form to this site. Still, do not paste client names, internal IDs, proprietary configuration, credentials, or confidential process details. Use synthetic or anonymized wording.</p>
  </div>

  <div class="triz-workbench__stage">
    <div class="triz-workbench__intro">
      <p class="triz-workbench__eyebrow">Input / problem frame</p>
      <h2>Useful function first. Technology later.</h2>
      <p>Choose a synthetic example or enter your own problem. The output is a design hypothesis, not an architecture decision. Its purpose is to make assumptions and trade-offs visible early.</p>
      <p class="triz-workbench__status" data-triz-status aria-live="polite">Loading synthetic presets…</p>
    </div>

    <form class="triz-workbench__form" data-triz-form>
      <div class="triz-workbench__form-group">
        <label for="triz-preset">Synthetic preset</label>
        <div class="triz-workbench__field">
          <select id="triz-preset" data-triz-preset>
            <option value="">Start from an empty frame</option>
          </select>
          <small>Presets are synthetic and safe to reuse in workshops or assessment practice.</small>
        </div>
      </div>

      <div class="triz-workbench__form-group triz-workbench__form-group--split">
        <label>Context</label>
        <div>
          <div class="triz-workbench__field">
            <label for="triz-domain">Domain</label>
            <select id="triz-domain" name="domain">
              <option value="sap_sales">SAP Sales</option>
              <option value="sap_procurement">SAP Procurement</option>
              <option value="master_data">Master data</option>
              <option value="integration">Integration</option>
              <option value="business_process">Business process</option>
              <option value="ai_agents">AI / agents</option>
              <option value="it_architecture">IT architecture</option>
            </select>
          </div>
          <div class="triz-workbench__field">
            <label for="triz-risk">Risk tier</label>
            <select id="triz-risk" name="risk_tier">
              <option value="R0">R0 · advisory only</option>
              <option value="R1">R1 · low-impact reversible</option>
              <option value="R2" selected>R2 · business-significant</option>
              <option value="R3">R3 · high-impact / hard to reverse</option>
            </select>
          </div>
        </div>
      </div>

      <div class="triz-workbench__form-group">
        <label for="triz-observed">Observed behavior</label>
        <div class="triz-workbench__field">
          <textarea id="triz-observed" name="observed_behavior" placeholder="What happens now? Describe the failure, waiting, repeated work, coupling, or decision problem."></textarea>
          <small>Describe behavior, not the requested solution.</small>
        </div>
      </div>

      <div class="triz-workbench__form-group">
        <label for="triz-function">Useful function</label>
        <div class="triz-workbench__field">
          <textarea id="triz-function" name="useful_function" placeholder="What useful outcome must the system or process provide?"></textarea>
          <small>Try to write this without naming a product, protocol, model, or platform.</small>
        </div>
      </div>

      <div class="triz-workbench__form-group triz-workbench__form-group--split">
        <label>Ownership</label>
        <div>
          <div class="triz-workbench__field">
            <label for="triz-actor">Actor</label>
            <input id="triz-actor" name="actor" type="text" placeholder="Process owner / sales ops / service owner" />
          </div>
          <div class="triz-workbench__field">
            <label for="triz-object">Business object</label>
            <input id="triz-object" name="business_object" type="text" placeholder="Sales order / purchase order / incident" />
          </div>
        </div>
      </div>

      <div class="triz-workbench__form-group triz-workbench__form-group--split">
        <label>Contradiction</label>
        <div>
          <div class="triz-workbench__field">
            <label for="triz-improve">Improve A</label>
            <input id="triz-improve" name="improve" type="text" placeholder="speed, freshness, automation…" />
          </div>
          <div class="triz-workbench__field">
            <label for="triz-preserve">Preserve B</label>
            <input id="triz-preserve" name="preserve" type="text" placeholder="control, privacy, flexibility…" />
          </div>
        </div>
      </div>

      <div class="triz-workbench__form-group triz-workbench__form-group--split">
        <label>Classification</label>
        <div>
          <div class="triz-workbench__field">
            <label for="triz-type">Contradiction type</label>
            <select id="triz-type" name="contradiction_type">
              <option value="speed_control">Speed vs control</option>
              <option value="standard_flexible">Standardization vs flexibility</option>
              <option value="automation_accountability">Automation vs accountability</option>
              <option value="integration_coupling">Integration vs coupling</option>
              <option value="freshness_cost">Freshness vs cost</option>
              <option value="accuracy_latency">Accuracy vs latency</option>
              <option value="context_privacy">Context vs privacy</option>
              <option value="autonomy_trust">Autonomy vs trust</option>
              <option value="specialization_handoffs">Specialization vs handoffs</option>
              <option value="local_global">Local optimization vs end-to-end outcome</option>
            </select>
          </div>
          <div class="triz-workbench__field">
            <label for="triz-evidence">Evidence</label>
            <textarea id="triz-evidence" name="evidence" placeholder="Queue age; logs; process data; rejected cases; correction rate"></textarea>
          </div>
        </div>
      </div>

      <div class="triz-workbench__form-group">
        <label for="triz-constraints">Constraints</label>
        <div class="triz-workbench__field">
          <textarea id="triz-constraints" name="constraints" placeholder="Authorization; policy; timing; legal; integration; data; operational limits"></textarea>
          <small>Separate hard constraints from habits and existing implementation choices.</small>
        </div>
      </div>

      <div class="triz-workbench__actions">
        <button class="triz-workbench__button" type="submit">Build design draft</button>
        <button class="triz-workbench__button triz-workbench__button--secondary" type="button" data-triz-reset>Reset</button>
      </div>
    </form>
  </div>

  <div class="triz-workbench__output" data-triz-output hidden></div>

  <section class="triz-workbench__lead" data-triz-lead hidden>
    <p class="triz-workbench__eyebrow">Assessment mode / 60–90 seconds</p>
    <h2>Explain the reasoning like a Lead.</h2>
    <p class="triz-workbench__lead-answer" data-triz-lead-answer></p>
  </section>

  <section class="triz-workbench__machine" data-triz-machine hidden>
    <div class="triz-workbench__machine-head">
      <div>
        <p class="triz-workbench__eyebrow">Agent handoff</p>
        <h2>Structured draft.</h2>
      </div>
      <button class="triz-workbench__button triz-workbench__button--secondary" type="button" data-triz-copy disabled>Copy JSON</button>
    </div>
    <pre class="triz-workbench__json" data-triz-json tabindex="0"></pre>
    <p><small>The draft follows the same concepts as the <a href="/datasets/triz-digital-framework/reasoning-schema.json">reasoning schema</a>. A deeper agent pass should verify evidence, assumptions, current technology facts, and real system constraints before recommending implementation.</small></p>
  </section>
</section>

<section class="triz-workbench__method" aria-labelledby="workbench-method">
  <p class="triz-workbench__eyebrow">Why this shape</p>
  <h2 id="workbench-method">Three options are more useful than three vendors.</h2>
  <p>I want the workbench to create real design distance. If every option keeps the same process, state, authority, and integration boundary, we did not explore the problem. We just changed the label on the box.</p>
  <div class="triz-workbench__method-grid">
    <article>
      <p class="triz-workbench__index">A / Simplify</p>
      <h3>Remove machinery.</h3>
      <p>Ask whether a handoff, copy, check, queue, or synchronous dependency can disappear because its useful function moves somewhere better.</p>
    </article>
    <article>
      <p class="triz-workbench__index">B / Deterministic</p>
      <h3>Redesign the system.</h3>
      <p>Use explicit state, rules, workflow, events, ownership, or data representation before adding probabilistic behavior.</p>
    </article>
    <article>
      <p class="triz-workbench__index">C / Uncertainty-assisted</p>
      <h3>Add AI where uncertainty remains.</h3>
      <p>Use models for interpretation and agents for unknown next steps, while authority and hard controls stay explicit.</p>
    </article>
  </div>
</section>

<section class="triz-workbench__method" aria-labelledby="machine-data">
  <p class="triz-workbench__eyebrow">Machine layer</p>
  <h2 id="machine-data">The browser and the agent use the same concepts.</h2>
  <div class="research-route-list">
    <a href="/datasets/triz-digital-framework/decision-map.json"><span>MAP</span><strong>Decision map</strong><small>Contradiction → operators → patterns → resource focus → experiment metrics.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    <a href="/datasets/triz-digital-framework/workbench-presets.json"><span>PRE</span><strong>Synthetic presets</strong><small>SAP Sales, Procurement, master data, integration, AI operations, and global/local process cases.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
    <a href="/datasets/triz-digital-framework/reasoning-schema.json"><span>JSON</span><strong>Reasoning schema</strong><small>Structured contract for a deeper agent analysis.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    <a href="https://github.com/dkharlanau/dkharlanau.github.io/blob/main/agent-skills/skills/triz-digital-problem-solving/SKILL.md"><span>SKILL</span><strong>Agent workflow</strong><small>Operational instructions for contradiction-driven problem solving.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
  </div>
</section>

<div class="research-canvas">
  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>

<script src="/assets/triz-workbench.js" defer></script>
