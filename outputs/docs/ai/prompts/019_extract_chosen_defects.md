# PROMPT LOG 019 - EXTRACT CHOSEN DEFECTS

## Status

IS AI-GENERATED: YES (Codex-assisted prompt log)

REVIEWED: yes (9AM18 01/06/2026 - Khoi Nguyen Minh)

ACCEPTED: yes (9AM18 01/06/2026 - Khoi Nguyen Minh)

---

## Prompt Metadata

| Field | Value |
| --- | --- |
| Prompt ID | PROMPT-019 |
| Prompt file | `019_extract_chosen_defects.md` |
| Original timestamp | 9AM15 01/06/2026 |
| Log timestamp | 9AM15 01/06/2026 |
| Prompter | Khoi Minh Nguyen |
| Responder | Codex |
| Tool | Codex |
| Related area | Requirement 2 software defect selection |
| Verdict | DRAFT |

---

## Prompt

```text
get into defects.json and extract data of these 20 defects (given paperId and title) without keeping others' information

journals/ese/TambonNAKA24 — Silent bugs in deep learning frameworks: an empirical study of Keras and TensorFlow
journals/ese/MorovatiNKJ23 — Bugs in machine learning-based systems: a faultload benchmark.
conf/icsm/HoMI0SKNR23 — An Empirical Study on Bugs Inside PyTorch: A Replication Study
conf/icse/GuanXLLB23 — A Comprehensive Study of Real-World Bugs in Machine Learning Model Optimization.
conf/icse/LiangLSSFD22 — gDefects4DL: A Dataset of General Real-World Deep Learning Program Defects.
conf/acl/TianYQCLPWHL0024 — DebugBench: Evaluating Debugging Capability of Large Language Models
conf/iclr/JimenezYWYPPN24 — SWE-bench: Can Language Models Resolve Real-world Github Issues?
conf/kbse/RuanLZL24 — VulZoo: A Comprehensive Vulnerability Intelligence Dataset.
conf/msr/NiSYZW24 — MegaVul: A C/C++ Vulnerability Dataset with Comprehensive Code Representations.
conf/msr/BuiSF22 — Vul4J: A Dataset of Reproducible Java Vulnerabilities Geared Towards the Study of Program Repair Techniques.
conf/raid/0001DACW23 — DiverseVul: A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection.
conf/icse/WangHGWC024 — A Repository-Level Dataset For Detecting, Classifying and Repairing Software Vulnerabilities.
conf/issta/XiongX0SWWP0023 — An Empirical Study of Functional Bugs in Android Apps.
conf/kbse/DasAM24 — Taxonomy of Security-related Issues in Android Apps: An Empirical Study.
journals/pacmpl/DrososSAM024 — When Your Infrastructure Is a Buggy Program: Understanding Faults in Infrastructure as Code Ecosystems
conf/issta/YuXZ0LS24 — Bugs in Pods: Understanding Bugs in Container Runtime Systems.
conf/issta/XuG024 — An Empirical Study on Kubernetes Operator Bugs.
journals/tosem/ZhangCWCLMMHL24 — Characterizing and Detecting WebAssembly Runtime Bugs.
journals/infsof/WangBWYGS23 — An empirical study on bugs in JavaScript engines.
conf/uss/XuLDDLWPM23 — Silent Bugs Matter: A Study of Compiler-Introduced Security Bugs.

then return chosen-defects.json in the same path of defects.json
```

---

## Response

Done.

Read:

```text
outputs/deliverables/requirement_2_software_defects/defects.json
```

Created:

```text
outputs/deliverables/requirement_2_software_defects/chosen-defects.json
```

The output file contains only the 20 requested defect records. The records are kept in the same order as the prompt list, and no other paper records were included.

Verification passed:

```text
COUNT=20
ORDER_MATCHES=True
```

---

## Response Time: 3m36s

## Project Effects

Created:

```text
outputs/deliverables/requirement_2_software_defects/chosen-defects.json
outputs/docs/ai/prompts/019_extract_chosen_defects.md
```

---

## Description

This prompt filtered the software defects source dataset into a curated 20-paper subset for Requirement 2.

---

## Final Notes

The extracted JSON preserves the selected records' source fields from `defects.json` while excluding all unselected records.
