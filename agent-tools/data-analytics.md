---
layout: default
title: MCP for SAP Data and Analytics
description: Safe evaluation boundaries for data and analytics MCP tools.
permalink: /agent-tools/data-analytics/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---
<section class="section note-detail"><p class="eyebrow">Data &amp; analytics</p><h1>MCP for SAP data and analytics</h1><p class="lead">Metadata discovery and live analytical data need different controls.</p><div class="note-body"><p>For HANA, Datasphere, BW, or Analytics Cloud, start with a schema and lineage question, then decide whether remote data access is justified. Use service identities with least privilege, bounded query cost, row-level restrictions, and auditable output. Do not pass personal, financial, or operational data through an agent without a data-owner decision.</p><p>The initial registry does not yet recommend a general-purpose data MCP server. That is intentional until ownership, API support, and security posture can be reviewed per product.</p></div></section>
