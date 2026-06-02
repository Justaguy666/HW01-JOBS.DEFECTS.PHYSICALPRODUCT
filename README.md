# HW01: Software Testing & QA/QC Analysis
## FIT@HCMUS — Software Testing Course (2026)

---

## 📌 Executive Summary

This repository contains the complete submission package for **HW01 - Jobs, Defects, and Physical Product Testing** as part of the Software Testing curriculum at the **Faculty of Information Technology, Ho Chi Minh City University of Science (FIT@HCMUS)**.

The assignment focuses on three main requirements:
1. **QA/QC Job-Market Research (R1)**: Analyzing 10 QA/QC job postings from ITviec, including AI's impact.
2. **Public Software Defect Analysis (R2)**: Reviewing 20 public software defects from 2022–2026, highlighting AI/LLM-related bugs.
3. **Physical Product Testing (R3)**: Designing 15 test cases, executing them, and documenting defects for a real **BRIDIO TH10 wireless over-ear headset**.
4. **AI Compliance & Audit**: Maintaining a prompt log, self-criticism, and completing the standard FIT@HCMUS AI Audit forms.

> [!WARNING]
> **Deliberate Evidence Gap**: In Requirement 3, the execution videos (YouTube links) were intentionally omitted and disclosed. As a result, 5 points have been deducted from the self-assessed grade (20/25 for Requirement 3), leading to a final self-assessed score of **95/100**.

---

## 👥 Student Information

* **FullName**: Nguyễn Minh Khôi (Khoi Minh Nguyen)
* **Student ID**: 23127070
* **Class**: FIT@HCMUS
* **Self-Assessed Grade**: **95/100**

---

## 📂 Repository Structure

The project is structured according to the defined file conventions:

```text
HW01-Jobs.Defects.PhysicalProduct/
├── inputs/                                 # Instructor-provided materials & requirements
│   ├── requirements/                       # HW01 requirements and policies PDF files
│   ├── testcase-templates/                 # Excel templates for test cases
│   └── ai-templates/                       # Standard AI Audit DOCX forms
├── outputs/                                # Student-created work and deliverables
│   ├── docs/                               # Internal guidance and conventions
│   │   ├── ai/                             # AI rules, audit guidelines, project context
│   │   ├── conventions/                    # Naming, status, document, and evidence rules
│   │   ├── templates/                      # Markdown templates for reports & jobs
│   │   └── workflows/                      # Workflows for jobs, defects, and testing
│   └── deliverables/                       # Submitted deliverables and proof files
│       ├── reports/                        # Main Report (PDF/MD) and Self-Assessment
│       ├── appendix/                       # Prompt log, AI Critique, and completed AI Audit Forms
│       ├── requirement_1_job_market/       # 10 job descriptions & AI impact analyses
│       ├── requirement_2_software_defects/  # 20 public defect analyses and evidence
│       ├── requirement_3_physical_testing/  # Device info, 15 test cases, and edge cases
│       ├── mindmap/                        # QA/QC role mindmap (PDF & PNG)
│       ├── github/                         # GitHub repository & issue links
│       └── references/                     # Consolidated reference list (358 URLs)
└── README.md                               # Root project overview (This file)
```

---

## 📑 Requirements Overview & Deliverables

### Requirement 1: QA/QC Job Market Research (Score: 40/40)
* **Goal**: Research current testing roles and analyze the market demand for QA/QC in 2026+.
* **Deliverables**: 10 job analysis folders, each containing:
  * Extracted requirements, job descriptions, and salary info.
  * Screenshots of postings on ITviec showing account/login name for anti-cheat verification.
  * AI Impact Analysis on how automation and LLMs accelerate/limit these roles.
  * *Note*: 3+ job postings require AI/Automation/LLM skills.
