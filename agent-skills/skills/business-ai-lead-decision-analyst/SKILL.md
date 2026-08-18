---
name: business-ai-lead-decision-analyst
description: Use when a Business AI or ERP architecture question needs a Lead-level recommendation traced through process, SAP context, controls, authority, evidence, counter-evidence, metrics, and proof gaps. Do not use for generic vendor comparison or unsupported autonomous action advice.
---

# Business AI Lead Decision Analyst

## Purpose

Turn a business or architecture question into a traceable Lead decision record instead of a generic AI recommendation.

## Use when

- A team must decide where AI should assist in an ERP process.
- A document, copilot, agent, or prediction pattern needs process and control analysis.
- The question involves SAP logistics, sales, procurement, data, integration, or operational authority.

## Do not use when

- The task is only factual SAP configuration lookup.
- No business decision is being made.
- The requested recommendation depends on private evidence that cannot be used.

## Required inputs

- Business question and expected outcome.
- `/ai/business-ai-agent-context.json`, pack `lead_decision_analyst`.
- Relevant process, stage, SAP capability, case, decision-profile, failure, metric, and source IDs.
- Known business rules, authority owner, and constraints.

## Workflow

1. Define the business problem, process boundary, and decision owner.
2. Resolve the relevant graph path and canonical IDs.
3. Separate deterministic rules from tasks suitable for probabilistic assistance.
4. Identify data and system-of-record dependencies.
5. Identify integration boundaries and possible side effects.
6. Build materially different options, including a lower-autonomy option where relevant.
7. Allocate read, propose, validate, approve, and execute authority for each option.
8. Attach required controls and human review.
9. Gather supporting cases, challenging evidence, failure patterns, limitations, and proof gaps.
10. Compare metrics and exit criteria without treating reported correlation as causation.
11. Weaken the recommendation when evidence or ownership is weak.
12. Produce the recommendation, assumptions, experiment or rollout boundary, and conditions that would change the decision.

## Decision rules

- Vendor capability is not proof of business value.
- Model confidence is not business authority.
- Exact pricing, tax, credit, posting, hard constraints, identity, and approval rules stay deterministic when the business rule is deterministic.
- High-impact side effects require explicit accountable approval unless evidence supports a different approved authority model.
- Supporting and challenging evidence must be visible together.
- Runtime proof may be claimed only when authorised runtime activity was observed.

## Output format

Produce a **Lead Decision Record** with: problem boundary, graph path, options, trade-offs, deterministic rules, data dependencies, integration boundaries, authority matrix, controls, supporting evidence, challenging evidence, metrics, exit criteria, proof gaps, recommendation, assumptions, and decision-change triggers.

## Quality gates

- [ ] Material claims trace to canonical IDs or are labelled assumptions.
- [ ] At least two materially different options are compared when a choice exists.
- [ ] Deterministic business rules are not delegated to probabilistic reasoning without justification.
- [ ] Authority is separated into read, propose, validate, approve, and execute.
- [ ] Supporting and counter-evidence are both considered.
- [ ] Weak evidence produces a conditional or narrower recommendation.
- [ ] Metrics and exit criteria are explicit.
- [ ] No invented runtime proof is present.

## References

- `references/method.md` — Decision and evidence method.
- `references/templates.md` — Lead Decision Record template.
- `references/examples.md` — Sales, Procurement/Logistics, and Integration/AI examples.
