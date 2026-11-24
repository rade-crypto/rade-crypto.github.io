import sys, re, collections, unicodedata
tsv, pat = sys.argv[1], re.compile(sys.argv[2])
NAMES = {'ְ':'shva','ֱ':'hat-seg','ֲ':'hat-pat','ֳ':'hat-qam','ִ':'hireq','ֵ':'tsere','ֶ':'segol','ַ':'patah','ָ':'qamats','ֹ':'holam','ֻ':'qubuts','ּ':'dagesh'}
dist = collections.defaultdict(collections.Counter)
ex = collections.defaultdict(list)
for line in open(tsv):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    m = pat.search(c)
    if not m: continue
    v = unicodedata.normalize("NFD", v)
    # find the first alef in vocalised token that corresponds to the prefix alef: after proclitic letters
    letters = [(i, ch) for i, ch in enumerate(v) if 'א' <= ch <= 'ת']
    pos = len(m.group(1) or "")  # number of proclitic letters
    i = letters[pos][0]
    j = letters[pos+1][0] if pos + 1 < len(letters) else len(v)
    marks = "".join(NAMES.get(ch, '') for ch in v[i+1:j] if ch in NAMES) or 'none'
    dist[corpus][marks] += 1
    if len(ex[(corpus, marks)]) < 6: ex[(corpus, marks)].append(f"{v}({ref})")
for c in dist:
    print(c, dict(dist[c].most_common()))
for k, v in ex.items():
    print(k, " ".join(v))
