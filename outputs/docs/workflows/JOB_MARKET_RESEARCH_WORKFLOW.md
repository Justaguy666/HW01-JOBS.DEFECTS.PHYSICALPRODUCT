# JOB MARKET RESEARCH WORKFLOW

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: yes (12AM:40 31/05/2026 - Khoi Minh Nguyen)
ACCEPTED: yes (12AM:44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the workflow for Requirement 1, QA/QC Job Market 2026+.

Goals:

* Find 10 valid QA/QC job postings
* Ensure postings are recent enough
* Capture required screenshot evidence
* Identify AI/LLM/automation-AI roles
* Produce consistent `JOB-XXX` analyses

---

## Requirement Summary

Requirement 1 needs:

* 10 QA/QC job postings
* Postings published within 60 days of submission date
* At least 3 positions requiring AI, LLM, or automation-AI skills
* Link, dated screenshot, job description, required skills, and salary for each posting
* AI Impact Analysis for each posting
* Screenshot must show account/login name

---

## Workflow

```text
Search job platforms
    ->
Screen for date and relevance
    ->
Capture screenshot evidence
    ->
Extract job details
    ->
Write JOB-XXX analysis
    ->
Review AI impact claims
    ->
Update report summary table
```

---

## Step 1 - Search

Recommended search targets:

* LinkedIn
* Indeed
* Company career pages
* VietnamWorks or similar local job boards
* Remote job boards if role details are complete

Search terms:

```text
QA Engineer
QC Engineer
Software Tester
Test Automation Engineer
Manual Tester
AI testing
LLM evaluation
QA automation AI
```

---

## Step 2 - Validate Posting

For each candidate:

* [ ] Role is QA/QC/testing related
* [ ] Posting date is visible or defensible
* [ ] Posting date is within 60 days of submission
* [ ] Job details are accessible
* [ ] Screenshot can show login/account name
* [ ] AI-related status is marked yes/no

---

## Step 3 - Save Evidence

Recommended evidence:

```text
EV-XXX_JOB-XXX_<platform>_<date>.png
```

Screenshot must show:

* Job title
* Company or platform context
* Posting date when possible
* Account/login name in the corner

---

## Step 4 - Write Analysis

Use:

```text
outputs/docs/templates/JOB_POSTING_TEMPLATE.md
```

Each `JOB-XXX` should include:

* Metadata
* Source and evidence
* Job description
* Required skills
* Salary or "Not listed"
* AI Impact Analysis
* Verification notes

---

## Step 5 - Review

Review questions:

* [ ] Did I invent any missing salary or date information?
* [ ] Does the screenshot satisfy anti-cheat requirements?
* [ ] Is the AI impact analysis role-specific?
* [ ] Are at least 3 postings AI-related?
* [ ] Can I explain why this role counts as QA/QC?

---

## Final Notes

Capture screenshots early. Job postings can change or disappear, and missing screenshot evidence can invalidate an otherwise good analysis.
