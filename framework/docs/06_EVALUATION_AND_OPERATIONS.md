# Evaluation and Operational Reliability

## Four separate measures

1. **Task quality:** correctness, completeness, adherence to directive, supporting evidence.
2. **Tool quality:** schema validity, authorization, API reliability, error recovery.
3. **System quality:** latency, throughput, cost, completion rates, restart recovery.
4. **Outcome quality:** whether the user/business goal was actually achieved.

Model self-assessment alone is not sufficient for high-stakes correctness or executed side effects.

## Evaluation suite

Design fixtures that include normal inputs, ambiguous requests, missing context, conflicting instructions, malformed tool results, upstream outages, duplicate triggers, unsupported requests, injected instructions, budget caps, and interrupted executions.

Measure: pass/fail, human override rate, factual support, latency, model/tool cost, retries, duplicate actions, tool errors, state consistency, and user-defined outcome measures.

## Operational run record

Store `run_id`, task ID, directive version, skill versions, model identifier, tool invocations, effect identifiers, relevant evidence references, validation results, finish state, error codes and costs. Avoid logging sensitive raw credentials or unnecessary personal content.

## Release discipline

- Keep skills/directives under version control.
- Make one change at a time where possible.
- Run deterministic tests and representative end-to-end evaluations.
- Compare to an established baseline; include regression cases.
- Deploy gradually, monitor changes, and support rollback.

## Completion definition

A run is **completed** only if an explicit validation confirms the desired artifact or effect exists and adheres to the output contract. Otherwise use `blocked`, `failed`, `cancelled`, or `escalated`, not an optimistic success message.
