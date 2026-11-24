"""Hebrew chronolect analysis: where does the Hebrew of Daniel (1:1-2:4a, 8-12) sit
on the time-line of ancient Hebrew?

Corpora
  * BHSA 2021 (Masoretic text, ETCBC annotation)
  * DSS 2.0.5 non-biblical Hebrew compositions (Abegg morphology, ETCBC-harmonised lexemes)
  * DSS biblical scrolls of classical books -> CONTROL: they must be placed near their MT
    counterparts, otherwise the model is learning annotation / orthography artefacts.

Features (orthography-free: lexemes and morphological categories, never spellings)
  * relative frequencies of the most frequent lexemes (no proper names, no divine names, no article)
  * share of each verb form (wayyiqtol, weqatal, qatal, yiqtol, imperative, ptc, inf.c, inf.a)
  * share of each verb stem
  * rate of pronominal suffixes overall / on verbs / on the object marker 'et

Models
  * anchor texts with broadly agreed dates -> ridge regression on composition date
    (leave-one-TEXT-out cross-validation gives an honest error estimate)
  * 4-period classifier (Classical / 6th c. / Persian LBH / Hellenistic-Qumran), leave-one-text-out
  * nearest anchor texts by cosine distance
"""
import sys, os, json, random, math
import numpy as np, pandas as pd
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from corpora import load_bhsa, load_dss

RES = os.path.join(os.path.dirname(__file__), "..", "results")
CHUNK = 300
FEATSET = sys.argv[1] if len(sys.argv) > 1 else "full"   # full | function
TAG = "" if FEATSET == "full" else "_" + FEATSET
random.seed(1); np.random.seed(1)

# ------------------------------------------------------------------ token streams
# token = (lex, vt, vs, has_suffix, suffix_on_verb, prev_is_W)
units = defaultdict(list)      # unit name -> token list
meta = {}                      # unit -> dict(date, period, role)

def add_meta(name, date, period, role):
    meta[name] = dict(date=date, period=period, role=role)

# --- BHSA
A = load_bhsa("book chapter verse lex sp vt vs prs language")
F, L, T = A.F, A.L, A.T

def bhsa_unit(book, ch, vs):
    if book == "Isaiah":
        return "Isaiah 1-39" if ch <= 39 else ("Isaiah 40-55" if ch <= 55 else "Isaiah 56-66")
    if book == "Zechariah":
        return "Zechariah 1-8" if ch <= 8 else "Zechariah 9-14"
    if book == "Daniel":
        return f"Daniel {ch}" if ch != 2 else "Daniel 1"   # 2:1-4a Hebrew goes with ch.1 narrative
    if book in ("1_Samuel", "2_Samuel"):
        return "Samuel"
    if book in ("1_Kings", "2_Kings"):
        return "Kings"
    if book in ("1_Chronicles", "2_Chronicles"):
        return "Chronicles"
    return book

prev_lex = None
for w in F.otype.s("word"):
    if F.language.v(w) != "Hebrew":
        prev_lex = None
        continue
    b, c, v = T.sectionFromNode(w)
    u = "MT " + bhsa_unit(b, c, v)
    lex = F.lex.v(w)
    prs = F.prs.v(w)
    has_s = prs not in ("absent", "n/a", None)
    vt = F.vt.v(w) if F.sp.v(w) == "verb" else None
    units[u].append((lex, vt, F.vs.v(w) if vt else None, has_s, has_s and vt is not None, prev_lex == "W"))
    prev_lex = lex

