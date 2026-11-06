# Pitch pack: five thesis proposals on AI and the stock market for Dr. Dong Nguyen

*Phase 4, written 7 Nov 2026 after the overnight run. Details: `supervisor_profile.md`, `lit_review_dong.md`, `ideas_10.md`, `proposals/*.md`. All scores are /75 with the weights from the brief and were computed by script.*

## 1. Morning summary (one page)

**What I found.** Dong Nguyen has no finance papers, so every proposal frames one of *her* 2025–2026 research problems in a financial setting: measuring data diversity (her ERC project DataDivers), treating language variation as signal, counterfactual bias benchmarks with prompt-sensitivity controls, and comparing human with LLM perception. Finance NLP in 2025–2026 is busy, but almost all of it optimises trading signals or detects look-ahead bias. Her kind of contribution is largely missing. Three gaps stood out:
- nobody varies *how the asker writes* when auditing LLM financial advice;
- nobody explains LLM memorisation of market events from the training data itself;
- nobody measures the diversity of financial NLP datasets.

Ten ideas were kill-tested; three others were killed and replaced. The five best are below.

**P1. Same Question, Different Voice (72/75)** — `proposals/same-question-different-voice.md`
Keep a person's financial situation fixed and change only how the question is written (African American English, Indian or Nigerian English, Dutch-L1 English, informal spelling). Then measure whether LLMs recommend a different share of stocks, other products or worse advice. Only differences larger than ordinary rewording count as bias.
- **Gap:** the closest 2026 paper (Choukhmane et al.) finds that about two-thirds of the gender gap in LLM advice comes from *what people write*, and says dialect remains untested.
- **Builds on:** her LREC 2026 hiring-bias benchmark and her 2025 spelling-perception study.
- **Data:** synthetic and public, low cost. **Artefact:** an audit dashboard (VoiceAudit).

**P2. MemTrace (66/75)** — `proposals/memtrace.md`
Use open-data models (OLMo with Dolma, Pythia with the Pile, the yearly DatedGPT models) and corpus counts (infini-gram). The question is which properties of the training data explain whether a model "remembers" how a stock moved: frequency, *diversity of contexts*, duplication or recency.
- **Gap:** the main 2026 look-ahead test says its score may just proxy firm salience; corpus frequency is not measured.
- **Builds on:** DataDivers aim 2 and Du et al. (ACL 2025).
- **Main risks:** heavier engineering, and the infini-gram API is blocked from the cloud, so it must run from a laptop.

**P3. FinDiv (65/75)** — `proposals/findiv.md`
Apply her own `emb-diversity` tool and EmbDivBench recommendations to financial sentiment datasets, then test whether training-data diversity at equal size makes models more robust across registers (news, retail social media, earnings calls).
- **Pilot already run:** on 500 texts per dataset, Financial PhraseBank's style diversity (Vendi 2.6) is about five times lower than retail tweets' (14.5). Graph Entropy hardly separates the datasets, which is a question for her.
- **Data:** all public and already downloaded.

**P4. Perceived Voice (59/75)** — `proposals/perceived-voice.md`
Extend her human-vs-LLM spelling-perception study to retail-investor posts. Do people who invest and LLMs judge credibility, expertise, bullishness and hype the same way when posts use emoji, slang or non-standard spelling? Do LLM monitoring tools then penalise some writers?
- **Fit:** very strong. **Main risk:** needs ethics approval and about €1.5k for a Prolific study.

**P5. Robust or Sensitive? (58/75)** — `proposals/robust-or-sensitive.md`
A controlled benchmark of retail-investor language variation that separates tasks that should ignore variation (sentiment) from tasks that should use it (community, hype). It follows her tokenization paper (Wegmann, Nguyen & Jurgens 2025).
- **Pilot:** FinBERT turns all 15 typical retail emoji (🚀💎🐻…) into the same unknown token.
- Overlaps with 2026 robustness work, so it is best **merged with P3**.

### Comparison

| | P1 Different Voice | P2 MemTrace | P3 FinDiv | P4 Perceived Voice | P5 Robust/Sensitive |
| --- | --- | --- | --- | --- | --- |
| **Total /75** | **72** | 66 | 65 | 59 | 58 |
| Her line it extends | bias benchmarks + sociolinguistics | data-centred NLP (DataDivers) | data diversity (DataDivers) | social meaning of variation | variation & tokenization |
| Closest 2026 work | Choukhmane et al. (names the gap) | Gao, Jiang & Yan; DatedGPT | EmbDivBench (her own); FinMTEB 2025 | Nguyen & Rosseel 2025 (her own) | Turetken & Leippold; Mahrous & Di Pietro |
| Data | synthetic + HF seeds; ~€500 API/raters | open models + corpus counts | 5 public datasets (downloaded) | MIT seeds + Prolific | public datasets |
| Human study | rewrite validation, quality ratings | none | optional | core (ethics needed) | rewrite validation |
| Main risk | closed models change; null result | API access, compute, scoop risk | null link to robustness | budget/ethics | incremental vs 2026 papers |
| Artefact | VoiceAudit dashboard | LeakScope risk tool | FinDiv cards | perception-gap explorer | RetailCheck stress test |
| Accenture/industry | high (EU AI Act, advice) | high (LLM model validation) | medium | medium | medium |

