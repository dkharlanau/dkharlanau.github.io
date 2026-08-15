---
layout: default
title: "AI Ready — Coding Agents Playbook"
description: "Practical rules, tools, patterns, and shortcuts for working effectively with Codex, Claude Code, and Kimi Code."
permalink: /labs/ai-ready/coding-agents/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, coding-agents, codex, claude-code, kimi-code, skills, agents, workflow]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Coding Agents</li></ol>
</nav>

# Coding Agents Playbook

Codex, Claude Code, and Kimi Code have different interfaces and configuration files, but the productive workflow is mostly the same.

The useful unit is not the prompt. It is the **working loop around the prompt**:

```text
understand
-> locate evidence
-> decide the smallest change
-> edit
-> run deterministic checks
-> inspect the diff
-> fix failures
-> stop with a clear result
```

A coding agent becomes useful when the repository gives it good boundaries, repeatable tools, and a way to prove that the change works.

## 1. Build one agent operating system

Do not maintain three unrelated sets of project rules unless the tools really need different behavior.

A practical repository shape is:

```text
AGENTS.md                         # shared project rules
CLAUDE.md                         # imports AGENTS.md + Claude-only notes
.agents/skills/                   # portable Agent Skills for Codex and Kimi
.claude/skills/                   # Claude-specific skill wrappers or extensions
.codex/agents/                    # Codex custom agents when needed
.claude/agents/                   # Claude Code custom subagents when needed
.kimi-code/agents/                # Kimi-specific custom agents when needed
```

Codex reads layered `AGENTS.md` files. Kimi Code also supports `AGENTS.md` and generic `~/.agents/AGENTS.md`. Claude Code reads `CLAUDE.md`, but a `CLAUDE.md` can import the repository `AGENTS.md`:

```markdown
@AGENTS.md

## Claude Code
- Use Plan mode before a cross-module refactor.
```

This keeps shared rules in one place and leaves only small tool-specific adapters.

## 2. What belongs in AGENTS.md

Keep always-on instructions short and operational.

Good content:

- build, test, lint, and format commands;
- repository boundaries and generated files;
- important architecture rules;
- naming and file-placement rules that are not obvious from code;
- how to validate a change;
- files or operations that need special care;
- the expected definition of done.

Weak content:

- a long tutorial about the whole system;
- copied framework documentation;
- every style rule already enforced by a formatter;
- temporary task details;
- vague instructions such as “write good code”.

A simple rule: if removing an instruction would not make the agent more likely to make a mistake, remove it.

## 3. Use this task contract

For a non-trivial change, give the agent a compact contract instead of a paragraph of wishes.

```text
Goal:
What should change for the user or system?

Scope:
Which module, feature, issue, or files are in scope?

Evidence:
Which issue, failing test, log, screenshot, or source defines the problem?

Constraints:
What architecture, compatibility, security, or style rules matter?

Do not:
What must remain untouched?

Verification:
Which tests, build, lint, type-check, screenshot, benchmark, or manual check must pass?

Done when:
What observable result proves completion?
```

This format works better than “fix this properly” because the agent can turn each field into an action or a check.

## 4. Three working modes

### Explore

Use read-only work when the repository is unfamiliar or the failure mode is unclear.

Ask for:

```text
Trace the request from entry point to persistence.
List the relevant files and explain why each matters.
Do not edit anything.
Return the smallest likely change surface and open questions.
```

Good uses for subagents are codebase exploration, log analysis, test-gap analysis, documentation lookup, and independent review.

### Implement

Once the failure or requirement is understood:

```text
Implement the smallest change that satisfies the goal.
Keep unrelated files untouched.
Follow existing patterns before creating new abstractions.
Run the narrowest useful checks first, then the required full checks.
Report changed files, verification, and remaining risk.
```

### Review

Use a fresh context or isolated reviewer when possible:

```text
Review the current diff against main.
Prioritize correctness, regression risk, security, data loss, and missing tests.
Ignore cosmetic preferences unless they create a real maintenance problem.
Return findings with file references and severity.
```

A separate review pass is useful because the agent that created a design already has reasons to like it. Machines have confirmation bias too; apparently we had to automate that part of humanity as well.

## 5. Context hacks that actually help

### Keep the main thread clean

Large search output, logs, and repeated test output reduce the useful signal in the main session. Delegate noisy read-heavy investigation to subagents and ask them to return short evidence summaries.

### Point to files instead of describing them

Use file references, repository search, or direct paths. Do not paste 2,000 lines into the prompt when the agent can read the file itself.

### Start a fresh session after the task changes

Do not keep a bug investigation, architecture debate, feature implementation, and final review in one endless conversation. Preserve durable project rules in files, then use a clean context for a new phase.

### Correct early

If the agent starts changing the wrong layer, interrupt it before it produces ten more files. A short correction early is cheaper than a heroic cleanup later.

