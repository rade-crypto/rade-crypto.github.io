"""KWIC: kwic.py TOKENS.tsv DOC FORM [width]"""
import sys
rows = [l.rstrip("\n").split("\t") for i, l in enumerate(open(sys.argv[1], encoding="utf-8")) if i]
w = int(sys.argv[4]) if len(sys.argv) > 4 else 6
for i, f in enumerate(rows):
    if f[0] == sys.argv[2] and f[4] == sys.argv[3]:
        L = " ".join(r[4] for r in rows[max(0, i-w):i] if r[0] == f[0]); R = " ".join(r[4] for r in rows[i+1:i+1+w] if r[0] == f[0])
        print(f"{f[0]}:{f[1]}:{f[2]} {f[5]} | {L} [{f[4]}] {R}")
