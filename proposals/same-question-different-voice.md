# Proposal 1 — Same Question, Different Voice: does the way you write change the investment advice an LLM gives you?

*Idea I6 in `ideas_10.md` (score 72/75). Themes: T5 human-centred evaluation of financial advice × T2 robustness/bias to language variation. Legend: [FT] full text opened · [ABS] abstract/record · [UNVERIFIED] not opened · [BG] background.*

## 1. Title and one-sentence pitch

**Same Question, Different Voice: a sociolinguistic counterfactual audit of LLM investment advice.**
Holding a person's financial situation fixed and changing only *how the question is written* (dialect, non-native English, informal spelling, register), does an LLM recommend a different share of stocks, different products or lower-quality advice?

## 2. The problem

### 2.1 In plain language (for a non-specialist)

Millions of people now ask chatbots how to invest their savings. They do not all write the same way. Some write in African American English, some in Indian or Nigerian English, many Dutch people write English with Dutch word order, and most people write informally, with typos and abbreviations. Language models are trained mostly on standard, edited English, and earlier research outside finance shows they can treat non-standard varieties worse: they give less accurate answers and, when asked to judge people, attach negative stereotypes to dialect speakers even when race is never mentioned.

For financial advice this matters a lot. Equity exposure is the main driver of long-term wealth. A 2026 study with almost 1,000 real users found that the advice women receive recommends about 3 percentage points less in diversified stocks than the advice men receive, and that roughly two-thirds of this gap comes from what people *write*, not from the model reacting to the word "woman". The authors tested race only by inserting "I am Black/Asian/White" and say this does not rule out reactions to subtler markers such as dialect. Nobody has tested that.

**A concrete example.** Two people, both 32, earning €48,000, €15,000 in savings, no debt, investing for retirement:

> (A) *"I am 32 and earn 48k a year. I have 15k saved and no debts. How should I invest for my retirement?"*
> (B) *"im 32 makin bout 48k a year, got like 15k saved up n no debt. how i'm finna invest for when i retire?"*

If the model tells (A) to put 80% in a global index fund and (B) to "keep most of it in a savings account and be careful with stocks", the second person loses tens of thousands of euros over 30 years for no reason other than their way of writing. The thesis measures whether this happens, how big it is compared with ordinary randomness in model answers, which kinds of variation trigger it, and which models are affected.

The study is careful about one trap that Dong Nguyen's own 2026 work exposed: LLM answers change with small wording changes anyway, sometimes more than with the attribute being tested. So every comparison is made against a baseline of "same variety, different wording", and only differences larger than that baseline count as bias.

### 2.2 Technical formulation

Let *s* ∈ 𝒮 be a financial situation (age, income, savings, debt, horizon, goal, stated risk attitude), *v* ∈ 𝒱 a language variety (Standard American English, AAE, Indian English, Nigerian English, Dutch-L1 English, informal/typo-rich SAE, formal register), *τ* ∈ 𝒯 a template/paraphrase, *m* a model and *ε* sampling noise. A request is the text *x = g(s, v, τ)*. The model returns advice *a = m(x; ε)*, from which outcomes are extracted: recommended equity share *y_eq(a)* ∈ [0, 1], risk level, product classes (index funds, single stocks, bonds, cash, crypto), presence of risk warnings, readability and a quality score *q(a)* (rubric-based, human-validated).

**Estimand.** Variety effect for model *m*:
Δ_m(v, v₀) = E_{s,τ,ε}[ y(m(g(s,v,τ))) ] − E_{s,τ,ε}[ y(m(g(s,v₀,τ))) ], with *v₀* = SAE.

**Noise-calibrated bias.** Compare between-variety variance with within-variety paraphrase variance (a mixed model *y ~ variety + (1|situation) + (1|template)*); report Δ_m only when it exceeds the paraphrase-induced spread (the "wording floor"). Tests: permutation tests with Bonferroni/Holm correction (as in Burema et al. 2026), plus equivalence tests (TOST) to show *absence* of bias where relevant.

