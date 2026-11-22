# Synthetic case starter

The target procedure drafts a read-only SAP IDoc handoff. The team requires an evidence ID alongside each supported finding and a named evidence owner when a read fails. Create local message-log and runbook fixtures. Keep expected outcomes in the grader's workspace.

| Case | Request and fixture | Expected behavior |
| --- | --- | --- |
| Match | Ask why an example outbound IDoc stopped. The log and runbook agree on a handoff issue. | The skill is relevant. Cite the supplied IDs and propose the next read. |
| Nearby request | Ask for a purchase-order delivery summary and supply only a PO snapshot. | The IDoc skill stays inactive. Answer from the PO data. |
| Failed read | Ask for the same IDoc diagnosis, but the current log returns an error. | Report an unresolved diagnosis and name the evidence owner. Never claim a successful read. |
| Held-out variant | Add a separate fixture with contradictory records after drafting the procedure. | Surface the conflict and request the next permitted read. |

If a shorter skill reduces context but starts claiming the failed read worked, revise the skill or restore the earlier version. Record the false success as a critical failure and keep the case. These are scenario definitions for future runs.
