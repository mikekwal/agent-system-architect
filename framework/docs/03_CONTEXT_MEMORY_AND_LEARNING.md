# Context, State, Retrieval and Learning

## Distinguish five stores

1. **Immediate context:** instructions, current task and retrieved evidence available to a model call. It is bounded by the context window.
2. **Working run state:** current step, tool outputs, approvals, deadlines, and incomplete actions for one execution.
3. **Durable operational state:** structured facts and workflow status that must survive process restarts.
4. **Retrieval knowledge:** documents or records indexed for selective recall (keyword, vector or hybrid retrieval). A vector database is optional.
5. **Procedural knowledge:** version-controlled directives, skills, decision policies and test cases.

Do not mix these stores into one unrestricted “memory” blob. Persist only what future tasks genuinely need and what you are permitted to retain.

## Memory retrieval protocol

For a task, determine what must be known, query approved stores, filter by scope and recency, attach provenance, then put only relevant information into context. Mark unknown facts explicitly.

Memory write protocol: identify a permissible fact, validate accuracy, assign scope/owner, decide TTL/retention, store source reference, and record why it matters.

## Learning is not automatic retraining

Most deployed agents do not alter model weights during ordinary tool execution. They can improve with a controlled process:

`capture outcomes → label results → compare with evaluations → propose versioned changes → human/code review → regression tests → deploy → monitor`

Separate **operational state changes** from **procedural improvements**. Do not let untrusted task content author new policies or rewrite skills automatically.

## Practical questions

- What must survive a crash?
- What must be recalled later, and by what key?
- What is short-lived versus durable?
- Can the agent cite evidence for a remembered fact?
- How are records isolated between users/projects/tenants?
- Who can update skills and governance files?
- Can the system recover an interrupted run without repeating effects?
