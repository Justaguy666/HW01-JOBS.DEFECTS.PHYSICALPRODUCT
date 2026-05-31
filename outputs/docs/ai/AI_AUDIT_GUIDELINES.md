# AI AUDIT GUIDELINES

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM:59 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (01PM:10 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines how to prepare AI audit materials for HW01.

Goals:

* Record AI-generated artifacts clearly
* Preserve prompts and outputs
* Explain human review decisions
* Track corrections and AI mistakes
* Support required AI02, AI03, AI05, critique, and disclosure artifacts

---

## What Counts As An AI-Generated Artifact

An AI-generated artifact may be:

* A batch of test cases
* A job analysis draft
* A defect explanation draft
* A checklist
* A report outline
* A rewritten paragraph
* A generated table or summary

One prompt that generates a batch can count as one audit entry, if the batch is reviewed together.

---

## AI Audit Entry Fields

Each audit entry should include:

| Section | Required Content |
| --- | --- |
| Prompt and tool | Full prompt, tool/model, timestamp |
| AI output | Full output or screenshot with label |
| Verdict | VALID / INVALID / INCOMPLETE |
| Reasoning | Why the verdict is justified |
| Student fix | Corrected or revised version |

---

## Prompt Log Rules

For every important prompt, record:

* Prompt ID
* Timestamp
* AI tool
* Full prompt text
* Output location or screenshot
* Related artifact ID
* Whether the output was accepted, rejected, or corrected

Recommended ID:

```text
PROMPT-XXX
```

---

## AI Observation Rules

Use `AI-OBS-XXX` reports for important AI mistakes.

Examples:

```text
AI-OBS-001 false readiness assumption
AI-OBS-002 missed physical-device edge case
AI-OBS-003 hallucinated defect source
```

Each observation should link back to:

* Prompt log entry
* AI output
* Human correction
* Related artifact
* Evidence or official requirement

---

## Accuracy Summary

At the end of the AI Audit Report, summarize:

| Verdict | Count | Percentage |
| --- | --- | --- |
| VALID | | |
| INVALID | | |
| INCOMPLETE | | |
| Total | | 100% |

---

## Final AI Use Conclusion

The conclusion should answer:

* When was AI useful?
* When was AI unreliable?
* What tasks required human judgment?
* What evidence could not be AI-generated?
* How should AI be used in future testing work?

---

## Final Notes

The AI audit is not just paperwork. It proves that AI output was reviewed, corrected, and controlled by the student.
