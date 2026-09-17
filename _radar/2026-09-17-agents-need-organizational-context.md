---
layout: note
title: "Agents Need Organizational Context, Not Just More Connections"
subtitle: "Access to information is not the same as understanding what matters."
date: 2026-09-17
source: "AI Engineer — Brandon Waselnuk, Unblocked"
source_url: https://www.youtube.com/watch?v=KcVkq5L-0f0
confidence: medium
summary: "Coding agents often fail because they must rediscover how the organization works. A useful context layer should reconcile sources, rank relevance, respect permissions, and give the agent a compact task-specific view before it starts coding."
topics:
  - ai_engineering
  - context_engineering
  - coding_agents
  - mcp
  - organizational_memory
---

Brandon Waselnuk frames a coding agent as a strong engineer on the first day at a company: technically capable, but missing the local knowledge that makes an implementation fit the organization.

That missing knowledge includes architecture decisions, rejected approaches, current conventions, incidents, pull-request history, ownership, and discussions that never became formal documentation.

## The useful idea

Giving an agent access to GitHub, Slack, documentation, or several MCP servers does not automatically create understanding. The agent still has to decide what to search, which source is current, which source has more authority, and whether another source contradicts the first answer it found.

A common failure mode is **satisfaction of search**: the agent finds one plausible result, treats it as sufficient, and starts implementing. The answer may be technically valid but wrong for the organization.

This creates another expensive loop:

**missing context → plausible assumption → implementation → human correction → another search → rework**

As agents become more autonomous and run in parallel or in the background, this problem becomes harder to catch early.

## What a useful context layer needs

Waselnuk describes six capabilities that matter more than simply adding another connector:

1. **Unified system context** — connect code, discussions, issues, documentation, and other relevant sources.
2. **Targeted retrieval** — return the evidence that matters for the current task instead of dumping large amounts of text into the context window.
3. **Conflict resolution** — handle stale or contradictory sources instead of accepting the first match.
4. **Personalized relevance** — shape context around the repository, team, task, and user.
5. **Token optimization** — give the agent a compact answer with a path to deeper evidence when needed.
6. **Permission enforcement** — the final answer must respect what the requesting user or agent is allowed to know, not only whether a connector is authenticated.

## Reported result — useful, but not a benchmark

Unblocked reports a same-prompt comparison where an agent without its context engine used about **20.9 million tokens and 2 hours 33 minutes**, while the context-assisted run used **10.8 million tokens and 25 minutes**. The second run also required much less correction before review.

These numbers are useful as a signal, not as a general productivity claim. They come from a vendor demonstration on a specific task and repository, so the result needs independent replication before it can be treated as a benchmark.

## Signal for our workflow

Our `AGENTS.md` and repository documentation are necessary, but they are only the beginning. For substantial work, the agent should receive a small research packet before implementation that answers questions such as:

- What part of the system owns this behavior?
- Which current rules and architecture decisions apply?
- Which files, pages, or integrations are actually relevant?
- Is there a newer source that replaces an older convention?
- What previous decision explains the current design?
- Which evidence should the agent cite before changing something important?

For SAP and enterprise work, the same principle is even more important. Technical documentation alone is rarely enough. Good context also includes process ownership, configuration rationale, integration relationships, incident history, master-data rules, and the reason a previous design decision was made.

A practical operating rule is:

> Do not make the agent search the whole organization from zero for every task. Give it a compact, current, permission-safe context package before it decides what to build.

## What remains unproven

The talk explains a strong architecture pattern, but it does not prove that one context-engine design is the correct solution for every organization. Context systems also have their own maintenance problem: freshness, conflicting sources, permissions, and indexing rules must stay correct over time.

**Primary source:** [Your agents lack context: Here's how to fix “You're absolutely right!”](https://www.youtube.com/watch?v=KcVkq5L-0f0), Brandon Waselnuk, Unblocked, AI Engineer 2026.  
**Transcript / talk notes:** [AI Engineer](https://ai.engineer/talks/KcVkq5L-0f0-your-agents-lack-context-heres-fix-youre)
