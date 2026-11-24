"""Old Greek (OG) vs Theodotion (Th) Daniel, Rahlfs 1935 (CenterBLC Text-Fabric).
Th follows the Hebrew/Aramaic closely, so OG/Th divergence per chapter measures how far the Old Greek's
Vorlage (Hebrew/Aramaic text it translated, c. 100 BCE) differed from the text we have.
Metrics per chapter: word counts, OG/Th ratio, mean verse-level lemma Jaccard similarity.
The Greek Additions (3:24-90 Prayer of Azariah and Song of the Three) are excluded."""
import os, csv
from collections import defaultdict
from tf.fabric import Fabric
TF = Fabric(locations=os.path.expanduser("~/text-fabric-data/github/CenterBLC/LXX/tf/1935"), silent="deep")
api = TF.load("book chapter verse word lex_utf8 sp", silent="deep")
F, L, T = api.F, api.L, api.T
def verses(book):
    out = {}
    for v in F.otype.s("verse"):
        b, c, vv = T.sectionFromNode(v)
        if b != book:
            continue
        if c == 3 and 24 <= vv <= 90:
            continue
        out[(c, vv)] = [F.lex_utf8.v(w) for w in L.d(v, "word")]
    return out
og, th = verses("Dan"), verses("DanTh")
rows = []
for ch in range(1, 13):
    keys = sorted(set(k for k in list(og) + list(th) if k[0] == ch))
    wo = sum(len(og.get(k, [])) for k in keys); wt = sum(len(th.get(k, [])) for k in keys)
    jac = []
    for k in keys:
        a, b = set(og.get(k, [])), set(th.get(k, []))
        if a or b:
            jac.append(len(a & b) / len(a | b))
    only_og = sum(1 for k in keys if k in og and k not in th); only_th = sum(1 for k in keys if k in th and k not in og)
    rows.append(dict(chapter=ch, og_words=wo, th_words=wt, ratio=round(wo / wt, 2), mean_jaccard=round(sum(jac) / len(jac), 3),
                     verses_only_in_og=only_og, verses_only_in_th=only_th))
    print(rows[-1])
with open(os.path.join(os.path.dirname(__file__), "..", "results", "lxx_og_vs_th.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
