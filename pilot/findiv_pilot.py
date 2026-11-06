"""FinDiv pilot (Proposal 3): embedding-based diversity of five public financial-sentiment datasets.

Run: python -I pilot/findiv_pilot.py /tmp/findiv_data  (data dir is created; parquet files from the HF Hub)
Samples n=500 texts per dataset (seed 0), short texts only, and reports the default emb-diversity
measures (Graph Entropy, Vendi score, Mean Pairwise Distance) on the semantic (all-MiniLM-L6-v2,
the light alternative model) and style (AnnaWegmann/Style-Embedding) axes.
This is a feasibility pilot, not a result: one seed, one sample size, small n.
"""
import json
import sys
import urllib.request
from pathlib import Path

import pandas as pd
from emb_diversity import measure_diversity

DATA_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/findiv_data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
HF = "https://huggingface.co/api/datasets/{}/parquet/{}/{}/0.parquet"
SETS = {
    # name: (repo, config, split, text column, register)
    "FPB (news, 2014)": ("warwickai/financial_phrasebank_mirror", "default", "train", None, "news"),
    "TFNS (finance tweets)": ("zeroshot/twitter-financial-news-sentiment", "default", "train", "text", "news-tweets"),
    "SEntFiN (headlines)": ("tasksource/sentfin", "default", "train", None, "headlines"),
    "FinTweets (retail tweets)": ("TimKoornstra/financial-tweets-sentiment", "default", "train", None, "retail social"),
    "Earnings calls (sentences)": ("jlh-ibm/earnings_call", "transcript-sentiment", "train", None, "calls"),
}
N, SEED = 500, 0


def load(repo, config, split, col):
    f = DATA_DIR / (repo.replace("/", "__") + f"__{config}__{split}.parquet")
    if not f.exists():
        urllib.request.urlretrieve(HF.format(repo, config, split), f)
    df = pd.read_parquet(f)
    if col is None:  # first string column with mean length > 20 chars
        col = next(c for c in df.columns if (df[c].dtype == object or pd.api.types.is_string_dtype(df[c])) and df[c].astype(str).str.len().mean() > 20)
    texts = df[col].dropna().astype(str)
    texts = texts[(texts.str.len() > 15) & (texts.str.len() < 400)].drop_duplicates()
    return col, len(df), texts.sample(n=min(N, len(texts)), random_state=SEED).tolist()


rows = []
for name, (repo, cfg, split, col, reg) in SETS.items():
    col, n_total, sample = load(repo, cfg, split, col)
    row = {"dataset": name, "repo": repo, "register": reg, "text_col": col, "rows_in_split": n_total, "n_sampled": len(sample)}
    for axis, model in [("semantic", "all-MiniLM-L6-v2"), ("style", "AnnaWegmann/Style-Embedding")]:
        res = measure_diversity(sample, embedding_model=model, cache_dir=str(DATA_DIR / "cache"))
        for m, v in res.items():
            row[f"{axis}:{m}"] = round(float(v["value"]), 4)
    rows.append(row)
    print(json.dumps(row), flush=True)

out = pd.DataFrame(rows)
Path("pilot").mkdir(exist_ok=True)
out.to_csv("pilot/findiv_pilot_results.csv", index=False)
print(out.drop(columns=["repo"]).to_markdown(index=False))
