# Method

Start with an observable symptom, then map the path from trigger to outcome. Preserve evidence before changes. Compare a failing case with a known-good case when possible. The most useful diagnostic point is usually the earliest meaningful divergence, not the final error message.

Use small hypotheses. Each hypothesis needs a test that can reject it. Change one meaningful variable at a time. Typical layers include business input, identity, client/UI, application, API or integration, queue or scheduler, persistence, configuration, platform, network, and external dependencies.

Close only after end-to-end validation. If the cause is still unclear, hand off the evidence, rejected hypotheses, and missing data instead of restarting analysis from zero.