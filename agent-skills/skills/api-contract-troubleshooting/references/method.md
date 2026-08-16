# API Contract Troubleshooting Method

## Boundary model

Trace the exchange in this order:

1. Caller construction
2. Authentication and identity
3. Routing and environment
4. Transport and protocol
5. Contract and schema validation
6. Provider business logic
7. Downstream dependencies
8. Consumer interpretation

The goal is to identify the first boundary where expected behavior stops being true.

## Comparison strategy

Prefer a known-good comparison. Change one variable at a time:

- caller
- identity
- environment
- API version
- payload
- business object
- time window

A useful comparison explains why one request succeeds and another fails. A large diff creates more theories than evidence.

## Contract layers

### Technical contract

- method and path
- headers
- content type
- encoding
- status codes
- schema and data types
- version

### Security contract

- authentication mechanism
- effective identity
- scopes or permissions
- tenant or resource boundary

### Business contract

- required business state
- lifecycle rule
- reference data
- ownership
- valid combinations
- expected side effect

### Operational contract

- timeout
- retry
- idempotency
- pagination
- asynchronous acknowledgement
- rate limits

A request can satisfy the technical contract and still fail the business or operational contract.

## Evidence discipline

Capture exact evidence before changing configuration. Remove passwords, tokens, cookies, private keys, personal data, and client-confidential values from public artifacts.

## Escalation

Escalate when diagnosis requires production write access, security-policy changes, uncontrolled replay, unknown duplicate risk, or changes owned by another team. Preserve the evidence pack so the next owner does not restart from a screenshot and folklore.
