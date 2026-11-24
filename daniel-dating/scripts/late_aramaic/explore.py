import sys, re, collections
tsv, pat = sys.argv[1], re.compile(sys.argv[2])
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 200
cnt = collections.defaultdict(collections.Counter)
for line in open(tsv):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    if pat.search(c):
        cnt[c][corpus[:8]] += 1
items = sorted(cnt.items(), key=lambda x: -sum(x[1].values()))
print(len(items), "types;", sum(sum(v.values()) for k, v in items), "tokens")
print(" ".join(f"{k}:{dict(v)}" for k, v in items[:limit]))
