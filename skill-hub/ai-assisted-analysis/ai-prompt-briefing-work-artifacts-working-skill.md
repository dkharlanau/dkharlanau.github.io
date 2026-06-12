---
layout: default
title: "AI Prompt Briefing for Work Artifacts Working Skill"
description: "Write prompts that produce concrete, professional work artifacts rather than generic explanations, by structuring context, constraints, and output format."
permalink: /skill-hub/ai-assisted-analysis/ai-prompt-briefing-work-artifacts-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI Prompt Briefing for Work Artifacts</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI Prompt Briefing for Work Artifacts</h1>
  <p class="lead">Write prompts that produce concrete, professional work artifacts rather than generic explanations, by structuring context, constraints, and output format.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Most AI output is generic because the prompt was generic. A prompt that says "write a test plan" produces a vague outline that could apply to any project. A prompt that says "write a test plan for SAP SD pricing condition validation, covering boundary values, error paths, and IDoc status checks, in the format of step-by-step cases with preconditions and expected results" produces a usable draft. This skill teaches how to write prompts that specify the artifact type, the audience, the system context, the constraints, and the output format so the AI produces something a professional can use with minimal correction. The output is a Prompt Briefing Template that can be reused, shared, and improved over time.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are about to ask an AI to produce a work artifact and you want to minimize the time spent correcting the output.</li>
      <li>A team is using AI for recurring tasks and the outputs are inconsistent in quality and format.</li>
      <li>You received a generic AI output and need to rewrite the prompt so the next iteration is usable.</li>
      <li>You are onboarding a team member to AI-assisted work and want to give them a reusable template for writing prompts.</li>
      <li>An AI agent needs instructions that produce structured, traceable artifacts rather than conversational text.</li>
      <li>You are building a library of prompts for common enterprise tasks such as requirements drafting, test case design, incident analysis, and status reporting.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Team gets generic AI output for a requirements draft</h3>
    <p>A business analyst asks an AI to "write requirements for a customer master data change" and receives a one-page list of generic statements such as "the system shall allow users to update customer data." The requirements are unusable because they lack field names, business rules, validation logic, and acceptance criteria. The analyst applies the prompt briefing skill, rewrites the prompt with the specific system context, the exact fields affected, the business rules from the stakeholder interview, and the required output format. The second AI output is a structured requirements draft with numbered items, field references, and acceptance criteria that the analyst can validate in thirty minutes instead of rewriting from scratch.</p>
    <h3>AI-generated test cases lack structure and traceability</h3>
    <p>A tester asks an AI to "generate test cases for the new EDI interface" and receives a bullet list of informal descriptions such as "test that the invoice is sent correctly." The test cases have no IDs, no preconditions, no steps, no expected results, and no links to requirements. The tester applies the prompt briefing skill and rewrites the prompt with the required test case template, the acceptance criteria, the system configuration, and the constraint that every case must include a negative path. The second output is a structured test case draft that the tester validates and adds to the test plan in under an hour.</p>
    <h3>AI meeting summary is too vague to act on</h3>
    <p>A project manager asks an AI to "summarize the meeting" and receives a paragraph that says "the team discussed several topics and agreed on next steps." The summary is useless because it contains no decisions, no action owners, no deadlines, and no risks. The manager applies the prompt briefing skill and rewrites the prompt with the attendee list, the agenda, the required output tables, and the constraint that every action must have an owner and a deadline. The second output is a structured meeting synthesis that the manager can distribute after a ten-minute verification pass.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Artifact type</strong> — what the AI must produce: requirements, test cases, status report, meeting synthesis, etc.</li>
      <li><strong>Audience</strong> — who will read and act on the output: developers, testers, stakeholders, steering committee, etc.</li>
      <li><strong>System or domain context</strong> — the specific system, module, version, and environment that the output must reference.</li>
      <li><strong>Constraints</strong> — what the output must not do, must not assume, or must not include.</li>
      <li><strong>Output format</strong> — the structure, template, or schema the output must follow.</li>
      <li><strong>Examples</strong> — one or two examples of good output for this type of artifact, to set the quality bar.</li>
      <li><strong>Source material</strong> — the documents, data, or transcripts the AI must analyze or reference.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the artifact, and what makes it usable rather than generic?</li>
      <li>Who is the audience, and what level of detail and terminology do they need?</li>
      <li>What must be true for the output to be correct, and what assumptions must the AI avoid?</li>
      <li>What format must the output follow, and are there mandatory sections or fields?</li>
      <li>What are the most common failure modes for this type of AI output, and how can the prompt prevent them?</li>
      <li>What source material must the AI use, and what must it not use or invent?</li>
      <li>How will the output be reviewed, and what quality signals will the reviewer look for?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the artifact.</strong> Name the artifact and describe what a usable version looks like. Be specific about what it must contain and what it must not contain.</li>
      <li><strong>Identify the audience.</strong> Write down who will read the artifact, what they need to decide, and what they already know. This determines the level of detail and the terminology.</li>
      <li><strong>Describe the system context.</strong> List the relevant system, module, version, landscape, and any known configuration that the AI must reference correctly.</li>
      <li><strong>State the constraints.</strong> Write down what the AI must not do: invent fields, skip negative paths, use generic language, assume real-time data, etc.</li>
      <li><strong>Specify the output format.</strong> Provide the template, schema, or structure that the output must follow. Include mandatory sections and field names.</li>
      <li><strong>Provide examples.</strong> Include one or two examples of strong output for this artifact type. The AI will use these as a quality reference.</li>
      <li><strong>Assemble the source material.</strong> Gather the documents, data, or transcripts that the AI must analyze. Ensure they are current and complete.</li>
      <li><strong>Write the prompt.</strong> Combine the artifact definition, audience, system context, constraints, output format, examples, and source material into a single prompt. Use clear section headers.</li>
      <li><strong>Test the prompt.</strong> Run the AI with the prompt and review the output against the quality checklist. If the output is weak, identify which part of the prompt was unclear and refine it.</li>
      <li><strong>Save the prompt as a template.</strong> Store the working prompt in a shared location so the team can reuse and improve it.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the prompt is shorter than three sentences, the output will be generic. Expand the prompt with context, constraints, and format before running it.</li>
      <li>If the AI output misses a required section, add that section to the output format instruction in the prompt and regenerate.</li>
      <li>If the AI output invents facts, add a constraint that says "do not invent" and provide the source material explicitly.</li>
      <li>If the AI output is too verbose, add a constraint on length or ask for a specific number of items.</li>
      <li>If the AI output uses the wrong tone for the audience, add an audience description and a tone constraint.</li>
      <li>If the same prompt produces inconsistent outputs across different sessions, add examples to anchor the quality bar.</li>
      <li>If the prompt works well, save it as a template. If it fails, update the template before the next use.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Prompt Briefing Template</strong> — a reusable prompt structure for a specific artifact type.</li>
      <li><strong>Tested Prompt Library</strong> — a collection of prompts that have been tested and produce usable output.</li>
      <li><strong>Prompt Improvement Log</strong> — a record of what failed, why, and how the prompt was corrected.</li>
      <li><strong>Quality Checklist</strong> — a checklist for evaluating whether a prompt is ready for production use.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Prompt Briefing Template</h3>
    <pre><code>---
