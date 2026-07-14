---
layout: default
title: Using SAP Atlas from AI Agents
description: Retrieval contract for using reviewed SAP Atlas material from agents.
permalink: /agent-tools/atlas-agents/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---
<section class="section note-detail"><p class="eyebrow">Agent-readable knowledge</p><h1>Using SAP Atlas from AI agents</h1><p class="lead">Start from reviewed records only, preserve the URL and review state, and state the limits of the material.</p><div class="note-body"><p>Use <a href="/atlas/manifest.json">the Atlas manifest</a>, <a href="/ai/atlas-compact-index.json">compact index</a>, <a href="/ai/rag/related.json">related-topic graph</a>, and <a href="/ai/verified-pages.json">verified-page inventory</a>. These are static public files generated from canonical Markdown frontmatter. Do not mix noindex candidate pages into trusted retrieval results.</p><p>Return the canonical URL, verification status, last-reviewed date, relevant evidence, and uncertainty. Product facts should be checked against official SAP documentation; Atlas is a diagnostic frame, not a substitute for an SAP system record.</p></div></section>
