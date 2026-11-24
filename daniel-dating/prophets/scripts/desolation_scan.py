"""Find every 'permanent desolation' statement in the Latter Prophets: verses that say a place will
never be inhabited / never rebuilt / be desolate forever. Used to measure the base rate: how many such
predictions about named places came true, compared with how many did not."""
import os, sys
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
from corpora import load_bhsa
A = load_bhsa("book chapter verse lex sp nametype g_cons_utf8 gloss")
F, L, T = A.F, A.L, A.T
BOOKS = ["Isaiah", "Jeremiah", "Ezekiel", "Hosea", "Joel", "Amos", "Obadiah", "Micah", "Nahum", "Habakkuk",
         "Zephaniah", "Haggai", "Zechariah", "Malachi"]
NEG = {"L>", ">JN/", "BLJ/", "BL"}
PERM = {"<WLM/", "NYX/", "DWR/"}            # forever, everlasting, generation (l'dor wador)
rows = []
for b in BOOKS:
    for v in L.d(T.nodeFromSection((b,)), "verse"):
        ws = L.d(v, "word"); lx = [F.lex.v(w) for w in ws]
        s = set(lx)
        never_inhab = any(lx[i] in NEG and lx[j] in ("JCB[",) for i in range(len(lx)) for j in range(i + 1, min(i + 4, len(lx))))
        never_built = any(lx[i] in NEG and lx[j] in ("BNH[",) for i in range(len(lx)) for j in range(i + 1, min(i + 4, len(lx))))
        perm_waste = bool(s & PERM) and bool(s & {"CMMH/", "CMM[", "XRBH/", "CMMH=/", "MCMH/"})
        no_more = ("<WD/" in s and bool(s & NEG) and bool(s & {"JCB[", "BNH[", "HJH["})) and bool(s & {"CMMH/", "CMM[", "XRBH/", "BNH["})
        if never_inhab or never_built or perm_waste:
            c, vs = T.sectionFromNode(v)[1:]
            names = sorted({F.gloss.v(w) for w in ws if F.sp.v(w) == "nmpr" and F.lex.v(w) not in ("JHWH/",)})
            kind = "+".join(k for k, f in [("never inhabited", never_inhab), ("never rebuilt", never_built), ("perpetual waste", perm_waste)] if f)
            rows.append(dict(ref=f"{b} {c}:{vs}", kind=kind, names_in_verse=", ".join(names),
                             text=" ".join(F.g_cons_utf8.v(w) for w in ws)))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(os.path.dirname(__file__), "..", "results", "desolation_statements_raw.csv"), index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 80)
print(len(df)); print(df[["ref", "kind", "names_in_verse"]].to_string(index=False))
