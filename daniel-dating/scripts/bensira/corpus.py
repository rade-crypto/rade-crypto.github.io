"""Finalize corpus: flag countable words, build per-witness and deduplicated corpora."""
import json, collections, re
W = json.load(open('out/all_words.json', encoding='utf-8'))
MAIN = ['B', 'A', 'M', 'C', 'D', 'E', 'F', '11QPsa', '2Q18']
for w in W:
    reason = None
    if w['mostly_rec']:
        reason = 'mostly reconstructed/illegible'
    elif len(w['cons']) == 1 and not w['abbr']:
        reason = 'single-letter fragment or section mark'
    w['countable'] = reason is None
    w['excl_reason'] = reason
    w['corpus'] = w['witness'] if w['witness'] in MAIN else ('marginalia' if w['witness'].endswith('mg') or w['witness'] == 'M-interlinear' else w['witness'])
# deduplicated: per verse choose witness by preference, unless it has < half the countable words of the best-covered witness
byv = collections.defaultdict(lambda: collections.Counter())
for w in W:
    if w['countable'] and w['corpus'] in MAIN and w['verse']:
        byv[w['verse']][w['corpus']] += 1
choice = {}
for v, c in byv.items():
    mx = max(c.values())
    for wit in MAIN:
        if c.get(wit, 0) * 2 >= mx and c.get(wit, 0) > 0:
            choice[v] = wit; break
for w in W:
    w['dedup'] = bool(w['countable'] and w['corpus'] in MAIN and w['verse'] and choice.get(w['verse']) == w['corpus'])
# words with no verse label (e.g., before first verse marker): report
nov = [w for w in W if w['countable'] and not w['verse']]
json.dump(W, open('out/corpus.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(choice, open('out/dedup_choice.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
tot = collections.Counter(); totall = collections.Counter(); excl = collections.Counter()
for w in W:
    totall[w['corpus']] += 1
    if w['countable']: tot[w['corpus']] += 1
    else: excl[(w['corpus'], w['excl_reason'])] += 1
for k in MAIN + ['marginalia']:
    print('%-10s countable=%5d  tokens=%5d' % (k, tot[k], totall[k]))
print('dedup total', sum(1 for w in W if w['dedup']))
print('dedup by source', collections.Counter(w['corpus'] for w in W if w['dedup']))
print('verses', len(choice), collections.Counter(choice.values()))
print('countable words without verse:', len(nov), [(w['witness'], w['file'], w['raw']) for w in nov][:10])
for k, v in sorted(excl.items()): print('excluded', k, v)
