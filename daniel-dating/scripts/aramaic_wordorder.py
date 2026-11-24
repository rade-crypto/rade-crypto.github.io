"""Constituent order in Biblical Aramaic clauses (BHSA phrase functions): Ezra vs Daniel.
Imperial (Achaemenid chancery) Aramaic is known for frequent object-before-verb order
under Akkadian/Old Persian influence; later Aramaic is predominantly verb-object.
We measure the share of O-V among clauses that contain both a predicate and an object phrase
(excluding objects that are only pronominal suffixes, which are always post-verbal)."""
import sys, os, csv
sys.path.insert(0, os.path.dirname(__file__))
from collections import Counter
from corpora import load_bhsa
A = load_bhsa(); F, L, T = A.F, A.L, A.T
res = Counter()
for cl in F.otype.s("clause_atom"):
    ws = L.d(cl, "word")
    if F.language.v(ws[0]) != "Aramaic":
        continue
    book = T.sectionFromNode(ws[0])[0]
    if book not in ("Daniel", "Ezra"):
        continue
    ch = T.sectionFromNode(ws[0])[1]
    ph = L.d(cl, "phrase_atom")
    funcs = []
    for p in ph:
        par = L.u(p, "phrase")[0]
        funcs.append((F.function.v(par), min(L.d(p, "word"))))
    pred = [s for f, s in funcs if f in ("Pred", "PreO", "PreS", "PtcO")]
    obj = [s for f, s in funcs if f == "Objc"]
    subj = [s for f, s in funcs if f == "Subj"]
    tag = book if book == "Ezra" else ("Daniel 2-3" if ch <= 3 else "Daniel 4-7")
    for t in (tag, book):
        if pred and obj:
            res[(t, "OV" if obj[0] < pred[0] else "VO")] += 1
        if pred and subj:
            res[(t, "SV" if subj[0] < pred[0] else "VS")] += 1
rows = []
for t in ("Ezra", "Daniel", "Daniel 2-3", "Daniel 4-7"):
    ov, vo, sv, vs = res[(t, "OV")], res[(t, "VO")], res[(t, "SV")], res[(t, "VS")]
    rows.append(dict(corpus=t, OV=ov, VO=vo, share_OV=round(ov / (ov + vo), 3), SV=sv, VS=vs, share_SV=round(sv / (sv + vs), 3)))
    print(rows[-1])
with open(os.path.join(os.path.dirname(__file__), "..", "results", "aramaic_wordorder.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