**Recommendation: P1 first, P3 second.**
- **P1** has the clearest gap, named by the closest 2026 paper. It extends two of her most recent papers, is cheap, and fits your background (fairness, EU AI Act, LLM validation) and the Accenture context.
- **P3** is the most "DataDivers" option, uses her own tool, and has a working pilot, so it shows you can execute. It is a safe, low-risk alternative and can absorb P5.
- **P2** is the most ambitious. Mention it as the option if she wants data-centred NLP with a harder engineering core.

## 2. Meeting brief (½ page)

**Opening (2 minutes).** Remind her you took Human-Centered Machine Learning. Say you want a thesis where her methods are central and finance is the domain, not the other way round. Name the two lines of hers you build on: the LREC 2026 bias benchmark plus the 2025 spelling-perception study, and DataDivers / EmbDivBench.

**Lead with two proposals.**
1. **P1 Same Question, Different Voice.** Show the example: the same financial situation written in standard vs informal or dialectal English. Mention the Choukhmane et al. 2026 gap sentence and the "wording floor" borrowed from her Burema et al. paper.
2. **P3 FinDiv.** Show the pilot table (style Vendi 2.6 vs 14.5) and the Graph Entropy observation. Ask whether that matches her group's experience.

Keep P2 (MemTrace) ready if she reacts most to training-data questions.

**What to ask.**
- **Scope:** which of the two she finds most interesting, and whether to merge P3 with P5.
- **Data and budget:** is LLM- or rule-generated dialect text acceptable after speaker validation? Is there budget for a small Prolific study (P1 rewrite check; P4 if chosen)? GPU access for open models?
- **Supervision:** would she be first supervisor? Could a lab member (Wegmann, Su or Ploeger) be the daily contact? Is co-supervision or second reading with Dr. Karnstedt-Hulpuș possible, given your current track?
- **Timing:** is a 1 December 2026 start feasible? Is the go/no-go around week 10 (early February) workable alongside the Accenture internship from January?
- **Output:** would she aim for a workshop or findings paper?

## 3. Email draft (≤180 words)

> **Subject:** Thesis ideas: language variation and data diversity in financial NLP
>
> Dear Dr. Nguyen,
>
> Thank you for agreeing to talk about a possible thesis. I followed Human-Centered Machine Learning and would like a topic where your methods are central and financial markets are the domain.
>
> Two ideas I would like to discuss:
>
> 1. **Same Question, Different Voice.** Do LLMs give different investment advice when the same financial situation is described in another English variety or style (e.g. African American, Indian or Dutch-L1 English, informal spelling)? It builds on your LREC 2026 bias benchmark and your work on spelling variation; a 2026 study on AI advice names dialect as untested.
> 2. **FinDiv.** Applying your emb-diversity tool to financial sentiment datasets and testing whether training-data diversity explains robustness across news, retail social media and earnings calls. A small pilot already shows large differences in style diversity.
>
> I would like to start around 1 December. Would you have time for a meeting in the coming weeks?
>
> Kind regards,
> Frank

*(Body: 155 words incl. greeting and sign-off, counted by script.)*

## 4. Other interesting directions (one line each)

- **Visibility prior:** LLMs favour large, famous firms; measure the training data behind it (Dimino et al. 2025) — <https://arxiv.org/abs/2510.05702>
- **Whose sentiment?** Sentiment as a latent construct with linguistic vs economic validity (Bisharat & Hean 2026) — <https://arxiv.org/abs/2609.20198>
- **Identity across meme-stock episodes:** her ICWSM 2026 identity-emergence design applied to the 2021, 2024 and 2025 meme episodes — <https://www.dongnguyen.nl/publications/Sepahpour-Fard-icwsm2026.pdf>
- **Validated hype measure** against SEC social-media manipulation cases; closest is AIMM (Dec 2025) — <https://arxiv.org/abs/2512.16103>
- **Validity of LLM central-bank stance indices** (prompt sensitivity, cross-model agreement) — <https://arxiv.org/abs/2603.14313>
- **Five "sins" of financial LLM evaluation** (look-ahead, survivorship, narrative, objective, cost) — <https://arxiv.org/abs/2602.14233>
- **Point-in-time models for leak-free research:** DatedGPT's 12 yearly checkpoints — <https://arxiv.org/abs/2603.11838>
- **Look-ahead benchmark for trading agents** — <https://arxiv.org/abs/2601.13770>
- **LLM financial advice and the life cycle** (demand vs supply of advice gaps) — <https://arxiv.org/abs/2608.01607>
- **Reliability of risk questions in AI advice** (classical test theory) — <https://arxiv.org/abs/2610.23060>
- **AI-written disclosures and markets** (accounting; crowded) — <https://ideas.repec.org/a/bla/joares/v64y2026i3p1189-1232.html>
- **AI-generated content in retail forums** (Seeking Alpha, WSB) — <https://www.nber.org/system/files/working_papers/w34807/w34807.pdf>
- **Managerial evasion benchmarks** (EvasionBench) — <https://arxiv.org/abs/2601.09142>
- **Geoeconomic pressure measured from earnings calls with LLMs** (tariffs, sanctions; fits your interest in politics) — <https://business.columbia.edu/sites/default/files-efs/imce-uploads/Research/Research_Papers/GCAP_pressure.pdf>
- **Public StockTwits archive 2008–2022** (550M posts, anonymised IDs) — <https://journalqd.org/article/view/8780>
