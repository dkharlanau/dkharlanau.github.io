---
layout: default
title: SAP Incident Lab
description: Synthetic SAP support cases for testing evidence collection, diagnostic reasoning, source use, and approval boundaries.
permalink: /agent-tools/incident-lab/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
tags: [sap-ams, diagnostics, agent-evaluation, mcp]
---

<section class="section note-detail incident-lab" data-incident-lab>
  <p class="eyebrow">Synthetic agent evaluation</p>
  <h1>SAP Incident Lab</h1>
  <p class="lead">Test whether an agent collects enough evidence, uses the relevant Atlas material, and stops before a controlled SAP action.</p>
  <div class="note-body">
    <p>Every case is synthetic. Do not enter client data, ticket details, credentials, or production identifiers. The browser evaluates text locally against the selected case; it does not contact SAP or send a response to a server.</p>
  </div>

  <div class="incident-lab__layout">
    <section class="incident-lab__panel" aria-labelledby="incident-case-title">
      <label for="incident-case">Synthetic case</label>
      <select id="incident-case" data-case-select></select>
      <p class="incident-lab__meta" data-case-meta></p>
      <h2 id="incident-case-title" data-case-title></h2>
      <p data-case-scenario></p>
      <h3>Known facts</h3><ul data-case-facts></ul>
      <h3>Evidence still needed</h3><ul data-case-missing></ul>
      <h3>Relevant Atlas routes</h3><ul data-case-sources></ul>
    </section>

    <form class="incident-lab__panel" data-response-form>
      <h2>Agent response</h2>
      <p>Use one line per item. A complete loop includes evidence, a bounded hypothesis, verified Atlas URLs, and an explicit approval boundary.</p>
      <label>Evidence collected<textarea name="evidence" rows="5" placeholder="IDoc number&#10;Status history&#10;Error text"></textarea></label>
      <label>Atlas URLs used<textarea name="evidence_refs" rows="3" placeholder="/atlas/diagnostics/sap-idoc-status-diagnostics/"></textarea></label>
      <label>Hypotheses<textarea name="hypotheses" rows="3" placeholder="Application posting error"></textarea></label>
      <label>Proposed actions<textarea name="proposed_actions" rows="3" placeholder="Collect the application log before deciding whether reprocessing is appropriate."></textarea></label>
      <label>Human approval boundary<textarea name="approval_boundary" rows="2" placeholder="A human owner must approve reprocessing after the cause is confirmed."></textarea></label>
      <button type="submit">Evaluate agent loop</button>
    </form>
  </div>

  <section class="incident-lab__result" data-evaluation-result aria-live="polite" hidden></section>
  <p class="incident-lab__footer">Machine-readable cases: <a href="/ai/incident-lab.json">/ai/incident-lab.json</a>. The local SAP Diagnostics MCP exposes <code>list_incident_cases</code>, <code>get_incident_case</code>, <code>evaluate_incident_response</code>, and <code>run_incident_loop</code>.</p>
</section>
<script src="/assets/incident-lab.js" defer></script>
