# PROMPT LOG 028 - NORMALIZE REQUIREMENT 3 NAMES

## Status

IS AI-GENERATED: YES (Codex-assisted prompt log)

REVIEWED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

ACCEPTED: yes (6PM12 01/06/2026 - Khoi Nguyen Minh)

---

## Prompt Metadata

| Field | Value |
| --- | --- |
| Prompt ID | PROMPT-028 |
| Prompt file | `028_normalize_requirement_3_names.md` |
| Original timestamp | 11AM03 01/06/2026 |
| Log timestamp | 11AM03 01/06/2026 |
| Prompter | Khoi Minh Nguyen |
| Responder | Codex |
| Tool | Codex |
| Related area | Requirement 3 physical testing structure |
| Verdict | VALID |

---

## Prompt

```text
use lower_case like tc_001, DEF-R3-001 -> def_r3_001, ec_001 (should have 5 folder, there are just 3)
```

---

## Response

Done.

Normalized Requirement 3 file and folder names under:

```text
outputs/deliverables/requirement_3_physical_testing/
```

Changes:

```text
TC-001.md through TC-015.md -> tc_001.md through tc_015.md
DEF-R3-001.md through DEF-R3-005.md -> def_r3_001.md through def_r3_005.md
EC-001 through EC-003 -> ec_001 through ec_003
Created ec_004 and ec_005
```

Each `ec_###` folder contains:

```text
ai_chat_screenshot.png
explanation.md
```

Verification passed:

```text
TC_LOWER_COUNT=15
TC_OLD_COUNT=0
DEF_R3_LOWER_COUNT=5
DEF_R3_OLD_COUNT=0
EC_LOWER_COUNT=5
EC_OLD_COUNT=0
```

---

## Response Time

Not measured by Codex. This log was created in the same turn as the Requirement 3 naming normalization request.

---

## Project Effects

Updated:

```text
outputs/deliverables/requirement_3_physical_testing/test_cases/
outputs/deliverables/requirement_3_physical_testing/discovered_defects/
outputs/deliverables/requirement_3_physical_testing/edge_cases_ai_missed/
```

Created:

```text
outputs/docs/ai/prompts/028_normalize_requirement_3_names.md
```

---

## Description

This prompt standardized Requirement 3 placeholder naming to lower-case snake-style IDs and completed the missing edge-case folders.

---

## Final Notes

Existing file contents were preserved.
