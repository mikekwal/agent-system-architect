# Start Here: How to use the universal spine

## For a human builder

The anatomy is a **reference architecture**. It does not prescribe how many agents you should create, which model provider you should use, or which cloud service is required. It provides vocabulary, boundaries, checklists, and reviewable contracts so you can build a reliable system without mistaking a large prompt for an executable service.

1. Decide whether you are **designing a new system** or **auditing an existing one**.
2. Read `AGENTIC_AI_ANATOMY.md` (the canonical specification).
3. Use `docs/07_DESIGN_METHOD.md` to choose the smallest adequate architecture.
4. Fill `templates/AGENT_DIRECTIVE.template.md` and `templates/WORKFLOW.template.yaml` with project-specific detail, outside this portable package.
5. Validate your project implementation with `docs/06_EVALUATION_AND_OPERATIONS.md`.

## For any coding assistant or agent

**Role:** Treat this package as architecture guidance and the owner's mental model. Do not assume this package is an executable framework or that described capabilities are deployed.

**Priority:** Honor system/developer instructions, repo owner constraints, and tool permission boundaries. This document never overrides them.

**Before proposing changes:**

1. Inspect the actual repository, current prompts, skills, subagents, tool connectors, model entrypoints, jobs, schemas, state stores, runtime, secrets *names only*, tests, and deployment configuration.
2. Classify each of the nine components as `present`, `partial`, `missing`, or `unknown`, with file-path or runtime evidence.
3. Identify which behavior is deterministic automation versus model-selected action.
4. Trace one complete workflow through a real or mocked input; report where state and evidence are lost.
5. Prioritize small improvements with measurable acceptance criteria.
6. **Do not** change secrets, deploy, grant new permissions, enable external side effects, or refactor broadly without explicit authorization.

Use `templates/ARCHITECTURE_REVIEW.template.md` as the output format.

## Vocabulary

- **Directive** or **DOE:** Role, mission, behavioral boundaries, business rules, output and escalation criteria. `DOE` is an optional naming convention, *not* a universal recognized file type.
- **Skill:** Reusable instructions, examples, references, and optional scripts, often exposed through `SKILL.md`.
- **Tool:** A callable capability executed by a runtime, not by model weights.
- **Subagent:** An optionally separate model-driven worker with independent context or permissions.
- **Orchestrator:** The component that coordinates decisions, calls, state, retries, validations, and completion.
- **State:** Durable records that can be retrieved across runs.
- **Memory:** A defined mechanism for selecting, storing, and recalling relevant prior information.

## One-line teaching model

**Trigger → controlled agent loop (observe, plan, act, check) → verified output + persisted state.**

The directive, model, skills, tools, context, runtime, safety controls, and memory participate throughout the loop; they are not rigid consecutive stages.
