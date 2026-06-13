# AI Tools and Development Workflow Cluster — Research Report

**Date:** 2026-06-13  
**Purpose:** Source-backed landscape scan for the new Atlas `ai-tools` cluster and Skill Hub `ai-assisted-development` cluster.  
**Method:** Public web search of official documentation, GitHub repositories, release notes, and vendor pages; local inspection with Repomix 1.14.1.

## Research scope

1. Repository context packaging / context engineering  
2. Terminal coding agents  
3. IDE and editor agents  
4. Autonomous / semi-autonomous engineering agents  
5. MCP and tool integration  
6. AI code review and PR quality  
7. AI testing, QA, and security  
8. AI development workflow patterns

## Key sources used

- Repomix: https://github.com/yamadashy/repomix and local `npx repomix@latest` run
- OpenAI Codex CLI: https://github.com/openai/codex and OpenAI Codex documentation
- Claude Code: https://claude.com/code and Anthropic documentation
- Aider: https://github.com/Aider-AI/aider and https://aider.chat/docs/
- Cursor: https://cursor.com and Cursor documentation
- Windsurf: https://windsurf.com and Codeium documentation
- GitHub Copilot / Copilot coding agent / Copilot code review: https://github.com/features/copilot and GitHub Docs
- Model Context Protocol: https://modelcontextprotocol.io/specification and Anthropic engineering blog
- CodeRabbit: https://coderabbit.ai and docs.coderabbit.ai
- GitHub Advanced Security / CodeQL / Copilot Autofix: https://github.com/features/security
- llms.txt proposal: https://llmstxt.org/ and public adoption reporting
- Public third-party analysis (used only for corroboration, not as primary source): StackLighthouse, Shareuhack, Justin McKelvey, MorphLLM, Limy, BuiltABot, etc.

## Research matrix

