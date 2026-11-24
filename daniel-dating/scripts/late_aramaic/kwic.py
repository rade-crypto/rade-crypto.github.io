import sys, re, collections
tsv, pat = sys.argv[1], re.compile(sys.argv[2])
width = int(sys.argv[3]) if len(sys.argv) > 3 else 5
corp = sys.argv[4] if len(sys.argv) > 4 else None
verses = collections.OrderedDict()
for line in open(tsv):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    verses.setdefault((corpus, ref), []).append(c)
for (corpus, ref), toks in verses.items():
    if corp and not corpus.startswith(corp): continue
    for i, t in enumerate(toks):
        if pat.search(t):
            print(f"{corpus[:10]} | {ref} | {' '.join(toks[max(0,i-width):i])} [{t}] {' '.join(toks[i+1:i+1+width])}")
