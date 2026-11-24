"""Search the I.PHI dataset (cleaned Packard Humanities Institute Greek inscriptions, with
editors' date ranges) for the Daniel 3 instrument words. Writes results/greek/inscriptions_hits.csv"""
import sys, re, unicodedata, glob, os
import pandas as pd
D = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "results", "greek", "inscriptions_hits.csv")
df = pd.concat([pd.read_parquet(f) for f in glob.glob(os.path.join(D, "*.parquet"))], ignore_index=True)
def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower().replace("ς", "σ")
    return s
df["t"] = df.text.map(norm)
print("inscriptions:", len(df), "words ~", int(df.t.str.split().map(len).sum()))
print("dated (has date_min):", df.date_min.notna().sum())
pats = {"symphon-": r"[σξ][υu]μφων", "psalter-": r"ψαλτηρ", "kithar-": r"κιθαρ", "psalt-": r"ψαλτ"}
rows = []
for key, pat in pats.items():
    for _, r in df[df.t.str.contains(pat, regex=True)].iterrows():
        for m in re.finditer(pat, r.t):
            a, b = max(0, m.start() - 70), min(len(r.t), m.end() + 70)
            word = re.search(r"\S*" + pat + r"\S*", r.t[max(0, m.start()-20):m.end()+20])
            rows.append(dict(stem=key, phi_id=r.id, region=r.region_main, sub=r["region_sub"], date_str=r.date_str,
                             date_min=r.date_min, date_max=r.date_max, word=word.group(0) if word else "", context=r.t[a:b]))
h = pd.DataFrame(rows)
h.to_csv(OUT, index=False)
for key in pats:
    x = h[h.stem == key]
    print(f"\n== {key}: {len(x)} hits; dated before 100 CE: {(x.date_max <= 100).sum()} ; before 0: {(x.date_max <= 0).sum()}")
    for _, r in x.sort_values("date_min").head(40 if key != 'kithar-' else 12).iterrows():
        print(f"  PHI {r.phi_id} | {r.region[:22]}/{str(r["sub"])[:22]} | {r.date_str} [{r.date_min}..{r.date_max}] | {r.word} | ...{r.context}...")
