---
layout: default
title: MCP for SAP Integration and OData
description: Boundaries for MCP use around SAP integration and OData services.
permalink: /agent-tools/integration/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---
<section class="section note-detail"><p class="eyebrow">Integration</p><h1>MCP for SAP Integration and OData</h1><p class="lead">An API wrapper becomes an SAP access path when it can reach a tenant or business service.</p><div class="note-body"><p>SAP Integration Suite supports MCP server artifacts, but that does not remove API ownership, authentication, quota, logging, or data-classification obligations. Start with read-only metadata and narrowly scoped APIs. Map each exposed tool to an accountable API owner and a specific authorization scope.</p><p>Never turn an undocumented endpoint into a production agent tool. Treat OData create, update, delete, and action calls as write operations even when a tool description sounds harmless.</p></div></section>
