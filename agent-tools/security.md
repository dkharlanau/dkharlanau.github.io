---
layout: default
title: MCP Security and Production Risks for SAP
description: A least-privilege security model for SAP-related MCP tools.
permalink: /agent-tools/security/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---

<section class="section note-detail"><p class="eyebrow">Security</p><h1>MCP security and production risks</h1><p class="lead">An agent can be influenced by untrusted content while an MCP server may hold real authority. Keep those concerns separate and explicit.</p><div class="note-body"><h2>Access levels</h2><ol><li><strong>Level 0:</strong> static public knowledge.</li><li><strong>Level 1:</strong> local project read.</li><li><strong>Level 2:</strong> remote SAP system read.</li><li><strong>Level 3:</strong> development write.</li><li><strong>Level 4:</strong> business or production write.</li></ol><h2>Default policy</h2><p>Default deny, read-only first, least privilege, separate development and production credentials, and explicit human approval for every write-capable operation. No secret belongs in a repository, prompt, static site, or client configuration checked into version control.</p><h2>Review before connection</h2><p>Inspect dependencies and licenses; verify the maintainer and repository state; enumerate tools; disable unused tools; confirm telemetry; and test against non-production data. Prompt injection in repository text or retrieved documents must never be allowed to override these boundaries.</p></div></section>
