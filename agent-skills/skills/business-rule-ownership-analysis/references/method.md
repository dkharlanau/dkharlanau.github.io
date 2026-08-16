# Method

Treat the business rule as a governed object with meaning, authority, data, implementation, exceptions, and lifecycle.

## Rule statement
Write the rule in business language first. Example: “Orders above the credit threshold require approval before delivery.” Avoid starting from transaction codes, tables, or implementation classes.

## Ownership layers
- business owner: decides what the rule means;
- data owner: owns data required by the rule;
- application owner: owns one implementation point;
- control owner: checks whether the rule is followed;
- change coordinator: manages cross-system updates.

One person can hold several roles, but do not assume this without evidence.

## Enforcement-point map
A rule can exist in workflow, configuration, custom code, UI validation, master data, integration mapping, API policy, batch logic, reports, or manual procedure. Record each point separately.

## Exception control
For every exception record scope, approver, reason, start date, expiry or review trigger, and how the exception is visible to downstream processes.

## Change analysis
A rule change should trigger impact analysis across data, integrations, applications, controls, tests, procedures, and reporting. A technically correct local change can still create an inconsistent enterprise rule.
