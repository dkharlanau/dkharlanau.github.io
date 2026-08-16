# Cutover & Hypercare Control Examples

All examples are synthetic.

## Example 1 — Data validation stops cutover

Observed: migration load completes technically.

Checkpoint evidence:
1. Required population reconciliation is outside tolerance.
2. Business validation cannot start reliably.
3. Recovery window is still open.

Decision: HOLD and correct or reload before opening for business.

## Example 2 — Delay without critical-path impact

Observed: one documentation task finishes 40 minutes late.

Evidence:
1. It is not a predecessor of a production step.
2. No checkpoint depends on it.
3. Technical and business validation remain on schedule.

Decision: record deviation but do not escalate as a cutover blocker.

## Example 3 — Forward recovery instead of rollback

Observed: one non-critical interface fails after most irreversible business data is already created.

Evidence:
1. Full rollback would create higher business risk.
2. Failed messages are safely queued.
3. A tested repair and replay path exists.

Decision: continue with explicit forward recovery and monitored backlog.

## Example 4 — Hypercare exit blocked by recurring issue

Observed: total incident volume is low, but one high-impact failure repeats daily.

Evidence:
1. Workaround exists.
2. Root cause is not yet removed.
3. Permanent action has no confirmed implementation date.

Decision: do not exit hypercare until ownership and permanent action are agreed, or obtain explicit risk acceptance for handover.
