# NOTES.md: decision log (alternative supervision track, Dr. Dong Nguyen)

Run started **Fri 6 Nov 2026, 17:52 CET**, unattended overnight. Branch: `main` (repo was empty at start).
Verification legend used throughout: **[FT]** full text opened · **[ABS]** abstract / record page only · **[UNVERIFIED]** not opened, mentioned but not relied on.
Date rule: a paper's "year" = first public date (arXiv v1 or venue, whichever is earlier). Peer-review status recorded separately.

---

## 0. Setup (6 Nov, 17:52–18:05)

### 0.1 Repositories read

| Repo | Access | What was there | What I reused |
| --- | --- | --- | --- |
| `alternative-thesis-dong` | push | **empty** (no commits) | output repo |
| `HCML-` | read (attached with credentials) | **empty**: GitHub API reports `size: 0`, no branches, "This repository is empty" (checked with `git ls-remote` and `gh api repos/LennyAmsterdam1717/HCML-`). | nothing; course summary rebuilt from other sources (see `supervisor_profile.md` §7) |
| `thesis-proposals` | public read | 1 Nov run: `NOTES.md` (access-test table), `lit_review.md`, `sweep/T1–T8`, kill tests | access-test results (Scholar, arXiv search, ACM DL, DBLP, UU portal blocked; arXiv abs/html, OpenReview API, papers.cool work); D0.5 lesson: only fetch URLs that surfaced in a search result; data checks for EDGAR / 13F / Financial-Statement-and-Notes text |
| `thesis-attempt-2` | public read | 2 Nov run: anchor (Krstev et al. 2026), crowding map, kill tests | access lessons (ScienceDirect, AAAI OJS block web fetch; Springer HTML rate-limits, PDF route works); text-relevant leads: DatedGPT, Look-Ahead-Bench, Köse et al. LLM firm networks, FinReflectKG |
| `thesis-subject-attempt-3` | public read, branch `scouting-ml-stock-2026` (main has only a README) | 2 Nov run: 12-area ML × stock taxonomy, A3 "LLM text → signals", A10 XAI, A11 leakage, A12 company KGs; `future_work_scan.md` | A3/A11 2026 entries as starting points for Phase 1 theme 1 and 4 (NoLBERT 2610.22745, Reddit identity leakage 2610.25468, DatedGPT 2603.11838, ChatGPT-time-capsule 2604.21433, Kirtac 2603.20965, FinLLM-KG 2610.36083, Yılkı 2606.29290); arXiv rate-limit lesson (≤2 parallel abs fetches) |

Earlier memory/project context used: Frank took HCML (COMPAS fairness assignments; an XAI project with ResNet18/CheXpert using Captum and Quantus is on file from his coursework, course attribution of that project unconfirmed).

### 0.2 Reading of the brief (decisions)
- **D0.1** "Her themes applied to finance" is read strictly: an idea qualifies only if a Dong-Nguyen-style contribution (data-centred NLP, bias/robustness measurement, language variation, computational social science, human-centred evaluation) is the core research question; finance supplies the domain and the outcome variables.
- **D0.2** Reused 2026 entries from the earlier repos are re-labelled with the tag they had there ([ABS] mostly). I upgrade them only if I open them again in this run.
- **D0.3** Scoring: weights sum to 15, max 75 (checked). Scores computed by script at the end.

## 1. Phase 0: supervisor profile (6 Nov, 18:05–18:50)

### 1.1 Access tests

| Source | Route | Result | Consequence |
| --- | --- | --- | --- |
| dongnguyen.nl, uu.nl/staff (URLs from the brief) | WebFetch directly | **Refused: PROVENANCE_REQUIRED** (approval prompt nobody can answer overnight) | Same lesson as `thesis-proposals` D0.5: fetch only URLs that surfaced in a search result or an opened page. Worked after a WebSearch surfaced them. |
| dongnguyen.nl/publications.html | WebFetch after search | **Works** | Complete 2025–2026 list |
| PDFs linked on her publications page | WebFetch | **Works** (9 PDFs opened) | [FT] for her papers |
| arXiv abs page linked from her page (2511.23041) | WebFetch | **Refused (provenance)** | Used search-result text instead ([ABS]) |
| UU research portal person page | WebFetch after search | **Works** (shows 5 of 34 outputs; "Supervised Work (2)" not expanded) | Partial |
| nlpsoc.github.io | WebFetch after search | Works | Lab members |
| DBLP person page | WebFetch after search | **Blocked** (Anubis bot wall) | Not retried |
| ACL Anthology author page | WebSearch | Not surfaced (search returns other Nguyens) | Used her own publications page instead |
| **Google Scholar** | **Not attempted**: no Scholar URL surfaced in any search, and a direct fetch would trigger the same unanswerable approval prompt that the tool told me not to repeat. Earlier runs (`thesis-proposals` 1 Nov) logged Scholar as `robots_disallowed`. | Logged once; no workaround. "Cited by" checks left for Frank. |
| UU student-theses repository | WebSearch (2 queries) | Nothing attributable to her | Ask her |

