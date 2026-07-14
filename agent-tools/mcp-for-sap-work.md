---
layout: default
title: What MCP Means for SAP Work
description: A practical boundary for Model Context Protocol use in SAP delivery and support.
permalink: /agent-tools/mcp-for-sap-work/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---

<section class="section note-detail"><p class="eyebrow">MCP primer</p><h1>What MCP means for SAP work</h1><p class="lead">MCP is a way for an AI client to discover and call tools. It does not make a tool safe, accurate, or authorized.</p><div class="note-body"><h2>Useful first use</h2><p>Start with Level 0 knowledge: static Atlas records, documentation, and local project context. These reduce repeated retrieval work without exposing a live SAP tenant.</p><h2>Where the boundary changes</h2><p>An MCP tool that reads an ABAP system or Integration Suite tenant crosses into remote access. A tool that creates, activates, transports, or posts business data crosses into a write boundary. Treat those as a normal privileged integration, not as chat convenience.</p><h2>Decision rule</h2><p>Use an MCP server only when its owner, transport, tool list, data path, permissions, and audit trail are understood. Keep the smallest tool set enabled for the task.</p></div></section>
