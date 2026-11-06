# alternative-thesis-dong

Overnight scouting run (6–7 Nov 2026) for an MSc AI thesis at Utrecht University on an **alternative supervision track with Dr. Dong Nguyen** (NLP and Society Lab): ten ideas and five worked-out proposals where her research line (data diversity, language variation, bias measurement, human-centred evaluation) is central and the stock market / financial text is the domain.

**Start here:** `pitch_summary.md` (morning summary, comparison table, recommendation, meeting brief, email draft, other directions).

| File | What it contains |
| --- | --- |
| `pitch_summary.md` | One-page summary of the 5 proposals, comparison table, recommendation (P1 first, P3 second), ½-page meeting brief, email draft (155 words), other directions with links |
| `supervisor_profile.md` | Her 2025–2026 publications (17, with verification tags), recurring methods and evaluation style, stated limitations of her papers, lab members, what she would likely find exciting / unconvincing, what Frank knows from HCML |
| `lit_review_dong.md` | Landscape at the intersection, 2026 first then 2025, six themes (T1–T6) with a crowding map |
| `ideas_10.md` | Ten ideas with pitches, kill tests (queries, findings, verdicts), three killed ideas, scoring table (/75) |
| `proposals/same-question-different-voice.md` | **P1 (72/75)**: sociolinguistic counterfactual audit of LLM investment advice |
| `proposals/memtrace.md` | **P2 (66/75)**: explaining LLM look-ahead memorisation from open pretraining data |
| `proposals/findiv.md` | **P3 (65/75)**: diversity of financial NLP datasets and robustness (with pilot) |
| `proposals/perceived-voice.md` | **P4 (59/75)**: human vs LLM perception of retail-investor language |
| `proposals/robust-or-sensitive.md` | **P5 (58/75)**: robust vs sensitive tasks under retail language variation (with tokenizer pilot) |
| `pilot/findiv_pilot.py`, `pilot/findiv_pilot_results.csv` | Diversity pilot: `emb-diversity` on 500-text samples of five public datasets |
| `pilot/tokenizer_pilot.py`, `pilot/tokenizer_pilot_results.json` | Tokenizer pilot: emoji/cashtag handling by FinBERT, BERT, RoBERTa, OLMo-2 |
| `references.bib` | 69 entries, each with a `note` (verification tag, first-public date, peer-review status) |
| `NOTES.md` | Decision log: repos read, access tests, all queries, decisions, rejected ideas, status |

**Verification legend:** [FT] full text opened · [ABS] abstract/record read · [UNVERIFIED] not opened · [BG] background (older work, not used as evidence that a niche is open or closed). Numbers quoted from papers come from web-fetch reads and should be checked against the PDFs before use in the thesis.

**Reproducing the pilots:** Python ≥ 3.11; `pip install emb-diversity sentence-transformers transformers pandas pyarrow tabulate` (CPU torch is enough); run `python -I pilot/findiv_pilot.py /tmp/findiv_data` and `python -I pilot/tokenizer_pilot.py` from the repo root.
