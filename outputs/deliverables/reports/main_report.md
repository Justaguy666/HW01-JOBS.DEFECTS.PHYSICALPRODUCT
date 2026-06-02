# HW01 Report - Jobs, Defects, and Physical Product Testing

## Report Metadata

| Field | Value |
| --- | --- |
| Assignment | HW01 - Jobs, Defects, and Physical Product Testing |
| Student | 23127070 - Khoi Minh Nguyen |

## Executive Summary

This report consolidates the work completed for HW01 across three areas: QA/QC job-market research, public software-defect analysis, and physical-product testing. The detailed evidence remains in the requirement folders, while this report explains the method, summarizes the findings, and records the main limitations.

The submission contains 10 QA/QC job postings, 20 software-defect records from 2022-2026, and a physical testing package for a BRIDIO TH10 wireless headset. Requirement 3 includes 15 executed test records and 5 discovered defects linked to GitHub issues. The strongest overall theme across the work is that testing roles and testing artifacts still depend heavily on human judgment: AI can speed up structure, first drafts, and consistency checks, but evidence validation, defect severity, and final acceptance decisions still require human review.

The main known limitation is video evidence for Requirement 3. No unlisted YouTube execution videos are provided, and the exception is explicitly recorded in `requirement_3_physical_testing/execution_videos/youtube_links.txt`. The self-assessment deducts points from the physical-product testing section for this missing evidence.

For more details, see:

- `reports/self_assessment.md`
- `references/references.md`
- `appendix/prompt_log.md`
- `appendix/ai_critique.md`

## Requirement 1 - QA/QC Job Market Research

The first requirement asks for current QA/QC job-market evidence. I collected 10 QA/QC-related job postings from ITviec and preserved each posting with a source link, screenshot, job description, extracted requirements, and AI impact analysis. The selected jobs include manual QA, automation QA, QC, process QA, and senior/lead testing positions, so the set covers both execution-focused and process-focused testing work.

The postings show that employers still expect the core testing baseline: requirement reading, test-case design, regression testing, defect reporting, API/database checks, and communication with developers or product teams. Automation is also common. Playwright, Python, Selenium, Postman/API testing, SQL, and test maintenance appear across multiple postings, which suggests that QA/QC roles are moving toward hybrid manual plus automation responsibility rather than only manual execution.

AI appears as a supporting skill rather than a full replacement for testers. Some postings explicitly mention an AI-first mindset or AI-related workflows, while others imply automation and tooling expectations that AI can support. The realistic impact is task acceleration: drafting test cases, generating sample data, helping with scripts, and reviewing repetitive documentation. The risk is over-trusting generated tests without checking business rules, edge cases, and product context.

Important observations:

- The job set contains 10 postings, satisfying the required count.
- More than 3 postings involve AI, automation, or AI-assisted QA work.
- Salary information is preserved where available; some postings only state non-specific compensation notes such as "You'll love it" or "Attractive".
- Screenshots and source links are kept with each job folder for evidence traceability.

For more details, see:

- `requirement_1_job_market/job_01/job_description.md`
- `requirement_1_job_market/job_01/extracted_requirements.md`
- `requirement_1_job_market/job_01/ai_impact_analysis.md`
- `requirement_1_job_market/job_02/job_description.md`
- `requirement_1_job_market/job_02/extracted_requirements.md`
- `requirement_1_job_market/job_02/ai_impact_analysis.md`
- `requirement_1_job_market/job_03/job_description.md`
- `requirement_1_job_market/job_03/extracted_requirements.md`
- `requirement_1_job_market/job_03/ai_impact_analysis.md`
- `requirement_1_job_market/job_04/job_description.md`
- `requirement_1_job_market/job_04/extracted_requirements.md`
- `requirement_1_job_market/job_04/ai_impact_analysis.md`
- `requirement_1_job_market/job_05/job_description.md`
- `requirement_1_job_market/job_05/extracted_requirements.md`
- `requirement_1_job_market/job_05/ai_impact_analysis.md`
- `requirement_1_job_market/job_06/job_description.md`
- `requirement_1_job_market/job_06/extracted_requirements.md`
- `requirement_1_job_market/job_06/ai_impact_analysis.md`
- `requirement_1_job_market/job_07/job_description.md`
- `requirement_1_job_market/job_07/extracted_requirements.md`
- `requirement_1_job_market/job_07/ai_impact_analysis.md`
- `requirement_1_job_market/job_08/job_description.md`
- `requirement_1_job_market/job_08/extracted_requirements.md`
- `requirement_1_job_market/job_08/ai_impact_analysis.md`
- `requirement_1_job_market/job_09/job_description.md`
- `requirement_1_job_market/job_09/extracted_requirements.md`
- `requirement_1_job_market/job_09/ai_impact_analysis.md`
- `requirement_1_job_market/job_10/job_description.md`
- `requirement_1_job_market/job_10/extracted_requirements.md`
- `requirement_1_job_market/job_10/ai_impact_analysis.md`

## Requirement 2 - Software Defects 2022-2026

The second requirement asks for publicized software defects from 2022-2026, with at least 5 AI/LLM-related cases. I selected 20 defect records and documented each one in a separate analysis file. Each analysis includes metadata, source evidence, severity, consequence, mitigation or fix direction, and an AI bias/hallucination observation.

The selected set contains more than the minimum number of AI/LLM-related records. The AI-related portion includes deep-learning framework defects, machine-learning system bugs, model-optimization defects, LLM debugging benchmarks, and AI-assisted vulnerability or repair datasets. The non-AI portion still matters because it shows the same testing pattern in traditional software systems: vulnerabilities, Android functional issues, infrastructure-as-code faults, container runtime bugs, Kubernetes operator bugs, WebAssembly runtime bugs, JavaScript engine bugs, and compiler-introduced security bugs.

One important limitation is the nature of the sources. Several records are research papers, datasets, or benchmark artifacts rather than one simple production incident with a single reproduction story. I treated those sources cautiously. The local analysis files preserve the public source and avoid presenting uncertain inferred details as confirmed facts.

The main lesson from this requirement is that public defect analysis is a traceability exercise. A plausible explanation is not enough. The source link, screenshot, defect context, severity rationale, and mitigation all need to be connected so the reader can inspect where the claim came from. This is especially important when using AI to summarize technical defects, because AI can make source-light explanations sound complete.

Important observations:

- The set contains 20 documented software defects.
- The year range is 2022-2026.
- The selected set exceeds the requirement of 5 AI/LLM-related cases.
- Every defect folder includes a Markdown analysis file and screenshot evidence.
- The analysis files include an AI bias or hallucination observation to record where AI-assisted reasoning could be risky.

For more details, see:

- `requirement_2_software_defects/def_01/analysis.md`
- `requirement_2_software_defects/def_02/analysis.md`
- `requirement_2_software_defects/def_03/analysis.md`
- `requirement_2_software_defects/def_04/analysis.md`
- `requirement_2_software_defects/def_05/analysis.md`
- `requirement_2_software_defects/def_06/analysis.md`
- `requirement_2_software_defects/def_07/analysis.md`
- `requirement_2_software_defects/def_08/analysis.md`
- `requirement_2_software_defects/def_09/analysis.md`
- `requirement_2_software_defects/def_10/analysis.md`
- `requirement_2_software_defects/def_11/analysis.md`
- `requirement_2_software_defects/def_12/analysis.md`
- `requirement_2_software_defects/def_13/analysis.md`
- `requirement_2_software_defects/def_14/analysis.md`
- `requirement_2_software_defects/def_15/analysis.md`
- `requirement_2_software_defects/def_16/analysis.md`
- `requirement_2_software_defects/def_17/analysis.md`
- `requirement_2_software_defects/def_18/analysis.md`
- `requirement_2_software_defects/def_19/analysis.md`
- `requirement_2_software_defects/def_20/analysis.md`