### If the same correction happens twice, make it durable

Move repeated knowledge into one of these places:

```text
always needed -> AGENTS.md / CLAUDE.md
path-specific -> scoped rule
repeatable procedure -> Skill
must always execute -> hook / permission / rule / CI
```

## 6. Verification is part of the prompt

Never ask only for code. Ask for evidence.

Useful verification layers:

```text
formatter
-> lint
-> type check / compile
-> focused unit test
-> broader regression test
-> build
-> integration or UI check
-> diff review
```

Not every task needs every layer. The task should name the checks that matter.

A useful instruction is:

```text
Do not stop after editing. Run the checks that can prove the requested behavior.
If a check cannot run, report the exact blocker and do not claim success.
```

## 7. Prompt instructions are not security controls

Use the right mechanism for the right job:

| Need | Better mechanism |
|---|---|
| Explain project conventions | `AGENTS.md` / `CLAUDE.md` |
| Reuse a workflow | Skill |
| Limit commands or tools | permission / rule |
| Run a check every time | hook / CI |
| Keep risky writes human-controlled | approval boundary |
| Connect external systems | MCP or narrow CLI/API tool |
| Prove behavior | tests / build / deterministic checks |

Do not rely on “never run dangerous commands” inside a prompt when the runtime can enforce the boundary.

## 8. Codex field guide

Codex has a strong layered setup for repository instructions, reusable Skills, rules, MCP, and subagents.

### Use

- `AGENTS.md` for project rules. Nested files can narrow instructions for a directory.
- `.agents/skills/<name>/SKILL.md` for reusable workflows.
- `/skills` or `$skill-name` to invoke a Skill explicitly.
- subagents for independent read-heavy work; use `/agent` in the CLI to inspect agent threads.
- `.codex/agents/*.toml` for specialized project agents only when a stable role is repeated.
- `.rules` files for command policy outside the sandbox.
- `codex execpolicy check` to test command rules rather than trusting that a pattern probably matches.

### High-signal pattern

```text
1. Put repository facts and verification commands in AGENTS.md.
2. Ask an explorer to map the change surface if the task is unclear.
3. Keep parallel work read-heavy first.
4. Let one owner make the final write-heavy change.
5. Run tests and inspect the diff before finishing.
```

Parallel subagents cost more tokens, so use them when work is genuinely independent, not because four terminals look impressive.

