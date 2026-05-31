# SOFTWARE DEFECT ANALYSIS TEMPLATE

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: yes (12AM:40 31/05/2026 - Khoi Minh Nguyen)
ACCEPTED: yes (12AM:44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the template for one Requirement 2 software defect analysis.

Goals:

* Capture one public software defect from 2022-2026
* Record source, severity, consequences, and solution
* Identify AI bias or hallucination in the AI explanation
* Support traceability to final report and references
* Keep each defect analysis consistent as `DEF-XXX`

---

## File Naming Format

```text
DEF-XXX_<system>_<short_issue>.md
```

Example:

```text
DEF-005_air_canada_chatbot_refund_policy.md
```

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Defect ID | DEF-XXX |
| System/Product |  |
| Organization |  |
| Year publicized | 2022 / 2023 / 2024 / 2025 / 2026 |
| AI/LLM related | yes/no |
| Source type | News / Vendor report / Incident report / Research / Other |
| Severity | LOW / MEDIUM / HIGH / CRITICAL |
| Status | DRAFT / REVIEWED / VERIFIED / FINAL |

---

## 2. Source Information

| Item | Value |
| --- | --- |
| Primary source URL |  |
| Source title |  |
| Publication date | YYYY-MM-DD |
| Access date | YYYY-MM-DD |
| Evidence ID | EV-XXX |

---

## 3. Defect Description

```text
Describe what failed, where it happened, and who was affected.
```

---

## 4. Severity Analysis

| Factor | Notes |
| --- | --- |
| User impact |  |
| Business impact |  |
| Safety/security impact |  |
| Scope |  |
| Justification for severity |  |

---

## 5. Consequences

```text
Describe the consequences, such as financial loss, user harm, security exposure, service outage, legal risk, or reputational damage.
```

---

## 6. Solution Or Mitigation

```text
Describe the fix, mitigation, rollback, policy change, testing improvement, or prevention method.
```

---

## 7. AI Bias Or Hallucination Found

Each defect needs one identified AI bias or hallucination in the AI explanation.

| Field | Value |
| --- | --- |
| AI tool |  |
| Prompt ID | PROMPT-XXX |
| AI issue type | HALLUCINATION / BIAS / MISSING_CONTEXT / OVERGENERALIZATION / WRONG_SEVERITY |
| Related AI observation | AI-OBS-XXX |

Explanation:

```text
Describe what the AI got wrong and how you verified it.
```

---

## 8. Report Summary

```text
Write a concise paragraph that can be copied into the main report after verification.
```

---

## Final Notes

Do not rely on AI as the source for the defect. AI can help explain or critique, but the defect itself must be backed by a public, verifiable source.