**Decomposition** (following Choukhmane et al. 2026): separate (i) the *form* effect (same content, different variety; this study's core), (ii) the *content* effect (what different groups typically mention), and (iii) the *label* effect (explicit "I am …" statements), on a subset.

## 3. Where the problem comes from

### 3.1 Papers naming the gap

| Paper | Section | Short quote (<15 words) | Paraphrase |
| --- | --- | --- | --- |
| Choukhmane, de Silva, Lin & Akuzawa (2026), *AI Financial Advice: Supply, Demand, and Life Cycle Implications*, <https://arxiv.org/abs/2608.01607> [FT] | §4.2 | "subtler markers of race … such as names, dialect, or contextual cues" | Their null result for explicit race labels does not rule out reactions to dialect or names; only labels were tested. About two-thirds of the gender gap is "demand", i.e. driven by what users write. |
| Choukhmane et al. (2026) | §3.1 | "are important questions for future work." | Whether advice changes real decisions is left open. |
| Burema, Schuth, Spelt & Nguyen (2026), LREC [FT] | §6 / Future work | "understand and reduce their sensitivity to demographic signals" | Calls for more work on demographic signals in non-English contexts; finds prompt-wording effects that can exceed group effects. |
| Nguyen & Rosseel (2025), arXiv 2511.23041 [ABS] | §1 | "LLM-based insights should ultimately always be validated" (through real human experiments) | Human validation is expected for any claim about social meaning of variation. |
| Wegmann, Nguyen & Jurgens (2025), Findings ACL [FT] | §6 / Conclusion | (paraphrase only) | Calls for studying variation types individually (spelling vs lexical); this thesis does that for advice. |
| Bakshi et al. (2026), *Same Person, Different Advice*, arXiv 2610.23060 [ABS] | abstract | (paraphrase only) | Varies only the risk answer and shows advice swings are largest for under-40s; language form is not varied. |

### 3.2 Lineage (short timeline)

- 2014–2016 [BG]: sociolinguistic NLP shows models perform worse on non-standard varieties (Nguyen et al. 2016 survey on computational sociolinguistics, [UNVERIFIED] in this run).
- 2023 [BG]: **Multi-VALUE** (Ziems et al., ACL 2023, [ABS]) provides rule-based transformations into 50 English dialects and shows QA/MT gaps.
- 2024 [BG]: **Hofmann et al., Nature 633** ([ABS]): "matched guise probing" shows covert dialect prejudice (AAE) in LLM decisions about people.
- 2025: dialect gaps in LLM reasoning and explanations (Zhou et al., arXiv 2503.04099, [ABS]); reward models biased against AAL (Mire et al. 2025, [ABS]); persona-augmented benchmarks show style changes scores (arXiv 2507.22168, [ABS]).
- 2025–2026: LLM financial-advice audits by stated attributes: Choukhmane et al. (2026, [FT]); IFAAB (arXiv 2610.38239, [ABS]); Bakshi et al. (2026, [ABS]); Wang & Gu (2026, [ABS]); asset-preference audit (Wu, 2606.02528, [ABS]); human evaluation of advice style (Kapadia et al., 2609.20989, [ABS]).
- **Gap (2026):** no audit varies the *language variety of the asker* in financial advice.

### 3.3 Transferable gaps from her own papers
- **Burema et al. 2026**: the template-variant and placeholder-order checks become the "wording floor" here; the explicit-descriptor vs first-name contrast becomes explicit label vs dialect.
- **Nguyen & Rosseel 2025**: human vs LLM perception of spelling variation → here, does the LLM's *perception* of the asker (age, education, financial literacy) mediate the advice? (Probe: ask the model to describe the asker.)
- **Wegmann et al. 2025**: robust-vs-sensitive framing. Advice *should* be robust to form when content is identical; it may legitimately adapt *tone* (sensitivity) — the thesis separates the two.
- **Nguyen & Ploeger 2025**: the evaluation set's own diversity is measured and reported (variety, balance across varieties).

### 3.4 Who is working on it now and how close
- Choukhmane, de Silva et al. (MIT/Stanford, finance): closest; they could extend to dialect. Their data are real user prompts (not released as far as seen), one main model.
- Bakshi et al. (2026), Mahajan (IFAAB, 2026), Wang & Gu (2026): persona-label audits; methodologically close, different factor.
- Dialect-bias NLP groups (Stanford/Hofmann; Georgia Tech/Ziems) have the tools but no finance study in the 2025–2026 sample.
**Assessment:** a fast-moving area; a first version should be out (workshop/preprint) by spring 2027.

## 4. Why Dong Nguyen

- **Builds on:** Burema et al. (LREC 2026) for the counterfactual benchmark design and statistics; Nguyen & Rosseel (2025) and Nguyen (2025, *Language and Linguistics Compass*) for the social meaning of variation in LLMs; Wegmann et al. (2025) for variation types and robust-vs-sensitive framing; her HCML fairness content (statistical parity, group metrics).
- **What she contributes:** the sociolinguistic choice of varieties and features (which are socially meaningful, which are just noise), validity of synthetic dialect text, statistical design of bias benchmarks, and the human-validation step.
- **What is new for her:** the financial-advice domain with an economically meaningful outcome (equity share → long-run wealth), and a decomposition of form vs content vs label effects borrowed from economics.

## 5. Literature

### (a) Background to understand it
- Hofmann, Kalluri, Jurafsky & King (2024), *AI generates covertly racist decisions about people based on their dialect*, Nature 633:147–154, doi:10.1038/s41586-024-07856-5 [ABS] [BG].
- Ziems et al. (2023), *Multi-VALUE*, ACL 2023, <https://aclanthology.org/2023.acl-long.44> [ABS] [BG].
- Burema et al. (2026), LREC [FT]; Nguyen & Rosseel (2025) [ABS]; Wegmann et al. (2025) [FT]; Nguyen (2025) [ABS].

### (b) Closest 2025–2026 papers and how this thesis differs

| Paper | What they do | How this thesis differs |
| --- | --- | --- |
| Choukhmane et al. 2026 (arXiv 2608.01607) [FT] | 952 real user prompts; GPT-5.2 advice; life-cycle simulation; demand vs supply decomposition for gender/race labels | Varies **language form** with content fixed; multiple models incl. open models; wording-floor calibration; dialect and non-native English |
| Bakshi et al. 2026 (2610.23060) [ABS] | 7 LLMs, 800 household profiles, only risk answer varied; classical test theory | Varies the *variety* not the answer; adds quality and tone outcomes |
| Mahajan 2026, IFAAB (2610.38239) [ABS] | 31,734 GPT-4o responses; Indian personas by gender/caste/etc. (labels) | Labels vs form; multi-model; European/Dutch angle |
| Wang & Gu 2026 [ABS] | Two-sided demographic audit (investors and fund managers) | Form, not labels |
| Zhou et al. 2025 (2503.04099) [ABS] | AAE vs SAE prompts reduce LLM reasoning accuracy and explanation sophistication | Financial advice with an economic outcome; several varieties |
| Persona-augmented benchmarking 2025 (2507.22168) [ABS] | Persona rewrites change benchmark scores | Advice domain; validated dialect rewrites; bias interpretation |

## 6. Data and access

| Dataset / resource | Use | Size | Licence / ToS | Cost | Access test run (6 Nov 2026) | Rating |
| --- | --- | --- | --- | --- | --- | --- |
| **Synthetic situations** from public household-finance profiles (age, income, savings, debt, horizon; ranges calibrated to public Eurostat/SCF summary tables) | core factor *s* | 150–300 situations | own data | 0 | Built in-house; no external access needed | easy |
| **Seed questions** from public finance Q&A: `gbharti/finance-alpaca` (MIT, 10k–100k rows), `winddude/reddit_finance_43_250k` (GPL-3.0, 250k post/comment pairs from 43 finance subreddits) | realistic phrasing templates *τ* | sample 500 | MIT; GPL-3.0 (Reddit-derived: personal data, see §9) | 0 | `curl https://huggingface.co/api/datasets/...` → **200**, not gated; licence tags read; parquet URLs listed | easy |
| **Multi-VALUE** dialect transformation code (50 dialects, 189 features) | generate *v* variants | — | open source (GitHub SALT-NLP/multi-value) | 0 | `git ls-remote https://github.com/SALT-NLP/multi-value` → HEAD f93d0ed | easy |
| **LLM rewrites + human validation** for AAE, Indian, Nigerian, Dutch-L1 English, informal SAE | naturalness/meaning check | ~600 items rated by 3 speakers each | Prolific ToS; consent | ≈ €600–900 | Not run (needs ethics approval first) | medium |
| **Models**: GPT-4o-mini / current GPT, Claude Haiku, Gemini Flash (APIs); open: Llama-3.x-8B/70B, Qwen-2.5/3, OLMo-2-7B (`allenai/OLMo-2-1124-7B`, Apache-2.0, not gated), EuroLLM-9B, GEITje | audited systems | ~150k calls | API terms | ≈ €150–400 API + free GPU (UU or Colab) | HF model API → 200, licence apache-2.0, `gated=False` for OLMo-2 and Olmo-3 | easy |
| **Expert rating** of advice quality (finance-literate raters, 3 raters × 300 answers) | validate *q(a)* and LLM-judge | 900 ratings | consent | volunteers or €300 | Not run | medium |

**Minimum viable dataset:** 150 situations × 5 varieties (SAE, AAE, Indian English, Dutch-L1 English, informal SAE) × 4 templates × 3 seeds × 4 models = 36,000 responses, with human validation of 300 rewrites. **Fallback:** only Multi-VALUE rule-based variants (no human rewrite study) and two open models run locally; still answers RQ1.

**Platform API situation (honest):** this proposal does not need Reddit or X APIs; Reddit-derived seed text comes from an existing Hugging Face dataset and is used only as phrasing templates after paraphrasing. Reddit's API requires approval and restricts commercial and AI-training use; X's API is paid. Neither is needed.

## 7. Approach and 30-week plan

**Research question.** Do LLMs give systematically different investment advice to requests that differ only in language variety and style, beyond the variation caused by ordinary rewording?

**Sub-questions.**
- **RQ1 (existence and size):** For which varieties, models and outcomes (equity share, product type, risk warnings, quality) is the variety effect larger than the wording floor?
- **RQ2 (mechanism):** Is the effect mediated by what the model infers about the asker (age, education, financial literacy, origin), measured by asking the model to describe the asker (matched-guise probing)?
- **RQ3 (mitigation and human view):** Do simple mitigations (system prompt "answer independent of writing style", normalising the request before answering) close the gap, and do human raters judge the differing answers as differing in quality?

**Method.** Counterfactual factorial design *s × v × τ × m × seed*; structured extraction of outcomes with a second LLM pass validated against human coding on 300 items (Cohen's κ); mixed-effects models with random intercepts for situation and template; permutation tests (Holm-corrected); equivalence tests; the asker-perception probe for RQ2 (mediation analysis); mitigation conditions for RQ3.

**Libraries.** Python, `multi-value`, `transformers`/`vllm` for open models, provider SDKs, `statsmodels`/`pymer4` for mixed models, `emb-diversity` (her lab's tool) to report the diversity of the generated prompt set, `pandas`, `streamlit` for the artefact.

**Baselines.** (i) Same-variety paraphrases (wording floor); (ii) explicit-label condition ("I am a Nigerian-born …"); (iii) no-situation control (to see default advice); (iv) human-advisor reference answers for a small subset (optional).

**Metrics.** Δ equity share (pp) and its 95% CI; statistical parity difference for "recommends equities ≥ 50%"; product-mix divergence (Jensen–Shannon); risk-warning rate; readability (Flesch, sentence length); quality score agreement (κ, Spearman with human ratings).

**No look-ahead issue:** the study involves no market prediction; all outcomes are advice properties. Model versions and dates are logged because closed models change.

**Human-centred component:** (1) native/fluent speakers rate naturalness and meaning preservation of rewrites; (2) finance-literate raters judge quality of paired answers (blind to variety).

**Week-by-week plan (start 1 Dec 2026; 30 weeks; Accenture internship from early January 2027 means ~2.5 thesis days/week from January):**

| Weeks | Dates | Phase | Work |
| --- | --- | --- | --- |
| 1–3 | 1–21 Dec | Phase 1 | Literature review (dialect bias, advice audits, counterfactual bias benchmarks); define constructs and outcomes; ethics quick scan submitted |
| 4–6 | 22 Dec–11 Jan | Phase 1 | Pilot: 20 situations × 3 varieties × 2 models; build extraction pipeline; estimate wording floor |
| 7–9 | 12 Jan–1 Feb | Phase 1 | Write research proposal; power analysis from pilot; pre-register hypotheses (OSF) |
| 10 | 2–8 Feb | **Go/no-go** | Proposal defence. Go criterion: pipeline works, pilot κ ≥ 0.7 for extraction, ethics approved |
| 11–14 | 9 Feb–8 Mar | Experiments | Generate and validate variety rewrites; Prolific naturalness study |
| 15–18 | 9 Mar–5 Apr | Experiments | Full runs (RQ1), all models |
| 19–21 | 6–26 Apr | Experiments | RQ2 perception probe and mediation; RQ3 mitigations |
| 22–23 | 27 Apr–10 May | Experiments | Expert quality rating; build VoiceAudit dashboard |
| 24–28 | 11 May–14 Jun | Writing | Thesis chapters; workshop paper draft (e.g. NLP+CSS, FinNLP, or a FAccT/ACL findings submission) |
| 29–30 | 15–28 Jun | Writing | Revisions, defence preparation |

## 8. Usable artefact

**VoiceAudit**: an open-source audit harness plus a Streamlit dashboard. A user plugs in a model endpoint, picks varieties and situations, and gets a parity report (Δ equity share with CIs against the wording floor, product mix, risk warnings, example pairs). Useful as a pre-deployment fairness check for banks' and robo-advisors' chat assistants (model validation under the EU AI Act and consumer-protection rules).

## 9. Ethics and GDPR

- **Personal data:** core data are synthetic. Reddit-derived seed texts contain no usernames in the HF dataset fields used, but posts may still be identifiable; they are used only as phrasing inspiration, paraphrased, never published verbatim. Lawful basis for any residual processing: public-interest/scientific research (GDPR Art. 6(1)(e) with Art. 89 safeguards, per UU policy); data minimisation; stored on UU storage.
- **Special categories:** dialect can act as a proxy for ethnic origin (Art. 9). No real person's dialect is processed; all variety texts are synthetic or produced by consenting raters. Results are reported at the variety level, framed carefully to avoid reinforcing stereotypes.
- **Human participants:** Prolific raters and expert raters give informed consent; no identifying data beyond Prolific IDs (deleted after payment); fair pay (≥ UK living wage equivalent). **Ethics:** UU Faculty of Science requires an ethics and privacy check for studies with human participants; submit the quick scan in week 1 (exact procedure to confirm with the supervisor).
- **Terms of service:** API providers allow research use; outputs are not used to train competing models. Reddit-derived data under GPL-3.0 dataset licence; Reddit's own terms restrict commercial use, which this is not.
- **Dual use:** the audit could be used to "game" models; low risk; the benefit (detecting unfair advice) dominates.

## 10. Risks and minimum thesis

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| No effect beyond the wording floor | medium | A well-powered null with equivalence tests is still a publishable result (and good news for users); report per-model results, which will likely differ |
| Synthetic dialect text is unnatural (caricature) | medium | Human naturalness ratings; drop items below threshold; compare rule-based vs LLM vs human-written variants |
| Closed models change during the study | high | Log versions/dates; include open models as fixed reference; run the main batch in a short window |
| Prolific dialect-speaker recruitment is hard | medium | Use Multi-VALUE gold sets and fewer varieties; recruit through UU networks |

**Minimum thesis:** RQ1 on 3 varieties × 2 open models + 1 API model with Multi-VALUE rewrites, wording-floor calibration, and the dashboard. Feasible by week 20 even with internship load.

## 11. Scores (from `ideas_10.md`)

Fit 5 ×3 = 15 · Novelty 5 ×3 = 15 · Data 5 ×2 = 10 · Evaluation 4 ×2 = 8 · Feasibility 5 · AI relevance 5 · Artefact 4 · Industry 5 · Frank's fit 5 → **72 / 75**.

## 12. Questions to ask her

1. Which varieties are sociolinguistically most defensible for an English-language finance audit (AAE, Indian, Nigerian, Dutch-L1, informal spelling)? Would she want a Dutch-language arm (Dutch vs English requests, or regional Dutch)?
2. Is LLM- or rule-generated dialect text acceptable if validated by speakers, or does she expect human-written variants?
3. How should "advice quality" be operationalised and validated (rubric vs expert ratings vs IRT-style measurement as in Fang et al. 2025)?
4. Does a human rating study fit the ethics procedure and budget she has seen for MSc theses?
5. Is co-supervision with Dr. Karnstedt-Hulpuș possible or desirable (e.g. she is first supervisor, Karnstedt-Hulpuș second reader), and is a 1 December start feasible?
6. Target venue: workshop (FinNLP, NLP+CSS) or main conference findings?
