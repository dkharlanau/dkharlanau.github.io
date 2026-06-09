---
layout: default
title: "Business Rules Discovery Working Skill"
description: "Extract the decision logic that governs how a business operates, document it independently of any system, and identify where current systems enforce, violate, or ignore it."
permalink: /skill-hub/business-analysis/business-rules-discovery-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Business Rules Discovery</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Business Rules Discovery Working Skill</h1>
  <p class="lead">Find the hidden decision logic that runs your business, write it down, and check whether your systems actually enforce it.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Business rules are the decision logic that determines what happens when: who approves what, which customers get which terms, when an order blocks, how a price is calculated. Most of this logic lives in people's heads, scattered spreadsheets, or buried in code. This skill extracts rules independently of any system, documents them with conditions and outcomes, and maps where they are enforced, violated, or missing. The output prevents the common failure where a new system is built without critical logic, or where existing systems enforce rules that the business no longer wants.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A system implementation or replacement is planned and no one knows all the rules the current system enforces.</li>
      <li>A process redesign keeps failing because different teams apply different versions of the same rule.</li>
      <li>A data quality investigation reveals records that violate policy but were created anyway.</li>
      <li>A compliance audit asks for documented business rules and the answer is "ask the person who retired last year."</li>
      <li>An integration mapping exercise needs to know which rules apply at which system boundary.</li>
      <li>An incident shows system behavior that contradicts business expectation, suggesting a hidden or changed rule.</li>
      <li>A master data governance setup needs validation rules with clear owners and override conditions.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Customer credit limit assignment</h3>
    <p>A sales team complains that credit limits seem arbitrary. Discovery reveals three rules: new customers receive a 10,000 EUR limit by default; existing customers receive 3 times their average monthly billing; exceptions require CFO approval and are logged to audit. The current system enforces only the default rule. The other two are applied manually via spreadsheet and email, causing delays and inconsistency. The rule documentation must separate the business intent from the current broken implementation.</p>

    <h3>Purchase order approval hierarchy</h3>
    <p>A procurement process has approval delays. Discovery reveals: orders under 5,000 EUR require a manager; 5,000 to 50,000 EUR require a director; over 50,000 EUR require a VP. Emergency orders bypass up to 10,000 EUR with a post-hoc review. The current SAP release strategy enforces only the manager and director levels. The VP level is handled by email after the fact. The emergency bypass is not in the system at all. The rules must be documented before the release strategy can be reconfigured.</p>

    <h3>Delivery block logic</h3>
    <p>A warehouse reports unpredictable delivery blocks. Discovery reveals: incomplete address blocks delivery for all customers; credit hold blocks delivery for non-cash customers; specific material groups (hazardous, cold chain) require special handling and block standard delivery. The current system checks address and credit but not material group. The material group rule is enforced by a warehouse clerk manually checking a paper list. The rules must be documented so the system can be extended or the manual check can be governed.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Current system configuration showing where rules are enforced: workflows, validation routines, condition tables.</li>
      <li>User interviews with people who apply, override, or suffer from the rules.</li>
      <li>Regulatory documents or compliance frameworks that mandate specific rules.</li>
      <li>Incident tickets showing where rules were violated or produced unexpected results.</li>
      <li>Existing procedure manuals, policy documents, or training materials.</li>
      <li>Master data samples showing how rules affect different record types.</li>
      <li>Workflow logs or approval history showing override frequency and approvers.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What conditions must be true for this action to happen, and what conditions prevent it?</li>
      <li>Who can override this rule, under what conditions, and what evidence is required?</li>
      <li>What happens when two rules conflict? Which one takes precedence?</li>
      <li>Where is this rule enforced today: system, manual check, spreadsheet, or unwritten habit?</li>
      <li>What is the business consequence if this rule is not followed?</li>
      <li>Which rules are written down and which exist only in people's heads?</li>
      <li>When did this rule last change, and who authorized the change?</li>
      <li>Which rules are enforced by the system but no longer match business policy?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify decisions in the process.</strong> Look for points where the path splits: approve/reject, block/release, calculate price, assign category.</li>
      <li><strong>For each decision, list conditions and outcomes.</strong> Format: "If [condition] and [condition], then [outcome]." Be specific about field values, thresholds, and dates.</li>
      <li><strong>Separate business rule from system implementation.</strong> The rule is the intent. The implementation is how a specific system enforces it. Document both, but separately.</li>
      <li><strong>Identify rule owner and override authority.</strong> Who can change the rule? Who can override it? What evidence is required for override?</li>
      <li><strong>Map where the rule is enforced and where it is missing.</strong> Use a matrix: rule vs system. Mark enforced, partially enforced, manual, or missing.</li>
      <li><strong>Document conflicts between rules.</strong> When two rules produce different outcomes for the same conditions, record both and flag for governance decision.</li>
      <li><strong>Validate with the rule owner.</strong> Walk through each rule, condition, and outcome with the person who has authority to change it.</li>
      <li><strong>Document in a Business Rules Catalog.</strong> One entry per rule. Include conditions, outcomes, owner, enforcement map, override conditions, and related rules.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a rule exists only in a user's head, it is not a rule until documented and validated with the owner.</li>
      <li>If two rules conflict, document both and flag for governance decision — do not silently pick one.</li>
      <li>If a rule is enforced in code but not documented, the rule is at risk of being lost in the next upgrade.</li>
      <li>If a rule has no owner, it is a governance gap, not a technical gap.</li>
      <li>If a rule is violated in more than 5 percent of transactions, either the rule is wrong or the enforcement is broken.</li>
      <li>If a rule can be overridden, the override conditions must be as explicit as the rule itself.</li>
      <li>If a system enforces a rule that contradicts current business policy, the system is out of date, not the business.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Business Rules Catalog</strong> — One entry per rule. Contains conditions, outcomes, owner, enforcement location, override conditions, and related rules. See template below.</li>
      <li><strong>Rule Ownership Matrix</strong> — Table mapping each rule to its business owner, technical implementer, and override authority.</li>
      <li><strong>Conflict Register</strong> — List of rule conflicts with business impact and governance decision status.</li>
      <li><strong>Enforcement Gap List</strong> — Rules that are documented but not enforced in any system, with proposed enforcement mechanism.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Business Rules Catalog entry (compact)</h3>
    <pre><code>---