| Tool/topic | Category | Official source | Status 2026-06-13 | License/commercial | Interface | Core use case | Strengths | Limitations | Privacy/security risks | Best-fit workflow | Atlas | Skill Hub | Proposed page | Confidence | Defer reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Repomix | Context packaging | github.com/yamadashy/repomix | Active; v1.14.1 released | Open source (MIT) | CLI, npx, web | Pack repository source into XML/Markdown for AI context | Fast, configurable include/ignore, security check, token metrics, XML/markdown/compressed styles | Static snapshot only; does not reason; large repos still exceed model context | Packs entire source; must exclude secrets, env files, private notes | Pre-task repo audit; focused context packs for code review or planning | Yes | Yes | `atlas/ai-tools/repomix-for-ai-codebase-analysis.md`, `skill-hub/ai-assisted-development/repository-context-packing-with-repomix.md` | High | — |
| gitingest / repository-to-text tools | Context packaging | github.com/cyclotruc/gitingest | Active | Open source | Web, CLI | Convert GitHub repo to LLM-friendly text | No install, public-repo friendly, token count | Public repos only; less configurable than Repomix | Sends repo to a web service; do not use for private code | Quick public repo overview | Yes (brief) | No | `atlas/ai-tools/repository-context-packaging.md` | Medium | Mentioned as alternative, not a dedicated page |
| llms.txt / llms-full.txt | Context packaging | llmstxt.org | Proposed standard; adoption growing in dev-tool/docs sector | Open convention | Static file | Curated machine-readable content map for AI agents | Clean markdown, token-efficient, agent-routing friendly | Not yet widely read by major search crawlers; voluntary signal | Exposes selected public content only; keep private paths out | AI-ready documentation bundle for public sites | Yes | Yes | `atlas/ai-tools/repository-context-packaging.md`, `skill-hub/ai-assisted-development/repository-context-packing-with-repomix.md` | High | — |
| Codex CLI | Terminal coding agent | github.com/openai/codex | Active; rapid 2025–2026 growth | Open source CLI (Apache 2.0); cloud tasks require OpenAI account | Terminal CLI, IDE extension, cloud agent | Autonomous coding tasks, issue-to-PR, review | Sandboxed execution, multi-agent roles, MCP-native, bundled with ChatGPT Plus/Pro | OpenAI ecosystem only; cloud tasks leave local machine | Cloud sandbox copies repo to OpenAI-managed environment; review data policies | Background tasks, large refactors, OpenAI-centric teams | Yes | Yes | `atlas/ai-tools/ai-coding-agents-landscape.md`, `skill-hub/ai-assisted-development/ai-tool-selection-for-development.md` | High | — |
| Claude Code | Terminal coding agent | claude.com/code | Generally available | Proprietary CLI; requires Anthropic account | Terminal CLI, IDE extensions | Multi-file edits, refactoring, test runs, long-running tasks | Strong reasoning, 1M context window, native MCP, CLAUDE.md project memory | Usage-based cost can spike; no free tier; terminal-first | Full local filesystem/shell access by default; use permission boundaries | Complex refactoring, architectural work, headless/CI runs | Yes | Yes | `atlas/ai-tools/ai-coding-agents-landscape.md`, `skill-hub/ai-assisted-development/ai-tool-selection-for-development.md` | High | — |
| Aider | Terminal coding agent | github.com/Aider-AI/aider | Active; 41k+ stars | Open source (Apache 2.0), BYO LLM | Terminal CLI | Model-agnostic pair programming in git repo | Multi-provider, repo map, git-native commits, architect mode, no PTY needed | No sandbox; operates directly on filesystem | API keys go to chosen provider; Aider itself does not host models | Targeted edits, multi-provider teams, programmatic delegation | Yes | Yes | `atlas/ai-tools/ai-coding-agents-landscape.md`, `skill-hub/ai-assisted-development/ai-tool-selection-for-development.md` | High | — |
| Cursor | IDE agent | cursor.com | Active; Cursor 3 launched April 2026 | Proprietary IDE | Standalone IDE (VS Code fork) | AI-native editing, Composer, parallel agents, tab completion | Deep editor integration, visual diffs, agents window | Cursor-only editor; credit-based billing can overage | Code sent to chosen model; Privacy mode on Business | Daily editor work, UI/front-end, visual diff review | Yes | Yes | `atlas/ai-tools/ai-coding-agents-landscape.md`, `skill-hub/ai-assisted-development/ai-tool-selection-for-development.md` | High | — |
| Windsurf | IDE agent | windsurf.com / codeium.com | Active; OpenAI acquired Codeium (Windsurf) May 2026 | Proprietary IDE | Standalone IDE (VS Code fork) | Agentic coding with Cascade flow | Strong agentic UX, lower starting price | Acquisition creates strategic uncertainty; smaller ecosystem than Cursor | Similar to Cursor | Budget-conscious IDE agent users | Yes (brief) | No | `atlas/ai-tools/ai-coding-agents-landscape.md` | Medium | Mentioned as alternative only |
| GitHub Copilot (agent mode / coding agent) | IDE agent + cloud agent | github.com/features/copilot | Agent mode GA March 2026; coding agent async issue-to-PR | Commercial subscription | IDE extension, GitHub.com, CLI | Inline completions, agent mode, issue-to-PR coding agent | Native GitHub integration, broad IDE support, enterprise controls | Agent mode less autonomous than Claude Code/Codex; review quality varies | Microsoft/GitHub data policies; configure exclusions | Teams already in GitHub/Microsoft ecosystem | Yes | Yes | `atlas/ai-tools/ai-coding-agents-landscape.md`, `skill-hub/ai-assisted-development/ai-tool-selection-for-development.md` | High | — |
| Devin | Autonomous engineering agent | cognition.ai | Commercial | Proprietary SaaS | Web | Fully autonomous software engineering tasks | High autonomy on scoped tasks | Expensive, waitlist/enterprise, opaque | Full repo and environment access; high trust requirement | Well-specified isolated tasks with human review | Yes (brief) | No | `atlas/ai-tools/ai-coding-agents-landscape.md` | Medium | Mentioned as example, not dedicated page |
| OpenHands | Autonomous engineering agent | github.com/All-Hands-AI/OpenHands | Active open source | Open source (MIT) | Docker-based | Sandboxed autonomous coding | Isolation, multi-model, open | Heavier setup than CLI agents | Self-hosted reduces vendor risk; configure secrets carefully | Research/experimentation, isolated agent tasks | Yes (brief) | No | `atlas/ai-tools/ai-coding-agents-landscape.md` | Medium | Mentioned as example |
| SWE-agent | Autonomous engineering agent | github.com/princeton-nlp/SWE-agent | Active open source | Open source | CLI / Docker | Academic/research agent for GitHub issues | Strong benchmark results, transparent | Not a commercial product; requires setup | Local/Docker execution | Benchmarking, research, advanced users | Yes (brief) | No | `atlas/ai-tools/ai-coding-agents-landscape.md` | Medium | Mentioned as example |
| Model Context Protocol (MCP) | MCP / tool integration | modelcontextprotocol.io | Open standard; donated to Linux Foundation Dec 2025; v2025-06-18 spec active | Open specification | stdio, SSE, HTTP | Universal tool interface for AI agents | Vendor-neutral, reusable servers, growing ecosystem | Auth spec still evolving; tool-poisoning/prompt-injection risks documented | Servers can expose filesystem, GitHub, browser; enforce least privilege | Adding tools to Claude Code, Cursor, Codex, custom agents | Yes | Yes | `atlas/ai-tools/mcp-for-development-workflows.md`, `skill-hub/ai-assisted-development/mcp-development-workflow.md` | High | — |
| CodeRabbit | AI code review | coderabbit.ai | Active; 2M+ repos reported | Commercial; free for OSS | GitHub/GitLab/Azure DevOps/Bitbucket app | Automated PR review | Line-by-line comments, 40+ linters, multi-platform, learns from feedback | Can be noisy; stores code 7 days; no BYOK | Third-party reads full PR diff; configure private-repo policy carefully | First-pass review before human reviewer | Yes | Yes | `atlas/ai-tools/ai-code-review-agents.md`, `skill-hub/ai-assisted-development/ai-generated-code-review.md` | High | — |
| GitHub Copilot code review / Copilot Autofix | AI code review + security | github.com/features/security | Agentic code review March 2026; Autofix GA | Commercial (GitHub Advanced Security / Copilot) | GitHub.com, IDE, Azure DevOps preview | PR review and automated security fixes | Zero setup for GitHub users, CodeQL integration, native workflow | GitHub-only; diff-based; limited cross-file reasoning | GitHub-hosted; configure enterprise data controls | Security-first review in GitHub-centric teams | Yes | Yes | `atlas/ai-tools/ai-code-review-agents.md`, `atlas/ai-tools/ai-security-for-generated-code.md` | High | — |
| Qodo / CodiumAI | AI code review / test generation | qodo.ai | Active | Commercial | IDE extension, GitHub app | AI review, test generation | Multi-agent review, strong benchmark claims | Smaller ecosystem than CodeRabbit/Copilot | Third-party code access | Test-driven teams wanting AI review | Yes (brief) | No | `atlas/ai-tools/ai-code-review-agents.md` | Medium | Mentioned as alternative |
| CodeQL / SAST + AI | AI security | github.com/github/codeql | Active | Open source engine; commercial GitHub Advanced Security integration | CLI, GitHub Actions | Static analysis for security vulnerabilities | Mature, deterministic, integrated with Copilot Autofix | Rule-based; needs configuration; not a reasoning agent | Scan results may include paths/names; keep in private CI | Security gate in CI before merge | Yes | Yes | `atlas/ai-tools/ai-security-for-generated-code.md`, `skill-hub/ai-assisted-development/ai-generated-code-review.md` | High | — |
| AI test generation / regression validation | AI testing/QA | Various (Copilot, Cursor, Claude Code, Aider, Qodo) | Active across tools | Mixed | IDE/CLI | Generate and validate tests | Speeds up coverage, catches surface bugs | Hallucinates tests, misses edge cases, wrong assumptions | Generated tests may expose business logic; review before commit | Human-validated AI test drafts | Yes | Yes | `atlas/ai-tools/ai-assisted-testing-and-quality.md`, `skill-hub/ai-assisted-development/ai-generated-code-review.md` | High | — |
| Repository context audit with Repomix | Workflow pattern | Local execution | Proven in this repository | Open source | CLI | Package repo context for architecture review | Reproducible, version-agnostic, safe if ignores are correct | Still requires human interpretation | Exclude secrets, private notes, generated artifacts | First step before assigning work to a coding agent | Yes | Yes | `atlas/ai-tools/repository-analysis-workflow-with-repomix.md`, `skill-hub/ai-assisted-development/repository-context-packing-with-repomix.md` | High | — |
| Coding-agent task design | Workflow pattern | Derived from multiple vendors + project conventions | Best practice | N/A | Any agent | Narrow, testable tasks for agents | Reduces scope creep, improves reviewability | Requires upfront work | N/A | Before every significant agent delegation | No | Yes | `skill-hub/ai-assisted-development/ai-coding-agent-task-design.md` | High | — |
| AI-generated code review protocol | Workflow pattern | Derived from multiple vendors + project conventions | Best practice | N/A | Any tool | Inspect agent output before merge | Catches hallucinations, drift, leaks | Adds review latency | N/A | Mandatory gate for agent-authored PRs | No | Yes | `skill-hub/ai-assisted-development/ai-generated-code-review.md` | High | — |

