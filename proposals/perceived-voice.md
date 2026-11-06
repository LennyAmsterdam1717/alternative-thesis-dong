# Proposal 4 — Perceived Voice: do LLMs read retail-investor posts the way investors do?

*Idea I7 in `ideas_10.md` (score 59/75). Themes: T3 retail-investor social media × T5 human-centred evaluation. A direct transfer of Nguyen & Rosseel (2025) to finance. Legend: [FT] full text opened · [ABS] abstract/record · [UNVERIFIED] not opened · [BG] background.*

## 1. Title and one-sentence pitch

**Perceived Voice: human versus LLM social perceptions of language variation in retail-investor posts.**
When a post says "$NVDA gonna rip tmrw 🚀🚀" instead of "I expect NVIDIA to rise tomorrow", do people and LLMs draw the same conclusions about how credible, expert, bullish or "hyped" it is, and do LLM-based monitoring tools inherit or distort those judgements?

## 2. The problem

### 2.1 In plain language

Platforms, brokers and research firms now use LLMs to read thousands of social-media posts about stocks and to summarise "what retail investors think", flag hype or rank posts by credibility. Humans who read these posts do not judge them only on content. The way something is written (spelling, slang, emoji, all-caps) changes how informed, careful, young or trustworthy the writer seems. Dong Nguyen and Laura Rosseel showed in 2025 that LLMs largely share human associations for spelling variation in general tweets (formality, carefulness, age) but differ in the details: LLM ratings are less variable, cluster at round numbers, and match humans worst for age.

In finance these perceptions have consequences. If an LLM systematically treats informal or dialectal posts as less credible, retail voices from some communities are filtered out of sentiment indices and "credible chatter" feeds; if it treats rocket emoji as stronger bullishness than humans do, it overstates hype. Nobody has measured whether human and LLM perceptions of financial posts line up.

**A concrete example.** Two versions of the same post:
> (A) "I think Tesla's delivery numbers next week will beat expectations. Buying some shares."
> (B) "tsla deliveries gonna smash next wk 🚀🚀 loading up"

Readers might rate (B) as more bullish, less credible, written by a younger and less experienced investor. The thesis collects such ratings from a sample of people who invest, collects ratings from several LLMs under the same instructions, and compares them per variation type. A second step checks whether LLM-based tools (credibility ranking, hype flags) treat the variants differently in ways humans would not.

### 2.2 Technical formulation

Stimuli: pairs (*x*, *x′*) where *x′* = φ_k(*x*) applies variation type *k* ∈ {g-dropping/phonetic spelling, abbreviation/vowel omission, lengthening, emoji (🚀💎🙌🐻), finance slang ("tendies", "bagholder"), all-caps, typos, AAE/non-standard grammar}. Attributes *A* = {credibility, expertise, bullishness, hype/promotional intent, writer age, carefulness}.
- Human ratings *h_a(x)* on 0–100 sliders (open-guise paired design as in Nguyen & Rosseel), *N* ≈ 200–250 participants who self-report investing.
- LLM ratings *ℓ_{m,a}(x)* with matched instructions (independent and paired setups), several prompt wordings, repeated to match human rating counts.
- **Main analysis:** Spearman correlation of item means for raw scores and **difference scores** δ_a(x) = r_a(x′) − r_a(x) (the more informative measure per Nguyen & Rosseel); per-type agreement; variance comparison; mixed models with rater and item effects.
- **Downstream test:** for an LLM-based credibility ranking or hype flag *g_m*, measure Δ_g = g_m(x′) − g_m(x) and compare with the human δ: bias = the part of Δ_g not explained by human perception.

## 3. Where the problem comes from

### 3.1 Papers naming the gap

| Paper | Section | Short quote (<15 words) | Paraphrase |
| --- | --- | --- | --- |
| Nguyen & Rosseel (2025), arXiv 2511.23041 [ABS; method read in HTML] | §6.1 | (paraphrase) | Only seven spelling types, three attributes, English; future work: other variation types, social attributes and languages. |
| Nguyen & Rosseel (2025) | §6.3 | (paraphrase) | Study how contextual factors activate social meanings and how rater characteristics/personas affect results. |
| Nguyen & Rosseel (2025) | §6.4 | (paraphrase) | Whether LLMs *should* mirror negative human evaluations of non-standard forms is open. |
| Kapadia et al. (2026), *Trustworthy FinAInce*, arXiv 2609.20989 [ABS] | abstract | (paraphrase) | Advice *style* (AI/expert/forum) shapes trust and reliance; they hold content fixed — the forum style is one level, not decomposed into language features. |
| Kong et al. (2026), arXiv 2602.14233 [FT] | §2.3 | (paraphrase) | "Narrative bias" (persuasive but unsupported text) is rated critical by practitioners. |

