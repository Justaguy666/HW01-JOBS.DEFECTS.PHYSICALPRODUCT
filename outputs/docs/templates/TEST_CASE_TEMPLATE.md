# TEST CASE TEMPLATE

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines the template for one Requirement 3 physical-product test case.

Goals:

* Keep all 15 test cases consistent
* Support execution and video evidence tracking
* Distinguish AI-suggested cases from human-added edge cases
* Record expected, actual, and verdict clearly
* Support GitHub defect issue creation when failures are found

---

## File Naming Format

```text
TC-XXX_<short_title>.md
```

Example:

```text
TC-005_rapid_power_reconnect.md
```

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Test case ID | TC-XXX |
| Title |  |
| Requirement | R3 |
| Product ID | DEV-001 |
| AI-generated draft | yes/no |
| AI missed edge case | yes/no |
| Status | DRAFT / REVIEWED / VERIFIED / FINAL |
| Execution status | NOT_RUN / PASS / FAIL / BLOCKED |

---

## 2. Objective

```text
State what behavior, risk, or quality attribute this test case checks.
```

---

## 3. Preconditions

```text
Device state, environment, setup, safety condition, input state, or required tools.
```

---

## 4. Test Data And Inputs

| Input | Value |
| --- | --- |
|  |  |

---

## 5. Steps

| Step | Action |
| --- | --- |
| 1 |  |
| 2 |  |
| 3 |  |

---

## 6. Expected Result

```text
State the expected observable outcome.
```

---

## 7. Actual Result

```text
Fill this after execution. If not executed, write NOT_RUN.
```

---

## 8. Verdict

| Field | Value |
| --- | --- |
| Verdict | PASS / FAIL / BLOCKED / NOT_RUN |
| Defect found | yes/no |
| GitHub issue | URL or N/A |
| Evidence ID | EV-XXX or N/A |
| Video evidence | EV-XXX / URL / N/A |

---

## 9. AI Missed Edge Case Evidence

Fill this section only if this test case is one of the at least 3 edge cases AI did not find.

| Field | Value |
| --- | --- |
| AI prompt ID | PROMPT-XXX |
| AI conversation screenshot | EV-XXX |
| Written explanation |  |

---

## 10. Notes

```text
Execution notes, safety notes, repeatability issues, or follow-up checks.
```

---

## Final Notes

A good physical-product test case must be executable on the real device and must produce observable evidence. Do not mark a test as passed without actual execution when the report says it was executed.
