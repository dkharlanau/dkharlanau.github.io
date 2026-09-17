---
layout: note
title: "Harness Engineering Is Not Enough — Keep Human Judgment in the Loop"
subtitle: "Fast implementation is not the same as maintainable software."
date: 2026-09-17
source: "AI Engineer — Dex Horthy, HumanLayer"
source_url: https://www.youtube.com/watch?v=Ib5GBkD555M
confidence: medium
summary: "Coding agents can pass tests while quietly damaging maintainability. The practical response is not less AI, but earlier design decisions and human review for consequential changes."
topics:
  - ai_engineering
  - coding_agents
  - software_architecture
  - agentic_workflows
---

Dex Horthy challenges the idea of a fully autonomous software factory where agents write code, tests pass, and nobody reads the implementation. His main point is simple: **a passing test proves current behavior, not long-term maintainability**.

## The useful idea

Current coding agents are strongly optimized around tasks with visible success conditions: make the change, pass the tests, avoid obvious regressions. Architecture quality is harder to measure. A weak dependency, duplicated concept, poor boundary, or confusing call flow may still pass every test today and become expensive months later.

This creates a dangerous gap:

**fast implementation → green tests → hidden structural debt → expensive change later**

Horthy describes a lights-off experiment at HumanLayer where people stopped reading much of the generated code. The approach worked until a difficult production problem forced humans back into a codebase whose mental model they had stopped maintaining. The lesson is not that coding agents are weak. It is that removing human judgment also removes the team's understanding of why the system has its current shape.

## Move judgment earlier

The practical alternative in the talk is to use AI heavily before and during implementation, while keeping humans involved in the decisions that are expensive to reverse:

1. **Product review** — define the problem, desired behavior, and success signal.
2. **System architecture** — define component boundaries, contracts, data models, and constraints.
3. **Program design** — define important types, method signatures, file changes, call flows, and dependencies.
4. **Vertical slices** — define the implementation order and a verification point after each meaningful slice.
5. **Human review** — review consequential code while the change is still small enough to understand and redirect.

The important shift is from reviewing a large AI-generated result at the end to shaping the solution before the code becomes expensive to change.

## Signal for our workflow

For our repository, large changes should not start with "implement this feature." They should start with a compact design packet: desired outcome, affected system boundaries, important contracts, expected file or call-flow changes, implementation slices, and proof for each slice.

Small, low-risk changes can still be handled directly. The stronger process should be reserved for work where architecture, maintainability, or cross-module behavior matters.

This gives a practical operating rule:

> Use agents to compress implementation time. Do not use that speed as a reason to remove architectural thinking or human ownership of the codebase.

## What remains unproven

The talk is based on direct engineering experience and a real failure case, but it is not a controlled benchmark. The broader claim that this pattern will apply equally to every team or codebase still needs local evidence. The safest interpretation is a workflow signal: test whether earlier design and smaller review slices reduce rework in our own repository.

**Primary source:** [Harness Engineering is not Enough: Why Software Factories Fail](https://www.youtube.com/watch?v=Ib5GBkD555M), Dex Horthy, HumanLayer, AI Engineer World's Fair 2026.  
**Transcript / talk notes:** [AI Engineer](https://www.ai.engineer/talks/Ib5GBkD555M-harness-engineering-is-not-enough-why-software)
