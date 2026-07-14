---
layout: default
title: SAP AI Skills Directory
description: Portable, evidence-first skills for recurring SAP support and diagnostic work.
permalink: /agent-tools/skills/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---

<section class="section note-detail"><p class="eyebrow">Portable procedures</p><h1>SAP AI Skills Directory</h1><p class="lead">These skills turn common SAP support patterns into repeatable, bounded procedures.</p><div class="note-body"><p>The source of truth is <code>agent-skills/skills/</code>; generated Codex and Claude exports are not edited by hand. The SAP AMS profile now includes incident triage, IDoc, BP replication, P2P, O2C, MDG, interface monitoring, evidence collection, and MCP tool selection.</p><h2>Operating rule</h2><p>Use reviewed Atlas content for diagnostic context, official SAP documentation for product facts, and MCP tools only when authorization exists. A write-capable MCP tool requires explicit human approval.</p><p>Validate changes with <code>python3 agent-skills/exporters/validate_agent_skills.py</code> before generating an export.</p></div></section>
