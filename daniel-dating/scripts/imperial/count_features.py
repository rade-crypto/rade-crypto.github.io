"""Count features per sub-corpus; write CSVs.
usage: count_features.py OUTDIR"""
import sys, os, csv, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import features as F
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(BASE, "corpus")
out = sys.argv[1]

def read_tokens(path):
    rows = []
    for i, line in enumerate(open(path, encoding="utf-8")):
        if i == 0: continue
        f = line.rstrip("\n").split("\t")
        rows.append(dict(doc=f[0], side=f[1], line=f[2], form=f[4], status=f[5], raw=f[6]))
    return rows

def read_docs(path):
    d = {}
    for i, line in enumerate(open(path, encoding="utf-8")):
        if i == 0: continue
        f = line.rstrip("\n").split("\t"); d[f[0]] = f
    return d

corpora = []  # (name, label, rows, docmeta)
# Elephantine
el_rows = read_tokens(os.path.join(C, "eleph_tokens.tsv"))
el_docs = read_docs(os.path.join(C, "eleph_docs.tsv"))
keep = {}
for i, line in enumerate(open(os.path.join(C, "eleph_keep.tsv"), encoding="utf-8")):
    if i == 0: continue
    f = line.rstrip("\n").split("\t"); keep[f[0]] = f[1] == "1"
def tadvol(doc, side):
    refs = el_docs[doc][5].split("|", 1)[1] if "|" in el_docs[doc][5] else ""
    m = re.search(r"TAD (?:no\.\s*)?([ABCD])[. ]?(\d+)\.(\d+)", refs)
    if "Palimpsest" in side and re.search(r"C3\.7", refs):
        return "C3-4 (accounts/lists)"
    if doc == "306603" and side.startswith("Mem"):
        return "C3-4 (accounts/lists)"
    if not m:
        if "CG no" in refs: return "D (ostraca, fragments, misc.)"
        return "no TAD ref (fragments)"
    v, n = m.group(1), int(m.group(2))
    if v == "C" and n == 1: return "C1 (Ahiqar)"
    if v == "C" and n == 2: return "C2 (Bisitun)"
    if v == "C": return "C3-4 (accounts/lists)"
    if v == "A" and n == 2: return "A2 (Hermopolis letters)"
    if v == "A" and n == 6: return "A6 (Arshama, Berlin/Cairo copies)"
    return {"A": "A3-5 (letters)", "B": "B (contracts)", "D": "D (ostraca, fragments, misc.)"}[v]
el_rows = [r for r in el_rows if keep.get(r["doc"], False)]
for r in el_rows:
    r["date"] = (el_docs[r["doc"]][3] + ".." + el_docs[r["doc"]][4]).strip(".")
    r["group"] = tadvol(r["doc"], r["side"])
    r["ref"] = el_docs[r["doc"]][5].split("|", 1)[1] if "|" in el_docs[r["doc"]][5] else ""
corpora.append(("ELEPH", "Elephantine/Syene Aramaic (ERC Elephantine DB), 5th c. BCE", el_rows))
ar = read_tokens(os.path.join(C, "arshama_tokens.tsv"))
for r in ar: r["group"] = "Arshama (Driver letters)"; r["ref"] = "TAD " + r["doc"]
corpora.append(("ARSHAMA", "Arshama letters (TAD A6.3-6.15, typed TAD text, OCR+proofread), late 5th c. BCE", ar))
for pre, lab in (("idum", "Idumean ostraca (IIP), 4th c. BCE"), ("mare", "Maresha Aramaic (IIP), 4th-2nd c. BCE"), ("mger", "Mt Gerizim Aramaic dedications (IIP), 3rd-2nd c. BCE")):
    rows = read_tokens(os.path.join(C, f"iip_{pre}_tokens.tsv"))
    if pre == "mger":
        rows = [r for r in rows if r["doc"] not in ("mger0384", "mger0388", "mger0394", "mger0395")]  # Hebrew-language items
    for r in rows: r["group"] = pre; r["ref"] = r["doc"]
    corpora.append((pre.upper(), lab, rows))
ba = read_tokens(os.path.join(C, "ba_tokens.tsv"))
for r in ba:
    r["group"] = r["doc"]; r["ref"] = f'{r["doc"]} {r["side"]}:{r["line"]}'
    raw, lem, mor = (r["raw"].split("|") + ["", ""])[:3]
    r["lemma"], r["morph"] = lem, mor
