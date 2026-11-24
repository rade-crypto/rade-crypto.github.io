"""Add ids, dates and part-of-speech classes to raw hits; write per-lemma CSVs.
Usage: python3 -I enrich.py RAW.csv OUTDIR"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dates import date_for  # noqa: E402

NOUN_SYM = re.compile(r"^(συμ|ξυμ|συν|ξυν)φωνι(α|ασ|αι|αν|ων|αισ|η|ησ|ην|ηισ|ησι)$")
ADJ_SYM = re.compile(r"^(συμ|ξυμ|συν|ξυν)φων(οσ|ον|ου|ω|οι|ων|οισ|ουσ|α|η|ησ|ην|αι|ασ|ωσ|οτερ\w*|οτατ\w*|οτητα|εσ)$")
KITHARA = re.compile(r"^κιθαρ(α|ασ|αν|αι|αισ|η|ησ|ην|ησι|ηισ|ων)$")
KITHARIS = re.compile(r"^κιθαρ(ισ|ιν|ι|ιοσ|ιδοσ|ιδα|ιδι|ιεσ)$")
KITHAROS = re.compile(r"^κιθαρ(οσ|ον|ου|ω|οι|ουσ|οισ)$")


def subclass(group, n):
    if group == "symphon":
        if NOUN_SYM.match(n):
            return "noun symphonia"
        if n.endswith("ημα") or n.startswith(("συμφωνησισ", "συμφωνησεωσ", "συμφωνησιν")):
            return "other noun (symphonema/symphonesis)"
        if ADJ_SYM.match(n):
            return "adjective/adverb symphonos (or ambiguous verb form)"
        return "verb symphoneo"
    if group == "psalter":
        return "psalterion" if n.startswith("ψαλτηρι") else "other"
    if group == "kithar":
        if KITHARA.match(n):
            return "noun kithara"
        if KITHARIS.match(n):
            return "noun kitharis"
        if KITHAROS.match(n):
            return "kitharos (fish/chest) or kithara-variant"
        return "derivative (kitharizo, kitharodos, etc.)"
    return ""


def main():
    raw, outdir = sys.argv[1], sys.argv[2]
    rows = list(csv.DictReader(open(raw, encoding="utf-8")))
    out = {"symphon": [], "psalter": [], "kithar": []}
    for r in rows:
        parts = r["file"].split("/")
        corpus = parts[0]
        aid, wid = parts[2], parts[3]
        yr, lab = date_for(aid, wid)
        fn = os.path.basename(r["file"])
        r2 = {
            "lemma_group": r["lemma_group"],
            "class": subclass(r["lemma_group"], r["norm"]),
            "form": r["form"],
            "norm": r["norm"],
            "approx_year": "" if yr is None else yr,
            "date_label": lab,
            "author_id": aid,
            "author": r["author"],
            "work_id": wid,
            "work": r["work"],
            "edition_file": fn,
            "corpus": corpus,
            "citation": r["citation"],
            "context": r["context"],
        }
        out[r["lemma_group"]].append(r2)
    names = {"symphon": "symphonia_hits.csv", "psalter": "psalterion_hits.csv", "kithar": "kithar_hits.csv"}
    for g, lst in out.items():
        lst.sort(key=lambda x: (x["approx_year"] if x["approx_year"] != "" else 9999, x["author_id"], x["work_id"], x["edition_file"]))
        p = os.path.join(outdir, names[g])
        with open(p, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(lst[0].keys()))
            w.writeheader()
            w.writerows(lst)
        print(p, len(lst))


if __name__ == "__main__":
    main()
