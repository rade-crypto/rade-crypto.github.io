"""Aramaic dialect-dating features: Daniel 2:4b-7:28 vs Ezra Aramaic vs Qumran Aramaic.

All features are computed from the CONSONANTAL text only (MT Kethiv for the Bible,
the scroll readings for Qumran), never from the medieval Masoretic vowels.
Each feature is a binary choice between an older and a younger variant; we report
the share of the "younger" variant with a Wilson 95% interval.

Output: results/aramaic_features.csv and results/aramaic_features.md
"""
import sys, re, csv, math, os
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from corpora import load_bhsa, load_dss

OUT = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(OUT, exist_ok=True)

FINAL = str.maketrans("ךםןףץ", "כמנפצ")
def norm(s):
    return (s or "").translate(FINAL)

def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0, c - h), min(1, c + h)

# feature -> {corpus -> Counter(variant)}, plus examples
counts = defaultdict(lambda: defaultdict(Counter))
examples = defaultdict(lambda: defaultdict(list))
wordtotals = Counter()

def hit(feature, corpus, variant, ref, form):
    counts[feature][corpus][variant] += 1
    if len(examples[feature][(corpus, variant)]) < 6:
        examples[feature][(corpus, variant)].append(f"{ref} {form}")

# Feature definitions: (feature, older-variant label, younger-variant label)
FEATURES = [
    ("3mp suffix", "-hm (הם)", "-hwn (הון)"),
    ("2mp suffix", "-km (כם)", "-kwn (כון)"),
    ("3fs suffix", "-h (ה)", "-hʾ (הא)"),
    ("2ms suffix", "-k (ך)", "-kh (כה)"),
    ("2ms pronoun", "ʾnt (אנת)", "ʾnth (אנתה)"),
    ("causative prefix", "h- (haphel)", "ʾ- (aphel)"),
    ("t-stem prefix", "ht- (hitpe./hitpa.)", "ʾt- (itpe./itpa.)"),
    ("3mp pronoun", "hmw/hmwn (המו/המון)", "ʾnwn/ʾnyn (אנון/אנין)"),
    ("plural demonstrative", "ʾlh/ʾlk (אלה/אלך)", "ʾlyn/ʾln (אלין/אלן)"),
    ("'earth'", "ʾrq (ארק)", "ʾrʿ (ארע)"),
    ("relative particle", "zy (זי)", "dy (די)"),
]

def classify_causative(form, vt):
    """form = consonants of a causative-stem verb (no clitics). Return 'old'/'new'/None."""
    f = norm(form)
    if vt in ("perf", "impv", "infc", "infa"):
        if f.startswith("ה"):
            return "old"
        if f.startswith("א"):
            return "new"
        return None
    if vt in ("impf",):
        if len(f) > 2 and f[0] in "יתאנ":
            return "old" if f[1] == "ה" else "new"
        return None
    if vt in ("ptca", "ptcp"):
        if f.startswith("מה"):
            return "old"
        if f.startswith("מ"):
            return "new"
    return None

def classify_tstem(form, vt):
    f = norm(form)
    if vt in ("perf", "impv", "infc", "infa"):
        if re.match(r"^ה[תשסצז]", f):
            return "old"
        if re.match(r"^א[תשסצז]", f):
            return "new"
    return None  # impf/ptc lose the prefix -> uninformative

def suffix_variant(feature, s):
    s = norm(s)
    if feature == "3mp suffix":
        if s.endswith("הונ") or s.endswith("ונ"):
            return "new"
        if s.endswith("המ") or s.endswith("הומ"):
            return "old"
    if feature == "2mp suffix":
        if s.endswith("כונ"):
            return "new"
        if s.endswith("כמ"):
            return "old"
    if feature == "3fs suffix":
        if s.endswith("הא"):
            return "new"
        if s.endswith("ה"):
            return "old"
    if feature == "2ms suffix":
        if s.endswith("כה"):
            return "new"
        if s.endswith("כ"):
            return "old"
    return None

def lexical(cons, kind):
    """Lexical features from a bare consonantal word.
    kind: 'pers' (personal pronoun), 'demo' (demonstrative), 'noun', 'rel' (relative particle)"""
    c = norm(cons)
    out = []
    if kind == "pers" and c in ("אנת",):
        out.append(("2ms pronoun", "old"))
    if kind == "pers" and c in ("אנתה",):
        out.append(("2ms pronoun", "new"))
    if kind == "pers" and c in ("המו", "המונ", "המ", "המה"):
        out.append(("3mp pronoun", "old"))
    if kind == "pers" and c in ("אנונ", "אנינ"):
        out.append(("3mp pronoun", "new"))
    if kind == "demo" and c in ("אלה", "אל", "אלכ"):
        out.append(("plural demonstrative", "old"))
    if kind == "demo" and c in ("אלינ", "אלנ"):
        out.append(("plural demonstrative", "new"))
    if kind == "noun" and c in ("ארק", "ארקא", "ארקה"):
        out.append(("'earth'", "old"))
    if kind == "noun" and c in ("ארע", "ארעא", "ארעה"):
        out.append(("'earth'", "new"))
    if kind == "rel" and c == "זי":
        out.append(("relative particle", "old"))
    if kind == "rel" and c == "די":
        out.append(("relative particle", "new"))
    return out

