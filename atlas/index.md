---
author: "Dzmitryi Kharlanau"
layout: default
title: "Knowledge Atlas — SAP, Operations, Data, Automation, and AI Support Concepts"
description: "Curated Knowledge Atlas for business, SAP, operations, data, automation, and AI-assisted support concepts."
permalink: /atlas/
last_modified_at: 2026-07-24
status: reviewed
verified: true
tags:
  - sap-ams
  - diagnostics
  - ai-operations
  - data-quality
  - automation
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/ai-operations/ai-agent-for-sap-support/
  - /atlas/data-quality/sap-master-data-quality/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li aria-current="page">Knowledge Atlas</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Knowledge Atlas</p>
  <h1>Business, SAP, operations, data, automation, and AI-assisted support concepts.</h1>
  <p class="lead">A curated working atlas for concepts that matter during SAP support, process analysis, operational memory work, side-by-side AI design, and management-level SAP decisions. It is intentionally small: reviewed pages first, raw research notes kept private.</p>
  <div class="atlas-hero__actions">
    <a class="button button--primary" href="/atlas/concepts/">Explore concepts</a>
    <a class="button" href="/atlas/diagnostics/">Open diagnostics</a>
    <a class="button" href="/atlas/ai-operations/">AI operations</a>
  </div>
</section>