## Requirement 3 - Physical Product Testing

The third requirement is based on a BRIDIO TH10 wireless over-ear headset. The product was identified using the device photo, packaging photo, barcode, SKU, and seller listing information. Public listing values such as Bluetooth V5.3, 300 mAh battery capacity, 2.5 hour charging time, approximately 10 m Bluetooth range, microphone support, AUX mode, and foldable design were treated as test-design assumptions, not as independently certified specifications.

The final test set contains 15 test cases and all 15 have execution records. The tests cover Bluetooth pairing, reconnection, phone Bluetooth recovery, range, obstruction behavior, audio playback, stereo mapping, video latency, microphone recording, call control, charging, comfort, and foldable hinge behavior. The result distribution is 10 PASS and 5 FAIL.

The failed cases produced 5 defects:

| Defect ID | Related test | Finding | GitHub issue |
| --- | --- | --- | --- |
| DEF-R3-001 | TC-002 | Automatic Bluetooth reconnection is unreliable after headset power cycle. | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/1 |
| DEF-R3-002 | TC-005 | Bluetooth playback drops repeatedly through one wall or closed door. | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/2 |
| DEF-R3-003 | TC-008 | Bluetooth mode has noticeable video lip-sync delay. | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/3 |
| DEF-R3-004 | TC-009 | Microphone recording is low and muffled in a quiet room. | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/4 |
| DEF-R3-005 | TC-014 | Right hinge becomes loose and clicks after rapid open-close cycles. | https://github.com/Justaguy666/HW01-JOBS.DEFECTS.PHYSICALPRODUCT/issues/5 |

The failures are mostly usability and durability issues rather than safety-critical failures. The headset can still perform basic Bluetooth playback, but reconnection reliability, obstruction handling, video latency, microphone quality, and hinge durability reduce confidence in daily use. The physical testing also showed why AI-generated test ideas need human expansion. Three AI-missed edge cases were added for fold/unfold while audio plays, rapid open-close stress, and one-sided fold pressure imbalance.

Requirement 3 has one deliberate evidence gap: no YouTube execution videos are included. The execution rows still record evidence IDs and GitHub issue links where applicable, but the video column is marked as not provided. This is the reason the physical-product testing score is reduced in the self-assessment.

Important observations:

- Device under test: BRIDIO TH10 wireless over-ear headset.
- Test cases completed: 15.
- Executed records: 15.
- Pass/fail result: 10 PASS, 5 FAIL.
- Discovered defects: 5.
- GitHub issues: 5 issue URLs recorded.
- AI-missed edge cases: 3.
- Video evidence: intentionally skipped and disclosed.

For more details, see:

- `requirement_3_physical_testing/device_info.md`
- `requirement_3_physical_testing/test_cases/test_cases.md`
- `requirement_3_physical_testing/test_cases/tc_001.md`
- `requirement_3_physical_testing/test_cases/tc_002.md`
- `requirement_3_physical_testing/test_cases/tc_003.md`
- `requirement_3_physical_testing/test_cases/tc_004.md`
- `requirement_3_physical_testing/test_cases/tc_005.md`
- `requirement_3_physical_testing/test_cases/tc_006.md`
- `requirement_3_physical_testing/test_cases/tc_007.md`
- `requirement_3_physical_testing/test_cases/tc_008.md`
- `requirement_3_physical_testing/test_cases/tc_009.md`
- `requirement_3_physical_testing/test_cases/tc_010.md`
- `requirement_3_physical_testing/test_cases/tc_011.md`
- `requirement_3_physical_testing/test_cases/tc_012.md`
- `requirement_3_physical_testing/test_cases/tc_013.md`
- `requirement_3_physical_testing/test_cases/tc_014.md`
- `requirement_3_physical_testing/test_cases/tc_015.md`
- `requirement_3_physical_testing/discovered_defects/defect_traceability.md`
- `requirement_3_physical_testing/discovered_defects/def_r3_001.md`
- `requirement_3_physical_testing/discovered_defects/def_r3_002.md`
- `requirement_3_physical_testing/discovered_defects/def_r3_003.md`
- `requirement_3_physical_testing/discovered_defects/def_r3_004.md`
- `requirement_3_physical_testing/discovered_defects/def_r3_005.md`
- `requirement_3_physical_testing/edge_cases_ai_missed/ec_001/explanation.md`
- `requirement_3_physical_testing/edge_cases_ai_missed/ec_002/explanation.md`
- `requirement_3_physical_testing/edge_cases_ai_missed/ec_003/explanation.md`
- `requirement_3_physical_testing/execution_videos/youtube_links.txt`

