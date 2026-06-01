# HW01 - Jobs, Defects, and Physical Product Testing Report

## 1. Report Metadata

| Field | Value |
| --- | --- |
| Assignment | HW01 - Jobs, Defects, and Physical Product Testing |
| Student | 23127070 - Khoi Minh Nguyen |
| ZIP root | Contents of the `deliverables` folder |
| Requirement sources | instructor-provided HW01 requirements and homework policy documents |
| References index | `references/references.md` |
| Self-assessment | `reports/self_assessment.xlsx`, `reports/self_assessment.md` |

## 2. Executive Summary

This submission package covers three required work areas:

- Requirement 1: QA/QC job-market research with 10 job postings, extracted requirements, screenshots, source links, and AI impact analyses.
- Requirement 2: 20 software-defect records from 2022-2026, including severity, consequences, mitigation notes, source evidence, screenshots, and AI bias/hallucination observations.
- Requirement 3: physical-product testing for a BRIDIO TH10 wireless headset, including device evidence, 15 test cases, 15 execution records, 5 discovered defects, GitHub issue links, and AI-missed edge-case documentation.

The package intentionally does not include Requirement 3 YouTube execution videos. The video evidence file records this as a skipped item: `requirement_3_physical_testing/execution_videos/youtube_links.txt`.

AI compliance documents are not duplicated in this main report. They should be kept in `appendix`, and this report only references them in Section 9.

## 3. Deliverables Map

| Area | Primary files/folders | Status |
| --- | --- | --- |
| Requirement 1 job-market research | `requirement_1_job_market` | Completed working set |
| Requirement 2 software defects | `requirement_2_software_defects` | Completed working set |
| Requirement 3 physical testing | `requirement_3_physical_testing` | Completed working set, videos skipped |
| GitHub issue evidence | `github`, `requirement_3_physical_testing/discovered_defects` | Completed local evidence |
| References | `references/references.md` | Completed URL scan |
| Prompt log | `appendix/prompt_log.md` | Appendix item |
| AI-02 Audit Report | `appendix/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx` | Appendix item |
| AI-03 Disclosure Statement | `appendix/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx` | Appendix item |
| AI-05 Privacy and Compliance Checklist | `appendix/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx` | Appendix item |
| AI critique | `appendix/ai_critique.md` | Appendix item |

## 4. Requirement 1 - QA/QC Job Market Research

### 4.1 Method

The job-market section collects 10 QA/QC-related job postings from ITviec. For each job, the deliverables include:

- source link,
- screenshot evidence,
- job description,
- extracted testing and skill requirements,
- salary information when available,
- short AI impact analysis.

The set includes more than the minimum 3 roles involving AI, automation, or AI-assisted QA workflows.

### 4.2 Job Posting Summary

