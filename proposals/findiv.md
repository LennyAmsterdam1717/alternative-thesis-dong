# Proposal 3 — FinDiv: measuring the diversity of financial NLP datasets, and whether it explains robustness

*Idea I3 in `ideas_10.md` (score 65/75). Themes: T4 data diversity of financial NLP benchmarks × T2 robustness. Can absorb idea I4 (language-variation robustness) as a work package. Legend: [FT] full text opened · [ABS] abstract/record · [UNVERIFIED] not opened · [BG] background.*

## 1. Title and one-sentence pitch

**FinDiv: how diverse are financial NLP datasets, and does diversity predict whether sentiment models survive the jump from news to retail social media and earnings calls?**
Apply Dong Nguyen's own diversity framework and tool to the standard financial sentiment datasets, then run controlled training experiments in which only the diversity of the training data changes.

## 2. The problem

### 2.1 In plain language

Banks, funds and fintech apps use "financial sentiment" models to turn news, tweets and transcripts into signals. Almost all of these models are trained and tested on a handful of small public datasets. The most popular, Financial PhraseBank, was built in 2014 from about 5,000 sentences of company news (many about Finnish firms), labelled by 16 annotators with a finance or business background. Fine-tuned models score around 90–97% on it. Yet when the same models meet a retail investor's tweet ("$TSLA puts printing 🐻") or a CEO's hedged answer on an earnings call, accuracy drops sharply, and a 2026 journal study showed that meaning-preserving rewrites flip a large share of FinBERT's predictions.

Why do models trained on these datasets break? One plausible reason is that the training data are **not diverse**: they cover few topics, one writing style and one register. Dong Nguyen's ERC project DataDivers argues that diversity is a key, under-measured property of training data, and her group has just built a benchmark of 21 diversity measures and a Python tool to compute them. Those measures have so far only been tested on Wikipedia sentences.

