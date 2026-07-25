---
layout: default
title: "SAP Extension Retain, Rebuild, or Retire Framework"
description: "A management-level framework for deciding which SAP custom developments should be kept, redesigned, replaced, or removed."
permalink: /atlas/concepts/sap-extension-retain-rebuild-retire-framework/
atlas_section: concepts
domain: Business operations
subdomain: SAP architecture and operating model decisions
concept_type: decision framework
sap_area: SAP extensibility and clean core
business_process: Cross-process operations
status: reviewed
verified: true
level: 2
last_reviewed: 2026-07-25
author: Dzmitryi Kharlanau
tags:
  - concepts
  - architecture
  - clean-core
  - custom-development
related:
  - /atlas/concepts/sap-transformation-recovery-framework/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP Extension Retain, Rebuild, or Retire Framework</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Knowledge Atlas</p>
    <h1>SAP extension retain, rebuild, or retire framework</h1>
    <p class="note-subtitle">Clean core decisions are useful only when they reduce future operating friction.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>Business operations</dd></div>
      <div><dt>Type</dt><dd>decision framework</dd></div>
      <div><dt>Reviewed</dt><dd>2026-07-25</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Most extension portfolios are not managed as portfolios. They are inherited. One report, user exit, sidecar app, integration rule, or workflow exception at a time. The result is a landscape where nobody can answer a basic management question: which custom logic still creates enough business value to justify its full lifecycle cost?</p>

    <h2>Symptoms visible to management</h2>
    <ul>
      <li>Every upgrade, release, or rollout triggers a fresh inventory of unknown dependencies.</li>
      <li>Clean core is discussed, but the organisation cannot name which custom logic should survive the programme.</li>
      <li>Support teams know which enhancements are fragile, but architecture forums still treat them as fixed facts.</li>
      <li>Local workarounds become permanent because nobody owns retirement.</li>
    </ul>

    <h2>Why common programmes fail</h2>
    <ul>
      <li>They ask where the code should run before asking whether the rule should still exist.</li>
      <li>They move custom logic off the ERP core without removing the operational burden attached to it.</li>
      <li>They assess technical feasibility but not business differentiation, run cost, supportability, or exit options.</li>
      <li>They classify extensions once during the project and never review them again.</li>
    </ul>

    <h2>What should be assessed</h2>
    <ul>
      <li><strong>Business necessity:</strong> does the extension protect a real differentiator, a legal requirement, or only a historical preference?</li>
      <li><strong>Standard gap maturity:</strong> is the gap still real, or did standard SAP catch up?</li>
      <li><strong>Operational burden:</strong> how much monitoring, testing, support knowledge, access control, and integration recovery does the extension create?</li>
      <li><strong>Change amplification:</strong> how many other components need to change whenever this one changes?</li>
      <li><strong>Retirement feasibility:</strong> what process, data, and ownership work is required to remove it safely?</li>
    </ul>

    <h2>Decision classes</h2>
    <ul>
      <li><strong>Retain:</strong> keep it because the value is clear, the ownership is explicit, and the operating cost is acceptable.</li>
      <li><strong>Rebuild:</strong> keep the capability, but redesign the implementation because the current form creates upgrade or support debt.</li>
      <li><strong>Replace with standard:</strong> use current SAP capability because the historic custom difference no longer justifies itself.</li>
      <li><strong>Retire:</strong> remove the logic because it protects no meaningful business outcome and mostly preserves old habits.</li>
    </ul>

    <h2>Architecture and organisational implications</h2>
    <p>An extension decision is not complete until someone owns the capability, the data consequences, the integration consequences, and the run-state support model. A technically clean rebuild on BTP can still make the operating landscape worse if it adds another runtime with no owner, weak monitoring, and unclear retirement rules.</p>

    <h2>Where AI may help, and where it is the wrong tool</h2>
    <p>AI can help inventory extension documentation, cluster duplicate patterns, and summarize where similar rules appear across a portfolio. It does not replace extension economics, process ownership, regression design, or the business decision to accept standardisation. Deterministic inventory and traceability work should come first.</p>

    <h2>Expected decision outputs</h2>
    <ul>
      <li>An extension portfolio segmented into retain, rebuild, replace, and retire decisions.</li>
      <li>A named owner and lifecycle expectation for each surviving extension.</li>
      <li>A shortlist of custom logic that blocks upgrades or creates disproportionate run cost.</li>
      <li>A retirement backlog tied to measurable complexity reduction.</li>
      <li>A clearer clean-core position grounded in operating reality rather than slogans.</li>
    </ul>

    <p>The useful clean-core question is not "can this be moved out of SAP?" It is "will the business need less expensive coordination after we do it?"</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a></li>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a></li>
      <li><a href="/scenarios/custom-extensions-driving-sap-change-cost/">When SAP custom extensions make change slower and more expensive</a></li>
      <li><a href="/atlas/concepts/sap-transformation-recovery-framework/">SAP Transformation Recovery Framework</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
