# Examples

All examples are synthetic. Do not replace them with client identifiers or production data.

## Example 1: App is missing for one user

**Symptom:** One user cannot see an app. A colleague with the same business task can.

**Evidence path:**
1. Confirm the same launchpad and system/client.
2. Compare launch content and role assignment.
3. Check semantic object/action and target mapping.
4. Do not start with OData or backend debugging because the app never launches.

**Likely failing layer:** Launchpad content or authorization.

**Good handoff:** “User A does not receive target X. User B in the same process does. The target mapping exists and works for User B. Please verify the business role/catalog assignment for User A.”

## Example 2: App loads, data request returns 500

**Symptom:** The UI shell loads, then a data section fails.

**Evidence path:**
1. Browser Network shows one OData request with HTTP 500.
2. Record timestamp, user, request path, and response.
3. In an ABAP Gateway scenario, correlate the request with `/IWFND/ERROR_LOG`.
4. If backend processing raised the error, continue with backend error/application evidence.
5. If the backend message is a business validation error, route to the functional owner with the document and rule context.

**Likely failing layer:** Gateway/backend application, not UI rendering.

## Example 3: HTTP 403 for one business action

**Symptom:** App loads, but pressing an action returns 403 for one user.

**Evidence path:**
1. Capture the exact request and timestamp.
2. Compare with a working user if allowed.
3. Collect authorization evidence in the affected system, using tools such as `SU53` or an authorization trace where appropriate.
4. Do not add broad roles to test randomly.

**Likely failing layer:** Authorization or service access.

**Bad response:** “Add SAP_ALL and test.”

**Good response:** “The failing action is request X at time Y. Authorization evidence shows missing check Z. Review the intended business role before changing access.”

## Example 4: Old UI after a deployment

**Symptom:** A changed label or UI behavior appears correctly for some users but others still see the old version.

**Evidence path:**
1. Capture the resource loaded by the browser and its version/cache behavior.
2. Compare with a clean or working session.
3. Only after confirming stale resources, use landscape-approved browser or launchpad cache invalidation.
4. Validate that the new resource is loaded and the business function still works.

**Likely failing layer:** Client/launchpad cache or resource versioning.

## Example 5: App is slow

**Symptom:** Users report that “Fiori is slow.”

**Evidence path:**
1. Use Network timing during one controlled reproduction.
2. Identify whether time is spent on static resources, one service request, or many service requests.
3. If one backend request dominates, route with that request, timestamp, and response time.
4. If static resources dominate, investigate UI resource delivery/cache path instead of the business service.

**Good result:** The handoff names a measurable slow component, not a product name.
