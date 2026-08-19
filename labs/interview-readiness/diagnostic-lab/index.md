---
layout: default
title: "SAP Lead Diagnostic Lab — Production Failure Scenarios"
description: "Practice SAP Lead production diagnostics with progressive evidence for sales, procurement, inventory, billing, ATP, and integration failures."
permalink: /labs/interview-readiness/diagnostic-lab/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-19
hide_global_cta: true
career_impact: mapped
career_skills:
  - sales-diagnostics
  - integration-recovery
  - logistics-inventory
  - sales-billing
  - sales-atp
  - delivery-testing
tags:
  - sap
  - diagnostics
  - production-support
  - integration
  - interview
---

<link rel="stylesheet" href="/assets/css/interview-readiness.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/interview-readiness/">Interview Readiness</a></li><li><a href="/labs/interview-readiness/drills/">Drills</a></li><li aria-current="page">Diagnostic Lab</li></ol></nav>

<div class="research-canvas ir-shell">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lead drills / Diagnostic Lab</p>
      <h1>Do not diagnose<br />from the symptom.</h1>
      <p>Each case starts with incomplete information. State what you would check first, then reveal one evidence item at a time. The goal is to find the failure boundary before proposing a fix.</p>
      <a class="research-canvas__button" href="#case">Start case <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
      <nav class="ir-nav" aria-label="Lead drills"><a href="/labs/interview-readiness/drills/">Drills</a><a href="/labs/interview-readiness/decision-cards/">Decision Cards</a><a href="/labs/interview-readiness/boss-battles/">Boss Battles</a><a href="/labs/interview-readiness/evidence-bank/">Evidence Bank</a></nav>
    </div>
    <div class="research-canvas__signal" aria-label="Diagnostic sequence">
      <p>Diagnostic sequence</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Impact</strong><small>Who and what is affected?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Boundary</strong><small>Where did expected flow stop?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Evidence</strong><small>What proves or rejects a cause?</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Recovery</strong><small>How do we restore safely?</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">troubleshoot</span>
    <p><strong>Rule:</strong> before every reveal, say what evidence you expect and how it would change your next step.</p>
    <p><strong>Lead signal:</strong> separate containment from root cause. A safe workaround can restore business flow while the permanent cause still needs analysis.</p>
  </section>

  <section class="research-canvas__inventory" id="case" data-reveal>
    <header><p class="research-canvas__eyebrow">Progressive case</p><h2 id="dl-title">Choose a failure scenario.</h2><p id="dl-context">The case will show only the evidence you have earned by asking the next useful question.</p></header>
    <div class="ir-story-form">
      <label>Scenario<select id="dl-select" aria-label="Diagnostic scenario"></select></label>
    </div>
    <div class="ir-grid" id="dl-meta"></div>
    <article class="ir-question" id="dl-prompt"></article>
    <div class="ir-question-list" id="dl-evidence" aria-live="polite"></div>
    <div class="ir-toolbar"><button type="button" class="ir-button--primary" id="dl-reveal">Reveal next evidence</button><button type="button" id="dl-reset">Reset case</button><a class="ir-button" href="/labs/enterprise-context/sales-diagnostics/">Open diagnostic reference</a></div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Debrief test</p><h2>Finish every case with five answers.</h2><p>A production diagnosis is incomplete until the business can act on it.</p></header>
    <div class="ir-grid">
      <article class="ir-card"><h3>Impact</h3><p>Which orders, materials, plants, customers, suppliers, or time window are affected?</p></article>
      <article class="ir-card"><h3>Failure boundary</h3><p>Where does expected business state diverge from actual state?</p></article>
      <article class="ir-card"><h3>Containment</h3><p>What can restore business flow without creating duplicate or inconsistent state?</p></article>
      <article class="ir-card"><h3>Root cause</h3><p>Which evidence proves the cause instead of merely correlating with it?</p></article>
      <article class="ir-card"><h3>Prevention</h3><p>What monitoring, control, test, data rule, or ownership change prevents recurrence?</p></article>
    </div>
  </section>
</div>

