# Portfolio external validation protocol

The portfolio uses `validated` as an evidence claim, not a synonym for "implemented", "tested", "published" or "looks useful".

A product may be technically strong before it is externally validated. Keeping those states separate makes the portfolio more credible and tells us what evidence to collect next.

## What validation means

External validation means an independent person uses the product for a concrete task that matches the intended job, using representative input they did not simply copy from the author's scripted demo, and the result is retained as reviewable evidence. Validation is scoped; it does not prove universal correctness, enterprise production suitability or market demand.

## Participant independence

A qualifying participant did not implement the tested feature or author the exact validation fixture, can judge whether the product helps with the intended task, and may receive setup help only when that assistance is recorded.

## Concrete task and input

The record states a real task in outcome language, such as reconciling a representative migration extract, governing a mapping change, modelling a real process, resolving an interface for a reviewed site, or using a knowledge workflow on a source chosen by the reviewer.

Prefer real privacy-safe input or independently prepared representative data. Sensitive enterprise input stays local; retain only safe metadata, hashes, redacted excerpts or aggregate characteristics needed to explain the test. Reproducing only an exact bundled author fixture is not independent validation.

## Required validation record

Each attempt records at least:

- product and version/commit;
- date and validation type;
- privacy-safe participant independence description;
- task and success criteria;
- input provenance/class;
- setup/assistance provided;
- outcome: success / partial / failed / blocked;
- friction and time-consuming steps;
- defects or incorrect/ambiguous output;
- workarounds;
- participant feedback or decision;
- retained evidence/artifact references where safe;
- limitations and what the attempt does **not** prove.

Negative attempts stay in the record set. A failed run is useful product evidence and must not disappear from the denominator.

## Validation types

- **Usability** — can an unfamiliar intended user complete the task with reasonable assistance?
- **Correctness** — can the independent reviewer verify the result against known or independently derived expectations?
- **Interoperability** — does it work in the target environment/toolchain or with an independently operated upstream/downstream system?
- **Production-suitability evaluation** — stronger evidence covering security, operations, representative performance, recovery and governance. A normal validated task does not imply this stronger claim.

## What does not qualify alone

Author-run demos, CI/regression tests, author-written synthetic fixtures, self/agent review, stars/clones/downloads/page views, a successful release pipeline, a documentation site, positive opinion without a task attempt, or exact bundled-example reproduction do not establish external validation by themselves.

## Promotion rule

A product may move to portfolio status `validated` only when:

1. at least one qualifying external validation record exists;
2. the task is relevant and input representative/non-scripted;
3. negative findings are retained honestly;
4. the status statement names the scope rather than implying universal validation;
5. limitations remain explicit.

A product backlog may impose a stricter threshold such as three practitioners or multiple environments; the stricter rule wins.

Example truthful status:

> Validated for three practitioner-run representative SAP migration reconciliation tasks; production deployment and enterprise security review remain unvalidated.

## Evidence count and revalidation

Report all qualifying outcomes, for example `3 attempts: 2 success, 1 partial`. Material contract, UX or architecture changes may make older evidence less representative; keep the history but scope current validation to the tested version.

## Machine-readable contract

The baseline protocol is mirrored in [`products/validation.json`](validation.json). Individual products may define stricter validation gates.
