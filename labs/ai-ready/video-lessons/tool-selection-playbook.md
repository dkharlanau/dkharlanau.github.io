---
layout: default
title: "AI Tool Selection: Choose One Experiment, Not Ten Frameworks"
description: "A grounded field guide to 2026 AI agent engineering tools, with experiments, decision rules, SAP use cases and boundaries."
permalink: /labs/ai-ready/video-lessons/tool-selection-playbook/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, tools, technology, langgraph, phoenix, graphrag, evals, sap, video-learning]
career_impact: mapped
career_skills: [ai-agents-mcp, ai-evaluation, ai-business-value]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# AI Tool Selection: Choose One Experiment, Not Ten Frameworks

**A practical field guide, checked 11 November 2026.** The talks in this series are useful because they show *which problem a tool is supposed to solve*. This page converts that into an adoption decision you can make without committing a project to a new platform.

The default is deliberately conservative: **start with Python/TypeScript, JSON, a small test set and a read-only adapter.** Add a framework after a test shows exactly which missing capability it provides.

## Tool map: what to try, what to check

| When you need... | Candidate and reference | First practical test | Risk / alternative |
| --- | --- | --- | --- |
| Stateful multi-step orchestration | [LangGraph](https://docs.langchain.com/oss/python/learn) | Three nodes: validate → read evidence → decide/stop. Test resume after a failed read. | A fixed Python workflow may be simpler. |
| Traces and evaluation of agent behavior | [Arize Phoenix](https://arize.com/docs/phoenix/) | Record one synthetic run with tool calls, retrieved evidence and a wrong answer. | Traces can contain sensitive data; redact and control access. |
| Versioned prompts, datasets and experiments | [Braintrust](https://www.braintrust.dev/blog) | Compare two candidate instructions on the same reviewed cases. | An evaluation tool cannot establish the ground truth for you. |
| Optimizing prompts from examples | [DSPy / GEPA](https://dspy.ai/learn/optimization/optimizers/) | Optimize a classifier on training cases; measure unseen holdout. | Bad metrics create optimized bad behavior. |
| Relationship-heavy retrieval | [Neo4j GraphRAG](https://neo4j.com/docs/neo4j-graphrag-python/current/) | Trace a synthetic order → BP → replication message dependency with source-backed edges. | Graph construction can invent relationships; do not skip validation. |
| Routing and cost/tenant controls | [LiteLLM](https://docs.litellm.ai/docs/proxy/users) | Apply separate budgets to two test workloads and record allowed vs rejected calls. | Budget enforcement depends on actual database/coordination setup; test fail-open/fail-closed behavior. |
| Self-hosted inference and prefix cache | [vLLM](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) | Measure repeated-prefix latency and throughput with non-sensitive text. | GPU memory, model compatibility and serving operations require real expertise. |
| Domain-specific agent packaging | [Standard Agent Specification](https://standardagentspec.org/) | Package one bounded read-only task on a compatible runtime. | A young specification is not evidence of universal interoperability. |
| Semantic business diagrams | [Visual Workbench](https://github.com/dkharlanau/visual-workbench) | Generate an owned, validated process or dependency diagram. | Do not replace the process owner with a visual model. |
| Exact mappings and lineage | [Mapping as Code](https://github.com/dkharlanau/mapping-as-code) and [Data Relationship Map](https://github.com/dkharlanau/data-relationship-map) | Run a source-target mapping check with synthetic data and record evidence. | LLM explanations cannot replace field-level verification. |

This is a **capability comparison**, not a vendor ranking. Prices, features, SaaS availability, license terms, deployment region and API versions can change. Confirm them from primary product documentation at implementation time.

## Tool choice should follow the workload

### Recipe A — Improve an SAP diagnostics assistant in one afternoon

**Problem:** plausible root-cause answers without a reliable source.

- Create six synthetic cases: stale target BP, unknown interface outcome, missing source attribute, correct data with configuration gap, access denied, and tool timeout.
- Implement read-only mock adapters that return field values, timestamps, and source IDs.
- Use a normal workflow first. If it needs stateful branching and safe interruptions, evaluate LangGraph against that baseline.
- Trace a run. Add Phoenix or an equivalent observability tool only if a trace actually helps identify why an answer was wrong.
- Score correct status, required evidence, unsafe actions and reviewer time.

**Deliverable:** a small experiment report showing whether agent autonomy improved the diagnostic outcome.

### Recipe B — Make AI documentation useful without adding another database

**Problem:** the assistant reads the wrong article and gives a confident explanation.

- Pick 10 real **public** documentation questions, not customer data.
- Identify canonical source pages and test whether exact keyword retrieval finds them.
- Add stable headings, source dates, concise examples and explicit uncertainty.
- Compare lexical, hybrid and — only for table/image-heavy material — multimodal retrieval.
- If the problem is **relationships**, try a minimal graph. If it is wrong chunks or stale versions, a graph database may not help.

**Deliverable:** before/after Hit@3, citation accuracy, and reader success.

### Recipe C — Cut model cost without hiding quality losses

**Problem:** a multi-step agent repeatedly sends large prompts.

- Log prompt version, cached/uncached input, output tokens, tool costs, steps and final accepted outcome.
- Keep a stable shared prefix and re-run the same cases.
- Measure cache hits from the actual provider. Test a small model for narrow classification; keep a more capable model for uncertain analysis if needed.
- If using a gateway, test tenant budgets and overload behavior. Do not assume a cost cap works just because it is present in YAML.

**Deliverable:** cost and latency **per accepted business result**, plus correctness and safety regressions.

## Adoption decisions worth writing down

| If you observe... | Prefer... | Avoid... |
| --- | --- | --- |
| A known path with predictable inputs | Deterministic workflow | Multi-agent orchestration by default |
| Missing context from PDFs and tables | Better document retrieval | Blindly increasing model size |
| A need to trace many related objects | Typed relationship model with evidence | An unverified graph inferred from prose |
| Bad output without failure evidence | Tracing + a small reviewed eval set | Adding more agents before finding the cause |
| Rising inference bills | Caching, fewer steps, task-level budgets | Comparing only advertised price/token |
| A risky SAP write | Separate approved execution path | Letting the LLM decide its own permissions |

## A sample 90-minute architecture exercise

**Simulated customer request:** "Use AI to check 2,000 source/target BP records and tell us which values to change."

1. **20 min:** Define the field-level decision contract and identify exact data owners.
2. **20 min:** Run deterministic equality, mandatory-field and mapping checks on synthetic inputs.
3. **20 min:** Let an LLM explain only unresolved cases, with source references and a no-evidence state.
4. **20 min:** Score explanations against reviewed examples; count human decisions.
5. **10 min:** Recommend an operating model, explicit permissions, the next experiment and success criteria.

A mature recommendation may be **90% ordinary code, 10% AI judgment**. The percentage here is an illustration, not a result. When exact data is available, using less AI can be a stronger solution.

## What this guide does not promise

The guide does not assert these tools are installed, licensed, suitable for regulated workloads, or compatible with every version of SAP S/4HANA. A local self-hosted model does not automatically meet enterprise privacy requirements. A graph package does not automatically validate its facts. A tracing tool does not replace acceptance testing. And a production-ready AI system still needs an accountable human owner.

**Next:** [Video Learning Hub](/labs/ai-ready/video-lessons/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security and Governance](/labs/ai-ready/security-governance/) · [Engineering Handbook](/labs/ai-ready/engineering/).

*Editorial status: working study material, pending human review; noindex. All SAP examples are synthetic. Official tool documentation is referenced for technical capabilities; this page does not reproduce vendor benchmarks as independent proof.*
