# Agent Loop and Orchestration Patterns

## Three execution patterns

**Fixed workflow:** Code controls steps; the model performs bounded tasks like classification or synthesis. Default for well-understood work.

**Single agent with tools:** The model chooses actions iteratively within fixed policy/step bounds. Default for ambiguous, multi-step work with manageable context.

**Multiagent orchestration:** The parent routes distinct subtasks to specialist workers with isolated context, different tools, or parallel execution. Use only when measurable benefits outweigh handoff complexity.

## Reference state machine

`created → queued → running → [waiting_approval | retryable_failure] → running → [completed | failed | cancelled | escalated]`

Transitions must be durable and validated. Define a separate mechanism for approval resume; don't keep an LLM call open while waiting days for a human or external event.

## Orchestrator responsibilities

1. Authenticate trigger and parse its payload.
2. Deduplicate event and create `run_id` and `idempotency_key`.
3. Resolve workflow and allowed tool registry.
4. Build minimal context and model request.
5. Enforce maximum step count, deadline, and cost budget.
6. Validate model-requested tool calls and apply authorizations.
7. Execute with timeouts; record input, output, and effect identifiers.
8. Apply quality checks; use bounded backoff/retry only where safe.
9. Persist completion, blocked state, or escalation reason.
10. Emit a structured run result and observability trace.

## Pseudocode

```python
# Illustrative, not an SDK implementation.
run = load_or_create_run(event)
while run.status == 'running' and within_limits(run):
    context = select_context(run)
    decision = model.decide(directive, context, available_tool_schemas(run))
    if decision.is_final:
        result = validate_final(decision)
        persist_result_and_state_atomically(run, result)
        break
    for request in decision.tool_requests:
        validate_schema(request)
        authorize_effect(request, run.policy)
        tool_result = execute_with_timeout(request, run.idempotency_key)
        persist_effect_and_trace(run, request, tool_result)
        validate_tool_output(tool_result)
    run.steps += 1
if not run.is_terminal:
    terminate_or_escalate(run, reason='limits_or_blocked')
```

## Handoff contract

Each handoff should specify task ID, parent run, objective, input references, output schema, deadline/budget, permitted tools, required provenance, and error mode. Avoid freeform handoffs that lose identity, context, or verification.

## Failure patterns

- Loop never terminates: missing stop criteria and step limits.
- Duplicate write on retry: missing durable idempotency and effect ledger.
- Delegation explosion: too many loosely defined subagents.
- Stale context: no freshness checks or data version references.
- False success: completion assessed only by an optimistic model statement.
- Silent degradation: no traces, offline test fixtures, or operational metrics.
