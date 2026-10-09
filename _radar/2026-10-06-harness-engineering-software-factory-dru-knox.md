---
layout: note
title: "Harness Engineering — From Coding Agent to Software Factory"
subtitle: "Reliable autonomy comes from the system around the agent, not from prompting alone."
date: 2026-10-06
source: "AI Engineer — Dru Knox, Tessl"
source_url: https://www.youtube.com/watch?v=X6l4lpA0_NY
confidence: medium
summary: "Dru Knox frames harness engineering as the work of improving inner, outer, and meta loops so teams can move from interactive coding sessions toward controlled software factories while measuring autonomy, automation, and quality separately."
topics:
  - ai_engineering
  - harness_engineering
  - software_factory
  - coding_agents
  - agentic_workflows
---

Dru Knox presents a useful way to think about the move from coding assistants to a **software factory**.

The key idea is not “use more agents.” It is to build the environment around the agents so they can work with less correction, pass stronger checks, and improve from repeated failures.

That surrounding system is the **harness**.

## The useful model

Knox separates the journey into three dimensions:

1. **Autonomy** — how many corrections the agent needs before it reaches an acceptable result.
2. **Automation** — how much of the workflow can run without a person watching every step.
3. **Quality** — whether the resulting software remains correct, understandable, and safe as more work is delegated.

This separation matters.

A team can have a highly autonomous agent that still needs a human to approve every result. That is high autonomy but limited automation.

A team can also automate many steps while producing weak results. That is automation without enough quality.

The target is not maximum autonomy. The target is a reliable accepted outcome with fewer unnecessary human touchpoints.

## Three loops

Knox explains harness engineering through three loops.

### 1. Inner loop — help the agent correct itself

The inner loop runs while the agent is doing the task.

Typical controls include:

- unit tests;
- linters and type checks;
- local validation;
- explicit repository rules;
- small skills and playbooks;
- deterministic checks where possible.

The goal is simple: the agent should discover obvious mistakes before a pull request reaches a reviewer.

A weak workflow is:

**agent writes → human finds basic error → agent fixes → human checks again**

A stronger workflow is:

**agent writes → local checks fail → agent corrects → checks pass → result moves forward**

This improves autonomy because the agent receives fast feedback inside the task.

### 2. Outer loop — decide whether the result is trustworthy

The outer loop runs around the completed task or pull request.

It can include:

- full regression tests;
- independent review agents;
- browser or end-to-end tests;
- security checks;
- architecture checks;
- screenshots or other evidence;
- human approval for higher-risk changes.

The outer loop is what allows automation to grow.

Without it, the team may have an agent that writes code well but still needs people to inspect everything manually because nobody trusts the result.

### 3. Meta loop — improve the harness itself

The meta loop looks across many runs.

It asks questions such as:

- Which review comments appear again and again?
- Which CI failures repeat?
- Which tasks need the same human correction?
- Which missing rule would have prevented several bad pull requests?
- Which check is producing too many false positives?

The output is not another product feature. The output is a better factory:

- a new test;
- a clearer skill;
- a better lint rule;
- a new verifier;
- a better task template;
- a tighter permission boundary.

This is the most important long-term idea in the talk.

Repeated human correction should become a system improvement.

## Do not automate the whole factory at once

The talk argues for an incremental path.

Pick one recurring workflow. Run it interactively. Observe failures. Add checks. Improve the instructions and tooling. When the workflow becomes predictable, automate more of it.

Then repeat.

A practical progression is:

**interactive agent → repeatable workflow → verified workflow → automated workflow → self-improving workflow**

This is stronger than starting with a large multi-agent design and hoping the architecture will make the work reliable.

## The important organizational point

The technical pieces are not the hardest part.

The difficult part is changing how a team reacts to failure.

The fast response to a bad agent result is often:

> Fix this pull request manually.

The higher-leverage response is:

> Why was this failure possible, and what should change so the next agent run catches it earlier?