### 3.2 Lineage
- Classic sociolinguistics [BG]: matched-guise tests of social meaning (Lambert et al. 1960s; Campbell-Kibler 2010) [UNVERIFIED in this run].
- 2021 [BG]: Nguyen, Rosseel & Grieve on social meaning in NLP (cited in Nguyen & Rosseel 2025).
- 2024 [BG]: Hofmann et al., Nature: matched-guise probing of LLMs for dialect prejudice [ABS].
- 2025: Nguyen & Rosseel (human vs LLM perception of spelling variation); human vs AI investment ratings (Berkeley WP, Aug 2025, [ABS]); GPT-4o credibility of visual posts (arXiv 2504.10878, [ABS]); emoji-sentiment work on StockTwits.
- 2026: financial advice style and trust (Kapadia et al.); emoji transfer in financial social media (Findings ACL 2026); LLM investor simulation fidelity (arXiv 2610.26524).
- **Gap:** perception of *retail-investor language* by humans vs LLMs is not studied.

### 3.3 Transferable gaps from her papers
The thesis extends Nguyen & Rosseel along the three future-work lines they name (new variation types and attributes, context, rater characteristics: investors vs non-investors) and adds a downstream consequence test. It also connects to Hoeken et al. (IWCS 2025) on annotator variation.

### 3.4 Who is working on it now
Her own lab and close collaborators (Rosseel at VUB) are the closest; finance HCI groups (Kapadia et al.) study advice style; emoji-finance groups study sentiment, not perception. **Low scooping risk; high fit.**

## 4. Why Dong Nguyen
- **Builds on:** Nguyen & Rosseel (2025) design, analysis and robustness checks; Nguyen (2025) on LLMs and sociolinguistics; STEL/style work (Wegmann) for describing variants.
- **She contributes:** sociolinguistic stimulus design and theory of social meaning; experimental design for human ratings; analysis practice (difference scores, pseudoword controls).
- **New for her:** finance-specific attributes (credibility, expertise, bullishness, hype) with real-world downstream tools; a rater population defined by investing experience.

## 5. Literature
### (a) Background
Nguyen & Rosseel 2025 [ABS + method]; Hofmann et al. 2024 [ABS]; Nguyen 2025 [ABS]; Wegmann et al. 2025 [FT].
### (b) Closest 2025–2026 papers and differences

| Paper | What they do | How this differs |
| --- | --- | --- |
| Nguyen & Rosseel 2025 (2511.23041) | 70 tweet pairs, 7 spelling types, 217 UK raters; 12 LLMs | Finance posts, finance attributes, more variation types (emoji, slang, AAE), investor raters, downstream tool test |
| Kapadia et al. 2026 (2609.20989) | Vignette N = 285; AI/expert/forum advice styles | Decomposes "forum style" into language features; posts not advice |
| *AI and Perception Biases in Investments* (Berkeley WP 2025) [ABS] | Human vs AI ratings of asset classes | Language variation of posts rather than assets |
| Mahrous & Di Pietro, Findings ACL 2026 [ABS] | Emoji semantics and transfer across communities | Human perception and LLM-human alignment, not classifier transfer |
| Kilian & Kleffmann 2026 (2607.24072) [ABS] | LLM sentiment dimensions (incl. sarcasm) for meme stocks | Validates such LLM dimensions against human perception |

## 6. Data and access

| Resource | Use | Size | Licence | Cost | Access test (6 Nov 2026) | Rating |
| --- | --- | --- | --- | --- | --- | --- |
| Seed posts: `TimKoornstra/financial-tweets-sentiment` (MIT), `ElKulako/stocktwits-emoji` (MIT), TFNS (MIT) | base texts *x* | 80–120 selected, rewritten neutral | MIT | 0 | first one downloaded (38,091 rows) for the FinDiv pilot; others HF API 200 | easy |
| StockTwits 2008–2022 dataset (Li, Al Ansari & Kaufman, JQD:DM 5, 2025, doi 10.51685/jqd.2025.020) | natural examples, anonymised IDs | > 550M posts | article CC BY-NC-ND; data terms not stated | 0 | article page opened; PDF fetch **refused (provenance)**; data host not located → ask authors | medium |
| Human ratings on Prolific (investors filter) | *h_a(x)* | 200–250 participants × ~40 ratings | Prolific ToS; consent | ≈ €1,200–1,800 (≈ 15 min at ≥ £9/h) | not run (needs ethics approval) | medium |
| LLMs (GPT, Claude, Gemini, Llama, Qwen, OLMo) | *ℓ_{m,a}(x)* | ~50k calls | API terms | ≈ €50–150 | OLMo-2/Olmo-3 HF API 200 | easy |
| Live StockTwits API | not needed | — | ToS | — | 200 (returns usernames: personal data) | not used |

**Minimum viable dataset:** 60 base posts × 6 variation types × 2 versions; 150 raters; 6 LLMs. **Fallback:** if funding for Prolific is not available, a smaller UU student sample plus a pre-registered replication with LLMs only (weaker on the human side).