corpora.append(("BA_DAN", "Biblical Aramaic, Daniel 2:4b-7:28 (OSHB/WLC ketiv)", [r for r in ba if r["doc"] == "Dan"]))
corpora.append(("BA_EZRA", "Biblical Aramaic, Ezra 4:8-6:18, 7:12-26 (OSHB/WLC ketiv)", [r for r in ba if r["doc"] == "Ezra"]))

OVR = {}
for row in csv.reader(open(os.path.join(BASE, "curation", "token_overrides.tsv"), encoding="utf-8"), delimiter="\t"):
    if row and not row[0].startswith("#") and len(row) >= 6:
        OVR[(row[0], row[1], row[2], row[3], row[4])] = row[5]
def apply_ovr(name, r, res):
    out = []
    for feat, var in res:
        act = OVR.get((name, r["doc"], r["line"], r["form"], feat)) or OVR.get((name, r["doc"], "*", r["form"], feat))
        if act == "drop": continue
        out.append((feat, act if act else var))
    return out
CAUS_STEMS, REFL_STEMS = set("haH"), set("uMiPtvzr")
def verb_stem(morph):
    for p in morph.split("/"):
        if p.startswith("AV"): return p[2:3]
    return ""
def spelled_prefix(form, kind):
    s = F.strip_w(form)
    if kind == "caus":
        if s.startswith("ה") or (len(s) > 2 and s[0] in "ילמתנא" and s[1] == "ה"): return "h- (haphel)"
        if s.startswith("א") or (len(s) > 2 and s[0] in "ילמתנ" and s[1] == "א"): return "ʾ- (aphel)"
        return "no prefix letter visible"
    else:
        if re.match(r"^(ה|לה)(ת|[שסצז][תטד])", s): return "ht- (hitpe/aal)"
        if re.match(r"^(א|לא)(ת|[שסצז][תטד])", s): return "ʾt- (itpe/aal)"
        return "no prefix letter visible"

def classify_row(name, r):
    res = F.classify(r["form"], r["raw"])
    if not name.startswith("BA"):
        res = [x for x in res if not (x[0] == "F11a_pron2ms" and x[1] == "אנתה")]  # outside BA, אנתה = 'woman/wife' (checked)
    if name.startswith("BA"):
        mor, lem = r["morph"], r["lemma"]
        st = verb_stem(mor)
        res = [x for x in res if x[0] not in ("F2_causative", "F3_reflexive")]
        if not re.search(r"Sp3m", mor): res = [x for x in res if x[0] != "F1a_sfx3mp"]
        if not re.search(r"Sp2m", mor): res = [x for x in res if x[0] != "F1b_sfx2mp"]
        if "AV" in mor and re.search(r"V[^/]*/Sp[23]m", mor):
            res = [("F1c_verbal_obj_sfx", v) if f in ("F1a_sfx3mp", "F1b_sfx2mp") else (f, v) for f, v in res]
        if st in CAUS_STEMS: res.append(("F2_causative", spelled_prefix(r["form"], "caus")))
        if st in REFL_STEMS: res.append(("F3_reflexive", spelled_prefix(r["form"], "refl")))
        if r["form"] in ("אל",) and "Pd" in mor: res = [x for x in res if x[0] != "F5_demPl"] + [("F5_demPl", "אל (dem.)")]
        elif any(x[0] == "F5_demPl" for x in res) and "Pd" not in mor: res = [x for x in res if x[0] != "F5_demPl"]
        if any(x[0] == "F7_earth" for x in res) and not re.search(r"(^|/)(772|778)", lem): res = [x for x in res if x[0] != "F7_earth"]
        if any(x[0] == "F7_earth" for x in res) and "Ncfsc/Sd" in mor: res = [x for x in res if x[0] != "F7_earth"]  # Dan 2:39 'inferior'
        if any(x[0] == "F10_objmark" for x in res) and "To" not in mor: res = [x for x in res if x[0] != "F10_objmark"]
        if any(x[0] == "F9c_that" for x in res) and "Pd" not in mor: res = [x for x in res if x[0] != "F9c_that"]
        if r["form"] == "להונ" and "1934" in lem: res = [x for x in res if x[0] != "F1a_sfx3mp"] + [("F11e_impf_hwy_prefix", "l-")]
        if any(x[0] == "F11a_pron2ms" for x in res) and "Pp2m" not in mor: res = [x for x in res if x[0] != "F11a_pron2ms"]
    return apply_ovr(name, r, res)

