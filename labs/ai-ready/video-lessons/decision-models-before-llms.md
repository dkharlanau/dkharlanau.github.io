---
layout: default
title: "Not Every Agent Decision Needs a Language Model"
description: "A practical route from rules to classifiers to LLMs, inspired by recursive decision models, with an SAP exception-routing exercise."
permalink: /labs/ai-ready/video-lessons/decision-models-before-llms/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, decision-models, classifiers, routing, cost, latency, sap, video-learning]
career_impact: mapped
career_skills: [ai-business-value, ai-evaluation, ai-agents-mcp]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Not Every Agent Decision Needs a Language Model

**The decision problem:** Calling a large model for exact checks adds expense and uncertainty without improving correctness. Use code for known rules and reserve generation for ambiguous work.

**Source:** Raymond Weitekamp (OpenProse), *“Your Agent Doesn't Need an LLM for Every Decision”*, AI Engineer, 10 November 2026 (52 min). [Searchable transcript](https://ainotes.us/summary/your-agent-doesn-t-need-an-llm-for-every-decision-raymond-weitekamp-openprose) · [AI Engineer channel](https://www.youtube.com/@aiDotEngineer).

Ask a large model: *“Is the interface message status equal to FAILED?”* It might answer correctly. But a string comparison could do the same job faster, cheaper and with predictable behavior.

Ask it: *“Which of these five fixed error categories best fits this short log line?”* A narrow classifier might be appropriate. Ask it: *“Explain the competing causes of a cross-system exception using this evidence.”* Now a language model may earn its cost.

The interesting design question is **which decisions actually need generation**.

## The core distinction

The speaker introduces **recursive decision models (RDMs)**, drawing from fast selection/classification models and recursive-agent ideas. The proposed architecture can ask a small decision model to select an option, call another bounded decision, or delegate an open-ended subtask to an LLM. Context stays outside each small decision call and is supplied selectively.

The presenter uses game and interactive-control demonstrations to illustrate the concept. These are research demonstrations, not evidence of production ERP reliability or a generally available “no-LLM enterprise agent” platform.

| Task | Preferred starting point | Reason |
| --- | --- | --- |
| Check whether a required field exists | Deterministic rule | Exact, cheap and explainable. |
| Compare two source/target values | Deterministic code | Equality should not depend on a model. |
| Route an ambiguous short incident description | Tested classifier | Bounded options, potentially low latency. |
| Explore several plausible root causes | Bounded LLM with source reads | Next evidence step is uncertain. |
| Generate a business-readable incident summary | LLM after validation | Free-form explanation is useful. |
| Execute an SAP update | Authorized deterministic workflow | A model decision is not execution permission. |

A rule is not the same thing as a decision model. Start with ordinary code when the condition is fully specified. Use a classifier only when the input ambiguity makes static rules inadequate.

## Example: a three-stage incident router

~~~text
Incoming incident
  -> Rule gate
       invalid ID?                  -> reject
       explicit processing failure? -> known diagnostic workflow
       ambiguous description?       -> classifier
  -> Classifier with allowed labels
       master_data / configuration / integration / unknown
  -> Confidence and evidence gate
       high enough on tested data?  -> selected read-only workflow
       otherwise                    -> LLM-assisted analysis or human triage
  -> Verified result with source references
~~~

Do not hardcode an arbitrary confidence threshold and call it “safe”. Calibrate routing on representative test cases, include out-of-distribution examples, monitor false routing, and keep an **abstain** state. A very confident model can still be wrong.

## One small contract

~~~json
{
  "incident_id": "SYN-057",
  "rule_result": "unresolved",
  "classifier": {
    "label": "integration",
    "score": 0.71,
    "calibrated": false
  },
  "routing_decision": "human_or_llm_review",
  "allowed_actions": ["read_message_status", "read_business_object"],
  "write_allowed": false
}
~~~

This is a synthetic output for an architecture exercise, not the API of the research system or SAP. The score is deliberately **not** treated as a production probability until calibration has been established.

## Why recursive decisions can go wrong

The approach may lower per-step latency, but recursion creates its own costs: depth limits, context slicing, error accumulation, hidden sub-decisions and operational complexity. A small classifier that misroutes a serious incident can create more work than one good LLM call.

For SAP, the expensive failure is not merely a wrong sentence. It is a wrong business action based on incorrectly classified evidence. A router should **never** bypass the authorization and business control layer.

## 50-minute practical experiment

Create 30 synthetic incidents: ten master-data defects, ten configuration/determination defects, and ten integration failures. Keep descriptions deliberately overlapping.

Evaluate three implementations on the **same cases**:

1. Hand-written rules with an `unknown` fallback.
2. Rules plus a constrained classifier.
3. Rules plus a bounded LLM investigation.

Record routing accuracy, dangerous false classifications, abstentions, time, tool calls, provider cost and reviewer interventions. A higher accuracy score is not enough if the design increases unauthorized writes or hides uncertainty.

**Architect question:** A classifier is cheaper and faster but misroutes 2 of 30 cases. One case would trigger a production master-data change. Can it still be the default router? Separate routing suggestions from execution authority in your answer.

## What this changes in a real architecture

A language model is excellent at synthesis, ambiguity and explanation. It should not become a replacement for equality checks, mappings, validation tables, policy rules or authorization decisions.

The best first implementation may be a **boring workflow with one carefully placed model call**. That is not a failure of agent engineering. It is usually a sign that the right level of autonomy was chosen.

**Related:** [System Boundaries](/labs/ai-ready/system-boundaries/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/).

*Evidence boundary: RDM is the speaker's research and architectural proposal. The SAP routing design is illustrative, not a reported production result. Human review is pending.*
