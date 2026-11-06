# Proposal 2 — MemTrace: explaining LLM look-ahead memorisation of stock-market events from open pretraining data

*Idea I1 in `ideas_10.md` (score 66/75), with idea I2 (the "visibility prior") as an optional sub-question. Theme: T1 training-data influence and look-ahead, in the data-centred NLP line of DataDivers. Legend: [FT] full text opened · [ABS] abstract/record · [UNVERIFIED] not opened · [BG] background.*

## 1. Title and one-sentence pitch

**MemTrace: which training data make language models "remember" how stocks moved?**
Using open models whose pretraining corpora are public, measure how often, how recently and in how many different contexts each firm–event appeared in training, and test whether these data properties explain which market outcomes a model has memorised.

## 2. The problem

### 2.1 In plain language

Researchers and banks test whether an AI model can "predict" stock moves by running it on historical news. The catch: a model trained in 2024 has read the internet up to 2024, including articles that say how those stocks moved. When asked about an old headline, it may simply remember the answer. This **look-ahead bias** makes AI trading results look far better than they are. In 2026 several papers built tests that detect it: they ask a model only "Did Kodak's stock go up or down on [a date in late July 2020]?" without any news, and if the model answers confidently and correctly, it has memorised the outcome.

These tests tell us *that* memorisation happens, not *why* it happens for some firms and dates and not others. The usual guess is "famous firms and big news get repeated a lot online", but nobody has measured it, because the big commercial models do not publish their training data. That leaves practitioners without a rule for when a backtest is safe.

There are now models whose complete training data are public (AllenAI's OLMo with the Dolma corpus; EleutherAI's Pythia with the Pile) and a family of small models trained on data cut off at the end of each year from 2013 to 2024 (DatedGPT). Search engines over these corpora (infini-gram) can count exact phrases across trillions of words in seconds. This makes it possible, for the first time, to line up "how often did the training data talk about this firm on this date, and in how many different ways?" against "does the model remember the outcome?".

**A concrete example.** In late July 2020 Kodak's share price jumped after a government-loan announcement (Gao et al. use Kodak as their illustration); it was covered by thousands of articles. Around the same time a mid-cap industrial firm fell 6% after an earnings miss, covered by a handful of wire stories. If OLMo recalls Kodak's move but not the industrial firm's, MemTrace asks whether the difference is explained by mention counts, by the number of *distinct* documents and sources (diversity), by repetition of near-identical copies (duplication), or by how close the event is to the training cut-off. The answer gives a practical rule ("events with fewer than *k* distinct mentions are safe to backtest") and a scientific one about how data properties drive memorisation.

### 2.2 Technical formulation

For a model *m* with pretraining corpus *D_m* and cut-off *c_m*, and a firm–date event *e = (i, t)* with realised outcome *y_e* ∈ {up, down} (next-day return sign, restricted to |r| > κ):

- **Memorisation strength** M_m(e): Lookahead Propensity (LAP, Gao, Jiang & Yan) = P_m("up") + P_m("down") from a date-only recall prompt, and **directional recall** R_m(e) = 1[argmax = y_e]; computed from exact token log-probabilities of open models.
- **Data properties** of *e* in *D_m*, from infini-gram counts and retrieved snippets:
  - F₁ = count(firm name), F₂ = count(firm ∧ date expression within w tokens) (CNF query), F₃ = count(firm ∧ outcome words, e.g. "shares jumped/plunged", within w tokens);
  - **Dup** = share of near-duplicate snippets (MinHash);
  - **Div** = diversity of the retrieved snippets (semantic and stylistic, `emb-diversity`; Graph Entropy and Vendi as recommended by Su et al. 2026);
  - **Src** = mix of corpus sources (web, Reddit, news-like domains, papers);
  - **Lag** = c_m − t (recency).
