# Proposal 5 — Robust or Sensitive? Language variation in retail-investor text and financial NLP models

*Idea I4 in `ideas_10.md` (score 58/75). Themes: T2 robustness of financial NLP × T3 retail social media. Shares data with Proposal 3 (FinDiv); the two can be merged into one thesis. Legend: [FT] full text opened · [ABS] abstract/record · [UNVERIFIED] not opened · [BG] background.*

## 1. Title and one-sentence pitch

**Robust or Sensitive? A controlled benchmark of language variation in retail-investor text for financial NLP.**
Separate the tasks where financial models *should ignore* how retail investors write (sentiment, stance, ticker) from those where they *should use it* (community, register, promotional intent), and test whether today's models get this split right.

## 2. The problem

### 2.1 In plain language

Retail investors write in their own way: "$AMC 🦍💎🙌 not selling", "stonks only go up", "im buyin the dip lol". Financial sentiment models were mostly trained on edited news sentences. When they read retail text, two different things can go wrong. They may **misread the meaning** because they don't understand slang, emoji or spelling ("🐻" means bearish). Or they may **ignore useful signals**: the same slang that confuses a sentiment model is exactly what tells you a post comes from a meme-stock community or is promotional.

Wegmann, Nguyen and Jurgens (2025) showed that design choices such as the tokenizer help some tasks and hurt others: tasks that should be *robust* to language variation (semantics) prefer different settings from tasks that should be *sensitive* to it (style, authorship, dialect). In finance this split has never been tested. Recent 2026 work attacks financial sentiment models with paraphrases written by GPT-4o or studies emoji transfer, but not the full range of retail variation, and not the robust-vs-sensitive distinction.

**A concrete example (from a tokenizer check run for this proposal).** The widely used FinBERT tokenizer (ProsusAI/finbert, a BERT-uncased vocabulary) turns **all 15 of the most typical retail-investor emoji** (🚀 💎 🙌 🐻 🐂 📈 📉 🌕 🦍 🔥 💰 🤡 😂 🩳 🧻) into the same "unknown" token. For FinBERT, "TSLA 🚀🚀" and "TSLA 🐻🐻" look identical, so a bullish and a bearish post can receive the same sentiment. Byte-level tokenizers (RoBERTa, OLMo-2) keep the emoji but split "$TSLA" into 3–4 pieces and "stonks" into 2–3. The thesis builds controlled test sets that change one kind of variation at a time and measures how each model family reacts on robust and on sensitive tasks.

### 2.2 Technical formulation

Base set *X* of retail and news-style financial texts with labels for **robust tasks** *T_R* (polarity, stance towards target ticker, target ticker identification) and **sensitive tasks** *T_S* (register/community: WSB-style vs news; promotional/hype vs informational; author-consistency/authorship verification). Variation operators φ_k: (1) phonetic/abbreviated spelling, (2) lengthening, (3) emoji insertion or replacement with word equivalents, (4) finance slang lexicon (tendies, bagholder, HODL, stonks), (5) cashtag vs company name, (6) all-caps and punctuation, (7) typos/keyboard errors, (8) dialect transformations (AAE, Indian English via Multi-VALUE), (9) sarcasm markers.

- **Robustness** on *T_R*: invariance rate *P(f(φ_k(x)) = f(x))* and ΔF1 under φ_k; label-preserving variants verified by humans on a subset.
- **Sensitivity** on *T_S*: does performance improve when variation is present, and does removing variation (normalisation) destroy the signal?
- **Model factors:** tokenizer type (WordPiece vs byte-level BPE), vocabulary size, pretraining domain (FinBERT vs general vs social-media BERTweet vs LLM), fine-tuning data register.
- **Mitigations:** normalisation, emoji-to-text mapping, register-diverse fine-tuning (link to FinDiv).

## 3. Where the problem comes from

### 3.1 Papers naming the gap

| Paper | Section | Short quote (<15 words) | Paraphrase |
| --- | --- | --- | --- |
| Wegmann, Nguyen & Jurgens (2025), Findings ACL [FT] | Limitations | "could explore interdependencies between tokenizer settings" | Future work: combine tokenizer settings; study variation types individually (spelling vs lexical, §6). |
| Wegmann et al. (2025) | Ethics | (paraphrase) | Data skew toward American, young, male authors; generalisation limited. |
| Mahrous & Di Pietro (2026), Findings ACL [ABS] | conclusion | (paraphrase) | Cross-language and cross-platform transfer hardest; calls for multilingual StockTwits-like data. |
| Turetken & Leippold (2026), JBF [ABS] | abstract | (paraphrase) | Need for "enhanced robustness" of financial classifiers against meaning-preserving attacks. |
| Herrewijnen et al. (2026), EACL [FT] | §6 | "explore attention regularisation for datasets with longer texts" | Spurious-cue reliance can be reduced with rationales; relevant for emoji/cashtag shortcuts. |

