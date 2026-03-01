# Agent Router

## Purpose
Determines which agent handles a request.

---

## Routing Rules

- Architecture design or question -> architect.agent.md
- Feature implementation -> builder.agent.md
- Bug or unexpected behavior -> debugger.agent.md
- Code review -> reviewer.agent.md
- Testing request -> tester.agent.md
- Formatting request -> formatter.agent.md
- Summary or changelog -> summary.agent.md
- Security-sensitive change -> threat-model skill

## Escalation Rules

- If structural change detected -> Architect first
- If security sensitive or security impact -> Threat-model before Builder
- If bug persists after fix -> Escalate to Reviewer
- Architectural flaw found during debugging → Escalate to Architect
