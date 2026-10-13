# Universal Agentic AI Architecture Handoff (paste into Claude Code)

Read `README.md`, `00_START_HERE.md`, and `AGENTIC_AI_ANATOMY.md` from the Universal Agentic AI Anatomy Framework.

This package is the **universal architecture spine** for agentic software. It is intentionally domain-neutral. Do not import examples, roles, or policies from unrelated agents. It expresses design principles, not proof that specific features already exist.

My goal is to align this repository's agentic system with the nine components: (1) trigger, (2) directive, (3) model, (4) skills, (5) tools, (6) context, (7) memory/state, (8) runtime, and (9) orchestration/validation.

Please work **read-only first**:

1. Inspect existing project instructions (`CLAUDE.md` etc.), agent/subagent definitions, skills, code entrypoints, integration wrappers, state stores, job/event paths, tests, deployment, and secrets **names only**.
2. Trace at least one existing or mocked end-to-end task.
3. Fill `templates/ARCHITECTURE_REVIEW.template.md`; mark components `present`, `partial`, `missing`, or `unknown`, with evidence.
4. Distinguish skills from tools, subagents from functions, working context from durable memory, and agent judgment from deterministic workflow.
5. Recommend the smallest, safest improvements with expected gains, dependencies, risk, and acceptance tests.
6. Do not create unnecessary new agents, migrate databases, modify secrets, deploy, send external communications, alter permissions, or rewrite significant files unless I explicitly authorize changes.
7. Use the universal agent-schema file only as an optional **design manifest**. It is not automatically parsed by Claude Code.

First deliver an architecture map, gap analysis, prioritized plan, and explicit decisions requiring my approval. Do not implement yet.
