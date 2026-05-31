# AI Observation Report: AI-OBS-001

## Status

IS AI-GENERATED: YES (Codex-assisted draft)

REVIEWED: yes (12AM40 31/05/2026 - Khoi Minh Nguyen)

ACCEPTED: yes (12AM44 31/05/2026 - Khoi Minh Nguyen)

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Observation ID | AI-OBS-001 |
| Date observed | 2026-05-31 |
| Time observed | 11AM20 |
| Observer | Khoi Minh Nguyen |
| AI tool | Codex |
| Related requirement | Project organization / AI compliance |
| Related artifact | outputs folder structure review |
| Mistake type | FALSE_ASSUMPTION |
| Severity | MEDIUM |
| Status | VERIFIED |

---

## 2. Short Summary

The AI response was useful for checking the `outputs` structure, but it assumed the folder structure was almost ready while the deliverables area still lacked a concrete evidence storage structure. The response correctly warned about evidence organization, but the readiness verdict should have been stricter because HW01 depends heavily on screenshots, device photos, videos, prompt evidence, and GitHub issue evidence.

---

## 3. Original Prompt

```text
I just added some documentation elements, please review the outputs folder structure again, and let me know if it is ready for work
```

---

## 4. AI Output With Mistake

```text
Reviewed again. Structurally, it is **almost ready**, but I would make **one small folder-level improvement before serious work**.

The new `outputs/docs` structure is good:

`ai`, `conventions`, `templates`, `workflows`, `notes`, `references`

That is a clean split for planning and working documentation. The files are currently empty/placeholders, but since you said you'll define content later, that is fine.

The `outputs/deliverables` structure is also mostly good:

`reports`, `appendix`, `github`, `mindmap`, `references`, and the three requirement folders are all appropriate.

The only thing I'd fix before starting is evidence organization. HW01 will generate a lot of screenshots/photos/videos, and right now there is no clear evidence area. Add either a top-level:

outputs/deliverables/evidence

or evidence subfolders inside each requirement folder, for example:

outputs/deliverables/requirement_1_job_market/screenshots
outputs/deliverables/requirement_2_software_defects/sources
outputs/deliverables/requirement_3_physical_testing/device_photo
outputs/deliverables/requirement_3_physical_testing/execution_videos
outputs/deliverables/requirement_3_physical_testing/ai_missed_edge_cases

I'd also optionally add:

outputs/deliverables/submission_package

for the final zip/PDF-ready bundle.

So my verdict: **yes, ready for work after adding an evidence folder/subfolders.** The structure is much cleaner now; just don't start collecting screenshots/videos without a clear evidence place, or it'll get messy fast.
```

Evidence file/link:

```text
Conversation response in current Codex thread.
```

---

## 5. What Was Wrong

Key issue:

```text
The response said the structure was "almost ready" and then "ready for work after adding an evidence folder/subfolders." Because evidence folders were not present yet, the clearer verdict should have been "not ready yet; add evidence storage first."
```

Why it matters:

```text
HW01 requires many evidence artifacts: 10 job-posting screenshots, a device photo with student ID card, at least 5 execution videos, AI conversation screenshots for missed edge cases, GitHub issue screenshots, prompt logs, and AI compliance forms. If work starts before evidence locations are defined, files may be scattered and traceability may become weaker.
```

---

## 6. Verification Method

Relevant source checked:

```text
inputs/requirements/hw01-requirements.pdf
outputs folder tree from the second structure review
outputs/docs/conventions/COMMIT_RULES.md
outputs/docs/notes/ai_mistake_observed/AI_MISTAKE_TEMPLATE.md
```

Verification result:

```text
The HW01 requirements require evidence-heavy deliverables, but the deliverables tree at the time had no dedicated evidence folder or evidence subfolders. The AI response identified this gap but softened the verdict too much.
```

---

## 7. Human Correction

```text
Corrected verdict:

The outputs structure is not fully ready for work until evidence storage is defined. Add a dedicated evidence folder or requirement-specific evidence subfolders before collecting screenshots, videos, photos, AI conversation proof, and GitHub issue proof.
```

Changed in artifact:

```text
AI-OBS-001.md
AI_MISTAKES_INDEX.md
Future file-structure convention or deliverables index should reference the evidence folder decision.
```

---

## 8. Traceability

| Trace item | ID or path |
| --- | --- |
| Prompt log entry | Conversation prompt: "I just added some documentation elements..." |
| AI audit report entry | Pending |
| Evidence | Current Codex thread |
| Related final artifact | outputs folder structure / deliverables organization |
| Git commit | Pending |

---

## 9. Lesson Learned

```text
AI can identify a structural gap but still phrase the conclusion too optimistically. For HW01, readiness should be judged against the required evidence workflow, not only against the presence of broad folders. A human reviewer should convert soft advice into a concrete required action when the missing structure affects traceability.
```

---

## 10. Oral Defense Note

```text
If asked, I will explain that I reviewed the AI response and found that it correctly noticed the missing evidence area, but its final verdict was too permissive. I corrected the project workflow by treating evidence folder creation as a required step before collecting screenshots, videos, and other proof artifacts.
```

---

## 11. Status Checklist

* [x] Mistake recorded in `AI_MISTAKES_INDEX.md`
* [x] Prompt or screenshot evidence saved
* [x] Correct requirement/source verified
* [x] Human correction applied to related artifact
* [ ] AI audit report updated if needed
* [ ] Final report/appendix references updated if needed

---

## Final Notes

This observation shows that even when an AI recommendation is mostly useful, the readiness verdict can still require human tightening. The corrected workflow is to create evidence storage before starting evidence-heavy HW01 work.
