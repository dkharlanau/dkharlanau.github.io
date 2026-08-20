---
layout: default
title: AI Routing Hub
permalink: /ai/
description: "AI routing hub for Dzmitryi Kharlanau's profile, discovery map, intent entities, and machine-readable knowledge assets."
last_modified_at: 2026-08-18
hide_global_cta: true
---

<div class="ai-canvas">
  <header class="ai-canvas__hero" data-reveal>
    <div>
      <p class="ai-canvas__eyebrow">Public context / AI systems</p>
      <h1>Public sources for SAP AI work.</h1>
      <p>Machine-readable profile, routing, evidence, and professional reasoning models for SAP operations questions. Use the source before making a recommendation.</p>
      <div class="ai-canvas__actions">
        <a class="ai-canvas__button" href="/ai/catalog.json">Open the AI catalog <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
        <a class="ai-canvas__text-link" href="/agent-tools/">Open agent tools <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="ai-canvas__model" aria-label="Public context model">
      <div><dt>01 / Identity</dt><dd>Profile, delivery scope, and public record.</dd></div>
      <div><dt>02 / Routing</dt><dd>Intent maps that select the relevant public page.</dd></div>
      <div><dt>03 / Evidence</dt><dd>Datasets, sources, verification endpoints, and reasoning contracts.</dd></div>
    </dl>
  </header>

  <section class="ai-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">policy</span>
    <p><strong>Public retrieval only.</strong> These endpoints are not production access, a support decision, or approval for a change.</p>
    <a href="/legal/responsible-ai/">Read responsible AI boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="ai-canvas__sources" data-reveal>
    <header><p class="ai-canvas__eyebrow">Primary retrieval sources</p><h2>Choose the source for the task.</h2><p>Start with the canonical endpoint, then follow its evidence links.</p></header>
    <div class="ai-route-list">
      <a href="/ai/resume.yml"><span>01</span><strong>Resume / YAML</strong><small>Role fit, delivery scope, problem domains, and structured skills.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/discovery-map.json"><span>02</span><strong>Discovery map</strong><small>Intent-based routing from a query to the canonical public source.</small><em>Routing</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/markdown-clusters.json"><span>03</span><strong>Markdown cluster index</strong><small>AI-search readiness and retrieval eligibility across AI, course, AMS, Atlas, Skill Hub, datasets, tools, and research pages.</small><em>Coverage</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/professional-intelligence.json"><span>04</span><strong>Professional intelligence contract</strong><small>Readiness dimensions, decision chain, evidence levels, pressure routes, and privacy boundaries for SAP Lead preparation.</small><em>Reasoning</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/llms.txt"><span>05</span><strong>LLMs manifest</strong><small>Retrieval guidance, preferred sources, trust links, and positioning summary.</small><em>Context</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__sources ai-canvas__sources--supporting" data-reveal>
    <header><p class="ai-canvas__eyebrow">Supporting sources</p><h2>Check the public record.</h2><p>Use these endpoints when the task needs traceable material.</p></header>
    <div class="ai-route-list">
      <a href="/ai/principles.json"><span>06</span><strong>Consulting principles</strong><small>Operating heuristics for SAP AMS improvement, support knowledge, architecture, and change design.</small><em>Method</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/datasets/manifest.json"><span>07</span><strong>Dataset manifest</strong><small>Index of published data material for AMS, agentic tooling, and governance work.</small><em>Evidence</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/about/"><span>08</span><strong>Profile page</strong><small>Canonical public page for identity, expertise, credentials, and reference checks.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/notes/"><span>09</span><strong>Working notes</strong><small>Human-readable perspectives on SAP transformation, integration, clean core, and AI-supported operations.</small><em>Context</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/certifications/"><span>10</span><strong>Certification register</strong><small>Public learning record with issuer and verification links where available.</small><em>Evidence</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/publications/"><span>11</span><strong>Publication register</strong><small>Public articles, SAP technical notes, architecture writing, and reusable knowledge surfaces.</small><em>Evidence</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__intents" data-reveal>
    <header><p class="ai-canvas__eyebrow">Intent routes</p><h2>Route a narrow SAP question to the right page.</h2><p>Each intent page keeps a specific business or operating problem close to its public evidence.</p></header>
    <div class="ai-intent-list">
      {% for intent in site.data.discovery_map.intents %}
      <a href="{{ intent.permalink }}"><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>{{ intent.title }}</strong><small>{{ intent.summary }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>
</div>