**A concrete example (from the pilot run for this proposal).** Taking 500 random texts from each of five public datasets, the effective number of distinct *writing styles* (Vendi score on Wegmann's style embeddings) is 2.6 for Financial PhraseBank, 4.9 for SEntFiN headlines, 5.8 for earnings-call sentences, 9.5 for finance-news tweets and 14.5 for retail-investor tweets. By this measure the most-used training set is about five times less stylistically diverse than the text it is applied to. Semantically, earnings-call sentences are the *least* diverse (Vendi 64 vs 89–105 for the others). The thesis asks whether such differences, measured properly, predict how well a model trained on one dataset transfers to another, and whether *choosing more diverse training data at the same size* makes models more robust.

### 2.2 Technical formulation

Let 𝒟 = {D₁,…,D_K} be financial sentiment datasets with harmonised labels (negative/neutral/positive; binary for self-labelled StockTwits). For a text set *S* and diversity axis *a* ∈ {semantic, style, register/lexical}, let Div_μ,a(S) be diversity under measure μ (Graph Entropy, Vendi (q = 1), MST dispersion, Chamfer distance, plus mean pairwise distance as the common baseline).

1. **Profiling (RQ1):** estimate Div_μ,a(D_k) with bootstrap CIs at several *n*; decompose into variety, balance and disparity (EmbDivBench components); check measure agreement (Kendall τ across measures) and sensitivity to embedding model.
2. **Observational link (RQ2):** for each train–test pair (D_i → D_j), relate transfer performance F1(D_i → D_j) to Div(D_i) and to distance d(D_i, D_j) (e.g. Chamfer/MMD between embedding clouds).
3. **Controlled intervention (RQ3):** from a pooled corpus *P*, build training sets *T_ℓ* of fixed size *n* and fixed label balance with target diversity levels ℓ (selected by greedy max/min Vendi or cluster-stratified sampling), train model *f_ℓ*, and estimate ∂ F1_OOD / ∂ Div holding *n* constant. Compare with diversity-based pruning methods from Du et al. (2025): SemDedup, SmallToLarge.

## 3. Where the problem comes from

### 3.1 Papers naming the gap

| Paper | Section | Short quote (<15 words) | Paraphrase |
| --- | --- | --- | --- |
| Su, Wegmann, Ploeger & Nguyen, EMNLP 2026 [FT] | Limitations | "Our benchmark only captures part of the picture." | Tested only English Wikipedia sentences and fixed hyperparameters; calls for longer texts, other languages and calibration to real embedding statistics. |
| Nguyen & Ploeger, EMNLP 2025 [FT] | §1/§3 | "within-language diversity remains underexplored" | Diversity within one language (registers, varieties) is rarely measured. |
| Nguyen & Ploeger 2025 [FT] | §4 | "We caution against the blind optimization of diversity metrics" | Diversity must be tied to outcomes, which RQ3 does. |
| Du et al., ACL 2025 [FT] | Limitations | "its focus on task-specific fine-tuning" | Data-selection findings tested on hate speech, commonsense, summarisation; not on domain-specific data. |
| Bisharat & Hean, *Evaluating Financial Sentiment in the Age of AI*, arXiv 2609.20198 [FT] | §5, §8 | (paraphrase) | Several transformers were fine-tuned on PhraseBank, which may inflate scores; extend to call transcripts and filings. |
| Mahrous & Di Pietro, Findings ACL 2026 [ABS] | conclusion | (paraphrase; notes call for multilingual StockTwits-like data) | Cross-platform and cross-language transfer is hardest; emoji help. |

### 3.2 Lineage (short timeline)
- 2014 [BG]: Financial PhraseBank (Malo et al.), annotated by 16 annotators with agreement subsets (HF dataset card, [ABS]).
- 2018–2022 [BG]: FiQA, SEntFiN, TFNS; FinBERT trained partly on FPB.
- 2023–2024 [BG]: adversarial attacks on financial sentiment (Leippold, FRL 2023); diversity measures proliferate in NLP.
- 2025: Nguyen & Ploeger call for better diversity measurement; FLAME (Findings ACL 2025) and EcoFinBench (BoE) check quality and leakage of financial benchmarks; FinMTEB (2502.10990) reports inter-dataset semantic similarity; FPB positive–neutral agreement 75% (ICAIF 2025).
- 2026: EmbDivBench and the `emb-diversity` tool (Su et al.); Battle of Transformers (JBF 2026) shows paraphrase fragility; emoji transfer (Findings ACL 2026); Bisharat & Hean (2026) separate linguistic from economic validity.
- **Gap:** no one measures within-dataset diversity of financial NLP data, or tests whether it causes robustness.

### 3.3 Transferable gaps from her papers
EmbDivBench natural tier → finance; DataDivers aims (1) measure and (2) impact on robustness; Du et al. data-pruning comparisons in a new domain; Wegmann et al. (2025) register/variation as a separate axis.

### 3.4 Who is working on it now
Financial-NLP benchmark builders (FLAME, FinMTEB, FinBen groups) focus on coverage and leakage, not diversity measurement. Her own lab (Su, Wegmann, Ploeger) is the closest group in method: **FinDiv would be a natural collaboration rather than competition.**

## 4. Why Dong Nguyen
- **Builds on:** Su et al. 2026 (EmbDivBench, measure recommendations), the `emb-diversity` tool, Nguyen & Ploeger 2025 (definitions, validity), Du et al. 2025 (data selection), Wegmann's style embeddings (`AnnaWegmann/Style-Embedding` is the tool's default style model).
- **She contributes:** diversity measurement expertise; lab tooling; data-centred experimental design.
- **New for her:** a domain with registers that differ sharply (news, filings, calls, retail social media) and an applied robustness payoff; a finance "natural tier" for EmbDivBench.

## 5. Literature

### (a) Background
Su et al. 2026 [FT]; Nguyen & Ploeger 2025 [FT]; Du et al. 2025 (ACL) [FT]; Wegmann et al. 2025 [FT]; Financial PhraseBank dataset card (HF) [ABS] [BG].

### (b) Closest 2025–2026 papers and differences

| Paper | What they do | How FinDiv differs |
| --- | --- | --- |
| FinMTEB, arXiv 2502.10990 (2025) [ABS] | Embedding benchmark for finance; inter-dataset semantic similarity | Within-dataset diversity along several axes and components; link to robustness |
| FLAME, Findings ACL 2025 [ABS] | Holistic financial benchmark with quality checks | Measures diversity, not quality; controlled training experiments |
| Bisharat & Hean 2026 (2609.20198) [FT] | 12 sentiment models; linguistic vs economic validity on FPB + 8-K | Explains *why* models transfer, through data properties |
| Turetken & Leippold, JBF 2026 [ABS] | GPT-4o paraphrase attacks flip FinBERT | Natural cross-register shift instead of adversarial; diversity-based remedy |
| Mahrous & Di Pietro, Findings ACL 2026 [ABS] | Emoji transfer across platforms and languages | Text diversity across registers; controlled diversity manipulation |
| Su et al., EMNLP 2026 [FT] | Diversity measure benchmark on Wikipedia | Finance tier; outcome link |

## 6. Data and access

