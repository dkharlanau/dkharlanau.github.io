---
layout: default
title: "SAP Lead Decision Cards — Architecture Trade-offs for Interviews"
description: "Practice SAP Lead architecture decisions with decision drivers, trade-offs, failure modes, and pressure questions."
permalink: /labs/interview-readiness/decision-cards/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-19
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-decision
  - lead-challenge
  - integration-patterns
  - integration-recovery
  - logistics-ewm
  - ai-readiness
tags:
  - sap
  - architecture
  - integration
  - interview
  - decision-making
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li><a href="/labs/interview-readiness/drills/">Drills</a></li><li aria-current="page">Decision Cards</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lead drills / Decision Cards</p>
      <h1>A technology choice<br />is not yet a decision.</h1>
      <p>Use these cards to practise the reasoning behind common SAP architecture choices. Give your recommendation first. Then open the card and compare your answer with the decision drivers and failure paths.</p>
      <a class="research-canvas__button" href="#cards">Open cards <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Lead drills"><a href="/labs/interview-readiness/drills/">Drills</a><a href="/labs/interview-readiness/diagnostic-lab/">Diagnostic Lab</a><a href="/labs/interview-readiness/boss-battles/">Boss Battles</a><a href="/labs/interview-readiness/evidence-bank/">Evidence Bank</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Decision structure">
      <p>Decision structure</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Need</strong><small>Business and operating requirement</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Options</strong><small>Real alternatives</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Trade-off</strong><small>Cost and risk accepted</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Recovery</strong><small>What happens when it fails</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Answer before opening:</strong> state the business need, preferred option, why the alternatives are weaker here, the main operational risk, and what would make you revisit the decision.</p>
    <p><strong>Avoid absolutes:</strong> “API is modern” and “events are scalable” are observations, not architecture decisions.</p>
  </section>

  <section class="research-canvas__inventory" id="cards" data-reveal>
    <header><p class="research-canvas__eyebrow">Decision set</p><h2>Eight recurring Lead-level choices.</h2><p>Open a card only after giving a short recommendation aloud.</p></header>
    <div class="ir-question-list">
      <details class="ir-question"><summary><strong>IDoc vs API vs Event</strong> — Which integration pattern fits the business interaction?</summary><p><strong>Use when:</strong> IDoc for durable business documents and established SAP processing; API for request/response or explicit service contracts; event for decoupled notification and downstream reaction.</p><p><strong>Decision drivers:</strong> business timing, coupling, acknowledgement need, replay, ordering, payload ownership, monitoring, volume, and consumer count.</p><p><strong>Trade-off:</strong> synchronous clarity can increase runtime coupling. Asynchronous durability can increase recovery and reconciliation work.</p><p><strong>Failure mode:</strong> every technical component is green while the business document is missing, duplicated, or processed in the wrong order.</p><p><strong>Lead recommendation:</strong> choose from the business interaction and recovery model first, then select the technology.</p><p><strong>Pressure:</strong> “The project already has an API platform. Why not use APIs for everything?”</p></details>

      <details class="ir-question"><summary><strong>Synchronous vs Asynchronous</strong> — Should the caller wait for the business result?</summary><p><strong>Use synchronous when:</strong> the next user or system action needs an immediate answer and failure can be handled in the same interaction.</p><p><strong>Use asynchronous when:</strong> work can continue later, temporary outages must be absorbed, or independent processing is more important than instant confirmation.</p><p><strong>Decision drivers:</strong> business latency, timeout risk, availability dependency, retry, duplicate control, and user experience.</p><p><strong>Failure mode:</strong> a four-hour outage causes thousands of retries without idempotency or creates a false success message to users.</p><p><strong>Pressure:</strong> “The business wants real time. Is that a reason for synchronous integration?”</p></details>

      <details class="ir-question"><summary><strong>Embedded vs Decentralised EWM</strong> — Where should warehouse execution live?</summary><p><strong>Use embedded when:</strong> operational scale, release independence, integration isolation, or system boundaries do not justify another warehouse platform.</p><p><strong>Use decentralised when:</strong> warehouse scale, availability, release lifecycle, landscape separation, or local execution needs justify the additional integration and operations model.</p><p><strong>Decision drivers:</strong> warehouse criticality, throughput, outage tolerance, lifecycle, integration, skills, and support ownership.</p><p><strong>Trade-off:</strong> independence increases integration, monitoring, master-data, and recovery complexity.</p><p><strong>Pressure:</strong> “Decentralised sounds more enterprise. Why not choose it for a global template?”</p></details>

      <details class="ir-question"><summary><strong>Standard Extension vs Custom Development</strong> — How much code does the requirement deserve?</summary><p><strong>Prefer standard:</strong> when configuration or supported extension points meet the real business need with acceptable process change.</p><p><strong>Customise:</strong> when the requirement creates measurable value or necessary control that standard behaviour cannot provide safely.</p><p><strong>Decision drivers:</strong> differentiation, upgrade impact, testing cost, support ownership, data model, clean-core boundary, and reversibility.</p><p><strong>Failure mode:</strong> custom code becomes the hidden owner of a process rule that nobody can explain after the original team leaves.</p><p><strong>Pressure:</strong> “The business refuses to change its current process. Do you build it?”</p></details>

      <details class="ir-question"><summary><strong>Batch vs Event-driven</strong> — When should a process react?</summary><p><strong>Use batch when:</strong> the business tolerates a window, reconciliation is easier in groups, or source systems cannot provide reliable events.</p><p><strong>Use events when:</strong> downstream action benefits from low latency and the organisation can operate event contracts, replay, ordering, and observability.</p><p><strong>Decision drivers:</strong> value of freshness, volume, recovery, ordering, source capability, and operations maturity.</p><p><strong>Trade-off:</strong> event-driven design removes waiting but creates a permanent contract and recovery responsibility.</p><p><strong>Pressure:</strong> “Events reduce latency. Why keep any batch interface?”</p></details>

      <details class="ir-question"><summary><strong>Central vs Local Master Data</strong> — Who owns the definition and who owns execution?</summary><p><strong>Centralise when:</strong> common identity, global controls, cross-company processes, and shared analytics need one governed definition.</p><p><strong>Keep local control when:</strong> attributes are truly market-specific, operational timing differs, or central governance would block legitimate execution.</p><p><strong>Decision drivers:</strong> ownership, replication latency, legal variation, process dependency, stewardship, and conflict resolution.</p><p><strong>Failure mode:</strong> a “single source of truth” exists technically but local teams maintain shadow values because the governance model cannot meet operational needs.</p><p><strong>Pressure:</strong> “Why not centralise all material attributes in MDG?”</p></details>

      <details class="ir-question"><summary><strong>RAG vs Fine-tuning</strong> — What should change: knowledge access or model behaviour?</summary><p><strong>Use retrieval:</strong> when answers depend on changing enterprise knowledge, permissions, freshness, citations, or traceable source context.</p><p><strong>Consider fine-tuning:</strong> when the target is stable behaviour, format, style, classification, or task pattern and there is enough governed training and evaluation data.</p><p><strong>Decision drivers:</strong> freshness, provenance, task stability, data quality, evaluation, privacy, cost, and operating ownership.</p><p><strong>Failure mode:</strong> the team fine-tunes a model to remember content that changes every week, then discovers version control the expensive way.</p><p><strong>Pressure:</strong> “The RAG prototype still gives wrong answers. Why not fine-tune?”</p></details>

      <details class="ir-question"><summary><strong>Agent Autonomy vs Human Approval</strong> — Which actions can an AI system execute?</summary><p><strong>Allow autonomy when:</strong> the action is bounded, reversible, observable, permissioned, and the cost of a wrong action is acceptable.</p><p><strong>Require approval when:</strong> the action changes money, access, master data, customer commitments, production state, or another high-impact business outcome without a reliable automatic safeguard.</p><p><strong>Decision drivers:</strong> impact, reversibility, confidence, identity, permissions, audit, fallback, and escalation.</p><p><strong>Failure mode:</strong> the model is evaluated for answer quality while the production risk is actually tool permission and uncontrolled execution.</p><p><strong>Pressure:</strong> “Human approval removes the productivity benefit. Why use an agent at all?”</p></details>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Answer test</p><h2>A Lead answer should survive one more question.</h2><p>After every card, force one change: lower budget, shorter timeline, four-hour outage, new country, higher volume, weaker operations team, or stronger audit requirement. Then decide again.</p></header>
    <div class="ir-toolbar"><a class="ir-button ir-button--primary" href="/labs/interview-readiness/boss-battles/">Move to Boss Battles</a><a class="ir-button" href="/labs/assessment/board/">Architecture Board</a></div>
  </section>
</div>
