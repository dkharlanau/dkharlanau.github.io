# Service Dependency Mapping Method

## Business-first boundary

Choose one business capability or journey. Examples:

- submit an order
- approve a purchase
- receive a shipment update
- create a customer
- complete a payment

Do not start from the full landscape. The map should show what this outcome depends on.

## Dependency types

Use explicit types:

- hard runtime — the flow stops when unavailable
- soft/degraded — the flow can continue with reduced function
- asynchronous — the immediate step succeeds but later processing depends on it
- data freshness — stale data changes correctness without technical outage
- security — identity or authorization is required
- operational — scheduled job, certificate, secret, or maintenance process
- human — manual approval or operational action is required

## Failure effects

Record what the business sees:

- blocked
- delayed
- stale
- partial
- duplicated
- degraded
- silent/invisible failure

## Ownership

For important boundaries distinguish:

- provider owner
- consumer owner
- platform owner if relevant
- escalation decision owner

A generic team label is less useful than an accountable area and a precise responsibility.

## Validation

Use a known-good runtime trace to confirm the map. The trace may reveal hidden queues, caches, lookup services, identity boundaries, or data-refresh jobs missing from design documentation.

## Operational use

The dependency map should improve:

- incident routing
- observability
- change impact analysis
- release readiness
- architecture reviews
- continuity and resilience planning
