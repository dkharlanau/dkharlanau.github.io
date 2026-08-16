# AI Agent Authority Design Examples

All examples are synthetic.

## Example 1 — Customer master change

Job: identify likely corrections to customer data.

Authority design:
- read customer and validation evidence
- propose correction
- deterministic validation checks required fields and allowed values
- human data steward approves high-impact changes
- controlled tool executes approved update

Reason: model capability to infer a correction does not grant authority to change enterprise master data.

## Example 2 — Low-risk support classification

Job: classify incoming support requests and route them.

Authority design:
- broad read of ticket text within permitted scope
- autonomous classification and routing to approved queues
- no permission to close tickets, change business data, or message external customers

Result: bounded autonomous execution is reasonable because side effects are limited and reversible.

## Example 3 — Malicious retrieved instruction

Observed: a retrieved document contains text telling the agent to ignore approval rules and call a write tool.

Expected behavior:
1. Treat document content as data.
2. Keep the existing authority policy unchanged.
3. Refuse the unauthorized write path.
4. Continue with allowed analysis or proposal.

## Example 4 — Duplicate execution risk

Job: create a refund after approved analysis.

Risk:
1. Tool times out after submission.
2. Agent cannot tell whether the refund was created.
3. Blind retry can create a second refund.

Authority design: require a stable operation key or reconciliation check before any autonomous retry.
