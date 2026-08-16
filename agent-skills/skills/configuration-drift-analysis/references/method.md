# Configuration Drift Analysis Method

## Effective-state principle

Compare what the system is actually using, not only what source control, configuration files, or release notes say should be active.

Effective state can include:

- deployed version
- active feature flag
- runtime setting
- environment variable
- route or endpoint
- tenant override
- cache or loaded configuration snapshot
- active policy
- dependency version

## Comparison layers

Use separate layers:

1. Application and runtime version
2. Feature and configuration state
3. Identity and secret references
4. External dependencies
5. Network and routing
6. Business data conditions
7. Scheduling and time conditions
8. Deployment and override history

## Causal relevance

Rank a difference higher when:

- it affects the failing path directly
- it changed near the first failure
- it differs in the known-good environment
- the product behavior explains the symptom
- a safe test can reproduce or remove the symptom

A long diff is not an analysis. Reduce it to differences that can plausibly explain the scenario.

## Governed correction

If configuration has a source of truth, correct it there and redeploy or synchronize through the normal path. Direct runtime editing may repair one instance while preserving the mechanism that caused drift.

## Sensitive state

For credentials and security policy, compare non-secret metadata such as reference name, version, expiry, target, policy identifier, or ownership. Never copy secret values into diagnostic records.