artifact: Business Rules Catalog Entry
id: BR-001
status: draft | reviewed | approved
---

## Rule name
<!-- Short, descriptive name. Example: "Customer Credit Limit Assignment" -->

## Conditions
<!-- List all conditions that must be true. Example: "Customer is new (no prior orders) AND account group is Z001 (Domestic)." -->

## Outcomes
<!-- What happens when conditions are met. Example: "Credit limit = 10,000 EUR. Valid for 12 months." -->

## Business owner
<!-- Who can change this rule -->

## Override authority
<!-- Who can override and under what conditions -->

## Enforcement location
<!-- Where this rule is enforced: system, module, transaction, manual process -->

## Enforcement status
<!-- enforced | partially enforced | manual | missing -->

## System implementation
<!-- How the current system enforces this rule. Separate from business intent. -->

## Violation handling
<!-- What happens when the rule is broken -->

## Related rules
<!-- Links to rules that interact with this one -->

## Last validated
<!-- Date and validator name -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every rule has explicit conditions and outcomes.</li>
      <li>Every rule has a named business owner who can authorize changes.</li>
      <li>Rules are separated from current system implementation.</li>
      <li>Override conditions are documented, not assumed.</li>
      <li>Conflicts between rules are flagged with governance status.</li>
      <li>Enforcement locations are mapped for every rule.</li>
      <li>Rules are validated with owners, not just inferred from system behavior.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Documenting system behavior as business rules.</strong> Consequence: rules are tied to current system limitations. The new system inherits old constraints that were technical, not business.</li>
      <li><strong>Failing to identify override conditions.</strong> Consequence: exceptions break processes because no one knows who can approve them or what evidence is required.</li>
      <li><strong>Ignoring rule conflicts.</strong> Consequence: unpredictable outcomes when two rules apply to the same situation. Users develop private workarounds.</li>
      <li><strong>Not identifying rule owners.</strong> Consequence: rules change without authority, or stale rules persist because no one is responsible for updating them.</li>
      <li><strong>Missing tacit rules that exist only in people's heads.</strong> Consequence: new systems omit critical logic that was never written down. Business operations degrade after go-live.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>AI agents should use this skill to extract and document business rules before recommending system changes, integrations, or automation.</p>
    <ul>
      <li><strong>Start with decisions, not systems.</strong> For each decision point in a process, ask what conditions lead to what outcomes.</li>
      <li><strong>Separate the business intent from the current system implementation.</strong> Document both, but in separate fields.</li>
      <li><strong>Identify who can change the rule.</strong> If no one can, flag a governance gap.</li>
      <li><strong>Document override conditions explicitly.</strong> Who can override, what evidence is required, and how the override is logged.</li>
      <li><strong>Flag conflicts between rules instead of resolving them.</strong> Document both rules and ask who has governance authority.</li>
      <li><strong>Map where each rule is enforced.</strong> Use a matrix: rule vs system. Mark enforced, partial, manual, or missing.</li>
      <li><strong>Produce a Business Rules Catalog entry per rule.</strong> Validate every entry with the named owner.</li>
      <li><strong>Do not infer rules from system behavior alone.</strong> System behavior may be a bug, a workaround, or outdated configuration.</li>
      <li><strong>Link to Atlas diagnostics</strong> when rules relate to SAP validation. For example, delivery block rules should reference <a href="/atlas/diagnostics/sap-delivery-block-analysis/">SAP Delivery Block Analysis</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a></li>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Rule context for credit limits.</li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a> — Approval rule context.</li>
      <li><a href="/atlas/diagnostics/sap-delivery-block-analysis/">SAP Delivery Block Analysis</a> — Block rule context.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — Rule violation scenario.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of business rules discovery practices. It is not official BABOK, DMN, or SAP documentation. It focuses on operational decision logic in enterprise systems and may not cover complex decision models or predictive analytics rules.</p>
    <p>Known limitations: the skill assumes access to rule owners and system configuration. In environments with high turnover or poor documentation, rule discovery becomes archaeological work. The skill does not cover formal decision model notation (DMN) or business rules management systems (BRMS) implementation.</p>
  </section>
</article>
