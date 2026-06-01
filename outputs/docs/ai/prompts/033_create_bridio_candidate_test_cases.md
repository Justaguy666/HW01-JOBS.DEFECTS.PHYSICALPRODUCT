# PROMPT LOG 033 - CREATE BRIDIO CANDIDATE TEST CASES

## Status

IS AI-GENERATED: YES (Codex-assisted prompt log)

REVIEWED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

ACCEPTED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

---

## Prompt Metadata

| Field | Value |
| --- | --- |
| Prompt ID | PROMPT-033 |
| Prompt file | `033_create_bridio_candidate_test_cases.md` |
| Original timestamp | 9PM41 01/06/2026 |
| Log timestamp | 9PM41 01/06/2026 |
| Prompter | Khoi Minh Nguyen |
| Responder | Codex |
| Tool | Codex |
| Related area | Requirement 3 candidate test cases |
| Verdict | VALID |

---

## Prompt

```text
no, don't decide what testcases will be apply, create a candidate_test_cases sheet in test_cases.xlsx file, I will choose what testcases will be apply
```

---

## Response

Added a separate `candidate_test_cases` sheet to:

```text
outputs/deliverables/requirement_3_physical_testing/test_cases/test_cases.xlsx
```

The existing official `test_cases` sheet was preserved and still contains only placeholder rows for `TC-001` through `TC-015`. No test case was selected or applied into the official test-case set.

The new candidate sheet contains 85 candidate test cases for the BRIDIO TH10 wireless headset across these areas:

* Identity and setup
* Bluetooth connectivity
* Audio playback
* Microphone and calls
* AUX wired mode
* Controls and indicators
* Charging and power
* Physical and ergonomic testing
* Environmental and safety testing

Columns added:

```text
Area
Candidate Test Case
Focus
Suggested Method
Expected Observation
Reason To Test
Edge Case Candidate
```

Verification completed:

* Workbook imports successfully
* `candidate_test_cases` sheet exists
* Candidate table range is `A1:G86`
* Formula error scan found no `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or `#N/A`
* The candidate sheet renders successfully

---

## Response Time

Not measured by Codex. This log was created in the same turn as the candidate test-case workbook update.

---

## Project Effects

Updated:

```text
outputs/deliverables/requirement_3_physical_testing/test_cases/test_cases.xlsx
```

Created:

```text
outputs/docs/ai/prompts/033_create_bridio_candidate_test_cases.md
```

---

## Description

This prompt corrected the workflow by separating candidate test-case ideation from final test-case selection. The candidate list is available for human selection before any `TC-XXX` files or official test-case rows are filled.

---

## Final Notes

The candidate test cases are draft ideas only. Human review is required before selecting the final 15 Requirement 3 test cases.