os.makedirs(out, exist_ok=True)
counts = collections.defaultdict(lambda: [0, set(), 0, set()])
gcounts = collections.defaultdict(lambda: [0, set(), 0, set()])
summary = []
audit = open(os.path.join(out, "audit_hits.csv"), "w", encoding="utf-8", newline="")
aw = csv.writer(audit)
aw.writerow(["corpus", "group", "doc", "doc_refs", "db_date_BCE(neg)", "side", "line", "form_normalised", "raw", "status", "feature", "variant"])
for name, label, rows in corpora:
    docs = {r["doc"] for r in rows}
    nA = sum(1 for r in rows if r["status"] == "A")
    summary.append([name, label, len(docs), len(rows), nA])
    for r in rows:
        if r["status"] == "F": continue
        for feat, var in classify_row(name, r):
            k = (name, feat, var); g = (name, r["group"], feat, var)
            for key, store in ((k, counts), (g, gcounts)):
                if r["status"] == "A":
                    store[key][0] += 1; store[key][1].add(r["doc"])
                store[key][2] += 1; store[key][3].add(r["doc"])
            aw.writerow([name, r["group"], r["doc"], r["ref"], r.get("date", ""), r["side"], r["line"], r["form"], r["raw"].split("|")[0], r["status"], feat, var])
audit.close()
with open(os.path.join(out, "corpus_summary.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["corpus", "description", "documents", "word_tokens_all", "word_tokens_fully_attested"])
    w.writerows(summary)
with open(os.path.join(out, "feature_counts.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["corpus", "feature", "variant", "tokens_attested", "docs_attested", "tokens_incl_restored", "docs_incl_restored"])
    for (n, f, v), c in sorted(counts.items()):
        w.writerow([n, f, v, c[0], len(c[1]), c[2], len(c[3])])
with open(os.path.join(out, "feature_counts_by_group.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["corpus", "group", "feature", "variant", "tokens_attested", "docs_attested", "tokens_incl_restored", "docs_incl_restored"])
    for (n, g, f, v), c in sorted(gcounts.items()):
        w.writerow([n, g, f, v, c[0], len(c[1]), c[2], len(c[3])])
# ratios (attested tokens), wide table
feats = sorted({(f, v) for (n, f, v) in counts})
names = [c[0] for c in corpora]
with open(os.path.join(out, "feature_table_wide.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["feature", "variant"] + [f"{n} tok(docs)" for n in names] + [f"{n} share%" for n in names])
    tot = collections.Counter()
    for (n, f, v), c in counts.items():
        if "ambiguous" not in v and "no prefix" not in v and "(?)" not in v: tot[(n, f)] += c[0]
    for f, v in feats:
        cells = []; shares = []
        for n in names:
            c = counts.get((n, f, v))
            cells.append(f"{c[0]} ({len(c[1])})" if c else "0")
            t = tot[(n, f)]
            shares.append(f"{100*c[0]/t:.0f}" if (c and t and "ambiguous" not in v and "no prefix" not in v and "(?)" not in v) else "")
        w.writerow([f, v] + cells + shares)
print("\n".join(",".join(map(str, s)) for s in summary))
# group summary + Elephantine by-group wide table
gs = collections.defaultdict(lambda: [set(), 0, 0])
for name, label, rows in corpora:
    for r in rows:
        k = (name, r["group"]); gs[k][0].add(r["doc"]); gs[k][1] += 1; gs[k][2] += r["status"] == "A"
with open(os.path.join(out, "group_summary.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["corpus", "group", "documents", "word_tokens_all", "word_tokens_fully_attested"])
    for (n, g), v in sorted(gs.items()): w.writerow([n, g, len(v[0]), v[1], v[2]])
groups = sorted(g for (n, g) in gs if n == "ELEPH")
with open(os.path.join(out, "eleph_by_group_wide.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["feature", "variant"] + groups)
    w.writerow(["(words attested)", ""] + [gs[("ELEPH", g)][2] for g in groups])
    for f, v in feats:
        if any(("ELEPH", g, f, v) in gcounts for g in groups):
            w.writerow([f, v] + [gcounts[("ELEPH", g, f, v)][0] if ("ELEPH", g, f, v) in gcounts else 0 for g in groups])