# ----------------------------------------------------------------- BHSA
A = load_bhsa()
F, L, T = A.F, A.L, A.T
SUFFIX_LABEL = {"HM": "3mp suffix", "HWN": "3mp suffix", "KM": "2mp suffix", "KWN": "2mp suffix",
                "H": "3fs suffix", "K": "2ms suffix"}
STEM_CAUS = {"haf", "afel", "hof"}
STEM_T = {"htpe", "htpa", "etpe", "etpa", "hsht"}

def bhsa_corpus(w):
    b, c, v = T.sectionFromNode(w)
    if b == "Daniel":
        return "Daniel (MT)", c
    if b == "Ezra":
        return "Ezra (MT)", c
    return None, c

for w in F.otype.s("word"):
    if F.language.v(w) != "Aramaic":
        continue
    corp, ch = bhsa_corpus(w)
    if not corp:
        continue
    wordtotals[corp] += 1
    if corp.startswith("Daniel"):
        wordtotals[f"Daniel ch.{ch}"] += 1
    ref = "{} {}:{}".format(*T.sectionFromNode(w))
    cons = F.g_cons_utf8.v(w) or ""
    corps = [corp] + ([f"Daniel ch.{ch}"] if corp.startswith("Daniel") else [])
    prs = F.prs.v(w)
    if prs in SUFFIX_LABEL:
        feat = SUFFIX_LABEL[prs]
        var = suffix_variant(feat, cons)
        if var:
            for cp in corps:
                hit(feat, cp, var, ref, cons)
    if F.sp.v(w) == "verb":
        vs, vt = F.vs.v(w), F.vt.v(w)
        if vs in STEM_CAUS:
            var = classify_causative(cons, vt)
            if var:
                for cp in corps:
                    hit("causative prefix", cp, var, ref, cons)
        if vs in STEM_T:
            var = classify_tstem(cons, vt)
            if var:
                for cp in corps:
                    hit("t-stem prefix", cp, var, ref, cons)
    lx = F.lex.v(w)
    kind = {"prps": "pers", "prde": "demo", "subs": "noun"}.get(F.sp.v(w))
    if lx == "DJ":
        kind = "rel"
    if lx == ">LH/":   # God -- never a demonstrative
        kind = None
    for feat, var in lexical(cons, kind):
        for cp in corps:
            hit(feat, cp, var, ref, cons)

# ----------------------------------------------------------------- DSS
D = load_dss()
F2, L2 = D.F, D.L
HEB = re.compile(r"[^א-ת׳]")
def dcons(w):
    return HEB.sub("", F2.full.v(w) or F2.glyph.v(w) or "")

QUMRAN_GROUPS = {
    "Genesis Apocryphon (1Q20)": {"1Q20"},
    "Targum of Job (11Q10, 4Q157)": {"11Q10", "4Q157"},
    "Aramaic Enoch (4Q201-212)": {f"4Q{n}" for n in range(201, 213)},
    "New Jerusalem (1Q32,2Q24,4Q554-555,5Q15,11Q18)": {"1Q32", "2Q24", "4Q554", "4Q554a", "4Q555", "5Q15", "11Q18"},
    "Aramaic Levi / Qahat / Amram (1Q21,4Q213-214b,4Q540-548)": {"1Q21", "4Q213", "4Q213a", "4Q213b", "4Q214", "4Q214a", "4Q214b",
                                                                "4Q540", "4Q541", "4Q542", "4Q543", "4Q544", "4Q545", "4Q546", "4Q547", "4Q548"},
    "Daniel-related (4Q242 PrNab, 4Q243-245 psDan, 4Q246, 4Q552-553 Four Kingdoms)": {"4Q242", "4Q243", "4Q244", "4Q245", "4Q246", "4Q552", "4Q553"},
    "Tobit (4Q196-199)": {"4Q196", "4Q197", "4Q198", "4Q199"},
    "Giants (1Q23-24,2Q26,4Q203,4Q530-533,6Q8)": {"1Q23", "1Q24", "2Q26", "4Q203", "4Q530", "4Q531", "4Q532", "4Q533", "6Q8"},
}
DSS_DANIEL = {"4Q112", "4Q113", "4Q114", "4Q115", "4Q116", "1Q71", "1Q72", "6Q7"}

