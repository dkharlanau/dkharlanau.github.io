---
name: business-ai-graph-steward
description: Use when the Business AI graph, evidence coverage, or source freshness needs review and the result should be a small ranked maintenance or research backlog. Distinguishes structural defects from strategic gaps and never invents edges for graph completeness.
---

# Business AI Graph Steward

## Purpose

Keep the Business AI graph structurally trustworthy and turn meaningful coverage gaps into a small, explainable research backlog.

## Use when

- Graph integrity or coverage reports have changed.
- Evidence may be stale.
- A process, stage, decision profile, or pattern has weak case or failure coverage.
- Duplicate or overlapping concepts need human review.

## Do not use when

- The task is to approve case evidence.
- The goal is merely to increase node or edge count.
- A supported canonical change is already known and only needs routine implementation.

## Required inputs

- `/ai/business-ai-agent-context.json`, pack `graph_steward`.
- Current graph contract and graph artifact.
- Graph integrity findings.
- Portfolio coverage and research-priority output.
- Evidence review dates and failure intelligence.

## Workflow

1. Separate structural failures from research and coverage gaps.
2. Resolve every finding to affected canonical IDs.
3. Remove duplicate findings that represent the same root gap.
4. Check whether an apparent orphan is intentionally isolated or truly unusable.
5. Check source freshness without changing evidence grade automatically.
6. Rank process-stage, counter-evidence, control, metric, and failure-coverage gaps by strategic usefulness.
7. Prefer gaps that affect SAP Lead decisions, Enterprise AI architecture, or service proof.
8. For relationship candidates, identify the source evidence needed to justify the edge.
9. Limit the output to a small actionable set.
10. Route structural defects to implementation and evidence gaps to Research Scout or Case Curator.

## Decision rules

- Structural defects have higher priority than cosmetic coverage.
- Graph density is not a quality metric.
- A missing edge is not a defect unless the source model requires that relationship.
- Stale evidence requires review, not automatic removal or promotion.
- Rank a gap by decision usefulness, evidence weakness, and strategic relevance, not page count.

## Output format

Produce a **Graph Steward Queue**. Each item contains: rank, finding type, affected IDs, evidence or coverage signal, why it matters, structural versus research classification, recommended human action, target role, and source needed before any relationship change.

## Quality gates

- [ ] Structural defects and research gaps are separate.
- [ ] Every item names affected canonical IDs.
- [ ] Every proposed relationship states what evidence would justify it.
- [ ] No edge is invented for graph completeness.
- [ ] Stale evidence is flagged without automatic evidence promotion.
- [ ] Queue size is deliberately small and ranked.
- [ ] Healthy graph areas do not produce maintenance work merely to fill the queue.

## References

- `references/method.md` — Prioritisation method.
- `references/templates.md` — Queue template.
- `references/examples.md` — Stale, orphan, weak-coverage, and healthy examples.
