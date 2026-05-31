# AI MISTAKES INDEX

## Status

IS AI-GENERATED: YES (Codex-assisted edit)
REVIEWED: no (pending human review)
ACCEPTED: no (pending human acceptance)

---

## Purpose

This document tracks all observed AI mistakes, hallucinations, weak reasoning patterns, and missed edge cases discovered during the HW01 workflow.

Goals:

* Maintain AI auditability
* Document human review activity
* Track AI limitations and failure patterns
* Support AI critique and oral defense
* Improve traceability across artifacts

---

## Observation Registry

| ID | Type | Related Requirement | Related Artifact | Severity | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| AI-OBS-001 | FALSE_ASSUMPTION | Project organization / AI compliance | outputs folder structure review | MEDIUM | VERIFIED | AI gave an overly soft readiness verdict even though evidence storage was still missing |

---

## Mistake Type Definitions

| Type | Meaning |
| --- | --- |
| HALLUCINATION | AI generated unsupported or false information |
| MISSED_EDGE_CASE | Important edge case not identified |
| INCORRECT_REASONING | Logical analysis is flawed |
| OVERGENERALIZATION | Output too generic or shallow |
| FALSE_ASSUMPTION | Incorrect assumptions about context |
| WEAK_SEVERITY_ANALYSIS | Severity assessment is inaccurate |
| CONTEXT_IGNORANCE | Important real-world context ignored |
| FAKE_REFERENCE | Fabricated or unverifiable reference |
| SHALLOW_ANALYSIS | Analysis lacks depth |
| UNSAFE_SUGGESTION | Potentially unsafe recommendation |

---

## Severity Definitions

| Severity | Meaning |
| --- | --- |
| LOW | Minor quality issue |
| MEDIUM | Misleading or incomplete reasoning |
| HIGH | Strong impact on testing quality or analysis |
| CRITICAL | May cause invalid conclusions or unsafe behavior |

---

## Status Definitions

| Status | Meaning |
| --- | --- |
| TODO | Observation not fully analyzed |
| REVIEWED | Human review completed |
| VERIFIED | Confirmed and corrected |
| RESOLVED | Correction integrated into final artifacts |

---

## Observation File Structure

Detailed observations are stored in:

```text
docs/notes/ai_mistake_observed/
```

Example:

```text
AI_MISTAKE_TEMPLATE.md
AI-OBS-001.md
AI-OBS-002.md
AI-OBS-003.md
```

---

## Recommended Workflow

```text
AI Draft
    ->
Human Review
    ->
Issue Detected
    ->
Create AI Observation
    ->
Human Correction
    ->
Update Related Artifact
```

---

## Related Artifacts

AI observations may reference:

* TC IDs (Test Cases)
* DEF IDs (Defects)
* JOB IDs (Job Analyses)
* EV IDs (Evidence)
* AI Audit Reports
* AI Critique Sections

Examples:

```text
TC-005
DEF-003
JOB-001
EV-010
```

---

## Final Notes

This index exists to demonstrate:

* active human oversight
* responsible AI usage
* critical evaluation of AI outputs
* iterative refinement process

AI-generated content is never treated as automatically correct without manual verification.
