# EVIDENCE RULES

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM:59 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (01PM:10 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines how evidence should be captured, named, stored, reviewed, and referenced for HW01.

Goals:

* Keep proof artifacts organized
* Satisfy anti-cheat requirements
* Make report claims traceable
* Prevent reliance on broken external links
* Support oral defense and final grading

---

## Evidence Types

| Evidence Type | Requirement | Example ID |
| --- | --- | --- |
| Job posting screenshot | R1 | EV-001 |
| Defect source screenshot or saved source note | R2 | EV-020 |
| Device photo with student ID | R3 | EV-040 |
| Execution video note or link | R3 | EV-050 |
| AI conversation screenshot | AI/R3 | EV-060 |
| GitHub issue screenshot | R3 | EV-070 |
| Prompt log | AI | PROMPT-XXX |

---

## Evidence Storage

Recommended structure:

```text
outputs/deliverables/evidence/
    job_posting_screenshots/
    software_defect_sources/
    device_photo/
    execution_videos/
    ai_conversation_screenshots/
    github_issue_screenshots/
```

If evidence is stored inside requirement folders instead, it must still be traceable by ID.

---

## Evidence Naming Pattern

Recommended:

```text
EV-XXX_<related-id>_<short_description>.<ext>
```

Examples:

```text
EV-001_JOB-001_linkedin_2026-05-31.png
EV-040_DEV-001_device_student_id.jpg
EV-050_TC-003_execution_video.md
EV-070_GH-ISSUE-002_issue_page.png
```

---

## Capture Rules

Job posting screenshots must show:

* Job title
* Platform or company context
* Posting date when possible
* Student login/account name

Device photo must show:

* Actual physical device
* Student ID card in the same frame
* Enough visual clarity to identify the device

Execution videos must include:

* Real device execution
* Student voice narration
* Test case being demonstrated
* Duration of 60 seconds or less when possible

---

## Evidence Review Status

| Status | Meaning |
| --- | --- |
| MISSING | Required evidence not collected |
| CAPTURED | File or link exists |
| LINKED | Referenced from report or index |
| VERIFIED | Satisfies the assignment requirement |
| REJECTED | Unusable or non-compliant |

---

## Evidence Index Fields

Recommended evidence index columns:

| Field | Meaning |
| --- | --- |
| Evidence ID | EV-XXX |
| Related artifact | JOB-XXX / DEF-XXX / TC-XXX / AI-OBS-XXX |
| File path or URL | Location |
| Evidence type | Screenshot / Photo / Video / Source / Prompt |
| Status | MISSING / CAPTURED / LINKED / VERIFIED / REJECTED |
| Notes | Short review note |

---

## External Link Rules

* Prefer local screenshots for required proof
* Use external links for video hosting when required
* Check that video links open before submission
* Do not rely only on a job posting URL because postings may disappear
* Do not include private or unrelated files in evidence folders

---

## Final Notes

Evidence is not decoration. In HW01, evidence proves that the work was done personally and that claims in the report are verifiable.
