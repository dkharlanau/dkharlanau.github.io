---
layout: default
title: "AI Coding Agent Task Design"
description: "Turn vague work into narrow, testable coding-agent tasks with one objective, relevant files, constraints, validation commands, done criteria, and stop conditions."
permalink: /skill-hub/ai-assisted-development/ai-coding-agent-task-design/
last_modified_at: 2026-06-13
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-development/">AI-Assisted Development</a></li>
    <li aria-current="page">AI Coding Agent Task Design</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Development</p>
  <h1>AI coding agent task design</h1>
  <p class="lead">Turn vague work into narrow, testable coding-agent tasks with one objective, relevant files, constraints, validation commands, done criteria, and stop conditions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill prevents agents from drifting. It produces a task brief that an agent can execute, a human can review, and a test suite can validate. The output is a coding-agent task card with objective, scope, constraints, validation, and reporting requirements.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are delegating implementation work to Claude Code, Codex CLI, Cursor, Copilot, Aider, or a similar agent.</li>
      <li>A stakeholder asks for a feature but the request is broad or ambiguous.</li>
      <li>You want to compare agent output against explicit acceptance criteria.</li>
      <li>You need to review agent work efficiently without reconstructing intent.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Add a new Atlas page</h3>
    <p>Instead of "add an AI tools page," the task becomes: "Create <code>atlas/ai-tools/repository-context-packaging.md</code> with frontmatter matching existing diagnostics pages, include sections X, Y, Z, and run <code>python scripts/generate_atlas_artifacts.py --check</code> without errors. Do not modify the homepage."</p>
    <h3>Fix a failing test</h3>
    <p>The task is: "Make <code>test_dynamic_discovery_returns_22_article_pages</code> pass after adding three new Atlas articles. Update only the count assertions in <code>tests/test_atlas_artifacts.py</code>. Run the test and confirm green."</p>
    <h3>Refactor a utility module</h3>
    <p>The task is: "Extract the URL validation logic from <code>src/links.py</code> into <code>src/link_validation.py</code>. Update all imports in <code>src/</code>. Run the test suite. Do not change public API behavior."</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>One-sentence objective</strong> — the single outcome the agent must produce.</li>
      <li><strong>Relevant files</strong> — what the agent should read and what it may edit.</li>
      <li><strong>Constraints</strong> — what must not change, break, or be touched.</li>
      <li><strong>Validation commands</strong> — how to prove the change works.</li>
      <li><strong>Done criteria</strong> — conditions that must be true for the task to be considered complete.</li>
      <li><strong>Stop conditions</strong> — when the agent must pause and ask for direction.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Can the objective be verified with a test, diff, or command?</li>
      <li>Which files must the agent edit, and which must it leave alone?</li>
      <li>What would prove the change is correct?</li>
      <li>What could go wrong, and what should trigger a stop?</li>
      <li>How should the agent report what it did?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>State the objective.</strong> One sentence. One outcome.</li>
      <li><strong>List relevant files.</strong> Use explicit paths and mark each as read-only or editable.</li>
      <li><strong>Define constraints.</strong> Include homepage, legal pages, verified pages, generated files, and private paths that must not be touched.</li>
      <li><strong>Specify validation commands.</strong> Examples: <code>pytest tests/test_atlas_artifacts.py</code>, <code>bundle exec jekyll build</code>, <code>python scripts/check_links.py _site</code>.</li>
      <li><strong>Write done criteria.</strong> Bulleted list of verifiable yes/no conditions.</li>
      <li><strong>Write stop conditions.</strong> When the agent must pause: failing validation, ambiguous requirement, need for human approval.</li>
      <li><strong>Define report format.</strong> Require a summary of changes, test results, and any assumptions.</li>
      <li><strong>Run and review.</strong> Execute the task, inspect the diff, and run validation yourself.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the objective has more than one outcome, split it into separate tasks.</li>
      <li>If the agent needs to touch a protected file, stop and get human approval.</li>
      <li>If validation fails, the agent must fix it or stop, not proceed.</li>
      <li>If the agent introduces a new dependency, it must be justified and reviewed.</li>
      <li>If the task changes public behavior, it needs a human sign-off before merge.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Coding-agent task card</strong> — the brief given to the agent.</li>
      <li><strong>Diff or patch</strong> — the changes produced by the agent.</li>
      <li><strong>Validation report</strong> — command outputs proving the change works.</li>
      <li><strong>Assumption log</strong> — anything the agent had to assume because the brief was incomplete.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Task card</h3>
    <pre><code>Objective: [one-sentence outcome]

Relevant files:
- READ/EDIT: [path]
- READ-ONLY: [path]
- DO NOT TOUCH: [path]

Constraints:
- [Constraint 1]
- [Constraint 2]

Validation commands:
- [command 1]
- [command 2]

Done criteria:
- [ ] [verifiable condition 1]
- [ ] [verifiable condition 2]

Stop conditions:
- [validation command] fails and cannot be fixed in one iteration.
- The requirement becomes ambiguous.
- Any change to a DO NOT TOUCH file is required.

Report format:
1. Summary of changes (one paragraph).
2. List of files edited.
3. Validation command outputs.
4. Any assumptions or unresolved issues.
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The objective is one sentence and one outcome.</li>
      <li>Every relevant file is labeled read-only or editable.</li>
      <li>Protected files are explicitly listed as do-not-touch.</li>
      <li>Validation commands can be run by a human to verify the result.</li>
      <li>Done criteria are yes/no verifiable.</li>
      <li>Stop conditions prevent silent drift.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Vague objective.</strong> Consequence: the agent produces plausible but wrong work.</li>
      <li><strong>No constraints.</strong> Consequence: the agent modifies files that should stay untouched.</li>
      <li><strong>Missing validation.</strong> Consequence: the change looks correct but breaks tests or links.</li>
      <li><strong>No stop conditions.</strong> Consequence: the agent iterates past the point of diminishing returns.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, first gather the objective, relevant files, constraints, validation commands, done criteria, and stop conditions. Do not start coding until the task card is complete. Separate facts from assumptions: existing file contents are facts; guesses about intent are assumptions. Produce the four deliverables. If a stop condition is reached, pause and report rather than continuing. Avoid generic summaries; cite specific files and command outputs.</p>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-development/repository-context-packing-with-repomix/">Repository Context Packing with Repomix</a></li>
      <li><a href="/skill-hub/ai-assisted-development/ai-generated-code-review/">AI-Generated Code Review</a></li>
      <li><a href="/skill-hub/ai-assisted-development/ai-tool-selection-for-development/">AI Tool Selection for Development</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-tools/ai-coding-agents-landscape/">AI Coding Agents Landscape</a></li>
      <li><a href="/atlas/ai-tools/repository-context-packaging/">Repository Context Packaging</a></li>
      <li><a href="/atlas/automation/agent-assisted-development-workflows/">Agent-Assisted Development Workflows</a></li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of task-decomposition practice. It is not official vendor documentation. Adapt the template to your team's conventions and tools.</p>
  </section>

</article>
