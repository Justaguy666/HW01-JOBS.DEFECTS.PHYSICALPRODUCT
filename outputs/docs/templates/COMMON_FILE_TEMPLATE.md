# COMMON FILE TEMPLATE

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: no (pending human review)

ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines the common structure for HW01 Markdown files and Excel workbooks.

Goals:

* Keep `.md` and `.xlsx` artifacts consistent
* Map artifact fields back to the official homework requirements
* Preserve AI review and human acceptance status
* Make evidence, sources, and verification easy to audit
* Reduce final packaging mistakes

---

## Scope

Use this template for:

* Project documentation under `outputs/docs`
* Requirement deliverable Markdown files under `outputs/deliverables`
* Prompt logs and AI audit notes
* Excel workbooks used for test cases, test summaries, defect traceability, checklist, and self-assessment

Do not use this template to replace official forms from `inputs/ai-templates` or official spreadsheet templates from `inputs/testcase-templates`. When an official input template has a stricter layout, the official template wins and this document only adds consistency rules around naming, status, traceability, and review.

---

## Official Requirement Sources Compared

| Source | Requirement Extracted | Template Response |
| --- | --- | --- |
| `inputs/requirements/hw01-requirements.pdf` | Main HW01 requirements, grading rubric, AI audit rules, anti-cheat artifacts, submission contents | Defines required fields for R1, R2, R3, AI compliance, and submission files |
| `inputs/requirements/homeword-policies.pdf` | Markdown-first submissions, PDF copies, Git usage, clear commits, self-assessment, zip naming | Requires Markdown source, PDF export readiness, review status, and traceable artifact metadata |
| `inputs/testcase-templates/testcase-template.xls` | Test case/checklist workbook baseline | Defines workbook tabs and columns for test case execution data |
| `inputs/testcase-templates/testcase-checklist.xlsx` | Checklist workbook baseline | Defines checklist/status workbook conventions |
| `inputs/ai-templates/[AI-02]...` | AI Audit Report, 5-section artifact entry | Requires prompt, full AI output, verdict, reasoning, and student fix |
| `inputs/ai-templates/[AI-03]...` | Mandatory AI disclosure | Preserves a dedicated disclosure artifact and report section |
| `inputs/ai-templates/[AI-05]...` | Privacy and responsible use checklist | Preserves a signed checklist artifact and AI compliance evidence |

---

## Common Markdown Template

Every generated or maintained Markdown file should follow this baseline unless a more specific template applies.

```markdown
# <DOCUMENT OR ARTIFACT TITLE>

## Status

IS AI-GENERATED: YES/NO (<short note if needed>)

REVIEWED: yes/no (<time date - reviewer> or pending human review)

ACCEPTED: yes/no (<time date - reviewer> or pending human acceptance)

---

## Purpose

State why this file exists.

Goals:

* Goal 1
* Goal 2
* Goal 3

---

## Artifact Metadata

| Field | Value |
| --- | --- |
| Artifact ID | <JOB-001 / DEF-001 / TC-001 / PROMPT-001 / N/A> |
| Requirement | <R1 / R2 / R3 / AI / Submission / Governance> |
| Source file or link | <path or URL> |
| Evidence file or link | <path, URL, or N/A> |
| Owner | Khoi Minh Nguyen |
| Current status | DRAFT / REVIEWED / VERIFIED / FINAL |

---

## Main Content

Write the artifact content here.

---

## Verification Notes

| Check | Result |
| --- | --- |
| Compared with official requirement | yes/no |
| Source or evidence available | yes/no/N/A |
| AI-generated claims reviewed | yes/no/N/A |
| Ready for final report | yes/no |

---

## Final Notes

Record limitations, pending manual checks, or final submission notes.
```

---

## Markdown Variant Rules

