# Examples

## Stale evidence

A case has a valid graph path but its source review is older than the freshness rule. Create a stale-evidence candidate. Keep the evidence grade unchanged until review.

## Orphan node

A high-value case node has no process or evidence relationship even though the canonical record contains both IDs. Classify this as a structural defect and repair the generated relationship.

## Weak domain coverage

Source-to-Pay has many cases but almost no negative evidence or control-linked cases. Rank a research gap for counter-evidence and control coverage instead of asking for more generic cases.

## Healthy graph

A process has valid IDs, current evidence, useful positive and negative cases, controls, and decision profiles. Return no maintenance item. Empty output is better than invented work.