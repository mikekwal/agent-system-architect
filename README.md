# agent-system-architect

A Claude Code skill for designing and reviewing agentic AI systems against the Universal Agentic AI
Anatomy Framework v1.0 (bundled in `framework/`). Read-only by design: it produces an architecture map, a
gap analysis and a prioritized plan. It does not deploy, send, or change permissions.

## Install

For every project on a machine, clone into the global skills folder:

```bash
git clone https://github.com/mikekwal/agent-system-architect.git ~/.claude/skills/agent-system-architect
```

For one repository, copy `SKILL.md` to `.claude/skills/agent-system-architect/SKILL.md` and either copy
`framework/` to `architecture/` in that repository or rely on the global copy.

## Use

In Claude Code, run `/agent-system-architect`. It only runs when called by name.

## Contents

- `SKILL.md`: the skill.
- `framework/`: the nine-part spine, ten reliability invariants, design method, templates, JSON contracts
  and diagrams. Keep it domain-neutral. Project findings belong in the project.
