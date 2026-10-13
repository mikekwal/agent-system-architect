# A Five-Minute Teaching Guide

## First minute: separate model from agent

A model generates decisions or text. An agent system wraps it with objective, instructions, tools, state, a runtime, and governance so it can attempt multi-step tasks. The brain is only one component.

## Second minute: the nine parts

1. Trigger: why it wakes up.
2. Directive: job description and rules.
3. Model: reasoning brain.
4. Skills: repeatable training manuals.
5. Tools: real-world capabilities.
6. Context: relevant information right now.
7. Memory/state: persistent records.
8. Runtime: where it executes.
9. Orchestration/validation: supervision, feedback, and completion.

## Third minute: explain the action loop

Observe → Plan → Act → Check → Save. The runtime loops through decisions and tools until the objective is verified or a stopping condition is reached.

## Fourth minute: teach the three misconceptions

- Loading a skill is **not** downloading new neural weights.
- Calling a tool is **not** the same as the model having performed a real-world action until the runtime confirms it.
- Logging results is **not** automatic learning or model improvement.

## Fifth minute: local versus cloud

A local CLI is a supervised workstation. A hosted worker is an always-available process with triggers, jobs, permissions, persistence and monitoring. Both can use the same spine, but the hosted system needs operational engineering.

## Close with one sentence

"Reliable agentic AI is not one clever prompt; it is coordinated intelligence, executable capabilities, durable state, and measurable controls."
