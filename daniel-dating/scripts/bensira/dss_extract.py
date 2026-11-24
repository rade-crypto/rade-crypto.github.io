import sys, json
sys.path.insert(0, sys.argv[1])
from tf import read_tf
D = sys.argv[2]; out = sys.argv[3]
def spec(s):
    r = []
    for p in s.split(','):
        if not p: continue
        if '-' in p:
            a, b = p.split('-'); r.extend(range(int(a), int(b)+1))
        else: r.append(int(p))
    return r
_, osl = read_tf(D + '/oslots.tf')
_, scroll = read_tf(D + '/scroll.tf')
targets = {}
for n, v in scroll.items():
    if 1605868 <= n <= 1606868 and v in ('2Q18', '11Q5'):
        targets.setdefault(v, []).extend(spec(osl[n]))
allslots = set()
for v in targets.values(): allslots |= set(v)
feats = {}
for f in ['full', 'glyph', 'rec', 'unc', 'cor', 'alt', 'vac', 'rem', 'after', 'punc', 'type', 'fragment', 'line', 'book', 'chapter', 'verse', 'biblical', 'lang']:
    _, feats[f] = read_tf(D + '/%s.tf' % f)
# words, fragments, lines containing slots
res = []
slot2frag = {}; slot2line = {}
for n in range(1531341, 1542523):  # fragments
    if n in osl:
        s = spec(osl[n])
        if s and s[0] in allslots:
            for x in s: slot2frag[x] = (n, feats['fragment'].get(n))
for n in range(1552973, 1605868):  # lines
    if n in osl:
        s = spec(osl[n])
        if s and s[0] in allslots:
            for x in s: slot2line[x] = (n, feats['line'].get(n))
for w in range(1606869, 2107864):
    if w not in osl: continue
    s = spec(osl[w])
    if not s or s[0] not in allslots: continue
    sc = [k for k, v in targets.items() if s[0] in v][0]
    signs = [{'g': feats['glyph'].get(x), 'rec': feats['rec'].get(x), 'unc': feats['unc'].get(x), 'cor': feats['cor'].get(x), 'rem': feats['rem'].get(x), 'alt': feats['alt'].get(x), 'vac': feats['vac'].get(x), 'type': feats['type'].get(x)} for x in s]
    res.append({'scroll': sc, 'word': w, 'frag': slot2frag.get(s[0], (None, None))[1], 'line': slot2line.get(s[0], (None, None))[1],
                'full': feats['full'].get(w), 'glyph': feats['glyph'].get(w), 'book': feats['book'].get(w), 'ch': feats['chapter'].get(w), 'vs': feats['verse'].get(w), 'biblical': feats['biblical'].get(w), 'signs': signs})
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(res))
