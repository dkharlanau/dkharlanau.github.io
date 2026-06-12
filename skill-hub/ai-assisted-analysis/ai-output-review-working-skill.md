---
layout: default
title: "AI Output Review Working Skill"
description: "Review any AI-generated output for hallucinations, inconsistency, and hidden assumptions before using it for work decisions."
permalink: /skill-hub/ai-assisted-analysis/ai-output-review-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI Output Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI Output Review</h1>
  <p class="lead">Review any AI-generated output for hallucinations, inconsistency, and hidden assumptions before using it for work decisions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>AI can generate code, analysis, recommendations, and summaries in seconds, but it invents facts, contradicts itself, and hides assumptions behind confident language. This skill provides a structured review workflow that catches these failures before the output is used in a document, a system, or a client conversation. The output is an AI Output Review Log that records what was checked, what was wrong, and what was corrected.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>After receiving any AI-generated output that you plan to forward, publish, or act on.</li>
      <li>When AI produces code, configuration, or scripts that will run in a production or pre-production system.</li>
      <li>When AI generates business analysis, requirements, or recommendations that will be presented to stakeholders.</li>
      <li>When AI summarizes data, incidents, or project status and you need to confirm the facts before using the summary.</li>
      <li>When AI provides an explanation of a system, process, or error and you are not certain the explanation is accurate.</li>
      <li>When multiple AI outputs are combined and you need to check for contradictions between them.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>AI generates a SAP table analysis with wrong field names</h3>
    <p>An AI produces a list of fields to check for a customer master data issue and includes ZZ_CUSTOMER_GROUP and Z_REGION_CODE as standard fields. Neither field exists in the target system. If the analyst copies this list into an investigation guide, the team will waste hours searching for fields that are not there, and the real root cause will remain unaddressed.</p>
    <h3>AI writes a shell script with deprecated commands</h3>
    <p>An AI generates a bash script to automate SAP transport imports and uses an obsolete command that was removed in the current kernel version. The script looks correct and runs in a test environment that still has the old command, but fails in production. The failure blocks a critical transport and requires emergency manual intervention.</p>
    <h3>AI summarizes a project status with fabricated milestones</h3>
    <p>An AI synthesizes a project status from chat logs and email threads and reports that the integration testing phase was completed last week. In reality, the phase was delayed and is still open. The false summary is sent to the steering committee, creating a credibility gap when the delay is discovered during the next review.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>AI-generated output</strong> — the raw text, code, or analysis produced by the AI tool.</li>
      <li><strong>Source context</strong> — the original documents, data, tickets, or transcripts that the AI was supposed to analyze.</li>
      <li><strong>Domain reference</strong> — system documentation, configuration guides, or known-behavior references for the subject matter.</li>
      <li><strong>Previous review logs</strong> — patterns of past AI errors on similar tasks (optional).</li>
      <li><strong>Intended use</strong> — a clear statement of what the output will be used for, so the review can focus on the highest-risk claims.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which specific claims does the AI make, and what evidence supports each claim?</li>
      <li>Which technical objects, field names, transaction codes, or APIs does the AI reference, and do they exist in this system?</li>
      <li>What assumptions does the AI make about the environment, data, process, or timing?</li>
      <li>Does the AI contradict itself, or does it contradict the source material?</li>
      <li>What is missing from the AI output that a human expert would normally include?</li>
      <li>What would happen if the most important claim in the AI output were wrong?</li>
      <li>Does the AI use generic language that sounds correct but is not actionable or verifiable?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Capture the raw output.</strong> Save the AI output exactly as received, with metadata about the tool, model, date, and prompt used.</li>
      <li><strong>Define the review scope.</strong> Based on the intended use, decide which parts of the output are high-risk and which are low-risk. Focus review time on high-risk sections.</li>
      <li><strong>Flag factual claims.</strong> Highlight every specific claim about a system, a number, a date, a person, a process step, or a technical object.</li>
      <li><strong>Cross-reference with source material.</strong> Compare each factual claim against the source documents, system data, or known configuration. Mark each claim as verified, unverified, or false.</li>
      <li><strong>Check for internal consistency.</strong> Read the output as a whole. Look for contradictions between sections, conflicting numbers, or recommendations that conflict with stated constraints.</li>
      <li><strong>Surface hidden assumptions.</strong> Identify what the AI assumes to be true but never states explicitly. List each assumption and its risk if it is wrong.</li>
      <li><strong>Assess completeness.</strong> Compare the output against a checklist of what a competent human would include for this type of artifact. Flag missing elements.</li>
      <li><strong>Produce the review log.</strong> Document every check, every finding, and every correction. Include the original claim, the verification result, and the corrected version.</li>
      <li><strong>Decide on usage.</strong> Based on the review log, decide whether the output is usable as-is, usable after correction, or must be discarded and rewritten.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a factual claim can be verified against source material, accept it. If it cannot be verified, flag it as unverified.</li>
      <li>If a factual claim is proven false, remove it and log it as a hallucination. Do not try to edit it into a correct claim.</li>
      <li>If the AI contradicts itself, trust the version that aligns with source material; if neither aligns, flag both as uncertain.</li>
      <li>If an assumption is unstated but critical, elevate it to a risk and assign an owner to verify it.</li>
      <li>If the output is missing a required element, add it manually or send the output back for regeneration with a clearer prompt.</li>
      <li>If the AI uses generic language that cannot be verified, demand specific terms, numbers, or examples before accepting.</li>
      <li>If the output is intended for a client, apply a stricter review standard than if it is for internal drafting.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>AI Output Review Log</strong> — a record of every claim checked, its verification result, and the correction applied.</li>
      <li><strong>Confidence Map</strong> — a section-by-section label showing which parts of the output are trusted, corrected, or discarded.</li>
      <li><strong>Correction List</strong> — a concise list of changes made to the AI output before it is used.</li>
      <li><strong>Assumption and Risk Register</strong> — unstated assumptions that must be verified before the output is relied on.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>AI Output Review Log</h3>
    <pre><code>---
