# Templates

## SAP MDG Domain Solution Design

### Business outcome
- Scenario:
- Domain:
- Critical consumers:
- Release / deployment scope:

### Identity model
- Business identity:
- Number/key strategy:
- Duplicate policy:
- Existing source identities:

### Grain and technical entity map
| Grain | Delivered/custom entity | Fields / meaning | Owner | Lifecycle | Consumers |
|---|---|---|---|---|---|

### Ownership / decision rights
| Grain / field group | Proposer | Business owner | Approver | Steward | Technical owner |
|---|---|---|---|---|---|

### Change-request type matrix
| CR pattern | Purpose | Allowed scope/entities | Risk | Workflow | Final check | Activation-error path |
|---|---|---|---|---|---|---|

### Rule catalog
| Rule ID | Class | Business statement | Grain | Inputs | Result | Execution point | Owner | Positive test | Negative test |
|---|---|---|---|---|---|---|---|---|---|

### Workflow and activation
- Steps:
- Decision rights:
- Agent determination:
- Rejection/revision path:
- Final check:
- Activation boundary:
- Activation-error path:

### Distribution contract
- Active source:
- Replication model:
- Outbound implementation:
- Filter/population:
- Target:
- Payload/service/message:
- Identity/key mapping:
- Target acceptance evidence:
- Persistence evidence:
- Consumer proof:

### DRF recovery decision
- Failed object/population:
- Current source state:
- Target state:
- Idempotency / duplicate behavior:
- Ordering concern:
- Recovery: safe replay / rebuild current truth / manual resolution / reconcile population
- Reconciliation evidence:

### Matching and survivorship
- Identity evidence:
- Automatic-match threshold/policy:
- Review band:
- Non-match rule:
- Reviewer/authority:
- Table/field survivorship rules:
- Manual override evidence:
- Duplicate strategy:
- Key-mapping impact:

### Migration / initial load / delta
- Source population:
- Mapping:
- Data profiling / quality:
- Load path:
- Selected count:
- Accepted/persisted count:
- Key/slice reconciliation:
- Cut-off / watermark:
- First delta:
- No-gap proof:

### Business proof
| Process | Test object/document | Expected governed behavior | Evidence |
|---|---|---|---|

### Operations
- Monitoring metrics:
- Exception owner:
- Replay owner:
- Review queue owner:
- SLA / aging threshold:
- Hypercare exit criteria:

### Risks / decisions
- Risk:
- Open assumption:
- Falsifying test:
- Recommended next decision:

---

## Change Request Type Record

- CR type / proposed ID:
- Business purpose:
- Data model:
- Allowed entity types:
- Single or multi-object:
- Risk class:
- Initial status:
- Workflow type/template:
- Agent determination:
- Validation points:
- Final check:
- Activation step:
- Activation-error step:
- Replication trigger:
- Audit evidence:
- Business owner:

---

## Rule Record

- Rule ID:
- Business statement:
- Rule class: workflow / validation / derivation / authorization / identity
- Domain and grain:
- CR types:
- Input entities/fields:
- Output/message:
- Execution point:
- Severity:
- Business owner:
- Technical owner:
- Source of authority:
- Positive test:
- Negative test:
- Monitoring signal:
- Change history:

---

## DRF Replay Decision Record

- Object / population:
- Target:
- Failure window:
- Source active version/state:
- Previous correlation/message identity:
- Target persistence known? yes/no/uncertain
- Later successful changes? yes/no
- Idempotent or duplicate-safe? yes/no/unknown
- Ordering requirement:
- Key mapping state:
- Decision: replay / rebuild current truth / manual resolution / stop-and-reconcile
- Population impact:
- Post-recovery reconciliation:
- Business proof:

---

## Match & Survivorship Decision Record

- Match group:
- Candidate identities:
- Strong evidence:
- Supporting/noisy evidence:
- Score / threshold band:
- Reviewer and authority:
- Match decision:
- Survivorship rules by table/field:
- Calculated best record:
- Manual overrides and reasons:
- Duplicate strategy:
- Surviving identity:
- Key mapping / replacement relationship:
- Downstream consumers checked:
- Final reconciliation:
