# Literature landscape: Dong Nguyen's themes × the stock market and financial text (2026 first, then 2025)

*Phase 1 of the alternative-supervision scouting run, 6–7 Nov 2026. Every query is logged in `NOTES.md` §2. Legend: **[FT]** full text opened (PDF/HTML read in this run) · **[ABS]** abstract or record page read (the fetched page, or the paper's own arXiv/ACL/SSRN/publisher page text returned by search) · **[UNVERIFIED]** seen only in a snippet or secondary source; not relied on. "PR" = peer-reviewed, "pre" = preprint. Older work is labelled **[BG]** (background) and never used as evidence that a niche is open or closed. Entries carried over from `thesis-subject-attempt-3` keep their earlier tag unless re-opened.*

---

## 0. Crowding map (summary)

| # | Theme (her line → finance) | 2025–2026 papers found (sample, not census) | Dominant groups / venues | Shared benchmarks / data | Crowding | Open angle that is *hers* |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Training-data influence, contamination, look-ahead / memorisation in LLM forecasting | **~15** (2026: ≥10) | Finance departments (CUHK, Chicago Booth, Florida/Lopez-Lira, NYU); q-fin.GN / cs.CL preprints; JF/RFS-style working papers | Bloomberg/RavenPack headlines, earnings calls, S&P 500; Llama-3.x, GPT checkpoints; DatedGPT, PiT-Inference models | **High** for "detect/mitigate look-ahead in returns" | **Explain memorisation from the training data itself** (frequency of firm–event pairs in an open corpus), which the main 2026 test paper explicitly does not measure |
| T2 | Robustness and bias of financial sentiment/NLP (variation, domain shift, paraphrase, fairness across firms) | **~12** | UZH/SFI (Leippold), Japanese finance-NLP groups, entity-bias auditors; FRL, JBF, Frontiers AI, ACL Findings | FPB, TFNS, SEntFiN, FiQA, StockTwits self-labels | **Medium**: adversarial paraphrase and firm-name bias are taken; **language-variation** (register, community slang, dialect) is thin | Robust-vs-sensitive split (Wegmann et al. 2025) applied to financial registers; diversity of training data as the cause |
| T3 | Retail-investor social media as CSS (variation, community dynamics, meme stocks, hype) | **~8** in 2025–2026 (+ a large 2021–2023 GME wave as BG) | Mixed: finance (retail attention), CSS (ICWSM 2022, RSOS 2022, BG), 2026 ICAIF/ACL Findings | WSB via Pushshift dumps, StockTwits (JQD:DM 2025 public dataset), StockEmotions | **Medium-low** in 2025–2026 (the GME wave is 2021–2023) | Language change and identity *across* meme episodes (2021 → 2024 → 2025) with market data as an external criterion; sociolinguistic robustness of retail sentiment |
| T4 | Earnings calls / 10-K / news language; data diversity of financial NLP benchmarks | **~12** | Accounting (JAR, SSRN), cs.CL benchmark papers (EvasionBench, DualEvasion), FLAME (ACL Findings 2025) | Capital IQ transcripts (paid), EarningsCall API (commercial), EDGAR (free), FPB | **High** for evasion detection and "AI-written disclosures"; **empty** for *measuring the diversity of financial NLP datasets* | DataDivers measures (EmbDivBench, `emb-diversity`) applied to financial benchmarks and linked to model robustness |
| T5 | Human-centred evaluation: explanations for analysts, trust, LLM financial-advice quality | **~12** (2026 surge) | Finance/HCI (MIT Sloan, Stanford, arXiv cs.CL/HC); audit papers from India, US | Synthetic personas, Prolific vignettes, SCF-type household profiles | **Medium-high** for persona audits; **open** for *how the asker writes* (dialect, non-native English, register) | Burema-style counterfactual audit where the varied factor is the user's language variety, not a stated demographic label |
| T6 | Political/geopolitical text and markets (central banks, tariffs, sanctions) | **~10** | Central banks (Fed, ECB, BIS, IMF), finance (Clayton–Coppola–Maggiori), MDPI/arXiv | FOMC statements, BIS speeches, Shah et al. hawkish–dovish set | **High** for stance measurement; validity checks thin | Construct-validity audit of LLM stance measures (prompt sensitivity, cross-model agreement, criterion validity) |

**Reading of the map.** The intersection of finance and NLP in 2025–2026 is busy, but almost all of it optimises or detects something *for the trader*: return signals, look-ahead adjustment, evasion scores. Her contribution type (measuring a construct validly, explaining model behaviour from training data, treating language variation as signal, counterfactual bias audits with prompt-sensitivity controls) is **largely absent**. The three clearest openings are (i) T1 × data-centred NLP (memorisation explained by corpus frequency), (ii) T5 × sociolinguistics (dialect/register of the user), and (iii) T4 × DataDivers (diversity of financial NLP datasets → robustness).

---

## T1. Training-data influence, contamination and look-ahead / memorisation

### 2026
- **Gao, Jiang & Yan — *Detecting Lookahead Bias in LLM Forecasts*.** <https://arxiv.org/abs/2512.23847> · first draft Dec 2025, v2 12 Jun 2026 · pre (q-fin.GN) · **[FT]**. Lookahead Propensity (LAP) = probability mass on "up/down" for a date-only recall query (firm, ticker, date). Llama-3.3-70B, Bloomberg headlines 2012–2023 and earnings calls 2006–2020; a positive LAP × signal interaction indicates memorisation. *Gaps stated or visible:* single model (§3.2); LAP "may proxy for salience or attention" (App. C); **pretraining corpus frequency is not measured**; no firm-level predictors of memorisation tested. → Closest work for idea D1 (see `ideas_10.md`). First public date is Dec 2025, so it counts as 2025 for the recency rule, with a 2026 revision.
- **Benhenda — *Look-Ahead-Bench*.** <https://arxiv.org/abs/2601.13770> · 20 Jan 2026 · pre · **[FT]**. Alpha decay of LLM trading agents in-sample (2021) vs out-of-sample (2024); point-in-time "Pitinf" models barely decay, standard Llama/DeepSeek lose 15–22 pp. Five stocks only; Pitinf models proprietary.
- **Kong, Lee, Hwang, Lopez-Lira, Levy, Mehta, Wen, Choi, Lee & Zohren — *Evaluating LLMs in Finance Requires Explicit Bias Consideration*.** <https://arxiv.org/abs/2602.14233> · 15 Feb 2026 · pre (position) · **[FT]** (first 100k chars). Five "sins" (look-ahead, survivorship, narrative, objective, cost); review of 164 papers 2023–2025 finds 26.8% acknowledge look-ahead; recommends entity-substitution tests and disclosure of pretraining cut-off dates. No empirical test of the framework.
- **Yan, Tang, Gao, Jiang & Lu — *DatedGPT*.** <https://arxiv.org/abs/2603.11838> · 12 Mar 2026 (v2 23 Jul) · pre · [ABS] (carried over). Twelve 1.3B LMs with annual cut-offs; checkpoints on Hugging Face (`hf.co/datedGPT`, per earlier run). **A time-stamped model family with known training cut-offs: usable as a controlled testbed.**
- **MemGuard-Alpha** — *Limits of Membership Inference for Detecting and Filtering Memorization-Contaminated Signals in LLM-Based Financial Forecasting*. <https://arxiv.org/abs/2603.26797> · Mar 2026 · pre · [ABS]. Membership-inference attacks to filter memorised alpha; reports limits of MIA.
- **Li et al. — *Summoning the Oracle to Slay It* (FinCAD).** <https://arxiv.org/abs/2605.24564> · 23 May 2026 · pre (cs.AI) · [ABS]. Inference-time context-aware decoding to suppress "parametric look-ahead bias", scaled per (entity, date) memorisation.
- **Lehner & Lopez-Lira — *ChatGPT as a Time Capsule*.** <https://arxiv.org/abs/2604.21433> · 23 Apr 2026 · pre · [ABS] (carried over). Frozen checkpoints as time-stamped summaries of public text.
- **Foley et al. — *Reading the News Without Hindsight: NoLBERT Topics*.** <https://arxiv.org/abs/2610.22745> · 15 Oct 2026 · pre · [ABS] (carried over). Pre-1996 pretrained reader; Sharpe not significant vs price-only after search correction.
- **Restatement prediction from earnings calls** — *Do Earnings Calls Help Predict Financial Restatements?* <https://arxiv.org/abs/2611.01123> · Nov 2026 · pre · [ABS]. An LLM names the exact ticker in 66% of masked transcripts: **masking does not anonymise firms**.

### 2025
- **Engelberg, Manela, Mullins & Vulicevic — *Entity Neutering*.** SSRN 5182756, posted 10 Apr 2025, rev. 31 Jul 2026 · working paper · [ABS]. LLM agents mask and paraphrase until an independent LLM cannot recognise the firm; sentiment agreement >95%; look-ahead bounds larger for high-VIX periods and longer texts.
- Lopez-Lira, Tang & Zhu — *The Memorization Problem* (arXiv 2504.14765, Apr 2025) · [UNVERIFIED] (cited by Gao et al.).

### Background (not evidence)
- Glasserman & Lin (2023) on look-ahead in GPT sentiment [BG, UNVERIFIED]; Liu et al. (2024) infini-gram [BG]; Dolma / OLMo open corpora and models (Soldaini et al., ACL 2024) [BG, ABS]; "Generalization vs memorization: tracing LMs' capabilities back to pretraining data" (ICLR 2025, Pythia/OLMo with n-gram frequency) [BG, ABS].

**Crowding.** High for detection and mitigation of look-ahead in return forecasting (≥10 papers in 2026; dominated by finance groups; shared data are commercial headline sets). **What nobody in the sample does:** use a model whose **pretraining data are public** (OLMo/Dolma, Pythia/Pile, DatedGPT) to show *which properties of the training data* (frequency, recency, duplication of firm–event mentions) explain firm-level memorisation. That is exactly the "data-centred NLP" question in DataDivers.

---

## T2. Robustness and bias of financial sentiment and NLP models

### 2026
- **Mahrous & Di Pietro — *Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media*.** Findings of ACL 2026, <https://aclanthology.org/2026.findings-acl.1106/> (arXiv 2605.09414, May 2026) · PR · [ABS]. Twitter and StockTwits in EN/ES/JA/TR; emoji-only models transfer across platforms with small gaps; cross-language transfer hardest; StockTwits native labels + GPT-5 weak labels.
- **FinMoji** — *A Framework for Emoji-driven Sentiment Analysis in Financial Social Media*. <https://arxiv.org/abs/2605.09469> · May 2026 · pre · [ABS]. 528k emoji-containing StockTwits posts; emoji-only F1 ≈ 0.75, text+emoji ≈ 0.88.
- **MSAR** — *Multi-stage adversarial representation learning for robust financial entity-level sentiment analysis*. Frontiers in AI, 11 Sep 2026, doi 10.3389/frai.2026.1888120 · PR · [ABS]. Dual-level adversarial training, FinBERT encoder.
- **DRNash** — *Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis*. Findings of EMNLP 2026, <https://aclanthology.org/2026.findings-emnlp.137/> · PR · [ABS]. Imbalance-robust fine-tuning for sentiment regression.
- **Entity-based bias auditing** — *A Scalable Entity-Based Framework for Auditing Bias in LLMs*. <https://arxiv.org/abs/2601.12374> · Jan 2026 · pre · [ABS]. Templates with sufficient evidence; prediction should be invariant to the entity; includes financial-risk and sentiment tasks; financial companies show model-dependent bias.
- ***When LLMs Go Abroad: Foreign Bias in AI Financial Predictions*.** HBS Working Paper 26-013, Jan 2026 (authors not shown in the snippet; possibly the "Cao et al. 2025" cited by Kong et al.) · WP · [ABS]. US-trained models more optimistic about Chinese firms; synthetic-firm placebo argues for an information-availability mechanism (i.e. a **training-data** explanation).
- **Turetken & Leippold — *Battle of Transformers: Adversarial Attacks on Financial Sentiment Models*.** J. Banking & Finance (2026, ScienceDirect S0378426626000725; SSRN WP Nov 2024) · PR · [ABS] (SFI/RePEc abstract; ScienceDirect blocked). GPT-4o meaning-preserving paraphrases flip FinBERT on ~30% of FPB sentences and ~50% on TFNS/SEntFiN. First public 2024 → treat as background for recency; the journal version is 2026.

### 2025
- *Quantifying Semantic Shift in Financial NLP: Robust Metrics for Market Prediction Stability.* <https://arxiv.org/abs/2510.00205> · Oct 2025 · pre · [UNVERIFIED] (snippet only).
- Nakagawa, Hirano & Fujimoto — *Evaluating Company-specific Biases in Financial Sentiment Analysis using LLMs* (arXiv 2411.00420; 2024) → [BG, ABS]. Bias = sentiment with vs without the company name.

**Crowding.** Medium. Adversarial paraphrase attacks (UZH line) and firm-name/foreign bias are taken. Emoji transfer has a 2026 ACL Findings paper. **Not found:** (a) a robust-vs-sensitive analysis of financial classifiers across *registers* (news vs StockTwits vs WSB vs earnings calls) and *sociolinguistic variation* (slang, spelling, AAE/non-native English in retail posts); (b) any study tying robustness to *measured diversity of the training data*. Both are direct transfers of Wegmann et al. (2025) and DataDivers.

---

## T3. Retail-investor social media as computational social science

### 2026
- **Kilian & Kleffmann — *LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks*.** <https://arxiv.org/abs/2607.24072> · 27 Jul 2026 · pre (cs.CL) · [ABS]. WSB, GME/AMC/NOK; LLM indicators (polarity, bullishness, sarcasm, relevance) vs VADER; heterogeneous relation to returns.
- **Zheng — *More Mentions, Less Information? Identity and Alignment in Reddit Embeddings for Volatility Forecasting*.** <https://arxiv.org/abs/2610.25468> · 18 Oct 2026 · PR (ICAIF '26) · [ABS] (carried over). Most apparent gain of WSB embeddings is firm identity.
- **Ren et al. — *retail co-attention and excess co-movement*.** J. Int. Fin. Markets, Inst. & Money 106 (2026 issue; DOI 10.1016/j.intfin.2025.102258, so first public 2025); arXiv 2605.08726 · PR · [FT] in `thesis-proposals` (check_B). Guba/StockTwits co-attention explains FF5-residual co-movement.
- **Wu, Liu, Chen & Li — *Do News and Social Media Tell the Same Story? Sentiment Spillover Networks*.** <https://arxiv.org/abs/2604.26811> · 29 Apr 2026 · pre · [ABS] (carried over).
- **Negi & Buitelaar — *Semantically Enriching Investor Micro-blogs for Opinion-Aware Emotion Analysis*.** <https://arxiv.org/abs/2605.03092> · 4 May 2026 · pre · [ABS]. Opinion graphs over StockEmotions (10k StockTwits comments).
- **Cambridge *Finance and Society* — *The dynamics of financial subjectivity in digital subcultures on social media platforms*.** 2025/2026, multimethod, ethnographic semantics of WSB emic terms · PR · [ABS] (date unverified).

### 2025
- **StockTwits: Comprehensive records of a financial social media platform from 2008 to 2022.** *Journal of Quantitative Description: Digital Media* 5 (2025) · PR · [ABS] (ResearchGate record). **First publicly available comprehensive StockTwits dataset**, with user-labelled sentiment and parent IDs. Key data source.
- *Retire or get retired: Stocks, memes, and desperation capitalism on r/WallStreetBets* (Telematics & Informatics-type journal, ScienceDirect S0736585324000996; 2024) → [BG, ABS].
- Kmak et al. — *Predicting stock prices with ChatGPT-annotated Reddit sentiment* (arXiv 2507.22922, Jul 2025) · pre · [ABS]. Notes emoji as the largest difference from FinBERT's training text.

### Background (2021–2023 GME wave)
- Lucchini et al., *From Reddit to Wall Street: committed minorities* (R. Soc. Open Sci. 2022) [BG, ABS]: identity = share of "we" among first-person pronouns; identity grows after the squeeze.
- *Short, Colorful, and Irreverent! New users on WSB during the GME short squeeze* (2022) [BG, ABS]: newcomers differ in post length and emoji; regulars shifted towards newcomers.
- Alvarez et al., *Turning Stocks into Memes* (ICWSM 2022 dataset) [BG, ABS]; Mancini et al., *Self-induced consensus* (2022) [BG, ABS]; Buz & de Melo, *WSB beyond GameStop* (2023) [BG, ABS].

**Crowding.** Medium-low for 2025–2026: the computational-social-science wave on WSB was 2021–2023 and centred on a single episode (Jan 2021). The pronoun-identity idea (Lucchini 2022) and newcomer style (2022) are taken for that episode. **Open in 2025–2026:** (i) whether identity markers, outgroup labels and newcomer convergence **replicate across later episodes** (Roaring Kitty's return, May–June 2024; the July 2025 meme revival), using the Sepahpour-Fard ICWSM 2026 toolkit; (ii) **robustness of retail-sentiment pipelines to community language** (emoji, slang, sarcasm) beyond emoji transfer.

---

## T4. Earnings calls, 10-K/8-K and news language; data diversity of financial NLP benchmarks

### 2026
- **EvasionBench** — *A Large-Scale Benchmark for Detecting Managerial Evasion in Earnings Call Q&A*. <https://arxiv.org/abs/2601.09142> · 14 Jan 2026 (v2 4 Feb) · pre · [ABS]. 22.7M Q&A pairs from S&P Capital IQ (paid); 84k training set; 1k expert-labelled test; Eva-4B 84.9% macro-F1. English only.
- **DualEvasion** — *A Shaky Voice Is Not Always a Dodge*. <https://arxiv.org/abs/2608.28040> · 28 Aug 2026 · pre · [ABS]. 505 Q&A pairs, 60 calls, separate text and audio labels; EarningsCall API under commercial licence.
- **Chen & Zhang — *Lie to me: Detecting Managerial Evasiveness via Conversational Audio Encoders*.** <https://arxiv.org/abs/2609.13893> · 12 Sep 2026 · pre · [ABS].
- **EarningsInOne** — *Bridging Quantitative and Qualitative Earnings Signals*. <https://arxiv.org/abs/2606.29734> · Jun 2026 · pre · [UNVERIFIED] (snippet). 5,428 events, S&P 1500.
- **Blankespoor et al. — *Generative AI in Financial Reporting*.** J. Accounting Research 64(3), 2026, 1189–1232 · PR · [ABS]. GPTZero validated; up to 4.5% of new text GAI-written in 2024.
- **Chen & Wang — *More Than Human: Capital-Market Effects of AI-Generated Corporate Disclosure*.** SSRN 5959496 (31 Aug 2026) · WP · [ABS]. AI-written text in earnings-call presentations increases informativeness.
- **Redigolo & Marcarini — *Generative AI and Risk Perception*.** SSRN 7201722 (2026) · WP · [ABS]. AI-written risk factors are more standardised and less firm-specific.
- *The use of AI in 10-K filings* (Finance Research Letters 2026, ScienceDirect) · PR · [ABS].
- **Su, Wegmann, Ploeger & Nguyen (2026), EmbDivBench** · [FT] (see `supervisor_profile.md`). Natural tier = English Wikipedia only.

### 2025
- **FLAME — *Finance Language Model Evaluation*.** Findings of ACL 2025, <https://aclanthology.org/2025.findings-acl.1164.pdf> · PR · [ABS]. Holistic benchmark; quality checks for label consistency, licence, leakage across 20 financial benchmarks.
- **EcoFinBench** (Bank of England Staff WP 1,163, Dec 2025) · WP · [ABS]. Notes possible leakage between FPB test sets and FinBERT's original training.
- *Reasoning or Overthinking* (ICAIF 2025, ACM DL 10.1145/3768292.3770341) · PR · [ABS]. FPB inter-annotator agreement: positive–neutral only 75.2%.
- *Bridging the Data Gap in Financial Sentiment* (ACL SRW 2025) · PR · [ABS]. "Data staleness" of FPB; RAG-driven augmentation.

**Crowding.** High for evasion detection (three 2026 benchmarks, mostly on paid or commercial data) and for "AI-written disclosures" (an accounting race: JAR 2026, two SSRN papers, FRL). **Empty for her angle:** nobody measures the **diversity** of the standard financial NLP datasets (FPB, FiQA, TFNS, SEntFiN, StockTwits sets) along semantic, stylistic and register dimensions, or tests whether diversity predicts cross-dataset robustness. FLAME and EcoFinBench check quality and leakage, not diversity.

---

## T5. Human-centred evaluation: explanations for analysts, trust, financial-advice quality

### 2026
- **Choukhmane, de Silva, Lin & Akuzawa — *AI Financial Advice: Supply, Demand, and Life Cycle Implications*.** <https://arxiv.org/abs/2608.01607> · dated 29 Jul 2026 (first draft Nov 2025) · pre (NBER-style WP) · **[FT]** (first 100k chars). 952 Prolific respondents write their own prompts; GPT-5.2 advice simulated over the life cycle. Advice to women → 2.94 pp lower equity share; **about two-thirds of the gender gap comes from what people write (demand), one-third from the label (supply)**. §4.2: race tested only with explicit labels; "subtler cues such as names or dialect remain unexamined" (paraphrased limitation). → **Direct gap for idea D5.**
- **Bakshi, Bose, Bose & Nandi — *Same Person, Different Advice*.** <https://arxiv.org/abs/2610.23060> · 16 Oct 2026 · pre (cs.CL) · [ABS] (HTML rate-limited twice). Seven LLMs, 800 household profiles, only the risk answer varies; applies classical test theory (reliability discounting cuts swings 2.4–3.3×); swings largest for clients under 40.
- **Mahajan — *IFAAB: Indian Financial Automated Advice Bias dataset*.** <https://arxiv.org/abs/2610.38239> · 28 Oct 2026 · pre (cs.CY) · [ABS]. 31,734 GPT-4o responses; personas vary gender, caste, education, etc.; male-labelled profiles get 60% higher implied resources.
- **Wu — *Auditing Asset-Specific Preferences in Financial LLMs* (Bitcoin).** <https://arxiv.org/abs/2606.02528> · Jun 2026 · pre (q-fin) · [ABS]. Three-level audit: preference, internal representation with causal leverage, downstream allocation.
- **Wang & Gu — *Who Invests, Who Gets Funded: Gender and Racial Bias in LLM-Generated Investment Advice*.** 2026 (journal; ResearchGate record) · PR? · [ABS]. Two-sided audit (investor and fund-manager demographics).
- **Kapadia et al. — *Trustworthy FinAInce: How AI-Mediated Financial Advice is Judged*.** <https://arxiv.org/abs/2609.20989> · 17 Sep 2026 · pre (cs.HC) · [ABS]. Preregistered vignette, N = 285; style (AI/expert/forum) and labels varied with content fixed; expert style preferred.
- *Beyond Behavioral Accuracy: Individual-Level Fidelity in LLM Investor Simulation.* <https://arxiv.org/abs/2610.26524> · 19 Oct 2026 · pre · [ABS]. 80-participant longitudinal paper-trading study.
- **Kong et al. 2026** (T1) also has a 50-respondent practitioner survey on bias criticality.

### 2025
- Winder et al. 2025 (investment biases), Hens & Nordlie 2025 (risk profiling), Takayanagi et al. 2025 (advisory agents) — cited inside Bakshi et al. · [UNVERIFIED].
- *Using Large Language Models for Financial Advice* (2025, ResearchGate) · [ABS]: no gender discrimination found; home bias inherited.

### Background
- Zhou et al., *Disparities in LLM Reasoning Accuracy and Explanations: AAE* (arXiv 2503.04099, Mar 2025) [ABS]; Mire et al., *Rejected Dialects: reward-model bias against AAL* (2025) [ABS]; *Analyzing Dialectical Biases in LLMs for Knowledge and Reasoning* (Findings EMNLP 2025) [ABS]. General-domain dialect bias is established; **none of these is on financial advice.**

**Crowding.** Medium-high and rising fast for persona-based advice audits (≥6 papers in Jun–Oct 2026). All vary *stated attributes* (gender, caste, risk answer). **Open:** varying the *language variety and style of the request* (dialect, non-native English, informal spelling, Dutch-English), with the Burema et al. 2026 template-sensitivity controls. Choukhmane et al. name this gap and show that writing ("demand") drives most of the gender gap.

---

## T6. Political and geopolitical text and markets

### 2026
- **Tang & Yang — *Mind the Shift: Delta-Consistent Scoring of FOMC stance*.** <https://arxiv.org/abs/2603.14313> · 15 Mar 2026 · pre (cs.CL) · [ABS]. Annotation-free stance from frozen LLM representations; notes that LLM-as-judge methods are "highly sensitive to prompt design and decoding parameters".
- **Xu & Vilán — *Assessing Monetary Policy Globally: Evidence from LLMs and Semi-structural Models*.** FEDS Notes, 9 Oct 2026 · official note · [ABS]. Claude Haiku 4.5 vs lexicon on BIS speeches; measures share a cycle but differ in magnitude.
- *Reading Copom's Tone* <https://arxiv.org/abs/2608.07251> · Aug 2026 · pre · [ABS]. The same LLM supplies class and weight; no manually labelled holdout (validity gap noted by a reviewer site).
- Silva, Moriya & Veyrune (IMF, 2025/2026): multilingual sentence transformer over 169 central banks, 74,882 documents (ECB forecasting conference discussion, Mar 2026) · [ABS] (discussant slides).
- Tariff-shock event studies (Research in International Business & Finance 2025; FRL 2025; Quality & Quantity 2026 via arXiv 2510.10877) · [ABS] — price-based, no NLP.

### 2025
- **Clayton, Coppola, Maggiori & Schreger — *Geoeconomic Pressure*.** GCAP working paper (May 2025) · WP · [ABS]. LLM-based firm-level measures of exposure to tariffs, sanctions and export controls from earnings calls; ~60% of US firms report being affected after "Liberation Day".
- Bernoth (DIW DP 2137, Sep 2025) — ECB Communication Stance Indicator · WP · [ABS].
- Hansen & Kazinnik (2023), Shah et al. (2023) hawkish–dovish benchmark → [BG].

**Crowding.** High for stance measurement (central banks themselves publish LLM stance indices). Validity work is the weak spot, but central-bank economists are already discussing it (Thorsrud discussion, DCS critique), so a validity audit is only moderately novel and only moderately Dong-specific (measurement theory, yes; social media and variation, no). Geopolitical exposure from text is owned by the GCAP group.

---

## Cross-cutting observations for idea generation

1. **The "who wrote it and how" dimension is missing everywhere.** Advice audits vary labels; sentiment robustness varies paraphrases; retail studies treat slang as noise. Her core claim, that variation is signal and that models treat varieties unequally, is not yet applied to finance.
2. **Training-data explanations are asserted, not measured.** Foreign bias (HBS 2026), look-ahead (Gao et al.) and entity bias are all attributed to "what the model saw", but no paper in the sample uses an open-corpus model to measure it.
3. **Benchmarks are reused without diversity analysis.** FPB (2014) is still the default; agreement levels and staleness are known, diversity is not measured.
4. **Validated measurement of social constructs (hype, collective identity, evasiveness) against market criteria** would give her CSS line the external criterion that her 2026 ICWSM paper lacked ("causality remains unestablished").
5. **Public data are a real constraint:** Capital IQ transcripts, Bloomberg headlines and RavenPack are paid; StockTwits has a public 2008–2022 dataset; Reddit history exists as community dumps with ToS questions; EDGAR is free. See the data sections of the proposals for access tests.
