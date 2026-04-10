---
title: "AI-Assisted Cancer Diagnosis at Amsterdam UMC: A Two-Year Clinical Trial"
source: "https://thelancet.com/journals/landig/article/PIIS2589-7500(25)00041-2/fulltext"
author: "Dr. Jan de Vries, Prof. Maria Santos, Dr. Kwame Asante"
published: "2025-06-03"
created: "2025-06-04T07:55:00"
tags: [ai, oncology, cancer-diagnosis, amsterdam-umc, deep-learning, pathology, clinical-trial, healthcare, machine-learning]
---

# AI-Assisted Cancer Diagnosis at Amsterdam UMC: A Two-Year Clinical Trial

A two-year randomised controlled trial conducted at Amsterdam UMC — the merged academic medical centre formed by the merger of the Academic Medical Center (AMC) and VU University Medical Center (VUmc) — has demonstrated that artificial intelligence-assisted pathology can significantly reduce diagnostic errors in early-stage colorectal cancer, while also cutting reporting time by 38%.

The findings, published June 3, 2025 in *The Lancet Digital Health*, represent one of the largest prospective studies of AI-assisted oncological pathology in Europe and have been described by independent reviewers as "a landmark in clinical AI validation."

## Background and Motivation

Colorectal cancer is the second most common cause of cancer death in the Netherlands, accounting for approximately 10,500 diagnoses per year according to the Dutch Cancer Registry (IKNL) in Utrecht. Early detection is critical: five-year survival rates for stage I colorectal cancer exceed 90%, compared to just 12% for stage IV.

However, histopathological diagnosis — examining tissue samples under a microscope to classify tumour type and stage — is time-consuming, subject to inter-rater variability, and increasingly hampered by a shortage of trained pathologists. A 2023 workforce report from the Dutch Association of Pathology (NVVP) projected a 24% shortfall in qualified pathologists by 2030.

## The Trial Design

Principal investigator Dr. Jan de Vries, a gastrointestinal pathologist at Amsterdam UMC's Cancer Center Amsterdam, designed the trial in collaboration with Prof. Maria Santos, head of computational pathology at Radboud University Medical Center in Nijmegen, and Dr. Kwame Asante of the KNAW (Royal Netherlands Academy of Arts and Sciences) AI & Health programme.

The trial enrolled 2,847 patients referred for colorectal biopsy evaluation between January 2023 and December 2024 at five Dutch hospitals: Amsterdam UMC, Radboud UMC, Erasmus MC in Rotterdam, UMCG in Groningen, and the Maastricht UMC+. Patients were randomly assigned to one of two pathology workflows:

- **Standard workflow:** Tissue samples assessed by a senior pathologist following conventional light microscopy.
- **AI-augmented workflow:** Tissue samples pre-screened by the PathAI Colorectal Classifier v3.1 (developed by Boston-based PathAI Inc. in collaboration with Google Health) before human pathologist review.

The AI system was trained on a dataset of 1.2 million annotated whole-slide images sourced from 14 European hospitals, using a Vision Transformer (ViT-L/16) architecture fine-tuned by researchers at Delft University of Technology under a Horizon Europe grant (grant no. 101082218).

## Key Findings

In the AI-augmented arm, the overall diagnostic accuracy for early-stage (T1/T2) colorectal cancer reached 96.3%, compared to 91.7% in the standard pathology arm — a statistically significant improvement (p < 0.001). False negative rates, which represent the most dangerous failure mode in cancer screening, fell from 4.1% to 1.8%.

Reporting time dropped from a median of 6.2 working days to 3.8 working days in the AI-augmented group, a 38.7% reduction. This aligns with projections from a 2022 economic modelling study by ZonMW (the Netherlands Organisation for Health Research and Development), which estimated that AI-assisted pathology could save the Dutch healthcare system up to €120 million annually by 2028.

Crucially, pathologist confidence — measured via a post-report self-assessment questionnaire — increased in the AI-augmented arm. Dr. de Vries noted: "The system does not replace pathologist judgement. It acts as a highly trained assistant that flags areas of concern, allowing the pathologist to focus their attention where it matters most."

## Subgroup Analyses

Among patients over the age of 70 — a population with higher rates of comorbidity and atypical tumour presentations — AI augmentation produced the largest accuracy gains: 97.1% vs 88.9%. This subgroup also showed the greatest reduction in false negatives (1.3% vs 5.6%), a finding the authors describe as "clinically highly significant."

In a secondary analysis of rare tumour subtypes (mucinous adenocarcinoma and signet-ring cell carcinoma), the AI model performed comparably to senior pathologists, though the authors caution that this analysis was underpowered due to sample size.

## Safety and Regulatory Considerations

The PathAI Colorectal Classifier v3.1 received CE marking as a Class IIb medical device under the EU Medical Device Regulation (MDR 2017/745) in November 2024. The trial protocol was approved by the Medical Ethics Review Committee of Amsterdam UMC (registration no. NL81203.018.23) and conducted in accordance with the Declaration of Helsinki.

A data governance framework developed jointly by Amsterdam UMC and the Dutch Data Protection Authority (Autoriteit Persoonsgegevens) ensured that all patient data remained within the Netherlands and was processed on encrypted servers operated by SURFsara, a subsidiary of SURF, the Dutch national research and education network.

## Reactions from the Field

Prof. Eric Lim, a thoracic oncologist at Royal Brompton Hospital in London and an independent reviewer for *The Lancet Digital Health*, praised the trial's rigour: "This is exactly the kind of large-scale, prospective, multicentre evidence that has been lacking in clinical AI validation. The effect sizes are clinically meaningful."

Dr. Mariana Costa of the European Society for Medical Oncology (ESMO) called for immediate consideration of AI-augmented pathology in European clinical guidelines, while urging caution about equity: "We must ensure that hospitals in lower-resource settings — in Eastern Europe and beyond — can also benefit from these technologies. AI must not widen the diagnostic divide."

## What Comes Next

The Amsterdam UMC team has already begun a follow-up study examining AI-assisted diagnosis in pancreatic and gastric cancer, with funding from KWF Kankerbestrijding (Dutch Cancer Society) and the European Research Council (ERC). Results are expected in 2027.

In parallel, PathAI Inc. and Philips Healthcare (headquartered in Amsterdam) have announced a commercial partnership to integrate the classifier into Philips' IntelliSite Pathology Solution, with a planned rollout to 35 Dutch hospitals by Q1 2026.

"The question is no longer whether AI can help pathologists," said Prof. Santos. "The question is how quickly we can implement it safely, equitably, and at scale."