### 1.2 Queries
- `Dong Nguyen Utrecht NLP and Society Lab publications`
- `Dong Nguyen ACL Anthology author page Utrecht`; `aclanthology.org people dong-nguyen 2025 Utrecht "Dong Nguyen"`
- `"Dong Nguyen" Utrecht arXiv 2026 language models` (extended)
- `dongnguyen.nl thesis supervision master students topics`; `studenttheses.uu.nl supervisor "Nguyen, D.P." …`; `studenttheses.uu.nl "Dong Nguyen" thesis NLP`
- `Google Scholar Dong Nguyen Utrecht citations` (to look for a Scholar URL; none surfaced)
- `"Measuring Data Diversity with Embeddings" …`; `Nguyen Rosseel "Social Perceptions …"`; `DataDivers ERC …`; `"Collaborative Growth …"`; `"A Survey on Representing Linguistic Style …"`
- `Utrecht University "Human-centered machine learning" INFOMHCML course fairness explainability`

### 1.3 Decisions
- **D1.1** No finance paper in her record. Every idea must be framed as one of her research problems in a new domain (see `supervisor_profile.md` §6).
- **D1.2** Her strongest 2026 lines are (a) **measuring data diversity** (EmbDivBench, emb-diversity tool), (b) **bias benchmarks with counterfactual templates and prompt-sensitivity checks**, (c) **identity and language change in online communities around trigger events**, (d) **rationales/explanations validated against baselines**. Scoring "fit with her expertise" uses these four as anchors.
- **D1.3** HCML repo empty → course summary built from her homepage, Frank's recorded coursework and public student summaries (secondary; topic list only).
- **D1.4** Status discrepancy: her own site and the research portal say Associate Professor; the UU staff page says assistant professor. I follow the brief (Associate).

## 2. Phase 1: landscape (6 Nov, 18:50–20:15)

### 2.1 Queries (all via WebSearch; "ext" = extended mode)
- T1: `LLM look-ahead bias memorization financial forecasting 2026 arXiv` (ext); `pretraining data frequency memorization firm entities OLMo Dolma infini-gram financial news look-ahead` (ext)
- T2: `financial sentiment analysis robustness domain shift adversarial paraphrase 2026` (ext); `entity bias financial sentiment LLM company name counterfactual substitution 2025 2026` (ext); `"Battle of transformers" adversarial attacks financial sentiment models arXiv …`; `financial sentiment model generalization news to social media StockTwits Reddit register slang emoji out-of-domain evaluation 2026` (ext); `data diversity financial sentiment training data selection robustness out-of-distribution finance NLP 2026` (ext)
- T3: `wallstreetbets language community identity meme stocks computational analysis 2026` (ext); `StockTwits retail investor posts NLP dataset 2025 2026 arXiv sentiment hype coordination` (ext); `wallstreetbets collective identity "we" pronouns linguistic convergence newcomers GameStop computational` (ext); `Reddit wallstreetbets dataset 2025 2026 arXiv LLM meme stock retail coordination language`
- T4: `earnings call transcripts language management evasiveness LLM 2026 arXiv dataset` (ext); `financial NLP benchmarks data quality duplicates annotation disagreement Financial PhraseBank 2025 2026 analysis` (ext); `generative AI written corporate disclosures earnings calls 10-K LLM-generated text detection prevalence market reaction 2026` (ext)
- T5: `LLM financial advice bias investor demographics robo-advisor audit 2026 arXiv` (ext); `dialect African American English non-native English prompt LLM financial advice quality disparity` (ext); `sociolinguistic variation user prompt writing style changes LLM advice quality audit 2026` (ext); `user study trust LLM financial advice explanations retail investors experiment 2026 arXiv overreliance` (ext)
- T6: `central bank communication NLP LLM 2026 FOMC hawkish dovish measurement validity` (ext); `tariff announcements 2025 stock market text analysis LLM news sanctions geopolitical risk measure 2026 arXiv` (ext); `LLM hawkish dovish measurement prompt sensitivity cross-model agreement validity ECB speeches multilingual 2026`

### 2.2 Full texts opened in Phase 1
Gao, Jiang & Yan (2512.23847, PDF), Benhenda (2601.13770, PDF), Kong et al. (2602.14233, HTML first 100k chars), Choukhmane et al. (2608.01607, HTML first 100k chars).

