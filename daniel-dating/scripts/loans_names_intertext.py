"""Loanword strata, name forms, the 'Chaldeans', and text reuse in Daniel (BHSA data).

Outputs results/loans_names_intertext.md (+ csv files)
"""
import sys, os, re, csv
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from corpora import load_bhsa

RES = os.path.join(os.path.dirname(__file__), "..", "results")
A = load_bhsa("book chapter verse lex gloss language g_cons_utf8 sp freq_lex g_word_utf8 nametype")
F, L, T = A.F, A.L, A.T
md = []

def ref(w):
    return "%s %d:%d" % T.sectionFromNode(w)

# ------------------------------------------------------------ 1. loanwords
# Etymologies follow the standard lexica of Biblical Aramaic/Hebrew; Old Persian forms given where attested.
LOANS = {
    # lexeme: (stratum, source form, gloss)
    ">XCDRPN/": ("Persian", "OP xšaçapāvan- 'satrap'", "satrap"),
    ">DRGZR/": ("Persian", "OP *andarzakara- 'counsellor'", "counsellor"),
    "GDBR/": ("Persian", "OP *ganzabara- 'treasurer'", "treasurer"),
    "GZBR/": ("Persian", "OP *ganzabara- 'treasurer'", "treasurer"),
    "DTBR/": ("Persian", "OP *dātabara- 'law-bearer, judge'", "judge"),
    "TPTJ/": ("Persian", "OP *tayupati- 'police chief'", "magistrate"),
    "HDBR/": ("Persian", "OP *hadabāra- 'companion, minister'", "minister"),
    "HMNJK/": ("Persian", "OP *hamyānaka- 'necklace'", "necklace"),
    "PTGM/": ("Persian", "OP *patigāma- 'message'", "word, decree"),
    "RZ/": ("Persian", "OP rāza- 'secret'", "mystery"),
    "DT/": ("Persian", "OP dāta- 'law' (Behistun)", "law"),
    "ZN/": ("Persian", "OP *zana- 'kind'", "kind"),
    "HDM/": ("Persian", "OP *handāma- 'limb'", "limb"),
    "NBZBH/": ("Persian", "OP *nibāzba- 'gift'", "reward"),
    "SRK/": ("Persian", "OP *sāraka- 'chief'", "high official"),
    ">ZD>": ("Persian", "OP azdā 'known'", "publicly known"),
    "KRBLH/": ("Persian", "Iranian 'cap'", "hat"),
    "PTJC/": ("Persian", "Iranian garment term", "garment"),
    "SRBL/": ("Persian", "Iranian *šaravāra- 'trousers'", "garment"),
    "GNZ/": ("Persian", "OP *ganza- 'treasury'", "treasury"),
    "NCTWN/": ("Persian", "Iranian *ništa(van)- 'written order'", "letter"),
    ">SPRN>": ("Persian", "OP *usprna- 'completely'", "diligently"),
    ">DRZD>": ("Persian", "OP *drazdā 'with zeal'", "with zeal"),
    ">PRSKJ/": ("Persian", "OP *frasaka- 'investigator'", "investigators"),
    ">PRSTKJ/": ("Persian", "OP *frastaka- 'envoy'", "envoys"),
    ">PTM/": ("Persian", "OP *apatama- 'at last'", "at last"),
    ">CRN/": ("Persian", "OP *āčarna- 'furnishing'", "structure"),
    "PRTMJM/": ("Persian", "OP fratama- 'foremost'", "nobles"),
    "PTBG/": ("Persian", "OP *patibaga- 'portion'", "royal rations"),
    ">PDN/": ("Persian", "OP apadāna- 'columned hall' (Susa, Artaxerxes II)", "palace"),
    "QJTRWS/": ("Greek", "kitharis / kithara", "lyre"),
    "QJTRS/": ("Greek", "kitharis / kithara", "lyre"),
    "PSNTRJN/": ("Greek", "psaltērion", "harp"),
    "SWMPNJH/": ("Greek", "symphōnia", "(instrument / ensemble)"),
}
present = defaultdict(list)
langtot = Counter()
for w in F.otype.s("word"):
    b = T.sectionFromNode(w)[0]
    if b not in ("Daniel", "Ezra", "Nehemiah", "Esther", "Chronicles", "1_Chronicles", "2_Chronicles"):
        continue
    key = f"{b} ({F.language.v(w)})"
    langtot[key] += 1
    if F.lex.v(w) in LOANS:
        present[F.lex.v(w)].append(w)
