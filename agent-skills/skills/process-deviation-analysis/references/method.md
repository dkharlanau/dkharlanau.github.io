# Method

Build the expected path and actual path at the same level of detail. Align them step by step and locate the first meaningful divergence. Later differences are usually consequences.

At the divergence, compare all inputs that can influence the decision: business data, reference data, status, time, organization, identity, rule configuration, feature flags, external responses, or manual action. Identify which component or actor selected the next state.

A useful explanation must cover both the failing and known-good case. If the rule executed correctly but the business result is wrong, classify the issue as process or rule design rather than a technical failure.

After correction, test the same decision point and include other objects that share the same rule in regression scope.