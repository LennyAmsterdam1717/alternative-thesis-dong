"""Proposal 5 pilot: how do financial-NLP tokenizers handle retail-investor variation?

Run: python -I pilot/tokenizer_pilot.py
Downloads tokenizers only (no model weights). Reports, per tokenizer, the share of common
retail-investor emoji mapped to the unknown token, and the number of subword tokens for cashtags,
slang and spelling variants versus their standard forms.
"""
import json

from transformers import AutoTokenizer

TOKENIZERS = {
    "FinBERT (ProsusAI/finbert)": "ProsusAI/finbert",
    "FinBERT-tone (yiyanghkust/finbert-tone)": "yiyanghkust/finbert-tone",
    "BERT-base-uncased": "bert-base-uncased",
    "RoBERTa-base": "roberta-base",
    "DeBERTa-v3-base": "microsoft/deberta-v3-base",
    "OLMo-2 (allenai/OLMo-2-1124-7B)": "allenai/OLMo-2-1124-7B",
}
EMOJI = ["🚀", "💎", "🙌", "🐻", "🐂", "📈", "📉", "🌕", "🦍", "🔥", "💰", "🤡", "😂", "🩳", "🧻"]
PAIRS = [  # (standard, variant)
    ("GameStop", "$GME"), ("Tesla", "$TSLA"), ("going to", "gonna"), ("tomorrow", "tmrw"),
    ("profits", "tendies"), ("holding", "HODL"), ("stocks", "stonks"), ("to the moon", "2 the moooon"),
    ("diamond hands", "💎🙌"), ("I am buying", "im buyin"), ("bearish", "🐻"),
]

rows = []
for name, repo in TOKENIZERS.items():
    try:
        tok = AutoTokenizer.from_pretrained(repo)
    except Exception as e:  # noqa: BLE001
        rows.append({"tokenizer": name, "error": str(e)[:120]})
        continue
    unk = tok.unk_token
    unk_rate = sum(1 for e in EMOJI if unk is not None and tok.tokenize(e) == [unk]) / len(EMOJI)
    lens = {f"{a} | {b}": (len(tok.tokenize(a)), len(tok.tokenize(b))) for a, b in PAIRS}
    rows.append({"tokenizer": name, "vocab": tok.vocab_size, "emoji_unk_rate": round(unk_rate, 2),
                 "pairs_std_vs_variant_tokens": lens})
    print(json.dumps(rows[-1], ensure_ascii=False), flush=True)

with open("pilot/tokenizer_pilot_results.json", "w") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
