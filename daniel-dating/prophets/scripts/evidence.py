"""Attach text-based evidence to every claim in claims.py:
  * consonantal Hebrew of the claim's verses (BHSA, ketiv)
  * which Dead Sea Scrolls preserve at least one word of those verses (ETCBC DSS 2.0.5, biblical scrolls)
  * whether the verses exist in the Old Greek (CenterBLC LXX, Rahlfs); Jeremiah is mapped to the Greek chapter order
Output: results/claims_evidence.csv and results/claims_hebrew.md
"""
import os, sys, re, glob
import pandas as pd
from collections import defaultdict
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from claims import CLAIMS
from corpora import load_bhsa, load_dss
from tf.fabric import Fabric

OUT = os.path.join(HERE, "..", "results")
BK = {  # abbreviation -> (BHSA, DSS, LXX)
    "Isa": ("Isaiah", "Is", "Isa"), "Jer": ("Jeremiah", "Jer", "Jer"), "Ezek": ("Ezekiel", "Ezek", "Ezek"),
    "Hos": ("Hosea", "Hos", "Hos"), "Joel": ("Joel", "Joel", "Joel"), "Amos": ("Amos", "Amos", "Amos"),
    "Obad": ("Obadiah", "Obad", "Obad"), "Mic": ("Micah", "Mic", "Mic"), "Nah": ("Nahum", "Nah", "Nah"),
    "Hab": ("Habakkuk", "Hab", "Hab"), "Zeph": ("Zephaniah", "Zeph", "Zeph"), "Hag": ("Haggai", "Hag", "Hag"),
    "Zech": ("Zechariah", "Zech", "Zech"), "Mal": ("Malachi", "Mal", "Mal"), "Dan": ("Daniel", "Dan", "DanTh"),
}
# Hebrew (MT) -> Greek chapter order in Jeremiah (Rahlfs); value: (lxx_chapter, verse_offset) or a function
def jer_mt2lxx(c, v):
    if c == 25 and v <= 13: return (25, v)
    if c == 25 and v >= 15: return (32, v - 14)
    if c == 49 and v >= 34: return (25, v - 20)       # Elam
    if c == 46: return (26, v)
    if c == 47: return (29, v)
    if c == 48: return (31, v)
    if c == 49 and v <= 6: return (30, v)             # Ammon 49:1-5 = 30:1-5
    if c == 49 and 7 <= v <= 22: return (29, v)       # Edom
    if c == 49 and 23 <= v <= 27: return (30, v - 11)  # Damascus = 30:12-16
    if c == 49 and 28 <= v <= 33: return (30, v - 22)  # Kedar = 30:6-11
    if c == 50: return (27, v)
    if c == 51: return (28, v)
    m = {26: 33, 27: 34, 28: 35, 29: 36, 30: 37, 31: 38, 32: 39, 33: 40, 34: 41, 35: 42, 36: 43, 37: 44, 38: 45,
         39: 46, 40: 47, 41: 48, 42: 49, 43: 50, 44: 51, 45: 51}
    if c in m:
        return (m[c], v if c != 45 else v + 30)
    return (c, v)

def parse_refs(refs):
    out = []
    for part in refs.split(";"):
        part = part.strip()
        m = re.match(r"(\w+)\s+(.*)", part)
        if m and m.group(1) in BK:
            book, rest = m.group(1), m.group(2)
        else:
            rest = part
        if ":" not in rest:                      # single-chapter book: 'Obad 1-21'
            rest = "1:" + rest
        c, vv = rest.split(":")
        a, b = (vv.split("-") + [None])[:2]
        for v in range(int(a), int(b or a) + 1):
            out.append((book, int(c), v))
    return out

A = load_bhsa("book chapter verse g_cons_utf8 trailer_utf8")
F, L, T = A.F, A.L, A.T
D = load_dss("scroll biblical book chapter verse")
F2, L2 = D.F, D.L
dss = defaultdict(set)   # (dssbook, ch, v) -> scrolls
for w in F2.otype.s("word"):
    if F2.biblical.v(w):
        try:
            key = (F2.book.v(w), int(F2.chapter.v(w)), int(F2.verse.v(w)))
        except (TypeError, ValueError):
            continue
        dss[key].add(F2.scroll.v(L2.u(w, "scroll")[0]))
LP = glob.glob(os.path.expanduser("~/text-fabric-data/github/CenterBLC/LXX/tf/*"))[0]
X = Fabric(locations=LP, silent="deep").load("book chapter verse word", silent="deep")
lxx = set()
for v in X.F.otype.s("verse"):
    b, c, vv = X.T.sectionFromNode(v)
    lxx.add((b, int(c), int(vv)))

def heb(book, c, v):
    vn = T.nodeFromSection((BK[book][0], c, v))
    if not vn:
        return None
    return "".join(F.g_cons_utf8.v(w) + (" " if F.trailer_utf8.v(w) else "") for w in L.d(vn, "word")).strip()

rows, md = [], ["# Hebrew text of the claims (consonantal, ketiv, BHSA)\n"]
for cl in CLAIMS:
    vs = parse_refs(cl["refs"])
    scrolls = defaultdict(int)
    n_lxx = 0
    for (b, c, v) in vs:
        for s in dss.get((BK[b][1], c, v), ()):
            scrolls[s] += 1
        lb = BK[b][2]
        if b == "Jer":
            lc, lv = jer_mt2lxx(c, v)
            n_lxx += (lb, lc, lv) in lxx
        else:
            n_lxx += (lb, c, v) in lxx or (b == "Dan" and ("Dan", c, v) in lxx)
    rows.append(dict(id=cl["id"], refs=cl["refs"], target=cl["target"], n_verses=len(vs),
                     dss_scrolls="; ".join(f"{s}({n})" for s, n in sorted(scrolls.items())),
                     dss_verses_covered=sum(1 for (b, c, v) in vs if dss.get((BK[b][1], c, v))),
                     lxx_verses_present=n_lxx, event_date=cl["event_date"],
                     narrative_includes_fulfilment=cl.get("narrative_includes_fulfilment", False)))
    md.append(f"## {cl['id']} {cl['refs']} - {cl['target']}\n")
    for (b, c, v) in vs[:12]:
        t = heb(b, c, v)
        if t:
            md.append(f"- {b} {c}:{v} {t}")
    if len(vs) > 12:
        md.append(f"- ... ({len(vs) - 12} more verses)")
    md.append("")
df = pd.DataFrame(rows)
df.to_csv(os.path.join(OUT, "claims_evidence.csv"), index=False)
open(os.path.join(OUT, "claims_hebrew.md"), "w").write("\n".join(md))
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 90)
print(df[["id", "n_verses", "dss_verses_covered", "lxx_verses_present", "dss_scrolls"]].to_string(index=False))
