# Authorization & Identity Diagnosis Method

## Layer model

Trace access in this order:

1. Authentication
2. Effective identity
3. Identity propagation
4. Coarse application or service access
5. Resource scope
6. Action permission
7. Business authorization rule
8. Session, token, or cache state

Do not skip directly to roles. A role may be correct while the effective identity, claim, object scope, or business state is wrong.

## Comparison strategy

Compare a failing identity with a known-good identity across:

- authentication path
- effective subject
- groups
- roles
- scopes
- tenant or client
- organizational scope
- resource ownership
- business object state
- token/session issue time

Job title and department name are weak evidence because effective access may differ.

## Least-change rule

The correction should address the proven gap only. Avoid wildcard permissions, administrator roles, broad group membership, or disabling policy checks as diagnostic shortcuts.

## Security boundary

If a correction changes privileged access, segregation of duties, sensitive data access, approval authority, or regulated controls, stop and route the change through the responsible security or business owner.

## Evidence discipline

Do not publish tokens, passwords, private keys, cookies, personal data, internal tenant identifiers, or confidential policy details. Use sanitized claims and synthetic identifiers in public examples.