### 2.3 Access results
- arXiv HTML for 2610.23060 (Bakshi et al.): **rate-limited twice** → kept at [ABS] from the abs-page text in search results; not retried.
- ScienceDirect (Battle of Transformers JBF 2026; FRL 2026 10-K AI paper): not fetched (blocked in earlier runs) → abstract from SFI/RePEc pages [ABS].
- SSRN abstracts appear in search results (Entity Neutering, Chen & Wang, Redigolo & Marcarini) → [ABS].
- Tag convention (decision D2.1): **[ABS]** covers abstract text read either from a fetched page or from the paper's own arXiv/ACL/SSRN/publisher page as returned by WebSearch (the earlier runs called the latter `[ABS-s]`). Snippets from aggregators (Pith, papers.cool, ResearchGate) count as [ABS] only when they reproduce the abstract; otherwise [UNVERIFIED].

### 2.4 Decisions
- **D2.2** Six themes kept as given in the brief (T1–T6). Crowding map at the top of `lit_review_dong.md`.
- **D2.3** The three clearest openings for her expertise: T1 × data-centred NLP (memorisation explained by open-corpus frequency), T5 × sociolinguistics (dialect/register of the asker), T4 × DataDivers (diversity of financial NLP datasets → robustness).
- **D2.4** Killed early (not carried to Phase 2): "detect AI-written corporate disclosures and their market effect" (JAR 2026 + two SSRN 2026 papers + FRL 2026); "new evasion benchmark" (three 2026 benchmarks, paid data).

## 3. Phase 2: ten ideas with kill tests (6 Nov, 20:15–21:20)

### 3.1 Kill-test queries (in addition to the Phase 1 queries reused per idea, listed in `ideas_10.md`)
- `open-data language model memorization stock returns firm news frequency training corpus explains look-ahead OLMo Pythia finance` (ext) → I1
- `measuring diversity of financial sentiment datasets embedding diversity cross-dataset generalization FiQA Financial PhraseBank StockTwits` (ext) → I3
- `hype detection retail investor posts validated measure pump and dump social media stocks 2025 2026 annotation` (ext) → I9
- `Roaring Kitty 2024 return GameStop Reddit language analysis 2025 meme stock revival Opendoor social media study` (ext) → I5 (only news coverage; no study)
- `annotator disagreement perspectivist financial sentiment retail versus professional annotators label variation finance NLP` (ext) → I8
- `faithfulness of LLM explanations financial sentiment rationales human analyst evaluation plausibility 2026` (ext) → K1 killed
- `human versus LLM perception financial social media posts credibility bullishness ratings spelling style investors experiment` (ext) → I7
- `LLM financial sentiment bias toward large-cap well-known firms pretraining exposure frequency explains entity bias 2026` → I2
- `robustness financial sentiment classifiers spelling variation slang sarcasm perturbation benchmark CheckList finance tweets` → I4
- Full text opened: Bisharat & Hean 2609.20198 (PDF).

### 3.2 Decisions
- **D3.1** Rejected and replaced: K1 (faithful narratives of stock predictions; 2609.38869), K2 (AI-written disclosures; JAR 2026 etc.), K3 (evasion benchmark; three 2026 benchmarks).
- **D3.2** Background-only prior work (e.g. Lucchini et al. 2022 for WSB identity) is not used to kill an idea, per the rules; it constrains the design (I5 must be cross-episode).
- **D3.3** Scores computed by script (weights sum to 15, max 75). Top five: I6 (72), I1 (66), I3 (65), I7 (59), I4 (58). Five distinct themes covered (T5, T1, T4, T3/T5, T2).
- **D3.4** I3 and I4 overlap in data; kept separate so Frank has a real choice, flagged as mergeable. I2 is offered as a sub-question of I1.

## 4. Phase 3: proposals (6–7 Nov)