| File Type | Required Sections | Requirement Link |
| --- | --- | --- |
| Project convention or workflow doc | Status, Purpose, rules/process, Final Notes | Supports Git, Markdown, review, and submission policy |
| Requirement 1 job artifact | Job metadata, source link, screenshot, job description, skills, salary, AI impact | R1 requires 10 jobs, screenshots, skills, salary, and AI impact |
| Requirement 2 defect artifact | Metadata, source link, description, severity, consequences, solution, AI bias/hallucination | R2 requires 20 defects and one AI issue per defect |
| Requirement 3 test case artifact | Metadata, objective, input, steps, expected, actual, verdict, evidence | R3 requires 15 test cases and execution evidence for at least 5 |
| Requirement 3 edge case note | AI prompt/screenshot, missed edge case explanation, linked test case | R3 requires at least 3 AI-missed edge cases with screenshot and explanation |
| Prompt log | Prompt metadata, prompt, full response, response time, project effects, description | AI policy requires prompt log with timestamps for every AI prompt |
| AI audit entry | Prompt/tool, full AI output, verdict, reasoning, student fix | AI-02 requires 5-section audit entry per AI-generated artifact |
| Report file | Student info, R1, R2, R3, AI critique, disclosure, self-assessment, appendices | Submission requires main report PDF and AI compliance sections |

---

## Common XLSX Workbook Template

Every HW01 workbook should be structured for review first, then data entry.

Recommended workbook tabs:

| Sheet | Purpose | Required When |
| --- | --- | --- |
| `status` | Workbook ownership, review status, requirement mapping, update history | All generated `.xlsx` files |
| `data` | Main editable rows | Workbooks that collect jobs, defects, test cases, or checklist items |
| `summary` | Compact report-ready summary table | Workbooks referenced from the main report |
| `traceability` | Links from rows to evidence, source, prompt, report section, or GitHub issue | Workbooks with evidence or multiple artifacts |
| `review` | Manual checks, unresolved issues, final acceptance status | Workbooks that will be submitted or exported |

Do not add unnecessary sheets. A small workbook may combine `data` and `summary` if the official template expects one worksheet.

---

## Common XLSX Status Sheet

Minimum fields for a `status` sheet:

| Field | Value |
| --- | --- |
| Workbook title |  |
| Requirement | R1 / R2 / R3 / AI / Submission |
| Source template | `inputs/testcase-templates/...` or N/A |
| IS AI-GENERATED | YES/NO |
| REVIEWED | yes/no |
| ACCEPTED | yes/no |
| Owner | Khoi Minh Nguyen |
| Last updated | HHAMMM DD/MM/YYYY |
| Ready for report | yes/no |
| Notes |  |

Rules:

* Freeze the header row on every data sheet
* Use filters for editable tables
* Keep one artifact per row when possible
* Use stable IDs such as `JOB-001`, `DEF-001`, `TC-001`, and `EV-001`
* Use `Not available` only when the source truly does not provide the value
* Do not hide source, evidence, or review columns
* Copy final summary tables into the Markdown report, as required by the homework policies

---

## Workbook-Specific Column Templates

### `self_assessment.xlsx`

| Column | Requirement |
| --- | --- |
| No. | Rubric item number such as `1`, `2`, `3`, `AI-1`, `AI-2`, `AI-3`, `Total` |
| Criteria | Official rubric text |
| Grade | Official maximum points |
| Self-Assessed Grade | Student score |

This workbook must match the official 100-point rubric:

* Job Market 2026+: 40
* Software Defects 2022-2026: 20
* Physical-product test design: 25
* AI-02 Audit Report: 8
* AI Critique and AI-03 Disclosure: 4
* AI-05 Checklist and anti-cheat artifacts: 3

### `test_cases.xlsx`

| Column | Requirement |
| --- | --- |
| TC ID | `TC-001` through `TC-015` |
| Objective | What behavior or risk is tested |
| Input | Test input, condition, or setup |
| Steps | Executable physical-device steps |
| Expected Result | Observable expected outcome |
| Actual Result | Filled after execution |
| Verdict | PASS / FAIL / BLOCKED / NOT_RUN |
| Edge Case AI Missed | yes/no |
| Evidence | Video, screenshot, or note link |
| GitHub Issue | Required if a defect is logged |

### `test_summary_report.xlsx`

| Column | Requirement |
| --- | --- |
| TC ID | Linked test case |
| Executed | yes/no |
| Video Link | YouTube unlisted URL or approved alternative |
| Voice Narration Included | yes/no |
| Result | PASS / FAIL / BLOCKED |
| Defect Found | yes/no |
| Notes | Concise execution note |

### `defect_traceability.xlsx`

| Column | Requirement |
| --- | --- |
| Defect ID | `DEF-R3-001` through `DEF-R3-005` or more |
| Related TC ID | Test case that found the defect |
| GitHub Issue Link | Required when logged |
| Screenshot Evidence | Path or evidence ID |
| Video Evidence | URL or evidence ID |
| Severity | LOW / MEDIUM / HIGH / CRITICAL |
| Status | OPEN / CONFIRMED / RESOLVED / CLOSED |

