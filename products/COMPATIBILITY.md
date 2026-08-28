# Portfolio compatibility policy

Cross-repository interoperability is only useful when producer contracts can evolve without forcing consumers to guess. This policy defines a small compatibility discipline for machine-readable artifacts, adapters and retained evidence.

It is deliberately decentralized: each product owns its schemas and implementation versions. The portfolio only defines how producers and consumers communicate compatibility.

## Version the contract, not only the package

A product implementation version and a portable contract/schema version answer different questions.

- package/application version identifies a software release;
- schema/contract version identifies the shape and semantics of a portable artifact;
- evidence may also identify the engine/runtime version that produced it.

A producer should expose an explicit contract/schema version in public machine-readable artifacts where compatibility matters. Consumers must not infer compatibility from a repository tag or package version alone.

## Consumer support is explicit

A consumer supports the contract versions it has intentionally implemented and tested.

A consumer must not silently interpret an unknown version as "close enough" to the latest known version. For required inputs, unsupported versions fail explicitly. For optional/pass-through relationships, a consumer may preserve an opaque external reference or unknown payload only when doing so cannot invent semantics or positive assurance.

## Compatible changes

An additive change may remain compatible when all of these are true:

- existing required fields keep the same meaning;
- identity/canonicalization semantics do not change;
- defaults and validation behavior for existing fields do not change materially;
- the new field is optional for existing consumers;
- an older consumer can safely ignore or preserve the field without changing the business result or widening authority.

"JSON still parses" is not enough. Compatibility is semantic, not only syntactic.

## Breaking changes

Treat a change as breaking when it does any of the following:

- removes or renames a field/enum value that supported consumers may use;
- changes the meaning, unit, default or validation behavior of an existing field;
- changes logical identity, canonicalization or lifecycle semantics;
- turns an optional semantic into a required one for existing artifacts;
- changes evidence meaning so a previously failed/unknown state could be interpreted as passed/verified;
- widens execution or agent authority from the same artifact;
- changes a producer/consumer ownership boundary;
- reuses an existing version number for different semantics.

Breaking contract changes require a new contract/schema version.

## Unknown fields and unknown semantics

Consumers may ignore unknown optional fields only if their contract explicitly permits safe forward-compatible ignoring.

Consumers must fail when an unknown field/version represents required semantics they need for a correct decision. Adapters must not rename, synthesize or coerce unknown semantics into a supported form merely to keep execution moving.

A compatibility adapter is allowed only when the transformation is explicit, deterministic and tested against both source and target contract versions.

## Deprecation

When practical, a producer should provide an overlap period before removing a public contract version:

1. mark the old version deprecated;
2. document the replacement and migration path;
3. keep fixtures/tests for the deprecated version while supported consumers migrate;
4. remove it only in a clearly breaking producer release or contract-version transition.

Security/correctness defects may require faster removal; in that case the producer should document why compatibility was intentionally broken.

## Evidence and provenance

Retained evidence should include the producer contract/schema version and runtime/engine version where available. This allows a later reviewer to determine which semantics applied when the evidence was generated.

A consumer that imports evidence should preserve upstream version/provenance rather than rewriting it to the consumer's own version.

## Cross-repository adapter tests

Every maintained cross-repository consumer should eventually cover at least:

- one current supported producer contract fixture;
- one unsupported/future contract-version fixture that fails explicitly;
- one integrity/provenance mismatch where the integration uses pins/hashes;
- one additive optional-field case when the contract claims forward-compatible ignoring.

Live cross-repository CI is useful for drift detection, but ordinary unit/contract tests should remain reproducible from committed fixtures so an upstream outage does not make all downstream development unusable.

## Release rule

Before calling a cross-repository integration release-ready:

- the producer contract version is explicit;
- the consumer support range/version list is documented;
- breaking-change behavior is tested;
- migration/deprecation behavior is described;
- release notes identify contract changes separately from unrelated implementation changes.

## Non-goals

This policy does not define:

- one portfolio-wide semantic version number;
- a central schema registry or package manager;
- automatic dependency upgrades across repositories;
- a promise that every product supports every historical contract version;
- compatibility based only on repository ownership or Git tags.

The machine-readable baseline is mirrored in [`products/compatibility.json`](compatibility.json). Product-native schemas and adapters remain authoritative.