### 3.2 Lineage
- 2020–2023 [BG]: robustness checklists and functional tests (HateCheck, co-authored by Nguyen, ACL 2021 [UNVERIFIED in this run]); VALUE/Multi-VALUE dialect transformations (ACL 2023, [ABS]); GPT-3 attacks on dictionaries (FRL 2023, [ABS]).
- 2024–2025 [BG]: emoji embeddings for StockTwits; FinTwitBERT; tokenization sensitivity to language variation (Wegmann et al. 2025, [FT]).
- 2026: paraphrase attacks (JBF 2026), emoji transfer (Findings ACL 2026), MSAR adversarial training (Frontiers AI 2026), FinMoji (arXiv 2605.09469), explanatory decoupling under counterfactual robustness of FinTwitBERT (X-FCA, Research Square 2026, [UNVERIFIED]).
- **Gap:** no controlled, sociolinguistically grounded variation benchmark for financial text that separates robust from sensitive tasks.

### 3.3 Transferable gaps from her papers
Wegmann et al. (2025) robust-vs-sensitive framework and tokenizer analysis; Nguyen & Rosseel (2025) variation types; Herrewijnen et al. (2026) spurious-correlation tests; Du et al. (COLING 2025) OOD robustness via training dynamics (FTFT) as a mitigation baseline.

### 3.4 Who is working on it now
UZH/SFI (adversarial paraphrase), Mahrous & Di Pietro (emoji, cross-cultural), entity-level robustness groups (MSAR). **Medium overlap**; the distinct contribution is the variation taxonomy + robust/sensitive split + tokenizer analysis.

## 4. Why Dong Nguyen
- **Builds on:** Wegmann, Nguyen & Jurgens (2025); her computational sociolinguistics line (variation as signal); Nguyen & Rosseel (2025); FTFT (Du et al. 2025) for robust fine-tuning.
- **She contributes:** a principled taxonomy of variation and of task types; experimental control; experience with robustness benchmarks (HateCheck lineage).
- **New for her:** finance registers and an applied pipeline where errors have monetary consequences; cashtags/emoji as variation types.

## 5. Literature
### (a) Background
Wegmann et al. 2025 [FT]; Ziems et al. 2023 Multi-VALUE [ABS]; Nguyen & Rosseel 2025 [ABS]; Herrewijnen et al. 2026 [FT].
### (b) Closest 2025–2026 papers and differences

| Paper | What they do | How this differs |
| --- | --- | --- |
| Turetken & Leippold, JBF 2026 [ABS] | GPT-4o paraphrase attacks on FinBERT/FinGPT (FPB, TFNS, SEntFiN) | Natural, sociolinguistic variation types, not adversarial optimisation; robust and sensitive tasks |
| Mahrous & Di Pietro, Findings ACL 2026 [ABS] | Emoji semantics and zero-shot transfer across platforms/languages | Nine variation types, controlled one at a time; tokenizer analysis |
| FinMoji (2605.09469) [ABS] | Emoji-only vs text+emoji sentiment on StockTwits | Robustness/sensitivity, not emoji as a feature |
| MSAR, Frontiers AI 2026 [ABS] | Adversarial training for entity-level sentiment | Evaluation benchmark + diagnosis; mitigation compared |
| Kilian & Kleffmann 2026 (2607.24072) [ABS] | LLM sentiment dimensions incl. sarcasm for meme stocks | Controlled tests of whether such signals survive variation |

## 6. Data and access

| Resource | Use | Size | Licence | Cost | Access test (6 Nov 2026) | Rating |
| --- | --- | --- | --- | --- | --- | --- |
| Retail financial tweets (`TimKoornstra/financial-tweets-sentiment`) | base texts, natural variation | 38,091 | MIT | 0 | downloaded (FinDiv pilot) | easy |
| StockTwits emoji (`ElKulako/stocktwits-emoji`) | self-labelled bullish/bearish | 100k–1M | MIT | 0 | HF API 200 | easy |
| FPB, TFNS, SEntFiN | news-style seeds for controlled rewrites | 4.8k / 9.5k / 11.4k | CC-BY-NC-SA / MIT / MIT | 0 | downloaded | easy |
| WSB NER set (`StephanAkkerman/wallstreetbets-ner`), `SocialGrep/reddit-wallstreetbets-aug-2021` | community register examples | small | per card (check) | 0 | appear in HF search (not opened) | medium |
| Multi-VALUE | dialect operators | — | open source | 0 | `git ls-remote` OK | easy |
| Tokenizers: FinBERT, BERT, RoBERTa, OLMo-2 (+ DeBERTa-v3, FinBERT-tone) | tokenizer analysis | — | per model | 0 | **ran `pilot/tokenizer_pilot.py`**: FinBERT and BERT-uncased map 15/15 retail emoji to [UNK]; RoBERTa/OLMo-2 0/15; FinBERT-tone and DeBERTa-v3 failed to load in the cloud venv (missing `sentencepiece`/`tiktoken`) | easy |
| Human validation of label-preserving variants | ~400 items × 3 raters | — | consent | ≈ €400 | not run | medium |

