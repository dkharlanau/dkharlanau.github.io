---
layout: default
title: "AI-Assisted Documentation Review Working Skill"
description: "Use AI to accelerate documentation review while keeping human judgment in control of every finding, producing a structured review report."
permalink: /skill-hub/ai-assisted-analysis/ai-assisted-documentation-review-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI-Assisted Documentation Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI-Assisted Documentation Review</h1>
  <p class="lead">Use AI to accelerate documentation review while keeping human judgment in control of every finding, producing a structured review report.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Technical documents, design specifications, handover packages, and compliance records are often too long for manual review under tight deadlines. AI can pre-scan these documents for gaps, inconsistencies, and structural issues, but it cannot replace human judgment on context, intent, or stakeholder impact. This skill provides a workflow where AI does the first pass and the human does the second pass, producing a Documentation Review Report that separates AI-assisted findings from human-reviewed findings.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A large technical document must be reviewed before a deadline and there is not enough time for a purely manual review.</li>
      <li>A document has been updated multiple times and you need to check for version drift, inconsistency, or orphaned sections.</li>
      <li>A compliance or regulatory document requires coverage checking against a standard set of required topics.</li>
      <li>A handover document needs a completeness review before the outgoing team leaves.</li>
      <li>Multiple documents describe the same system and you need to identify contradictions between them.</li>
      <li>You want to use AI to surface potential issues but do not want to blindly trust its findings.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>SAP integration design document needs review in two hours</h3>
    <p>A project team has produced an eighty-page SAP integration design document for a new EDI interface. The technical review meeting is in two hours. A manual read is impossible. The AI pre-scan flags three sections where the error handling description contradicts the retry policy table. The human reviewer focuses on those three sections and confirms the contradiction, saving the review meeting from discovering the issue live.</p>
    <h3>Handover document has gaps that the outgoing team forgot</h3>
    <p>A senior consultant is leaving the project and has produced a forty-page handover document. The AI pre-scan checks the document against a standard handover checklist and flags that there is no section on monitoring alerts, no owner listed for the batch job schedule, and no contact information for the second-line support team. The human reviewer confirms all three gaps are real and the outgoing team adds them before the handover is signed off.</p>
    <h3>Regulatory compliance document needs consistency checking</h3>
    <p>A data governance team must submit a compliance document that references SAP master data policies, GDPR retention rules, and internal audit procedures. The document is sixty pages and was written by three authors. The AI pre-scan flags that one author uses the term "data subject" while another uses "data owner" for the same role, and that a referenced policy number is out of date. The human reviewer confirms the terminology conflict and the stale policy reference before submission.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Document to review</strong> — the current version of the document, in a machine-readable format.</li>
      <li><strong>Review criteria or checklist</strong> — the standard topics, structure, or rules the document must satisfy.</li>
      <li><strong>Previous version or baseline</strong> — to check for unintended changes or missing content (optional).</li>
      <li><strong>Stakeholder list or ownership matrix</strong> — to verify that the right owners and contacts are named.</li>
      <li><strong>Reference documents</strong> — related documents that the reviewed document should be consistent with.</li>
      <li><strong>Intended audience</strong> — so the AI can assess whether the level of detail and terminology are appropriate.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which required sections are present, and which are missing?</li>
      <li>Does the document use consistent terminology throughout, or are there conflicting terms for the same concept?</li>
      <li>Are all referenced documents, policies, and versions current and accurate?</li>
      <li>Does the document contradict any related document or known system behavior?</li>
      <li>Are the owners, contacts, and approvers named and still correct?</li>
      <li>Does the document contain placeholders, TODOs, or draft markers that should have been removed?</li>
      <li>Is the level of detail appropriate for the intended audience and use case?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Prepare the review scope.</strong> Define which sections, topics, and criteria the review must cover. Decide what the AI will check and what the human will check.</li>
      <li><strong>Run the AI pre-scan.</strong> Submit the document and the review criteria to the AI. Ask it to flag missing sections, inconsistent terminology, stale references, contradictions, and placeholder content.</li>
      <li><strong>Capture the AI findings.</strong> Save the AI output as a structured list with section references and severity labels.</li>
      <li><strong>Validate each AI finding.</strong> Go through the AI findings one by one. Confirm true positives, reject false positives, and note any findings the AI missed.</li>
      <li><strong>Perform the human review pass.</strong> Focus on context, intent, stakeholder impact, and anything the AI cannot judge. Add human-only findings to the list.</li>
      <li><strong>Consolidate findings into a report.</strong> Combine AI-assisted and human-reviewed findings into a single Documentation Review Report. Label the source of each finding.</li>
      <li><strong>Assign owners and deadlines.</strong> For every finding that requires action, assign an owner and a deadline for correction.</li>
      <li><strong>Close the review.</strong> Track corrections until all findings are resolved or accepted as risks. Archive the report for audit.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the AI flags a gap and the human confirms it, record it as a confirmed finding. If the human rejects it, record it as a false positive.</li>
      <li>If the AI misses a gap that the human finds, record it as a missed finding and use it to improve the review criteria or prompt.</li>
      <li>If the AI finds a contradiction between documents, verify both documents before deciding which one is correct.</li>
      <li>If the document contains placeholders or draft markers, treat them as findings regardless of whether the AI flagged them.</li>
      <li>If the document is for a client, apply a stricter review standard than if it is for internal use.</li>
      <li>If the AI and human disagree on severity, the human decision takes precedence. Log the disagreement to improve future AI pre-scans.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Documentation Review Report</strong> — a structured report with AI-assisted findings and human-reviewed findings, each with a severity, status, and owner.</li>
      <li><strong>AI Pre-Scan Findings</strong> — the raw AI output, preserved for traceability and improvement.</li>
      <li><strong>Correction Tracker</strong> — a list of required corrections with owners and deadlines.</li>
      <li><strong>Review Sign-Off</strong> — a record that the document was reviewed, by whom, and when.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Documentation Review Report</h3>
    <pre><code>---
