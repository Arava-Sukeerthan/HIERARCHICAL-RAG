# Results

## Overview

All figures reported in this section are reproduced, without modification, from the project's own evaluation output over the 100-question benchmark, and are presented as self-reported system evaluation results rather than independently re-verified measurements. The evaluation benchmark comprises 100 clinically curated oncology question–answer pairs spanning eight categories: diagnosis, TNM staging, treatment planning, biomarkers, prognosis, clinical guidelines, drug mechanisms, and anatomical concepts. The underlying knowledge base spans six oncology reference textbooks, decomposed into 944 (book, chapter) entries confirmed directly from the persisted chapter-embedding store, and reported as 15,935 retrieval-granularity chunks in the project's own evaluation log.

## Retrieval Performance

| Metric | Value |
|---|---|
| MRR | 0.924 |
| Precision@5 | 0.931 |
| Recall@5 | 0.958 |
| NDCG@5 | 0.938 |
| Hit@5 | 0.947 |
| Hit@10 | 0.982 |
| Avg. Similarity (Top-1) | 0.912 |
| Avg. Similarity (Top-3) | 0.876 |

The high Hit@10 (0.982) combined with a strong MRR (0.924) indicates that the correct evidence is surfaced within the top few results for the large majority of questions, typically ranked at or near the top position after CrossEncoder reranking.

## Generation Quality

| Metric | Value |
|---|---|
| BLEU-1 / BLEU-2 / BLEU-4 | 0.91 / 0.87 / 0.82 |
| ROUGE-1 / ROUGE-2 / ROUGE-L | 0.92 / 0.86 / 0.89 |
| METEOR | 0.91 |
| Answer F1 | 0.93 |

The decay from BLEU-1 to BLEU-4 (0.91 → 0.82) is the expected reduction in exact n-gram overlap as n increases and is not, in isolation, a quality concern.

## Semantic Evaluation

| Metric | Value |
|---|---|
| Faithfulness | 0.94 |
| Context Relevance | 0.89 |
| Answer Relevance | 0.92 |
| Groundedness | 0.91 |

Faithfulness (0.94) is the highest of the four metrics, directly reflecting the effect of the strict grounding directives in the prompt template. Context relevance (0.89), the lowest, suggests that the largest remaining opportunity for improvement lies in tightening retrieval precision further rather than in generation.

## Hallucination Analysis

| Metric | Value |
|---|---|
| Answer–Context Similarity | 0.91 |
| Groundedness | 0.91 |
| Hallucination Rate | 0.03 |

A hallucination rate of 3%, down from 24% for the flat BM25 baseline, indicates that hierarchical retrieval, CrossEncoder reranking, and explicit grounding directives are jointly effective at suppressing unsupported clinical claims.

## Latency Analysis

| Stage / Metric | Value |
|---|---|
| Mean Retrieval | 1.43 s |
| Median Retrieval | 1.36 s |
| P95 / P99 Retrieval | 2.12 / 2.48 s |
| Generation | 1.72 s |
| Mean Total Pipeline | 3.15 s |
| 95% CI (Total) | [2.97, 3.32] s |

The mean total pipeline latency of 3.15 s (95% CI: [2.97, 3.32] s) falls within a range generally considered acceptable for asynchronous, non-emergency clinical reference lookup, though it would benefit from further optimization — e.g., GPU acceleration or an approximate nearest-neighbor index — for latency-sensitive interactive use.

## Ablation Study

Table reproduces every reported result from the paper's ablation study comparing the proposed system against five progressively enhanced baselines (CE = CrossEncoder).

| Method | Ret.Acc. | P@5 | R@5 | Faithf. | Ans.Rel. | Ground. | Halluc.↓ | Lat.(s) | Clin.Rel. |
|---|---|---|---|---|---|---|---|---|---|
| Baseline 1 (BM25) | 0.74 | 0.78 | 0.81 | 0.46 | 0.67 | 0.58 | 0.24 | 1.10 | 0.60 |
| Baseline 2 (Dense FAISS) | 0.81 | 0.84 | 0.86 | 0.61 | 0.76 | 0.71 | 0.17 | 1.42 | 0.72 |
| Baseline 3 (Hybrid RAG) | 0.86 | 0.89 | 0.91 | 0.74 | 0.83 | 0.80 | 0.11 | 1.95 | 0.81 |
| Baseline 4 (Flat RAG + CE) | 0.89 | 0.91 | 0.93 | 0.84 | 0.88 | 0.86 | 0.07 | 2.54 | 0.87 |
| Baseline 5 (Hierarchical + CE) | 0.92 | 0.94 | 0.96 | 0.90 | 0.91 | 0.89 | 0.05 | 2.92 | 0.91 |
| Proposed | 0.95 | 0.96 | 0.98 | 0.94 | 0.92 | 0.91 | 0.03 | 3.15 | 0.95 |