# also find Greek words by consonants in case lexeme codes differ
for w in L.d(T.nodeFromSection(("Daniel", 3)), "word"):
    c = F.g_cons_utf8.v(w)
    if c in ("קיתרס", "קתרס", "פסנתרין", "פסנטרין", "סומפניה", "סיפניה") and F.lex.v(w) not in LOANS:
        LOANS[F.lex.v(w)] = ("Greek", {"ק": "kitharis", "פ": "psaltērion", "ס": "symphōnia"}[c[0]], F.gloss.v(w))
        present[F.lex.v(w)].append(w)
present = defaultdict(list)
for w in F.otype.s("word"):
    if F.lex.v(w) in LOANS:
        present[F.lex.v(w)].append(w)
md.append("# Loanwords, names, 'Chaldeans', and text reuse\n\n## 1. Persian and Greek loanwords\n")
md.append("| word | stratum | etymon | Daniel refs | other books |\n|---|---|---|---|---|")
strata = Counter()
for lex, ws in sorted(present.items(), key=lambda x: (LOANS[x[0]][0], x[0])):
    st, et, gl = LOANS[lex]
    dref = sorted({ref(w) for w in ws if T.sectionFromNode(w)[0] == "Daniel"})
    oth = Counter(T.sectionFromNode(w)[0] for w in ws if T.sectionFromNode(w)[0] != "Daniel")
    for w in ws:
        strata[(T.sectionFromNode(w)[0], st)] += 1
    md.append(f"| {F.g_cons_utf8.v(ws[0])} '{gl}' | {st} | {et} | {', '.join(dref) if dref else '-'} | "
              f"{', '.join(f'{k} {v}' for k, v in oth.items()) or '-'} |")
md.append("\nTokens per stratum: " + ", ".join(f"{b} {s}: {n}" for (b, s), n in sorted(strata.items())))
# Persian titles inside the Babylonian-court stories
md.append("\n**Persian administrative titles placed in Nebuchadnezzar's court (Dan 3:2-3, 3:27):** " +
          ", ".join(sorted({f"{F.g_cons_utf8.v(w)} ({ref(w)})" for lex, ws in present.items() for w in ws
                            if T.sectionFromNode(w)[0] == "Daniel" and T.sectionFromNode(w)[1] == 3 and LOANS[lex][0] == "Persian"})))

# ------------------------------------------------------------ 2. Nebuchadnezzar spellings
md.append("\n## 2. Spelling of 'Nebuchadnezzar' by book\n")
md.append("Akkadian Nabû-kudurri-uṣur -> the -r- form (Nebuchadrezzar) is closer to the original; the -n- form is a later dissimilated form.\n")
md.append("| book | -r- form (נבוכדראצר) | -n- form (נבוכדנאצר / נבכדנצר) |\n|---|---|---|")
nb = defaultdict(Counter)
for w in F.otype.s("word"):
    c = F.g_cons_utf8.v(w) or ""
    if c.startswith("נבוכד") or c.startswith("נבכד"):
        b = T.sectionFromNode(w)[0]
        nb[b]["r" if "דר" in c else "n"] += 1
for b, c in sorted(nb.items(), key=lambda x: -sum(x[1].values())):
    md.append(f"| {b} | {c['r']} | {c['n']} |")

