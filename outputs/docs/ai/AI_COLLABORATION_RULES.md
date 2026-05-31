# AI COLLABORATION RULES

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines how AI tools may be used during HW01 while keeping the work transparent, reviewable, and compliant.

Goals:

* Use AI as support, not as final authority
* Preserve prompt and output evidence
* Make human review visible
* Prevent fabricated or unsupported claims
* Support AI audit, critique, and oral defense

---

## Allowed AI Uses

AI may be used for:

* Brainstorming QA/QC job-market analysis angles
* Drafting first-pass job impact analysis
* Explaining public software defects for review
* Suggesting physical-product test ideas
* Helping identify possible edge cases
* Reviewing report structure
* Drafting templates or checklists
* Improving clarity after facts are verified

---

## Restricted AI Uses

AI must not be used to generate or fake:

* Device photo with student ID card
* Execution videos with student voice narration
* Job-posting screenshots with account/login name
* Prompt log timestamps
* Real-world evidence that must be personally produced
* Fabricated citations, sources, salaries, dates, or defect facts

---

## Required Human Responsibilities

The student must:

* Verify all facts from sources
* Execute physical-product tests personally
* Capture required evidence personally
* Decide final severity, verdict, and conclusions
* Correct AI-generated mistakes
* Document AI use in prompt log and audit report
* Explain decisions during oral defense

---

## Prompting Rules

Good prompts should include:

* Assignment requirement being addressed
* Current artifact ID
* Constraints from HW01
* Expected output format
* Request for uncertainty or assumptions
* Request to avoid fabricating facts

Example:

```text
For HW01 Requirement 3, I am testing DEV-001, a specific household device. Suggest possible test ideas, but do not invent device facts. Mark which ideas need real execution evidence and which are edge cases.
```

---

## Review Rules

Every important AI output should be classified:

| Verdict | Meaning |
| --- | --- |
| VALID | Correct after review and can be used |
| INVALID | Wrong or unusable |
| INCOMPLETE | Partly useful but needs correction |

If an AI mistake matters, create an `AI-OBS-XXX` report.

---

## Traceability Rules

AI-assisted work should connect:

```text
PROMPT-XXX
    ->
AI output
    ->
Human review
    ->
Student correction
    ->
Final artifact
```

---

## Final Notes

The safest AI collaboration pattern is to ask AI for drafts and alternatives, then use human review, real evidence, and official requirements to decide what is true.
