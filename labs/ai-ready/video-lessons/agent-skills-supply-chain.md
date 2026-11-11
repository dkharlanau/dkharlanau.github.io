---
layout: default
title: "A Skill File Is Not a Security Review"
description: "How to assess agent skills as software dependencies: transitive code, network behavior, sandboxes and runtime evidence."
permalink: /labs/ai-ready/video-lessons/agent-skills-supply-chain/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, skills, supply-chain, security, prompt-injection, sandbox, video-learning]
career_impact: mapped
career_skills: [ai-security, ai-agents-mcp, delivery-cicd]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# A Skill File Is Not a Security Review

**Source:** Roey Ben Chaim (Zenity / MATS Fellowship), *“You Can't Tell What an Agent Skill Will Do by Reading It”*, AI Engineer, 10 November 2026 (14 min). [Detailed talk notes and chapters](https://www.qabash.com/bash-tv/74559) · [AI Engineer channel](https://www.youtube.com/@aiDotEngineer).

A Markdown file looks harmless. It tells your assistant to run a diagnostics script, install a package or read another instruction file. That second step can fetch another script, which launches another process. A careful reader of the **original** `SKILL.md` may never see the code that actually ran.

This is the video's central warning: **a skill is a supply-chain entry point, not simply a reusable prompt**.

## Why the first file is not the whole story

~~~text
SKILL.md
  -> setup instructions
     -> dependency install
        -> script or plugin
           -> process / filesystem / network / credentials
~~~

Some of these steps are legitimate. A cloud diagnostic tool, for example, may read credentials and query a metadata endpoint for a legitimate purpose. The very same behavior can resemble credential theft. That makes review harder than looking for a few suspicious keywords.

The speaker describes an **agent detonation chamber**: run the skill in an isolated environment, supply safe mocked services to exercise paths, and observe child processes, network access and file operations. This is an investigation approach, not a promise that one scan can distinguish every malicious action.

## A practical trust model

| Layer | Review question | Required control |
| --- | --- | --- |
| Entry instructions | What goal, files, tools and privileges are requested? | Human-readable capability and scope review. |
| Dependencies | Which scripts, versions and child skills will be loaded? | Pin versions, inspect provenance and transitive downloads. |
| Execution | Which commands and child processes actually run? | Isolated sandbox, no production secrets by default. |
| Network | Where can data leave the environment? | Destination policy, egress logs, deny-by-default where possible. |
| State | What files, hooks or scheduled tasks survive the run? | Ephemeral environment and persistence review. |
| Evidence | Can we reconstruct the observed behavior? | Process, filesystem, network and tool-call traces. |

Static analysis is valuable, but **static analysis alone is incomplete**. Also avoid treating all network access as malicious. Classification requires intended purpose, observed behavior, scope and provenance together.

## SAP case: an innocent “BP extract helper”

Suppose a public skill says: *“Help a consultant compare Business Partner data between systems.”* It asks to install a tool that reads local exports and uploads diagnostic logs.

Before installation, ask where the exports go, whether the tool reads other local files, and whether a remote update can change the executable later. A mock extract is enough for initial testing—**never evaluate an untrusted skill using live customer records or productive credentials**.

A useful policy for an SAP diagnostic skill might be:

~~~yaml
skill: bp-reconciliation-helper
scope: synthetic-fixtures-only
filesystem:
  read: ["./fixtures"]
  write: ["./output"]
network:
  mode: denied
execution:
  sandbox: ephemeral
  credentials: none
human_review:
  required_for:
    - new_dependency
    - external_upload
    - write_connector
~~~

This YAML is an **illustrative policy document**, not configuration accepted by a specific agent product. The enforcement must exist in the runtime, operating system, network and credential architecture; prose by itself will not enforce anything.

## 35-minute exercise: inspect without executing

Take a publicly available skill or create a synthetic example. Draw its **dependency closure**: entry file → referenced files → install scripts → packages → external endpoints. Note every unknown.

Then build a short review record: intended purpose, expected commands, observed commands in a safe sandbox, requested network egress, file writes, secrets exposure and final decision. A mismatch is a reason to investigate; it is not automatically proof of compromise.

**Defend this decision:** A popular skill passes a Markdown review but downloads the latest helper code every run. Would you authorize it to read production SAP exports? What must change first?

**Related:** [Security and Governance](/labs/ai-ready/security-governance/) · [Coding Agents Playbook](/labs/ai-ready/coding-agents/) · [Standard Agents](/labs/ai-ready/standard-agents/).

*Evidence boundary: the reported investigations belong to the speaker. This page does not independently validate his sample counts or individual malicious packages. The SAP skill and policy are synthetic. Human review is pending.*
