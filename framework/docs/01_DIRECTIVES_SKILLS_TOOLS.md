# Directives, Skills, Tools, Subagents: The Four-Way Split

## Directive / DOE

A directive defines the role, objective, authorities, prohibitions, output shape, stopping conditions, and escalation triggers. Keep broad policy separate from task-specific evidence. Directives cannot supersede application/system permissions.

Recommended fields: purpose, scope, success measure, non-goals, trust boundaries, allowed effects, escalation, outputs, uncertainty handling, owner and version.

An arbitrary `DOE.md` file is only a convention. Hook it into the chosen loader and test that it is actually available when needed.

## Skills

A skill is a reusable, discoverable procedure. An Agent Skills-style `SKILL.md` may include YAML frontmatter (`name`, `description`) and a Markdown body. The body can link to reference files or scripts. Skills should be focused, measurable, composable and versioned; do not load an entire skill library into every run.

A skill teaches **how**. It does not by itself supply authenticated **access** or guarantee an outcome. Its inclusion in context is not the same as training/fine-tuning the model.

## Tools

A tool is a typed execution interface. Its tool contract should state input/output schemas, required permissions, side effect class, timeout, retry policy, idempotency behavior, failure codes, and observability.

The model may request a tool call; the runtime decides if it can execute it and performs the action. Tool descriptions are part of context; they are not executable implementations.

MCP is a standardized option for connecting tools/resources; direct SDK functions and HTTP APIs are alternatives.

## Subagents

A subagent is a delegated worker with its own instructions and (often) context. Use it when isolation or parallelism is valuable. It returns bounded, checkable results; the parent is still responsible for integrating outputs and respecting global authority limits.

A subagent is not required for every skill, every tool, or every workflow stage.

## Decision guide

| Need | Prefer |
|---|---|
| Repeat a reliable written process | Skill |
| Enforce a fixed validation rule | Function / deterministic code |
| Call external software | Tool |
| Isolate a large research or specialist task | Subagent |
| Coordinate end-to-end work and recovery | Orchestrator |
| Preserve facts across sessions | Persistent state + retrieval policy |

## Checklist

- Can a reviewer find the directive's intended loading point?
- Can a reviewer tell whether a named skill is installed, discovered, and invoked?
- Does every tool have a real implementation and permission boundary?
- Do specialist workers return structured outputs rather than freeform assumptions?
- Does the architecture work without multiplying agents unnecessarily?