That second answer can feel slower today because the engineer has to improve the harness instead of only closing the ticket. But it creates reusable capacity.

This is the same logic as fixing a recurring SAP incident at its root instead of repeatedly clearing the queue.

## Where I would be careful

The factory framing is useful, but several claims should be treated as direction rather than proof.

First, an agent reviewer is not automatically an independent authority. If the coder and reviewer share the same blind spot, the second agent may simply confirm the first one.

Second, more capacity does not mean every backlog item should be implemented. Some work is intentionally deferred because it adds operational risk, maintenance cost, or product complexity.

Third, allowing people outside engineering to create production changes can be valuable, but only when ownership, permissions, testing, and approval rules are explicit.

Finally, fully removing human review is not a safe default for consequential software. A related AI Engineer talk by Dex Horthy argues that tests can pass while maintainability becomes worse over time. The two talks fit together: stronger loops increase useful autonomy, but architecture and human judgment still matter when the cost of a bad decision is high.

## What this means for enterprise and SAP work

The same model can be applied beyond software development.

For an SAP or enterprise workflow, the loops could look like this.

### Inner loop

Fast checks close to the task:

- schema validation;
- mapping validation;
- decision-table checks;
- process-rule checks;
- synthetic test data;
- reconciliation checks;
- interface contract validation;
- mandatory evidence fields.

### Outer loop

Independent acceptance:

- integration testing;
- end-to-end process validation;
- segregation-of-duties checks;
- architecture review;
- security controls;
- business approval;
- cutover readiness checks;
- rollback proof.

### Meta loop

Improvement across repeated work:

- recurring incident patterns become diagnostics;
- repeated mapping defects become validators;
- repeated review comments become rules;
- repeated cutover failures become readiness checks;
- repeated architecture questions become decision records or templates.

This is a useful way to think about enterprise AI: not as an agent that “knows SAP,” but as an agent working inside a controlled engineering system.

## Signal for this lab

The Enterprise Engineering Toolkit already follows part of this logic because it makes process, decisions, interfaces, mappings, reconciliation, transformation, cutover, architecture, visualization, and operations explicit.

The next useful step is to treat those tools not only as separate utilities, but as parts of a harness.

A task should move through a chain where each stage produces an inspectable artifact and the next stage can verify it.

For example:

**process intent → decision rules → interface contract → mapping → reconciliation → architecture decision → cutover evidence → operational feedback**

The meta loop then uses failures and review comments to improve the contracts, templates, checks, and agent skills that control the next run.

That is more valuable than adding another general-purpose coding agent.

## Assessment takeaway

A strong SAP Lead answer is not:

> I would maximize agent autonomy.

A stronger answer is:

> I would separate autonomy, automation, and quality. I would first make the workflow explicit, then add fast inner-loop checks, independent outer-loop validation, and a meta loop that converts recurring failures into reusable controls. I would automate only after the result is measurable and the authority boundaries are clear.

This shows that AI is being treated as part of an engineering operating model, not as a shortcut around governance.

## What remains unproven

The talk is a practitioner view from a company building tools for this category. It gives a useful operating model, but it is not a controlled study proving that the same factory design will work for every team or repository.

Claims about productivity, quality improvement, or reduced review effort should be tested locally with measures such as:

- human corrections per accepted result;
- escaped defects;
- review time;
- rollback rate;
- repeated failure rate;
- cost per accepted change;
- percentage of work that can pass defined checks without manual intervention.

The model is useful because it tells us what to measure and where to improve the system.

**Primary source:** [Harness Engineering: How to Build a Software Factory](https://www.youtube.com/watch?v=X6l4lpA0_NY), Dru Knox, Tessl, AI Engineer.  
**Conference context:** [AI Engineer World's Fair 2026 — Harness Engineering: The New Core Skill for Agentic Developers](https://ai.engineer/worldsfair/schedule).  
**Related signal:** [Harness Engineering Is Not Enough — Keep Human Judgment in the Loop](/radar/harness-engineering-maintainability-human-judgment/).
