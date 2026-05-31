# NAMING CONVENTIONS

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines file, folder, and artifact naming conventions for HW01.

Goals:

* Keep deliverables easy to scan
* Preserve traceability between report sections and evidence
* Avoid ambiguous file names
* Support Git commits and oral defense
* Reduce final packaging mistakes

---

## General Naming Rules

* Use lowercase folder names
* Use uppercase prefixes for tracked artifact IDs
* Use underscores for long descriptive file names
* Use hyphens only inside formal IDs such as `AI-OBS-001`
* Avoid spaces in filenames
* Avoid vague names such as `final`, `new`, `updated`, or `screenshot1`
* Include an ID when the file supports a tracked artifact
* Keep names stable after linking them in reports or indexes

---

## Artifact ID Prefixes

| Prefix | Meaning | Example |
| --- | --- | --- |
| `JOB` | Requirement 1 job posting | `JOB-001` |
| `DEF` | Requirement 2 software defect | `DEF-001` |
| `TC` | Requirement 3 test case | `TC-001` |
| `DEV` | Physical device profile | `DEV-001` |
| `EV` | Evidence artifact | `EV-001` |
| `PROMPT` | Prompt log entry | `PROMPT-001` |
| `AUDIT` | AI audit entry | `AUDIT-001` |
| `AI-OBS` | AI mistake observation | `AI-OBS-001` |

---

## File Naming Patterns

| File Type | Pattern | Example |
| --- | --- | --- |
| Job analysis | `JOB-XXX_<platform>_<role>.md` | `JOB-001_linkedin_qa_engineer.md` |
| Job screenshot | `EV-XXX_JOB-XXX_<platform>_<date>.png` | `EV-001_JOB-001_linkedin_2026-05-31.png` |
| Defect analysis | `DEF-XXX_<product_or_company>_<short_issue>.md` | `DEF-004_openai_prompt_injection.md` |
| Test case | `TC-XXX_<short_title>.md` | `TC-005_rapid_power_reconnect.md` |
| Device photo | `EV-XXX_DEV-001_device_student_id.jpg` | `EV-030_DEV-001_device_student_id.jpg` |
| Execution video note | `EV-XXX_TC-XXX_execution_video.md` | `EV-041_TC-003_execution_video.md` |
| AI observation | `AI-OBS-XXX.md` | `AI-OBS-002.md` |
| Prompt log | `prompt_log.md` | `prompt_log.md` |

---

## Folder Naming Rules

| Folder | Purpose |
| --- | --- |
| `requirement_1_job_market` | Job posting research and analysis |
| `requirement_2_software_defects` | Public software defect analysis |
| `requirement_3_physical_testing` | Physical-device test design and execution |
| `evidence` | Screenshots, photos, videos, and proof artifacts |
| `appendix` | AI forms, prompt log, and supporting appendices |
| `reports` | Main report drafts and final exports |
| `submission_package` | Final zip-ready package |

---

## Date Format

Use ISO date format in filenames when a date is useful:

```text
YYYY-MM-DD
```

Example:

```text
EV-012_JOB-006_indeed_2026-05-31.png
```

---

## Final Package Naming

Final Moodle package:

```text
StudentID_HW01_AI_<grade>.zip
```

Example:

```text
23123456_HW01_AI_095.zip
```

---

## Final Notes

Names should make artifacts understandable without opening them. If a file cannot be traced from its name, add an index entry or rename it before final packaging.
