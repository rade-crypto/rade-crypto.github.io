"""Hebrew linguistic variables (choice between two equivalent expressions).

Each variable records which of two alternatives a writer chose where both were available,
so the measure is largely independent of genre and topic.  Shares are computed from
lexemes / morphemes, never from spelling conventions.

Output: results/hebrew_variables.csv, results/hebrew_variables.md
"""
import sys, os, csv, math
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from corpora import load_bhsa, load_dss

RES = os.path.join(os.path.dirname(__file__), "..", "results")

def wilson(k, n, z=1.96):
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0, c - h), min(1, c + h)

GROUPS_MT = {
    "Classical prose (Gen-Kings)": {"Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges",
                                     "1_Samuel", "2_Samuel", "1_Kings", "2_Kings"},
    "6th c.: Ezekiel": {"Ezekiel"},
    "6th c.: Jeremiah": {"Jeremiah"},
    "6th c.: Haggai + Zechariah 1-8": {"Haggai", "Zechariah<9"},
    "Persian LBH: Ezra-Nehemiah": {"Ezra", "Nehemiah"},
    "Persian LBH: Chronicles": {"1_Chronicles", "2_Chronicles"},
    "LBH: Esther": {"Esther"},
    "Qohelet": {"Ecclesiastes"},
    "DANIEL Hebrew (1:1-2:4a, 8-12)": {"Daniel"},
}
VARS = [
    ("1cs pronoun", "ʾānōkî", "ʾănî"),
    ("'kingdom'", "mamlākâ", "malkût"),
    ("1cs wayyiqtol", "short (wāʾeqṭōl)", "long (wāʾeqṭəlâ)"),
    ("object pronoun", "ʾēt + suffix", "verbal suffix"),
    ("paragogic nun (yiqtol 2/3mp)", "with -ûn", "without (-û)"),
    ("'arise/stand'", "qûm", "ʿāmad"),
    ("relative", "ʾăšer", "še-"),
    ("'in order to/so that'", "ləmaʿan", "bišbîl / baʿăbûr"),
]
counts = defaultdict(lambda: defaultdict(Counter))

def tally(group, var, which):
    counts[var][group][which] += 1

def classify(lex, vt, ps, nu, gn, vbe_par, has_sfx, prev_lex):
    out = []
    if lex == ">NKJ": out.append(("1cs pronoun", "old"))
    if lex == ">NJ": out.append(("1cs pronoun", "new"))
    if lex in ("MMLKH/", "MMLKWT/"): out.append(("'kingdom'", "old"))
    if lex == "MLKWT/": out.append(("'kingdom'", "new"))
    if vt == "wayq" and ps == "p1" and nu == "sg" and not lex.endswith("H["):
        out.append(("1cs wayyiqtol", "new" if vbe_par == "H" else "old"))
    if vt in ("perf", "impf", "wayq", "impv") and has_sfx:
        out.append(("object pronoun", "new"))
    if lex == ">T" and has_sfx:
        out.append(("object pronoun", "old"))
    if vt == "impf" and ps in ("p2", "p3") and nu == "pl" and gn == "m":
        if vbe_par == "WN": out.append(("paragogic nun (yiqtol 2/3mp)", "old"))
        elif vbe_par == "W": out.append(("paragogic nun (yiqtol 2/3mp)", "new"))
    if lex == "QWM[": out.append(("'arise/stand'", "old"))
    if lex == "<MD[": out.append(("'arise/stand'", "new"))
    if lex == ">CR": out.append(("relative", "old"))
    if lex == "C": out.append(("relative", "new"))
    if lex == "LM<N": out.append(("'in order to/so that'", "old"))
    if lex in ("BCBJL", "B<BWR"): out.append(("'in order to/so that'", "new"))
    return out

# ---- BHSA
A = load_bhsa("book chapter lex sp vt vs ps nu gn prs vbe language")
F, L, T = A.F, A.L, A.T
for w in F.otype.s("word"):
    if F.language.v(w) != "Hebrew":
        continue
    b, c, v = T.sectionFromNode(w)
    key = b
    if b == "Zechariah":
        key = "Zechariah<9" if c < 9 else "Zechariah9+"
    groups = [g for g, bs in GROUPS_MT.items() if key in bs or b in bs]
    if not groups:
        continue
    if b == "Daniel":
        groups.append(f"  Daniel ch.{1 if c == 2 else c}")
    vt = F.vt.v(w) if F.sp.v(w) == "verb" else None
    vbe = F.vbe.v(w)
    par = "H" if vbe == "H=" else ("WN" if vbe == "WN" else ("W" if vbe == "W" else ""))
    has_s = F.prs.v(w) not in ("absent", "n/a", None)
    for var, which in classify(F.lex.v(w), vt, F.ps.v(w), F.nu.v(w), F.gn.v(w), par, has_s, None):
        for g in groups:
            tally(g, var, which)

