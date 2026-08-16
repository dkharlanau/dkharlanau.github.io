# Decision Facilitation Examples

All examples are synthetic.

## Example 1 — API or event

Decision: choose how a downstream system should receive order-status changes.

Options:
1. synchronous API pull
2. event publication
3. scheduled file extract

Key trade-off: freshness and loose coupling versus operational complexity and consumer capability.

Missing evidence: consumer volume and tolerance for delayed updates.

Result: DEFERRED until volume and latency requirements are measured. Owner and deadline recorded.

## Example 2 — AI approval boundary

Decision: allow an AI agent to execute customer-data changes automatically or require approval.

Constraint: policy requires accountable approval for high-impact changes.

Options:
1. agent proposes, human approves, deterministic tool executes
2. agent executes only low-risk changes under a strict rule set

Result: choose a risk-tiered authority model rather than debating whether "AI is accurate enough" in general.

## Example 3 — Release go/no-go

Decision: release with one known reporting defect or delay the complete package.

Evidence:
- core transaction path is unaffected
- workaround exists
- report owner accepts temporary limitation
- fix is scheduled

Result: CONDITIONAL GO using `release-readiness`; decision facilitation records the owner and rationale.

## Example 4 — Fake option diversity

Observed: meeting compares three integration products, all implementing the same synchronous point-to-point API design.

Facilitation action: treat them as one system-shape option and add materially different alternatives before vendor comparison.

Lesson: vendor choice and architecture choice are different decisions.
