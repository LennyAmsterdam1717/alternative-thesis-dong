# Ten thesis ideas at the intersection of Dong Nguyen's research and the stock market, with kill tests

*Phase 2, 6–7 Nov 2026. Each idea makes one of her research problems the core question and uses finance as the domain and as a source of external criteria. Ideas that only add NLP features to return prediction were excluded by design. Kill-test queries are listed per idea (all WebSearch; "ext" = extended mode). Older work is labelled [BG] and is **not** used to decide whether a niche is open; it only constrains the design. Legend for papers: see `lit_review_dong.md`.*

Themes (from Phase 1): **T1** training-data influence and look-ahead · **T2** robustness and bias of financial NLP · **T3** retail social media as CSS · **T4** financial text and benchmark data diversity · **T5** human-centred evaluation and advice · **T6** political/central-bank text.

---

## I1. MemTrace: explaining firm-level look-ahead memorisation from open pretraining data (T1)

**Pitch.** LLMs "remember" how stocks moved, which inflates backtests. The 2026 detection literature measures this memorisation but only *guesses* why some firm-events are remembered (media salience, firm size). This thesis uses open-data models (OLMo with its public Dolma corpus and infini-gram counts; Pythia/Pile; the DatedGPT family with yearly cut-offs) to measure how often each firm–event pair, and its outcome, appears in the training data, and tests whether frequency, recency, duplication and source mix explain memorisation. It turns a finance nuisance into a data-centred NLP question: how training data shapes model behaviour.

- **Her theme:** data-centred NLP / training-data influence (DataDivers aim 2; Du et al. 2025 on data representations).
- **Stock-market angle:** look-ahead bias in LLM-based backtests; which firms (size, sector, country, media coverage) carry the most contamination risk.
- **Data:** open models and corpora (OLMo 2/3 + Dolma via infini-gram API; Pythia + Pile; DatedGPT checkpoints); firm–event list from SEC EDGAR 8-K filings (free) with dates; daily returns from a free price source (run locally); optional GDELT event counts.
- **Kill test.** Queries: `pretraining data frequency memorization firm entities OLMo Dolma infini-gram financial news look-ahead` (ext); `open-data language model memorization stock returns firm news frequency training corpus explains look-ahead OLMo Pythia finance` (ext); `LLM look-ahead bias memorization financial forecasting 2026 arXiv` (ext).
  Found: Gao, Jiang & Yan (2512.23847, v2 Jun 2026, [FT]) build the LAP memorisation measure on Llama-3.3 but state that LAP may proxy for salience and **do not measure corpus frequency**; Look-Ahead-Bench (2601.13770, [FT]), FinCAD (2605.24564), MemGuard-Alpha (2603.26797) detect or mitigate; DatedGPT (2603.11838) supplies dated models. General-domain papers relate fact frequency to recall in OLMo (Findings EMNLP 2025) but not for financial outcomes.
  **Verdict: survived.** No 2025–2026 paper links financial look-ahead to measured pretraining-data properties.

## I2. The visibility prior: does training-data exposure explain LLMs' favouritism towards large, famous firms? (T1, T2)

**Pitch.** LLMs rate large, well-known firms more favourably and are more optimistic about foreign firms, and papers attribute this to "overrepresentation in pretraining data" without measuring it. This thesis builds an entity-substitution benchmark (same evidence, different firm name, including Dutch AEX and small-cap firms) and correlates the bias with measured name frequency in open corpora. It is a fairness-across-firms study in her counterfactual-audit style.

- **Her theme:** measuring and explaining bias; data-centred explanation.
- **Stock-market angle:** representation bias against small caps and non-US firms in LLM-assisted research.
- **Data:** templates built from FPB/EDGAR sentences; firm lists (S&P 500, Russell 2000 sample, AEX/AMX); open models + infini-gram counts.
- **Kill test.** Queries: `entity bias financial sentiment LLM company name counterfactual substitution 2025 2026` (ext); `LLM financial sentiment bias toward large-cap well-known firms pretraining exposure frequency explains entity bias 2026`.
  Found: Dimino et al., *Uncovering Representation Bias for Investment Decisions in Open-Source LLMs* (2510.05702, Oct 2025, [ABS]) find that confidence tracks firm size and visibility, "likely overrepresented in LLM pretraining data", without measuring it; *Your AI, Not Your View* (2507.20957, Jul 2025, [ABS]) report a "popularity effect"; *When LLMs Go Abroad* (HBS WP 26-013, Jan 2026, [ABS]) foreign bias with a synthetic-firm placebo; an entity-based audit framework (2601.12374, Jan 2026, [ABS]).
  **Verdict: weakened.** Bias is documented three times; only the *measured-frequency explanation* is new, and that overlaps with I1.

