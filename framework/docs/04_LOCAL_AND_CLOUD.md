# Running the Same Spine Locally or in the Cloud

The **architecture** transfers. Its dependencies, security, persistence, and scheduling do not transfer automatically.

| Concern | Local CLI session | Cloud service or worker |
|---|---|---|
| Trigger | Interactive message, shell invocation, local script | Authenticated API, queue, webhook, schedule |
| Orchestration | CLI harness, local code, SDK | Hosted SDK, orchestrator, service logic |
| Model | Usually remote model API | Usually remote model API |
| Skills | Files discoverable in local environment | Bundled or accessible files/resources |
| Tool execution | Local shell, local permissions, reachable APIs | Container/worker sandbox and network policies |
| Secrets | Environment or local secret store | Managed secret vault/environment variables |
| Files | Local disk, often ephemeral session outputs | Durable object storage/volumes when needed |
| State | Local files or database | Database/queue/transactional state |
| Operations | Manual oversight; exits with process | Logs, alerts, retries, rate limits, recovery |

## Deployment-neutral reference architecture

```text
CLI / API / schedule / event
  -> authentication & input validation
  -> durable job state / queue
  -> orchestrator / agent runtime
  -> model call ↔ authorized tools
  -> validation / approvals
  -> durable result + trace + next event
```

## CLI mode

Useful for experimentation, coding, supervised runs, and development. A terminal session is not inherently always-on. A command/file may be recognized by one CLI and completely ignored by another. Validate actual instruction discovery and permission behavior.

## Cloud mode

Common patterns: an API gateway or webhook creates a job, a queue or jobs table persists it, a worker runs the agent loop, and a durable store captures results. Human approvals become waiting states and new events rather than long-lived model conversations.

Lightweight agents may run in serverless handlers. Shell-heavy, browser-heavy or media-heavy workloads generally need an appropriately provisioned process/container/sandbox. Product choice depends on runtime constraints, not an architectural mandate.

## Separation of concerns

- **Frontend/UI:** human oversight, job status, approvals.
- **Entry point:** authentication, validation, enqueueing.
- **Runtime:** executes model/tool loop.
- **Model provider:** reasoning; may be remote.
- **Data:** persistence, retrieval, artifacts.
- **Tool adapters:** controlled integrations.
- **Observability:** logs, traces, budgets and alerts.

## Migration checklist

- Can every local dependency run in the target runtime?
- Does it have the correct filesystem, CPU, memory, browser/binary and network access?
- Are tool credentials scoped and stored in managed secrets?
- Does a restart preserve or safely resume work?
- Are timeouts and platform execution ceilings understood?
- Can duplicate deliveries and retries be handled idempotently?
- Do approvals avoid silent autonomous external actions?