## Practical findings from Repomix usage on this repository

- Full repository pack (atlas, skill-hub, includes, layouts, data, scripts, tests, docs, root): **506 files, ~1.29M tokens (XML), ~1.21M tokens (compressed Markdown)**.  
- This exceeds the context window of most production models. A full-repo pack is useful for indexing and architecture overview, but not for direct single-prompt analysis.  
- Token distribution is highly skewed: a few large docs and data files dominate. Focused include/ignore patterns are essential.  
- Repomix security check reported **no suspicious files** for the configured include set.  
- Generated packs must stay in `.tmp/` or `/tmp` and must not be committed.

## Deferred topics and reasons

| Topic | Reason |
|---|---|
| Devin, OpenHands, SWE-agent dedicated pages | Fit is real but audience is narrower; covered in landscape page to avoid thin content. |
| Windsurf dedicated page | Acquisition by OpenAI (May 2026) creates strategic uncertainty; mention as alternative only. |
| Sourcegraph Cody | Public sources suggest continued relevance but less momentum than Cursor/Copilot; mention as alternative. |
| Cline / Roo Code | Active in open-source community but smaller ecosystem; mention as alternatives. |
| Gemini CLI | Public tooling exists but less documented than Codex/Claude Code; avoid precise claims. |
| Context7 / Playwright MCP | Interesting but too nascent for source-backed practical guidance; mention as emerging patterns. |
| Pricing tables | Avoided because pricing changes frequently and sources disagree; direct readers to official pages. |

## Source confidence legend

- **High:** Official documentation, GitHub repository, or direct local verification.  
- **Medium:** Vendor-claimed data corroborated by multiple third-party sources.  
- **Low:** Single third-party source, rapidly changing, or unverified claim (not used).

## Conclusion

The cluster will focus on practical, source-backed decision logic rather than rankings. Repomix is treated as a core workflow tool for repository context engineering. Coding agents are organized by interface (terminal vs IDE vs autonomous), not by hype. MCP is framed as a tool-integration standard with real security boundaries. Code review and security are treated as human-gated workflows, not autonomous replacements.
