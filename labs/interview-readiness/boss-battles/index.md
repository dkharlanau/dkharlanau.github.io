---
layout: default
title: "SAP Lead Boss Battles — Long-form Interview Pressure Cases"
description: "Practice long-form SAP Lead cases with changing constraints across sales, logistics, integration, architecture, AI, and stakeholder pressure."
permalink: /labs/interview-readiness/boss-battles/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-19
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-answer
  - lead-challenge
  - lead-decision
  - lead-stakeholders
  - integration-ownership
  - logistics-p2p
  - sales-o2c
  - ai-readiness
tags:
  - sap
  - sap-lead
  - assessment
  - architecture
  - pressure-interview
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li><a href="/labs/interview-readiness/drills/">Drills</a></li><li aria-current="page">Boss Battles</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lead drills / Boss Battles</p>
      <h1>The first answer<br />is only round one.</h1>
      <p>Boss Battles are 20–30 minute cases. The problem changes while you answer. You need to keep the business outcome, architecture, evidence, ownership, and delivery constraints connected under pressure.</p>
      <a class="research-canvas__button" href="#battle">Enter battle <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Lead drills"><a href="/labs/interview-readiness/drills/">Drills</a><a href="/labs/interview-readiness/decision-cards/">Decision Cards</a><a href="/labs/interview-readiness/diagnostic-lab/">Diagnostic Lab</a><a href="/labs/interview-readiness/evidence-bank/">Evidence Bank</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Battle sequence">
      <p>Battle sequence</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Frame</strong><small>Scope and business impact</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Diagnose</strong><small>Evidence and failure boundary</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Design</strong><small>Options and controls</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Defend</strong><small>Cost, time, outage, stakeholder pressure</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">sports_mma</span>
    <p><strong>Do not rush to solution:</strong> start with impact, scope, assumptions, owners, and the evidence you need.</p>
    <p><strong>Self-rating:</strong> Weak = answer loses structure. Acceptable = correct but reactive. Strong = keeps business, evidence, trade-off, recovery, and ownership connected after the constraint changes.</p>
  </section>

  <section class="research-canvas__inventory" id="battle" data-reveal>
    <header><p class="research-canvas__eyebrow">Pressure case</p><h2 id="bb-title">Choose a Boss Battle.</h2><p id="bb-summary">Each reveal adds new evidence or an interviewer challenge.</p></header>
    <div class="ir-story-form"><label>Battle<select id="bb-select" aria-label="Boss Battle"></select></label></div>
    <div class="ir-grid" id="bb-meta"></div>
    <article class="ir-question" id="bb-opening"></article>
    <div class="ir-question-list" id="bb-rounds" aria-live="polite"></div>
    <div class="ir-toolbar"><button type="button" class="ir-button--primary" id="bb-next">Reveal round 1</button><button type="button" id="bb-reset">Restart battle</button></div>
  </section>

  <section class="research-canvas__inventory" id="rating" data-reveal>
    <header><p class="research-canvas__eyebrow">Self-check</p><h2>Did the answer stay Lead-level?</h2><p>Rate the whole battle after the final round. The score is stored only in this browser.</p></header>
    <div class="ir-rating" id="bb-rating"><button type="button" data-score="0">Weak</button><button type="button" data-score="1">Acceptable</button><button type="button" data-score="2">Strong</button></div>
    <p class="ir-muted" id="bb-history"></p>
    <div class="ir-toolbar"><a class="ir-button" href="/labs/assessment/mock/">Run scored mock</a><a class="ir-button" href="/labs/assessment/board/">Architecture Board</a><a class="ir-button" href="/labs/interview-readiness/evidence-bank/">Check project evidence</a></div>
  </section>
</div>

