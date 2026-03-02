# State Management Policy

This document defines how shared project state files must be updated.

Applies to:

- tasks/decisions.md
- tasks/logs.md
- tasks/todo.md
- documents/architect/
- documents/builder/
- documents/tester/

---

# 1. tasks/decisions.md
## Purpose
Permanent record of architectural and strategic decisions.

## When To Update
Must be updated when:

- A new architectural pattern is introduced
- A new infrastructure dependency is added
- A breaking API change is approved
- A security posture change occurs
- A core principle is modified

## Who Updates It
- Architect (primary)
- Reviewer (if missing)
- Threat-model (if security-driven decision)

## Format
Each decision must include:

ID:  
Date:  
Status: Proposed / Approved / Deprecated  
Context:  
Decision:  
Consequences:  

---

# 2. tasks/logs.md
## Purpose
Chronological record of significant technical changes.

## When To Update
Must be updated when:

- A feature is completed
- A bug fix is merged
- A refactor changes behavior
- A security mitigation is added
- Infrastructure changes

## Who Updates It
- Summary agent (primary)
- Builder (if requested explicitly)

## Format
## YYYY-MM-DD
- Short bullet summary
- Reference to decision ID (if applicable)

---

# 3. tasks/todo.md
## Purpose
Active task tracking.

## When To Update
- New tasks identified by Architect
- Security mitigations required by threat-model
- Follow-up actions identified by Reviewer
- Bug fixes identified by Debugger

## Who Updates It

- Architect
- Threat-model
- Reviewer
- Debugger

Builder does not create tasks unless instructed.

---

# 4. Mutation Rules
- Agents may append.
- Agents must not rewrite history.
- Decisions cannot be deleted - only deprecated.
- Logs must remain chronological.
- No retroactive modification without explicit instruction.
- Builder and Tester must generate per-request documentation artifacts in 'documents/builder/' and 'documents/tester/'.
- Architect must generate per-request documentation artifacts in 'documents/architect/'.
- Threat-model output must be presented in table format for readability and stored in 'documents/architect/'.
- Architecture outputs must include readable cost estimate sections with a summary and more granular sections by technology or service stored in 'documents/architect/'.
- Architecture diagrams must be produced as '.drawio' files.
- Architecture diagrams must use official vendor/service icons for vendor-specific diagrams and include relevant connections, ports/protocols (when known), and applicable network/security controls.

---

# 5. Enforcement
If a change requires a decision entry and none exists:

Reviewer must block approval.

If a feature is merged without log entry:

Summary agent must generate one.