# ------------------------------------------------------------ 3. 'Chaldeans'
md.append("\n## 3. 'Chaldean(s)' - ethnic/national vs. professional (diviner caste) sense\n")
md.append("Sense assigned from the immediate context (listed with magicians/enchanters/sorcerers = professional).\n")
PRO_WORDS = {"XRVM/", ">CP/", "KCP[", "MKCP/", "GZR/", "XKJM/", "MKCPJM/", "XRVM", ">CP", "GZRJN/"}
chal = []
for w in F.otype.s("word"):
    if F.lex.v(w) in ("KFDJ/", "KFDJM/", "KFDJ=/", "KFDJM") or (F.g_cons_utf8.v(w) or "").startswith("כשד"):
        if F.sp.v(w) in ("prep", "conj", "art"):
            continue
        b = T.sectionFromNode(w)[0]
        v = L.u(w, "verse")[0]
        ctx = {F.lex.v(x) for x in L.d(v, "word")}
        prev_v = T.nodeFromSection((b, T.sectionFromNode(w)[1], max(1, T.sectionFromNode(w)[2] - 1)))
        ctx |= {F.lex.v(x) for x in L.d(prev_v, "word")} if prev_v else set()
        prof = bool(ctx & {"XRVM/", ">CP/", "KCP[", "GZR[", "XKJM/", "MKCP/", "XRVMJN/"}) or \
               bool({F.g_cons_utf8.v(x) for x in L.d(v, "word")} & {"חרטמיא", "אשפיא", "גזריא", "חכימין", "חכימי", "חרטמים", "אשפים", "מכשפים", "חרטמין"})
        chal.append((b, ref(w), "professional" if prof else "ethnic/national"))
cc = defaultdict(Counter)
for b, r, s in chal:
    cc[b][s] += 1
md.append("| book | ethnic/national | professional |\n|---|---|---|")
for b, c in sorted(cc.items(), key=lambda x: -sum(x[1].values())):
    md.append(f"| {b} | {c['ethnic/national']} | {c['professional']} |")
md.append("\nDaniel occurrences: " + "; ".join(f"{r} ({s})" for b, r, s in chal if b == "Daniel"))

# ------------------------------------------------------------ 4. text reuse: shared lexeme 3-grams and rare words
md.append("\n## 4. Text reuse: rare words and lexeme trigrams shared by Daniel's Hebrew with other books\n")
heb = [w for w in F.otype.s("word") if F.language.v(w) == "Hebrew"]
book_of = {}
lexseq = defaultdict(list)
for w in heb:
    b = T.sectionFromNode(w)[0]
    lexseq[b].append(w)
STOP = {"W", "H", "B", "L", "K", "MN", ">T", ">CR", "KJ", ">L", "<L", "L>", "KL/", "JHWH/"}
def grams(ws, n=3):
    out = defaultdict(list)
    content = [w for w in ws if F.lex.v(w) not in STOP]
    for i in range(len(content) - n + 1):
        g = tuple(F.lex.v(x) for x in content[i:i + n])
        out[g].append(content[i])
    return out
dan_heb = [w for w in lexseq["Daniel"]]
dg = grams(dan_heb)
other = defaultdict(set)
gref = defaultdict(list)
for b, ws in lexseq.items():
    if b == "Daniel":
        continue
    for g, starts in grams(ws).items():
        if g in dg:
            other[g].add(b)
            gref[g].extend(ref(s) for s in starts[:2])
rows = []
for g, books in other.items():
    if len(books) <= 3:   # distinctive (not formulaic)
        rows.append((g, sorted({ref(s) for s in dg[g]}), sorted(set(gref[g]))[:4]))
md.append("Content-lexeme trigrams (function words removed) found in Daniel and in at most three other books:\n")
md.append("| lexemes | Daniel | elsewhere |\n|---|---|---|")
for g, dr, orf in sorted(rows, key=lambda r: r[1][0]):
    md.append(f"| {' '.join(g)} | {', '.join(dr)} | {', '.join(orf)} |")
# rare words (<=4 occurrences in HB) shared with exactly one or two other books
md.append("\nRare lexemes (<= 5 occurrences in the whole Hebrew Bible) shared by Daniel with other books:\n")
md.append("| lexeme | gloss | Daniel | elsewhere |\n|---|---|---|---|")
lexocc = defaultdict(list)
for w in heb:
    lexocc[F.lex.v(w)].append(w)
seen = set()
for w in dan_heb:
    l = F.lex.v(w)
    if l in seen or F.sp.v(w) == "nmpr":
        continue
    seen.add(l)
    occ = lexocc[l]
    if len(occ) <= 5:
        others = [x for x in occ if T.sectionFromNode(x)[0] != "Daniel"]
        if others:
            md.append(f"| {F.g_cons_utf8.v(w)} | {F.gloss.v(w)} | {', '.join(sorted({ref(x) for x in occ if T.sectionFromNode(x)[0]=='Daniel'}))} | {', '.join(ref(x) for x in others)} |")

open(os.path.join(RES, "loans_names_intertext.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))
