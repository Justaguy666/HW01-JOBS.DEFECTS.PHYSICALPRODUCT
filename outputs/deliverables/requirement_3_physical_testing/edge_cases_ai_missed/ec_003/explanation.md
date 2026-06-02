# EC-003 - ONE-SIDE FOLD PRESSURE IMBALANCE

## Purpose

This file documents one Requirement 3 edge case that the AI tool did not identify.

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Edge case ID | EC-003 |
| Requirement | R3 |
| Related test case | TC-015 |
| AI prompt ID | PROMPT-035 |
| AI conversation screenshot | `ai_chat_screenshots/Screenshot 2026-06-01 220616.png` |
| Current status | FINAL |

---

## 2. Edge Case Description

The headset should be checked when normal folding pressure is applied to only one side at a time. This can reveal hinge misalignment, uneven pressure, discomfort, or one-channel audio problems that may not appear when both sides are handled evenly.

---

## 3. Why AI Missed It

This edge case depends on asymmetric physical stress, which is easy to overlook when test generation assumes balanced or ideal handling. A general AI test list may mention foldable durability but miss one-sided pressure imbalance as a distinct real-world risk.

---

## 4. Evidence

| Check | Result |
| --- | --- |
| AI screenshot attached | yes |
| Screenshot shows AI did not generate this edge case | yes |
| Written explanation completed | yes |
| Linked to a test case | TC-015 |
