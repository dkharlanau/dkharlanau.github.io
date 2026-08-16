# Release Readiness Examples

All examples are synthetic.

## Example 1 — Integration release with unknown consumer

Observed: provider API change is tested, but one consumer owner has not confirmed compatibility.

Readiness result:
- scope known
- provider tests passed
- critical dependency state unknown
- no controlled fallback for that consumer

Decision: NO-GO until compatibility or an accepted isolation plan exists.

## Example 2 — Data load with no simple rollback

Observed: a large production data load cannot be reversed with one technical rollback.

Readiness result:
- representative rehearsal completed
- reconciliation controls defined
- pre-load backup exists
- forward correction procedure exists
- business owner accepts the recovery model

Decision: GO can be reasonable even without a simple rollback because recovery is explicit and evidence is strong.

## Example 3 — Small UI change with weak risk

Observed: text and layout change, no API or data contract impact.

Readiness result:
- automated checks pass
- target page tested
- deployment is reversible
- monitoring uses normal frontend error signals

Decision: GO. Do not invent an enterprise ceremony for a low-risk reversible change.

## Example 4 — Conditional go

Observed: one non-critical report defect remains with a documented workaround and owner.

Readiness result:
- core business flow tested
- defect does not affect data creation
- workaround is accepted
- fix has an owner and date

Decision: CONDITIONAL GO. Record the condition instead of pretending the release is fully green.