<script>
(() => {
  'use strict';
  const STORAGE = 'dkharlanau-boss-battle-history-v1';
  const battles = [
    {
      id:'global-order', title:'Global Order Fulfilment Failure', domain:'Sales / EWM / TM / Integration', target:'Protect customer promise while recovering cross-system order flow.',
      opening:'A global business runs S/4HANA with EWM, TM, a 3PL, and EDI customer channels. After a release, some orders are duplicated, some deliveries are late, and the 3PL claims SAP is sending inconsistent messages. You are asked to lead the response.',
      rounds:[
        ['Round 1 — Scope','The issue affects two countries and one EDI channel. Web orders are normal. What do you isolate first, and which business metric tells you the real impact?'],
        ['Round 2 — Evidence','Technical dashboards show green connectivity. EDI retries increased after response times crossed the partner timeout. Some original requests completed after the partner retried. What changes in your hypothesis?'],
        ['Round 3 — Architecture','The current contract has no business idempotency key. A middleware team proposes deduplication by payload hash. Do you accept it as the target design? Defend the boundary.'],
        ['Round 4 — Executive pressure','The business wants all duplicate orders deleted today and a permanent fix within six weeks. What containment do you approve, what do you refuse, and how do you sequence the permanent change?'],
        ['Round 5 — Operations','The interface may be unavailable for four hours during the next carrier maintenance window. Explain the recovery model, monitoring, ownership, and reconciliation before you call the design complete.']
      ]
    },
    {
      id:'supplier-disruption', title:'Supplier Confirmation and Inventory Crisis', domain:'Procurement / Inventory / Integration', target:'Restore reliable supply decisions without hiding data-quality and acknowledgement gaps.',
      opening:'A manufacturing company reports material shortages although buyers say purchase orders were sent on time. Supplier acknowledgements are missing for critical items, inventory figures differ across warehouse and ERP views, and production planners are escalating daily.',
      rounds:[
        ['Round 1 — Process boundary','Map the P2P and inventory hand-offs before naming a root cause. Which states must be reconciled?'],
        ['Round 2 — Evidence','Outbound PO messages are successful. Supplier acknowledgements exist in middleware dead-letter storage after a supplier code change. What is the immediate business risk?'],
        ['Round 3 — Complication','Warehouse movements from a four-hour outage are also waiting for recovery. Some materials have physical stock that ATP and planning cannot use. How do you keep two incidents from becoming one vague “SAP stock problem”?'],
        ['Round 4 — Stakeholder pressure','Procurement wants manual confirmations loaded. Warehouse wants direct stock correction. Production wants both done immediately. What do you approve, and what control do you insist on?'],
        ['Round 5 — Prevention','Design the operating model: acknowledgement SLA, dead-letter ownership, stock reconciliation, message recovery order, and monitoring that reports business outcomes rather than only technical success.']
      ]
    },
    {
      id:'ai-approval', title:'AI Agent Wants Production Authority', domain:'AI / Procurement / Governance', target:'Qualify automation value while keeping production decisions controlled and auditable.',
      opening:'A procurement team has an AI agent that reads supplier emails, proposes purchase-order changes, and can call an ERP tool. A sponsor asks you to remove human approval because the pilot saves time. The model performs well on a small evaluation set.',
      rounds:[
        ['Round 1 — Qualification','What business action is actually being automated, and which failure costs matter more than model accuracy?'],
        ['Round 2 — Evidence','The evaluation measures extraction accuracy but not permission errors, duplicate tool calls, stale supplier data, or incorrect commercial changes. Can the pilot evidence support autonomous production use?'],
        ['Round 3 — Architecture','Propose a control boundary for low-risk suggestions, high-impact PO changes, identity, tool permissions, logging, and rollback.'],
        ['Round 4 — Sponsor pressure','The sponsor says approval destroys the ROI and competitors are already using autonomous agents. How do you challenge the claim without turning the answer into generic AI caution?'],
        ['Round 5 — Exit criteria','Define the evidence that would allow more autonomy later: evaluation coverage, failure rate, reversibility, permission controls, monitoring, incident response, and business owner acceptance.']
      ]
    }
  ];

  const select = document.getElementById('bb-select');
  const title = document.getElementById('bb-title');
  const summary = document.getElementById('bb-summary');
  const meta = document.getElementById('bb-meta');
  const opening = document.getElementById('bb-opening');
  const rounds = document.getElementById('bb-rounds');
  const next = document.getElementById('bb-next');
  const reset = document.getElementById('bb-reset');
  const rating = document.getElementById('bb-rating');
  const historyText = document.getElementById('bb-history');
  let battleIndex = 0;
  let round = 0;

  battles.forEach((item,i) => { const option = document.createElement('option'); option.value = String(i); option.textContent = item.title; select.appendChild(option); });

  function history() { try { const rows = JSON.parse(localStorage.getItem(STORAGE) || '[]'); return Array.isArray(rows) ? rows : []; } catch (_) { return []; } }
  function save(row) { try { const rows = history(); rows.unshift(row); localStorage.setItem(STORAGE, JSON.stringify(rows.slice(0,30))); } catch (_) {} }

  function renderMeta(item) {
    meta.replaceChildren();
    [['Domain',item.domain],['Mission',item.target]].forEach(([label,value]) => {
      const card = document.createElement('article'); card.className = 'ir-card';
      const kicker = document.createElement('p'); kicker.className = 'ir-kicker'; kicker.textContent = label;
      const p = document.createElement('p'); p.textContent = value;
      card.append(kicker,p); meta.appendChild(card);
    });
  }

  function render() {
    const item = battles[battleIndex];
    title.textContent = item.title;
    summary.textContent = item.target;
    renderMeta(item);
    opening.replaceChildren();
    const h = document.createElement('h3'); h.textContent = 'Opening case';
    const p = document.createElement('p'); p.textContent = item.opening;
    opening.append(h,p);
    rounds.replaceChildren();
    for (let i = 0; i < round; i += 1) {
      const card = document.createElement('article'); card.className = 'ir-question';
      const metaRow = document.createElement('div'); metaRow.className = 'ir-question__meta';
      const pill = document.createElement('span'); pill.className = 'ir-pill'; pill.textContent = item.rounds[i][0];
      const copy = document.createElement('p'); copy.textContent = item.rounds[i][1];
      metaRow.appendChild(pill); card.append(metaRow,copy); rounds.appendChild(card);
    }
    next.disabled = round >= item.rounds.length;
    next.textContent = round >= item.rounds.length ? 'Battle complete' : `Reveal round ${round + 1}`;
    const rows = history().filter(row => row.battle_id === item.id);
    historyText.textContent = rows.length ? `${rows.length} previous attempt${rows.length === 1 ? '' : 's'} in this browser. Latest: ${['Weak','Acceptable','Strong'][rows[0].score]}.` : 'No saved attempt for this battle yet.';
    rating.querySelectorAll('button').forEach(button => button.setAttribute('aria-pressed','false'));
  }

  select.addEventListener('change', () => { battleIndex = Number(select.value) || 0; round = 0; render(); });
  next.addEventListener('click', () => { if (round < battles[battleIndex].rounds.length) { round += 1; render(); } });
  reset.addEventListener('click', () => { round = 0; render(); });
  rating.addEventListener('click', event => {
    const button = event.target.closest('button[data-score]'); if (!button || round < battles[battleIndex].rounds.length) { if (round < battles[battleIndex].rounds.length) historyText.textContent = 'Finish all rounds before rating the battle.'; return; }
    const score = Number(button.dataset.score);
    save({battle_id:battles[battleIndex].id, score, attempted_at:new Date().toISOString()});
    render();
    button.setAttribute('aria-pressed','true');
  });
  render();
})();
</script>