| Job ID | Role | Company | Salary / compensation note | Local artifact |
| --- | --- | --- | --- | --- |
| JOB-01 | [Software QA Engineer (AI-first mindset)](https://itviec.com/it-jobs/software-qa-engineer-ai-first-mindset-zen8labs-5907) | Zen8Labs | Up to $2000 | `requirement_1_job_market/job_01` |
| JOB-02 | [Chuyen Vien QC Phan Mem (QC Executive)](https://itviec.com/it-jobs/chuyen-vien-qc-phan-mem-qc-executive-kingfoodmart-0249) | Kingfoodmart | $950 - $1,400 | `requirement_1_job_market/job_02` |
| JOB-03 | [Automation QA Engineer (QA QC/Tester/Automation Test)](https://itviec.com/it-jobs/automation-qa-engineer-qa-qc-tester-automation-test-nakivo-0115) | Nakivo | $1,100 - $1,500 | `requirement_1_job_market/job_03` |
| JOB-04 | [Senior QA/QC Automation Tester (Playwright/Python)](https://itviec.com/it-jobs/senior-qa-qc-automation-tester-playwright-python-bosch-global-software-technologies-company-limited-3146) | Bosch Global Software Technologies | "You'll love it" | `requirement_1_job_market/job_04` |
| JOB-05 | [Lead QA/QC Tester (Python/Playwright)](https://itviec.com/it-jobs/lead-qa-qc-tester-python-playwright-bosch-global-software-technologies-company-limited-1608) | Bosch Global Software Technologies | "You'll love it" | `requirement_1_job_market/job_05` |
| JOB-06 | [Senior Manual Test Engineer (QA/QC)](https://itviec.com/it-jobs/senior-manual-test-engineer-qa-qc-kms-technology-3100) | KMS Technology | Attractive | `requirement_1_job_market/job_06` |
| JOB-07 | [Principal QC Engineer](https://itviec.com/it-jobs/principal-qc-engineer-titan-dms-3614) | Titan DMS | "You'll love it" | `requirement_1_job_market/job_07` |
| JOB-08 | [Process Quality Assurance (PQA, QA QC)](https://itviec.com/it-jobs/process-quality-assurance-pqa-qa-qc-fpt-software-3809) | FPT Software | OT compensation noted | `requirement_1_job_market/job_08` |
| JOB-09 | [Junior/Senior/Leader QA Tester (ERP, API, SQL, NoSQL)](https://itviec.com/it-jobs/junior-senior-leader-qa-tester-erp-api-sql-nosql-ai-di-4555) | AI+DI | "You'll love it" | `requirement_1_job_market/job_09` |
| JOB-10 | [Software Tester (QA QC, Selenium, SQL, Postman)](https://itviec.com/it-jobs/software-tester-qa-qc-selenium-sql-postman-cong-ty-co-phan-phan-mem-phan-phoi-va-ban-le-beec-1809) | BEEC | "You'll love it" | `requirement_1_job_market/job_10` |

### 4.3 Requirement 1 Findings

The postings show that QA/QC roles still require core testing skills such as test planning, test-case design, regression testing, API testing, defect reporting, and cross-team communication. Automation skills are repeatedly visible through Playwright, Python, Selenium, API tools, and test-script maintenance. AI impact is strongest in roles that explicitly ask for an AI-first mindset or mention AI-assisted test generation, mock data creation, automation support, or QA workflow optimization.

Human review remains necessary because the job descriptions emphasize judgment-heavy work: understanding business requirements, clarifying acceptance criteria, checking edge cases, reproducing defects, and communicating with developers and product teams. AI can accelerate test drafting and automation support, but it does not replace responsibility for verifying correctness and business fit.

## 5. Requirement 2 - Software Defects 2022-2026

### 5.1 Method

The software-defect section contains 20 defect-analysis folders. Each local analysis file includes metadata, defect description, cause/root-cause notes, consequence/impact, severity assessment, mitigation, and an AI bias/hallucination observation. The selected set includes 11 AI/LLM-related records, exceeding the requirement of at least 5.

Several records are based on public research artifacts, datasets, or benchmark repositories rather than a fully confirmed single incident narrative. Where the source evidence is dataset-level, the local analysis marks uncertainty and avoids overstating unsupported technical details.

### 5.2 Defect Summary

| Defect ID | Title / subject | Year | AI/LLM-related | Severity | Local artifact |
| --- | --- | --- | --- | --- | --- |
| DEF-01 | Silent bugs in Keras and TensorFlow | 2024 | Yes | High | `requirement_2_software_defects/def_01/analysis.md` |
| DEF-02 | Bugs in machine learning-based systems faultload benchmark | 2023 | Yes | Medium | `requirement_2_software_defects/def_02/analysis.md` |
| DEF-03 | Bugs inside PyTorch replication study | 2023 | Yes | High | `requirement_2_software_defects/def_03/analysis.md` |
| DEF-04 | Real-world bugs in machine learning model optimization | 2023 | Yes | High | `requirement_2_software_defects/def_04/analysis.md` |
| DEF-05 | gDefects4DL deep-learning program defects | 2022 | Yes | Medium | `requirement_2_software_defects/def_05/analysis.md` |
| DEF-06 | DebugBench LLM debugging capability | 2024 | Yes | Medium | `requirement_2_software_defects/def_06/analysis.md` |
| DEF-07 | SWE-bench real-world GitHub issues for language models | 2024 | Yes | Medium | `requirement_2_software_defects/def_07/analysis.md` |
| DEF-08 | VulZoo vulnerability intelligence dataset | 2024 | No | High | `requirement_2_software_defects/def_08/analysis.md` |
| DEF-09 | MegaVul C/C++ vulnerability dataset | 2024 | No | High | `requirement_2_software_defects/def_09/analysis.md` |
| DEF-10 | Vul4J reproducible Java vulnerabilities | 2022 | Yes | High | `requirement_2_software_defects/def_10/analysis.md` |
| DEF-11 | DiverseVul vulnerable source-code dataset | 2023 | Yes | High | `requirement_2_software_defects/def_11/analysis.md` |
| DEF-12 | Repository-level vulnerability detection and repair dataset | 2024 | Yes | High | `requirement_2_software_defects/def_12/analysis.md` |
| DEF-13 | Functional bugs in Android apps | 2023 | No | Medium | `requirement_2_software_defects/def_13/analysis.md` |
| DEF-14 | Security-related issues in Android apps | 2024 | No | High | `requirement_2_software_defects/def_14/analysis.md` |
| DEF-15 | Faults in infrastructure-as-code ecosystems | 2024 | No | High | `requirement_2_software_defects/def_15/analysis.md` |
| DEF-16 | Bugs in container runtime systems | 2024 | Yes | High | `requirement_2_software_defects/def_16/analysis.md` |
| DEF-17 | Kubernetes operator bugs | 2024 | No | High | `requirement_2_software_defects/def_17/analysis.md` |
| DEF-18 | WebAssembly runtime bugs | 2024 | No | Medium | `requirement_2_software_defects/def_18/analysis.md` |
| DEF-19 | Bugs in JavaScript engines | 2023 | No | Medium | `requirement_2_software_defects/def_19/analysis.md` |
| DEF-20 | Compiler-introduced security bugs | 2023 | No | High | `requirement_2_software_defects/def_20/analysis.md` |

### 5.3 Requirement 2 Findings

The defect set shows that public software-defect evidence often appears through a combination of papers, datasets, issue trackers, and artifact repositories. AI/LLM-related defects are especially sensitive to hallucination risk because model-generated explanations can sound plausible even when source evidence is incomplete. For that reason, the local defect files distinguish confirmed evidence from inferred context and include an AI bias/hallucination observation for every defect.

The most severe records involve systems where correctness and security failures can propagate downstream: ML frameworks, vulnerability datasets, Java/C/C++ vulnerability benchmarks, infrastructure-as-code systems, runtime platforms, and compiler-introduced defects. Recommended mitigation across the set is consistent: preserve traceability to source evidence, reproduce the issue when possible, verify fixes with regression tests, and avoid relying on AI-generated summaries without human review.

## 6. Requirement 3 - Physical Product Testing

### 6.1 Device Under Test

| Field | Value |
| --- | --- |
| Device ID | DEV-001 |
| Product category | Wireless over-ear headset |
| Brand / SKU | BRIDIO / BD-A-B-TH10BRLDL0-BK |
| Model | TH10 |
| Year | 2024 |
| Serial number | Not found |
| Barcode | 6972706515155 |
| Device info file | `requirement_3_physical_testing/device_info.md` |
| Required photo | `requirement_3_physical_testing/device_photo_with_student_id.jpg` |
| Packaging photo | `requirement_3_physical_testing/device_packaging.jpg` |

The tested product is a BRIDIO TH10 wireless over-ear headset. Public seller information describes Bluetooth V5.3 support, 300 mAh battery capacity, approximately 2.5 hours charging time, approximately 10 m Bluetooth range, 40 mm driver size, microphone support, AUX wired mode, and basic headset controls. The test scope treats those seller-listing values as assumptions to be checked, not as independently certified manufacturer claims.

### 6.2 Test Design and Execution Summary

| Metric | Value |
| --- | --- |
| Total test cases | 15 |
| Execution rows completed | 15 |
| Pass count | 10 |
| Fail count | 5 |
| Discovered defects | 5 |
| AI-missed edge cases documented | 3 |
| Execution date used in records | 2026-06-01 |
| Video links provided | 0 |
| Voice narration confirmed | 0 |

Detailed test cases are stored in:

- `requirement_3_physical_testing/test_cases/test_cases.md`
- `requirement_3_physical_testing/test_cases/test_cases.xlsx`
- individual files `tc_001.md` through `tc_015.md`

The tests cover Bluetooth pairing, reconnection, range, audio playback, stereo orientation, video delay, microphone quality, call controls, charging, comfort, folding behavior, one-sided pressure, and other common household-use scenarios.

### 6.3 Execution Video Note

Requirement 3 normally asks for at least 5 unlisted YouTube execution videos with voice narration. This package does not provide those videos. The local record `requirement_3_physical_testing/execution_videos/youtube_links.txt` states that no YouTube execution videos are included and that video evidence is skipped.

### 6.4 Discovered Physical-Product Defects

| Defect ID | Related test case | Title | Severity | GitHub issue |
| --- | --- | --- | --- | --- |
| DEF-R3-001 | TC-002 | Automatic Bluetooth reconnection is unreliable after headset power cycle | Medium | [Issue 1](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/1) |
| DEF-R3-002 | TC-005 | Bluetooth playback drops repeatedly through one wall or closed door | Medium | [Issue 2](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/2) |
| DEF-R3-003 | TC-008 | Bluetooth mode has noticeable video lip-sync delay | Medium | [Issue 3](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/3) |
| DEF-R3-004 | TC-009 | Microphone recording is low and muffled in quiet room | Medium | [Issue 4](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/4) |
| DEF-R3-005 | TC-014 | Right hinge becomes loose and clicks after rapid open-close cycles | Medium | [Issue 5](https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/5) |

Traceability is recorded in:

- `requirement_3_physical_testing/discovered_defects/defect_traceability.md`
- `requirement_3_physical_testing/discovered_defects/defect_traceability.xlsx`
- `requirement_3_physical_testing/discovered_defects/def_r3_001.md` through `def_r3_005.md`

GitHub issue screenshot evidence is stored in:

- `github/github_issues_screenshot.png`
- `requirement_3_physical_testing/discovered_defects/github_issues_screenshot.png`

### 6.5 AI-Missed Edge Cases

The Requirement 3 package documents three edge cases that were not sufficiently covered by the initial AI-generated test scope:

| Edge case | Title | Local artifact |
| --- | --- | --- |
| EC-001 | Fold/unfold while audio is playing | `requirement_3_physical_testing/edge_cases_ai_missed/ec_001/explanation.md` |
| EC-002 | Rapid open-close stress | `requirement_3_physical_testing/edge_cases_ai_missed/ec_002/explanation.md` |
| EC-003 | One-side fold pressure imbalance | `requirement_3_physical_testing/edge_cases_ai_missed/ec_003/explanation.md` |

Supporting AI chat screenshots are stored in `requirement_3_physical_testing/edge_cases_ai_missed/ai_chat_screenshots`.

## 7. References

All scanned source links are centralized in `references/references.md`.

The references index currently contains 358 unique URLs:

- Requirement 1 job-market links: 10
- Requirement 2 software-defect links: 340
- Requirement 3 physical-testing links: 8

This main report does not repeat the full references list. The references file should be used as the submission bibliography/link index.

## 8. Self-Assessment

The self-assessment workbook and Markdown export are stored at:

- `reports/self_assessment.xlsx`
- `reports/self_assessment.md`

Current self-assessed score:

| Criteria | Grade | Self-assessed grade |
| --- | --- | --- |
| Job Market 2026+ | 40 | 40 |
| Software Defects 2022-2026 | 20 | 20 |
| Physical-product test design | 25 | 20 |
| AI-02 Audit Report | 8 | 8 |
| AI Critique + AI-03 Disclosure | 4 | 4 |
| AI-05 Checklist + anti-cheat artifacts | 3 | 3 |
| Total | 100 | 95 |

The reduced score for physical-product testing reflects the skipped Requirement 3 video evidence.

## 9. AI Compliance and Appendix References

The detailed AI compliance materials are intentionally not repeated in this main report. They should be placed under `appendix` and included in the final submission package.

| Appendix item | Expected location | Main report handling |
| --- | --- | --- |
| Prompt log | `appendix/prompt_log.md` | Referenced only |
| AI-02 Audit Report | `appendix/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx` | Referenced only |
| AI-03 Disclosure Statement | `appendix/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx` | Referenced only |
| AI-05 Privacy and Compliance Checklist | `appendix/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx` | Referenced only |
| AI critique, 200-300 words | `appendix/ai_critique.md` | Referenced only |

The prompt log should exclude the Requirement 3 enrichment prompt that the student explicitly marked as not to be logged.