### Checklist Workbook

| Column | Requirement |
| --- | --- |
| Checklist ID | Stable row ID |
| Requirement | R1 / R2 / R3 / AI / Submission |
| Check Item | What must be verified |
| Evidence | Path, URL, or N/A |
| Status | TODO / DRAFT / REVIEWED / VERIFIED / FINAL |
| Reviewer | Human reviewer |
| Notes | Remaining issue or acceptance note |

When using `inputs/testcase-templates/testcase-checklist.xlsx`, preserve the official review markers:

| Marker | Meaning |
| --- | --- |
| `x` | problem |
| `o` | ok |
| `i` | ignore |

The checklist should keep the provided quality focus areas visible, especially:

* Accurate
* Economical
* Repeatable and self-standing
* Appropriate for future testers
* Traceable to requirements
* Self-cleaning after execution
* Named and numbered
* Clear setup, actions, expected results, and proof/evidence needs
* Active case language
* No more than 15 steps where the checklist requires it
* Naming, numbering, versioning, storage, and access control

---

## Requirement Coverage Matrix

| Homework Requirement | Required Artifact | Markdown Template Coverage | XLSX Template Coverage | Ready Condition |
| --- | --- | --- | --- | --- |
| R1: 10 QA/QC jobs within 60 days | `job_01` through `job_10`, screenshot evidence | Job metadata, source, description, skills, salary, AI impact | Optional summary table if needed | 10 jobs verified, at least 3 AI-related, screenshots show account name |
| R2: 20 public software defects from 2022-2026 | `def_01` through `def_20` analyses | Defect metadata, description, severity, consequences, solution, AI issue | Optional defect summary or traceability workbook | 20 sourced defects, at least 5 AI/LLM-related, one AI issue per defect |
| R3: One physical product | `device_info.md`, device photo | Device metadata and photo reference | Optional device row in summary workbook | Brand, model, year, masked serial number, device plus student ID photo |
| R3: 15 test cases | `tc_001.md` through `tc_015.md` | Objective, input, steps, expected, actual, verdict | `test_cases.xlsx` | 15 executable physical-device test cases |
| R3: At least 5 videos | YouTube links and execution notes | Video evidence references in test cases | `test_summary_report.xlsx` | At least 5 executed tests with voice narration links |
| R3: At least 3 AI-missed edge cases | `ec_001` and related notes | Screenshot and explanation for AI miss | Edge-case column in `test_cases.xlsx` | Conversation screenshot plus written explanation |
| R3: Physical defects | `def_r3_001.md` and GitHub issue evidence | Defect notes and issue links | `defect_traceability.xlsx` | GitHub issue evidence, screenshot, traceability |
| AI Audit Report | AI-02 appendix | Prompt, full output, verdict, reasoning, student fix | Optional audit index | 5-section entry per AI-generated artifact |
| AI Critique | 200-300 word report section | Dedicated critique template | N/A | Word count and concrete critique of AI limitations |
| AI Disclosure | AI-03 appendix and report paragraph | Disclosure template | N/A | Signed or completed disclosure attached |
| AI Privacy Checklist | AI-05 appendix | Checklist reference | Checklist workbook if used | Signed checklist and anti-cheat artifacts available |
| Prompt log | `outputs/docs/ai/prompts/*.md` and appendix prompt log | Prompt metadata, prompt, response, effects | Optional audit index | Every prompt has timestamp and full response |
| Submission package | PDF, Markdown, Excel, evidence, links | Report and appendix templates | Workbook templates | Zip named `StudentID_HW01_AI_<grade>.zip` |

---

## Review Checklist

Before marking a file accepted:

* [ ] File follows the naming convention used in its folder
* [ ] Status block is accurate
* [ ] Artifact ID is stable and traceable
* [ ] Requirement number is clear
* [ ] Source or evidence is linked where required
* [ ] AI-generated content is identified
* [ ] Unsupported claims are removed or marked uncertain
* [ ] Excel summaries are copied into Markdown where required
* [ ] Final report can reference the artifact without guessing
* [ ] Anti-cheat evidence is not AI-generated

---

## Final Notes

This common template is a control layer. It standardizes review, traceability, and requirement coverage, but it does not replace the detailed templates for jobs, defects, test cases, AI audit reports, or official input forms.