<section class="section atlas-pathfinder" data-atlas-pathfinder aria-labelledby="pathfinder-title">
  <header class="section-heading">
    <p class="eyebrow">Interactive diagnostic map</p>
    <h2 id="pathfinder-title">Start from the operating question.</h2>
    <p class="lead">Choose the question that best describes the work in front of you. The map points to the Atlas area that helps structure the next check.</p>
  </header>
  <div class="atlas-pathfinder__layout">
    <div class="atlas-pathfinder__steps" role="tablist" aria-label="Diagnostic starting points">
      <button class="atlas-pathfinder__step is-active" id="atlas-path-blocked" type="button" role="tab" aria-selected="true" aria-controls="pathfinder-panel" data-path-icon="troubleshoot" data-path-title="A business process is blocked" data-path-detail="Start with the observable symptom, the affected business outcome, and the point where the expected process stops moving." data-path-link="/atlas/diagnostics/" data-path-link-label="Open diagnostic patterns">
        <span class="material-symbols-outlined" aria-hidden="true">troubleshoot</span><span>Blocked outcome</span>
      </button>
      <button class="atlas-pathfinder__step" id="atlas-path-data" type="button" role="tab" aria-selected="false" aria-controls="pathfinder-panel" data-path-icon="database" data-path-title="The data cannot be trusted" data-path-detail="Trace the critical object, its owner, validation point, activation state, and downstream use before treating the issue as a local data fix." data-path-link="/atlas/data-quality/" data-path-link-label="Open data-quality patterns">
        <span class="material-symbols-outlined" aria-hidden="true">database</span><span>Data signal</span>
      </button>
      <button class="atlas-pathfinder__step" id="atlas-path-handoff" type="button" role="tab" aria-selected="false" aria-controls="pathfinder-panel" data-path-icon="account_tree" data-path-title="A handoff fails between systems or teams" data-path-detail="Separate source, mapping, transport, target, recovery, and ownership evidence before assuming that an interface status explains the business result." data-path-link="/atlas/maps/" data-path-link-label="Open dependency maps">
        <span class="material-symbols-outlined" aria-hidden="true">account_tree</span><span>Broken handoff</span>
      </button>
      <button class="atlas-pathfinder__step" id="atlas-path-action" type="button" role="tab" aria-selected="false" aria-controls="pathfinder-panel" data-path-icon="fact_check" data-path-title="The team needs a controlled next move" data-path-detail="Turn the investigation into a clear decision, owner, review point, and reusable operating artefact rather than a one-off recovery." data-path-link="/atlas/automation/" data-path-link-label="Open automation and operating-memory patterns">
        <span class="material-symbols-outlined" aria-hidden="true">fact_check</span><span>Controlled action</span>
      </button>
    </div>
    <article class="atlas-pathfinder__panel" id="pathfinder-panel" role="tabpanel" tabindex="0" aria-labelledby="atlas-path-blocked" aria-live="polite">
      <span class="atlas-pathfinder__panel-icon material-symbols-outlined" aria-hidden="true" data-path-output-icon>troubleshoot</span>
      <p class="eyebrow">Suggested starting point</p>
      <h3 data-path-output-title>A business process is blocked</h3>
      <p data-path-output-detail>Start with the observable symptom, the affected business outcome, and the point where the expected process stops moving.</p>
      <a class="button button--primary" href="/atlas/diagnostics/" data-path-output-link>Open diagnostic patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </article>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Sections</p>
    <h2>Curated entry points</h2>
    <p class="lead">Each section is designed as an editorial surface, not a dump of draft notes. Pages are added only after they are useful, conservative, and safe to expose publicly.</p>
  </header>

  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/concepts/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">lightbulb</span>
      <h2>Concepts</h2>
      <p>Business and SAP concepts explained from the operational problem outward.</p>
      <span class="link-arrow">Open concepts</span>
    </a>
    <a class="atlas-card" href="/atlas/maps/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">account_tree</span>
      <h2>Maps</h2>
      <p>Process, document-flow, data dependency, and cross-domain navigation maps.</p>
      <span class="link-arrow">Open maps</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">settings</span>
      <h2>SAP Notes</h2>
      <p>Curated SAP configuration and support explanations with conservative boundaries.</p>
      <span class="link-arrow">Open SAP section</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">troubleshoot</span>
      <h2>Diagnostics</h2>
      <p>Support-oriented diagnostic patterns for repeat incidents and process blockers.</p>
      <span class="link-arrow">Open diagnostics</span>
    </a>
    <a class="atlas-card" href="/scenarios/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">conversion_path</span>
      <h2>Scenarios</h2>
      <p>Business pain mapped to SAP process context, cost drivers, and diagnostic workflows.</p>
      <span class="link-arrow">Open scenarios</span>
    </a>
    <a class="atlas-card" href="/atlas/ai-operations/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">psychology</span>
      <h2>AI Operations</h2>
      <p>AI-assisted support, operational memory, governance, and human review patterns.</p>
      <span class="link-arrow">Open AI operations</span>
    </a>
    <a class="atlas-card" href="/atlas/ai-tools/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">terminal</span>
      <h2>AI Tools</h2>
      <p>Repository context packaging, coding agents, MCP, AI code review, testing, and security.</p>
      <span class="link-arrow">Open AI tools</span>
    </a>
    <a class="atlas-card" href="/atlas/data-quality/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">database</span>
      <h2>Data Quality</h2>
      <p>Master data, quality signals, governance failure modes, and operational data problems.</p>
      <span class="link-arrow">Open data quality</span>
    </a>
    <a class="atlas-card" href="/atlas/automation/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">precision_manufacturing</span>
      <h2>Automation</h2>
      <p>Support automation, operational memory, agentic workflows, and developer automation patterns.</p>
      <span class="link-arrow">Open automation</span>
    </a>
    <a class="atlas-card" href="/atlas/research-notes/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">science</span>
      <h2>Research Notes</h2>
      <p>Noindex working area for material that is useful but not ready to be treated as polished expert content.</p>
      <span class="link-arrow">Open research notes</span>
    </a>
    <a class="atlas-card" href="/atlas/links/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">link</span>
      <h2>Links</h2>
      <p>Reference routes to profile, services, datasets, and future curated sources.</p>
      <span class="link-arrow">Open links</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Pilot Pages</p>
    <h2>Reviewed first pages</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/concepts/sap-atp-is-not-inventory/">
      <h3>SAP ATP Is Not Inventory</h3>
      <p>A practical distinction between stock visibility and customer promise logic.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-pricing-procedure-debugging/">
      <h3>SAP Pricing Procedure Debugging</h3>
      <p>A conservative troubleshooting frame for pricing issues in sales documents.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">
      <h3>SAP Sales Order Block Diagnosis</h3>
      <p>How to separate master data, credit, delivery, billing, and incompletion causes.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/concepts/order-to-cash/">
      <h3>Order to Cash</h3>
      <p>The operating chain from customer demand to billing and cash collection.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/ai-operations/ai-agent-for-sap-support/">
      <h3>AI Agent for SAP Support</h3>
      <p>A grounded pattern for retrieval, diagnosis, escalation, and human approval.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/data-quality/sap-master-data-quality/">
      <h3>SAP Master Data Quality</h3>
      <p>How weak master data turns into repeated SAP support issues.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/automation/operational-memory-for-sap-ams/">
      <h3>Operational Memory for SAP AMS</h3>
      <p>Runbooks, KEDB, and structured support knowledge for repeat incidents.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-idoc-diagnostics/">
      <h3>SAP IDoc Diagnostics</h3>
      <p>Trace an IDoc failure from creation and dispatch through receipt and application posting.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-authorization-diagnostics/">
      <h3>SAP Authorization and Role Diagnostics</h3>
      <p>Separate missing authorization objects, organizational values, profile generation, and user-context issues.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-transport-governance-diagnostics/">
      <h3>SAP Transport Governance Diagnostics</h3>
      <p>Investigate queue conflicts, dependency order, approval gaps, and parallel changes before re-importing.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/concepts/sap-ams-cost-reduction-framework/">
      <h3>SAP AMS Cost Reduction Framework</h3>
      <p>A management-level lens for separating visible ticket reduction from real operating simplification.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/concepts/sap-extension-retain-rebuild-retire-framework/">
      <h3>SAP Extension Retain, Rebuild, or Retire Framework</h3>
      <p>Classify custom logic by business value, operating burden, and retirement potential.</p>
      <span class="link-arrow">Read page</span>
    </a>
    <a class="atlas-card" href="/atlas/concepts/enterprise-ai-around-sap-decision-framework/">
      <h3>Enterprise AI Around SAP Decision Framework</h3>
      <p>Decide where AI should assist, where automation should stay deterministic, and where neither is the real issue.</p>
      <span class="link-arrow">Read page</span>
    </a>
  </div>
</section>

<section class="section">
  <div class="section-shell section-shell--flat">
    <header class="section-heading">
      <p class="eyebrow">Context</p>
      <h2>How this Atlas should be read</h2>
    </header>
    <p class="lead">The Atlas is not official SAP documentation and it is not a replacement for system-specific analysis. It is a structured way to capture practical concepts, diagnostic questions, and operating patterns that help teams reason about SAP-heavy environments.</p>
    <div class="section-actions">
      <a class="button" href="/about/">Author profile</a>
      <a class="button" href="/services/sap-ams-consulting/">SAP AMS consulting</a>
      <a class="button" href="/services/sap-ai-ml-enablement/">SAP AI enablement</a>
      <a class="button" href="/ai/practical-ai-for-sap-support/">Practical AI for SAP support</a>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Related</p>
    <h2>Related Atlas pages</h2>
  </header>
  <ul>
    <li><a href="/atlas/concepts/order-to-cash/">Order to Cash concept</a></li>
    <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI agent for SAP support</a></li>
    <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP master data quality</a></li>
    <li><a href="/atlas/concepts/sap-ams-cost-reduction-framework/">SAP AMS Cost Reduction Framework</a></li>
  </ul>
</section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
