# Portfolio trust boundaries

The portfolio connects small products through files, logical references, deterministic projections and evidence. Those connections must not silently become trust escalation paths.

This document defines a bounded security posture for cross-repository artifacts. It does not introduce a shared authentication service, policy engine, secret store or signing infrastructure.

## Core rule

> A cross-repository artifact is input, not authority.

A consumer may parse an artifact only through a contract it explicitly supports. The fact that an artifact comes from another portfolio repository, contains an `eac://` reference, or has a matching SHA-256 does not grant permission to execute code, approve a business action, expose sensitive data or treat the artifact as positive assurance.

## Separate states

Keep these questions separate:

1. **Identity** — what logical artifact is referenced?
2. **Structural validity** — does the document satisfy the consumer's supported schema/contract?
3. **Content integrity** — does the observed content match the expected hash/version?
4. **Provenance** — where did this observed artifact come from, and when?
5. **Authorization** — is this actor/process allowed to perform the requested action?
6. **Assurance** — does the observed evidence actually satisfy the owning product's gate/control?

Passing one state does not imply the others. A valid `eac://` identity is not evidence. A matching hash is not approval. A signed or versioned artifact, if signing is introduced later, would still not prove the business result is correct.

## Cross-repository input rule

Consumers treat upstream files and projections as untrusted structured input until validated.

A consumer must:

- validate only documented schemas/contracts it claims to support;
- reject or explicitly preserve unsupported semantics instead of guessing;
- fail closed when a required binding is missing, ambiguous or integrity-pinned content has changed;
- keep the producer's semantic ownership intact;
- retain provenance/version/hash when the consumer contract supports it.

A consumer must not execute arbitrary scripts, expressions, commands or plugin code merely because they are embedded in or referenced by an upstream portable artifact.

Example: Reconciliation as Code may resolve a Mapping as Code `lookup` value map because that bounded data contract is supported. It must not execute arbitrary transformation code from a referenced mapping artifact.

## Data boundary

Enterprise source data, extracts, operational evidence and credentials are local/private by default.

Portfolio rules:

- public examples and documentation use synthetic, anonymized or deliberately non-sensitive fixtures;
- portable evidence should contain the minimum data needed for review/audit;
- products that support masking, hashing or omission should prefer those controls for sensitive values;
- a projection intended for a public site must not copy raw enterprise evidence merely because the source artifact is technically readable;
- detached snapshots keep their own lifecycle and distribution decision; provenance does not make a sensitive snapshot safe to publish.

The portfolio website and public GitHub repositories are not an enterprise evidence store.

## Secrets and credentials

Secrets are runtime configuration, not portable artifact content.

Credentials, tokens, database URLs, passwords and private keys must not be written into shared YAML/JSON evidence just to make an integration self-contained. Products may retain non-secret connection references, query hashes, endpoint identities or similar metadata when useful for provenance.

If a connector requires credentials, the execution environment supplies them through the product's supported runtime mechanism.

## Hashes and versions

SHA-256 and version pins establish content identity and change detection. They are useful for reproducibility and stale-input detection.

They do not establish:

- who is authorized to approve the artifact;
- whether the producer itself is trustworthy;
- whether the business outcome is correct;
- whether sensitive data may be distributed;
- whether an action should execute.

Consumers therefore record hash/provenance separately from approval and assurance status.

## Agent and execution surfaces

Products that expose agent-callable or operational capabilities keep their own execution policy, but cross-portfolio integrations share two defaults:

- inspection, validation and dry-run are preferred before consequential execution;
- an upstream artifact cannot widen a consumer's execution authority.

For example, an Interface/Mapping/Process artifact may inform an agent's plan, but it cannot grant SAP write authority. SAP Agentic Operations remains the owner of its bounded capability/policy contract.

## Evidence boundary

Evidence is producer/consumer specific. A consumer may bind an upstream evidence document and decide whether it satisfies its own gate, but must not rewrite the upstream result.

The implemented assurance path illustrates the boundary:

```text
Mapping artifact
  -> validated bounded lookup input
Reconciliation run
  -> evidence + document/configuration hashes
Cutover registry
  -> explicit binding + checkpoint decision
Project Evidence Graph
  -> assurance relationship/projection
```

Each stage owns a different decision. No stage gets positive assurance merely from the presence of an upstream reference.

## Failure behavior

Required cross-product inputs fail explicitly when:

- the referenced file is missing;
- the supported schema/shape is invalid;
- a required logical reference cannot be resolved;
- an expected hash/version does not match;
- multiple bindings make the result ambiguous;
- required evidence is present but does not satisfy the consumer's gate.

A product may continue with partial analysis only when its contract explicitly distinguishes partial/unknown from passed/verified.

## Public versus local boundary

Public portfolio artifacts should be safe to clone, inspect and run against synthetic examples without access to private systems.

Local enterprise execution may add private datasets, credentials, internal endpoint bindings and evidence. Those local additions are not automatically eligible for commit, public documentation, GitHub Pages or cross-repository fixture use.

## Non-goals

This contract deliberately does not define:

- a universal identity provider or RBAC model;
- a shared secrets service;
- a portfolio-wide PKI/signature scheme;
- one central policy decision point;
- a global network resolver for `eac://`;
- automatic trust between repositories owned by the same GitHub account.

Those would introduce new infrastructure and trust boundaries. Add them only if a concrete use case cannot be handled by a bounded producer/consumer contract.

## Machine-readable contract

The same baseline rules are mirrored in [`products/trust-boundaries.json`](trust-boundaries.json). Individual products remain responsible for stronger domain-specific controls.