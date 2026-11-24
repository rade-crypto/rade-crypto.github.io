import sys, re, collections, unicodedata
tsv, pat, want = sys.argv[1], re.compile(sys.argv[2]), sys.argv[3]
corpfilter = sys.argv[4] if len(sys.argv) > 4 else ""
NAMES = {'ְ':'shva','ֱ':'hat-seg','ֲ':'hat-pat','ֳ':'hat-qam','ִ':'hireq','ֵ':'tsere','ֶ':'segol','ַ':'patah','ָ':'qamats','ֹ':'holam','ֻ':'qubuts'}
cnt = collections.Counter()
for line in open(tsv):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    if corpfilter and not corpus.startswith(corpfilter): continue
    m = pat.search(c)
    if not m: continue
    v = unicodedata.normalize("NFD", v)
    letters = [(i, ch) for i, ch in enumerate(v) if 'א' <= ch <= 'ת']
    pos = len(m.group(1) or "")
    i = letters[pos][0]; j = letters[pos+1][0] if pos+1 < len(letters) else len(v)
    marks = "".join(NAMES.get(ch, '') for ch in v[i+1:j] if ch in NAMES) or 'none'
    if re.fullmatch(want, marks):
        cnt[c[pos:]] += 1
print(len(cnt), sum(cnt.values()))
print(" ".join(f"{k}:{v}" for k, v in cnt.most_common()))