title: Documentation Review Report
document: [document name and version]
reviewer: [human reviewer name]
ai_tool: [AI tool used for pre-scan]
date: [YYYY-MM-DD]
---

## Review Scope
- **Sections covered**: [list]
- **Criteria used**: [checklist / standard / policy]
- **AI pre-scan scope**: [structural / consistency / reference / terminology]
- **Human review scope**: [context / intent / stakeholder / accuracy]

## AI-Assisted Findings
| # | Section | Finding | Severity | AI Source | Human Verdict | Owner |
|---|---------|---------|----------|-----------|---------------|-------|
| 1 | [heading] | [description] | [Major / Minor / Info] | [AI flag] | [Confirmed / False positive] | [name] |

## Human-Reviewed Findings
| # | Section | Finding | Severity | Human Verdict | Owner |
|---|---------|---------|----------|---------------|-------|
| 1 | [heading] | [description] | [Major / Minor / Info] | [Confirmed] | [name] |

## False Positives Log
| # | AI Finding | Why It Was Wrong | Lesson for Prompt |
|---|------------|------------------|-------------------|
| 1 | [description] | [reason] | [how to avoid next time] |

## Correction Tracker
| # | Finding | Correction Required | Owner | Deadline | Status |
|---|---------|---------------------|-------|----------|--------|
| 1 | [ref] | [action] | [name] | [YYYY-MM-DD] | [Open / Done] |

## Review Sign-Off
- [ ] All Major findings resolved or accepted as risk
- [ ] Reviewer sign-off: [name] [date]
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] The review scope is defined before the AI pre-scan begins.</li>
      <li>[ ] Every AI finding is validated by a human before it enters the report.</li>
      <li>[ ] Every human finding is labeled separately from AI findings.</li>
      <li>[ ] False positives are logged so the AI pre-scan prompt can be improved.</li>
      <li>[ ] Every finding that requires action has an owner and a deadline.</li>
      <li>[ ] The correction tracker shows the status of every finding.</li>
      <li>[ ] The review sign-off is completed before the document is published or submitted.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating the AI pre-scan as the final review. <strong>Consequence:</strong> False positives waste time, and false negatives create gaps that the human never checks because they assume the AI would have caught them.</li>
      <li><strong>Mistake:</strong> Not logging false positives, so the same AI errors repeat on every document. <strong>Consequence:</strong> The team loses trust in the AI pre-scan and abandons the workflow, returning to purely manual review.</li>
      <li><strong>Mistake:</strong> Asking the AI to review without giving it the review criteria. <strong>Consequence:</strong> The AI checks for generic issues and misses domain-specific gaps that the criteria would have surfaced.</li>
      <li><strong>Mistake:</strong> Letting the AI assign severity without human confirmation. <strong>Consequence:</strong> A minor stylistic issue is escalated as a major finding, while a real structural gap is labeled as informational.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A team runs an AI pre-scan on a SAP design document and receives a generic list of issues: "the document could be clearer," "some sections are long," and "consider adding a glossary." The team accepts these as the review result and marks the document as reviewed. The document is missing a critical section on rollback procedures, contains a contradictory error-handling statement, and references a deprecated API version. None of these are caught because the AI was not given specific criteria and the human did not validate the findings or do a second pass. The document is approved and the project proceeds with hidden gaps.</p>
    <h3>Strong output — good AI usage</h3>
    <pre><code>## Documentation Review Report — SAP EDI Integration Design v2.3

