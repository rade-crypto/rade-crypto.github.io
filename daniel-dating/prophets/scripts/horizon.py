"""Political horizon of each prophetic book: how often each empire / ruler is NAMED (BHSA lexemes),
per book section, and in the Greek translation of Jeremiah vs the Hebrew (named-entity growth).
A writer names the powers of his own world; names of powers that rose later are a dating signal."""
import os, sys, glob
from collections import Counter, defaultdict
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
from corpora import load_bhsa
from tf.fabric import Fabric
OUT = os.path.join(os.path.dirname(__file__), "..", "results")
A = load_bhsa("book chapter verse lex gloss sp language")
F, L, T = A.F, A.L, A.T
NAMES = {"Assyria": {">CWR/"}, "Babylon/Chaldea": {"BBL/", "KFDJ/", "KFDJM/"}, "Media": {"MDJ/", "MDJ=/"}, "Persia": {"PRS/", "PRS=/", "PRSJ/"},
         "Elam": {"<JLM/", "<LMJ/"}, "Greece (Yavan)": {"JWN=/"}, "Kittim": {"KTJ/"}, "Egypt": {"MYRJM/"},
         "Nineveh": {"NJNWH/"}, "Tiglath-pileser/Pul": {"TGLT_PL>SR/", "PWL/"}, "Sargon": {"SRGWN/"}, "Sennacherib": {"SNXRJB/"},
         "Nebuchadnezzar": {"NBWKDN>YR/", "NBWKDR>YR/"}, "Cyrus": {"KWRC/"}, "Darius": {"DRJWC/"},
         "Ararat/Minni/Ashkenaz": {">RRV/", "MNJ=/", ">CKNZ/"}, "Thebes (No-Amon)": {"N>=/", "N>_>MWN/"}, "Cush": {"KWC/", "KWC=/"}}
lexes = set().union(*NAMES.values())
found = {F.lex.v(w) for w in F.otype.s("word")} & lexes
missing = lexes - found
def section(b, c):
    if b == "Isaiah": return "Isa 1-39" if c <= 39 else ("Isa 40-55" if c <= 55 else "Isa 56-66")
    if b == "Zechariah": return "Zech 1-8" if c <= 8 else "Zech 9-14"
    if b in ("1_Kings", "2_Kings"): return "Kings"
    if b in ("1_Chronicles", "2_Chronicles"): return "Chronicles"
    return b
ORDER = ["Amos", "Hosea", "Micah", "Isa 1-39", "Nahum", "Zephaniah", "Habakkuk", "Jeremiah", "Ezekiel", "Obadiah",
         "Isa 40-55", "Haggai", "Zech 1-8", "Isa 56-66", "Joel", "Malachi", "Zech 9-14", "Jonah", "Kings", "Ezra", "Nehemiah",
         "Chronicles", "Esther", "Daniel"]
cnt = defaultdict(Counter)
for w in F.otype.s("word"):
    lx = F.lex.v(w)
    if lx in lexes:
        b, c, v = T.sectionFromNode(w)
        s = section(b, c)
        for k, ls in NAMES.items():
            if lx in ls:
                cnt[s][k] += 1
df = pd.DataFrame({s: cnt[s] for s in ORDER}).T.reindex(columns=list(NAMES)).fillna(0).astype(int)
df.to_csv(os.path.join(OUT, "horizon_names_by_book.csv"))
pd.set_option("display.width", 250)
print("lexemes not found in BHSA:", missing)
print(df.to_string())

# Greek Jeremiah vs Hebrew Jeremiah: how often Babylon / Nebuchadnezzar / Chaldeans are named
LP = glob.glob(os.path.expanduser("~/text-fabric-data/github/CenterBLC/LXX/tf/*"))[0]
X = Fabric(locations=LP, silent="deep").load("book chapter verse word lex", silent="deep")
g = Counter()
for w in X.F.otype.s("word"):
    if X.T.sectionFromNode(w)[0] != "Jer":
        continue
    lx = X.F.lex.v(w) or ""
    import unicodedata
    wd = "".join(ch for ch in unicodedata.normalize("NFD", X.F.word.v(w)) if not unicodedata.combining(ch))
    for k, pat in {"Babylon": "Βαβυλ", "Nebuchadnezzar": "Ναβουχοδονοσορ", "Chaldeans": "Χαλδα"}.items():
        if wd.startswith(pat):
            g[k] += 1
h = Counter()
for w in F.otype.s("word"):
    if T.sectionFromNode(w)[0] == "Jeremiah":
        lx = F.lex.v(w)
        if lx == "BBL/": h["Babylon"] += 1
        if lx in ("NBWKDN>YR/", "NBWKDR>YR/"): h["Nebuchadnezzar"] += 1
        if lx in ("KFDJ/", "KFDJM/"): h["Chaldeans"] += 1
jt = pd.DataFrame({"Hebrew (MT)": h, "Old Greek": g})
jt.to_csv(os.path.join(OUT, "jeremiah_names_mt_vs_lxx.csv"))
print("\nJeremiah, named references:\n", jt.to_string())
