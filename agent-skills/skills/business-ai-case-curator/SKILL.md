---
name: business-ai-case-curator
description: Use when a public Business AI research candidate must be turned into a structured, review-ready case proposal with canonical graph IDs, explicit evidence claims, limitations, and proof gaps. Do not use to approve or publish a case automatically.
---

# Business AI Case Curator

## Purpose

Convert a source-backed research candidate into a comparable Business AI case proposal without inventing missing implementation facts.

## Use when

- A new public source may describe an AI implementation, foundation, or solution example.
- Existing evidence may materially update a known case.
- A candidate needs canonical process, stage, pattern, technology, and evidence IDs.

## Do not use when

- The source is private, client-confidential, or cannot be attributed.
- The task is to approve or publish a case.
- The source only proves product capability but the requested record claims a business outcome.

## Required inputs

- Candidate source records or public source references.
- `/ai/business-ai-agent-context.json`, pack `case_curator`.
- Current Business AI case schema and review lifecycle.
- Current case, process, stage, pattern, technology, platform, and source IDs.
- Relevant strategic coverage gap when the candidate came from research prioritisation.

## Workflow

1. Resolve the source identity and candidate implementation identity.
2. Check existing case IDs for the same company, implementation, process, and evidence set.
3. Prefer an update proposal when the candidate describes the same implementation.
4. Classify case kind only when the source supports it.
5. Resolve domain, process, stage, AI job, pattern, technology, and platform IDs from canonical indexes.
6. Separate each material statement into source fact, supported inference, runtime proof, unsupported claim, or proof gap.
7. Record reported metrics exactly as reported, including source ownership and disclosed baseline or period.
8. Record data, integration, autonomy, authority, controls, and human review only when supported.
9. Add limitations, transferability questions, failure notes, and missing proof.
10. Propose graph relationships with supporting source IDs. Never add an edge only for completeness.
11. Set the lifecycle state no higher than `review_ready` and produce the reviewer checklist.
12. Return reject or needs-more-evidence when the case cannot meet the next lifecycle gate.

## Decision rules

- Missing evidence stays null, unknown, or a proof gap.
- More fields do not improve evidence grade.
- Vendor capability is not implementation evidence or outcome evidence.
- Runtime proof requires authorised and observed runtime activity.
- A duplicate candidate updates the existing identity instead of creating a second case.
- Unsupported claims cannot remain in a review-ready proposal.

## Output format

Produce a **Business AI Case Proposal** with: candidate identity, duplicate decision, case kind, canonical IDs, implementation summary, autonomy and authority, data and integration boundaries, controls, evidence claims, metrics, source IDs, limitations, proof gaps, transferability, proposed edges, lifecycle state, and reviewer checklist.

## Quality gates

- [ ] Candidate identity and duplicate check are explicit.
- [ ] Every proposed graph ID exists in the supplied context.
- [ ] Source facts and supported inferences are separate.
- [ ] Metrics retain source ownership and claim type.
- [ ] Missing implementation details are not inferred.
- [ ] Limitations and proof gaps are present where evidence is incomplete.
- [ ] Lifecycle state is no higher than `review_ready`.
- [ ] No proprietary or private material is included.

## References

- `references/method.md` — Curation and evidence classification method.
- `references/templates.md` — Structured proposal template.
- `references/examples.md` — Strong, duplicate, weak-source, and missing-metric examples.