## References and Source Traceability

The references were not copied into this report because the full link list is long. Instead, all scanned URLs are centralized in `references/references.md`. The references index contains 358 unique URLs grouped by source area, including job-market links, software-defect links, Requirement 3 product links, and GitHub issue links.

For more details, see:

- `references/references.md`

## AI Use, Review, and Compliance

AI was used for structure, drafting support, summarization, consistency checks, workbook/Markdown conversion, and report preparation. It was not treated as final evidence. The student reviewed, accepted, corrected, or rejected AI outputs before including them in the submission.

The prompt log contains 36 prompt records. In the AI audit, the 36 prompt entries are treated as 36 prompt groups. Based on the verdicts recorded in the AI-02 audit appendix, 35 groups are VALID and 1 group is INVALID. The invalid case is Prompt 002, which gave a readiness verdict that was too soft while evidence organization still needed stronger treatment; it is traced to AI-OBS-001. The audit therefore records 97.2% valid as-is from prompt metadata, with the invalid output rejected or corrected during review.

The main AI lesson is that AI works well as a drafting and organization assistant, but it is weak as an evidence authority. It can miss physical edge cases, overstate source certainty, or make an incomplete project state sound ready. For this assignment, final responsibility stays with the student: source links, screenshots, device evidence, defect severity, test execution notes, and disclosure statements were reviewed before final packaging.

The AI compliance attachments are kept in the appendix and are not repeated here.

For more details, see:

- `appendix/prompt_log.md`
- `appendix/ai_critique.md`
- `appendix/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx`
- `appendix/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx`
- `appendix/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx`

## Self-Assessment

The current self-assessed score is 95/100. Requirement 1 and Requirement 2 are assessed as complete. Requirement 3 is assessed at 20/25 because the test design, execution records, and defects are present, but the required execution videos are missing. AI compliance sections are assessed as complete because the prompt log, AI audit report, AI disclosure form, privacy checklist, and AI critique are present.

| Area | Maximum | Self-assessed |
| --- | ---: | ---: |
| Job Market 2026+ | 40 | 40 |
| Software Defects 2022-2026 | 20 | 20 |
| Physical-product test design | 25 | 20 |
| AI-02 Audit Report | 8 | 8 |
| AI Critique and AI-03 Disclosure | 4 | 4 |
| AI-05 Checklist and anti-cheat artifacts | 3 | 3 |
| Total | 100 | 95 |

For more details, see:

- `reports/self_assessment.md`

## Conclusion

The completed work satisfies the main evidence requirements for job-market research, software-defect analysis, and physical-product testing, with one disclosed exception for Requirement 3 videos. The job-market section shows that QA/QC work increasingly combines manual judgment, automation, API/database skills, and AI-supported workflows. The software-defect section shows that source traceability is essential, especially when defects come from papers or datasets rather than simple incident reports. The physical-product testing section shows that practical consumer-product defects can be found through ordinary use scenarios, especially reconnection, obstruction, latency, microphone, and hinge durability tests.

Overall, AI helped with consistency and coverage, but the most important testing decisions remained human decisions: what evidence counts, which defects are credible, how severe the defects are, and what limitations must be disclosed.
