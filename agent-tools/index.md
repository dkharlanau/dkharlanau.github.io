---
layout: default
title: SAP Agent Tools
description: MCP servers, agent skills and machine-readable SAP knowledge for practical SAP work.
permalink: /agent-tools/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
tags: [sap, mcp, agent-tools]
---

<section class="agent-tools-canvas" data-agent-tools>
  <header class="agent-tools-canvas__hero">
    <div>
      <p class="agent-tools-canvas__eyebrow">Knowledge system / Agent tools</p>
      <h1>Find the tool by the SAP job.</h1>
      <p>MCP servers, agent skills, and machine-readable knowledge for investigation, documentation, development, and controlled automation around SAP.</p>
    </div>
    <aside aria-label="Directory boundary">
      <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
      <p><strong>Static public registry.</strong> This directory does not run services, hold credentials, or grant SAP access. Check official documentation before installation.</p>
    </aside>
  </header>

  <nav class="agent-tools-canvas__routes" aria-label="Agent tools routes">
    <a href="/agent-tools/mcp-for-sap-work/"><span>01</span><strong>MCP for SAP work</strong><small>What a tool connection can and cannot do.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/agent-tools/incident-lab/"><span>02</span><strong>Incident Lab</strong><small>Diagnostic material for repeat support work.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/agent-tools/security/"><span>03</span><strong>Security boundaries</strong><small>Credentials, permissions, and production risk.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/agent-tools/skills/"><span>04</span><strong>SAP AI skills</strong><small>Portable instructions for repeatable work.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
  </nav>

  <section class="agent-tool-workbench" aria-labelledby="tool-catalogue-title">
    <header><p class="agent-tools-canvas__eyebrow">Tool catalogue</p><h2 id="tool-catalogue-title">Filter by boundary and capability.</h2></header>
    <form class="agent-tool-filters" aria-label="Filter SAP Agent Tools">
      <label class="agent-tool-filters__search"><span>Search</span><input name="q" type="search" placeholder="CAP, ABAP, documentation" /></label>
      <label><span>Status</span><select name="status"><option value="">All</option><option>official</option><option>community</option><option>experimental</option></select></label>
      <label><span>Domain</span><select name="domain"><option value="">All</option><option>abap</option><option>cap</option><option>ui5</option><option>fiori</option><option>integration-suite</option><option>sap-documentation</option></select></label>
      <label><span>Access</span><select name="access"><option value="">All</option><option>read-only</option><option>mixed</option><option>write-capable</option></select></label>
      <label><span>Location</span><select name="deployment"><option value="">All</option><option>local</option><option>local-http</option><option>remote</option></select></label>
      <label><span>Maturity</span><select name="maturity"><option value="">All</option><option>maintained</option><option>emerging</option><option>experimental</option></select></label>
    </form>
    <div class="agent-tool-workbench__result-head"><p data-tool-count aria-live="polite"></p><p>Read the access and system-modification risk before connecting a tool to a landscape.</p></div>
    <div data-tool-list class="agent-tool-grid" aria-live="polite"></div>
  </section>
</section>
<script src="/assets/agent-tools.js" defer></script>
