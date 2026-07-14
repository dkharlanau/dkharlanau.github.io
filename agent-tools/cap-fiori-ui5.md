---
layout: default
title: MCP for CAP, Fiori and UI5
description: A controlled local-project workflow for CAP and UI5 MCP tools.
permalink: /agent-tools/cap-fiori-ui5/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---
<section class="section note-detail"><p class="eyebrow">Application development</p><h1>MCP for CAP, Fiori and UI5</h1><p class="lead">Use project-aware tools to retrieve current model and framework context before asking an agent to change code.</p><div class="note-body"><p>The CAP and UI5 servers are local development tools. Their value is precise project and framework context, not unrestricted code generation. Run UI5 lint or manifest validation after a change, review the diff, and keep service credentials outside the MCP configuration.</p><p>For Fiori/OData work, distinguish design-time metadata from a live business-service call. The former can stay local; the latter needs a separately approved integration boundary.</p></div></section>