artifact: [name of artifact]
audience: [who will read it]
system_context: [system, module, version, landscape]
constraints: [what the AI must not do]
output_format: [template or schema]
examples: [included / attached]
---

## Artifact Definition
Produce a [artifact name] for [specific feature / process / system].
A usable artifact must include:
- [mandatory section 1]
- [mandatory section 2]
- [mandatory section 3]
It must not include:
- [prohibited content 1]
- [prohibited content 2]

## Audience
The reader is [role] who needs to [decision / action].
They understand [domain knowledge] but may not know [specific detail].
Use [terminology level] and avoid [ jargon / acronyms / generic language].

## System Context
- System: [name and version]
- Module: [SAP module / component]
- Landscape: [dev / test / prod / hybrid]
- Relevant configuration: [key settings, tables, transactions]
- Known limitations: [what the system cannot do]

## Constraints
- Do not invent [fields / tables / transactions / APIs].
- Do not assume [real-time data / specific permissions / external system availability].
- Do not use generic phrases such as [list phrases].
- If a requirement is unclear, flag it as unclear rather than guessing.
- If data is missing, state "data not available" rather than omitting the section.

## Output Format
Produce the output in this exact structure:
```
[Section 1]
- [Field 1]: [description]
- [Field 2]: [description]

[Section 2]
[table or list format]
```

## Examples
Here is an example of a strong [artifact] for this context:
```
[example]
```

## Source Material
Analyze the following material and use it as the basis for the output:
```
[source documents / data / transcripts]
```</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] The prompt defines the artifact and what makes it usable.</li>
      <li>[ ] The prompt identifies the audience and their level of domain knowledge.</li>
      <li>[ ] The prompt provides specific system context including versions, modules, and relevant configuration.</li>
      <li>[ ] The prompt includes at least three constraints that prevent common AI failure modes.</li>
      <li>[ ] The prompt specifies the output format with mandatory sections and field names.</li>
      <li>[ ] The prompt includes at least one example of strong output.</li>
      <li>[ ] The prompt has been tested and the output meets the quality checklist for the artifact type.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Writing a one-sentence prompt such as "write a test plan." <strong>Consequence:</strong> The AI produces a generic outline that requires hours of rewriting because it lacks context, constraints, and format.</li>
      <li><strong>Mistake:</strong> Providing source material without specifying the output format. <strong>Consequence:</strong> The AI produces a conversational summary instead of a structured artifact, and the reviewer must restructure everything manually.</li>
      <li><strong>Mistake:</strong> Forgetting to include constraints. <strong>Consequence:</strong> The AI invents field names, assumes real-time data, or skips negative paths because it was never told not to.</li>
      <li><strong>Mistake:</strong> Not saving tested prompts, so every team member writes their own prompt from scratch. <strong>Consequence:</strong> Output quality varies wildly, and the team spends more time reviewing and correcting than if they had written the artifact manually.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A consultant asks an AI to "write a status report for the SAP project" and receives a three-paragraph essay that says "the project is progressing well, the team is working hard, and there are some challenges that are being addressed." The output has no metrics, no dates, no owners, no blockers, and no next steps. The consultant cannot use it. The prompt was weak because it did not specify the artifact type, the audience, the system, the required sections, or the source material. The consultant spends two hours rewriting the report manually and decides that AI is not useful for this task.</p>
    <h3>Strong output — good AI usage</h3>
    <pre><code>## Prompt Briefing — SAP AMS Weekly Status Report

