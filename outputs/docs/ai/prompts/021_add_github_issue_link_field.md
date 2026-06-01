# PROMPT LOG 021 - ADD GITHUB ISSUE LINK FIELD

## Status

IS AI-GENERATED: YES (Codex-assisted prompt log)

REVIEWED: yes (10AM42 01/06/2026 - Khoi Nguyen Minh)

ACCEPTED: yes (10AM42 01/06/2026 - Khoi Nguyen Minh)

---

## Prompt Metadata

| Field | Value |
| --- | --- |
| Prompt ID | PROMPT-021 |
| Prompt file | `021_add_github_issue_link_field.md` |
| Original timestamp | 9AM52 01/06/2026 |
| Log timestamp | 9AM52 01/06/2026 |
| Prompter | Khoi Minh Nguyen |
| Responder | Codex |
| Tool | Codex |
| Related area | Requirement 2 software defect analysis metadata |
| Verdict | VALID |

---

## Prompt

```text
add github issue link field into metadata section
```

---

## Response

Done.

Added this metadata row to every Requirement 2 defect analysis file:

```text
| GitHub Issue Link | Not available in source JSON |
```

The value is marked as unavailable because `chosen-defects.json` contains paper/source links and artifact links, but does not contain specific GitHub issue URLs.

Updated:

```text
outputs/deliverables/requirement_2_software_defects/def_01/analysis.md
outputs/deliverables/requirement_2_software_defects/def_02/analysis.md
outputs/deliverables/requirement_2_software_defects/def_03/analysis.md
outputs/deliverables/requirement_2_software_defects/def_04/analysis.md
outputs/deliverables/requirement_2_software_defects/def_05/analysis.md
outputs/deliverables/requirement_2_software_defects/def_06/analysis.md
outputs/deliverables/requirement_2_software_defects/def_07/analysis.md
outputs/deliverables/requirement_2_software_defects/def_08/analysis.md
outputs/deliverables/requirement_2_software_defects/def_09/analysis.md
outputs/deliverables/requirement_2_software_defects/def_10/analysis.md
outputs/deliverables/requirement_2_software_defects/def_11/analysis.md
outputs/deliverables/requirement_2_software_defects/def_12/analysis.md
outputs/deliverables/requirement_2_software_defects/def_13/analysis.md
outputs/deliverables/requirement_2_software_defects/def_14/analysis.md
outputs/deliverables/requirement_2_software_defects/def_15/analysis.md
outputs/deliverables/requirement_2_software_defects/def_16/analysis.md
outputs/deliverables/requirement_2_software_defects/def_17/analysis.md
outputs/deliverables/requirement_2_software_defects/def_18/analysis.md
outputs/deliverables/requirement_2_software_defects/def_19/analysis.md
outputs/deliverables/requirement_2_software_defects/def_20/analysis.md
```

Verification passed:

```text
GITHUB_FIELD_COUNT=20
TITLE_ORDER_MATCHES=True
```

---

## Response Time: 3m44s

## Project Effects

Updated all 20 defect analysis Markdown files and created:

```text
outputs/docs/ai/prompts/021_add_github_issue_link_field.md
```

---

## Description

This prompt added an explicit GitHub issue link metadata field to the per-defect analysis template instances.

---

## Final Notes

No GitHub issue URLs were invented.
