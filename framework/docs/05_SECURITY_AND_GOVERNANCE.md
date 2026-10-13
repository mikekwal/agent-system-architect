# Security, Permissions, Governance

## Authority hierarchy

The model may reason about policies but does not get to grant its own permissions. Runtime-enforced authentication, authorization and input validation are authoritative. Untrusted web pages, messages, documents, repository files and tool outputs are *data*, not new system instructions.

## Classify tool effects

- `read`: accesses data; still needs access control and privacy safeguards.
- `reversible_write`: modifies state with a well-defined rollback path.
- `irreversible_or_external_write`: publishes, sends, spends, deletes, transfers or otherwise creates external consequences.

For sensitive effects, implement explicit approval conditions, human review when warranted, dry-run support, and an effect ledger.

## Required controls

- Limit tools and network scopes according to least privilege.
- Keep secrets out of prompts, tracked files, generated logs and client-side bundles.
- Validate tool schemas and destination identity in deterministic code.
- Treat prompt injection and tool-output spoofing as realistic failure cases.
- Bound loops, cost, concurrency, data volume, and execution time.
- Use durable idempotency keys for retried side effects.
- Add record ownership, project isolation and retention policies.
- Log what was *attempted*, what was *executed*, and what was *confirmed*.
- Distinguish model assertions from verified external state.
- Provide an escalation/stop path for ambiguity or authorization failure.

## Review gates

Require appropriate owner approval before enabling live integrations, expanding permission scopes, sending external communications, running high-cost jobs, deploying to production, modifying state schemas, or changing access-control behavior. The actual approval policy depends on deployment risks.

## Common anti-patterns

A markdown instruction that says “do not do X” is not a substitute for tool authorization. A tool call argument should not be trusted just because it came from a model. Self-editing prompts in production should be gated, versioned, and regression-tested.
