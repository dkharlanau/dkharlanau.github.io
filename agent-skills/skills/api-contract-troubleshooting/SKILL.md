---
name: api-contract-troubleshooting
description: Use when an API returns 4xx, 5xx, unexpected data, or no useful result and the failure must be isolated across client construction, identity, routing, schema, business semantics, downstream dependencies, and consumer handling. Produces an API Contract Troubleshooting Record. Do not use for broad architecture design or for message backlog diagnosis after the API exchange already succeeded.
---

# API Contract Troubleshooting

## Purpose

Find the first broken contract in an API exchange and prove whether the failure belongs to the caller, identity layer, route, schema, provider logic, downstream dependency, or consumer handling.

## Use when

- An API returns 4xx or 5xx.
- A response is technically successful but business data is wrong or missing.
- A consumer fails after a contract, version, gateway, or mapping change.
- One caller, environment, identity, or payload works while another fails.

## Do not use when

- The API exchange succeeded and the problem is now in an asynchronous queue or worker. Use `batch-queue-troubleshooting`.
- You are deciding whether to use an API, event, or file integration. Use architecture skills.
- The failure is already clearly an identity or permission problem and no API contract work is needed. Use `authorization-identity-diagnosis`.

## Required inputs

- Caller and provider.
- Environment, endpoint, method, timestamp.
- Sanitized failing request and response.
- Expected contract or schema.
- Correlation or trace ID when available.
- Known-good request or caller when available.

## Workflow

1. Define the expected exchange and business outcome.
2. Capture method, path, status, headers, request body, response body, timestamp, and correlation ID. Remove secrets.
3. Classify the first candidate boundary: client construction, identity, routing, transport, contract validation, provider logic, downstream dependency, or consumer handling.
4. Validate method, path, query values, content type, encoding, required headers, and body structure.
5. Validate identity acceptance and operation authorization.
6. Validate environment, host, API version, gateway route, proxy, and service target.
7. Compare schema rules: required fields, types, enums, cardinality, nullability, and compatibility.
8. Check business semantics and lifecycle rules after structural validation passes.
9. If the provider accepted the request, trace downstream database, queue, workflow, or API dependencies.
10. Verify how the consumer interprets status codes, empty results, pagination, retries, asynchronous responses, and optional fields.
11. Compare against a known-good case by changing one dimension at a time.
12. Apply the smallest proven correction and repeat the original failing call.
13. Validate the business result, not only the HTTP status.

## Decision rules

- Treat 401 as an identity-acceptance signal and 403 as an authorization signal, but verify actual evidence before concluding.
- Do not blame the provider for validation errors before comparing the request to the actual contract.
- A 2xx response is not proof that the intended business state was created or changed.
- If only one API version fails, compare contracts before changing runtime configuration.
- If retry can create duplicate side effects, stop replay until idempotency is known.
- If the provider accepted the request but processing disappears later, switch to `batch-queue-troubleshooting` or end-to-end flow tracing.

## Output format

Produce an **API Contract Troubleshooting Record**:

```markdown
## Exchange
Caller:
Provider:
Environment:
Endpoint / method:
Timestamp:
Correlation ID:

## Expected contract
Schema / version:
Required headers:
Expected business outcome:

## Failure evidence
Request summary:
Response status:
Response summary:

## Boundary classification
client | identity | routing | schema | provider | downstream | consumer | unknown

## Checks
| Check | Evidence | Result |
|---|---|---|

## First broken contract

## Action

## Retry / side-effect risk

## Validation
Technical result:
Business result:

## Open questions
```

## Quality gates

- [ ] Request and response evidence is captured without credentials or secrets.
- [ ] The expected contract is explicit.
- [ ] Identity, routing, schema, provider logic, downstream processing, and consumer handling are separated.
- [ ] The first failing boundary is identified or unknowns are listed.
- [ ] Retry and duplicate side effects are considered before replay.
- [ ] Validation proves the business result.

## References

- `references/method.md` — Layer model and comparison strategy.
- `references/templates.md` — API Contract Troubleshooting Record and handover template.
- `references/examples.md` — Synthetic examples for 400 validation, 403 authorization, 500 provider failure, and successful response with missing business result.
