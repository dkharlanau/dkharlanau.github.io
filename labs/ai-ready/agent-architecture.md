---
layout: default
title: "AI Ready — Agent Architecture"
description: "A practical guide to workflows, routers, bounded tool loops, orchestration, budgets, approvals, and agent control."
permalink: /labs/ai-ready/agent-architecture/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-04
hide_global_cta: true
tags: [ai, agents, workflow, orchestration, tools, approval]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Agent Architecture</li></ol>
</nav>

# Agent Architecture

An agent is useful when the system cannot know every next step before the task starts. That is the architectural reason to add autonomy. The word *agent* by itself is not a design goal.

If a task always follows the same sequence, a normal workflow is easier to test, operate, and explain. When the next useful action depends on evidence found during the run, a bounded agent can earn its extra complexity.

## Autonomy should grow with the problem

We normally start with the least autonomous shape that can solve the task.

A stable process may need only a deterministic workflow with one model call inside it:

```text
input -> validate -> retrieve -> model -> schema check -> output
```

The model may classify a request, extract fields, or write an explanation, while the application still owns the sequence.

A router adds one model decision when several known paths exist:

```text
request -> router
             |-- research workflow
             |-- coding workflow
             |-- support workflow
             |-- data-analysis workflow
```

The routes are known; only the selection is uncertain.

A tool loop is different. Here the result of one read changes what should happen next:

```text
question
  -> choose an allowed read
  -> validate and execute the tool
  -> inspect evidence
  -> decide: enough / another read / escalate
  -> stop
```

This is the point where an agent becomes more than a routed workflow. The model is controlling part of the path rather than only one decision inside a fixed path.

## The best agent is usually bounded

A useful agent does not need unlimited freedom. It needs enough room to investigate, plus clear limits around that room.

Consider a deployment investigation. We may allow the agent to inspect deployment status, failing job logs, recent changes, environment configuration, dependency health, service events, and relevant runbooks. It can choose the order because each result changes the next useful read.

The same agent does not automatically receive permission to restart production or roll back a release. Finding a suspicious change and executing a corrective action are different capabilities.

This separation gives us a practical architecture:

```text
read -> interpret -> gather more evidence if needed
     -> form a diagnosis
     -> prepare a proposed change
     -> validate
     -> approve
     -> execute through a narrow write path
```

The investigative part may be adaptive. The write path should usually be much more controlled.

## Budgets are part of the design

Without explicit limits, an agent can continue searching long after the useful information has stopped increasing. That increases cost and latency and may also increase risk.

