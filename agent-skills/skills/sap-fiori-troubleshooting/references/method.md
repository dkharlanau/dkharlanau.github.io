# Method

## Diagnostic principle

Follow the request from the visible symptom to the first failing layer. Do not jump directly from a Fiori screen to ABAP debugging.

Use this layer order:

1. Launchpad content and navigation.
2. Browser and UI resources.
3. HTTP service request.
4. Gateway or service routing.
5. Backend application logic, data, and configuration.
6. Authorization and identity.
7. Platform and connectivity.
8. Cache or performance branch when the evidence fits.

## Evidence sequence

Capture the user, system/client, timestamp, exact action, observed result, expected result, and a known-good comparison when possible.

In browser developer tools, record relevant Console messages and the Network request that first fails or becomes slow. Preserve the request method, path, HTTP status, response, and request/correlation ID when available. Remove credentials, tokens, cookies, personal data, and sensitive business payload values before sharing.

For ABAP Gateway OData flows, correlate the browser timestamp with `/IWFND/ERROR_LOG`. If backend processing raised the error, use backend error information and `/IWBEP/ERROR_LOG` where applicable.

## Symptom routing

### Missing app or tile

Stay in launchpad content, role assignment, target mapping, and intent resolution. Compare with a working user before checking application code.

### App cannot open

Use Console and Network first. Separate failed intent resolution, missing resources, service failures, and authorization failures.

### App opens but has no data

Find the data request. If the request fails technically, follow service/Gateway evidence. If it succeeds and returns a business error or empty result, move to backend business logic, authorization, filters, or master/configuration data.

### Wrong business result

If the HTTP flow is successful, Fiori may only be the presentation layer. Switch to the relevant functional diagnostic Skill and trace the business object.

### Slow app

Name the slow resource or request. Static-resource delay, service delay, and backend processing delay require different owners.

### Stale app

Capture the stale/missing resource and current version first. Use browser or launchpad cache invalidation only after the cache hypothesis has evidence.

## Owner routing

- Launchpad content or target mapping: Fiori content/security administration.
- UI resource or JavaScript defect: UI5/frontend development.
- Gateway/service routing: Gateway or backend development depending on the failing side.
- Business validation or document behavior: functional process owner.
- Authorization: security team with exact failed-check evidence.
- Platform/connectivity: Basis or platform team.

Every handoff must contain a specific question and evidence. “Please check Fiori” is not an actionable handoff.

## Validation

Repeat the original business action using the same scope. Confirm the previously failing request or resource, the user-visible result, and the business result. Record regression checks relevant to the changed layer.
