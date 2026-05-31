# AI AUDIT WORKFLOW

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document defines the workflow for AI logging, review, audit reporting, and mistake tracking in HW01.

Goals:

* Keep all AI use transparent
* Maintain a timestamped prompt log
* Review AI-generated artifacts before use
* Track mistakes as `AI-OBS-XXX`
* Prepare AI02, AI03, AI05, critique, and disclosure materials

---

## Required AI Compliance Artifacts

| Artifact | Required |
| --- | --- |
| Prompt log | yes |
| AI02 AI Audit Report | yes |
| AI03 AI Disclosure Form | yes |
| AI05 Privacy Checklist | yes |
| AI Critique, 200-300 words | yes |
| Mandatory Disclosure paragraph | yes |
| AI observations for mistakes | recommended and useful |

---

## Workflow

```text
Use AI
    ->
Record prompt and timestamp
    ->
Save AI output or screenshot
    ->
Review output manually
    ->
Accept, correct, or reject output
    ->
Create AI audit entry
    ->
Create AI-OBS entry if mistake found
    ->
Update final report disclosure
```

---

## Step 1 - Prompt Log

For each important AI interaction, record:

* Prompt ID
* Timestamp
* Tool/model
* Full prompt
* Summary of output
* Related artifact
* Whether the output was used

Recommended ID:

```text
PROMPT-XXX
```

---

## Step 2 - Audit Entry

For every AI-generated artifact or batch, record:

* Prompt and tool
* Full AI output or screenshot
* Verdict: VALID / INVALID / INCOMPLETE
* Reasoning grounded in source, course material, or requirements
* Student fix

---

## Step 3 - AI Observation

Create an `AI-OBS-XXX` when AI output contains:

* Hallucination
* Missed edge case
* False assumption
* Weak severity analysis
* Fabricated reference
* Shallow analysis
* Unsafe suggestion

Use:

```text
outputs/docs/notes/ai_mistake_observed/AI_MISTAKE_TEMPLATE.md
```

---

## Step 4 - AI Critique

Use AI observations and audit results to write a 200-300 word critique.

The critique should explain:

* Where AI helped
* Where AI failed
* Why AI failed
* How human review corrected the output
* When AI should and should not be used

---

## Step 5 - Disclosure

Before submission:

* [ ] Compare report claims to prompt log
* [ ] Confirm all AI-assisted sections are disclosed
* [ ] Confirm prohibited artifacts are not AI-generated
* [ ] Attach AI02, AI03, and AI05
* [ ] Include Mandatory Disclosure before appendices

---

## Final Notes

AI audit work should happen during the project, not after the report is finished. Retrofitting prompt logs and corrections at the end is risky and weakens traceability.