# ---- DSS non-biblical Hebrew
import re
D = load_dss("scroll biblical lang lex_etcbc vt_etcbc ps_etcbc nu_etcbc gn_etcbc g_prs_etcbc g_vbe_etcbc type morpho full")
F2, L2 = D.F, D.L
PS = {"p1": "p1", "p2": "p2", "p3": "p3"}
for w in F2.otype.s("word"):
    if F2.lang.v(w) is not None or F2.biblical.v(w) or F2.type.v(w) != "glyph":
        continue
    lex = F2.lex_etcbc.v(w)
    if not lex:
        continue
    vt = F2.vt_etcbc.v(w); vt = vt if vt not in ("NA", "unknown", None, "") else None
    nu = {"sg": "sg", "pl": "pl"}.get(F2.nu_etcbc.v(w))
    gn = F2.gn_etcbc.v(w)
    # Abegg morphology marks the long (paragogic-he) form with a final 'h' in the morph code;
    # paragogic nun is read off the consonants of the host word (suffixes follow the ׳ mark)
    morph = F2.morpho.v(w) or ""
    host = re.sub(r"[^\u05d0-\u05ea]", "", (F2.full.v(w) or "").split("׳")[0])
    par = ""
    if re.search(r"1csh", morph):
        par = "H"
    elif vt == "impf":
        par = "WN" if host.endswith("ון") else ("W" if host.endswith("ו") else "")
    has_s = F2.g_prs_etcbc.v(w) not in ("NA", None, "")
    for var, which in classify(lex, vt, F2.ps_etcbc.v(w), nu, gn, par, has_s, None):
        tally("Qumran non-biblical Hebrew (2nd-1st c. BCE)", var, which)

# ---- ETCBC extrabiblical: Epigraphic Hebrew and Rabbinic Hebrew (same annotation scheme as BHSA)
from corpora import load_extra
from extra_tokens import extra_tokens, bhsa_lex_map
EA = load_extra()
_lexmap = bhsa_lex_map(F)
EXG = {"EX Epigraphic Hebrew c. 700-587 BCE": "Epigraphic Hebrew c. 700-587 BCE (Arad, Lachish, Siloam, ...)",
       "EX Mishnah: Pirqe Avot (c. 200-250 CE)": "Rabbinic Hebrew c. 200-250 CE (Pirqe Avot, Mekhilta Shirata)",
       "EX Mekhilta: Shirata (3rd c. CE)": "Rabbinic Hebrew c. 200-250 CE (Pirqe Avot, Mekhilta Shirata)"}
for u, toks in extra_tokens(EA, _lexmap).items():
    g = EXG.get(u)
    if not g:
        continue
    for t in toks:
        cons = (t["cons"] or "").replace("ן", "נ")
        par = ""
        if t["vt"] == "wayq" and t["ps"] == "p1" and t["nu"] == "sg":
            par = "H" if cons.endswith("ה") else ""
        elif t["vt"] == "impf":
            par = "WN" if cons.endswith("ונ") else ("W" if cons.endswith("ו") else "")
        for var, which in classify(t["lex"], t["vt"], t["ps"], t["nu"], t["gn"], par, t["has_suffix"], None):
            tally(g, var, which)

ORDER = ["Epigraphic Hebrew c. 700-587 BCE (Arad, Lachish, Siloam, ...)"] + list(GROUPS_MT)[:-1] + ["Qumran non-biblical Hebrew (2nd-1st c. BCE)", "Rabbinic Hebrew c. 200-250 CE (Pirqe Avot, Mekhilta Shirata)", "DANIEL Hebrew (1:1-2:4a, 8-12)"] + \
        [f"  Daniel ch.{c}" for c in (1, 8, 9, 10, 11, 12)]
rows = []
md = ["# Hebrew linguistic variables\n", "Share of the LATER variant where a writer chose between two equivalents.\n"]
for var, old, new in VARS:
    md.append(f"\n## {var}: {old} (earlier) vs {new} (later)\n\n| corpus | earlier | later | share later (95% CI) |\n|---|---|---|---|")
    for g in ORDER:
        c = counts[var][g]; n = c["old"] + c["new"]
        if n == 0:
            continue
        p, lo, hi = wilson(c["new"], n)
        rows.append(dict(variable=var, earlier=old, later=new, corpus=g.strip(), n_earlier=c["old"], n_later=c["new"],
                         share_later=round(p, 3), ci_lo=round(lo, 3), ci_hi=round(hi, 3)))
        md.append(f"| {g.strip()} | {c['old']} | {c['new']} | {p:.0%} ({lo:.0%}-{hi:.0%}) |")
with open(os.path.join(RES, "hebrew_variables.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
open(os.path.join(RES, "hebrew_variables.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))