<script>
(() => {
  'use strict';
  const cases = [
    {
      id:'idoc-51', title:'IDoc 51 after customer-order inbound', domain:'Integration / Sales', impact:'Orders from one channel stopped posting after a transport.',
      prompt:'A partner says messages are delivered, but SAP orders are missing. What do you check first, and what would make you avoid mass reprocessing?',
      evidence:[
        ['Source fact','Inbound IDocs exist and have status 51. The external gateway reports successful delivery to SAP.'],
        ['Source fact','The error text points to a missing value used during sales-order creation, not a communication failure.'],
        ['Supported inference','The transport changed mapping or validation behaviour in the application layer. Connectivity is currently a weak hypothesis.'],
        ['Source fact','A subset of failed IDocs contains a new partner value that is not present in the relevant SAP mapping table.'],
        ['Lead conclusion','Contain the new value, correct governed mapping, test one representative message, then reprocess only the affected set with duplicate checks and business reconciliation.']
      ]
    },
    {
      id:'duplicate-orders', title:'Duplicate sales orders after API retries', domain:'Integration / Sales', impact:'Customers see duplicate confirmations after an intermittent outage.',
      prompt:'The API client says it retried only failed requests. SAP contains duplicate orders. Where is the first useful boundary?',
      evidence:[
        ['Source fact','The client timed out after 30 seconds and retried the same business request with a new technical request ID.'],
        ['Source fact','Some original SAP requests completed after 38–45 seconds. The client had already treated them as failed.'],
        ['Supported inference','Transport-level timeout and business-level failure are not the same state.'],
        ['Source fact','The integration contract has no stable business idempotency key and no duplicate lookup before create.'],
        ['Lead conclusion','Stop blind retries, define idempotency around the business request, reconcile duplicates, and make timeout handling distinguish unknown outcome from confirmed failure.']
      ]
    },
    {
      id:'billing-block', title:'Delivery complete but invoice not created', domain:'Sales / Billing', impact:'Revenue recognition and customer invoicing are delayed.',
      prompt:'Goods issue is complete. The business asks why billing did not happen. What evidence sequence do you use?',
      evidence:[
        ['Source fact','The sales and delivery document flow is complete through goods issue.'],
        ['Source fact','The delivery appears in the billing due list but is excluded by a billing block set earlier in the process.'],
        ['Source fact','The block was set by a custom validation when a commercial reference was missing. The reference is now present.'],
        ['Proof gap','It is not yet proven whether the block should clear automatically after the reference is added.'],
        ['Lead conclusion','Confirm intended control ownership before clearing or automating the block. Restore affected billing safely, then fix the control lifecycle and regression test the unblock path.']
      ]
    },
    {
      id:'atp-stock', title:'Stock exists but ATP confirms zero', domain:'Sales / ATP / Inventory', impact:'Sales cannot promise material that warehouse users can physically see.',
      prompt:'What do you separate before blaming ATP configuration?',
      evidence:[
        ['Source fact','Physical stock is visible in the plant, but part of it is in a stock category not available to the sales requirement.'],
        ['Source fact','Open requirements and receipts exist in the same horizon as the requested date.'],
        ['Source fact','The checking rule excludes the observed stock category by design.'],
        ['Supported inference','The system may be behaving correctly while business users use “stock” and “available stock” as the same concept.'],
        ['Lead conclusion','Explain physical stock vs availability, confirm the business policy for the stock category, and change ATP scope only if the policy is wrong.']
      ]
    },
    {
      id:'stock-mismatch', title:'Warehouse quantity and ERP stock do not match', domain:'Logistics / Inventory / Warehouse', impact:'Picking is blocked and planners distrust available quantity.',
      prompt:'How do you avoid “fixing the quantity” before understanding the state transition?',
      evidence:[
        ['Source fact','Warehouse execution shows the movement completed. ERP inventory has no corresponding material document.'],
        ['Source fact','The integration queue contains failed messages from the outage window.'],
        ['Source fact','Some later messages processed successfully, so current connectivity is healthy.'],
        ['Supported inference','The problem is historical business-state recovery, not current network availability.'],
        ['Lead conclusion','Freeze manual stock correction for the affected set, reconcile warehouse and ERP documents, recover messages in controlled order, then verify stock and downstream availability.']
      ]
    },
    {
      id:'po-ack', title:'Purchase order acknowledgement missing', domain:'Procurement / Supplier Integration', impact:'Buyers do not know whether critical supplier orders were accepted.',
      prompt:'The PO was sent. The supplier portal says nothing is wrong. What must be proven?',
      evidence:[
        ['Source fact','Outbound PO messages are technically successful.'],
        ['Proof gap','Technical send status does not prove supplier acceptance or business acknowledgement.'],
        ['Source fact','The supplier changed one acknowledgement code last week. The inbound mapping does not recognise the new value.'],
        ['Source fact','Inbound acknowledgements are present in middleware dead-letter storage.'],
        ['Lead conclusion','Restore acknowledgement processing with a governed code mapping, reconcile open POs, and add monitoring for missing business acknowledgements rather than only outbound transport success.']
      ]
    },
    {
      id:'api-timeout', title:'API timeout with unknown business outcome', domain:'Integration / Architecture', impact:'A downstream system cannot tell whether a business action succeeded.',
      prompt:'What do you tell the caller to do after a timeout if create may already have completed?',
      evidence:[
        ['Source fact','The caller received HTTP timeout without a business response.'],
        ['Source fact','Server logs show some timed-out requests continued processing after the connection closed.'],
        ['Supported inference','Immediate retry can create duplicate state unless the operation is idempotent or queryable.'],
        ['Source fact','The API contract supports a client-provided reference but the caller currently generates a new value on retry.'],
        ['Lead conclusion','Treat timeout as unknown outcome, reuse a stable business reference, query or safely retry by idempotency contract, and expose operational reconciliation for unresolved cases.']
      ]
    },
    {
      id:'queue-backlog', title:'Queue backlog after a four-hour outage', domain:'Integration Operations', impact:'Systems are online again but business processing is hours behind.',
      prompt:'Do you simply increase consumers and drain the queue as fast as possible?',
      evidence:[
        ['Source fact','The backlog contains four hours of mixed create and update events.'],
        ['Source fact','Some consumers require ordering by business object. Others are independent.'],
        ['Source fact','Downstream rate limits are lower than the maximum queue-consumer throughput.'],
        ['Supported inference','Maximum technical throughput can create ordering errors, duplicate retries, or a second outage downstream.'],
        ['Lead conclusion','Classify by ordering and business criticality, throttle to downstream capacity, preserve per-object order, monitor lag and failures, then reconcile business outcomes after drain.']
      ]
    }
  ];

  const select = document.getElementById('dl-select');
  const title = document.getElementById('dl-title');
  const context = document.getElementById('dl-context');
  const meta = document.getElementById('dl-meta');
  const prompt = document.getElementById('dl-prompt');
  const evidence = document.getElementById('dl-evidence');
  const reveal = document.getElementById('dl-reveal');
  const reset = document.getElementById('dl-reset');
  let index = 0;
  let step = 0;

  cases.forEach((item,i) => { const option = document.createElement('option'); option.value = String(i); option.textContent = item.title; select.appendChild(option); });

  function renderMeta(item) {
    meta.replaceChildren();
    [['Domain',item.domain],['Business impact',item.impact]].forEach(([label,value]) => {
      const card = document.createElement('article'); card.className = 'ir-card';
      const kicker = document.createElement('p'); kicker.className = 'ir-kicker'; kicker.textContent = label;
      const p = document.createElement('p'); p.textContent = value;
      card.append(kicker,p); meta.appendChild(card);
    });
  }

  function renderCase() {
    const item = cases[index];
    title.textContent = item.title;
    context.textContent = item.impact;
    renderMeta(item);
    prompt.replaceChildren();
    const h = document.createElement('h3'); h.textContent = 'Your first move';
    const p = document.createElement('p'); p.textContent = item.prompt;
    prompt.append(h,p);
    evidence.replaceChildren();
    for (let i = 0; i < step; i += 1) appendEvidence(item.evidence[i], i);
    reveal.disabled = step >= item.evidence.length;
    reveal.textContent = step >= item.evidence.length ? 'Case complete' : `Reveal evidence ${step + 1} of ${item.evidence.length}`;
  }

  function appendEvidence(row,i) {
    const card = document.createElement('article'); card.className = 'ir-question';
    const metaRow = document.createElement('div'); metaRow.className = 'ir-question__meta';
    const count = document.createElement('span'); count.className = 'ir-pill'; count.textContent = `Evidence ${i + 1}`;
    const level = document.createElement('span'); level.className = 'ir-pill'; level.textContent = row[0];
    const p = document.createElement('p'); p.textContent = row[1];
    metaRow.append(count,level); card.append(metaRow,p); evidence.appendChild(card);
  }

  select.addEventListener('change', () => { index = Number(select.value) || 0; step = 0; renderCase(); });
  reveal.addEventListener('click', () => { if (step < cases[index].evidence.length) { step += 1; renderCase(); } });
  reset.addEventListener('click', () => { step = 0; renderCase(); });
  renderCase();
})();
</script>
