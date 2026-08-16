---
name: configuration-drift-analysis
description: Use when the same scenario behaves differently between environments, tenants, regions, or nodes and the cause may be version, effective configuration, feature flags, identity references, dependencies, data conditions, or deployment history. Produces a Configuration Drift Analysis Record and tests the most causally relevant differences. Do not use for broad configuration design or blind environment synchronization.
---

# Configuration Drift Analysis

## Purpose

Explain behavior differences between environments by comparing effective state, ranking meaningful differences, and testing the smallest causal hypothesis before synchronization.

## Use when

- The same function works in one environment and fails in another.
- Production behavior differs from test after a release.
- Configuration may have changed through multiple delivery paths.
- A suspected drift needs evidence before correction.

## Do not use when

- You are designing new configuration rather than explaining an existing difference.
- The behavior difference is already proven to come from business data only.
- The proposal is to copy all settings from a working environment without causal analysis.

## Required inputs

- Failing and known-good environments or instances.
- One exact scenario with the same input and expected result.
- Effective configuration, version, feature, deployment, and dependency evidence where available.
- Expected configuration source of truth.

## Workflow

1. Define the exact behavioral difference using the same scenario in both environments.
2. Define comparison scope: components, services, rules, dependencies, and data conditions that can affect it.
3. Capture effective runtime state, not only intended repository or documentation state.
4. Compare application, package, schema, runtime, plugin, model, or deployment versions.
5. Compare settings, flags, routes, endpoints, thresholds, jobs, policies, and environment variables.
6. Compare identity and secret references, expiry metadata, and ownership without exposing secret values.
7. Compare external dependencies: services, data sources, queues, storage, network routes, and reference data.
8. Compare business data conditions that may change behavior independently of configuration.
9. Rank differences by causal relevance to the observed scenario.
10. Test one safe reversible difference or reproduction hypothesis at a time.
11. Correct through the governed source of truth where one exists.
12. Validate behavior and add drift detection or delivery controls when recurrence is plausible.

## Decision rules

- A difference is not a root cause until it explains the observed behavior.
- If runtime state differs from source-controlled state, investigate override or delivery mechanisms before editing runtime values.
- Separate data-condition differences from configuration drift.
- Do not bulk-copy configuration as a diagnostic shortcut.
- For sensitive credentials or security policy, compare references, versions, ownership, and state rather than secret values.

## Output format

Produce a **Configuration Drift Analysis Record**:

```markdown
## Scenario
Failing environment:
Known-good environment:
Input / business case:
Expected behavior:
Observed difference:

## Comparison scope

## Effective-state differences
| Layer | Failing | Known-good | Relevance | Evidence |
|---|---|---|---|---|

## Version differences

## Dependency differences

## Data-condition differences

## Candidate causes
| Candidate | Why relevant | Test | Result |
|---|---|---|---|

## First proven causal difference

## Governed correction source

## Correction

## Validation

## Prevention / drift control
```

## Quality gates

- [ ] The same scenario is compared across environments.
- [ ] Effective runtime state is separated from intended state.
- [ ] Version, config, dependency, identity reference, and data conditions are distinct layers.
- [ ] Differences are ranked by causal relevance.
- [ ] At least one hypothesis is tested rather than assumed.
- [ ] Correction uses the governed source of truth when available.
- [ ] Validation confirms the behavior difference is removed.

## References

- `references/method.md` — Effective-state comparison and causal-ranking model.
- `references/templates.md` — Drift record and controlled-diff table.
- `references/examples.md` — Synthetic feature flag, endpoint, version, and data-condition cases.