- **Model:** logit(R_m(e)) or M_m(e) = β₀ + β·g(F₂, F₃) + γ·Div + δ·Dup + λ·Lag + firm controls (size, sector, US vs non-US) + ε, with mixed effects for firm and month.
- **Natural experiment (DatedGPT):** for an event in year *t*, compare models with cut-off < *t* and ≥ *t*; the jump in recall at the cut-off should scale with the event's frequency in that year's crawl.
- **Causal check (optional RQ3):** continued pretraining of a small Pythia model on synthetic firm–event documents injected at controlled frequency and diversity.

## 3. Where the problem comes from

### 3.1 Papers naming the gap

| Paper | Section | Short quote (<15 words) | Paraphrase |
| --- | --- | --- | --- |
| Gao, Jiang & Yan, *Detecting Lookahead Bias in LLM Forecasts*, arXiv 2512.23847 (v2 Jun 2026) [FT] | App. C, Step 5 | "confounds in which LAP proxies for entity salience or attention" | Their memorisation score may reflect how famous an entity is; the corpus frequency behind it is not measured. |
| Gao et al. | §3.2 | "We adopt Llama-3.3-70B in this paper for replicability." | Evidence comes from one open-weight model whose training data are not public. |
| Gao et al. | §4 (Conclusion) | "it can be run on any model, any prompt, and any sample" | They invite applying the test elsewhere; open-data models are the obvious next step. |
| Kong et al., *Evaluating LLMs in Finance Requires Explicit Bias Consideration*, arXiv 2602.14233 [FT] | §2.1 / §3 | (paraphrase) | Ask authors to disclose pretraining cut-off dates and to run entity-substitution tests; only 26.8% of 164 papers acknowledge look-ahead. |
| Benhenda, *Look-Ahead-Bench*, arXiv 2601.13770 [FT] | §5.1 | (paraphrase) | Five stocks, two periods; calls for more stocks, periods and counterfactual tests. |
| Dimino et al., *Uncovering Representation Bias…*, arXiv 2510.05702 [ABS] | §1/§4 | "likely overrepresented in LLM pretraining data" | Attributes a size/visibility bias to pretraining data without measuring it (basis for sub-question I2). |

### 3.2 Lineage (short timeline)
- 2020–2023 [BG]: Pile (2020) and Pythia (ICML 2023, [ABS]) enable memorisation studies with known data order; Glasserman & Lin (2023) raise look-ahead in GPT sentiment [UNVERIFIED].
- 2024 [BG]: Dolma (ACL 2024, [ABS]) and OLMo release full corpora; infini-gram (Liu et al. 2024) makes exact n-gram counts over trillion-token corpora fast; factual knowledge acquisition studies on OLMo checkpoints (NeurIPS 2024, [ABS]).
- 2025: frequency ↔ recall relations shown for general facts (ICLR 2025 "Generalization vs memorization" with Pythia/OLMo, [ABS]; multilingual fact frequency in OLMo, Findings EMNLP 2025, [ABS]); in finance, Entity Neutering (SSRN 2025, [ABS]), "memorization problem" (Lopez-Lira et al. 2025, [UNVERIFIED]), visibility bias (Dimino et al. 2025, [ABS]).
- 2026: detection and mitigation in finance: Look-Ahead-Bench (Jan), DatedGPT (Mar), MemGuard-Alpha (Mar), FinCAD (May), Gao et al. v2 (Jun); memorisation propensity with infini-gram on the 52 TB Dolma 3 index (arXiv 2606.06286, [ABS]) in the general domain.
- **Gap:** finance papers detect memorisation in closed-data models; general NLP papers explain memorisation by frequency in open-data models; nobody joins them.

### 3.3 Transferable gaps from her own papers
- **Du et al. (ACL 2025)**: representations from training dynamics/gradients identify which instances matter; here, data properties identify which *events* a model absorbed.
- **DataDivers aim 2** (CORDIS): "investigate how data diversity impacts NLP model behavior" → does *diversity* of mentions (not just count) drive memorisation?
- **Nguyen & Ploeger (EMNLP 2025)** and **Su et al. (EMNLP 2026)**: measure diversity with validated measures (avoid mean pairwise distance), which the thesis applies to snippet sets.
- **Su et al. limitation**: natural tier limited to Wikipedia; financial web text is a new tier.

