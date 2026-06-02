# EC-001 - FOLD/UNFOLD WHILE AUDIO IS PLAYING

## Purpose

This file documents one Requirement 3 edge case that the AI tool did not identify.

---

## 1. Metadata

| Field | Value |
| --- | --- |
| Edge case ID | EC-001 |
| Requirement | R3 |
| Related test case | TC-013 |
| AI prompt ID | PROMPT-035 |
| AI conversation screenshot | `ai_chat_screenshots/Screenshot 2026-06-01 220616.png` |
| Current status | FINAL |

---

## 2. Edge Case Description

The headset should be tested while audio is actively playing and the foldable hinge is slowly folded and unfolded using normal hand force. This checks whether hinge movement or internal wiring causes audio interruption, crackling, one-side channel loss, or Bluetooth disconnection.

---

## 3. Why AI Missed It

This edge case focuses on the interaction between mechanical movement and active audio playback. A general AI-generated test list may test Bluetooth playback and hinge durability separately, but miss the combined risk where folding movement affects audio continuity.

---

## 4. Evidence

| Check | Result |
| --- | --- |
| AI screenshot attached | yes |
| Screenshot shows AI did not generate this edge case | yes |
| Written explanation completed | yes |
| Linked to a test case | TC-013 |
