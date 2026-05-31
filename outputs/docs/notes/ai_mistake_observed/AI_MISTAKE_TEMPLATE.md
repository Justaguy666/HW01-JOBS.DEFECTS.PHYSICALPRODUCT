# AI MISTAKE TEMPLATE

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: yes (12AM:09 31/05/2026 - Khoi Minh Nguyen)
ACCEPTED: yes (12AM:10 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the standard report template for one observed AI mistake, hallucination, weak reasoning pattern, or missed edge case.

Goals:

* Keep AI observations consistent
* Support traceability across prompts, evidence, and final artifacts
* Make human review and correction visible
* Provide material for the AI Audit Report, AI Critique, and oral defense
* Preserve evidence that AI output was not accepted without verification

---

## File Naming Format

```text
AI-OBS-XXX.md
```

Examples:

```text
AI-OBS-001.md
AI-OBS-002.md
AI-OBS-003.md
```

---

## Report Title

```markdown
# AI Observation Report: AI-OBS-XXX
```

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Observation ID | AI-OBS-XXX |
| Date observed | YYYY-MM-DD |
| Time observed | HH:MM |
| Observer | Student name / Student ID |
| AI tool | Tool name and version/model if known |
| Related requirement | R1 / R2 / R3 / AI compliance / Project organization |
| Related artifact | JOB-XXX / DEF-XXX / TC-XXX / EV-XXX / prompt_log / report section |
| Mistake type | HALLUCINATION / MISSED_EDGE_CASE / INCORRECT_REASONING / OVERGENERALIZATION / FALSE_ASSUMPTION / WEAK_SEVERITY_ANALYSIS / CONTEXT_IGNORANCE / FAKE_REFERENCE / SHALLOW_ANALYSIS / UNSAFE_SUGGESTION |
| Severity | LOW / MEDIUM / HIGH / CRITICAL |
| Status | TODO / REVIEWED / VERIFIED / RESOLVED |

---

## 2. Short Summary

Briefly describe the AI mistake in 1-3 sentences.

Example:

```text
The AI assumed that all device test cases could be evaluated without physical execution, but HW01 requires at least 5 real-device execution videos with student voice narration.
```

---

## 3. Original Prompt

Paste the exact prompt that produced the mistake.

```text
Prompt:
```

---

## 4. AI Output With Mistake

Paste the relevant AI output excerpt or link to the screenshot/evidence file.

```text
AI output:
```

Evidence file/link:

```text
EV-XXX or relative path
```

---

## 5. What Was Wrong

Explain why the output is incorrect, incomplete, biased, hallucinated, shallow, or unsafe.

Use concrete reasoning, not only a general statement.

Key issue:

```text
Describe the mistake clearly.
```

Why it matters:

```text
Explain the impact on the assignment, test quality, evidence quality, or AI compliance.
```

---

## 6. Verification Method

Describe how the mistake was detected and verified.

Relevant source checked:

```text
Assignment requirement / template / screenshot / real device behavior / trusted source
```

Verification result:

```text
State what the correct requirement or fact is.
```

---

## 7. Human Correction

Describe the corrected version or the human fix.

```text
Corrected content / corrected reasoning / corrected test case / corrected report wording:
```

Changed in artifact:

```text
JOB-XXX / DEF-XXX / TC-XXX / report section / appendix / prompt log
```

---

## 8. Traceability

| Trace item | ID or path |
| --- | --- |
| Prompt log entry | PROMPT-XXX / path |
| AI audit report entry | AUDIT-XXX / path |
| Evidence | EV-XXX / path |
| Related final artifact | JOB-XXX / DEF-XXX / TC-XXX / report section |
| Git commit | Commit hash or pending |

---

## 9. Lesson Learned

Write 2-5 sentences explaining what this mistake teaches about using AI for HW01.

```text
Lesson:
```

---

## 10. Oral Defense Note

Write a short explanation you could give if asked during oral defense.

```text
If asked, I will explain:
```

---

## 11. Status Checklist

* [ ] Mistake recorded in `AI_MISTAKES_INDEX.md`
* [ ] Prompt or screenshot evidence saved
* [ ] Correct requirement/source verified
* [ ] Human correction applied to related artifact
* [ ] AI audit report updated if needed
* [ ] Final report/appendix references updated if needed

---

## Final Notes

Each `AI-OBS-XXX.md` report should show that the AI output was checked, corrected, and connected back to concrete project artifacts.