## I3. FinDiv: measuring the diversity of financial NLP datasets and whether it predicts robustness (T4, T2)

**Pitch.** Financial sentiment models are trained and tested on a few small, old datasets (Financial PhraseBank 2014, FiQA, TFNS), yet nobody has measured how diverse these datasets are, or whether diversity explains why models break on other registers (StockTwits, Reddit, earnings calls). Using her own `emb-diversity` tool and EmbDivBench findings, the thesis profiles semantic, stylistic and register diversity of the main financial datasets, then trains models on equal-size subsets that differ only in diversity and measures cross-register robustness. It is the first finance "natural tier" for DataDivers.

- **Her theme:** data diversity measurement (Nguyen & Ploeger 2025; Su et al. 2026) and its effect on robustness.
- **Stock-market angle:** reliability of sentiment pipelines that feed trading, risk and monitoring tools.
- **Data:** FPB, FiQA-SA, TFNS, SEntFiN, StockEmotions, the public StockTwits 2008–2022 dataset (JQD:DM 2025), earnings-call sentences from EDGAR exhibits; all public or research-licensed.
- **Kill test.** Queries: `measuring diversity of financial sentiment datasets embedding diversity cross-dataset generalization FiQA Financial PhraseBank StockTwits` (ext); `data diversity financial sentiment training data selection robustness out-of-distribution finance NLP 2026` (ext); `financial NLP benchmarks data quality duplicates annotation disagreement Financial PhraseBank 2025 2026 analysis` (ext).
  Found: FinMTEB (2502.10990, Feb 2025, [ABS]) reports inter-dataset semantic similarity of its embedding benchmark (not within-dataset diversity components, not linked to robustness); FLAME (Findings ACL 2025) and EcoFinBench (BoE 2025) check quality and leakage; several 2026 papers use "diversity" loosely for augmentation (Digital 2026; distillation 2606.18875). Nothing applies variety/balance/disparity measures to financial datasets or tests diversity → robustness.
  **Verdict: survived** (slightly weakened by FinMTEB's inter-dataset similarity analysis).

## I4. Robust or sensitive? Language variation in retail-investor text and financial NLP models (T2, T3)

**Pitch.** Retail investors write "$GME to the moon 🚀🚀 diamond hands", with creative spelling, slang, sarcasm and non-standard English. Some tasks should ignore this variation (what is the sentiment?), others should use it (which community wrote this? is this hype?). Following Wegmann, Nguyen & Jurgens (2025), the thesis builds a controlled variation benchmark (spelling, slang, emoji, AAE and non-native English, sarcasm) on financial text, tests sentiment models and LLMs, and analyses tokenisation of cashtags and emoji.

- **Her theme:** language variation and robustness; tokenisation sensitivity.
- **Stock-market angle:** retail sentiment indices built from social media.
- **Data:** FPB/TFNS seeds rewritten under controlled transformations (LLM + human check); natural tier from StockTwits and WSB.
- **Kill test.** Queries: `financial sentiment model generalization news to social media StockTwits Reddit register slang emoji out-of-domain evaluation 2026` (ext); `robustness financial sentiment classifiers spelling variation slang sarcasm perturbation benchmark CheckList finance tweets`; `financial sentiment analysis robustness domain shift adversarial paraphrase 2026` (ext).
  Found: Mahrous & Di Pietro (Findings ACL 2026, [ABS]) on emoji transfer across platforms and languages; Turetken & Leippold (JBF 2026, [ABS]) on meaning-preserving paraphrase attacks; X-FCA counterfactual robustness of FinTwitBERT (Research Square 2026, [UNVERIFIED]); MSAR (Frontiers AI 2026). None separates robust vs sensitive tasks or tests sociolinguistic varieties.
  **Verdict: weakened.** The adversarial and emoji angles are taken; the sociolinguistic variety angle survives.

## I5. Who is "we" this time? Collective identity across meme-stock episodes (T3)

**Pitch.** Her ICWSM 2026 paper tracks how a collective identity emerges in French vaccine-critical Twitter after a trigger speech (I → we, outgroup labels, newcomer convergence). Meme-stock communities offer the same dynamics with something her paper lacked: market data as an external criterion. The thesis compares identity markers, outgroup labels and newcomer adaptation across three episodes (Jan 2021 squeeze, May–June 2024 "Roaring Kitty" return, 2025 revival) and tests whether they lead or lag trading volume.

- **Her theme:** CSS on social media; identity and language change (Sepahpour-Fard et al. 2026).
- **Stock-market angle:** retail coordination and attention shocks.
- **Data:** Reddit history from community-maintained dumps (Pushshift/Arctic Shift-type archives, ToS caveats); StockTwits 2008–2022 dataset; volume data.
- **Kill test.** Queries: `wallstreetbets collective identity "we" pronouns linguistic convergence newcomers GameStop computational` (ext); `wallstreetbets language community identity meme stocks computational analysis 2026` (ext); `Roaring Kitty 2024 return GameStop Reddit language analysis 2025 meme stock revival …` (ext).
  Found (2025–2026): Kilian & Kleffmann (2607.24072) on LLM sentiment for meme stocks; a *Finance and Society* multimethod study of WSB emic terms ([ABS]); no computational study of identity across the 2024/2025 episodes. Background [BG]: Lucchini et al. (RSOS 2022) already used the "we/I" ratio for Jan 2021; a 2022 study compared newcomer style.
  **Verdict: survived,** with the constraint that the design must be cross-episode (the single-episode version exists as 2022 background).

## I6. Same question, different voice: does the way you write change the financial advice an LLM gives you? (T5, T2)

**Pitch.** People ask chatbots for investment advice in their own words: in African American English, as non-native speakers, in Dutch-English, with typos. A 2026 study found that two-thirds of the gender gap in LLM advice comes from *how people write*, not from stated gender, and explicitly left dialect untested. This thesis builds a Burema-style counterfactual audit in which the financial situation is fixed and only the language variety and style of the request change, measures differences in recommended equity share, risk, product type and advice quality, and controls for template sensitivity.

- **Her theme:** sociolinguistic variation + bias benchmarks with counterfactual templates (Burema et al. 2026; Nguyen & Rosseel 2025; Wegmann et al. 2025).
- **Stock-market angle:** quality and fairness of AI investment advice to retail investors; exposure to equities.
- **Data:** synthetic but realistic request templates seeded from public household profiles (e.g. SCF-style vignettes) and public prompt datasets; dialect/style rewrites validated by humans; LLM APIs and open models.
- **Kill test.** Queries: `LLM financial advice bias investor demographics robo-advisor audit 2026 arXiv` (ext); `dialect African American English non-native English prompt LLM financial advice quality disparity` (ext); `sociolinguistic variation user prompt writing style changes LLM advice quality audit 2026` (ext).
  Found: Choukhmane et al. (2608.01607, Jul 2026, [FT]) — demand-side writing differences explain about two-thirds of the gender gap; dialect "remains unexamined" (§4.2, paraphrased); Bakshi et al. (2610.23060, [ABS]) vary only the risk answer; IFAAB (2610.38239) varies persona labels; Wang & Gu 2026 two-sided audit by labels. General-domain dialect-bias papers (AAE reasoning 2503.04099; *Rejected Dialects* 2025; Findings EMNLP 2025) are outside finance.
  **Verdict: survived.** The gap is named by the closest 2026 paper.

## I7. Perceived voice: do LLMs read retail-investor posts the way investors do? (T3, T5)

**Pitch.** LLMs increasingly summarise and score social-media chatter for investors. Her current paper shows that LLMs largely, but not fully, share human social perceptions of spelling variation. This thesis asks the same for financial posts: do humans (retail investors recruited online) and LLMs judge the credibility, expertise, bullishness and "hype" of StockTwits/Reddit posts the same way, and does that change with spelling, slang and emoji? Disagreements show where LLM-based monitoring misreads retail communities.

- **Her theme:** social meaning of language variation; human vs LLM comparison (Nguyen & Rosseel 2025).
- **Stock-market angle:** LLM-based social-media monitoring and retail sentiment indices.
- **Data:** public StockTwits 2008–2022 dataset sample + controlled variants; human ratings (Prolific, ~150–300 participants); LLM ratings.
- **Kill test.** Queries: `human versus LLM perception financial social media posts credibility bullishness ratings spelling style investors experiment` (ext); `user study trust LLM financial advice explanations retail investors experiment 2026 arXiv overreliance` (ext).
  Found: Kapadia et al. (2609.20989) compare how people judge AI/expert/forum-*style advice*; Berkeley *AI and perception biases in investments* (2025) compare human and AI investment ratings of assets; GPT-4o credibility of visual posts in science/health/politics (2504.10878, 2025). None compares human and LLM perception of retail posts or the effect of spelling/style.
  **Verdict: survived.**

## I8. Whose sentiment? Annotator perspective in financial sentiment labels (T4, T5)

**Pitch.** Financial PhraseBank labels come from 16 business students; positive vs neutral agreement is only 75%. Retail investors, professionals and LLMs may read the same sentence differently. The thesis collects ratings from different annotator groups on a stratified sample, models label variation perspectivist-style, and tests which perspective best predicts market reactions as a criterion.

- **Her theme:** annotator variation (Hoeken et al. 2025), measurement validity.
- **Stock-market angle:** what "sentiment" means for investors.
- **Data:** FPB with agreement levels; new ratings (Prolific + small professional panel); 8-K earnings releases as a criterion.
- **Kill test.** Queries: `annotator disagreement perspectivist financial sentiment retail versus professional annotators label variation finance NLP` (ext); `faithfulness of LLM explanations financial sentiment rationales human analyst evaluation plausibility 2026` (ext).
  Found: *Evaluating Financial Sentiment Analysis with Annotators' Instruction Assisted Prompting* (2505.07871, May 2025, [ABS]) — new expert-annotated WSB dataset motivated by FPB subjectivity; Bisharat & Hean, *Evaluating Financial Sentiment in the Age of AI* (2609.20198, Jul 2026, [FT]) — sentiment as a latent construct with linguistic vs economic validity; general perspectivism surveys (2601.09065).
  **Verdict: weakened.** Sentiment-as-construct and annotation subjectivity are both addressed in 2025–2026; the group-perspective comparison remains open but is narrower.

## I9. A validated hype measure for retail-investor text (T3)

**Pitch.** "Hype" is used everywhere in finance commentary but never defined. The thesis defines hype as a construct (content, convergent and criterion validity), builds a measure from StockTwits/Reddit text, and validates it against self-labels, abnormal attention and SEC enforcement cases of social-media pump-and-dump.

- **Her theme:** NLP for measuring social phenomena with measurement theory.
- **Stock-market angle:** manipulation risk, retail protection.
- **Data:** StockTwits public dataset; SEC litigation releases (free); price/volume.
- **Kill test.** Queries: `hype detection retail investor posts validated measure pump and dump social media stocks 2025 2026 annotation` (ext); `StockTwits retail investor posts NLP dataset 2025 2026 arXiv sentiment hype coordination` (ext).
  Found: *Detecting Pump&Dump Stock Market Manipulation from Online Forums* (Digital Finance, Mar 2025, [ABS]); AIMM multimodal manipulation framework (2512.16103, Dec 2025, [ABS] in `thesis-proposals`); LLM "Retail Investor Buzz" event factors (2508.07408, Aug 2025, [ABS]).
  **Verdict: weakened.** Detection exists; only the measurement-validity framing is new, and labels are scarce.

## I10. Is an LLM hawk a hawk? Construct validity of LLM-based central-bank stance measures (T6)

**Pitch.** Central banks and researchers now publish LLM-based hawkish–dovish indices. The thesis runs a multitrait–multimethod validity study: different LLMs, prompts and languages (ECB, DNB, Fed), inter-model agreement, sensitivity to wording, and criterion validity against yield moves, in the measurement-theory style of her lab.

- **Her theme:** measurement validity of NLP measures; prompt sensitivity.
- **Stock-market angle:** monetary-policy text and bond/equity reactions; fits Frank's interest in politics.
- **Data:** ECB, Fed, BIS speeches and statements (public); Shah et al. hawkish–dovish labels [BG]; FRED yields.
- **Kill test.** Queries: `central bank communication NLP LLM 2026 FOMC hawkish dovish measurement validity` (ext); `LLM hawkish dovish measurement prompt sensitivity cross-model agreement validity ECB speeches multilingual 2026`.
  Found: Tang & Yang DCS (2603.14313, Mar 2026) note prompt sensitivity of LLM-as-judge; Fed FEDS Note (Oct 2026) compares LLM vs lexicon; Copom tone (2608.07251) lacks a labelled holdout; IMF multilingual 169-central-bank classifier discussed at the ECB conference (Mar 2026).
  **Verdict: weakened.** Validity concerns are already voiced by the field; a systematic audit is moderately new, and the fit with her social-media/variation line is weaker.

---

## Killed ideas (replaced)

| Idea | Killing paper(s) | Why |
| --- | --- | --- |
| K1. Faithfulness of LLM explanations for stock-prediction narratives, with human evaluation | *Reasoning Externalization for Faithful LLM Narratives of Stock Return Predictions* (arXiv 2609.38869, Sep 2026, [ABS]); Pratama & Tseng 2026 on credit-risk report fidelity (cited there, [UNVERIFIED]) | Evidence-ID faithfulness plus a human evaluation for exactly this setting. Replaced by I7. |
| K2. Detecting AI-written corporate disclosures and their market effect (style representations) | Blankespoor et al., JAR 64(3) 2026; Chen & Wang (SSRN, Aug 2026); Redigolo & Marcarini (SSRN 2026); FRL 2026 | Prevalence, detection validation and market effects done by accounting. |
| K3. New large-scale managerial-evasion benchmark | EvasionBench (2601.09142), DualEvasion (2608.28040), Chen & Zhang (2609.13893) | Three 2026 benchmarks, mostly on paid transcripts. |

---

## Scoring (1–5 per criterion; weights from the brief; max 75; totals computed by script)

| Idea | Fit ×3 | Novelty ×3 | Data ×2 | Eval ×2 | Feas. ×1 | AI ×1 | Artefact ×1 | Industry ×1 | Frank ×1 | **Total** | Kill-test verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **I6 Same question, different voice** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | **72** | survived |
| **I1 MemTrace** | 5 | 5 | 4 | 4 | 3 | 5 | 3 | 4 | 5 | **66** | survived |
| **I3 FinDiv** | 5 | 4 | 5 | 5 | 5 | 4 | 3 | 3 | 3 | **65** | survived (slightly weakened) |
| **I7 Perceived voice** | 5 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | **59** | survived |
| **I4 Robust or sensitive** | 5 | 3 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | **58** | weakened |
| I2 Visibility prior | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 56 | weakened |
| I10 Stance validity | 3 | 3 | 5 | 4 | 5 | 3 | 3 | 4 | 5 | 56 | weakened |
| I8 Whose sentiment | 5 | 3 | 4 | 4 | 3 | 4 | 2 | 3 | 3 | 55 | weakened |
| I5 Meme identity | 5 | 3 | 3 | 3 | 4 | 3 | 4 | 2 | 4 | 53 | survived (design-constrained) |
| I9 Validated hype | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 51 | weakened |

**Score rationale (short).**
- *Fit* = how central her own methods are (5 = a direct extension of a 2025–2026 paper of hers). I10 scores 3 because it uses her measurement-theory line but not her data or variation line.
- *Novelty* reflects the kill test: 5 = gap named by the closest 2026 paper (I6: Choukhmane §4.2; I1: Gao et al. App. C).
- *Data*: 5 = fully public and small; I5 and I9 lose points for Reddit terms of service and scarce labels; I1 loses one point because the infini-gram API and local GPU inference must work.
- *Feasibility*: I1 is 3 because open-model inference and corpus counting are the heaviest engineering of the ten; I7 and I8 are 3 because of a human study.
- *Industry*: I6 scores 5 (consumer-facing AI advice falls under EU AI Act transparency duties and MiFID suitability rules; Accenture's financial-services clients deploy such assistants); I1 scores 4 (model validation of LLMs in banks).

**Selected for Phase 3:** I6, I1, I3, I7, I4 (top five; themes T5, T1, T4, T3/T5 and T2 → five distinct themes). Note that I3 and I4 share data and could be merged into one thesis; I2 can be added to I1 as a sub-question.