Useful limits include maximum steps, tool calls, wall-clock time, model or token cost, retries, parallel workers, and the set of tools the agent may call. [Token economics](/labs/ai-ready/build-operate/#token-economics) gives the cost-control view: measure cost per successful task, not only tokens per call. Data scope matters just as much: an agent that can read every repository or every customer record has a much larger failure surface than one that can read only the current workspace.

The run also needs explicit stop states. `resolved` is only one of them. `insufficient_evidence`, `permission_denied`, `approval_required`, `tool_failure`, and `budget_exhausted` are legitimate outcomes. A reliable system is allowed to stop without pretending it solved the task.

## Multi-agent designs solve a narrower problem than they appear to

An orchestrator with workers can help when work is genuinely independent and the results can be merged cleanly. For example, one worker may inspect logs, another may check documentation, and another may review recent code changes. The orchestrator then compares the evidence.

That pattern is useful because the work can proceed independently, not because three agents are automatically smarter than one. Workers can repeat the same search, receive overlapping context, disagree without a resolution rule, and multiply latency. If one agent with good tools can do the work clearly, adding more agents usually adds coordination rather than capability.

## Trace the path, not only the answer

An agent can reach a plausible final answer through a poor sequence of actions. That is why the trace matters.

For each step, we want enough information to reconstruct what happened: request or trace ID, model and instruction version, selected tool, sanitized arguments, authorization result, tool status and latency, evidence identifiers, remaining budget, approvals, and the final stop reason.

This is especially important when the agent fails. If two runs produce different conclusions, the trace should show whether the difference came from the model, the retrieved evidence, a tool failure, a permission boundary, or a changed instruction.

## Evaluate the trajectory

Testing only the final sentence misses much of agent behavior. A useful evaluation set should include cases where the first read is enough, evidence conflicts, a relevant tool is forbidden, a tool times out, data is stale, two causes remain possible, a write is required, approval is rejected, or the budget runs out.

We also need hostile content inside tool results. A log line or retrieved document can contain instructions that the agent should treat as data rather than authority.

The questions are practical: Did the agent choose a useful first action? Did it repeat equivalent calls? Did it stop when the evidence was sufficient? Did it escalate when it was not? Did it keep write actions behind the correct control?


## Closed-loop operations need a model of the system

Incident automation becomes much harder when the visible symptom is several dependencies away from the real cause. A failed API, delayed message, or blocked business process can be only the downstream effect.

This creates an important distinction:

```text
observability -> what changed?
causal diagnosis -> what caused the change?
remediation -> what should we change?
verification -> did the system return to the expected state?
```

Correlation helps us find candidates. It is not enough to prove root cause.

For an agent to investigate across a complex environment, it needs more than logs and a large context window. It needs an operational model that connects the important entities: services, applications, interfaces, business objects, recent changes, dependencies, ownership, telemetry, and known operating knowledge.

The model does not need to copy every raw event into the prompt. Its job is to make relationships queryable so the agent can move from symptom to plausible upstream causes, test them against evidence, and prune the paths that do not fit.

### Autonomy is a ladder, not a switch

A useful way to discuss operational autonomy is as a progression. The levels below are an authored adaptation for this lab, not an industry standard.

| Level | Operating pattern | Human role |
|---|---|---|
| 0 | Manual triage and diagnosis | Human investigates and acts |
| 1 | Rules and known runbooks | Human handles novel cases |
| 2 | AI-assisted evidence collection | Human owns diagnosis |
| 3 | Bounded diagnosis for a defined domain | Human verifies the finding and chooses the action |
| 4 | Cross-domain diagnosis and prepared remediation | Human approves high-impact changes |
| 5 | Closed-loop remediation inside a tightly governed domain | Human governs policy, exceptions, and design |

The jump from diagnosis to remediation is the important risk boundary. A system can be very good at investigation and still be unsafe to let it change production state without approval.

### Close the loop with verification

A production agent should not stop at *“I applied the fix.”* The useful completion chain is:

```text
detect
 -> investigate
 -> identify the first causally consistent failure
 -> prepare a remediation
 -> validate / approve
 -> execute
 -> observe the resulting state
 -> verify recovery
 -> close or reopen the investigation
```

Verification should use the business or operational condition that originally mattered. A successful API call, deployment, retry, or configuration update is not proof that the incident is resolved.

### Translate this to SAP operations

The same reasoning works for SAP, although the system model is different.

For a logistics incident, useful relationships may connect:

- business object and document flow;
- current document and item status;
- master-data ownership;
- configuration or determination result;
- IDoc, API, queue, or middleware message;
- EWM or TM execution object;
- recent transport or configuration change;
- FI/CO consequence;
- responsible application or support team.

For example, a delayed outbound delivery can appear as an SD symptom while the first wrong state sits in warehouse execution, transportation planning, an integration queue, or master data. A Lead should not automate a correction until the evidence shows which layer owns the failure.

This supports a conservative SAP autonomy path:

1. **Read-only triage** — gather and normalize evidence.
2. **Causal diagnosis** — compare hypotheses across the dependency chain.
3. **Prepared remediation** — propose the exact retry, data correction, configuration change, or operational action.
4. **Controlled execution** — use normal SAP authorization, approval, and change controls.
5. **Business verification** — prove that the document, message, stock, posting, or downstream process reached the expected state.

Full autonomous remediation should be limited to narrow, reversible, well-observed cases with explicit duplicate protection and rollback or recovery rules.

### Case evidence

A 2026 Traversal talk presents this idea as “self-driving production”: detect an incident, find the root cause, prepare or apply a fix, then verify recovery. Traversal's current public material describes a continuously updated production model and a causal search layer for multi-hop investigations. These are vendor claims and architecture examples, not neutral industry benchmarks.

Sources: [Traversal — Self-Driving Production](https://www.traversal.com/blog/self-driving-production) · [Traversal — Production World Model](https://www.traversal.com/blog/introducing-production-world-model-ai-readable-model-your-entire-production-environment) · [Traversal — Causal Search Engine](https://www.traversal.com/blog/introducing-causal-search-engine-from-correlated-alerts-to-causally-consistent-diagnoses) · [Video case](https://youtu.be/y-OVWZD4j6U?si=ZoQDKWftpF8cNawM)

## A simple rule to remember

Use a workflow when the path is known. Add model routing when the path is known but the choice is messy. Use a bounded agent when the next useful action genuinely depends on what the system discovers.

More autonomy should solve a real uncertainty. Otherwise it is only more moving parts.

## Further reading

- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [System Boundaries](/labs/ai-ready/system-boundaries/) · [Token Economics](/labs/ai-ready/build-operate/#token-economics) · [Agent with Approval Lab](/labs/ai-ready/labs/agent-approval/)