**Minimum viable dataset:** 1,000 seeds × 6 operators, automatic + 300 human-checked; robust tasks: polarity and target; sensitive task: register (news vs retail). **Fallback:** natural-variation contrasts only (retail vs news subsets matched on content via embedding nearest neighbours).

**Platform APIs:** Reddit's API requires approval and restricts commercial/AI use; X's API is paid; the thesis needs neither (HF datasets + rewrites).

## 7. Approach and 30-week plan

**RQ.** Do financial NLP models treat retail-investor language variation correctly, i.e. robustly on meaning tasks and sensitively on register/intent tasks, and which model design choices explain the difference?

**Sub-questions.**
- **RQ1:** How much does each variation type change predictions on robust tasks, per model family?
- **RQ2:** Does variation carry signal for sensitive tasks, and do normalisation steps remove it?
- **RQ3:** Which factors (tokenizer, vocabulary, pretraining domain, fine-tuning register diversity) explain the robust–sensitive trade-off, and do mitigations (emoji-to-text, diverse fine-tuning, FTFT) shift it?

**Method.** Controlled perturbation generation (rule-based + LLM with verification); human label-preservation check; fine-tune BERT-base, FinBERT, RoBERTa, BERTweet, DeBERTa (3 seeds); zero-shot LLMs; invariance and ΔF1 metrics; mixed models with operator and model factors; optional small tokenizer re-training on financial social text (Wegmann et al. setup, small scale).

**Baselines.** Unperturbed performance; random-noise perturbations (control for "any change"); normalised input.

**Metrics.** Invariance rate, ΔF1 per operator, sensitive-task F1 with/without variation, worst-operator F1.

**Chronology:** no market prediction → no look-ahead; if a downstream check links retail sentiment to next-day volume, use a strictly chronological split.

**Human-centred component:** speaker validation of rewrites (label and meaning preserved, naturalness).

| Weeks | Dates | Phase | Work |
| --- | --- | --- | --- |
| 1–3 | 1–21 Dec | Phase 1 | Literature; variation taxonomy; task definitions |
| 4–6 | 22 Dec–11 Jan | Phase 1 | Operators implemented; tokenizer analysis extended (fix DeBERTa/FinBERT-tone loading) |
| 7–9 | 12 Jan–1 Feb | Phase 1 | Proposal; human-validation protocol; ethics quick scan |
| 10 | 2–8 Feb | **Go/no-go** | Go if operators pass a small human check |
| 11–14 | 9 Feb–8 Mar | Experiments | Benchmark construction + validation |
| 15–18 | 9 Mar–5 Apr | Experiments | RQ1/RQ2 across models |
| 19–22 | 6 Apr–3 May | Experiments | RQ3 factors and mitigations |
| 23 | 4–10 May | Experiments | Stress-test tool |
| 24–28 | 11 May–14 Jun | Writing | Thesis; paper (FinNLP / W-NUT / findings) |
| 29–30 | 15–28 Jun | Writing | Revisions, defence |

## 8. Usable artefact
**RetailCheck**: a CheckList-style stress-test suite for financial NLP models (pip package + report), producing per-operator invariance scores and a "robust vs sensitive" profile; usable by teams before deploying sentiment models on social data.

## 9. Ethics and GDPR
- Public MIT/CC datasets; handles masked; no re-identification; dialect operators are applied to synthetic/seed text, not to identify real speakers.
- Human validation: consent, anonymous IDs, fair pay; UU ethics quick scan.
- Avoid stereotyping: dialect results reported as model failures; dialect variants validated by speakers.

## 10. Risks and minimum thesis

| Risk | Mitigation |
| --- | --- |
| Overlap with 2026 robustness papers seen as incremental | Emphasise the robust/sensitive split and tokenizer analysis; merge with FinDiv for a stronger story |
| Synthetic variants unnatural | Human checks; natural-variation contrast set |
| Label preservation hard for slang/sarcasm | Restrict to operators with ≥ 90% human-confirmed label preservation |

**Minimum thesis:** RQ1 + RQ2 on 5 operators, 4 encoders + 2 LLMs, with the tokenizer analysis and RetailCheck prototype.

## 11. Scores
Fit 5 ×3 = 15 · Novelty 3 ×3 = 9 · Data 4 ×2 = 8 · Evaluation 4 ×2 = 8 · Feasibility 5 · AI 4 · Artefact 3 · Industry 3 · Frank 3 → **58 / 75**.

## 12. Questions to ask her
1. Is the robust-vs-sensitive split from Wegmann et al. (2025) the right frame, and which sensitive tasks are most convincing in finance?
2. Should the thesis include tokenizer training experiments, or stay at evaluation level?
3. Would she prefer this merged with FinDiv (diversity of training data as the explanation for robustness)?
4. Is Anna Wegmann available as daily supervisor or advisor?
5. Co-supervision with Karnstedt-Hulpuș and a 1 December start?
