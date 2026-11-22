# Paired skill evaluations

Start with the smallest procedure that repeats often enough to measure. Write what a completed job looks like and which rule is critical before choosing a grader.

- **Skill effect.** Keep the model, runtime, permissions, tools, settings, and case fixtures fixed. Compare no skill against the current skill under normal discovery. Observe discovery separately when the runtime records it.
- **Revision effect.** Compare original and revised skill versions on the same setup. Hold back cases that were not used to make the edits. A separately forced load can diagnose the body when discovery is uncertain. Keep those results outside the natural-discovery comparison.
- **Upgrade effect.** Repeat the paired test on the new model or runtime. Compare results within each environment first. When testing a general-knowledge instruction by itself, return to full tasks before removing it. A recall check can miss a team-specific action or field that is required under pressure.

Use exact fields or trusted tool receipts for observable facts. Ask a reviewer to resolve subjective judgments and disagreements. Report raw counts, the number of trials, and per-case failures. Use cost per accepted result only when the runtime reports enough data to calculate it. Decide how much variation is acceptable before relying on a small sample.

Source reading: [Philipp Schmid on testing agent skills](https://ai.engineer/talks/0vphxNt4wyk-dont-ship-skills-without-evals) and [Nikolay Petrov on testing instruction precision](https://ai.engineer/talks/yzx4IuEh_tU-your-skill-md-is-70-stuff-model).
