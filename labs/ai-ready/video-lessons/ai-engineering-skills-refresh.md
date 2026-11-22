---
layout: default
title: "AI Engineering Skills to Practise and Retest"
description: "An AI Engineer reading pass with hands-on SAP exercises, evidence to keep, and a method for retesting agent skills after a model change."
permalink: /labs/ai-ready/video-lessons/ai-engineering-skills-refresh/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-22
hide_global_cta: true
tags: [ai, video-learning, agent-skills, evaluation, sap]
career_impact: mapped
career_skills: [agent-skill-evaluation, ai-evaluation, ai-agents-mcp]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# AI Engineering Skills to Practise and Retest

**Source pass: 22 November 2026.** This selection draws on the November CODE Summit recordings and one earlier World's Fair session from the [AI Engineer channel](https://www.youtube.com/@aiDotEngineer). Revisit the stack by **22 January 2027**, or sooner after a model, agent runtime, tool contract, or team procedure changes.

A support assistant explains why an SAP integration message (IDoc) failed. The explanation sounds reasonable, but its only source is an old incident note. The current message log is unavailable. A consultant needs to tell which part of the answer is supported, what to check next, and whether the assistant should stop. That is a professional skill. A short `SKILL.md` can teach an agent the team's handoff procedure. An evaluation can show whether the procedure still helps after an upgrade.

## What I would practise from these talks

1. **Turn a repeated procedure into a testable agent skill.** Philipp Schmid proposes checking which requests select a skill and comparing outcomes with it enabled and disabled. For SAP support, give the skill one job, such as drafting a read-only IDoc handoff. Preserve a ticket that matches, a ticket from a different process, and a failure where the evidence is unavailable. Keep the cases and the traces. [Don't Ship Skills Without Evals, 9:03 and 18:46](https://ai.engineer/talks/0vphxNt4wyk-dont-ship-skills-without-evals).
2. **Audit what the model actually learned.** Nikolay Petrov checks individual instructions at the precision the task requires, then reruns complete tasks after editing. A model may know that evidence needs a timestamp and still omit the exact evidence identifier your team requires for a handoff. Preserve one test that fails when that identifier is missing. [Nikolay Petrov on testing what a skill adds, 9:16 and 11:55](https://ai.engineer/talks/yzx4IuEh_tU-your-skill-md-is-70-stuff-model).
3. **Verify the action against its receipt.** Brian Kennedy opens with a judge that accepted a claimed email schedule after the relevant tool call failed. Give the evaluator a fluent diagnosis alongside a failed read and ask it to grade the actual result. Inspect the tool receipt first. Record the false acceptance as a regression case. [Your Judge Is Hallucinating Too, CODE day 1 at 6:11:43](https://ai.engineer/code/2026/talks/brian-kennedy).
4. **Move an invariant into an executable check.** Lydia Hallie uses legacy-session behavior to illustrate how a concrete test can narrow an agent's interpretation of a migration. For a support assistant, let the application enforce read-only access and let a schema require a reference for every supported finding. Preserve a failing test before changing instructions. [Rethinking Claude Code Best Practices, 3:04 and 12:55](https://ai.engineer/code/2026/talks/lydia-hallie).
5. **Improve the workbench before adding orchestration.** Armin Ronacher describes stronger models getting more from a small set of familiar tools. My experiment would start with a local case file, one read-only adapter, and a reviewed result. Add a runtime feature only after a case shows which capability is missing. Keep the before-and-after comparison on the same tasks. [The Software Atelier, CODE day 2 at 0:40:03](https://ai.engineer/code/2026/talks/armin-ronacher).

## The working stack

{% capture skills_stack_table %}
| Learn to do | Start with | Evidence you can show |
| --- | --- | --- |
| Specify an outcome and a stop condition | JSON and JSON Schema, plus a versioned task brief | A failing test for missing evidence and an explicit escalation outcome |
| Verify and diagnose an agent run | Python or TypeScript, a deterministic checker, and tool receipts | A case where plausible prose gets rejected because a read failed |
| Maintain an agent skill | `SKILL.md`, a pinned model/runtime pair, and paired runs | A per-case comparison with the skill enabled and disabled |
| Choose context and tools from observed gaps | A small versioned corpus, a read-only adapter, and an execution trace | A comparison showing which missing source or tool call changed the decision |
{% endcapture %}
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Working AI engineering skills and evidence">
  {{ skills_stack_table | markdownify | replace_first: "<table>", "<table class='study-table__table'>" }}
</div>

Start with the first three rows for the lab below. Use the [Tool Selection Playbook](/labs/ai-ready/video-lessons/tool-selection-playbook/) when a measured gap calls for retrieval, orchestration, or tracing infrastructure. Check adapter, connector, model, and runtime details in the current documentation before each rerun.

## Lab: retest a read-only SAP handoff

1. Run the [five-case SAP support exercise](/labs/ai-ready/video-lessons/#practical-lab-run-the-synthetic-evaluator) to see how deterministic grading handles missing evidence, permission denial, and conflicting records. Open the case JSON and give the agent only the prompt and fixture fields. Keep the expected results and reviewer checks with the grader. The bundled baseline and candidate outputs are synthetic. Replace them with observed outputs for the paired comparison.
2. Give a test agent a short procedure for one job: draft an IDoc handoff using a synthetic message log and an approved runbook. Require a status, supporting evidence IDs, and the next allowed read. If the current log is unavailable, require an unresolved status and a handoff to the evidence owner. Use local fixtures and a read-only tool set.
3. Run the same tasks in clean sessions with the skill available and with it absent. Add one unrelated request to check false activation and hold back a new case until after you edit the skill. Repeat each pair three times for a first pass. Keep model, runtime, fixtures, tools, and settings fixed during a comparison.
4. Count task passes and inappropriate triggers separately. Inspect tool receipts and verify that a failed read produces an unresolved result. Keep raw counts and record time or tokens when the runtime reports them.
5. Write one decision for the current environment. **Keep** rules that protect team-specific behavior or improve outcomes. **Trim** duplicate material when the shorter version preserves the tested behavior and costs less. **Retire** the skill from a tested runtime when that runtime passes the critical and held-out cases without it and satisfies the agreed quality threshold. Keep the tests. When the results vary too much to support a decision, record the uncertainty and retest.

The useful artifact is a short evaluation record that another engineer can rerun. It names the skill revision, model, runtime, case version, any critical failure, and the next review trigger. Take the same record into an interview and explain what changed your decision. The package is available in the repository's `lead-architect` profile. It includes the record template and a synthetic case starter. [Agent Skill Evaluation package](https://github.com/dkharlanau/dkharlanau.github.io/tree/main/agent-skills/skills/agent-skill-evaluation) · [Agent Skills specification](https://agentskills.io/specification).

At the next review, read the current [AI Engineer recordings and transcripts](https://ai.engineer/talks) for a change that affects one of these tasks. Add a case when a talk exposes a failure your tests miss. Change the tools in the stack after a rerun shows what the replacement improves.
