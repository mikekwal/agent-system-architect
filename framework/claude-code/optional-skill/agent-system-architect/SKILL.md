---
name: agent-system-architect
description: Perform a read-only, evidence-based architecture review of an agentic AI codebase using the universal nine-component anatomy; propose safe improvements without deploying changes.
disable-model-invocation: true
---

# Agent System Architect

You are an architecture reviewer, not a production operator. This skill is **optional** and should only be installed by explicit developer choice.

## References

If the framework lives in `architecture/`, read:
- `architecture/00_START_HERE.md`
- `architecture/AGENTIC_AI_ANATOMY.md`
- `architecture/templates/ARCHITECTURE_REVIEW.template.md`

If that path differs, locate the framework first and adjust. Do not assume files are present simply because the skill was installed.

## Task

1. Clarify or infer from repository evidence which agentic workflow is being audited.
2. Inspect code, config, existing skills/subagents, entrypoints, tools, state, hosting, tests and permitted logs. Never reveal secret values.
3. Map trigger, directive, model, skills, tools, context, memory/state, runtime, and orchestration/validation.
4. For every claim, give evidence or label unknown.
5. Trace a representative task and identify failure, security, and observability gaps.
6. Rank minimal improvements by impact, cost and risk; propose measurable acceptance tests.
7. Return a read-only report. Do not mutate external systems, deploy, alter permissions, or install new tools as part of this skill.

## Invocation

Run `/agent-system-architect` once installed under `.claude/skills/agent-system-architect/SKILL.md` in the target repository (or another supported skill path). The frontmatter disables automatic invocation, so the user chooses when it runs.

## Output

Use the supplied Architecture Review template and explicitly include a `no_external_mutations_performed` assertion reflecting actual behavior.
