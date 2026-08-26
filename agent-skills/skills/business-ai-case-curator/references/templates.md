# Template

Use this compact record:

```yaml
candidate_id:
duplicate_decision: new | update | reject
case_kind:
review_state:
canonical_ids:
  process_id:
  process_stage_ids: []
  pattern_ids: []
  technology_family_ids: []
evidence_claims:
  - statement:
    level: source_fact | supported_inference | runtime_proof | unsupported_claim | proof_gap
    source_ids: []
metrics: []
data_dependencies: []
integration_boundaries: []
authority_boundary:
controls: []
limitations: []
proof_gaps: []
transferability_questions: []
proposed_edges: []
reviewer_checklist: []
```

Leave unsupported fields empty and explain the gap. Never use a placeholder that looks like a verified fact.