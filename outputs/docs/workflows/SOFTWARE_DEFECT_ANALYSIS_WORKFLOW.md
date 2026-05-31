# SOFTWARE DEFECT ANALYSIS WORKFLOW

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the workflow for Requirement 2, 20 software defects publicized from 2022-2026.

Goals:

* Select 20 valid public software defects
* Include at least 5 AI/LLM related defects
* Record severity, consequences, and solution
* Identify one AI bias or hallucination per defect
* Keep all `DEF-XXX` entries source-backed

---

## Requirement Summary

Requirement 2 needs:

* 20 software defects publicized between 2022 and 2026
* At least 5 defects related to AI/LLM
* Source link for each defect
* Description, severity, consequences, and solution
* One AI bias or hallucination found in AI explanation for every defect

---

## Workflow

```text
Build defect candidate list
    ->
Validate year and source
    ->
Ask AI to explain or analyze
    ->
Check AI explanation for bias/hallucination
    ->
Write DEF-XXX analysis
    ->
Verify severity and solution
    ->
Update report summary
```

---

## Step 1 - Select Defects

Candidate sources:

* Public incident reports
* Vendor postmortems
* News articles
* Security advisories
* Court or regulator reports
* Research writeups

Selection rules:

* [ ] Publicized between 2022 and 2026
* [ ] Software-related defect or failure
* [ ] Source is verifiable
* [ ] Consequences are identifiable
* [ ] Solution or mitigation can be described

---

## Step 2 - Classify AI Relation

Mark a defect as AI/LLM related only when the defect directly involves:

* Hallucination
* Prompt injection
* Model bias
* Unsafe automated decision
* LLM or chatbot failure
* AI-generated false information
* AI system evaluation or guardrail failure

---

## Step 3 - Analyze AI Explanation

For each defect:

* Ask AI to explain the defect
* Compare the AI explanation against the trusted source
* Identify one bias, hallucination, missing context, or weak reasoning issue
* Create or reference an `AI-OBS-XXX` entry if useful

---

## Step 4 - Write DEF Entry

Use:

```text
outputs/docs/templates/SOFTWARE_DEFECT_ANALYSIS_TEMPLATE.md
```

Each entry should include:

* Metadata
* Source information
* Description
* Severity analysis
* Consequences
* Solution or mitigation
* AI bias or hallucination found
* Report-ready summary

---

## Step 5 - Review

Review questions:

* [ ] Is the defect public and verifiable?
* [ ] Is the date between 2022 and 2026?
* [ ] Is the severity justified by evidence?
* [ ] Are consequences specific?
* [ ] Is the solution real or reasonably inferred from the source?
* [ ] Is the AI hallucination/bias concrete?

---

## Final Notes

Do not let AI become the source of truth for defects. AI is useful for critique, but final facts must come from public sources.
