import sys, re, collections, unicodedata
tsv, pat = sys.argv[1], re.compile(sys.argv[2])
NAMES = {'ְ':'shva','ֱ':'hat-seg','ֲ':'hat-pat','ֳ':'hat-qam','ִ':'hireq','ֵ':'tsere','ֶ':'segol','ַ':'patah','ָ':'qamats','ֹ':'holam','ֻ':'qubuts'}
d = collections.defaultdict(collections.Counter); ex = {}
for line in open(tsv):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    m = pat.search(c)
    if not m: continue
    v = unicodedata.normalize("NFD", v)
    letters = [(i, ch) for i, ch in enumerate(v) if 'א' <= ch <= 'ת']
    pos = len(m.group(1) or "")
    i = letters[pos][0]; j = letters[pos+1][0] if pos+1 < len(letters) else len(v)
    marks = "".join(NAMES.get(ch, '') for ch in v[i+1:j] if ch in NAMES) or 'none'
    d[c[pos:]][marks] += 1
    ex.setdefault((c[pos:], marks), f"{v} {ref}")
for k in sorted(d, key=lambda x: -sum(d[x].values())):
    print(k, dict(d[k]), " | ".join(ex[(k, mk)] for mk in d[k]))
