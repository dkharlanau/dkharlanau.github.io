# Portfolio external validation protocol

The portfolio uses `validated` as an evidence claim, not a synonym for "implemented", "tested", "published" or "looks useful".

A product may be technically strong before it is externally validated. Keeping those states separate is a feature: it makes the portfolio more credible and tells us what evidence to collect next.

## What validation means

External validation means an independent person uses the product for a concrete task that matches the product's intended job, using representative input they did not simply copy from the product author's scripted demo, and the result is retained as reviewable evidence.

Validation is scoped. It does not prove universal correctness, enterprise production suitability or market demand.

## Minimum participant independence

A qualifying participant:

- did not implement the product or the tested feature;
- did not author the exact validation fixture/input;
- is able to judge whether the product helps with the intended task;
- may receive installation/setup help, but the assistance must be recorded.

A colleague, practitioner, client-side expert, open-source user or independent reviewer can qualify. The participant does not need to be anonymous or unpaid; independence is about the tested work, not the commercial relationship.

## The task must be concrete

The record states the real task in outcome language, for example:

- reconcile a representative source/target migration extract and inspect the evidence;
- govern a source-to-target mapping change and identify a breaking semantic change;
- model a real operating process and detect a trapped path;
- resolve the best machine/agent interface for a reviewed public site;
- use a knowledge capture/review flow on a source the reviewer selected.

"Look at the repository and tell me if it is cool" is feedback, not product validation.

## Input rule

Prefer real privacy-safe input or independently prepared representative data.

If real enterprise data cannot be retained:

- keep the sensitive source local;
- retain only safe metadata, hashes, redacted/synthetic excerpts or aggregate characteristics needed to explain the test;
- state what was withheld;
- do not publish participant/customer identity or proprietary data without permission.

Author-provided examples can support onboarding, but a run that only reproduces the exact bundled fixture is not independent validation.

## Required validation record

Each attempt records at least:

- product and version/commit;
- date;
- validation type;
- participant independence description (privacy-safe);
- task and success criteria;
- input provenance/class (real, independently prepared representative, author fixture);
- setup/assistance provided;
- outcome: success / partial / failed / blocked;
- observed friction and time-consuming steps;
- defects or incorrect/ambiguous output;
- workarounds;
- participant feedback or decision;
- retained evidence/artifact references where safe;
- limitations and what this attempt does **not** prove.

Negative attempts stay in the record set. A failed run is useful product evidence and must not be silently removed from the denominator.

## Validation types

### Usability validation

Question: can an unfamiliar intended user understand and complete the task with reasonable assistance?

Evidence focuses on onboarding, workflow clarity, error recovery and output usefulness.

### Correctness validation

Question: does the product produce a result the independent reviewer can verify against known or independently derived expectations?

Evidence focuses on false positives/negatives, semantic correctness, deterministic behavior and edge cases.

### Interoperability validation

Question: does the product work in the target environment/toolchain or with an independently operated upstream/downstream system?

Evidence focuses on setup, compatibility, version drift, integration failures and retained provenance.

### Production-suitability evaluation

This is stronger than normal `validated` status. It may include security review, operational support, performance under representative load, recovery, governance and real organizational constraints. A product must not imply production suitability merely because one external task succeeded.

## What does not qualify by itself

The following are useful evidence, but not external validation alone:

- author-run demos;
- CI or regression tests;
- synthetic fixtures written by the implementation author;
- self-review or agent review;
- GitHub stars, clones, downloads or page views;
- a successful package/release workflow;
- a documentation/Pages site;
- someone saying they like the idea without attempting a task;
- reproducing only the exact bundled example with no independent judgment.

## Promotion rule

A product may move to portfolio status `validated` only when:

1. at least one qualifying external validation record exists;
2. the attempt used a relevant task and representative/non-scripted input;
3. outcome and negative findings are retained honestly;
4. the status statement names the scope rather than implying universal validation;
5. explicit limitations remain visible.

For products where one result is too weak to be meaningful, the product backlog may define a higher threshold (for example three practitioners or multiple environments). The stricter product-specific rule wins.

Example truthful status:

> Validated for three practitioner-run synthetic/representative SAP migration reconciliation tasks; production deployment and enterprise security review remain unvalidated.

Not acceptable:

> Enterprise validated.

## Evidence count

Report all qualifying attempts in the selected scope:

```text
3 attempts: 2 success, 1 partial
```

Do not report only successful attempts. When an attempt is excluded, record why it did not meet the protocol.

## Revalidation

Material contract, UX or architecture changes may make old validation less representative. Keep historical records, but mark the product's current status scope/version clearly. A validated 0.1 workflow does not automatically validate a rewritten 1.0 interaction model.

## Machine-readable contract

The baseline protocol and reusable record shape are mirrored in [`products/validation.json`](validation.json). Individual products may define stricter validation gates.