title: AI Output Review Log
ai_tool: [tool name / model]
date: [YYYY-MM-DD]
reviewer: [name]
intended_use: [document / code / presentation / decision]
---

## Source
- **Original prompt**: [summary or attached]
- **AI output length**: [pages / lines / tokens]
- **Source material**: [documents / tickets / data used]

## Claim Verification
| # | Section | Claim | Source Check | Result | Correction |
|---|---------|-------|--------------|--------|------------|
| 1 | [heading] | [exact claim] | [doc / system / known] | [Verified / False / Unverified] | [none / corrected / removed] |

## Consistency Check
- [ ] No internal contradictions
- [ ] No contradictions with source material
- [ ] No contradictions with known system behavior

## Assumption Register
| # | Assumption | Risk if Wrong | Owner to Verify |
|---|------------|-------------|-----------------|
| 1 | [assumption] | [consequence] | [name] |

## Confidence Map
| Section | Confidence | Notes |
|---------|------------|-------|
| [heading] | [High / Medium / Low / Discarded] | [reason] |

## Usage Decision
- [ ] Usable as-is
- [ ] Usable after correction
- [ ] Must be discarded and rewritten
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every factual claim in the output is either verified or explicitly flagged as unverified.</li>
      <li>[ ] Every hallucination or false claim is logged, not silently corrected.</li>
      <li>[ ] The confidence map covers every section of the AI output.</li>
      <li>[ ] The assumption register contains at least one entry, or a note that no assumptions were found.</li>
      <li>[ ] The review log can be read by someone who did not see the AI output and still understand the findings.</li>
      <li>[ ] The correction list is specific enough that another reviewer can apply the same changes.</li>
      <li>[ ] A usage decision is recorded and signed off by the reviewer.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Copying AI output into a client document without any review. <strong>Consequence:</strong> A hallucinated claim reaches the client, damages credibility, and may trigger incorrect work.</li>
      <li><strong>Mistake:</strong> Reviewing only for grammar and tone while ignoring factual accuracy. <strong>Consequence:</strong> A technically polished but factually wrong output is approved and used.</li>
      <li><strong>Mistake:</strong> Trusting the AI because it sounds confident. <strong>Consequence:</strong> Invented field names, deprecated commands, or fabricated dates are treated as facts.</li>
      <li><strong>Mistake:</strong> Failing to log corrections so the same AI error pattern repeats on the next task. <strong>Consequence:</strong> The team never learns which prompts or topics produce unreliable output.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A consultant receives a five-page AI-generated analysis of a SAP integration error, skims it for obvious nonsense, and forwards it to the client with a note that it was "AI-assisted." The analysis incorrectly states that the error is caused by a missing filter in the IDoc distribution model, when the actual cause is a misconfigured partner profile. The client acts on the wrong diagnosis and spends two days rebuilding the distribution model before discovering the real issue. The consultant has no record of what was checked and cannot explain why the wrong cause was sent.</p>
    <h3>Strong output — good AI usage</h3>
    <pre><code>## AI Output Review Log — Integration Error Analysis

