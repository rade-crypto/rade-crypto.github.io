"""Tokenise a plain Leiden-style transcription TSV (doc, line, text) with [] restorations.
usage: extract_plain.py IN.tsv OUT_tokens.tsv"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_eleph import tokens_from_items
out = open(sys.argv[2], "w", encoding="utf-8")
out.write("doc\tside\tline\tidx\tform\tstatus\traw\n")
bydoc = {}
for line in open(sys.argv[1], encoding="utf-8"):
    d, l, t = line.rstrip("\n").split("\t")
    bydoc.setdefault(d, []).append((l, t))
for d, lines in bydoc.items():
    items = []
    for l, t in lines:
        items.append(("LB", (l, None), None))
        items.append(("T", t, False))
    for i, r in enumerate(tokens_from_items(items, d)):
        out.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{i}\t{r[3]}\t{r[4]}\t{r[5]}\n")
