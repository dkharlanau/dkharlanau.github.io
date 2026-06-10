---
title: "Synthesis: Weak vs Strong Output Patterns"
robots: noindex
sitemap: false
---

# Weak vs. Strong Output Patterns

## Pattern: Data Governance Recommendation

### Weak output

> "You should implement data governance. Make sure you have policies and assign owners."

### Why it is weak

- No actionable structure (what policies? which owners?)
- No decision rules or quality gates
- No artifact references
- No source backing
- Could apply to any organization without specificity

### Strong output

> "Governance operating model recommendation:
> 
> 1. **Scope**: Start with tier-1 financial and customer data (classification coverage audit gate).
> 2. **Ownership**: Assign domain stewards per business unit using DAMA's three-role model (owner, steward, custodian). Reference: DAMA-DMBOK (src-001).
> 3. **Policy-as-code**: Implement classification tags at ingestion and propagate through lineage. Reference: AWS Data Analytics Lens (src-002).
> 4. **Pilot**: Run a 4-week pilot in one domain before tenant-wide rollout. Decision rule: If a governance change is proposed, then pilot in one domain first.
> 5. **Quality gate**: Verify stewardship accountability, metadata completeness, and access recertification cycle before expanding."

### Skills that should use this pattern

- `federated-governance-operating-model`
- `data-stewardship-ownership-mapping`
- `classification-taxonomy-architecture`

---

## Pattern: Acceptance Criteria

### Weak output

> "The user should be able to log in. The system should be fast and secure."

### Why it is weak

- "Fast" and "secure" are vague adjectives, not measurable criteria
- No edge cases or error conditions
- No Given-When-Then structure
- No testability

### Strong output

> "**User Story**: As a registered user, I want to log in with my email and password so that I can access my dashboard.
> 
> **Acceptance Criteria**:
> - Given a valid email and password, when the user submits the login form, then the user is redirected to the dashboard within 2 seconds.
> - Given an invalid password, when the user submits the login form, then an error message 'Invalid credentials' is displayed and the login attempt is logged.
> - Given 5 consecutive failed attempts, when the user tries again, then the account is locked for 15 minutes and an email notification is sent.
> - Given a locked account, when the user clicks 'Forgot password', then a reset link is sent to the registered email within 30 seconds.
> 
> **Definition of Done**: All criteria pass automated tests; accessibility audit (WCAG 2.1 AA) complete; security review for OWASP Top 10 risks complete."

### Skills that should use this pattern

- `given-when-then-authoring`
- `edge-case-identification`
- `definition-of-done-crafting`

---

## Pattern: Architecture Decision Record

### Weak output

> "We decided to use microservices because they are scalable."

### Why it is weak

- No context about the problem being solved
- No alternatives considered
- "Scalable" is vague; no measurable quality attribute scenario
- No consequences or risks documented
- No link to code or review process

### Strong output

> "# ADR-042: Adopt event-driven architecture for order processing
> 
> **Status**: Accepted
> **Date**: 2024-03-15
> **Decision-makers**: Jane Doe (Architect), John Smith (Engineering Lead)
> **Consulted**: Platform Team, Security Team
> **Informed**: Product Team
> 
> ## Context
> 
> The monolithic order service handles 10,000 orders/day with synchronous REST calls. Peak load (Black Friday) causes cascading timeouts when the payment gateway degrades.
> 
> ## Decision Drivers
> 
> - Decouple order creation from payment processing to prevent cascading failures
> - Support 50,000 orders/day within 18 months
> - Maintain audit trail for compliance (SOX)
> 
> ## Considered Options
> 
> 1. **Keep synchronous REST, add circuit breakers** — simpler, but still tightly coupled; does not solve audit trail requirement.
> 2. **Adopt event-driven architecture (Kafka)** — decouples services, supports audit trail via event log, adds operational complexity.
> 3. **Hybrid: async for payment, sync for inventory** — partial decoupling, increases architectural inconsistency.
> 
> ## Decision
> 
> Choose Option 2: Adopt event-driven architecture with Kafka for order lifecycle events.
> 
> ## Consequences
> 
> - **Positive**: Decouples order and payment services; event log provides audit trail; supports future scaling.
> - **Negative**: Team must learn Kafka operations; need new runbooks for event replay and dead-letter queue handling.
> - **Risk**: Eventual consistency may confuse downstream consumers; requires explicit consumer education.
> 
> ## Confirmation
> 
> - Kafka topic `orders.v1` created with retention policy 7 days.
> - Consumer contract tests added to CI.
> - Runbook for event replay drafted and reviewed."