| Dataset | Register | Size (split used) | Licence | Cost | Access test (6 Nov 2026) | Rating |
| --- | --- | --- | --- | --- | --- | --- |
| Financial PhraseBank (`warwickai/financial_phrasebank_mirror`; original `takala/financial_phrasebank`) | company news | 4,846 | CC-BY-NC-SA-3.0 | 0 | Parquet downloaded via HF API; 4,846 rows | easy |
| TFNS (`zeroshot/twitter-financial-news-sentiment`) | finance-news tweets | 9,543 train | MIT | 0 | downloaded; 9,543 rows | easy |
| SEntFiN (`tasksource/sentfin`) | headlines, entity-level | 11,412 train | MIT | 0 | downloaded; 11,412 rows | easy |
| Financial tweets (`TimKoornstra/financial-tweets-sentiment`) | retail social | 38,091 | MIT | 0 | downloaded; 38,091 rows | easy |
| Earnings-call sentences (`jlh-ibm/earnings_call`, transcript-sentiment) | calls | 6,851 train | CC0-1.0 | 0 | downloaded; 6,851 rows | easy |
| StockTwits emoji set (`ElKulako/stocktwits-emoji`) | retail social, self-labelled | 100k–1M | MIT | 0 | HF API 200, not gated (not downloaded) | easy |
| StockTwits 2008–2022 comprehensive dataset (JQD:DM 2025) | retail social | very large | per paper | 0 | not tested (host not located in this run) | medium |
| FiQA-SA (`pauri32/fiqa-2018`), `ChanceFocus/flare-fiqasa` | mixed | ~1k | check card | 0 | HF API 200 | easy |
| Live StockTwits API | retail social | — | StockTwits ToS | 0 | `api.stocktwits.com/.../GME.json` → 200 with usernames and sentiment tags | not needed (personal data) |

**Pilot actually run** (`pilot/findiv_pilot.py`, results in `pilot/findiv_pilot_results.csv`; n = 500 per dataset, one seed, MiniLM-L6 for semantic, Style-Embedding for style):

| Dataset | Semantic Vendi | Semantic MPD | Style Vendi | Style MPD | Graph Entropy (sem / style) |
| --- | --- | --- | --- | --- | --- |
| FPB (news, 2014) | 96.8 | 0.857 | **2.57** | 0.197 | 3102 / 3026 |
| TFNS (finance tweets) | **104.6** | 0.850 | 9.47 | 0.587 | 3103 / 3058 |
| SEntFiN (headlines) | 88.1 | 0.821 | 4.86 | 0.353 | 3103 / 3043 |
| Retail financial tweets | 95.0 | 0.826 | **14.51** | 0.790 | 3103 / 3073 |
| Earnings-call sentences | **64.1** | 0.770 | 5.82 | 0.532 | 3101 / 3028 |

Readings (preliminary): style diversity varies five-fold across datasets and orders them by register as expected; semantic diversity is lowest for earnings calls. **Graph Entropy with default parameters hardly separates the datasets at n = 500** (range 3101–3103 semantic), although Su et al. (2026) found it best overall on Wikipedia; this is itself a finding worth checking (parameter or sample-size sensitivity), and exactly the kind of question her group would care about.

**Minimum viable dataset:** the five downloaded datasets (≈ 70k texts, all MIT/CC0/CC-BY-NC-SA). **Fallback:** FPB + TFNS + financial tweets only. No API access or scraping needed; no personal data beyond what public datasets contain (tweets may contain handles → removed in preprocessing).

## 7. Approach and 30-week plan

**Research question.** Can validated diversity measures characterise financial NLP datasets, and does training-data diversity, at fixed size, cause better robustness across financial registers?

**Sub-questions.**
- **RQ1 (measurement):** How diverse are the main financial sentiment datasets on semantic, stylistic and lexical/register axes; do measures agree; how sensitive are they to *n*, embedding model and parameters?
- **RQ2 (observation):** Does diversity of the training set, and distance between train and test sets, predict cross-dataset transfer of fine-tuned encoders and zero-shot LLMs?
- **RQ3 (intervention):** At equal size and label balance, do more diverse training sets (and diversity-based selection methods) improve out-of-register robustness, and on which axis (semantic vs style)?

**Method.** `emb-diversity` with several embedding models (MiniLM, mpnet, a finance embedding from FinMTEB, Style-Embedding); bootstrap CIs; label harmonisation; fine-tune DeBERTa-v3-base / FinBERT (3 seeds, as in her papers); zero-shot Qwen/Llama for comparison; train–test matrix; mixed models of F1 on diversity and distance; controlled diversity selection (greedy Vendi max/min, k-means stratification); comparison with SemDedup/S2L (Du et al. 2025 code).