# --- DSS
D = load_dss("scroll biblical lang lex_etcbc vt_etcbc vs_etcbc g_prs_etcbc book type sp_etcbc")
F2, L2 = D.F, D.L
QUMRAN = {
    "Q Community Rule (1QS, 4QS)": ["1QS"] + [f"4Q{n}" for n in range(255, 265)],
    "Q Rule of Congregation/Blessings (1QSa, 1QSb)": ["1QSa", "1QSb"],
    "Q War Scroll (1QM, 4Q491-496)": ["1QM"] + [f"4Q{n}" for n in range(491, 497)],
    "Q Hodayot (1QHa, 4Q427-432)": ["1QHa"] + [f"4Q{n}" for n in range(427, 433)],
    "Q Damascus Document (CD, 4Q266-273)": ["CD"] + [f"4Q{n}" for n in range(266, 274)],
    "Q MMT (4Q394-399)": [f"4Q{n}" for n in range(394, 400)],
    "Q Temple Scroll (11Q19-20, 4Q524)": ["11Q19", "11Q20", "4Q524"],
    "Q Pesharim & Florilegium (1QpHab, 4Q161-177)": ["1QpHab"] + [f"4Q{n}" for n in range(161, 178)],
    "Q Instruction (4Q415-418, 4Q423, 1Q26)": ["4Q415", "4Q416", "4Q417", "4Q418", "4Q418a", "4Q423", "1Q26"],
    "Q Songs of Sabbath Sacrifice (4Q400-407, 11Q17)": [f"4Q{n}" for n in range(400, 408)] + ["11Q17"],
    "Q Jubilees Hebrew (4Q216-224)": [f"4Q{n}" for n in range(216, 225)] + ["4Q223_224"],
    "Q Words of Luminaries (4Q504-506)": ["4Q504", "4Q505", "4Q506"],
    "Q Apocryphon Jer./Ps-Ezekiel (4Q383-391)": [f"4Q{n}" for n in range(383, 392)] + ["4Q385a", "4Q385b", "4Q387a"],
    "Q Barkhi Nafshi & Songs of Sage (4Q434-438, 4Q510-511)": ["4Q434", "4Q435", "4Q436", "4Q437", "4Q438", "4Q510", "4Q511"],
    "Q Mysteries (1Q27, 4Q299-301)": ["1Q27", "4Q299", "4Q300", "4Q301"],
    "Q Berakhot (4Q286-290)": ["4Q286", "4Q287", "4Q288", "4Q289", "4Q290"],
    "Q Copper Scroll (3Q15)": ["3Q15"],
}
scroll2unit = {s: u for u, ss in QUMRAN.items() for s in ss}
BIB_CONTROL = {  # DSS biblical copies: (book) -> unit
    "Is": "DSS-copy Isaiah", "1Sam": "DSS-copy Samuel", "2Sam": "DSS-copy Samuel", "Ex": "DSS-copy Exodus",
    "Num": "DSS-copy Numbers", "Lev": "DSS-copy Leviticus", "Deut": "DSS-copy Deuteronomy", "Jer": "DSS-copy Jeremiah",
    "Ezek": "DSS-copy Ezekiel", "Hos": "DSS-copy Minor Prophets", "Amos": "DSS-copy Minor Prophets",
    "Mic": "DSS-copy Minor Prophets", "Jonah": "DSS-copy Minor Prophets", "Joel": "DSS-copy Minor Prophets",
    "Zeph": "DSS-copy Minor Prophets", "Hag": "DSS-copy Minor Prophets", "Nah": "DSS-copy Minor Prophets",
    "Hab": "DSS-copy Minor Prophets", "Obad": "DSS-copy Minor Prophets", "Zech": "DSS-copy Minor Prophets",
    "Mal": "DSS-copy Minor Prophets", "Dan": "DSS-copy Daniel (Hebrew parts)", "Gen": "DSS-copy Genesis",
}
for s in F2.otype.s("scroll"):
    name = F2.scroll.v(s)
    prev = None
    for w in L2.d(s, "word"):
        if F2.lang.v(w) is not None or F2.type.v(w) != "glyph":
            prev = None
            continue
        lex = F2.lex_etcbc.v(w)
        if not lex:
            prev = None
            continue
        if F2.biblical.v(w):
            u = BIB_CONTROL.get(F2.book.v(w))
        else:
            u = scroll2unit.get(name)
        if u:
            vt = F2.vt_etcbc.v(w)
            vt = vt if vt not in ("NA", "unknown", None, "") else None
            vs = F2.vs_etcbc.v(w) if vt else None
            prs = F2.g_prs_etcbc.v(w)
            has_s = prs not in ("NA", None, "")
            units[u].append((lex, vt, vs, has_s, has_s and vt is not None, prev == "W"))
        prev = lex

units["MT Daniel (all Hebrew)"] = sum((units[f"MT Daniel {c}"] for c in (1, 8, 9, 10, 11, 12)), [])
units["MT Daniel 8-12"] = sum((units[f"MT Daniel {c}"] for c in (8, 9, 10, 11, 12)), [])

