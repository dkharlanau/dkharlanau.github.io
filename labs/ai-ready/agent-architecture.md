---
layout: default
title: "AI Ready — Agent Architecture"
description: "A practical guide to workflows, routers, bounded tool loops, orchestration, budgets, approvals, and agent control."
permalink: /labs/ai-ready/agent-architecture/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
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

Useful limits include maximum steps, tool calls, wall-clock time, model or token cost, retries, parallel workers, and the set of tools the agent may call. Data scope matters just as much: an agent that can read every repository or every customer record has a much larger failure surface than one that can read only the current workspace.

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

## A simple rule to remember

Use a workflow when the path is known. Add model routing when the path is known but the choice is messy. Use a bounded agent when the next useful action genuinely depends on what the system discovers.

More autonomy should solve a real uncertainty. Otherwise it is only more moving parts.

## Further reading

- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [System Boundaries](/labs/ai-ready/system-boundaries/) · [Agent with Approval Lab](/labs/ai-ready/labs/agent-approval/)