**Baselines.** Random selection at equal *n*; full data; mean pairwise distance as the "naive" measure; data-pruning baselines.

**Metrics.** Macro-F1 in-domain and OOD; worst-register F1; Kendall τ between measures; incremental R² of diversity over size; robustness gap (in − out).

**No look-ahead issue:** no market prediction; datasets are used as text classification benchmarks. If an economic-validity check is added (as Bisharat & Hean), use 8-K releases with chronological splits.

**Human-centred component (optional):** a small register annotation (≈ 300 texts) to validate that "style diversity" tracks human-perceived register variety.

| Weeks | Dates | Phase | Work |
| --- | --- | --- | --- |
| 1–3 | 1–21 Dec | Phase 1 | Literature (diversity measurement, financial NLP datasets, robustness); dataset inventory and licences |
| 4–6 | 22 Dec–11 Jan | Phase 1 | Extend pilot: 5 seeds, n ∈ {250, 500, 1000, 2000}, 3 embedding models; label harmonisation |
| 7–9 | 12 Jan–1 Feb | Phase 1 | Proposal; pre-register RQ3 hypotheses |
| 10 | 2–8 Feb | **Go/no-go** | Go if measures separate datasets reliably on at least one axis |
| 11–14 | 9 Feb–8 Mar | Experiments | RQ1 full profiling + sensitivity |
| 15–18 | 9 Mar–5 Apr | Experiments | RQ2 train–test matrix (encoders + zero-shot LLMs) |
| 19–22 | 6 Apr–3 May | Experiments | RQ3 controlled diversity experiments; pruning baselines |
| 23 | 4–10 May | Experiments | Datasheet/dashboard (FinDiv cards) |
| 24–28 | 11 May–14 Jun | Writing | Thesis; short paper (e.g. FinNLP or a data-centric workshop) |
| 29–30 | 15–28 Jun | Writing | Revisions, defence |

## 8. Usable artefact
**FinDiv cards**: a diversity datasheet per financial dataset (axes, components, CIs, nearest registers) and a small dashboard where a practitioner uploads their own training sample and sees where it sits relative to the public datasets and which registers it covers poorly. Helps choose training data for in-house sentiment pipelines.

## 9. Ethics and GDPR
- Public research datasets only; tweets may contain @handles and cashtags → handles masked as @USER before analysis; no re-identification; no redistribution of raw tweets beyond what the licence allows.
- Lawful basis for residual personal data in public tweets: scientific research (Art. 6(1)(e)/Art. 89), minimisation, UU storage.
- No human participants unless the optional register annotation is added (then consent + ethics quick scan).
- Licences: FPB is CC-BY-NC-SA (non-commercial; fine for a thesis, flag for Accenture reuse).

## 10. Risks and minimum thesis

| Risk | Mitigation |
| --- | --- |
| Diversity does not predict robustness (null) | RQ1 profiling and measure-sensitivity results stand on their own; a null with good power is informative for DataDivers |
| Label schemes are not comparable across datasets | Binary polarity subset; report per-dataset label mapping; use entity-level SEntFiN carefully |
| Diversity confounded with domain distance | RQ3 controls size and labels and varies diversity within a pooled corpus |
| Measures unstable at small *n* (pilot hint for Graph Entropy) | Sweep *n* and parameters; this is a reportable finding |

**Minimum thesis:** RQ1 (profiling with sensitivity analysis) + RQ2 (transfer matrix) on the five downloaded datasets, plus FinDiv cards.

## 11. Scores
Fit 5 ×3 = 15 · Novelty 4 ×3 = 12 · Data 5 ×2 = 10 · Evaluation 5 ×2 = 10 · Feasibility 5 · AI 4 · Artefact 3 · Industry 3 · Frank 3 → **65 / 75**.

## 12. Questions to ask her
1. Would a finance natural tier be useful for EmbDivBench follow-up work, and could the thesis use or contribute to `emb-diversity`?
2. Is the Graph Entropy behaviour in the pilot (little separation at n = 500) expected, or a parameter issue?
3. Which register/style representation does she prefer for "register diversity" (Style-Embedding, STEL-based, LUAR)?
4. Should the thesis include I4 (controlled language-variation probes) as a work package, or keep diversity only?
5. Daily supervision by a DataDivers member (Su or Wegmann)? Co-supervision with Karnstedt-Hulpuș? 1 December start?
