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

