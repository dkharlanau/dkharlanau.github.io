# Service Dependency Mapping Examples

All examples are synthetic.

## Example 1 — Hidden identity dependency

Capability: create an order from a web application.

Initial map includes frontend, API, order service, and database.

Runtime trace shows every API call also depends on an identity provider and token-validation service.

Result: identity becomes a critical shared dependency with high blast radius and its own health evidence.

## Example 2 — Technically healthy but stale

Capability: show product availability.

Dependency: reference data cache is available and returns HTTP 200.

Failure effect: cache refresh job has not run, so business data is stale.

Result: classify as data-freshness dependency. Availability of the service alone is not a sufficient health signal.

## Example 3 — Asynchronous dependency

Capability: submit a customer request.

The initial API returns success, but final processing depends on a queue and background worker.

Result: queue and worker are asynchronous dependencies. Failure causes delayed rather than immediate blocked behavior.

## Example 4 — Ownership gap

Capability: transmit shipping status to a partner.

The internal integration owner is known, but nobody owns the partner-facing contract and escalation path.

Result: critical boundary has an operational ownership risk even when the interface is currently healthy.