### Claim Verification
| # | Claim | Source Check | Result |
|---|-------|--------------|--------|
| 1 | Error caused by missing IDoc filter | Checked WE20 partner profile | FALSE — partner profile uses wrong message type |
| 2 | Message type is ORDERS | Checked EDP13 and partner profile | VERIFIED |
| 3 | Distribution model needs rebuild | Checked BD64 and source docs | UNVERIFIED — no evidence in logs |

### Correction Applied
- Removed the claim about the IDoc filter being the root cause.
- Added the correct root cause: partner profile message type mismatch in WE20.
- Flagged claim 3 as unverified and escalated to the integration team.

### Usage Decision
- Corrected version approved for client communication.
- Unverified claim held back pending integration team confirmation.</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are an AI output review assistant.
Context: I have received AI-generated output for [type of work artifact]. I need you to review it systematically before I use it.
Tasks:
1. Flag every factual claim the AI makes, especially technical objects, numbers, dates, and named people.
2. Cross-reference each claim against the source material I provide.
3. Identify any claim that contradicts the source material or itself.
4. Surface hidden assumptions that the AI did not state explicitly.
5. Check for completeness: what would a human expert normally include that the AI omitted?
6. Produce an AI Output Review Log in the template format provided.
Constraints: Do not trust the AI's tone of confidence as evidence. Do not skip a claim because it "sounds right." If you cannot verify a claim, label it as unverified. Do not invent source material.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the source material and the intended use before starting the review.</li>
      <li>Produce the review log as a separate artifact so the review itself is traceable.</li>
      <li>Log every hallucination or false claim so the team can improve prompts or avoid the pattern.</li>
      <li>Link findings to specific sections or line numbers in the AI output for easy correction.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not copy AI output into a deliverable without producing a review log.</li>
      <li>Do not treat grammar and polish as evidence of factual accuracy.</li>
      <li>Do not skip cross-referencing because the AI output is long or the deadline is tight.</li>
      <li>Do not present your own assumptions as verified facts during the review.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/">Validate AI-Generated Requirements</a> — focused validation for requirements-specific AI output.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-accountability-working-skill/">AI Accountability</a> — defining ownership and review gates for AI-generated output.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/convert-notes-to-requirements-working-skill/">Convert Notes to Requirements</a> — turning raw input into structured drafts before AI review.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-assisted-documentation-review-working-skill/">AI-Assisted Documentation Review</a> — using AI to pre-review large documents with human sign-off.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — how process documentation is structured for AI-assisted review.</li>
      <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a> — operational context for AI-assisted analysis in SAP support.</li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — building reviewable knowledge records from AI output.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI output review practices. It is not official vendor guidance, SAP documentation, or an AI governance framework. The review steps assume access to source material or system documentation; if neither is available, the verification results will be less reliable. AI tools and models change frequently; the error patterns described here are representative, not exhaustive. Use this skill as a structured starting point, not as a guarantee that all AI errors will be caught.</p>
  </section>
</article>
