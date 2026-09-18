---
layout: note
title: "Design Knowledge Agents for Knowledge Work"
subtitle: "Coding-agent patterns do not transfer directly to enterprise knowledge work."
date: 2026-09-18
source: "AI Engineer — Benjamin Clavié, Mixedbread"
source_url: https://www.youtube.com/watch?v=O84lhGc1OOI
confidence: medium
summary: "Enterprise knowledge is ambiguous, distributed, and driven by intent. Strong agents need task decomposition, specialist retrieval, the right search primitive, and compact evidence passed to a final decision-maker."
topics:
  - ai_engineering
  - knowledge_agents
  - retrieval
  - agent_orchestration
  - sap_ai
---

Benjamin Clavié makes a useful distinction: a **coding agent is not a general template for every knowledge agent**.

Code is a special kind of knowledge. It has file paths, identifiers, method names, structured dependencies, and many exact strings that are easy to search. Coding tasks are also usually narrow: fix this bug, implement this feature, change this API.

Enterprise knowledge is different. Meaning is often implicit and depends on context. A phrase such as "30 days" may describe a deadline, a grace period, a retention rule, or something unrelated. The agent must first understand what the user is actually trying to decide.

## The practical model

Clavié defines knowledge work as work where information is the main input and the useful output is a judgment, decision, recommendation, or other actionable conclusion.

That changes the agent architecture.

Instead of:

**question → one large search → answer**

use:

**open question → decomposition → specialist searches → short evidence memos → synthesis → human decision**

This is close to how mature knowledge organizations already work. A senior lawyer does not personally search every document. The problem is decomposed, research is delegated, findings are returned in a compact form, and the senior person makes the final judgment.

## Search is not one tool

A second important point is that search tools are different primitives.

- **Exact or lexical search** is useful for identifiers, exact terms, codes, and known phrases.
- **Semantic search** is useful when the wording is different but the meaning is similar.
- **Metadata and filters** are useful when the search space can be reduced by document type, date, owner, system, or another known attribute.
- **Multimodal retrieval** matters when important evidence is inside tables, diagrams, scanned PDFs, or other content that plain text extraction can lose.

The agent should know when to use each primitive. Adding more tools is not the goal. A new tool is useful when it removes a measured quality, cost, or latency ceiling.

## Context is still finite

A huge context window does not remove the retrieval problem.

Real organizations can have years of documentation, tickets, architecture decisions, logs, contracts, policies, code, and operational history. Loading everything is expensive and creates noise.

The better pattern is to retrieve the evidence needed for each sub-question, compress it into a small finding, preserve the source, and pass only the relevant findings to the agent making the final decision.

## Why this matters for SAP

This pattern maps very well to SAP Lead work.

A business question such as "Why are deliveries late?" may require evidence from several domains:

- SD process and configuration;
- ATP or aATP behavior;
- material and business-partner master data;
- purchasing or production dependencies;
- interface, API, IDoc, event, or queue history;
- warehouse execution;
- FI impact;
- previous incidents and design decisions.

A useful SAP agent should not search the whole landscape and immediately produce a confident answer. It should first split the problem into bounded research questions.

For example:

1. **Process agent:** reconstruct the business flow and identify the failing process step.
2. **Configuration agent:** check the relevant configuration and current design rules.
3. **Integration agent:** inspect interfaces, message flow, queues, mappings, and technical evidence.
4. **Master-data agent:** verify whether the decision depends on customer, supplier, material, product, or organizational data.
5. **Cross-process synthesizer:** combine the evidence, expose conflicts, and prepare the decision for the SAP Lead.

The names of the agents are less important than the separation of evidence and responsibility.

## Signal for our workflow

For substantial SAP, architecture, or enterprise-AI research, create a small **knowledge-work packet** before the final answer or implementation:

- business question and expected decision;
- three to five bounded sub-questions;
- authoritative sources for each sub-question;
- short findings with links to evidence;
- confidence and unresolved conflicts;
- cross-process dependencies;
- final synthesis and human decision point.

This is stronger than asking one agent to "research everything" with a long prompt.

A useful operating rule is:

> Do not design enterprise agents as coding agents with more documents. Design the work around evidence, specialization, and decision-making.

## Reported benchmark signal

In the talk, Clavié shows retrieval benchmarks where better search tools reduce the number of tool calls while keeping high accuracy. He also reports that delegated search agents, which return focused memos to the answering agent, reduce part of the gap between an agent and a stronger reference result.

The direction is useful: **better retrieval plus better orchestration can improve both quality and efficiency**.

The exact numbers should not be treated as a universal production benchmark. Mixedbread builds retrieval technology, the examples are bounded evaluation tasks, and real enterprise systems add permissions, stale sources, latency, coordination failures, and governance requirements.

## Assessment takeaway

For a SAP Lead, the important point is not "multi-agent is better." The stronger answer is:

> An SAP problem is usually a knowledge-work problem. I would decompose the business question, retrieve evidence with the right search method, let bounded specialists produce compact findings, and then make the cross-process decision with explicit evidence and human accountability.

**Primary source:** [If we want them to do Knowledge Work, design them as Knowledge Agents](https://www.youtube.com/watch?v=O84lhGc1OOI), Benjamin Clavié, Mixedbread, AI Engineer World's Fair 2026.  
**Conference context:** [AI Engineer — knowledge tools and specialized organizational roles](https://ai.engineer/topics/knowledge-tools-and-specialized-organizational-roles-evolve-together)
