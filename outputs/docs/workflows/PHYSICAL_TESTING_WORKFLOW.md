# PHYSICAL TESTING WORKFLOW

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines the workflow for Requirement 3, designing and executing test cases for one physical product.

Goals:

* Select a specific household device
* Design 15 test cases
* Execute and record at least 5 test cases
* Identify at least 3 edge cases AI did not find
* Preserve device, video, and defect evidence

---

## Requirement Summary

Requirement 3 needs:

* One specific physical product
* One photo showing the device and student ID card in the same frame
* Brand, model, year, and masked serial number
* 15 total test cases
* At least 5 executed test cases
* At least 5 short videos, each 60 seconds or less
* Videos with student voice narration
* At least 3 AI-missed edge cases
* Aim to find at least 5 physical-device defects

---

## Workflow

```text
Select device
    ->
Capture device identity evidence
    ->
Ask AI for draft test ideas
    ->
Find human edge cases AI missed
    ->
Write 15 test cases
    ->
Execute at least 5 tests
    ->
Record videos and actual results
    ->
Log defects as GitHub issues
    ->
Update report and summary tables
```

---

## Step 1 - Device Profile

Capture:

* Brand
* Model
* Year
* Serial number with middle 4 characters masked
* Device condition
* Main functions
* Safety concerns

Evidence:

```text
EV-XXX_DEV-001_device_student_id.jpg
```

---

## Step 2 - Generate And Review Test Ideas

Use AI for brainstorming only.

Required human review:

* [ ] Remove impossible tests
* [ ] Add realistic household-use scenarios
* [ ] Add boundary and stress conditions
* [ ] Add at least 3 edge cases AI did not find
* [ ] Save AI conversation screenshot proving missed edge cases

---

## Step 3 - Write Test Cases

Use:

```text
outputs/docs/templates/TEST_CASE_TEMPLATE.md
```

Each test case needs:

* Objective
* Input
* Steps
* Expected result
* Actual result after execution if run
* Verdict

---

## Step 4 - Execute Tests

For each executed test:

* [ ] Prepare safe setup
* [ ] Record short video
* [ ] Include voice narration
* [ ] Follow documented steps
* [ ] Record actual result
* [ ] Assign verdict
* [ ] Save video link or evidence note

---

## Step 5 - Log Defects

When a defect is found:

* Create a GitHub issue
* Include steps to reproduce
* Include expected and actual behavior
* Attach or link evidence
* Capture screenshot of Issues page showing GitHub username

---

## Final Notes

Physical-product testing must be grounded in real execution. AI can suggest test ideas, but actual evidence must come from the student's device and execution.