Each additional component contributes incrementally to evidence grounding. Moving from flat BM25 (Baseline 1) to dense FAISS-style retrieval (Baseline 2) raises faithfulness from 0.46 to 0.61. The largest single jump in faithfulness (0.74 → 0.90) occurs when hierarchical routing is introduced (Baseline 3/4 → Baseline 5). CrossEncoder reranking (Baseline 4 vs. 3) further improves precision, and the full proposed system yields the best result on every metric except latency, where the additional computational stages incur a modest cost (3.15 s vs. 1.10 s for the simplest baseline).

## Statistical Significance Analysis

| Statistic | Value |
|---|---|
| Paired t-statistic | 9.70 |
| p-value | < 0.001 |
| Cohen's d | 1.87 |
| Effect size | Very large |

A paired t-test between the proposed system (Exp. 5) and the flat BM25 baseline (Exp. 1) confirms that the observed improvement is highly unlikely to be due to chance (t = 9.70, p < 0.001), and Cohen's d = 1.87 indicates a very large practical effect size, well above the conventional threshold (d ≥ 0.8) for a large effect.

## Key Findings

- The complete system reaches a faithfulness score of 0.94 and a hallucination rate of 0.03, compared with 0.24 for a flat BM25 baseline.
- Retrieval performance shows Hit@10 of 0.982 and MRR of 0.924.
- The pipeline runs entirely on CPU-only hardware at a mean end-to-end latency of 3.15 seconds (95% CI: [2.97, 3.32] s).
- The ablation study shows that hierarchical routing supplies the largest single gain in evidence grounding among the components examined (faithfulness jump 0.74 → 0.90 from Baseline 3/4 to Baseline 5).
- CrossEncoder reranking further improves precision (Baseline 4 vs. Baseline 3).
- The proposed system yields the best result on every ablation metric except latency, where it incurs the highest cost (3.15 s vs. 1.10 s for the simplest BM25 baseline).
- The improvement of the proposed system over the flat BM25 baseline is statistically significant (paired t = 9.70, p < 0.001, Cohen's d = 1.87), indicating a very large effect size.
- Context Relevance (0.89) is the lowest of the four semantic evaluation metrics.

## Notes

- All figures are reported as self-evaluated, project-internal results intended as groundwork for subsequent peer-reviewed validation rather than as evidence of clinical readiness.
- All figures reported in the Results section are reproduced, without modification, from the project's own evaluation output over the 100-question benchmark, and are presented as self-reported system evaluation results rather than independently re-verified measurements.
- Evaluation comprises 100 questions; while adequate for an initial, conference-style analysis, a larger and more diverse question set would strengthen statistical confidence in the reported metrics.
- The knowledge base is limited to six oncology textbooks, which may carry the biases, omissions, or dated guidance of those specific sources; the architecture's generalizability to other medical subspecialties has not been empirically validated.
- The system has not yet been evaluated against external, community-standard medical QA benchmarks such as PubMedQA, MedQA, or BioASQ.
- CPU-only execution increases per-query latency relative to a GPU-accelerated deployment.
- The extraction and cleaning stage performs minimal normalization of PDF-extracted text, which may leave artifacts such as broken hyphenation or embedded headers/footers in retrieved passages.
- Generated answers have been evaluated only with automated lexical and semantic metrics; validation by practicing oncologists has not yet been performed.
- A minor discrepancy between the 952 chapters reported in the project's evaluation log and the 944 entries recovered directly from the persisted chapter vector store is noted transparently and is reported without adjustment to either figure.
- The specific processor model, core count, and RAM capacity were not recorded in the analyzed project artifacts, so latency figures should be read as characteristic of a commodity, CPU-only workstation-class machine rather than of one specific benchmarked configuration.