Official references: [AGENTS.md](https://developers.openai.com/codex/agent-configuration/agents-md) · [Skills](https://developers.openai.com/codex/skills) · [Subagents](https://developers.openai.com/codex/subagents) · [Rules](https://developers.openai.com/codex/rules)

## 9. Claude Code field guide

Claude Code gives several layers with clear jobs: `CLAUDE.md`, path-scoped rules, Skills, subagents, hooks, permissions, MCP, and session controls.

### Use

- `CLAUDE.md` for the short set of facts needed in almost every session.
- `@AGENTS.md` inside `CLAUDE.md` when the repository already has shared agent instructions.
- `.claude/rules/` for language, directory, or file-specific rules.
- `.claude/skills/<name>/SKILL.md` for procedures and reference material that should load only when needed.
- `.claude/agents/` for repeated specialist roles.
- hooks for deterministic actions such as formatting, validation, or blocking an operation.
- `/context` to inspect context pressure.
- `/memory` to see loaded instructions and memory.
- `/agents`, `/hooks`, `/mcp`, and `/permissions` when debugging configuration.
- `/clear` when the session has moved to a different problem; `/compact` when you need to keep the task but reduce history.

### High-signal pattern

For a large feature:

```text
research
-> review plan
-> implement
-> verify
-> fresh-context review
```

For a tiny local fix, skip the ceremony. Planning a one-line null check for twenty minutes is still waste, even when an AI does it very eloquently.

Official references: [Best practices](https://code.claude.com/docs/en/best-practices) · [Memory and CLAUDE.md](https://code.claude.com/docs/en/memory) · [Extension map](https://code.claude.com/docs/en/features-overview) · [Hooks](https://code.claude.com/docs/en/hooks-guide)

## 10. Kimi Code field guide

Kimi Code supports a useful portable layer: `AGENTS.md`, generic `.agents/skills`, isolated subagents, hooks, MCP, Plan mode, and session controls.

### Use

- `/init` to create a first project `AGENTS.md`, then edit it down to the non-obvious rules.
- `.agents/skills/` for Skills that can also be reused by Codex.
- `explore` for read-only codebase investigation and `coder` for implementation-oriented delegated work.
- `kimi --plan` or `/plan` when you want exploration before edits.
- `/compact` when the current task should continue with less context.
- `kimi --continue` to resume the latest session for the working directory.
- `kimi -p "..."` for non-interactive one-shot work and automation.
- `/mcp-config` and `/update-config` for tool/configuration setup.
- `/import-from-cc-codex` when moving selected instructions, Skills, and MCP settings from Claude Code or Codex.
- `/swarm` only when the work can be divided cleanly.

### Important hook detail

Kimi hooks are fail-open if the hook itself fails or times out. Use them for useful interception and automation, but do not make a hook the only security barrier for a high-risk action.

### About YOLO and Auto modes

They remove approval friction and therefore remove part of the safety boundary. Use broad auto-approval only in a trusted, disposable, or strongly sandboxed working environment. For normal repository work, narrow permissions are usually a better trade.

Official references: [Getting started](https://www.kimi.com/code/docs/en/kimi-code-cli/guides/getting-started.html) · [Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html) · [Agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html) · [Hooks](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/hooks.html) · [Commands](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/slash-commands.html)

## 11. Portable setup matrix

| Capability | Codex | Claude Code | Kimi Code |
|---|---|---|---|
| Shared project instructions | `AGENTS.md` | `CLAUDE.md`, can import `AGENTS.md` | `AGENTS.md` |
| Reusable workflow | `.agents/skills/` | `.claude/skills/` | `.agents/skills/` or Kimi skill dirs |
| Path-specific instructions | nested `AGENTS.md` | `.claude/rules/` / nested `CLAUDE.md` | nested/project `AGENTS.md` |
| Isolated workers | subagents | subagents | subagents / swarm |
| External tools | MCP / CLI | MCP / CLI | MCP / CLI |
| Deterministic guard | rules / sandbox / approvals | permissions / hooks | permissions; hooks are fail-open |
| Plan-first mode | prompt / planning workflow | Plan mode | `--plan` / `/plan` |
| Session cleanup | new task/thread | `/clear`, `/compact` | `/new`, `/compact` |

The goal is portability of the **working method**, not identical configuration syntax.

## 12. Ten practical hacks

1. **Ask for the change surface before the change.** A five-file map can prevent a fifty-file refactor.
2. **Give the agent a failing example.** A reproducible failure is stronger context than a long explanation.
3. **Name the verification command in the task.** Agents are much better when “done” is executable.
4. **Use a fresh reviewer.** Do not ask only the implementing context whether its own design is excellent.
5. **Parallelize reading before writing.** Exploration merges well; concurrent edits often do not.
6. **Turn repeated prompts into Skills.** Repetition is configuration trying to become a file.
7. **Turn repeated corrections into rules.** If you say the same thing twice, the repository should remember it.
8. **Use CLIs and MCP instead of pasted data.** Let the agent retrieve the current fact at the moment it needs it.
9. **Checkpoint before a large change.** Git is still useful, despite decades of attempts to invent a more exciting way to regret a refactor.
10. **Stop when the evidence is weak.** “I cannot verify this because X is unavailable” is a better result than invented confidence.

## 13. Anti-patterns

### “Improve the whole repository”

No boundary, no measurable finish, huge context, difficult review.

### One giant instruction file

Always-on context is expensive and important rules become harder to notice. Move procedures to Skills and path-specific knowledge to scoped rules.

### Endless session

A long session can carry stale assumptions from one task into another. Start clean when the objective changes.

### Agent decides and approves its own risky write

Preparation and execution should be separate for high-impact operations.

### Multi-agent by default

More agents create more tokens, more coordination, and more possible conflicts. Start with one. Add workers when tasks are independent or context isolation has clear value.

### Passing tests means perfect code

Tests prove only what they cover. Review the diff, edge cases, migrations, permissions, data handling, and rollback risk too.

## 14. A reusable repository rule

This small block is a useful starting point for `AGENTS.md`:

```markdown
## Working contract

- Read the relevant code before editing.
- Make the smallest change that solves the stated problem.
- Keep unrelated files untouched.
- Prefer existing project patterns over new abstractions.
- Never edit generated files manually; use the generator.
- Run the narrowest relevant checks after a change, then required project checks.
- Review `git diff` before reporting completion.
- If verification cannot run, state the blocker and do not claim success.
- Ask before adding production dependencies or performing destructive external actions.
- Use subagents mainly for independent read-heavy work; keep final write ownership clear.
```

Tune it to the repository. Rules that are not true for the project are worse than having no rule.

## Machine-readable map

[`coding-agents.json`](/labs/ai-ready/data/coding-agents.json) keeps the portable rules, tool profiles, task modes, anti-patterns, and source registry in a reusable form.

Reviewed against official product documentation on **15 Aug 2026**. These tools change quickly, so commands and configuration details should be checked against their current docs before making them organizational policy.

Related: [Engineering Handbook](/labs/ai-ready/engineering/) · [Practical Use Cases](/labs/ai-ready/use-cases/#coding) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Tools and MCP](/labs/ai-ready/tools-mcp/)
