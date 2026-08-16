# Examples

All examples are synthetic.

## Example 1: delivery block rule
Business statement: orders above a defined credit risk threshold must not be delivered without approval.

Discovery shows three enforcement points: order save validation, delivery creation check, and a custom integration that creates deliveries directly. The integration does not apply the same rule.

Result: one business rule, three implementation points, one conflict. Business owner decides expected behaviour; integration owner implements the missing control; regression testing covers all three paths.

## Example 2: supplier selection
A purchasing team says “preferred suppliers must always be selected first.” Configuration, a spreadsheet used by buyers, and an external sourcing tool all contain different preferred-supplier lists.

Result: authoritative source unresolved. Do not choose one technically convenient list. Assign a business/data ownership decision first, then align implementations.

## Example 3: temporary tax exception
A country-specific exception was added during a regulatory transition and never removed.

The exception has no expiry and new products continue to inherit it. The analysis records the original approval, current scope, affected enforcement points, and review owner. The exception becomes a governed rule change instead of permanent folklore.
