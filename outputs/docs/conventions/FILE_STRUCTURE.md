# FILE STRUCTURE

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the intended folder structure for HW01 working files, deliverables, evidence, and documentation.

Goals:

* Keep input materials separate from generated work
* Keep final deliverables separate from planning docs
* Make evidence easy to trace
* Support Git history and final submission
* Avoid losing required files near the deadline

---

## Top-Level Structure

```text
HW01-Jobs.Defects.PhysicalProduct/
    inputs/
    outputs/
    temp/
```

| Folder | Purpose |
| --- | --- |
| `inputs` | Assignment requirements, provided templates, and source materials |
| `outputs` | Student-created documentation, working notes, and deliverables |
| `temp` | Scratch work, experiments, drafts, and disposable generated files |

---

## Outputs Structure

```text
outputs/
    docs/
    deliverables/
```

| Folder | Purpose |
| --- | --- |
| `docs` | Internal guidance, templates, conventions, workflows, and notes |
| `deliverables` | Files intended to become part of the final submission or GitHub artifact set |

---

## Documentation Structure

```text
outputs/docs/
    ai/
    conventions/
    notes/
    references/
    templates/
    workflows/
```

| Folder | Purpose |
| --- | --- |
| `ai` | AI rules, audit guidance, project context, and review rules |
| `conventions` | Common project rules for names, statuses, commits, and structure |
| `notes` | Lightweight observations and working notes |
| `references` | Reference-management notes |
| `templates` | Reusable report and artifact templates |
| `workflows` | Step-by-step execution processes |

---

## Deliverables Structure

Recommended structure:

```text
outputs/deliverables/
    reports/
    appendix/
    references/
    github/
    mindmap/
    evidence/
    requirement_1_job_market/
    requirement_2_software_defects/
    requirement_3_physical_testing/
    submission_package/
```

| Folder | Purpose |
| --- | --- |
| `reports` | Main report Markdown and exported PDF |
| `appendix` | Prompt log, AI audit report, AI forms, and supporting appendices |
| `references` | Source lists and citation support |
| `github` | GitHub repository evidence, issue screenshots, and commit-log notes |
| `mindmap` | QA/QC role mindmap artifact |
| `evidence` | Screenshots, photos, videos, and proof files |
| `requirement_1_job_market` | Job posting analysis files |
| `requirement_2_software_defects` | Software defect analysis files |
| `requirement_3_physical_testing` | Physical-device test cases, execution notes, and defect notes |
| `submission_package` | Final zip-ready staging area |

---

## Evidence Structure

Recommended evidence subfolders:

```text
outputs/deliverables/evidence/
    job_posting_screenshots/
    software_defect_sources/
    device_photo/
    execution_videos/
    ai_conversation_screenshots/
    github_issue_screenshots/
```

Rules:

* Save evidence before referencing it in reports
* Link each evidence file to an artifact ID
* Keep original screenshots and photos unmodified when possible
* Do not store private or unrelated files in evidence folders
* Do not rely only on external links for required proof

---

## Temp Folder Rules

Use `temp` for:

* Draft text that will not be submitted
* Generated screenshots used only for review
* Scratch exports
* Experiments or discarded alternatives

Do not use `temp` for:

* Required evidence
* Final reports
* AI forms
* Prompt logs
* Submission packages

---

## Final Notes

The structure is ready only when every required HW01 artifact has an obvious destination before work starts. Evidence folders are especially important because HW01 grading depends on proof artifacts.
