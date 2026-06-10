---
title: "Domain Research: AI Agent Skills"
robots: noindex
sitemap: false
---

# AI Agent Skills

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from agent skill formats, tool use, structured outputs, evals, safety, and memory management?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [OpenAI Structured Outputs Guide](https://platform.openai.com/docs/guides/structured-outputs) (src-601) | 1 | Canonical reference for constrained decoding | JSON Schema, Pydantic, refusal handling |
| [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) (src-602) | 1 | Canonical multi-turn tool-calling loop | Function schemas, namespaces, parallel calls |
| [Anthropic Claude Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) (src-603) | 1 | Vision-based GUI automation with safety guardrails | Sandbox design, human approval gates |
| [Microsoft Agent Framework](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/) (src-604) | 1 | Consolidated open-source multi-agent orchestration | Agent/Workflow orchestration, human-in-the-loop |
| [OpenAI–Anthropic Safety Evaluation](https://openai.com/index/openai-anthropic-safety-evaluation/) (src-605) | 1 | First cross-lab safety evaluation | Jailbreak testing, instruction hierarchy, reasoning models |
| [Google ADK Design Patterns](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agents/genai-experience-concierge/agent-design-patterns/README.md) (src-606) | 1 | Reusable multi-agent control flows | Planner-Executor-Reflector, DAG execution |
| [LangChain & LlamaIndex Docs](https://python.langchain.com/docs/integrations/providers/llama_index/) (src-607) | 2 | Widely adopted open-source orchestration frameworks | RAG + agent hybrid, observability |
| [SWE-bench / AgentBench](https://arxiv.org/abs/2510.08996) (src-608) | 1 | Current frontier for agent evaluation | Three-layer evaluation, benchmark mutation |
| [Self-Reflection in LLM Agents](https://arxiv.org/abs/2405.06682) (src-609) | 2 | Empirical evidence on reflection effectiveness | Reflection prompt design, generator-critic pairs |
| [Agent Memory & Context Management](https://arxiv.org/abs/2604.01599) (src-610) | 2 | Taxonomy of agent memory architectures | Three-tier compression, hierarchical memory |

## Key practical patterns

- Portable skill packages (Claude Skills / `SKILL.md`, OpenAI Custom GPTs) are converging on markdown-frontmatter + instruction-body formats.
- Cross-platform install patterns use symlinks or copy commands for multiple IDEs and agents.
- Skills should be separated from live data access: a Skill defines *how* to do something; an MCP server defines *what is true right now*.
- The canonical tool-use loop is five steps: request → tool_call → execute → return → final response.
- Namespaces and deferred loading prevent context bloat when >20 tools are available.
- Constrained decoding (CFG-based token masking) guarantees syntactic adherence but not semantic correctness; downstream validation is still required.
- Reasoning models (o3, Claude Opus 4 with thinking) consistently show stronger safety performance than non-reasoning models.
- Three-tier adaptive compression: Early Warning (40%), Critical Threshold (60%), Emergency Truncation (95%).

## Artifacts found

- `SKILL.md` with YAML frontmatter (`name`, `description`, `tags`, `allowed-tools`)
- `guides/` and `references/` folders for deep-dive documentation
- `scripts/` for automation hooks
- Platform-specific entry points (`.github/copilot-instructions.md`, `GEMINI.md`, `AGENTS.md`)
- Validation scripts (`validate_agent_skills.py`)
- Function JSON schemas with strict mode (`additionalProperties: false`)
- Namespace manifests grouping related tools by domain
- Tool call execution logs with `call_id` correlation
- Evaluation harnesses (Docker-based for isolation)
- Trajectory logs with tool calls, observations, and final outputs
- Safety evaluation rubrics (jailbreak resistance, misuse cooperation, sycophancy)
- Human approval queue schemas (pending → approved → denied → logged)

## Decision rules found

- If the target audience uses multiple IDEs, ship a portable `SKILL.md`-based folder.
- If the skill requires live data, pair it with an MCP server rather than embedding static knowledge files.
- If the model must decide between multiple external actions, use function calling; if it only needs to format data, use structured outputs.
- If you have >20 functions, use namespaces or deferred loading.
- If using a reasoning model, preserve and return reasoning items in the conversation history.
- If deploying a general-purpose model, add extra output filters because non-reasoning models are more susceptible to misuse.
- If context exceeds 40% of the window, begin compressing inactive files.
- If the agent must learn across sessions, store memories as human-readable markdown with stable IDs.

## Quality gates found

- Run `validate_agent_skills.py` before committing changes.
- Pass the "intern test": a human given only the function description should know how to call it.
- Use enums and boolean flags to make invalid states unrepresentable.
- Validate tool outputs with application-level business logic, not just JSON schema compliance.
- Log every tool call, argument, and result for audit and debugging.
- Run StrongREJECT or similar adversarial suites before every major model update.
- Manually review a sample of refusal responses to ensure nuanced redirects are not mis-scored.
- Terminate reflection loops if the score does not improve between iterations.

## Common failure modes

- Concept inflation: rebranding basic prompt engineering as a "skill architecture" without measurable improvement.
- Prompt injection via malicious skill files that bypass agent guardrails.
- Static knowledge files in GPTs/Gems become stale; without live connectors, answers drift.
- Overly long instructions exceed context windows or degrade retrieval quality.
- Model calls the wrong tool when descriptions are vague or overlapping.
- Including too many functions at once degrades accuracy and increases token cost.
- Flawed self-evaluation can lead the agent further astray (compounding error).
- Append-only history guarantees token-limit failure for complex tasks.

## Candidate skills

- `structured-output-designer`
- `tool-use-orchestrator`
- `agent-memory-curator`
- `reflection-loop-designer`
- `safety-gatekeeper`
- `schema-contract-designer`
- `eval-harness-builder`
- `context-compressor`
- `red-team-prompt-designer`
- `human-approval-gate`

## Source-backed notes

- OpenAI Structured Outputs Guide defines schema size limits: ≤5,000 object properties, ≤10 nesting levels, ≤120,000 characters for names/enums (src-601).
- OpenAI Function Calling Guide introduces namespaces, `tool_search` deferral, and parallel tool calls (src-602).
- Anthropic Computer Use requires a production architecture with Task controller → Sandbox → Policy layer → Human approval (src-603).
- Microsoft Agent Framework consolidates Semantic Kernel and AutoGen into a single open-source framework with two orchestration modes (src-604).
- Cross-lab safety evaluation shows reasoning models outperform non-reasoning models on safety evaluations, but past-tense jailbreaks remain effective (src-605).
- Google ADK catalogs reusable multi-agent control flows: Planner → Executor → Reflector (src-606).
- SWE-bench and AgentBench define three-layer evaluation: reasoning, action, execution; recommend running stochastic agents 5+ times per configuration (src-608).
- Self-reflection research shows Composite reflection > Solution > Instructions > Explanation > Advice > Keywords > Retry > Baseline (src-609).
- Agent memory research proposes three-tier adaptive compression and hierarchical memory: Working, Compressed, Architectural (src-610).

## Gaps / further research needed

- Official Google ADK / Gemini structured-output docs are incomplete; the GitHub reference is a demo README rather than comprehensive API documentation.
- Anthropic structured outputs / strict schema docs are less detailed than OpenAI's equivalent.
- Production observability and telemetry standards for agent trace formats are still emerging.
- Real-world cost and latency benchmarks for multi-agent workflows with reflection loops are scarce.
- Standardized skill format specification (like an RFC) does not yet exist.
- Human-in-the-loop UX patterns are mentioned as requirements but lack concrete interface research.