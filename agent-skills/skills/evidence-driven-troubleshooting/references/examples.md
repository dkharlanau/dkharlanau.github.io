# Examples

## SaaS application

A user can open a case but cannot save it. Another user can save the same case type. Compare identity, role, feature flags, request payload, and server response. If the first divergence is an authorization response, route to identity or authorization analysis instead of changing application data.

## API flow

The source sends a request and receives HTTP 500. Preserve the request ID, payload, response, timestamp, and target logs. Compare with a successful request. If the target accepts the same contract for a known-good payload, inspect the earliest field or business state that differs.

## File processing

A scheduled CSV import rejects only one supplier file. Compare schema, delimiter, encoding, column count, header, key values, and file size with a successful file. Do not rewrite the import job until the first structural difference is understood.