### AI-Assisted Findings
| # | Section | Finding | Severity | Human Verdict |
|---|---------|---------|----------|---------------|
| 1 | Section 4.2 | Error handling says "retry once" but table 3 says "retry three times" | Major | Confirmed |
| 2 | Section 7.1 | References API version 1.2; current version is 2.1 | Major | Confirmed |
| 3 | Section 5.3 | No rollback procedure described | Major | Confirmed |
| 4 | Section 2.1 | "Data owner" and "data steward" used interchangeably | Minor | Confirmed |

### Human-Reviewed Findings
| # | Section | Finding | Severity |
|---|---------|---------|----------|
| 1 | Section 6.4 | Monitoring alert owner is a contractor who leaves next week | Major |

### Correction Tracker
| # | Finding | Correction | Owner | Deadline | Status |
|---|---------|------------|-------|----------|--------|
| 1 | 4.2 | Align retry policy to three attempts | Integration Lead | 2026-06-14 | Open |
| 2 | 7.1 | Update API version and compatibility notes | Developer | 2026-06-14 | Open |
| 3 | 5.3 | Add rollback procedure with owner | Architect | 2026-06-15 | Open |
| 4 | 6.4 | Update alert owner to permanent team member | Operations Lead | 2026-06-13 | Open |</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a documentation review assistant.
Context: I need to review a [type of document] for [purpose]. The document is attached or pasted below. I want you to do a pre-scan for specific issues.
Tasks:
1. Check for missing required sections based on this checklist: [list].
2. Check for inconsistent terminology. Flag any term that is used with multiple meanings or conflicting definitions.
3. Check for stale or incorrect references to documents, versions, policies, or APIs.
4. Check for contradictions between sections or between this document and the reference documents I provide.
5. Check for placeholders, TODOs, draft markers, or incomplete sentences.
6. Assign a severity to each finding: Major (blocks approval), Minor (should be fixed), or Info (nice to have).
Constraints: Do not review tone, style, or grammar unless I ask for it. Do not invent findings. If a section is unclear, flag it as unclear rather than guessing what it means. Output findings in a structured table with section references.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the review criteria and reference documents before running the pre-scan.</li>
      <li>Validate every AI finding against the actual document before including it in the report.</li>
      <li>Log false positives to improve the prompt for the next review.</li>
      <li>Keep the AI pre-scan raw output as a separate artifact for traceability.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not treat the AI pre-scan as the final review.</li>
      <li>Do not accept AI severity ratings without human confirmation.</li>
      <li>Do not discard the AI findings without recording why they were rejected.</li>
      <li>Do not skip the human review pass because the AI output looks comprehensive.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a> — general review workflow for any AI-generated output.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/">Validate AI-Generated Requirements</a> — focused validation for requirements documents.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-prompt-briefing-work-artifacts-working-skill/">AI Prompt Briefing for Work Artifacts</a> — writing better prompts to improve AI pre-scan quality.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — structuring documentation so AI can review it effectively.</li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — structured diagnostic frame that feeds into documentation review criteria.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted documentation review. It is not official technical writing guidance, SAP documentation, or a certified quality assurance process. The effectiveness of the AI pre-scan depends on the quality of the prompt, the review criteria, and the document format. AI tools may struggle with complex tables, embedded diagrams, or heavily formatted documents. The human review pass remains essential and cannot be eliminated. Use this skill as a structured starting point, not as a replacement for human judgment.</p>
  </section>
</article>
