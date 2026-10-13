# Agentic AI Anatomy: Canonical Architecture

`framework_id: universal.agentic.anatomy`  
`framework_version: 1.0.0`  
`scope: domain-neutral`  
`normative: component definitions, invariants, safety principles`  
`not_normative: cloud vendor choices, model selection, number of subagents`

> An agentic AI system is software that uses a reasoning model to select and adapt actions toward a defined objective within a controlled execution environment. An LLM alone is not an operational agent.

## The nine-part spine

| ID | Component | Key question | Typical implementation | Required design evidence |
|---|---|---|---|---|
| A1 | Trigger | Why start or resume? | User prompt, CLI, timer, queue, webhook | Entry-point and authenticated trigger contract |
| A2 | Directive / DOE | Who are you and what are the boundaries? | System instructions, repo guidance, directive Markdown | Role, objective, constraints, success / escalation |
| A3 | Model / brain | Who interprets ambiguity and chooses next steps? | LLM API or local model | Model selection, prompt policy, decision scope |
| A4 | Skills / procedures | What reusable methods apply? | `SKILL.md`, reference data, scripts | Discovery/loading and skill version provenance |
| A5 | Tools / actions | What can actually happen? | Typed functions, APIs, MCP, CLI | Input schemas, authorization, timeout, side-effect class |
| A6 | Context | What does the model need *now*? | Task input, retrieved files, tool outputs | Grounded context selection, size, origin, freshness |
| A7 | Memory / state | What must survive a run? | Database, files, object store, retrieval index | Data model, persistence, recall and retention rules |
| A8 | Runtime | Where do code and tools execute? | CLI, sandbox, cloud worker, container | Runtime dependencies, process lifecycle, secrets |
| A9 | Orchestration + validation | How does work finish safely and correctly? | Loop, state machine, validators, approvals, logs | Step budget, completion criteria, failure paths, tests |

**These are architectural responsibilities, not nine sequential commands.** In practice, context may be retrieved after every tool call, a skill may be invoked late, and validation can happen before or after many intermediate actions.

## Operational sequence

1. **Trigger** identifies a bounded objective and creates an identifiable run.
2. **Initialize** loads directive, available tools, approved policies, and minimal relevant context.
3. **Observe** obtains facts and captures uncertainty/provenance.
4. **Plan** selects the next smallest useful step. The plan can change as evidence arrives.
5. **Act** requests an authorized tool; the runtime validates the call and executes it.
6. **Check** validates tool effects and outputs; on uncertainty retry safely, halt, or escalate.
7. **Save** durable state, evidence, and next-work trigger; stop when completion conditions hold.
8. **Repeat** only within budget, deadline, and policy limits.

```text
TRIGGER → RUN STATE → ORCHESTRATOR ↔ MODEL
                          |           ↑
                          ↓           |
                     TOOL REQUEST → RESULT
                          ↓
                    VALIDATION + GATES
                          ↓
                VERIFIED OUTPUT + PERSISTENCE
```

## What each term is *not*

- **Command / trigger ≠ agent:** It initiates a run but does not add autonomous judgment.
- **Directive ≠ magic file:** An arbitrary DOE file must be explicitly loaded or referenced unless the chosen runtime recognizes its name.
- **LLM ≠ runtime:** The model requests actions; application tools actually run them.
- **Skill ≠ tool:** A skill may *describe* how to use tools; it does not grant access to those tools.
- **Subagent ≠ skill:** A subagent is a separately delegated worker, often with its own context/tool scope.
- **RAG ≠ memory by default:** Retrieval only contributes what the system stores, indexes, selects, and presents.
- **Logs ≠ learning:** Progress toward better behavior needs evaluation, feedback, controlled updates, and review.
- **Cloud hosting ≠ model hosting:** Running orchestration in the cloud usually still calls a remote LLM service.

## Minimal reliability invariants

1. Every run has an ID, bounded objective, validated input, and measurable completion condition.
2. Every tool is explicit, permissioned, typed, logged, and assigned an effect category (`read`, `reversible_write`, `irreversible_or_external_write`).
3. Untrusted retrieved content never gains policy authority over system/developer instructions.
4. External effects that can be harmful, costly, or hard to reverse use an authorization policy and (where appropriate) human approval.
5. Retries cannot repeat external side effects accidentally; use durable idempotency keys and inspect result state.
6. The agent has maximum steps, token/cost limits, timeouts, and terminal failure/escalation states.
7. Important decisions cite or retain provenance for the inputs that informed them.
8. State writes and memory updates have explicit scope, ownership, privacy rules, and retention.
9. Directive/skill changes are versioned and tested, not silently rewritten on each run.
10. A deployment's actual behavior is established by code/tests/observations, not specification text alone.

## When to split into multiple agents

**Default: one agent plus multiple skills/tools.** Introduce additional subagents only when one or more of these are material: context isolation, distinct permission domains, parallelizable independent tasks, different specialist evaluations, or an unusually long workflow that benefits from delegated bounded results.

Avoid turning each function into a separate LLM agent. A deterministic function is preferable when the rule is known and the task does not require language-model judgment.

## How this design adapts

The spine is constant. A particular implementation supplies different values for triggers, directive, model, tool registry, skills, context sources, memory, runtime, and evaluation. See `contracts/agent-spec.schema.json` for an optional *design manifest*, and `docs/04_LOCAL_AND_CLOUD.md` for deployment variants.

## Output envelope

An agent run should report at minimum `run_id`, `status`, `outcome`, `evidence`, `errors`, `side_effects`, and `next_action`. See `contracts/run-result.schema.json`. This makes agents composable and their behavior auditable.

## Teaching analogy

An agent is a digital worker with a job description (directive), reasoning capability (model), reference manuals (skills), equipment (tools), available case files (context), persistent records (memory/state), a workplace (runtime), and supervision/quality control (orchestration and validation).

**The useful business promise is not “it thinks.” It is “it can work reproducibly, with evidence, oversight, and observable outcomes.”**
