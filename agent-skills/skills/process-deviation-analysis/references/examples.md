# Examples

## Approval workflow

A purchase request is routed to a different approver than a similar request. Align both paths and compare amount, company code, cost center, requester role, delegation state, and rule version at the first routing decision.

## Pricing or calculation

Two otherwise similar orders produce different prices. Compare the first point where condition or rule selection differs. If the rule executed exactly as configured but the commercial result is wrong, treat the issue as rule design rather than runtime failure.

## Case status

A support case moves directly from New to Closed while the expected path includes Review. Compare automation rules, timestamps, user actions, integration callbacks, and feature flags. Preserve the original audit trail before reopening the case.
