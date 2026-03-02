# Agent Router

## Purpose
Determines which agent handles a request.

---

## Routing Rules

- Architecture design or question -> architect.agent.md
- Feature implementation -> builder.agent.md
- Code review -> reviewer.agent.md
- Testing request -> tester.agent.md
- Summary or changelog -> summary.agent.md
- Security-sensitive change -> architect.agent.md (architect invokes threat-model skill)
- Any request that changes code, configuration, architecture, or infrastructure -> architect.agent.md first; architect must run threat-model skill, then hand off to implementation/review agents.

## Escalation Rules

- If structural change detected -> Architect first
- Threat-model is mandatory before any implementation or fix activity, and is orchestrated by architect for implementation requests.
- If bug persists after fix -> Escalate to Reviewer
- Architectural flaw found during debugging → Escalate to Architect
- Limit Builder <-> Tester <-> Reviewer rework to 2 cycles per request; if unresolved, escalate to Architect (design issue) or Builder (behavior issue), then stop auto-handoffs.
- Do not auto-handoff on pure formatting or summary requests unless explicitly requested by the user.

## Evidence Contract

- Any change request that modifies code, configuration, architecture, or infrastructure must include 'Threat-Model-Ref'.
- If 'Threat-Model-Ref' is missing or invalid, halt implementation flow and route to architect, which must invoke threat-model skill.
- Downstream agents must preserve 'Threat-Model-Ref' in outputs and handoffs.
- Agents must not claim file/task changes unless they include exact changed file paths and concrete changed content.
- Agents must not assume stack, frameworks, or file layout not discoverable from workspace files.
- Architect outputs must include a readable cost estimate report.
- Architecture diagrams must be delivered as '.drawio' artifacts and use official vendor/service icons for vendor-specific architectures.
- Architecture diagrams must include relevant connections, protocol/port details (when known), and applicable network/security boundaries and controls.
- Threat-model outputs must use table format.
- Architect, Builder, and Tester outputs must include generated documentation files under 'documents/'.

## Phase Contract

- Implementation workflows must emit phase markers in sequence:
- 'Phase: Architect'
- 'Phase: Threat-Model'
- 'Phase: Builder'
- 'Phase: Tester'
- 'Phase: Reviewer'
- 'Phase: Summary'

## Execution Contract

- If required workspace context is missing, the agent must output 'Blocked' with exact missing files/fields and stop auto-claims of implementation.
