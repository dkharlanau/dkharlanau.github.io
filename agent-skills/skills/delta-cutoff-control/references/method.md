# Method

The core control is an explicit, repeatable data window.

## Delta key
Choose a source signal that really represents relevant change. Creation time may miss updates. Change time may be rewritten. Event offsets may be safer but require durable consumer position. Document-number ranges are not always chronological.

## Window semantics
Record:
- authoritative timezone;
- start value;
- end value;
- whether each boundary is inclusive or exclusive;
- how daylight/timezone conversion is handled if timestamps cross systems.

## Watermark lifecycle
Separate extraction start from accepted watermark. A robust pattern is:
1. read previous accepted watermark;
2. calculate candidate window;
3. extract and apply;
4. reconcile;
5. persist new accepted watermark.

## Late arrivals
Timestamp-driven flows need a strategy for records that become visible after their logical time. Options include overlap/lookback plus deduplication, source change logs, event replay, or periodic full reconciliation.

## Replay
Reprocessing the same window should be safe. Define idempotent target behaviour or a controlled cleanup/reconciliation procedure before replay.

## Cutover
For migrations, connect technical delta windows to business freeze rules. Explicitly cover transactions created during freeze, emergency changes, and late source updates.