* **Key Files**:
  * [Requirement 1 Folder](outputs/deliverables/requirement_1_job_market/)
  * [Main Report - Section R1](outputs/deliverables/reports/main_report.md#requirement-1---qaqc-job-market-research)

### Requirement 2: Software Defects 2022-2026 (Score: 20/20)
* **Goal**: Analyze 20 publicized software defects to understand real-world failure patterns and mitigations.
* **Deliverables**: 20 defect analysis folders, each detailing:
  * Bug descriptions, root causes, severity justifications, consequences, and fixes.
  * Proof of source links and screenshots.
  * Critical check for AI bias or hallucination.
  * *Note*: 5+ defects are related to AI/LLM systems (deep learning frameworks, model optimization).
* **Key Files**:
  * [Requirement 2 Folder](outputs/deliverables/requirement_2_software_defects/)
  * [Main Report - Section R2](outputs/deliverables/reports/main_report.md#requirement-2---software-defects-2022-2026)

### Requirement 3: Physical Product Testing (Score: 20/25)
* **Goal**: Test a real-world physical device using manual techniques and document discovered bugs.
* **Device**: **BRIDIO TH10 Wireless Over-Ear Headset** (Bluetooth V5.3, 300mAh, Foldable).
* **Deliverables**:
  * Device photo with student ID card.
  * 15 detailed test cases spanning Connectivity, Audio Playback, Controls, Charging, and Ergonomics.
  * 3 AI-missed edge cases (Hinge rapid folding/pressure stress).
  * 5 discovered defects, logged as real GitHub issues in this repository.
  * *Disclosed Gap*: Missing execution videos.
* **Key Files**:
  * [Requirement 3 Folder](outputs/deliverables/requirement_3_physical_testing/)
  * [Test Cases List (Markdown)](outputs/deliverables/requirement_3_physical_testing/test_cases/test_cases.md)
  * [Defect Traceability](outputs/deliverables/requirement_3_physical_testing/discovered_defects/defect_traceability.md)

---

## 🐛 Discovered Physical Product Defects (GitHub Issues)

We executed 15 test cases on the BRIDIO TH10 Wireless Headset, resulting in **10 PASS** and **5 FAIL** verdicts. The 5 failures were filed as GitHub issues:

| Defect ID | Test Case | Defect Description | GitHub Issue Link | Status |
|---|---|---|---|---|
| **DEF-R3-001** | TC-002 | Automatic Bluetooth reconnection fails after headset power cycle. | [#1](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/1) | Open |
| **DEF-R3-002** | TC-005 | Bluetooth audio drops repeatedly through single household wall or door. | [#2](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/2) | Open |
| **DEF-R3-003** | TC-008 | High Bluetooth latency (~450-600ms) causing lip-sync delay in videos. | [#3](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/3) | Open |
| **DEF-R3-004** | TC-009 | Built-in microphone records muffled, low-volume audio even in quiet rooms. | [#4](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/4) | Open |
| **DEF-R3-005** | TC-014 | Right hinge becomes loose and clicks after 20 rapid open-close cycles. | [#5](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/5) | Open |

---

## 🤖 AI Collaboration & Compliance

In accordance with course policies, AI (LLMs) was utilized strictly as an assistant for drafting, structuring, and spelling/grammar checks.

* **Audit Verdict**: 36 prompt groups were audited. **35/36 (97.2%)** were validated as compliant. Prompt 002 was rejected during human review due to overly lenient readiness evaluation.
* **Mandatory Disclosure**: Disclosed in full in the appendix.
* **AI-Generated Files Review**: Every AI-generated file is marked with a Status block indicating review and acceptance details.

### Compliance Deliverables:
* [Prompt Log (36 entries)](outputs/deliverables/appendix/prompt_log.md)
* [AI Critique (200-300 words)](outputs/deliverables/appendix/ai_critique.md)
* [AI-02 Audit Report (.docx)](<outputs/deliverables/appendix/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx>)
* [AI-03 Disclosure Form (.docx)](<outputs/deliverables/appendix/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx>)
* [AI-05 Privacy Checklist (.docx)](<outputs/deliverables/appendix/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx>)

---

## 📊 Self-Assessment Scorecard

| Area | Max Points | Self-Assessed Score | Justification / Status |
| --- | :---: | :---: | --- |
| Job Market 2026+ (R1) | 40 | **40** | 10 jobs documented with screenshots, salary, and AI impact analysis. |
| Software Defects (R2) | 20 | **20** | 20 public defects from 2022-2026 documented with source evidence & AI bias check. |
| Physical Product testing (R3) | 25 | **20** | 15 TCs designed, 15 executed, 5 defects logged on GitHub. (-5 pts due to missing video evidence). |
| AI-02 Audit Report | 8 | **8** | Fully completed 5-section AI Audit Report appended. |
| AI Critique & AI-03 Disclosure | 4 | **4** | Critique (200-300 words) and signed Disclosure Form appended. |
| AI-05 Checklist & anti-cheat | 3 | **3** | Privacy Checklist completed; device photo with student ID provided. |
| **Total** | **100** | **95** | **Ready for final submission.** |

---

## 🔗 Key Links & Entry Points

* **Main Report**: [main_report.md](outputs/deliverables/reports/main_report.md) or [main_report.pdf](outputs/deliverables/reports/main_report.pdf)
* **Self-Assessment**: [self_assessment.md](outputs/deliverables/reports/self_assessment.md)
* **Documentation Index**: [DOCS_INDEX.md](outputs/docs/DOCS_INDEX.md)
* **References Index**: [references.md](outputs/deliverables/references/references.md)
