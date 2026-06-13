---
layout: default
title: "AI-Generated Code Review"
description: "Review AI-authored changes before merge: diff inspection, tests, security checks, public/private boundaries, architecture drift, and final merge checklist."
permalink: /skill-hub/ai-assisted-development/ai-generated-code-review/
last_modified_at: 2026-06-13
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-development/">AI-Assisted Development</a></li>
    <li aria-current="page">AI-Generated Code Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Development</p>
  <h1>AI-generated code review</h1>
  <p class="lead">Review AI-authored changes before merge: diff inspection, tests, security checks, public/private boundaries, architecture drift, and final merge checklist.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill provides a structured review workflow for code produced or edited by AI agents. The output is a reviewed diff with explicit human decisions on each risk category, plus a final merge checklist.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are reviewing a PR that an agent authored or heavily edited.</li>
      <li>You want to catch hallucinations, architecture drift, and privacy leaks before merge.</li>
      <li>You need a repeatable review process for AI-generated contributions.</li>
      <li>You maintain a public repository and must ensure no private material is exposed.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Agent adds new Atlas pages</h3>
    <p>An agent created several new Atlas pages. The reviewer checks that all pages have <code>status: needs_verification</code>, <code>verified: false</code>, <code>robots: noindex,follow</code>, and <code>sitemap: false</code>. The reviewer confirms that generated artifacts were regenerated and that no private paths appear in the diff.</p>
    <h3>Agent refactors a script</h3>
    <p>An agent refactored a Python generator. The reviewer verifies that the script still produces identical output, that tests pass, and that no new dependencies were added without justification.</p>
    <h3>Agent updates site navigation</h3>
    <p>An agent updated the Skill Hub index to include a new skill group. The reviewer checks that all links are valid, that the homepage was not modified, and that the change does not break Jekyll build.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Pull request or diff</strong> — the AI-authored changes.</li>
      <li><strong>Original task brief</strong> — what the agent was asked to do.</li>
      <li><strong>Validation commands</strong> — tests, builds, link checks, and linters.</li>
      <li><strong>Protected files list</strong> — homepage, legal pages, verified pages, generated files.</li>
      <li><strong>Project conventions</strong> — frontmatter patterns, naming rules, SEO rules.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Does the diff match the original task brief?</li>
      <li>Are there changes to files that should not have been touched?</li>
      <li>Do tests, builds, and link checks pass?</li>
      <li>Are there new secrets, private paths, or unverified content?</li>
      <li>Does the change preserve architecture and conventions?</li>
      <li>Would a human reviewer understand why each change was made?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the task brief.</strong> Know what the agent was supposed to do.</li>
      <li><strong>Inspect the diff file by file.</strong> Do not rely on summary comments alone.</li>
      <li><strong>Run validation commands.</strong> Tests, builds, link checks, SEO checks, and public-repo hygiene checks.</li>
      <li><strong>Check for secrets and private paths.</strong> Search for tokens, env files, local paths, and private notes.</li>
      <li><strong>Check public/private boundaries.</strong> Ensure no private corpus, client data, or internal IDs are exposed.</li>
      <li><strong>Check architecture drift.</strong> Confirm the change follows existing patterns and does not introduce inconsistency.</li>
      <li><strong>Check SEO and site quality.</strong> For site content, verify frontmatter, links, robots, and sitemap settings.</li>
      <li><strong>Check generated artifacts.</strong> If the repo has generators, confirm they were run and outputs are consistent.</li>
      <li><strong>Record findings.</strong> Mark each item as pass, fail, or needs discussion.</li>
      <li><strong>Decide on merge.</strong> Approve only when all blockers are resolved.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a protected file was modified without approval, reject.</li>
      <li>If validation fails, reject until fixed.</li>
      <li>If secrets or private paths are found, reject and rotate credentials if needed.</li>
      <li>If architecture drift is introduced, request a redesign or split the PR.</li>
      <li>If generated artifacts are inconsistent, request regeneration.</li>
      <li>If the change is large, request smaller sequential PRs.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Review report</strong> — pass/fail/needs-discussion for each category.</li>
      <li><strong>Corrected diff</strong> — the approved version of the changes.</li>
      <li><strong>Validation log</strong> — command outputs proving checks pass.</li>
      <li><strong>Merge checklist</strong> — signed-off yes/no items.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Review report</h3>
    <pre><code>PR: [URL or branch]
Agent task: [brief]

Diff inspection:
- [ ] Files changed match the task scope.
- [ ] No protected files were modified.
- [ ] No secrets, tokens, or env files added.
- [ ] No private paths or client data exposed.

Validation:
- [ ] Tests pass: [command + output]
- [ ] Build passes: [command + output]
- [ ] Link check passes: [command + output]
- [ ] SEO/public-repo checks pass: [command + output]

Quality:
- [ ] Architecture and conventions preserved.
- [ ] Generated artifacts consistent.
- [ ] Frontmatter/SEO settings correct.

Decision: [Approve / Request changes / Reject]
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every changed file was inspected, not just summarized.</li>
      <li>Validation commands were run and passed.</li>
      <li>No secrets, private paths, or unverified public content are present.</li>
      <li>Protected files remain unchanged unless explicitly approved.</li>
      <li>Generated artifacts are consistent with source changes.</li>
      <li>The merge checklist is complete and signed off.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Trusting the agent summary.</strong> Consequence: missed changes to protected files.</li>
      <li><strong>Skipping validation.</strong> Consequence: broken tests or links reach main.</li>
      <li><strong>Ignoring architecture drift.</strong> Consequence: inconsistent patterns accumulate.</li>
      <li><strong>Approving because "it looks fine."</strong> Consequence: public repo hygiene failures or security leaks.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, start by reading the task brief and the full diff. Separate facts from assumptions: the diff contents are facts; the agent's intent is an assumption. Run all validation commands and capture outputs. Produce the four deliverables. Do not approve a PR because the agent claims it works; approve because the evidence shows it works. If any blocker is found, report it explicitly.</p>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-development/ai-coding-agent-task-design/">AI Coding Agent Task Design</a></li>
      <li><a href="/skill-hub/ai-assisted-development/repository-context-packing-with-repomix/">Repository Context Packing with Repomix</a></li>
      <li><a href="/skill-hub/ai-assisted-development/mcp-development-workflow/">MCP Development Workflow</a></li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-tools/ai-code-review-agents/">AI Code Review Agents</a></li>
      <li><a href="/atlas/ai-tools/ai-security-for-generated-code/">AI Security for Generated Code</a></li>
      <li><a href="/atlas/ai-tools/ai-assisted-testing-and-quality/">AI-Assisted Testing and Quality</a></li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of code-review practice. It is not official vendor documentation. The exact validation commands depend on the project's tech stack and must be adapted locally.</p>
  </section>

</article>
