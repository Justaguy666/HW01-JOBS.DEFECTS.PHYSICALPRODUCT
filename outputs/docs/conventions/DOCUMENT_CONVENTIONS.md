# DOCUMENT CONVENTIONS

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM:59 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (01PM:10 31/05/2026 - Khoi Minh Nguyen)

---

## Purpose

This document defines common Markdown and documentation conventions for HW01 project files.

Goals:

* Keep all project documents consistent
* Make files easy to review and diff
* Support PDF export from Markdown
* Preserve AI review status clearly
* Reduce formatting noise in commits

---

## Required Document Header

Most project documentation files should begin with:

```text
# DOCUMENT TITLE

## Status

IS AI-GENERATED: YES/NO

REVIEWED: yes/no (time date - reviewer)

ACCEPTED: yes/no (time date - reviewer)

---

## Purpose
```

Rules:

* Use one H1 title per file
* Use uppercase for governance document titles
* Include `## Status` for rules, templates, workflows, and AI-generated drafts
* Use `---` to separate major sections
* End with `## Final Notes` when the file is guidance or convention material

---

## Markdown Style

Use:

* `#` for document title
* `##` for major sections
* `###` only when a section truly needs substructure
* `*` for bullet lists
* Numbered lists only for ordered steps
* Markdown tables for compact metadata
* Fenced code blocks for filenames, prompts, commands, or exact text

Avoid:

* Decorative formatting
* Long unstructured paragraphs
* Mixed bullet styles in one file
* Ambiguous placeholder text
* Broken encoding characters

---

## Code Fence Rules

Use `text` fences for plain examples:

```text
JOB-001_linkedin_qa_engineer.md
```

Use `markdown` fences only when showing Markdown syntax:

```markdown
# Example Heading
```

Do not add random code-fence attributes unless a tool requires them.

---

## Table Rules

Recommended table style:

| Column | Meaning |
| --- | --- |
| ID | Stable artifact ID |
| Status | Current review or execution state |

Rules:

* Keep tables narrow enough to read in Markdown
* Use empty cells only when the value is intentionally missing
* Prefer IDs over long descriptions when linking artifacts
* Do not put large raw content in tables

---

## Placeholder Rules

Allowed placeholders:

```text
TBD
Pending
N/A
JOB-XXX
DEF-XXX
TC-XXX
EV-XXX
```

Rules:

* Replace placeholders before final submission
* Use `N/A` only when an item truly does not apply
* Use `Pending` only for work that is planned
* Avoid vague placeholders like `something`, `fix later`, or `???`

---

## Review Rules

Before marking a document accepted:

* [ ] Status block is accurate
* [ ] No broken encoding appears
* [ ] No final-submission placeholders remain
* [ ] Links and paths are valid
* [ ] File follows naming conventions
* [ ] Content matches official requirements

---

## Final Notes

These conventions apply to project documentation, not necessarily to official template files that must preserve a required format.
