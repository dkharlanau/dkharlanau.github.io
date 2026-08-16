---
name: authorization-identity-diagnosis
description: Use when a user or technical identity can sign in but cannot access a function, API, record, or action, or when access differs by user, environment, claim, role, scope, or object context. Separates authentication, effective identity, propagation, coarse access, resource scope, and action authorization. Produces an Authorization & Identity Diagnosis Record. Do not use to design an enterprise IAM architecture from scratch.
---

# Authorization & Identity Diagnosis

## Purpose

Find the first point where identity or authorization behavior differs from the expected access model, and correct the smallest proven gap without broadening access unnecessarily.

## Use when

- A user signs in but cannot open or execute a function.
- An API or application returns 401 or 403.
- Similar users receive different access results.
- Access changed after role, group, policy, identity-provider, token, or deployment changes.

## Do not use when

- Authentication and authorization work and the problem is application logic.
- You are designing the complete IAM architecture or role model from scratch.
- The issue is only an API schema or routing problem. Use `api-contract-troubleshooting`.

## Required inputs

- Identity, environment, resource, action, timestamp, and exact symptom.
- Expected role, group, scope, claim, ownership, or business authorization rule.
- Relevant sign-in, gateway, application, or authorization evidence.
- Known-good identity or scenario when available.
- Recent access-model changes.

## Workflow

1. Define the exact requested resource and action.
2. Confirm whether authentication succeeded and identify the authentication mechanism.
3. Determine the effective identity at the failing system boundary.
4. Trace important claims, groups, scopes, tenant, client, delegation, or mapped user values across boundaries.
5. Check coarse access to the application, API, service, page, or function.
6. Check resource-level restrictions such as organization, company, region, ownership, document state, field, or row-level policy.
7. Check action-level permissions such as read, create, change, approve, delete, export, or execute.
8. Compare a known-good case using effective access data, not job titles.
9. Check relevant recent changes and propagation or cache timing.
10. Correct the smallest proven access gap and obtain required approval.
11. Repeat the original action and test for unintended access expansion.

## Decision rules

- If authentication fails, stop business-authorization analysis until identity is established.
- If the effective identity is wrong, fix identity propagation or mapping before adding roles.
- If two users have the same visible role but different results, compare claims, groups, organization scope, object context, and effective policy.
- Never assign broad administrator access only to prove that authorization is the problem.
- If the correction affects segregation of duties, sensitive data, privileged actions, or regulatory controls, escalate to the accountable security or process owner.
- If access works only after token or session renewal, investigate propagation or cache timing before redesigning roles.

## Output format

Produce an **Authorization & Identity Diagnosis Record**:

```markdown
## Requested access
Identity:
Environment:
Resource:
Action:
Timestamp:

## Expected access model
Role / group / scope / claim / business rule:

## Authentication
Mechanism:
Result:
Evidence:

## Effective identity
At entry point:
At target boundary:
Relevant claims / groups / scopes:

## Authorization checks
| Layer | Expected | Actual | Evidence |
|---|---|---|---|

## Known-good comparison

## First failing access rule

## Correction

## Approval / SoD considerations

## Validation
Original action:
Unintended extra access check:

## Open questions
```

## Quality gates

- [ ] Resource and action are exact.
- [ ] Authentication and authorization are separated.
- [ ] Effective identity at the failing boundary is known or marked unknown.
- [ ] Comparison uses effective access evidence, not job title.
- [ ] Correction follows least privilege.
- [ ] Sensitive or segregation-of-duties impact is assessed.
- [ ] Validation checks both restored access and unintended expansion.

## References

- `references/method.md` — Identity and authorization layer model.
- `references/templates.md` — Diagnosis record and security handover template.
- `references/examples.md` — Synthetic user, service-account, claim, and object-scope cases.
