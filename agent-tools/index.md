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

<section class="section agent-tools" data-agent-tools>
  <p class="eyebrow">Knowledge &amp; tools</p>
  <h1>SAP Agent Tools</h1>
  <p class="lead">MCP servers, agent skills and machine-readable SAP knowledge for practical SAP work.</p>
  <p>This directory is a static, reviewed registry. It does not run services, hold credentials, or grant SAP access. Check each tool's official documentation before installation.</p>
  <p><a href="/agent-tools/mcp-for-sap-work/">What MCP means for SAP work</a> · <a href="/agent-tools/connect/">Connection boundaries</a> · <a href="/agent-tools/security/">Security and production risks</a> · <a href="/agent-tools/skills/">SAP AI skills</a></p>
  <form class="agent-tool-filters" aria-label="Filter SAP Agent Tools">
    <label>Search <input name="q" type="search" placeholder="CAP, ABAP, documentation"></label>
    <label>Status <select name="status"><option value="">All</option><option>official</option><option>community</option><option>experimental</option></select></label>
    <label>Domain <select name="domain"><option value="">All</option><option>abap</option><option>cap</option><option>ui5</option><option>fiori</option><option>integration-suite</option><option>sap-documentation</option></select></label>
    <label>Access <select name="access"><option value="">All</option><option>read-only</option><option>mixed</option><option>write-capable</option></select></label>
    <label>Location <select name="deployment"><option value="">All</option><option>local</option><option>local-http</option><option>remote</option></select></label>
    <label>Maturity <select name="maturity"><option value="">All</option><option>maintained</option><option>emerging</option><option>experimental</option></select></label>
  </form>
  <p data-tool-count aria-live="polite"></p>
  <div data-tool-list class="agent-tool-grid"></div>
</section>
<script src="/assets/agent-tools.js" defer></script>
