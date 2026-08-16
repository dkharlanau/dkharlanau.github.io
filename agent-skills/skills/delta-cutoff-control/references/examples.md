# Examples

All examples are synthetic.

## Example 1: inclusive timestamp overlap
Run 1 selects `changed_at >= 10:00 and <= 11:00`. Run 2 starts with `changed_at >= 11:00`.

Result: records exactly at 11:00 can be extracted twice. Use a half-open window such as `[10:00, 11:00)` and `[11:00, 12:00)`, or keep overlap with explicit deduplication.

## Example 2: watermark advanced too early
Extraction succeeds and watermark advances, but target apply fails halfway.

Next run starts after the failed window and misses unapplied records. Correct design advances the accepted watermark only after apply and required reconciliation succeed.

## Example 3: late source update
A source record has business timestamp 09:30 but becomes visible to extraction at 12:05 because an upstream process completed late.

A strict `changed_at` window may miss it depending on source semantics. Use a trusted change timestamp, lookback overlap, change log, or periodic reconciliation.

## Example 4: cutover emergency transaction
Business freeze starts at 18:00, but one emergency sales order is entered at 18:20 in the old system.

The cutover plan requires a controlled exception log and final delta/reconciliation so the order is not lost between source freeze and target go-live.