# ------------------------------------------------------------------ metadata (anchor dates = approx. composition midpoints, BCE negative)
ANCHORS = {
    "MT Judges": (-600, "Classical"), "MT Samuel": (-600, "Classical"), "MT Kings": (-570, "Classical"),
    "MT Amos": (-760, "Classical"), "MT Hosea": (-740, "Classical"), "MT Micah": (-720, "Classical"),
    "MT Isaiah 1-39": (-700, "Classical"),
    "MT Jeremiah": (-590, "6th c."), "MT Ezekiel": (-580, "6th c."), "MT Lamentations": (-580, "6th c."),
    "MT Isaiah 40-55": (-540, "6th c."), "MT Haggai": (-520, "6th c."), "MT Zechariah 1-8": (-518, "6th c."),
    "MT Malachi": (-460, "Persian LBH"), "MT Ezra": (-400, "Persian LBH"), "MT Nehemiah": (-400, "Persian LBH"),
    "MT Chronicles": (-350, "Persian LBH"), "MT Esther": (-300, "Persian LBH"),
    "Q Jubilees Hebrew (4Q216-224)": (-160, "Hellenistic"), "Q MMT (4Q394-399)": (-150, "Hellenistic"),
    "Q Temple Scroll (11Q19-20, 4Q524)": (-150, "Hellenistic"), "Q Instruction (4Q415-418, 4Q423, 1Q26)": (-175, "Hellenistic"),
    "Q Words of Luminaries (4Q504-506)": (-150, "Hellenistic"), "Q Apocryphon Jer./Ps-Ezekiel (4Q383-391)": (-150, "Hellenistic"),
    "Q Community Rule (1QS, 4QS)": (-100, "Hellenistic"), "Q Rule of Congregation/Blessings (1QSa, 1QSb)": (-100, "Hellenistic"),
    "Q Damascus Document (CD, 4Q266-273)": (-100, "Hellenistic"), "Q Hodayot (1QHa, 4Q427-432)": (-100, "Hellenistic"),
    "Q Songs of Sabbath Sacrifice (4Q400-407, 11Q17)": (-100, "Hellenistic"), "Q War Scroll (1QM, 4Q491-496)": (-75, "Hellenistic"),
    "Q Pesharim & Florilegium (1QpHab, 4Q161-177)": (-60, "Hellenistic"), "Q Mysteries (1Q27, 4Q299-301)": (-150, "Hellenistic"),
    "Q Barkhi Nafshi & Songs of Sage (4Q434-438, 4Q510-511)": (-75, "Hellenistic"), "Q Berakhot (4Q286-290)": (-100, "Hellenistic"),
}
for u in units:
    if u in ANCHORS:
        add_meta(u, ANCHORS[u][0], ANCHORS[u][1], "anchor")
    elif u.startswith("MT Daniel"):
        add_meta(u, None, None, "DANIEL")
    elif u.startswith("DSS-copy"):
        add_meta(u, None, None, "control")
    else:
        add_meta(u, None, None, "test")

# ------------------------------------------------------------------ chunking & features
def chunks(tokens, size=CHUNK):
    n = len(tokens) // size
    if n == 0:
        return [tokens] if len(tokens) >= size * 0.6 else []
    return [tokens[i * size:(i + 1) * size] for i in range(n)]

EXCLUDE_LEX = {"H", "JHWH/", ">LHJM/", ">L/", ">DNJ/", "JH/"}
# lexeme part-of-speech from BHSA to drop proper nouns
lex_sp = {}
for w in F.otype.s("word"):
    lex_sp.setdefault(F.lex.v(w), F.sp.v(w))
anchor_tokens = Counter()
for u, toks in units.items():
    if meta[u]["role"] == "anchor":
        # weight each anchor text equally when picking the vocabulary
        c = Counter(t[0] for t in toks)
        tot = sum(c.values())
        for k, v in c.items():
            anchor_tokens[k] += v / tot
if FEATSET == "full":
    vocab = [l for l, _ in anchor_tokens.most_common(400) if l not in EXCLUDE_LEX and lex_sp.get(l) != "nmpr"][:150]
