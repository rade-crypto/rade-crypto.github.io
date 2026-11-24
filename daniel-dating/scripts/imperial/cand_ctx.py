"""List distinct candidate forms for a regex with counts and one context.
usage: cand_ctx.py REGEX TOKENS.tsv..."""
import sys, re, collections
pat = re.compile(sys.argv[1])
cnt = collections.Counter(); ctx = {}
for path in sys.argv[2:]:
    rows = [l.rstrip("\n").split("\t") for i, l in enumerate(open(path, encoding="utf-8")) if i]
    for i, f in enumerate(rows):
        if f[5] == "F": continue
        if pat.search(f[4]):
            cnt[f[4]] += 1
            if f[4] not in ctx:
                left = " ".join(r[4] for r in rows[max(0, i-3):i] if r[0] == f[0])
                right = " ".join(r[4] for r in rows[i+1:i+4] if r[0] == f[0])
                ctx[f[4]] = f"{f[0]}:{f[2]} | {left} [{f[4]}] {right}"
for form, c in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{form}\t{c}\t{ctx[form]}")
