# PROMPT LOG 031 - DEFINE COMMON MD XLSX TEMPLATE

## Status

IS AI-GENERATED: YES (Codex-assisted prompt log)

REVIEWED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

ACCEPTED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

---

## Prompt Metadata

| Field | Value |
| --- | --- |
| Prompt ID | PROMPT-031 |
| Prompt file | `031_define_common_md_xlsx_template.md` |
| Original timestamp | 11AM43 01/06/2026 |
| Log timestamp | 11AM43 01/06/2026 |
| Prompter | Khoi Minh Nguyen |
| Responder | Codex |
| Tool | Codex |
| Related area | Common templates and homework requirement comparison |
| Verdict | VALID |

---

## Prompt

```text
define common template for all .md and xlsx file (compare the template with requirements in homework (inputs))
```

---

## Response

Created a common file template for Markdown and Excel artifacts:

```text
outputs/docs/templates/COMMON_FILE_TEMPLATE.md
```

The template was compared against:

```text
inputs/requirements/hw01-requirements.pdf
inputs/requirements/homeword-policies.pdf
inputs/testcase-templates/testcase-template.xls
inputs/testcase-templates/testcase-checklist.xlsx
inputs/ai-templates/
```

Updated the documentation index so the new template is discoverable:

```text
outputs/docs/DOCS_INDEX.md
```

The new template defines:

* Common Markdown status, metadata, content, and verification sections
* Common Excel workbook structure for `status`, `data`, `summary`, `traceability`, and `review`
* Workbook-specific columns for self-assessment, test cases, test summary, defect traceability, and checklist workbooks
* Compatibility notes for the provided checklist workbook's `x`, `o`, and `i` review markers
* A requirement coverage matrix mapping R1, R2, R3, AI audit, AI critique, disclosure, privacy checklist, prompt logs, and final submission requirements to Markdown and Excel artifacts

Read-only workbook inspection confirmed:

* `inputs/testcase-templates/testcase-checklist.xlsx` contains the official checklist marker convention and quality-attribute rows
* `outputs/deliverables/reports/self_assessment.xlsx` matches the 100-point rubric structure
* `outputs/deliverables/requirement_3_physical_testing/test_cases/test_cases.xlsx` is currently a zero-byte placeholder and has no inspectable workbook content yet

---

## Response Time: 4m12s

## Project Effects

Created:

```text
outputs/docs/templates/COMMON_FILE_TEMPLATE.md
outputs/docs/ai/prompts/031_define_common_md_xlsx_template.md
```

Updated:

```text
outputs/docs/DOCS_INDEX.md
```

---

## Description

This prompt added a project-wide common file template so future Markdown and Excel deliverables can be checked against the official homework inputs before content is finalized.

---

## Final Notes

The new template is pending human review and acceptance.