### Artifact Definition
Produce a weekly status report for a SAP AMS support engagement.
A usable report must include:
- Key metrics (tickets opened, resolved, reopened, avg resolution time)
- Workstream progress (incidents, changes, enhancements)
- Risks and blockers with severity and owner
- Next steps with owners and deadlines
It must not include:
- Generic progress statements without supporting data
- Opinions or subjective assessments
- Client names or internal incident IDs (privacy rule)

### Audience
The reader is the client delivery manager who needs to report to their steering committee.
They understand SAP support but do not know the internal tooling.
Use specific metrics and avoid acronyms unless defined.

### System Context
- System: SAP S/4HANA 2023
- Modules: SD, MM, MM-PUR, MDG
- Ticketing system: ServiceNow
- SLA: 4-hour response, 8-hour resolution for priority 2

### Constraints
- Do not invent ticket numbers or metrics.
- Do not assume all tickets are resolved within SLA.
- If a metric is unavailable, state "not available" rather than omitting it.
- Use Red / Yellow / Green only for workstreams with explicit criteria.

### Output Format
```
## Executive Summary
- Overall status: [R/Y/G] — [reason]

## Key Metrics
| Metric | This Week | Last Week | Trend |

## Risks and Blockers
| # | Item | Severity | Owner | Target |

## Next Steps
| # | Action | Owner | Deadline |
```

### Source Material
Analyze the attached ServiceNow export and the meeting notes from the weekly standup.</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a prompt engineering assistant for enterprise work artifacts.
Context: I need to write a prompt that produces a usable [artifact] for [system / process]. The current prompt is too generic and the output requires too much correction.
Tasks:
1. Review my current prompt and identify what is missing: artifact definition, audience, system context, constraints, output format, or examples.
2. Rewrite the prompt using the Prompt Briefing Template structure.
3. Add at least three constraints that prevent the most common AI failure modes for this artifact type.
4. Provide an example of strong output that the AI should emulate.
5. Test the rewritten prompt against a sample input and evaluate the output.
Constraints: Do not write a prompt that is shorter than 200 words. Do not omit the system context section. Do not use vague constraints like "be thorough." Use specific, verifiable constraints.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the artifact type, audience, and system context before writing the prompt.</li>
      <li>Include examples of strong output in every prompt to anchor the quality bar.</li>
      <li>Test the prompt with real source material and evaluate the output against the quality checklist.</li>
      <li>Save working prompts as reusable templates and share them with the team.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not write one-sentence prompts and expect usable output.</li>
      <li>Do not omit constraints because they seem obvious; AI does not share your assumptions.</li>
      <li>Do not skip the testing step; an untested prompt is not ready for production use.</li>
      <li>Do not keep prompts private; sharing them improves team consistency and reduces rework.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a> — reviewing the output to verify that the prompt produced what was intended.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/">Validate AI-Generated Requirements</a> — example of a skill that benefits from a strong prompt briefing.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-assisted-test-case-generation-working-skill/">AI-Assisted Test Case Generation</a> — applying prompt briefing to produce structured test cases.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-assisted-status-reporting-working-skill/">AI-Assisted Status Reporting</a> — applying prompt briefing to produce honest, structured status updates.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — structuring inputs so AI can produce reliable outputs.</li>
      <li><a href="/atlas/ai-operations/practical-ai-ml-for-sap-support/">Practical AI/ML for SAP Support</a> — operational context for AI-assisted work in SAP environments.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of prompt engineering for professional work artifacts. It is not official AI vendor documentation, SAP guidance, or a certified prompt engineering methodology. The effectiveness of a prompt depends on the AI model, the context window size, and the quality of the source material. Different models respond differently to the same prompt, and a prompt that works today may need adjustment as models change. The testing step is essential and cannot be skipped. Use this skill as a structured starting point, not as a guarantee of perfect AI output.</p>
  </section>
</article>
