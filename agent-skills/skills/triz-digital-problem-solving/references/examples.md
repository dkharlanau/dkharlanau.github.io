# Examples

## Approval bottleneck

A team wants to remove approvals to improve speed, but control and auditability are useful too. Separate by condition: low-risk changes use deterministic validation and automatic approval, while high-risk changes keep human approval. Measure lead time and control exceptions together.

## Integration freshness versus source load

A consumer wants fresher data, but more frequent polling increases source load. Explore events for changed objects, cached projections, or demand-driven reads. Compare freshness with source load, complexity, and failure recovery.

## AI autonomy versus control

An agent should reduce manual work but must not own high-impact authorization. Separate authority: the model reads and proposes, deterministic checks validate, an accountable role approves, and a controlled tool executes. Measure cycle time and unsafe or rejected actions together.