### Skills that should use this pattern

- `adr-authoring-madr`
- `adr-trade-off-analysis`
- `event-driven-pattern-selection`

---

## Pattern: Incident Triage Brief

### Weak output

> "There is an outage. We are looking into it. Will update soon."

### Why it is weak

- No severity classification
- No roles assigned
- No timeline or impact quantification
- No action-oriented language
- No expected next update time

### Strong output

> "**Incident Declaration**: SEV-2 — Customer checkout degraded
> 
> **Impact**: ~15% of checkout attempts failing with 504 Gateway Timeout (confirmed via payment gateway dashboard). Affected region: US-East.
> 
> **Roles**:
> - Incident Commander: Alex Chen
> - Operations Lead: Maria Garcia
> - Communications Lead: Sam Patel
> 
> **Current Status**: Mitigation in progress. We have identified the payment gateway connection pool exhaustion as the trigger. Operations Lead is scaling connection pools and enabling circuit breaker fallback.
> 
> **Next Update**: 15 minutes (14:30 UTC) or upon significant change.
> 
> **Action Needed from Stakeholders**: None at this time. Customer-facing status page updated."

### Skills that should use this pattern

- `incident-commander-basics`
- `severity-classification`
- `escalation-brief-writing`

---

## Pattern: Agent Tool Use Instruction

### Weak output

> "Use the search tool to find information. Then use the calculator if needed."

### Why it is weak

- Vague tool descriptions ("find information" — what information?)
- No parameter schemas
- No error handling guidance
- No decision rules for when to use which tool
- No output validation requirements

### Strong output

> "## Tool Use Instructions
> 
> ### `search_knowledge_base(query: string, filters: object)`
> 
> **When to use**: When the user asks a question that requires factual information not present in the current context. Do NOT use for opinions, creative writing, or calculations.
> 
> **Parameters**:
> - `query`: A concise, keyword-rich search string. Must be ≤200 characters.
> - `filters`: Optional. Use `{"domain": "data-governance"}` to narrow scope when the question is domain-specific.
> 
> **Error handling**:
> - If search returns zero results, inform the user and ask for clarification. Do NOT hallucinate an answer.
> - If search returns >10 results, apply the top-3 relevance filter and summarize.
> 
> **Output validation**: After receiving search results, verify that the answer directly addresses the user's question before responding. If not, perform a follow-up search with refined query.
> 
> ### `calculate(expression: string, precision: number)`
> 
> **When to use**: Only for mathematical expressions that cannot be solved mentally. Always prefer mental math for simple arithmetic.
> 
> **Parameters**:
> - `expression`: Valid mathematical expression in infix notation.
> - `precision`: Number of decimal places (default 2, max 10).
> 
> **Validation**: After calculation, perform a sanity check (order of magnitude, sign) and report if the result seems unexpected."

### Skills that should use this pattern

- `tool-use-orchestrator`
- `schema-contract-designer`
- `safety-gatekeeper`

---

## Pattern: Risk Triage Assessment

### Weak output

> "This project has some risks. We should monitor them."

### Why it is weak

- No specific risks identified
- No probability or impact assessment
- No treatment plan
- No owner or review cadence
- No decision rules for escalation

### Strong output

> "**Risk Triage Assessment — Project Alpha**
> 
> | Risk ID | Description | Probability | Impact | Risk Score | Treatment | Owner | Review Date |
> |---|---|---|---|---|---|---|---|
> | R-01 | SAP MDG workflow approval bottleneck delays go-live | Medium | High | 12 | Mitigate: Parallel workflow testing in Q2; backup approver pool | D. Kharlanau | 2024-04-15 |
> | R-02 | Data quality rules from legacy system incompatible with BRFplus | High | Medium | 10 | Mitigate: Rule mapping workshop in March; prototype 5 critical rules | A. Seifried | 2024-03-30 |
> | R-03 | Key data steward leaves before knowledge transfer | Low | High | 6 | Transfer: Document stewardship decisions in ADR-037; shadowing program | HR + Team Lead | 2024-03-20 |
> 
> **Escalation trigger**: If any risk score exceeds 15, or if treatment plan slips by >2 weeks, escalate to program director.
> 
> **Decision rule**: If a risk exceeds organizational risk appetite (score >12), then escalate to senior leadership before proceeding."

### Skills that should use this pattern

- `risk-triage-and-register-management`
- `assumption-log-maintenance`
- `escalation-brief-writing`