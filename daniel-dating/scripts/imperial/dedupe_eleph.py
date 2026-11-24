"""Find duplicate Elephantine records (object vs text records carrying the same edition).
usage: dedupe_eleph.py TOKENS.tsv DOCS.tsv OUT_keep.tsv
A record is dropped if >=50% of its word 3-grams (A/R tokens) occur in a larger record."""
import sys, collections
toks = collections.defaultdict(list)
for i, line in enumerate(open(sys.argv[1], encoding="utf-8")):
    if i == 0: continue
    f = line.rstrip("\n").split("\t")
    if f[5] != "F":
        toks[f[0]].append(f[4])
    else:
        toks[f[0]].append("#")
docs = {}
for i, line in enumerate(open(sys.argv[2], encoding="utf-8")):
    if i == 0: continue
    f = line.rstrip("\n").split("\t"); docs[f[0]] = f
def grams(seq):
    return {tuple(seq[j:j+3]) for j in range(len(seq)-2) if "#" not in seq[j:j+3]}
G = {d: grams(t) for d, t in toks.items()}
index = collections.defaultdict(set)
for d, g in G.items():
    for x in g: index[x].add(d)
size = lambda d: (len(toks[d]), -int(d))
order = sorted(G, key=lambda d: size(d), reverse=True)
dropped = {}
for d in order:
    g = G[d]
    if len(g) < 3: continue
    cnt = collections.Counter()
    for x in g:
        for e in index[x]:
            if e != d and size(e) > size(d) and e not in dropped:
                cnt[e] += 1
    if cnt:
        e, c = cnt.most_common(1)[0]
        if c / len(g) >= 0.5:
            dropped[d] = (e, round(c / len(g), 2))
with open(sys.argv[3], "w", encoding="utf-8") as out:
    out.write("doc\tkeep\tdup_of\toverlap\ttitle\trefs\n")
    for d in sorted(docs):
        if d in dropped:
            out.write(f"{d}\t0\t{dropped[d][0]}\t{dropped[d][1]}\t{docs[d][1]}\t{docs[d][5]}\n")
        else:
            out.write(f"{d}\t1\t\t\t{docs[d][1]}\t{docs[d][5]}\n")
print("records", len(docs), "dropped", len(dropped))