else:   # closed-class words only: far less sensitive to topic and genre
    FUNC = {"prep", "conj", "advb", "nega", "prps", "prde", "prin", "inrg", "intj"}
    vocab = [l for l, _ in anchor_tokens.most_common(2000) if l not in EXCLUDE_LEX and lex_sp.get(l) in FUNC][:80]
print("vocab size", len(vocab))
VT = ["wayq", "weqt", "perf", "impf", "impv", "ptca", "ptcp", "infc", "infa"]
VS = ["qal", "nif", "piel", "pual", "hit", "hif", "hof"]

def featurize(tok):
    n = len(tok)
    c = Counter(t[0] for t in tok)
    f = {f"lex:{l}": c[l] / n for l in vocab}
    verbs = [t for t in tok if t[1]]
    nv = max(1, len(verbs))
    vtc = Counter(("weqt" if (t[1] == "perf" and t[5]) else t[1]) for t in verbs)
    for v in VT:
        f[f"vt:{v}"] = vtc[v] / nv
    vsc = Counter(t[2] for t in verbs)
    for v in VS:
        f[f"vs:{v}"] = vsc[v] / nv
    f["sfx:all"] = sum(t[3] for t in tok) / n
    f["sfx:verb"] = sum(t[4] for t in tok) / nv
    f["sfx:et"] = sum(1 for t in tok if t[0] == ">T" and t[3]) / n
    f["verbs/token"] = len(verbs) / n
    return f

rows = []
for u, toks in units.items():
    for i, ch in enumerate(chunks(toks)):
        r = featurize(ch)
        r.update(unit=u, chunk=i, ntok=len(ch), **meta[u])
        rows.append(r)
df = pd.DataFrame(rows)
featcols = [c for c in df.columns if ":" in c or c == "verbs/token"]
if FEATSET != "full":   # drop verb-form distribution (narrative vs. predictive discourse = genre)
    featcols = [c for c in featcols if not c.startswith("vt:") and c != "verbs/token"]
print("units:", df.unit.nunique(), "chunks:", len(df), "features:", len(featcols))
print(df.groupby("role").unit.nunique())

# standardise on anchors
X = df[featcols].values.astype(float)
mu = X[df.role == "anchor"].mean(0); sd = X[df.role == "anchor"].std(0) + 1e-9
Z = (X - mu) / sd
df_z = pd.DataFrame(Z, columns=featcols)

from sklearn.linear_model import RidgeCV, LogisticRegression
from sklearn.decomposition import PCA

anc = (df.role == "anchor").values
groups = df.unit.values
y_date = df.date.values

# ---- 1. leave-one-text-out date regression on chunks, then average per text
loo_pred = {}
alphas = np.logspace(0, 4, 20)
for u in sorted(set(groups[anc])):
    tr = anc & (groups != u)
    te = groups == u
    m = RidgeCV(alphas=alphas).fit(Z[tr], y_date[tr].astype(float))
    loo_pred[u] = float(np.median(m.predict(Z[te])))
err = pd.DataFrame([(u, meta[u]["date"], p, p - meta[u]["date"]) for u, p in loo_pred.items()],
                   columns=["text", "anchor_date", "loo_predicted", "error"]).sort_values("anchor_date")
mae = err.error.abs().mean()
print(err.to_string(index=False))
print(f"Leave-one-text-out MAE = {mae:.0f} years")

final = RidgeCV(alphas=alphas).fit(Z[anc], y_date[anc].astype(float))
df["pred_date"] = final.predict(Z)
print("ridge alpha", final.alpha_)

# bootstrap over anchor TEXTS for an uncertainty band on non-anchor units
boot = defaultdict(list)
anchor_units = sorted(set(groups[anc]))
for b in range(200):
    pick = np.random.choice(anchor_units, len(anchor_units), replace=True)
    idx = np.concatenate([np.where(groups == u)[0] for u in pick])
    m = RidgeCV(alphas=alphas).fit(Z[idx], y_date[idx].astype(float))
    p = m.predict(Z)
    for u in set(groups[~anc]):
        boot[u].append(float(np.median(p[groups == u])))

