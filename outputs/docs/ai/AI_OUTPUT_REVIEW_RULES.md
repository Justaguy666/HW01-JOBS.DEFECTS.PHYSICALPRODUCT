# AI OUTPUT REVIEW RULES

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines the review process for AI-generated outputs used in HW01.

Goals:

* Prevent unverified AI output from entering final deliverables
* Identify hallucinations, omissions, and weak reasoning
* Create a repeatable human review process
* Support AI Audit Report entries
* Provide evidence for the AI Critique

---

## Review Verdicts

| Verdict | Meaning | Action |
| --- | --- | --- |
| VALID | Correct and complete after checking | Use with citation or traceability |
| INVALID | Wrong, unsupported, or unsafe | Reject and document if important |
| INCOMPLETE | Partly useful but missing key parts | Correct before use |

---

## Common AI Mistakes

| Mistake Type | Example |
| --- | --- |
| HALLUCINATION | Invents a source, salary, date, or defect detail |
| MISSED_EDGE_CASE | Fails to suggest realistic boundary or stress scenario |
| FALSE_ASSUMPTION | Assumes folder/file state without checking |
| OVERGENERALIZATION | Gives generic QA advice instead of role-specific analysis |
| WEAK_SEVERITY_ANALYSIS | Labels a defect critical without impact evidence |
| CONTEXT_IGNORANCE | Ignores anti-cheat or evidence requirements |
| FAKE_REFERENCE | Provides unverifiable references |
| UNSAFE_SUGGESTION | Suggests risky physical-device testing |

---

## Review Checklist

For each important AI output:

* [ ] Does it answer the actual prompt?
* [ ] Does it follow HW01 requirements?
* [ ] Are all facts source-backed?
* [ ] Are dates, counts, and thresholds correct?
* [ ] Does it avoid invented evidence?
* [ ] Does it separate assumptions from facts?
* [ ] Does it miss required edge cases?
* [ ] Does it need an AI observation report?

---

## Source Verification

Use direct evidence when possible:

* Official assignment PDF
* Job posting page and screenshot
* Public incident or defect source
* Device behavior observed during execution
* GitHub issue or repository evidence
* AI prompt log and screenshots

Do not use AI-generated text as the only source for factual claims.

---

## Correction Process

```text
AI output
    ->
Human review
    ->
Find issue
    ->
Verify against source or evidence
    ->
Correct artifact
    ->
Record audit entry
    ->
Create AI-OBS if needed
```

---

## When To Create AI-OBS

Create an `AI-OBS-XXX` report when:

* The AI mistake affects a deliverable
* The mistake shows a useful limitation for the critique
* The mistake could mislead final analysis
* The mistake relates to an AI-missed edge case
* The mistake needs traceability for oral defense

---

## Final Notes

AI output is not final work. The final work begins after review, correction, evidence checking, and traceability.