**Platform APIs:** no Reddit/X API needed; seeds come from MIT-licensed HF datasets and are rewritten and anonymised.

## 7. Approach and 30-week plan

**RQ.** How closely do LLM perceptions of language variation in retail-investor posts match human perceptions, and where they diverge, do LLM-based financial monitoring tools treat writers unequally?

**Sub-questions.**
- **RQ1:** For which variation types and attributes do human and LLM difference scores agree (Spearman, per type)?
- **RQ2:** Do investors and non-investors perceive variants differently, and which group do LLMs resemble (rater-characteristic effect, her §6.3 future work)?
- **RQ3:** Do LLM credibility rankings and hype flags penalise or reward variants beyond what human perception predicts?

**Method.** Stimulus construction following Nguyen & Rosseel (neutral seeds, controlled variants, pseudoword controls); pilot free-response study to select attributes (*N* ≈ 60); main slider study (open-guise pairs, attention checks); LLM ratings (independent and paired prompts, 4 wordings); Spearman on raw and difference scores; mixed-effects models; equivalence tests; downstream audit of two LLM "monitoring" prompts and one fine-tuned credibility classifier.

**Baselines.** Trivial baseline (predicting no difference); human split-half reliability as the ceiling; pseudoword control for LLMs.

**Metrics.** Spearman ρ (raw, difference); rating SD; per-type rating drop; ICC for human reliability; Δ_g bias for downstream tools.

**Chronology:** no market prediction; no look-ahead issue.

**Human-centred component:** the core (pre-registered online rating experiment).

| Weeks | Dates | Phase | Work |
| --- | --- | --- | --- |
| 1–3 | 1–21 Dec | Phase 1 | Literature (social meaning, matched guise, finance social media); ethics application drafted |
| 4–6 | 22 Dec–11 Jan | Phase 1 | Stimulus design; free-response pilot (small); LLM pilot |
| 7–9 | 12 Jan–1 Feb | Phase 1 | Proposal; pre-registration; ethics submission |
| 10 | 2–8 Feb | **Go/no-go** | Go if ethics approved/expected and pilot attributes are reliable |
| 11–13 | 9 Feb–1 Mar | Experiments | Main human study on Prolific |
| 14–16 | 2–22 Mar | Experiments | LLM ratings, robustness (pseudowords, prompt wordings) |
| 17–20 | 23 Mar–19 Apr | Experiments | Analyses RQ1–RQ2 |
| 21–23 | 20 Apr–10 May | Experiments | RQ3 downstream audit; dashboard |
| 24–28 | 11 May–14 Jun | Writing | Thesis; paper (ICWSM/EMNLP findings) |
| 29–30 | 15–28 Jun | Writing | Revisions, defence |

## 8. Usable artefact
**Perception gap explorer**: an interactive page showing, per variation type and attribute, human vs LLM ratings with examples, plus a "tool audit" panel where a monitoring prompt can be tested on the variant pairs. Useful for teams building retail-sentiment or social-listening products.

## 9. Ethics and GDPR
- Human participants: informed consent; anonymous Prolific IDs (deleted after payment); optional demographics (age band, investing experience) only; no special-category data collected; fair pay. Requires the UU ethics procedure for studies with human participants (confirm the Faculty of Science route with the supervisor).
- Stimuli are rewritten seeds: no usernames, no verbatim real posts → no personal data of third parties.
- Avoid harm: stimuli containing AAE are created and validated with speakers; results framed to criticise model behaviour, not speakers.
- Licences: MIT seed datasets; LLM terms of service.

## 10. Risks and minimum thesis

| Risk | Mitigation |
| --- | --- |
| Ethics approval or Prolific budget delayed | Start ethics in week 1; budget request to department; fallback student sample |
| Attributes like "credibility" have low human reliability | Free-response pilot; keep reliable attributes only; report ICC |
| High LLM–human correlation everywhere (no story) | Difference scores and per-type analysis usually reveal divergence (as in Nguyen & Rosseel); downstream audit adds a second result |

**Minimum thesis:** RQ1 with 4 variation types × 3 attributes, 150 raters, 4 LLMs.

## 11. Scores
Fit 5 ×3 = 15 · Novelty 4 ×3 = 12 · Data 4 ×2 = 8 · Evaluation 4 ×2 = 8 · Feasibility 3 · AI 4 · Artefact 3 · Industry 3 · Frank 3 → **59 / 75**.

## 12. Questions to ask her
1. Would she (and Laura Rosseel) see this as a welcome extension or too close to ongoing work in her lab?
2. Which finance attributes are worth eliciting (credibility, expertise, bullishness, hype)? Should a free-response pilot decide?
3. Is there departmental budget for a Prolific study of ~€1,500 for an MSc thesis?
4. Investors vs general population as raters: needed, or out of scope?
5. Co-supervision, ethics route and a 1 December start?
