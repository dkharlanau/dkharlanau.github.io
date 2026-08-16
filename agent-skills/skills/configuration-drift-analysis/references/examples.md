# Configuration Drift Analysis Examples

All examples are synthetic.

## Example 1 — Feature flag differs

Observed: a new workflow path works in test but is missing in production.

Comparison:
1. Application version is identical.
2. Relevant feature flag is enabled in test and disabled in production.
3. The flag directly controls the missing path.

Diagnosis: proven effective-configuration difference.

Closure: correct through the governed flag-management process and validate the same scenario.

## Example 2 — Endpoint override

Observed: integration succeeds in test but production receives timeouts.

Comparison:
1. Client version and payload are identical.
2. Production runtime override points to an obsolete dependency endpoint.
3. Source-controlled default points to the current endpoint.

Diagnosis: runtime drift caused by an unmanaged override.

Closure: remove or correct the override at its governed source and add drift detection.

## Example 3 — Difference is not configuration

Observed: one environment rejects a business transaction.

Comparison:
1. Versions, rules, flags, and dependency state match.
2. The failing environment contains different reference data for the business object.

Diagnosis: data condition, not configuration drift.

Next skill: `data-reconciliation` or domain-specific data analysis.

## Example 4 — Version mismatch after partial deployment

Observed: only one node behaves differently.

Comparison:
1. Configuration is identical.
2. One node still runs the previous application package.
3. Requests routed to that node reproduce the old behavior.

Diagnosis: deployment-state drift.

Closure: complete deployment and validate across all nodes.