### 4.1 Access tests run from the shell (6 Nov, ~21:30)
| Resource | Command | Result |
| --- | --- | --- |
| Hugging Face Hub API (datasets/models metadata) | `curl https://huggingface.co/api/datasets/takala/financial_phrasebank` | **200** (not gated; licence CC-BY-NC-SA-3.0) — HF reachable from the shell, unlike earlier runs' assumption |
| HF datasets: TFNS (`zeroshot/twitter-financial-news-sentiment`, MIT, 10k–100k), `ElKulako/stocktwits-emoji` (MIT, 100k–1M), `winddude/reddit_finance_43_250k` (GPL-3.0), `gbharti/finance-alpaca` (MIT), `pauri32/fiqa-2018`, `ChanceFocus/flare-fiqasa` | HF API | 200, not gated |
| HF models: `allenai/OLMo-2-1124-7B`, `allenai/Olmo-3-1025-7B` (Apache-2.0), `EleutherAI/pythia-6.9b(-deduped)`, `datedgpt/datedgpt-2013…2024-base/-instruct` (20 repos) | HF API | 200, not gated |
| `allenai/dolma` dataset | HF API | 200, licence ODC-By, not gated |
| infini-gram public API `api.infini-gram.io` | curl | **403 (proxy)** from cloud shell → must be called from Frank's machine; Python package `infini-gram` 2.6.0 wheel downloadable from PyPI (local engine for downloaded indexes; small `v4_pileval_llama` index 2.3 GiB free) |
| `emb-diversity` 0.1.0 (her lab's tool) | `pip download emb-diversity` | wheel downloaded OK |
| GitHub: nlpsoc/emb-diversity, liujch1998/infini-gram, allenai/OLMo, SALT-NLP/multi-value, ArthurHeitmann/arctic_shift | `git ls-remote` | all reachable |
| StockTwits public API `api.stocktwits.com/api/2/streams/symbol/GME.json` | curl | **200**, 30 latest messages with `body`, `created_at`, `user.username`, `entities.sentiment.basic` (e.g. "Bullish") — live data are personal data |
| Reddit `reddit.com/r/wallstreetbets/about.json` | curl | 403 (proxy/Reddit blocks cloud IPs) |
| SEC EDGAR (`sec.gov`, `data.sec.gov`) | curl | 403 from cloud shell (needs a declared User-Agent and a non-cloud IP; worked via web fetch in earlier runs) |
| Stooq prices | curl | timeout (000) |
| arxiv.org homepage | curl | 200 |
No large downloads were made (metadata and a 10 kB API response only).

### 4.2 Proposal 1 (I6, Same Question, Different Voice)
- Verified quote in Choukhmane et al. §4.2 by a targeted re-fetch: "the null supply effect does not rule out differential responses to subtler markers of race … such as names, dialect, or contextual cues".
- Added background: Hofmann et al. 2024 (Nature, [ABS]); Multi-VALUE (ACL 2023, [ABS]).
- Decision D4.1: use synthetic situations + validated variety rewrites rather than real user prompts (GDPR and dialect-as-proxy for ethnicity, Art. 9).

### 4.3 Proposal 2 (I1, MemTrace)
- Verified quotes in Gao et al. by targeted re-fetch: App. C Step 5 "confounds in which LAP proxies for entity salience or attention"; §3.2 "We adopt Llama-3.3-70B in this paper for replicability."; §4 "it can be run on any model, any prompt, and any sample".
- DatedGPT is built from FineWeb-Edu filtered by crawl year (arXiv 2603.11838, search text); its authors promise to release data "upon paper acceptance" (HTML v1 text). Models are already on HF (20 repos).
- infini-gram indexes listed in the docs include Pile-train, Dolma v1.7, OLMoE/OLMo-2 mixes; 2606.06286 reports a 52 TB Dolma 3 index (served publicly or not: unverified).
- Decision D4.2: I2 (visibility prior) folded in as RQ2's firm-size/country analysis rather than a separate thesis.
- Decision D4.3: Kodak example kept at "late July 2020" (exact day not verified in this run).

### 4.4 Proposal 3 (I3, FinDiv) — pilot run
- Installed CPU-only torch (download.pytorch.org reachable), `emb-diversity` 0.1.0 (wheel from PyPI) and `sentence-transformers` 6.2 in a venv; models `all-MiniLM-L6-v2` and `AnnaWegmann/Style-Embedding` downloaded from HF.
- Downloaded five small public parquet files via the HF parquet API into `/tmp/findiv_data` (not committed): FPB mirror (4,846 rows), TFNS (9,543), SEntFiN (11,412), financial tweets (38,091), earnings-call sentences (6,851). Original `takala/financial_phrasebank` has no parquet export ("Cannot get the config names") → used `warwickai/financial_phrasebank_mirror`.
- `pilot/findiv_pilot.py` (run with `python -I`), output `pilot/findiv_pilot_results.csv`. n = 500, seed 0. Style Vendi: FPB 2.57, SEntFiN 4.86, calls 5.82, TFNS 9.47, retail tweets 14.51. Semantic Vendi lowest for calls (64.1). Graph Entropy (default params) nearly constant across datasets (3101–3103 semantic) → flagged as a question for her.
- Decision D4.4: label the pilot "feasibility, not a result" everywhere (one seed, small n).

