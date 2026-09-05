# Portfolio external validation protocol

Public demos, synthetic fixtures and CI prove that a product can be exercised reproducibly. They do not prove that an independent practitioner can use it for the intended job. This protocol defines the minimum evidence required to make external-validation claims across the portfolio.

It is intentionally small. Individual products may use stricter protocols, but they should not use a weaker definition of `validated` than this portfolio baseline.

## What external validation means

A qualifying validation attempt has all of these properties:

1. **Independent participant** — the participant did not implement the tested product change and did not author the tested fixture.
2. **Relevant task** — the task represents a concrete job the product claims to support.
3. **Representative input** — the input is real or independently prepared and representative of the intended use case. Synthetic author-owned regression fixtures do not qualify by themselves.
4. **Pinned product state** — the tested repository commit and, where available, package/product version are recorded.
5. **Observed outcome** — success, partial success, failure or inconclusive outcome is retained together with material friction and workarounds.
6. **Explicit limitations** — the record states what the attempt does not prove.
7. **Privacy-safe retention** — no client-confidential, personal or proprietary source content is committed merely to prove that validation occurred.

A failed qualifying attempt is still validation evidence. It must not disappear from the denominator or be rewritten as a non-attempt after the fact.

## Three validation dimensions

Validation claims must identify the dimension being tested.

### Usability validation

Question: can an independent target user understand, install/run and complete the intended workflow with acceptable friction?

Typical evidence includes setup friction, task completion, points of confusion, documentation gaps and whether the participant can explain the result correctly.

### Correctness validation

Question: does the product produce the expected result on independently prepared representative input, with failures and limitations visible rather than hidden?

This may include comparison against a separately established expected result, practitioner review, or an independent reference method appropriate to the product.

### Production-suitability validation

Question: is the product suitable for a stated production context under that context's operational, security, performance, support and governance constraints?

Usability or correctness evidence does **not** imply production suitability. Production-suitability validation must be claimed separately and within an explicit environment/scope.

## What does not qualify by itself

The following can be useful evidence, but none is sufficient on its own for external-validation status:

- author-run demo;
- CI success;
- synthetic regression fixture authored by the implementation team;
- self-review or agent review;
- generated documentation or Pages deployment;
- GitHub stars, clones or package downloads;
- friendly feedback without an observed relevant task;
- a benchmark whose expected answers were authored by the same implementation loop and never independently reviewed.

These signals may support engineering confidence. They are not substitutes for an independent use attempt.

## Record every qualifying attempt

Use [`validation-record.schema.json`](validation-record.schema.json) for retained records. A sanitized example is provided in [`validation-record.example.json`](validation-record.example.json).

At minimum record:

- product and exact commit/version tested;
- validation dimension;
- date/time;
- participant independence and broad role archetype;
- task and input class;
- environment/setup and whether author assistance was required;
- outcome: `passed`, `partial`, `failed`, or `inconclusive`;
- material friction, failures and workarounds;
- participant feedback as a privacy-safe paraphrase where retained;
- explicit limitations;
- retention location/classification.

Do not commit names, email addresses, employer/client identifiers, raw enterprise exports, recordings, credentials or confidential screenshots just to make the record look more concrete.

## Maturity promotion rule

The portfolio maturity ladder remains:

```text
experimental -> usable -> release-ready -> validated
```

`validated` is always a **scoped evidence statement**, not a universal quality badge.

A product may use the `validated` label only when:

- at least one qualifying external validation record exists for the claimed dimension and task class;
- every known qualifying attempt in the stated cohort is represented, including failed/partial/inconclusive attempts;
- the public status names the validation dimension and sample/scope, for example `validated — usability, 3 external practitioner runs`;
- limitations and assistance level are visible;
- the claim does not generalize from usability/correctness into production suitability without production-suitability evidence.

One successful run is evidence and may justify a narrowly scoped statement such as `externally exercised once`; it must not be presented as broad or universal validation.

The portfolio deliberately sets no universal minimum sample size because products and task classes differ. Each product should increase the sample until the evidence is strong enough for the breadth of the public claim it wants to make.

## Assistance is evidence, not disqualification

Author assistance does not automatically invalidate a run. It changes what the run proves.

Record whether the participant required help with installation, configuration, input preparation, interpretation or recovery. A heavily assisted successful run may provide correctness evidence while revealing that independent usability is not yet demonstrated.

## Negative evidence and fixes

When an external attempt fails:

1. retain the failed/partial record;
2. classify the failure rather than hiding it;
3. create an implementation-sized issue when a product fix is justified;
4. after the fix, perform a new attempt or explicit re-test record;
5. do not mutate the original failure into a pass.

Historical evidence should remain understandable against the product commit that produced it.

## Public versus private retention

A validation record may point to evidence retained privately when the source material cannot be published. Public repositories should store only a sanitized record that proves the existence, scope and outcome of the attempt without leaking the source data.

Acceptable retention classes are defined in the record schema:

- `private_local`;
- `secure_org_system`;
- `public_sanitized`.

The record is evidence about the validation attempt; it is not permission to publish the participant's underlying data.

## Machine-readable policy

The same baseline is mirrored in [`validation-policy.json`](validation-policy.json). The reusable record contract is [`validation-record.schema.json`](validation-record.schema.json).

Product-specific protocols may extend these fields and thresholds while preserving the core rules: independence, relevant task, pinned product state, retained negative outcomes, scoped claims and privacy-safe evidence.