summary = []
for u in sorted(set(groups)):
    sel = groups == u
    r = dict(unit=u, role=meta[u]["role"], n_chunks=int(sel.sum()), anchor_date=meta[u]["date"],
             pred_median=float(np.median(df.pred_date[sel])))
    if u in loo_pred:
        r["loo_pred"] = loo_pred[u]
    if u in boot:
        r["boot_lo"], r["boot_hi"] = np.percentile(boot[u], [5, 95])
    summary.append(r)
summ = pd.DataFrame(summary).sort_values("pred_median")

# ---- 2. period classifier, leave-one-text-out
periods = ["Classical", "6th c.", "Persian LBH", "Hellenistic"]
yp = df.period.values
loo_cls = {}
for u in anchor_units:
    tr = anc & (groups != u)
    clf = LogisticRegression(C=0.05, max_iter=5000).fit(Z[tr], yp[tr])
    pr = clf.predict_proba(Z[groups == u]).mean(0)
    loo_cls[u] = dict(zip(clf.classes_, pr))
acc = np.mean([max(v, key=v.get) == meta[u]["period"] for u, v in loo_cls.items()])
print(f"Leave-one-text-out period accuracy (text level) = {acc:.0%}")
clf = LogisticRegression(C=0.05, max_iter=5000).fit(Z[anc], yp[anc])
probs = {u: dict(zip(clf.classes_, clf.predict_proba(Z[groups == u]).mean(0))) for u in set(groups[~anc])}
for u, v in loo_cls.items():
    probs[u] = v

# ---- 3. nearest anchors (cosine on mean z-vector of text)
cent = df_z.assign(unit=df.unit).groupby("unit").mean()
def nearest(u, k=5):
    a = cent.loc[u].values
    out = []
    for v in anchor_units:
        if v == u:
            continue
        b = cent.loc[v].values
        out.append((v, float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))))
    return sorted(out, key=lambda x: -x[1])[:k]

# ---- 4. PCA on anchors for the map
pca = PCA(n_components=2).fit(cent.loc[anchor_units].values)
pc = pd.DataFrame(pca.transform(cent.values), index=cent.index, columns=["PC1", "PC2"])

# ---- output
summ["P_Classical"] = summ.unit.map(lambda u: probs.get(u, {}).get("Classical"))
summ["P_6th"] = summ.unit.map(lambda u: probs.get(u, {}).get("6th c."))
summ["P_Persian"] = summ.unit.map(lambda u: probs.get(u, {}).get("Persian LBH"))
summ["P_Hellenistic"] = summ.unit.map(lambda u: probs.get(u, {}).get("Hellenistic"))
summ["nearest"] = summ.unit.map(lambda u: "; ".join(f"{v} ({s:.2f})" for v, s in nearest(u, 4)))
summ = summ.merge(pc, left_on="unit", right_index=True)
summ.to_csv(os.path.join(RES, "hebrew_chronolect_summary" + TAG + ".csv"), index=False)
err.to_csv(os.path.join(RES, "hebrew_chronolect_loo_errors" + TAG + ".csv"), index=False)
df[["unit", "chunk", "role", "date", "pred_date"]].to_csv(os.path.join(RES, "hebrew_chronolect_chunks" + TAG + ".csv"), index=False)
coef = pd.Series(final.coef_, index=featcols).sort_values()
coef.to_csv(os.path.join(RES, "hebrew_chronolect_coefficients" + TAG + ".csv"))
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 120)
print(summ[["unit", "role", "n_chunks", "anchor_date", "loo_pred", "pred_median", "boot_lo", "boot_hi",
            "P_Classical", "P_6th", "P_Persian", "P_Hellenistic"]].round(2).to_string(index=False))
print("\nMost 'early' features:\n", coef.head(15).round(1).to_string())
print("\nMost 'late' features:\n", coef.tail(15).round(1).to_string())
for u in [x for x in summ.unit if x.startswith("MT Daniel")] + ["DSS-copy Daniel (Hebrew parts)", "MT Ecclesiastes", "MT Jonah", "MT Isaiah 56-66"]:
    if u in cent.index:
        print(u, "->", nearest(u, 5))
json.dump(dict(mae=mae, period_acc=acc, chunk=CHUNK, n_features=len(featcols)),
          open(os.path.join(RES, "hebrew_chronolect_meta" + TAG + ".json"), "w"))
