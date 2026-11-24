"""Build graphic words for 2Q18 and 11Q5 (Sir 51) from ETCBC/dss (Abegg) data."""
import sys, json, re, collections
r = json.load(open(sys.argv[1], encoding='utf-8'))
HEB = set(chr(c) for c in range(0x05D0, 0x05EB))
def in_sirach(w):
    if w['scroll'] == '2Q18':
        return True
    if w['scroll'] == '11Q5':
        if w['frag'] == '21' and w['line'] in ('11', '12', '13', '14', '15', '16', '17'):
            return True
        if w['frag'] == '22' and w['line'] == '1':
            return True
    return False
seq = [w for w in r if in_sirach(w)]
# join morphological segments into graphic words
gw = []; cur = None
for w in seq:
    if cur is None:
        cur = {'scroll': w['scroll'], 'frag': w['frag'], 'line': w['line'], 'parts': [], 'signs': [], 'full': ''}
    cur['parts'].append(w['glyph'] or '')
    cur['signs'].extend(w['signs'])
    cur['full'] += (w['full'] or '')
    cur['punc'] = w.get('punc')
    if w.get('after') == ' ' or w.get('punc'):
        gw.append(cur); cur = None
if cur: gw.append(cur)
# 11Q5: keep only up to end of 51:30 ("שכרכם בעתו ׃") on col 22 line 1
out = []
stop = False
for g in gw:
    if g['scroll'] == '11Q5' and g['frag'] == '22':
        if stop: continue
        if g['punc'] == '׃' or any(s['g'] == '׃' for s in g['signs']):
            stop = True
    out.append(g)
words = []
for g in out:
    letters = []
    for s in g['signs']:
        ch = s['g']
        if ch and ch in HEB:
            if s['rem']:  # removed by ancient/modern editor
                continue
            letters.append({'c': ch, 'rec': bool(s['rec']), 'unc': bool(s['unc']), 'sup': False})
    if not letters:
        continue
    words.append({'ms': g['scroll'], 'file': 'ETCBC/dss', 'line': '%s:%s' % (g['frag'], g['line']), 'verse': None,
                  'letters': letters, 'ill': 0, 'raw': ''.join(('[%s]' % L['c']) if L['rec'] else L['c'] for L in letters),
                  'full': g['full'], 'abbr': False})
# verse assignment
v2Q18 = {('f1', '1'): '6:14', ('f1', '2'): '6:15'}
for w in words:
    fr, ln = w['line'].split(':')
    if w['ms'] == '2Q18':
        if fr == 'f1': w['verse'] = v2Q18.get((fr, ln))
        elif fr == 'f2': w['verse'] = '6:%d' % (19 + int(ln))
# 11Q5: sequential by verse-start words (graphic forms) in col 21:11-17, 22:1
starts = [('אני', '51:13'), ('באה', '51:14'), ('גם', '51:15'), ('הטיתי', '51:16'), ('ועלה', '51:17'), ('זמותי', '51:18'), ('חריתי', '51:19'), ('כפי', '51:20'), ('שכרכם', '51:30')]
si = 0; cv = None
for w in words:
    if w['ms'] != '11Q5': continue
    form = ''.join(L['c'] for L in w['letters'])
    if si < len(starts) and form == starts[si][0]:
        cv = starts[si][1]; si += 1
    w['verse'] = cv
assert si == len(starts), si
for w in words:
    w['cons'] = ''.join(L['c'] for L in w['letters'])
    w['n_rec'] = sum(1 for L in w['letters'] if L['rec'])
    w['n_unc'] = sum(1 for L in w['letters'] if L['unc'])
    w['n_tot'] = len(w['letters'])
    w['mostly_rec'] = w['n_rec'] * 2 >= w['n_tot']
    w['witness'] = {'2Q18': '2Q18', '11Q5': '11QPsa'}[w['ms']]
    w['ms'] = w['witness']
json.dump(words, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
print(collections.Counter((w['witness'], w['mostly_rec']) for w in words))
for w in words:
    print(w['witness'], w['verse'], w['line'], w['raw'], 'MOSTLY-REC' if w['mostly_rec'] else '')
