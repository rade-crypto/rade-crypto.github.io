import csv, json, re, glob, collections, unicodedata, os, sys
allw = json.load(open('out/all_words.json', encoding='utf-8'))
ours = collections.defaultdict(list)
for w in allw:
    if w['verse']:
        ours[(w['witness'], w['verse'])].append(w['cons'])
def clean(t):
    t = unicodedata.normalize('NFKD', t)
    return ''.join(ch for ch in t if 'א' <= ch <= 'ת')
colmap = {'MS_A': 'A', 'MS_B': 'B', 'MS_C': 'C', 'MS_D': 'D', 'MS_E': 'E', 'MS_F': 'F', 'MS_M': 'M', 'MS_Bmg': 'Bmg', 'MS_11QPsa': '11QPsa'}
stats = collections.defaultdict(lambda: [0, 0, 0])  # matched tokens, csv tokens, our tokens
miss = collections.defaultdict(list)
seen = set()
for f in sorted(glob.glob('dl/va/data/MSS_*.csv')):
    rows = list(csv.reader(open(f, encoding='utf-8')))
    hdr = rows[0]
    ch = vs = None
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows[1:]:
        if r[0]: ch = r[0]
        if r[1]: vs = r[1]
        for ci in (3, 4):
            col = hdr[ci]
            if col in colmap:
                t = clean(r[ci])
                if t: per[colmap[col]]['%s:%s' % (ch, vs)].append(t)
    for wit, d in per.items():
        for v, toks in d.items():
            if (wit, v) in seen: continue
            seen.add((wit, v))
            mm = re.match(r'(\d+):(\d+)', v); vv = '%s:%s' % mm.groups() if mm else v
            o = ours.get((wit, vv), [])
            if not o: 
                stats[wit][1] += len(toks); miss[wit].append(v); continue
            co = collections.Counter(o); ct = collections.Counter(toks)
            stats[wit][0] += sum((co & ct).values()); stats[wit][1] += len(toks); stats[wit][2] += len(o)
for wit, (a, b, c) in sorted(stats.items()):
    print('%-7s csv_tokens=%5d matched=%5d (%.1f%%) ours_in_same_verses=%5d  verses_missing_in_ours=%d %s' % (wit, b, a, 100 * a / max(b, 1), c, len(miss[wit]), miss[wit][:12]))
