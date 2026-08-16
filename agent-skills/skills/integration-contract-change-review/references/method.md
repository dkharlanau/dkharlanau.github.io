# Method

Review an integration contract across several surfaces, not only payload shape.

## Contract surfaces
- schema and field structure;
- business meaning and allowed values;
- identity and authorization;
- endpoint and routing;
- ordering and timing;
- error model;
- retry and idempotency;
- service expectations;
- ownership and version lifecycle.

## Compatibility classes
- additive: new optional behaviour that existing parties can ignore safely;
- compatible with conditions: works only when consumers or producers meet known assumptions;
- breaking: existing party cannot continue without change;
- semantic breaking: syntax remains valid but business meaning changes.

## Transition strategies
Choose based on producer/consumer independence and rollout constraints: tolerant reader, dual-read, dual-write, new version, compatibility mapping, feature flag, staged rollout, or coordinated cutover.

## Validation
Use representative payloads and business scenarios. Include unknown fields, new values, missing mandatory data, retry, duplicate, ordering, and error cases where relevant. Confirm downstream business state, not only HTTP or schema success.

## Retirement
Old versions, fields, mappings, and bridges create long-term complexity. Retire them only when usage evidence, owner agreement, and rollback expectations support removal.
