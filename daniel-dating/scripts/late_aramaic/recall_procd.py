import sys, random, collections, re
tsv, audit = sys.argv[1], sys.argv[2]
pos = set()
for line in open(audit, encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if f[0].startswith("relative particle (proclitic"):
        pos.add((f[1], f[3], f[5]))
verses = collections.OrderedDict()
for line in open(tsv, encoding="utf-8"):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    verses.setdefault((corpus, ref), []).append(c)
pool = []
for (corpus, ref), toks in verses.items():
    if corpus.startswith("Megillat"): continue
    for i, c in enumerate(toks):
        if re.match(r"^ו?ד", c) and c not in ("די", "ודי") and (corpus, ref, c) not in pos:
            pool.append((ref, " ".join(toks[max(0,i-3):i]) + " [" + c + "] " + " ".join(toks[i+1:i+4])))
print("non-proclitic d-initial tokens:", len(pool))
random.seed(7)
for i, (r, x) in enumerate(random.sample(pool, 100), 1):
    print(i, r, "|", x)
