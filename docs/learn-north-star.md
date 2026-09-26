# Learn North Star

This is the editorial source of truth for Learn. It applies to SAP learning content,
including the existing SAP Enterprise and Assessment routes. Learn names the learning
purpose here; it does not introduce a new route or replace existing URL ownership.

## North Star

Learn is not a place to collect SAP theory.

Its purpose is to build the thinking of a strong SAP Lead: understand how the process works, see dependencies, find the real problem, make good decisions, explain trade-offs, and design a solution that works in the full system.

A good page should make the reader able to understand, reason, decide, explain, and act.

Theory is useful only when it helps with one of these goals.

We do not optimize for the amount of information.
We optimize for the quality of understanding.

## What every Learn page should teach

### See the system.

Understand what is upstream, what is downstream, what owns the behavior, and what can break.

### Find the decision.

Move from “How does SAP work?” to “What decision do I need to make here?”

### Build a mental model.

Explain why the system behaves this way, not only where a field or configuration exists.

### Separate facts from assumptions.

Know what SAP guarantees, what depends on configuration, what depends on data, and what must be verified.

### Think in trade-offs.

A Lead rarely chooses between right and wrong. More often the choice is between different costs, risks, complexity, and flexibility.

### Connect the layers.

Business process, master data, configuration, integration, extensions, analytics, AI, operations, and support belong to one system.

### Diagnose before changing.

Teach how to investigate evidence and narrow the problem before touching configuration or code.

### Explain clearly.

A Lead must be able to explain the same problem to a business user, consultant, developer, architect, and manager.

### Use the knowledge.

The reader should be able to apply the page in an assessment, workshop, incident, design discussion, or real project.

## Editorial test

Before publishing a section, ask:

> «After reading this, will a person only know more — or will they think better?»

If the answer is only “know more”, the section is not finished.

## Applying the North Star

The sections above are the governing North Star. The rules below translate it into
writing and review practice; they are not a mandatory page layout.

### Write for an observable capability

Before drafting, finish this sentence: “After this page, the reader can…” Name a
specific explanation, diagnosis, decision, or action, rather than “knows about” a topic.
Identify the situation in which the capability matters and the decision the page owns.

Use the nine principles as review lenses, not nine headings to paste onto every page.
Do not force every technical layer into every article. Include the layers that change
this decision and link to the existing owner for deeper treatment.

### Keep depth; remove accumulation

Keep configuration, fields, tables, transactions, APIs, and extension details when they
explain behavior, distinguish causes, support a choice, or enable execution. Connect a
technical detail to its purpose, dependency, consequence, or verification step. Do not
replace technical substance with generic advice about leadership.

A useful reference table can support reasoning without repeating an essay in every row.
Explain how to use it and connect it to the owning mental model. Remove or relocate
material that adds neither understanding nor an actionable reference.

### Make the evidence boundary visible

Distinguish source-backed product behavior, configuration-dependent behavior,
data-dependent outcomes, assumptions, and checks still required in the target system.
State deployment and release boundaries where they change the answer. Illustrative
cases must be labeled as examples, not presented as observed project evidence.

For diagnosis, connect symptom → competing explanations → discriminating evidence →
responsible layer → justified change → proof of outcome. Do not jump from a symptom to
a configuration change, or treat the first plausible explanation as a confirmed cause.

For a design choice, explain the viable alternatives, relevant costs and risks, why a
choice fits the stated constraints, and what would make us choose differently. State
who owns the next action and how its result will be checked when these are relevant.

### Review for transfer, not recall

Use a realistic example or reviewer exercise with one changed condition. Ask whether
the reader can still reason to the next step rather than repeat the page's wording.
Keep the exercise in the review record when publishing it would add clutter.

Record the outcome in the PR or editorial handoff, with concrete page anchors or
excerpts, using these five prompts:

| Outcome | Review prompt |
|---------|---------------|
| Understand | Can the reader explain why the behavior occurs and identify its owner and dependencies? |
| Reason | Can the reader separate facts from assumptions and choose evidence that distinguishes plausible causes? |
| Decide | Can the reader compare viable options and explain when the preferred choice should change? |
| Explain | Can the reader give a clear business explanation and connect it to a precise technical explanation? |
| Act | Can the reader name the next step, its prerequisites, and the evidence that would confirm the result? |

For each outcome, record demonstrated evidence or a specific gap to resolve. A heading,
a keyword count, a generic checklist, or a passing build is not proof of understanding.
If a section only increases recall, revise its reasoning, connect it to a useful
reference, or remove it before calling the editorial work complete.

### Preserve meaning in machine reuse

When Learn material is exposed through existing datasets, API exports, or MCP tools,
preserve the decision context, dependencies, evidence, assumptions, trade-offs, and
verification boundaries. Do not turn a conditional explanation into an unconditional
instruction or strip uncertainty from a retrieved answer.

Reuse the existing canonical sources and generators. This North Star does not create
a second content schema, require a machine artifact for every prose edit, or change
publication eligibility. Human review, source verification, indexing policy, and the
repository's existing validation requirements remain in force.
