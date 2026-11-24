"""Systematic inventory of predictive statements about named places, peoples and persons
in the Latter Prophets (Isaiah, Jeremiah, Ezekiel, the Twelve) and Daniel (Hebrew parts).

A verse is flagged as 'predictive about X' when it contains a proper name X (BHSA nametype
topo / gens / pers) AND at least one verb in a future-referring form:
  yiqtol (impf), weqatal (perf directly preceded by the conjunction w-), or a participle
  after hinneh (the 'futurum instans' 'behold I am bringing ...').
This is deliberately over-inclusive; it guarantees that no oracle about a named place or
people is missed when the claim database is curated. Israel/Judah/Jerusalem/Zion and divine
names are kept (Jerusalem's fate is itself a testable claim).

Output: results/inventory_verses.csv (one row per verse x name) and
        results/inventory_oracles.csv (chapter x name, number of predictive verses).
"""
import os, sys
import pandas as pd
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
from corpora import load_bhsa

OUT = os.path.join(os.path.dirname(__file__), "..", "results")
BOOKS = ["Isaiah", "Jeremiah", "Ezekiel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
         "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Daniel"]
SKIP = {"JHWH/", ">LHJM/", "JH/", ">DNJ/", "YB>WT/"}

A = load_bhsa("book chapter verse lex sp nametype vt language g_cons_utf8 gloss lex_utf8")
F, L, T = A.F, A.L, A.T

rows = []
for b in BOOKS:
    bn = T.nodeFromSection((b,))
    for v in L.d(bn, "verse"):
        ws = L.d(v, "word")
        if any(F.language.v(w) != "Hebrew" for w in ws):
            continue                                        # Aramaic portions handled separately
        fut, hinne = False, False
        prev = None
        for w in ws:
            lx = F.lex.v(w)
            if lx == "HNH/" or lx == "HNH":
                hinne = True
            vt = F.vt.v(w) if F.sp.v(w) == "verb" else None
            if vt == "impf" or (vt == "perf" and prev == "W") or (vt == "ptca" and hinne):
                fut = True
            prev = lx
        if not fut:
            continue
        _, c, vs = T.sectionFromNode(v)
        seen = set()
        for w in ws:
            if F.sp.v(w) != "nmpr":
                continue
            lx = F.lex.v(w)
            if lx in SKIP or lx in seen:
                continue
            seen.add(lx)
            rows.append(dict(book=b, chapter=c, verse=vs, lex=lx, name=F.lex_utf8.v(w), gloss=F.gloss.v(w),
                             nametype=F.nametype.v(w) or ""))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(OUT, "inventory_verses.csv"), index=False)
orc = (df.groupby(["book", "chapter", "gloss", "nametype"]).verse.agg(["count", lambda s: ",".join(map(str, s))])
         .reset_index().rename(columns={"count": "n_verses", "<lambda_0>": "verses"}))
orc.to_csv(os.path.join(OUT, "inventory_oracles.csv"), index=False)

# summary: which foreign names are targets of predictive statements, and where
dom = {"Israel", "Judah", "Jerusalem", "Zion", "Jacob", "Ephraim", "David", "Joseph", "Benjamin"}
f = orc[~orc.gloss.isin(dom)]
tot = f.groupby("gloss").n_verses.sum().sort_values(ascending=False)
print("verses flagged:", df[["book", "chapter", "verse"]].drop_duplicates().shape[0], "| verse-name rows:", len(df))
print("distinct names:", df.gloss.nunique())
print(tot.head(60).to_string())
