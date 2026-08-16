# API Contract Troubleshooting Examples

All examples are synthetic.

## Example 1 — 400 after client release

Observed: a previously working create request now returns 400.

Evidence path:
1. Same endpoint and identity still work with the old client.
2. New client sends `quantity` as text instead of number.
3. Provider validation rejects the request before business logic.

Diagnosis: first broken contract is request schema.

Closure: correct serialization, repeat original request, confirm the intended business record is created.

## Example 2 — 403 for one service account

Observed: request shape is identical but one technical identity receives 403.

Evidence path:
1. Authentication succeeds.
2. Working account and failing account reach the same route.
3. Failing account lacks the operation scope for the target resource.

Diagnosis: authorization boundary, not API schema.

Next skill: `authorization-identity-diagnosis` if policy analysis is required.

## Example 3 — 500 in provider

Observed: provider returns 500 for one business object.

Evidence path:
1. Contract validation succeeds.
2. Other objects with the same request shape succeed.
3. Provider log shows a downstream reference lookup failure.

Diagnosis: provider accepted the API contract; failure is in downstream business processing.

Closure: correct the dependency or business data and repeat with the same object.

## Example 4 — 202 accepted but nothing happens

Observed: API returns 202, but the expected downstream object never appears.

Evidence path:
1. Provider accepted the request and returned a tracking ID.
2. A queue item was created.
3. The worker retried and moved the item to a dead-letter state.

Diagnosis: API exchange succeeded. The failing boundary is asynchronous processing.

Next skill: `batch-queue-troubleshooting`.
