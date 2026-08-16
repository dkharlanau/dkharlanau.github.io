# Method

Reconciliation starts with business scope, grain, and keys, not with a VLOOKUP or SQL join. Profile each dataset independently before matching. Record structure, row count, nulls, duplicates, date range, and key quality.

Normalize only approved differences such as date format, unit conversion, casing, whitespace, currency, or known mapping rules. Keep the original data unchanged.

Classify exceptions before investigating them. Useful classes include source-only, target-only, duplicate, timing, expected transformation, mapping issue, source defect, target defect, and unknown. Trace representative material examples from source through transformation to target.

A good reconciliation is rerunnable. The same rules should prove the correction without manual reinterpretation.