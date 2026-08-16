# Authorization & Identity Diagnosis Examples

All examples are synthetic.

## Example 1 — User signs in but cannot approve

Observed: user opens the application and reads the document but the approve action fails.

Evidence path:
1. Authentication succeeds.
2. Effective identity is correct.
3. User has read access to the document.
4. Approval action requires a separate permission not present in the effective role.

Diagnosis: action-level authorization gap.

Closure: add the approved narrow permission through the normal access process and test both approval and unrelated privileged actions.

## Example 2 — API returns 401 after credential rotation

Observed: service call started returning 401 after a credential change.

Evidence path:
1. Request route and schema match the known-good call.
2. Target system rejects the presented identity.
3. The caller is still using the previous credential reference.

Diagnosis: authentication failure, not API business authorization.

## Example 3 — Same role, different data visibility

Observed: two users have the same visible role but one cannot see a regional record.

Evidence path:
1. Both authenticate and open the application.
2. Role names match.
3. Effective organizational scope differs by group claim.
4. The failing record belongs to a region outside the user's scope.

Diagnosis: resource-scope authorization, not missing application access.

## Example 4 — Access works after new session

Observed: approved role assignment appears ineffective until the user signs in again.

Evidence path:
1. Policy assignment is correct.
2. Existing session contains old claims.
3. New session receives the updated claim set.

Diagnosis: session or token propagation timing.

Closure: document expected propagation behavior rather than repeatedly changing roles.
