# Template

```yaml
queue:
  - rank: 1
    type: structural_defect | research_gap | stale_evidence | relationship_review
    affected_ids: []
    signal:
    why_it_matters:
    priority_reason:
    evidence_required:
    recommended_human_action:
    target_role:
```

Keep the queue small. Prefer a few items with a clear decision impact over a large inventory of minor gaps. A relationship-review item is not permission to add an edge; it is a request to establish the supporting evidence first.