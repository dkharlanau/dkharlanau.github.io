# Method

Separate the stable procedure from one execution record. The procedure defines the reusable method. The run record stores case values, evidence, decisions, and results.

Each important step should have a small contract: Action, Input, Expected Result, Evidence, Decision Point, Risk, and one of Continue / Retry / Stop / Rollback / Escalate. Put stop conditions before dangerous actions, not in a final warning section.

Use linked Skills for complex judgment. A runbook should not grow into a troubleshooting encyclopedia. If a step requires diagnosis, call the relevant troubleshooting Skill and return the result to the procedure.

Dry-run with a person who did not write the procedure. Every place where they need undocumented context is a defect in the runbook.