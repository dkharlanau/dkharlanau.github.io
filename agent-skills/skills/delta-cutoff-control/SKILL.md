---
name: delta-cutoff-control
description: Use this skill when incremental data extraction, migration delta, business cutoff, CDC window, replay, or reprocessing needs explicit boundary control. Define delta keys, time windows, watermarks, late arrivals, duplicates, replay, reconciliation, and safe watermark advancement.
---

# Delta / Cutoff Control

## Purpose
Control the boundary between one data or transaction window and the next so incremental processing, migration deltas, and cutovers do not silently lose or duplicate business records.

## Use when
- Designing incremental file, API, event, CDC, or batch extraction.
- Preparing migration deltas or cutover windows.
- Defining a business cutoff for transactional or master data.
- Reprocessing failed time windows.
- Investigating missing or duplicate records around a boundary.

## Do not use when
- The task is a full data migration validation with no delta-window problem.
- The source provides a proven transactional snapshot with no incremental handover.
- The main issue is unknown dataset structure; use `data-discovery-mapping` first.

## Required inputs
- Source population and target scope.
- Candidate delta key or change indicator.
- Source and target timezone assumptions.
- Current watermark or previous successful window.
- Duplicate and business-key rules.
- Cutover/freeze rules where relevant.
- Reconciliation capabilities.

## Workflow
1. Define the business-object population and exclusions.
2. Choose the delta key: creation/change time, sequence, event offset, version, number range, or source change token.
3. Define window start/end, timezone, and inclusive/exclusive semantics.
4. Define watermark storage, advancement, and recovery behaviour.
5. Define late-arrival handling using overlap, lookback, change log, replay, or periodic reconciliation.
6. Define duplicate handling with stable keys and idempotent apply behaviour.
7. Define safe replay for a failed or uncertain window.
8. Define business cutoff, source freeze, open-transaction handling, or delta mode during cutover.
9. Reconcile extracted, applied, rejected, and expected business results.
10. Advance the accepted watermark only when required evidence is complete.

## Decision rules
- Never leave timezone or boundary inclusivity implicit.
- Do not advance watermark merely because extraction finished if apply or reconciliation can still fail.
- A replay strategy is incomplete until duplicate behaviour is understood.
- Late-arrival strategy must be explicit for timestamp-driven deltas.
- Use business keys or stable technical keys to distinguish duplicates from legitimate repeated events.
- For cutover, define how transactions created during freeze or transition are handled.

## Output format
Produce a **Delta / Cutoff Control Record** containing:
- flow and population;
- delta key and timezone;
- window start/end and boundary semantics;
- watermark before/after;
- late-arrival, duplicate, and replay strategies;
- business cutoff and open-transaction handling;
- extracted/applied/rejected counts;
- reconciliation result and exceptions;
- decision to advance watermark and owner.

## Quality gates
- Delta key, timezone, and boundary semantics are explicit.
- Watermark lifecycle is documented.
- Late arrivals, duplicates, and replay are covered.
- Business cutoff includes open transactions or changes during transition.
- Reconciliation exists for high-risk windows.
- Watermark advancement is evidence-based.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
