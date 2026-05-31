# TRACEABILITY RULES

## Status

IS AI-GENERATED: YES (Codex-assisted draft)
REVIEWED: yes (12AM:59 31/05/2026 - Khoi Minh Nguyen)
ACCEPTED: yes (01PM:10 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines how project artifacts should link to requirements, evidence, AI prompts, review notes, and final report sections.

Goals:

* Make every claim traceable
* Connect evidence to final deliverables
* Support AI audit and oral defense
* Avoid orphan files
* Improve final review and packaging

---

## Traceability Model

Recommended chain:

```text
Requirement
    ->
Artifact ID
    ->
Evidence ID
    ->
Review or audit note
    ->
Report section
```

For AI-assisted work:

```text
PROMPT-XXX
    ->
AI output
    ->
Human review
    ->
AI-OBS-XXX if mistake found
    ->
Corrected artifact
```

---

## Core IDs

| ID | Meaning |
| --- | --- |
| `JOB-XXX` | Job posting analysis |
| `DEF-XXX` | Software defect analysis |
| `TC-XXX` | Physical-product test case |
| `DEV-XXX` | Physical product profile |
| `EV-XXX` | Evidence item |
| `PROMPT-XXX` | Prompt log entry |
| `AUDIT-XXX` | AI audit report entry |
| `AI-OBS-XXX` | AI mistake observation |

---

## Minimum Traceability By Requirement

Requirement 1:

```text
R1 -> JOB-XXX -> EV-XXX screenshot -> report R1 table
```

Requirement 2:

```text
R2 -> DEF-XXX -> source link/EV-XXX -> AI issue -> report R2 table
```

Requirement 3:

```text
R3 -> TC-XXX -> EV-XXX video/photo -> actual result -> report R3 table
```

AI compliance:

```text
AI -> PROMPT-XXX -> AUDIT-XXX -> AI-OBS-XXX -> AI critique/disclosure
```

---

## Artifact Metadata Fields

Each major artifact should include:

| Field | Purpose |
| --- | --- |
| Artifact ID | Stable reference |
| Related requirement | R1 / R2 / R3 / AI |
| Evidence ID | Proof link |
| Source or prompt ID | Source trace |
| Status | Review state |
| Report section | Where it appears in final report |

---

## Review Questions

Before finalizing an artifact:

* [ ] Can I identify which requirement it supports?
* [ ] Does it have an ID?
* [ ] Does it link to evidence or source?
* [ ] Does the report mention the same ID?
* [ ] If AI helped, is the prompt logged?
* [ ] If AI made a mistake, is the correction documented?

---

## Orphan File Rule

A file is an orphan if it has no clear relationship to:

* Requirement
* Artifact ID
* Evidence ID
* Report section
* Appendix
* Workflow or convention doc

Orphan files should be moved, indexed, renamed, or deleted before final packaging.

---

## Final Notes

Traceability should make it possible to answer: "Where did this claim come from, how was it checked, and where is the proof?"
