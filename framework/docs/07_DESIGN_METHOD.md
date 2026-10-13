# From Vision to an Agent System: The Design Method

This method works for a founder, builder, maker, operator, or creative without assuming a specific industry.

## Phase 1: Clarify objective

Write the measurable outcome, beneficiary, trigger, inputs, acceptable autonomy, constraints, critical failure modes, and evidence of success. Specify what should remain human-owned.

## Phase 2: Locate uncertainty

Identify tasks requiring judgment or flexible interpretation. Keep deterministic checks deterministic. Avoid agentizing a known sequence just for the label.

## Phase 3: Choose the smallest architecture

Prefer: single model call → deterministic workflow with bounded model steps → single tool-using agent → multiagent orchestration, only as needed.

## Phase 4: Complete the nine-part inventory

Fill `templates/AGENT_DIRECTIVE.template.md`, the tool registry, context data-flow, storage, runtime, orchestration and validation. Use `templates/ARCHITECTURE_REVIEW.template.md` for existing systems.

## Phase 5: Design the interfaces

Specify trigger event schema, per-tool input/output schema, effect class, state keys, task output envelope, handoff contract, approval and error transitions.

## Phase 6: Build a thin vertical slice

Run one representative input through trigger, decision, tool execution, validation, persistence and review. Prefer a working, inspectable slice over a large untested constellation of subagents.

## Phase 7: Harden and evaluate

Test malformed inputs, injection, errors, retries, duplicates, stale memory, missing credentials, cancellation, and recovery. Confirm observable outcomes, not just plausible text.

## Phase 8: Extend safely

Add specialized skills and subagents only after a clear benefit is measured. Improve based on labeled outcomes and tests, with versioned changes and rollback.

## Design review rubric (0–2 each)

- Role and success criteria are explicit.
- Tool permissions and effects are controlled.
- Agent can distinguish observed evidence from inference.
- State survives restarts where needed.
- Validation can detect incorrect/partial results.
- Errors and ambiguous cases escalate safely.
- A new developer can trace what happened.
- Workflow complexity is justified.
- Costs, latency and context use are bounded.

`0 = absent; 1 = partial; 2 = robust. Max = 18.` This rubric is a conversation aid, not a substitute for integration tests.
