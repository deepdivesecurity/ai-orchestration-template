# AI Orchestration Template

Template repository for running a structured multi-agent software delivery workflow.

This project provides:
- Agent routing rules
- Role-specific agent instructions
- Threat modeling requirements
- Persistent state files for decisions, logs, and tasks
- Documentation artifact conventions for each phase

## What This Repository Is For

Use this template when you want repeatable, policy-driven execution across architecture, security, implementation, testing, review, and summary phases.

The workflow is designed to:
- Require architecture + threat modeling before implementation on structural or security-relevant changes
- Preserve evidence and traceability (`Threat-Model-Ref`, changed files, test evidence)
- Keep project state synchronized in `tasks/` and `documents/`

## Repository Structure

```text
.github/
  router.md                  # Agent routing + escalation + contracts
  agents/
    architect.agent.md       # Architecture phase instructions
    builder.agent.md         # Implementation phase instructions
    tester.agent.md          # Testing phase instructions
    reviewer.agent.md        # Review phase instructions
    summary.agent.md         # Summary/changelog phase instructions
  skills/
    threat-model/SKILL.md    # Security threat modeling skill (STRIDE + mappings)

context/
  project.md                 # Core project context (name, goal, stack, constraints)
  state-policy.md            # Rules for updating tasks/ and documents/

tasks/
  todo.md                    # Active tasks
  decisions.md               # Architectural/strategic decisions
  logs.md                    # Chronological change log

documents/
  README.md                  # Artifact expectations
  architect/                 # Architecture outputs
  builder/                   # Implementation outputs
  tester/                    # Test outputs

architecture/
  diagram/                   # Architecture diagram artifacts (.drawio)

examples/
  architecture_agent_example_output/
                             # Example generated outputs

.workflow.md                 # Standard and bug flows
```

## Workflow Overview

Standard flow:
1. Architect
2. Threat-Model
3. Builder
4. Tester
5. Reviewer
6. Summary

Bug flow:
1. Builder
2. Tester
3. Reviewer

Routing and escalation behavior is defined in [`.github/router.md`](.github/router.md).

## Key Contracts (Enforced by Prompts)

- Any request changing code/config/architecture/infrastructure must run through `Architect` first.
- A threat model is mandatory before implementation/fix activity for qualifying changes.
- Implementation and testing outputs must carry `Threat-Model-Ref`.
- Claims of changes or test results must include concrete evidence.
- If state updates are required, files under `tasks/` and `documents/` must be updated following `context/state-policy.md`.

## Artifact and Naming Conventions

- Documentation artifacts:
  - `documents/architect/YYYY-MM-DD-<slug>.md`
  - `documents/builder/YYYY-MM-DD-<slug>.md`
  - `documents/tester/YYYY-MM-DD-<slug>.md`
- Architecture diagrams:
  - `architecture/diagram/<unique-name>.drawio`
- Threat model reference format:
  - `Threat-Model-Ref: TM-YYYYMMDD-<slug>`

See [documents/README.md](documents/README.md) for required section content.

## Getting Started

1. Fill out [`context/project.md`](context/project.md) with real project details.
2. Add initial backlog items in [`tasks/todo.md`](tasks/todo.md).
3. Start requests through your orchestrator/router so phase ordering is respected.
4. Store generated phase artifacts under `documents/` and diagrams under `architecture/diagram/`.

## Minimal Bootstrapping Checklist

- [ ] `context/project.md` is populated (goal, stack, constraints, architecture context)
- [ ] `tasks/todo.md` contains prioritized tasks
- [ ] `tasks/decisions.md` includes any foundational decisions
- [ ] `tasks/logs.md` has an initial project entry
- [ ] Router and agent instructions align with your team process

## Example Output

See [`examples/architecture_agent_example_output/`](examples/architecture_agent_example_output/) for a sample architecture + threat-model-driven output set.

## Notes

This template does not include application runtime code. It is an orchestration scaffold for AI-assisted software delivery governance.
