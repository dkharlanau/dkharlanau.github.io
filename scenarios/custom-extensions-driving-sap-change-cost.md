---
layout: default
title: "When SAP custom extensions make change slower and more expensive"
description: "A landscape full of inherited enhancements, sidecar apps, and local exceptions can make every SAP release slower, riskier, and more costly."
permalink: /scenarios/custom-extensions-driving-sap-change-cost/
last_modified_at: 2026-07-25
scenario_cluster: Management & Architecture Decisions
domain: SAP architecture
subdomain: Extension portfolio and clean core
concept_type: business scenario
sap_area: "SAP extensibility / clean core / custom development"
business_process: Cross-process operations
status: reviewed
verified: true
level: 2
last_reviewed: 2026-07-25
author: Dzmitryi Kharlanau
tags:
  - architecture
  - clean-core
  - custom-development
  - transformation
related:
  - /atlas/concepts/sap-extension-retain-rebuild-retire-framework/
  - /atlas/concepts/sap-transformation-recovery-framework/
  - /atlas/concepts/sap-clean-core-strategy/
  - /atlas/concepts/composable-erp-for-sap-operations/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/scenarios/">Scenarios</a></li>
    <li aria-current="page">When SAP custom extensions make change slower and more expensive</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Scenario - Management & Architecture Decisions</p>
    <h1>When SAP custom extensions make change slower and more expensive</h1>
    <p class="note-subtitle">The issue is often not one bad enhancement. It is an unmanaged extension portfolio with no retirement logic.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP extensibility / clean core / custom development</dd></div>
      <div><dt>Indexing</dt><dd>Indexed after review against public SAP and architecture guidance.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Business pain</h2>
    <p>Each release planning cycle starts with uncertainty. Nobody knows which custom reports, exits, sidecar apps, enhancement spots, workflow add-ons, or mapping rules will be affected. The programme wants faster change, but every change now requires extra testing, cross-team review, and post-go-live support. Management begins to ask which custom developments should be removed, retained, or rebuilt, but the organisation lacks a disciplined way to decide.</p>

    <h2>Process context</h2>
    <p>Custom logic enters an SAP landscape for many reasons: local market requirements, gaps in historic standard capability, urgent operational workarounds, or differentiation. Over time those reasons blur. The system remembers the code. The organisation forgets the decision. That is why extension complexity often surfaces during upgrades, carve-outs, S/4 transformations, or provider transitions rather than during the original build.</p>

    <h2>SAP touchpoints</h2>
    <ul>
      <li>ABAP enhancements, BADIs, user exits, reports, Z tables, forms, and custom transactions.</li>
      <li>BTP or side-by-side extensions using APIs, events, workflow, or integration services.</li>
      <li>Custom mapping logic in middleware, message handlers, and validation layers.</li>
      <li>Regression test packs, transport dependency chains, and release approvals.</li>
    </ul>

    <h2>Root causes</h2>
    <ul>
      <li><strong>Historic business exceptions became permanent.</strong> Nobody revisited whether the logic still creates enough value.</li>
      <li><strong>No lifecycle owner exists.</strong> Teams inherit support responsibility without owning the business decision.</li>
      <li><strong>Clean core is treated as relocation.</strong> Logic moves platforms, but the process and support burden remains.</li>
      <li><strong>Retirement was never designed.</strong> Extensions accumulate because removal has no sponsor or measurement.</li>
      <li><strong>Testing and operational readiness lag behind complexity.</strong> Each new extension adds change surface faster than control design catches up.</li>
    </ul>

    <h2>Cost drivers</h2>
    <ul>
      <li>Longer upgrade and release preparation because dependencies are unclear.</li>
      <li>Higher testing effort across process, integration, and sidecar boundaries.</li>
      <li>More specialist support because each extension has unique operating knowledge.</li>
      <li>Delayed simplification because programmes preserve local exceptions by default.</li>
      <li>Duplicate tools and controls because trust in the end-to-end process is low.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Build a portfolio view of extensions by business capability, not only by technical object type.</li>
      <li>For each extension, ask what business rule it protects, who owns that rule, and what would happen if it were removed.</li>
      <li>Measure operating burden: testing effort, support effort, release friction, and integration dependencies.</li>
      <li>Separate truly differentiating logic from historical local preference and emergency workarounds.</li>
      <li>Classify each item into retain, rebuild, replace with standard, or retire.</li>
    </ol>

    <h2>Solution patterns</h2>
    <ul>
      <li>Treat extensions as a portfolio with explicit business case, owner, and retirement path.</li>
      <li>Link clean-core decisions to operating cost, not only to technical compliance.</li>
      <li>Retire low-value exceptions before major transformation waves where possible.</li>
      <li>Rebuild surviving capabilities only when the future operating model is clear.</li>
      <li>Make support, testing, and release readiness part of extension approval.</li>
    </ul>

    <h2>Retain, rebuild, replace, or retire?</h2>
    <div class="decision-table"><table><thead><tr><th>Signal</th><th>Question</th><th>Likely decision direction</th></tr></thead><tbody>
      <tr><td>Business rule is still differentiating and has a named owner</td><td>Can the capability be tested, supported, and upgraded with a clear contract?</td><td>Retain or rebuild with an explicit lifecycle model.</td></tr>
      <tr><td>Standard capability now meets the need</td><td>Is the extension preserving a historical local preference rather than a live control?</td><td>Replace with standard and plan a safe transition.</td></tr>
      <tr><td>Logic is unowned, undocumented, or duplicated</td><td>What business consequence would actually remain if it stopped?</td><td>Investigate retirement before investing in another platform.</td></tr>
      <tr><td>Edge service is proposed for “clean core”</td><td>Who will operate the contract, data, recovery, security, and release path?</td><td>Rebuild only if the operating model is as clear as the technical design.</td></tr>
    </tbody></table></div>

    <h2>AI / automation opportunity</h2>
    <p>AI can help inventory documentation, cluster similar custom patterns, and identify where descriptions are missing. It does not decide whether a rule is still justified. Deterministic inventory, traceability, and testing remain the foundation for any serious extension review.</p>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-extension-retain-rebuild-retire-framework/">SAP Extension Retain, Rebuild, or Retire Framework</a> - A management framework for classifying extension decisions.</li>
      <li><a href="/atlas/concepts/sap-transformation-recovery-framework/">SAP Transformation Recovery Framework</a> - How extension debt becomes programme debt.</li>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> - The architectural boundary, and why it is broader than code placement.</li>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a> - A useful design stance when side-by-side capability is genuinely needed.</li>
    </ul>

    <h2>Verification status and limitations</h2>
    <p>This scenario is a public-safe decision pattern. Specific extension objects, SAP product capabilities, and lifecycle economics vary by release, industry solution, and programme history. Validate object inventories and technical dependencies in your own landscape before acting.</p>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
