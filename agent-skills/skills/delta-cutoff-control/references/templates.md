# Templates

## Delta / Cutoff Control Record

```text
Flow:
Population:
Delta key:
Timezone:
Window start:
Window end:
Start inclusive: yes/no
End inclusive: yes/no
Watermark before:
Candidate watermark after:

Late-arrival strategy:
Duplicate key / strategy:
Replay strategy:
Business cutoff:
Source freeze:
Open-transaction handling:

Extracted count:
Applied count:
Rejected count:
Expected count / control total:
Reconciliation result:
Exceptions:

Advance watermark: yes/no
Accepted watermark after:
Evidence:
Owner:
```

## Window history

| Window ID | Start | End | Extracted | Applied | Rejected | Reconciled | Watermark advanced | Owner |
|---|---|---:|---:|---:|---:|---|---|---|

## Replay record

```text
Original window:
Reason for replay:
Target cleanup required:
Idempotency control:
Expected duplicates:
Replay result:
Reconciliation:
Decision:
```
