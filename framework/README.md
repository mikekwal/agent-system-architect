# Universal Agentic AI Anatomy Framework

**Version:** 1.0.0  
**Purpose:** A portable, domain-neutral architectural spine for designing, inspecting, improving, teaching, and deploying agentic AI systems.  
**Audience:** Builders, architects, founders, developers, reviewers, and AI coding assistants.  
**Status:** Design standard and starter templates. **Not** an installed agent, production runtime, or license to make changes.

## Start in under one minute

1. Read [`00_START_HERE.md`](00_START_HERE.md) and [`AGENTIC_AI_ANATOMY.md`](AGENTIC_AI_ANATOMY.md).
2. In an existing repository, ask your coding assistant to **inspect first**, using [`claude-code/HANDOFF_PROMPT.md`](claude-code/HANDOFF_PROMPT.md). This pack assumes nothing about the existing codebase.
3. Use the templates and machine-readable contracts as *proposals*. Nothing in `contracts/` automatically configures Claude Code or another orchestration library.
4. If desired, **deliberately** install the optional Claude Code skill from `claude-code/optional-skill/agent-system-architect/SKILL.md` into your own `.claude/skills/agent-system-architect/SKILL.md`. The skill is read-only and architecture-focused.
5. To make the **optional skill available across your own Claude Code projects**, install only its `SKILL.md` in `~/.claude/skills/agent-system-architect/SKILL.md`; for team-wide repo use install it in that repository's `.claude/skills/agent-system-architect/SKILL.md`. This is a manual choice, not automatic installation.
6. Keep a copy of the framework accessible to the agent and tell it the actual path when invoking the skill. A global skill installation does not itself install or expose the full framework everywhere.
7. Review the visual and editable diagrams in `diagrams/`.

## What is inside

| Path | Purpose |
|---|---|
| `AGENTIC_AI_ANATOMY.md` | Canonical nine-part architecture and invariants |
| `docs/` | Design, runtime, memory, reliability, security, teaching |
| `templates/` | Reusable directive, skill, tool, workflow, inventory, review templates |
| `contracts/` | JSON Schema for agent manifests and run results, plus valid example |
| `claude-code/` | Portable handoff prompt, `CLAUDE.md` snippet, optional skill |
| `diagrams/` | Editable Mermaid and rendered SVG/PNG architecture illustrations |
| `scripts/validate_package.py` | Offline JSON Schema and neutrality checks |

## The golden rule

**Use the same architecture, not the same agent behavior.** Each deployment chooses its own objective, tool permissions, execution model, storage, review criteria, and lifecycle. This framework is deliberately **not** optimized for any particular business function.

## Boundaries

- The system *may* use an LLM to choose actions; policies and critical invariants should be enforced by code or infrastructure.
- A Markdown skill teaches a procedure; it does not install external tools, give credentials, or train model weights.
- A subagent is an optional isolation/delegation boundary, not the definition of an agent.
- Persistent memory requires explicit read/write behavior; logs alone do not imply learning.
- Agents must not silently rewrite their governing policies based on raw task outcomes.
- Never infer deployed capabilities solely because a file or specification describes them.

## Compatibility

The core material is plain Markdown, JSON, YAML, and Mermaid, usable by Claude Code and other coding assistants. The optional Claude Code skill uses supported `SKILL.md` frontmatter; it is not mandatory. See `docs/04_LOCAL_AND_CLOUD.md` for CLI and hosted runtimes.

## Official reference links

- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code memory: https://code.claude.com/docs/en/memory
- Claude Agent SDK: https://platform.claude.com/docs/en/agent-sdk/overview
- Model Context Protocol: https://modelcontextprotocol.io/
- Agent Skills standard: https://agentskills.io/

Recheck installed versions and security policies before applying any tool-specific configuration. This document does not claim all features work in all environments.