### 3.4 Who is working on it now and how close
- CUHK finance group (Gao, Jiang, Yan; DatedGPT) owns the detection side; a natural next step for them, but their models' data are FineWeb-Edu slices, so they could do the DatedGPT arm. **Closest competitor.**
- AllenAI/UW (infini-gram, OLMoTrace) owns the tooling; general-domain only.
- Lopez-Lira (Florida) and co-authors (memorisation, Kong et al. position paper).
**Assessment:** medium-high risk of being scooped on the DatedGPT arm; low on the OLMo/Pythia data-diversity arm.

## 4. Why Dong Nguyen
- **Builds on:** DataDivers (data diversity → model behaviour), Du et al. 2025 (data-centred analysis of what models learn from which instances), Su et al. 2026 and the `emb-diversity` tool (diversity measures), Nguyen & Ploeger 2025 (measurement validity of diversity).
- **She contributes:** the diversity-measurement methodology, training-data analysis framing, and evaluation rigour; her lab's tooling.
- **New for her:** a temporal, outcome-labelled domain where memorisation has a measurable economic cost; time-sliced models (DatedGPT) as a natural experiment on data recency.

## 5. Literature

### (a) Background
- Biderman et al., *Pythia* (ICML 2023) [ABS] [BG]; Soldaini et al., *Dolma* (ACL 2024) [ABS] [BG]; Liu et al., *infini-gram* (2024; docs at infini-gram.readthedocs.io, [ABS]) [BG]; *How Do LLMs Acquire Factual Knowledge During Pretraining?* (NeurIPS 2024) [ABS] [BG]; *Generalization v.s. Memorization: tracing capabilities back to pretraining data* (ICLR 2025) [ABS].
- Gao, Jiang & Yan (2025/2026) [FT] for the LAP measure.

### (b) Closest 2025–2026 papers and differences

| Paper | What they do | How MemTrace differs |
| --- | --- | --- |
| Gao, Jiang & Yan 2512.23847 [FT] | LAP test on Llama-3.3-70B; headlines → returns; earnings calls → capex | Explains LAP by **measured** corpus properties; open-data models; diversity and duplication |
| Yan et al., DatedGPT 2603.11838 [ABS] | 12 yearly-cut-off 1.3B models; shows look-ahead premium | Uses DatedGPT as a natural experiment on recency × frequency, not as a mitigation |
| Benhenda, Look-Ahead-Bench 2601.13770 [FT] | Alpha decay of agents with standard vs point-in-time LLMs | Event-level, not portfolio-level; data explanation |
| Li et al., FinCAD 2605.24564 [ABS] | Inference-time decoding to suppress memorised outcomes | Diagnosis of the cause; could predict where FinCAD is needed |
| MemGuard-Alpha 2603.26797 [ABS] | Membership inference to filter contaminated signals; reports limits | Uses ground-truth corpus counts instead of MIA guesses; can validate MIA |
| Dimino et al. 2510.05702 [ABS] | Visibility/size bias in Qwen investment preferences | Sub-question I2 measures the data behind it |
| Memorisation propensity (2606.06286) [ABS] | General-domain memorisation vs infini-gram counts on Dolma 3 | Finance outcomes, temporal cut-offs, diversity of contexts |

## 6. Data and access

