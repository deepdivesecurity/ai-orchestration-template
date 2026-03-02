---
name: threat-model
description: Perform structured security threat modeling for any feature, architecture, or infrastructure change.
license: Complete terms in LICENSE.txt
---

# Threat Model Skill

## Purpose
Analyze security risks in a proposed or implemented change.

---

## Context Resolution
Before performing analysis, read:

- context/project.md

Identify:
- Trust boundaries
- External dependencies
- Secrets
- Data flows
- Untrusted inputs

Do not assume specific technologies.

---

## Methodology
### 1. Identify Assets
- Secrets
- User data
- Credentials
- Internal services
- Logs

### 2. Identify Entry Points
- APIs
- User input
- Configuration
- External services
- Deployment pipelines

### 3. Apply STRIDE Analysis
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

### 4. Map Threat
 - Map threat to Mitre ATT&CK, Mitre CWE, Mitre CAPEC, OWASP Top 10

### 5. Evaluate Mitigations
- Validation
- Authentication
- Authorization
- Rate limiting
- Encryption
- Monitoring

### 6. Map Compliance Framework Security Controls
- NIST SP 800-53
- ISO 27001
- SOC 2
- CSA CCM
- PCI DSS
---

## Output Format
- If mitigation introduces architectural change, require new decision entry in tasks/decisions.md with reference to this analysis according to context/state-policy.md.
- If mitigation introduces new task, append to tasks/todo.md.
- Include a unique evidence field: 'Threat-Model-Ref: TM-YYYYMMDD-<slug>'.

### Threat Model Report
Threat-Model-Ref:

Feature Analyzed:

Threat table (required):

| Threat | Category (STRIDE) | Threat Mapping (ATT&CK/CWE/CAPEC/OWASP) | Severity | Likelihood | Impact | Mitigation | Compliance Security Controls | Residual Risk |
|---|---|---|---|---|---|---|---|---|
| ... | ... | ... | Low/Medium/High/Critical | Low/Medium/High | ... | ... | ... | ... |

The report must be easy to scan and use table format as the primary presentation.

---

## Guardrails
- Assume user input is hostile
- Assume external systems are untrusted
- Prefer defense-in-depth
- Prefer fail-closed behavior
- Secrets must remain protected
