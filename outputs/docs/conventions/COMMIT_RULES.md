# COMMIT RULES

## Status

REVIEWED: yes (11AM:44 31/05/2026)

---

## Purpose

This document defines commit message conventions and repository commit practices for the HW01 project.

Goals:

* Maintain traceability
* Improve auditability
* Keep repository history clean
* Distinguish AI-assisted work from human-reviewed work
* Support oral defense and evidence tracking

---

## Commit Message Format

```text
<type>(<scope>): <summary>
```

---

## Examples

```text
chore(structure): initialize HW01 project structure
docs(conventions): define naming conventions
docs(ai): add AI collaboration rules
feat(r1): add JOB-001 LinkedIn analysis
feat(r2): analyze DEF-005 Meta AI hallucination case
feat(r3): add TC-005 rapid power reconnection test
test(r3): execute TC-003 on physical device
audit(ai): add AI-OBS-002 missed edge case log
evidence(r3): upload TC-005 execution screenshots
refactor(report): reorganize appendix structure
build(report): export final PDF report
chore(submission): finalize HW01 deliverables package
```

---

## Commit Types

| Type     | Meaning                              |
| -------- | ------------------------------------ |
| feat     | Add new deliverable/content          |
| fix      | Correct mistakes or inaccuracies     |
| docs     | Documentation or governance updates  |
| test     | Testing execution activities         |
| audit    | AI audit, critique, or observations  |
| evidence | Screenshots, videos, proof artifacts |
| refactor | Restructure without changing meaning |
| build    | Export/generated final artifacts     |
| chore    | Maintenance/setup/organization       |

---

## Commit Scopes

| Scope       | Meaning                     |
| ----------- | --------------------------- |
| ai          | AI governance/audit         |
| conventions | Project standards           |
| workflows   | Process/workflow updates    |
| templates   | Templates/forms             |
| structure   | Folder/repository structure |
| report      | Main report                 |
| appendix    | Appendix materials          |
| references  | Reference management        |
| r1          | Requirement 1               |
| r2          | Requirement 2               |
| r3          | Requirement 3               |
| evidence    | Evidence-related changes    |
| submission  | Final packaging/submission  |
| mindmap     | QA/QC mindmap               |

---

## Commit Rules

### General Rules

* Keep commits atomic
* One logical change per commit
* Use meaningful summaries
* Commit after human review
* Avoid committing temporary files
* Avoid committing unused generated outputs

---

### AI-Assisted Work Rules

* AI-generated drafts must be reviewed before commit
* Human modifications should be reflected in commit history
* Do not commit fabricated information
* Do not commit hallucinated references as facts
* AI outputs are not considered verified until manually checked

---

## Recommended Workflow

```text
AI Draft
    ↓
Human Review
    ↓
Manual Refinement
    ↓
Evidence Verification
    ↓
Commit
```

---

## Good Commit Examples

```text
feat(r3): add abnormal temperature stress test case
audit(ai): document hallucinated defect severity analysis
docs(conventions): define evidence naming rules
evidence(r3): upload TC-004 execution video
```

---

## Bad Commit Examples

```text
update
fix stuff
changes
final final real final
misc updates
```

---

## Commit Frequency

Recommended:

* Commit after completing a meaningful unit of work
* Commit after major manual review/refinement
* Commit before major restructuring
* Commit before exporting final deliverables

Avoid:

* Massive mixed commits
* Extremely tiny spam commits
* Long periods without commits

---

## Traceability Recommendations

Whenever possible, reference:

* TC IDs
* DEF IDs
* AI-OBS IDs
* JOB IDs

Examples:

```text
feat(r3): add TC-005 rapid power reconnection test
audit(ai): add AI-OBS-003 hallucination observation
fix(r2): correct severity analysis for DEF-004
```

---

## Final Notes

Repository history should demonstrate:

* iterative development
* human review
* AI governance
* evidence-based workflow
* authentic progress

The repository is considered part of the project's audit trail.
