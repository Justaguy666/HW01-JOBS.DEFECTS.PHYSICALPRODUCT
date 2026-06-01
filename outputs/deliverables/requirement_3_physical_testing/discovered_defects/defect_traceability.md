# defect_traceability workbook

Source workbook: `requirement_3_physical_testing/discovered_defects/defect_traceability.xlsx`

## Sheet: status

| Field | Value |
| --- | --- |
| Workbook title | Requirement 3 Defect Traceability |
| Requirement | R3 |
| Source template | N/A |
| IS AI-GENERATED | YES (Codex-assisted workbook update) |
| REVIEWED | yes (content consistency reviewed) |
| ACCEPTED | yes (included in final Requirement 3 package) |
| Owner | Khoi Minh Nguyen |
| Last updated | 10PM58 01/06/2026 |
| Ready for report | yes |
| Notes | Five Requirement 3 defect records are linked to failed test cases. |

## Sheet: defects

| Defect ID | Related TC ID | Title | GitHub Issue Link | Screenshot Evidence | Video Evidence | Severity | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEF-R3-001 | TC-002 | Automatic Bluetooth reconnection is unreliable after headset power cycle | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/1 | github_issues_screenshot.png | N/A (no video provided) | MEDIUM | FINAL | This affects daily usability because users expect a paired headset to recover after normal power cycling. The issue is not safety-critical, but it creates repeated setup friction and may be mistaken for a pairing failure. |
| DEF-R3-002 | TC-005 | Bluetooth playback drops repeatedly through one wall or closed door | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/2 | github_issues_screenshot.png | N/A (no video provided) | MEDIUM | FINAL | This limits practical use when the phone is left in another room. The severity is medium because the core Bluetooth function still works in open space but degrades in a common indoor scenario. |
| DEF-R3-003 | TC-008 | Bluetooth mode has noticeable video lip-sync delay | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/3 | github_issues_screenshot.png | N/A (no video provided) | MEDIUM | FINAL | The defect affects video watching and casual gaming. Severity is medium because the device still plays audio, but one advertised use case is noticeably degraded. |
| DEF-R3-004 | TC-009 | Microphone recording is low and muffled in quiet room | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/4 | github_issues_screenshot.png | N/A (no video provided) | MEDIUM | FINAL | This impacts calls, online meetings, and voice messages. Severity is medium because microphone quality is a core headset function, although playback is unaffected. |
| DEF-R3-005 | TC-014 | Right hinge becomes loose and clicks after rapid open-close cycles | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/5 | github_issues_screenshot.png | N/A (no video provided) | MEDIUM | FINAL | This is a durability concern because repeated folding is expected for a portable headset. Severity is medium because function still works, but the symptom may worsen with continued use. |


## Sheet: traceability

| Defect ID | Markdown File | Evidence Status | Report Section | Notes |
| --- | --- | --- | --- | --- |
| DEF-R3-001 | discovered_defects/def_r3_001.md | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/1; github_issues_screenshot.png; video not provided | Requirement 3 discovered defects | Linked to TC-002 |
| DEF-R3-002 | discovered_defects/def_r3_002.md | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/2; github_issues_screenshot.png; video not provided | Requirement 3 discovered defects | Linked to TC-005 |
| DEF-R3-003 | discovered_defects/def_r3_003.md | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/3; github_issues_screenshot.png; video not provided | Requirement 3 discovered defects | Linked to TC-008 |
| DEF-R3-004 | discovered_defects/def_r3_004.md | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/4; github_issues_screenshot.png; video not provided | Requirement 3 discovered defects | Linked to TC-009 |
| DEF-R3-005 | discovered_defects/def_r3_005.md | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/5; github_issues_screenshot.png; video not provided | Requirement 3 discovered defects | Linked to TC-014 |

## Sheet: review

| Check Item | Status | Notes |
| --- | --- | --- |
| Defects linked to test cases | DONE | All five defect rows include TC IDs |
| GitHub issues created | DONE | Issue URLs 1 through 5 recorded |
| Screenshot evidence available | DONE  | github_issues_screenshot.png referenced |
| Severity reviewed | DONE | All severities set to MEDIUM |
| Retest/follow-up recorded | DONE | Follow-up included in Markdown defect files |
| Ready for final report | PARTIAL | Defects ready; video evidence missing |

