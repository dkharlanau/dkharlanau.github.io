---
layout: default
title: "Repository Context Packing with Repomix"
description: "Package selected repo context with Repomix, analyze architecture, discover weak spots, and generate a safe implementation plan."
permalink: /skill-hub/ai-assisted-development/repository-context-packing-with-repomix/
last_modified_at: 2026-06-13
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-development/">AI-Assisted Development</a></li>
    <li aria-current="page">Repository Context Packing with Repomix</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Development</p>
  <h1>Repository context packing with Repomix</h1>
  <p class="lead">Package selected repo context, analyze architecture, discover weak spots, and generate a safe implementation plan.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill turns a repository into a focused, safe, AI-readable context bundle. The output is a temporary pack file and a structured prompt that an AI model can use to audit architecture, scope work, or plan changes without guessing or accessing private material.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You need an architecture audit or dependency review before planning work.</li>
      <li>You want to brief a coding agent with reproducible, scoped context.</li>
      <li>You are onboarding a new team member or agent to a codebase.</li>
      <li>You want to measure how much of the repo fits into a model's context window.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Audit a Jekyll site before adding a new section</h3>
    <p>You need to add a new Atlas section to a Jekyll site. You pack <code>atlas/</code>, <code>_includes/</code>, <code>_layouts/</code>, <code>_data/</code>, <code>scripts/</code>, and <code>tests/</code> with Repomix, excluding <code>_site/</code> and images. The model identifies the frontmatter conventions, the generator scripts, and the test files that will need updating. You avoid breaking the manifest count tests because the pack made the test structure visible.</p>
    <h3>Scope a refactor in a Python project</h3>
    <p>You want to refactor a module with many imports. You pack only the relevant package and its tests. The model maps call sites and proposes a migration plan file by file, rather than editing blindly.</p>
    <h3>Prepare a handover brief</h3>
    <p>A consultant is leaving a project. You pack the source, configuration, and README files into a Markdown bundle. The model produces a structured handover summary that the team can verify against the actual repo.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Goal statement</strong> — what question the pack must answer.</li>
      <li><strong>Repository path</strong> — root of the project to pack.</li>
      <li><strong>Include patterns</strong> — globs for files relevant to the goal.</li>
      <li><strong>Ignore patterns</strong> — globs for secrets, generated artifacts, images, and private notes.</li>
      <li><strong>Output format</strong> — XML, Markdown, or compressed Markdown.</li>
      <li><strong>Target model context window</strong> — so you know whether to split or compress.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What specific question must the AI answer from this pack?</li>
      <li>Which files are essential, which are helpful, and which are noise?</li>
      <li>Does the repo contain secrets, credentials, or private notes that must be excluded?</li>
      <li>Is the token count within the target model's context window?</li>
      <li>Can another team member reproduce this exact pack?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>State the goal.</strong> Write one sentence describing what the AI should do with the pack.</li>
      <li><strong>Create a temporary directory.</strong> Use <code>.tmp/repomix/</code> or <code>/tmp/repomix/</code>; never commit packs.</li>
      <li><strong>Draft include patterns.</strong> Start with the directories and file types relevant to the goal.</li>
      <li><strong>Draft ignore patterns.</strong> Exclude <code>.git/</code>, <code>node_modules/</code>, <code>_site/</code>, <code>dist/</code>, <code>.env</code>, secrets, images, and private working directories.</li>
      <li><strong>Run Repomix.</strong> Use <code>npx repomix@latest</code> with explicit flags.</li>
      <li><strong>Review token count.</strong> If too high, split by concern or use compressed Markdown.</li>
      <li><strong>Inspect the pack.</strong> Search for accidental inclusions such as secrets, private paths, or large generated files.</li>
      <li><strong>Write the prompt.</strong> Tell the AI the goal, scope, evidence requirements, and stop conditions.</li>
      <li><strong>Run the analysis.</strong> Feed the pack and prompt to the model.</li>
      <li><strong>Validate findings.</strong> Check citations against the actual repository before acting.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the full repo exceeds the context window, split the pack by subsystem or layer.</li>
      <li>If the pack contains any secret or credential, delete it and fix the ignore patterns.</li>
      <li>If the goal is a single-file change, do not pack the whole repo.</li>
      <li>If the output will be shared, prefer XML for clear file boundaries.</li>
      <li>If token budget is tight, prefer compressed Markdown and add line numbers.</li>
      <li>If the model cannot answer from the pack, say so rather than invent a narrower pack.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Repomix command</strong> — saved in the task notes so the pack is reproducible.</li>
      <li><strong>Pack file</strong> — temporary XML or Markdown bundle in <code>.tmp/repomix/</code>.</li>
      <li><strong>Analysis prompt</strong> — structured request sent to the AI.</li>
      <li><strong>Findings report</strong> — AI output with citations, reviewed by a human.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Focused audit command</h3>
    <pre><code>mkdir -p .tmp/repomix

