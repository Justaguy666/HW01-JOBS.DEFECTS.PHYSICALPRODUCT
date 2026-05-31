# STATUS CONVENTIONS

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines status labels used across HW01 documentation, deliverables, evidence, and AI observations.

Goals:

* Make progress visible
* Avoid treating drafts as final
* Distinguish AI-assisted content from human-verified content
* Support traceability and oral defense
* Keep indexes and reports consistent

---

## Document Review Status

Use this block near the top of project documentation files:

```text
IS AI-GENERATED: YES/NO
REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)
ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)
```

Rules:

* Use `IS AI-GENERATED: YES` for AI-assisted drafts or AI-assisted edits
* Use `REVIEWED: yes` only after a human reads and checks the file
* Use `ACCEPTED: yes` only after the file is approved for use
* Include reviewer name when marking reviewed or accepted
* Do not mark generated content as accepted without human review

---

## Artifact Status Values

| Status | Meaning | Use For |
| --- | --- | --- |
| TODO | Planned but not started | Missing work items |
| DRAFT | Started but incomplete | Early written content |
| IN_PROGRESS | Active work is happening | Research, testing, report writing |
| REVIEWED | Human review completed | AI outputs, analyses, templates |
| VERIFIED | Checked against source/evidence | Requirements, facts, screenshots, videos |
| RESOLVED | Correction or issue has been handled | AI mistakes, defects, checklist items |
| FINAL | Ready for submission | Report, appendix, final package |

---

## Evidence Status Values

| Status | Meaning |
| --- | --- |
| MISSING | Evidence has not been collected |
| CAPTURED | Evidence file exists |
| LINKED | Evidence is referenced from a report or index |
| VERIFIED | Evidence satisfies the assignment condition |
| REJECTED | Evidence is unusable and should not be submitted |

---

## AI Observation Status Values

| Status | Meaning |
| --- | --- |
| TODO | Observation is created but not analyzed |
| REVIEWED | Human reviewed the AI mistake |
| VERIFIED | Mistake is confirmed against a requirement or source |
| RESOLVED | Correction is integrated into the related artifact |

---

## Recommended Workflow

```text
TODO
    ->
DRAFT
    ->
REVIEWED
    ->
VERIFIED
    ->
FINAL
```

For mistakes:

```text
TODO
    ->
REVIEWED
    ->
VERIFIED
    ->
RESOLVED
```

---

## Status Update Rules

* Update status only after the required check is complete
* Prefer `VERIFIED` over vague words like "done"
* Keep status values uppercase in tables
* Do not mix multiple statuses in one field
* Use notes when a status needs explanation
* If evidence fails a requirement, mark it `REJECTED` and capture the replacement plan

---

## Final Notes

Status labels are part of the audit trail. They should reflect the real state of work, not the intended or hoped-for state.
