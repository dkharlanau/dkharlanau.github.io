# Portfolio interoperability contract

The portfolio connects bounded products without introducing one universal writable schema. Cross-repository links therefore use small explicit contracts: stable logical references, producer-owned semantics, deterministic adapters, and evidence provenance.

**Status:** implemented bounded convention, currently exercised by the live Mapping → Reconciliation → Cutover → Project Evidence assurance path. It is not a proposal for a universal enterprise artifact service.

## `eac://` is a logical artifact reference

Implemented portfolio integrations use references shaped as:

```text
eac://<owner>/<repository>/<kind>/<local-id>[?version=<version>]
```

`<local-id>` may contain multiple path segments when a producer needs a structured identity.

Examples already used by the portfolio:

```text
eac://dkharlanau/cutover-graph/task/reconcile-customers
eac://dkharlanau/cutover-graph/checkpoint/reconcile-customers
eac://dkharlanau/reconciliation-as-code/reconciliation/customer-country/run/run-123
```

The reference answers **what artifact is being referred to**. It is not an HTTP URL, download location, credential, or proof that the referenced artifact exists.

Consumers must not turn `eac://...` into a network fetch by convention. Resolution happens through an explicit adapter, registry, evidence pack, or other bounded integration that already knows how to bind that logical identity to an observed artifact.

## Namespace ownership

The URI authority and first path segments preserve producer ownership:

- `owner` identifies the namespace owner;
- `repository` identifies the product that owns the referenced artifact kind;
- `kind` is producer-defined, for example `task`, `checkpoint`, or `reconciliation`;
- `local-id` is producer-defined stable identity inside that kind;
- optional `version` qualifies identity when a producer contract requires it.

The producer owns the meaning and lifecycle of its `kind/local-id`. A consumer may validate and relate the reference, but must not reinterpret the producer's domain semantics.

This keeps the portfolio directional: Cutover owns cutover task/checkpoint identity; Reconciliation owns reconciliation run identity; Project Evidence may connect those references but does not become their semantic owner.

## Canonical form

The currently implemented canonicalizer accepts:

- scheme exactly `eac`;
- non-empty token-safe `owner`, `repository`, and `kind`;
- one or more non-empty local-id path segments;
- percent encoding for characters outside the safe segment set;
- at most one optional `version` query parameter;
- no other query parameters.

Canonicalization is syntax/identity normalization only. It does **not** verify that the artifact exists or is trustworthy.

## Presence is not evidence

This is a mandatory portfolio rule:

> A syntactically valid `eac://` reference is never, by itself, positive assurance.

For evidence-backed relationships, a consumer needs an explicit binding that can retain observation/provenance such as:

- evidence status;
- document SHA-256;
- producer configuration/specification SHA-256;
- observed timestamp;
- producer artifact kind/version;
- source file or registry binding where appropriate.

The live reference chain enforces this today:

```text
Mapping as Code artifact
  -> Reconciliation as Code run
  -> RAC evidence document + configuration hash
  -> Cutover evidence registry
  -> verified checkpoint
  -> verified Cutover artifact index
  -> Project Evidence Graph evidence node
```

The same Cutover checkpoint exported without its evidence registry remains unverified and cannot become positive evidence merely because the `eac://` RAC reference is present.

## Reference versus projection

Use a logical reference when the downstream product only needs identity or a relationship to producer-owned truth.

Use a deterministic projection when the downstream product needs a derived representation of upstream content.

Examples:

- Cutover checkpoint → RAC run: logical reference plus evidence registry binding.
- Cutover artifact index → Project Evidence Graph: deterministic adapter/projection that preserves producer refs.
- Mapping as Code → RAC lookup: product-native `map_ref` plus Mapping artifact SHA, because RAC needs the mapping rule at execution time.
- Mapping/Interface → Transformation Graph: deterministic derived graph projection with source provenance.

Do not replace a reference with a copied business rule just because copying is easier for one consumer.

## No universal dereference service

The portfolio does not currently define a global `eac://` network resolver or central artifact registry. That is intentional.

A universal service would create a new coupling and trust boundary before there is evidence that the portfolio needs one. Current integrations resolve references through bounded producer/consumer contracts.

If a future shared resolver is proposed, it must first answer:

1. what problem cannot be solved by producer-specific adapters/registries;
2. how authorization and sensitive enterprise evidence remain bounded;
3. how versioning and stale references are handled;
4. how a resolver distinguishes identity lookup from trust/assurance;
5. how failure remains explicit instead of silently materializing placeholder truth.

## Compatibility rule

A producer may add new artifact kinds without forcing every other repository to understand them.

A consumer should:

- validate only the kinds/contracts it claims to support;
- preserve unknown external refs when safe rather than invent semantics;
- fail explicitly when a required reference cannot be resolved;
- keep structural validity separate from assurance completeness where those are different questions.

This is why Project Evidence Graph can remain structurally valid while separately reporting that an externally backed checkpoint is unverified.

## Trust boundary

Interoperability does not create transitive trust. Cross-repository artifacts remain untrusted structured input until the consumer validates the bounded contract it supports. A matching hash proves content identity, not authorization, business approval or positive assurance; referenced scripts/code do not execute by convention; enterprise data and credentials remain local/private by default.

The portfolio baseline for validation, data handling, secrets, agent authority and fail-closed behavior is defined in [Portfolio trust boundaries](TRUST_BOUNDARIES.md) and mirrored in `products/trust-boundaries.json`.

## Machine-readable contract

The bounded rules and examples above are mirrored in [`products/interoperability.json`](interoperability.json). It describes the portfolio convention; producer repositories remain authoritative for their artifact kinds and domain semantics.