npx repomix@latest \
  -o .tmp/repomix/audit.xml \
  --style xml \
  --include "src/**/*.py,tests/**/*.py,README.md,pyproject.toml" \
  --ignore "**/__pycache__/**,**/.git/**,**/node_modules/**,**/*.png,**/*.jpg,.env,.env.*"
</code></pre>

    <h3>Repository audit prompt</h3>
    <pre><code>Goal: Audit the architecture of the repository in the attached pack.

Scope:
- Focus on src/ and tests/ only.
- Ignore generated artifacts, configuration secrets, and build outputs.

Tasks:
1. Summarize the overall structure and main modules.
2. Identify the three highest-risk areas for a refactor and explain why.
3. List any missing tests, documentation, or guardrails.

Rules:
- Cite specific files and line numbers for every finding.
- Do not propose changes that delete data or modify CI/CD without explicit confirmation.
- If you cannot determine something from the pack, say "unknown" rather than invent it.
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The goal is stated in one sentence.</li>
      <li>Include and ignore patterns are documented and reproducible.</li>
      <li>The pack contains no secrets, credentials, or private paths.</li>
      <li>The token count fits the target model's context window.</li>
      <li>The prompt asks for citations and defines stop conditions.</li>
      <li>AI findings are validated against the actual repository before action.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Packing everything.</strong> Consequence: token budget is wasted on irrelevant files.</li>
      <li><strong>Ignoring secrets too late.</strong> Consequence: credentials or private paths leak into the pack.</li>
      <li><strong>Committing packs.</strong> Consequence: repository bloat and potential exposure of context bundles.</li>
      <li><strong>Trusting AI architecture findings blindly.</strong> Consequence: changes based on hallucinated file relationships.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, gather the goal, repository path, and target model first. Separate facts from assumptions: the pack contents are facts; the AI's interpretation is an assumption until verified. Produce the four deliverables listed above. Avoid generic language such as "analyze the codebase"; instead, use concrete goals like "identify the three highest-risk coupling points." If information is missing, ask for it rather than guess.</p>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-development/ai-coding-agent-task-design/">AI Coding Agent Task Design</a></li>
      <li><a href="/skill-hub/ai-assisted-development/ai-generated-code-review/">AI-Generated Code Review</a></li>
      <li><a href="/skill-hub/ai-assisted-development/ai-tool-selection-for-development/">AI Tool Selection for Development</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-tools/repository-context-packaging/">Repository Context Packaging</a></li>
      <li><a href="/atlas/ai-tools/repomix-for-ai-codebase-analysis/">Repomix for AI Codebase Analysis</a></li>
      <li><a href="/atlas/ai-tools/ai-coding-agents-landscape/">AI Coding Agents Landscape</a></li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of Repomix and context-engineering practice. Repomix version and behavior may change; verify commands against the current official documentation. This skill does not replace code review or security scanning.</p>
  </section>

</article>