scroll_of = {}
for s in F2.otype.s("scroll"):
    name = F2.scroll.v(s)
    for w in L2.d(s, "word"):
        scroll_of[w] = name

DSS_STEM_CAUS = {"haphel", "aphel", "hophal"}
DSS_STEM_T = {"ithpeel", "ithpaal", "hithpeel", "hithpaal", "hithpolel", "hithaphel", "hishtaphel", "ishtaphel", "hitpael"}

for w in F2.otype.s("word"):
    if F2.lang.v(w) != "a":
        continue
    sc = scroll_of.get(w, "?")
    if F2.biblical.v(w):
        if sc in DSS_DANIEL:
            corps = ["Daniel (Qumran MSS)"]
        else:
            continue
    else:
        corps = ["Qumran Aramaic (all non-biblical)"]
        for g, members in QUMRAN_GROUPS.items():
            if sc in members:
                corps.append("  Qumran: " + g)
    for cp in corps:
        wordtotals[cp] += 1
    t = dcons(w)
    host, _, suf = t.partition("׳")
    ref = f"{sc} {F2.fragment.v(L2.u(w,'fragment')[0]) if L2.u(w,'fragment') else ''}"
    m = re.search(r"X([123][mfc][sp])", F2.morpho.v(w) or "")
    if m and suf:
        lab = {"3mp": "3mp suffix", "2mp": "2mp suffix", "3fs": "3fs suffix", "2ms": "2ms suffix"}.get(m.group(1))
        if lab:
            var = suffix_variant(lab, suf)
            if var:
                for cp in corps:
                    hit(lab, cp, var, ref, t)
    if F2.sp.v(w) == "verb":
        vs, vt = F2.vs.v(w), F2.vt.v(w)
        if vs in DSS_STEM_CAUS:
            var = classify_causative(host, vt)
            if var:
                for cp in corps:
                    hit("causative prefix", cp, var, ref, t)
        if vs in DSS_STEM_T:
            var = classify_tstem(host, vt)
            if var:
                for cp in corps:
                    hit("t-stem prefix", cp, var, ref, t)
    sp2, lx2 = F2.sp.v(w), F2.lex.v(w) or ""
    kind = {"pron": "pers", "subs": "noun", "ptcl": "rel"}.get(sp2)
    if sp2 == "adjv" and HEB.sub("", lx2) in ("אלה", "אלין", "אלך", "אל", "אלן"):
        kind = "demo"
    if "׳" not in t:
        for feat, var in lexical(t, kind):
            for cp in corps:
                hit(feat, cp, var, ref, t)

# ----------------------------------------------------------------- report
ORDER = ["Ezra (MT)", "Daniel (MT)", "Daniel (Qumran MSS)", "Qumran Aramaic (all non-biblical)"] + \
        sorted(k for k in wordtotals if k.startswith("  Qumran")) + \
        [f"Daniel ch.{c}" for c in range(2, 8)]
rows = []
for feat, old, new in FEATURES:
    for cp in ORDER:
        c = counts[feat][cp]
        k, n = c["new"], c["old"] + c["new"]
        p, lo, hi = wilson(k, n)
        rows.append(dict(feature=feat, corpus=cp.strip(), older=old, younger=new, n_old=c["old"], n_new=k, n=n,
                         share_younger=p, ci_lo=lo, ci_hi=hi, words=wordtotals[cp]))
with open(os.path.join(OUT, "aramaic_features.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    wr.writeheader(); wr.writerows(rows)

with open(os.path.join(OUT, "aramaic_features.md"), "w") as fh:
    fh.write("# Aramaic diagnostic features (consonantal text)\n\n")
    fh.write("Word totals: " + ", ".join(f"{k.strip()}={v}" for k, v in wordtotals.items() if not k.startswith("Daniel ch")) + "\n\n")
    for feat, old, new in FEATURES:
        fh.write(f"## {feat}: older {old} vs younger {new}\n\n| corpus | older | younger | share younger (95% CI) |\n|---|---|---|---|\n")
        for cp in ORDER:
            c = counts[feat][cp]
            n = c["old"] + c["new"]
            if n == 0:
                continue
            p, lo, hi = wilson(c["new"], n)
            fh.write(f"| {cp.strip()} | {c['old']} | {c['new']} | {p:.0%} ({lo:.0%}-{hi:.0%}) |\n")
        fh.write("\nExamples:\n")
        for (cp, var), ex in examples[feat].items():
            if cp.startswith("  ") or cp.startswith("Daniel ch"):
                continue
            fh.write(f"- {cp} [{var}]: {'; '.join(ex)}\n")
        fh.write("\n")
print(open(os.path.join(OUT, "aramaic_features.md")).read())