| Resource | Use | Size | Licence / ToS | Cost | Access test (6 Nov 2026) | Rating |
| --- | --- | --- | --- | --- | --- | --- |
| **OLMo-2-1124-7B**, **Olmo-3-1025-7B** (open weights) | memorisation probes | 7B | Apache-2.0 | free; 1 GPU (A100/L4) | HF API → 200, not gated | easy |
| **Pythia-6.9B (deduped)** | second corpus (Pile) | 6.9B | Apache-2.0 | free | HF API → 200 | easy |
| **DatedGPT 2013…2024 base/instruct** | yearly cut-off natural experiment | 12 × 1.3B | per model card (check) | free | HF API search → 20 repos under `datedgpt/` | easy |
| **infini-gram** counts on Pile, Dolma v1.7, OLMo-2 mixes (and Dolma 3 if served) | F₁–F₃, snippets | API (no download) | free research API | free | `api.infini-gram.io` → **403 from the cloud shell (proxy)**; docs list indexes incl. `v4_piletrain_llama`, `v4_dolma-v1_7_llama`, OLMoE/OLMo-2 mixes; Python package wheel downloads from PyPI | medium (run from Frank's laptop) |
| **Dolma** corpus (for snippet diversity, Src) | metadata, snippet retrieval | sample only | ODC-By | free | HF API → 200, not gated | easy |
| **FineWeb-Edu** yearly slices (DatedGPT's base data) | year-specific frequency, by streaming a sample | sample | ODC-By (per HF card; verify) | free | not tested (large; stream only) | medium |
| **Event list**: firm–dates with |return| > 5% for S&P 500 + AEX firms, 2015–2025 | targets *e*, *y_e* | ~20–50k events | prices: Stooq/Yahoo (personal/research use) | free | Stooq → **timeout from cloud**; to run locally | medium |
| **SEC EDGAR 8-K** filing dates (earnings, Item 2.02) | event typing | free | public domain, fair-access rules | free | `data.sec.gov` → **403 from cloud** (needs User-Agent, non-cloud IP); worked via web fetch in earlier runs | medium |

**Minimum viable dataset:** 3,000 firm–day events (S&P 500, 2016–2023, |r| > 5%) + 3,000 matched non-events; probes on OLMo-2-7B and Pythia-6.9B; infini-gram counts F₁–F₃ on their two corpora. **Fallback:** if the infini-gram API is unavailable, download the free `v4_pileval_llama` index (2.3 GiB) for method development and use Dolma samples streamed from HF for counts; or switch to DatedGPT + FineWeb-Edu sampling only.

**Platform APIs:** no social-media API needed.

## 7. Approach and 30-week plan

**Research question.** Which properties of pretraining data (frequency, diversity of contexts, duplication, recency, source) explain whether a language model memorises the outcome of a stock-market event?

**Sub-questions.**
- **RQ1:** How strongly do mention frequency and co-mention of firm–date–outcome predict LAP and directional recall in OLMo and Pythia?
- **RQ2:** Beyond frequency, does the **diversity** of contexts (number of distinct sources, semantic/stylistic diversity of snippets) and duplication matter? Does it differ by firm size and country (incl. Dutch AEX firms) → visibility prior (I2)?
- **RQ3:** Is the effect causal? (a) DatedGPT cut-off discontinuities; (b) controlled injection in continued pretraining of a small Pythia model.

**Method.** LAP and recall probes with exact log-probs (`vllm`/`transformers`); infini-gram count and CNF queries; snippet retrieval and diversity with `emb-diversity` (Graph Entropy, Vendi); near-duplicate detection (MinHash, `datasketch`); mixed-effects logistic regression; regression discontinuity across DatedGPT cut-offs; small-scale continued pretraining (Pythia-410M, LoRA or full) with injected documents at 1, 4, 16, 64 copies × low/high diversity.

**Baselines.** Firm size and media-coverage proxies alone (does frequency add explanatory power beyond "famous firm"?); random non-event firm-days (placebo); post-cut-off events (should show no recall).

**Metrics.** AUC/pseudo-R² of memorisation predictors; elasticity of recall to log-frequency; incremental R² of diversity over frequency; discontinuity estimates with CIs; for RQ3, recall as a function of injected copies × diversity.

**Chronology / no look-ahead:** all memorisation tests are about past events relative to each model's cut-off; post-cut-off events serve as placebo. Price data for event construction are realised outcomes (that is the point), not features for prediction.

**Human-centred component:** none required; optional small expert check that outcome words in snippets match the event (precision of F₃).

**Week-by-week plan (start 1 Dec 2026):**

| Weeks | Dates | Phase | Work |
| --- | --- | --- | --- |
| 1–3 | 1–21 Dec | Phase 1 | Literature (memorisation, look-ahead, data attribution, diversity measures); event-list design |
| 4–6 | 22 Dec–11 Jan | Phase 1 | Pilot: 300 events; LAP on OLMo-2-7B; infini-gram counts from laptop; check variance in F and M |
| 7–9 | 12 Jan–1 Feb | Phase 1 | Research proposal; power analysis; pre-registration of main regression |
| 10 | 2–8 Feb | **Go/no-go** | Go if pilot shows usable variance in M and working count pipeline |
| 11–14 | 9 Feb–8 Mar | Experiments | Full event set; probes on OLMo-2, Olmo-3, Pythia; counts and snippet retrieval |
| 15–17 | 9–29 Mar | Experiments | RQ1/RQ2 models; diversity and duplication features; visibility-prior analysis |
| 18–20 | 30 Mar–19 Apr | Experiments | RQ3a DatedGPT discontinuities |
| 21–23 | 20 Apr–10 May | Experiments | RQ3b injection study (if time); build LeakScope |
| 24–28 | 11 May–14 Jun | Writing | Thesis; short paper (FinNLP / ACL findings / ICAIF) |
| 29–30 | 15–28 Jun | Writing | Revisions, defence |

## 8. Usable artefact

**LeakScope**: a small tool and dashboard that, for a ticker, date range and open model, reports the memorisation risk per event (LAP), the training-data evidence (counts, example snippets, diversity) and a "safe backtest window" recommendation. Relevant for model-risk teams validating LLM-based research tools (the brief's Accenture context: LLM validation for financial clients).

## 9. Ethics and GDPR
- **Personal data:** none by design (firms and dates). Snippets may contain names of executives or journalists; they are processed transiently for counting/diversity, not stored or published beyond short anonymised examples. Lawful basis: scientific research (Art. 6(1)(e)/Art. 89).
- **Licences/ToS:** corpora used through official search APIs and released indexes; no redistribution of corpus text (the Pile contains copyrighted material; only counts and short quotes). Price data from free sources under their terms (personal/research use).
- **Ethics board:** no human participants → UU ethics/privacy quick scan only.
- **Dual use:** a memorisation map could help someone cherry-pick backtests; publishing it is meant to prevent exactly that.

## 10. Risks and minimum thesis

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| infini-gram API unavailable or rate-limited | medium | Laptop access; local engine with downloadable indexes; streamed Dolma samples |
| Little memorisation in 7B open models (low variance) | medium | Restrict to high-coverage events; add Olmo-3-32B via hosted inference if needed; DatedGPT instruct models are trained on finance prompts |
| Scooped on DatedGPT arm by CUHK group | medium | Lead with OLMo/Pythia + diversity (her angle); DatedGPT arm optional |
| Compute | low–medium | 7B inference on one GPU (UU cluster or Colab Pro); events ≤ 50k |

**Minimum thesis:** RQ1 + RQ2 on OLMo-2-7B and Pythia-6.9B with 3k events, infini-gram counts and snippet diversity, plus the LeakScope prototype.

## 11. Scores
Fit 5 ×3 = 15 · Novelty 5 ×3 = 15 · Data 4 ×2 = 8 · Evaluation 4 ×2 = 8 · Feasibility 3 · AI 5 · Artefact 3 · Industry 4 · Frank 5 → **66 / 75**.

## 12. Questions to ask her
1. Would she see "diversity of contexts" as a meaningful DataDivers construct for memorisation, and which measures from EmbDivBench fit snippet sets?
2. Is a regression on observational corpus counts convincing enough, or does she want the injection experiment (RQ3b) as the core?
3. Compute: can the thesis use the NLP group's GPU resources?
4. Would she like a Dutch angle (AEX/AMX firms, Dutch-language news in the corpora)?
5. Co-supervision with Karnstedt-Hulpuș (who might value the event-level market design) and a 1 December start?
