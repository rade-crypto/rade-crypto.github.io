"""Build word lists for Genizah MSS A-F from parsed bensira.org lines (out/lines/*.json)."""
import sys, json, glob, os, re, unicodedata, collections

indir, outpath, logpath = sys.argv[1], sys.argv[2], sys.argv[3]
HEB = set(chr(c) for c in range(0x05D0, 0x05EB))
UNC_MARKS = {'֯', 'ׄ'}
SEPS = set(' \t\xa0׃·.־,;:׀–~')

def norm(t):
    t = unicodedata.normalize('NFKD', t)
    out = []
    for ch in t:
        o = ord(ch)
        if ch in UNC_MARKS:
            out.append('¤')  # uncertainty flag placeholder
        elif 0x0591 <= o <= 0x05C7 and ch not in ('׃', '־', '׀'):
            continue  # vowel points, accents, dagesh etc.
        elif ch == '◌':
            continue
        else:
            out.append(ch)
    return ''.join(out)


SWAP = str.maketrans({'[': ']', ']': '[', '{': '}', '}': '{'})
def anomalies(t):
    """count bracket anomalies in a row assuming '[' opens and ']' closes"""
    a = 0; rec = False; dbl = False; dl = False
    i = 0
    while i < len(t):
        two = t[i:i+2]
        if two == '[[':
            a += dbl; dbl = True; i += 2; continue
        if two == ']]':
            a += (not dbl); dbl = False; i += 2; continue
        if two == '{{':
            a += dl; dl = True; i += 2; continue
        if two == '}}':
            a += (not dl); dl = False; i += 2; continue
        c = t[i]
        if c == '[':
            a += rec; rec = True
        elif c == ']':
            a += (not rec); rec = False
        i += 1
    a += rec + dbl + dl
    return a
def rowtext(l):
    return ''.join(t for k, t in l['segs'] if k == 'H')

LABEL = re.compile(r'(\d+)([rv]):(\d+)')
VERSE = re.compile(r"\((\d+):(\d+)[a-z]*\)")

words = []
log = []
for f in sorted(glob.glob(os.path.join(indir, '*.json'))):
    name = os.path.basename(f)[:-5]
    ms = name.split('_')[0]
    lines = json.load(open(f, encoding='utf-8'))
    a0 = sum(anomalies(rowtext(l)) for l in lines); a1 = sum(anomalies(rowtext(l).translate(SWAP)) for l in lines)
    default_flip = a1 < a0
    nflip = 0
    st = {'rec': False, 'mg': False, 'sup': False, 'del': False, 'dbl': False, 'car': False}
    verse = None; label = None
    cur = None  # current word buffer
    def flush():
        global cur
        if cur and (cur['letters'] or cur['ill']):
            words.append(cur)
        cur = None
    def newword():
        return {'ms': ms, 'file': name, 'line': label, 'verse': verse, 'letters': [], 'ill': 0, 'raw': '', 'abbr': False}
    started = False
    for l in lines:
        segs = l['segs']
        Ltxt = ' '.join(t for k, t in segs if k == 'L')
        m = LABEL.search(Ltxt)
        if not started:
            if m or VERSE.search(Ltxt):
                started = True
            else:
                continue
        if m:
            flush()
            for k in st:
                if st[k] and k not in ('mg', 'sup'):
                    log.append('%s %s: state %s open at new line' % (name, label, k))
                if k not in ('mg', 'sup'):
                    st[k] = False
            label = m.group(0)
        rt = rowtext(l); r0 = anomalies(rt); r1 = anomalies(rt.translate(SWAP))
        flip = (r1 < r0) or (r1 == r0 and default_flip)
        nflip += flip
        hsegs = [norm(t.translate(SWAP) if flip else t) for k, t in segs if k == 'H']
        hidx = -1
        for kind, t in segs:
            if kind == 'H' and flip:
                t = t.translate(SWAP)
            if kind == 'L':
                vs = VERSE.findall(t)
                if vs:
                    flush()
                    verse = '%s:%s' % vs[-1] if len(vs) > 1 else '%s:%s' % vs[0]
                continue
            t = norm(t)
            hidx += 1
            after_seg = ''.join(hsegs[hidx+1:])
            i = 0
            while i < len(t):
                two = t[i:i+2]
                ch = t[i]
                if two in ('[[', ']]'):
                    st['dbl'] = (two == '[['); i += 2; flush(); continue
                if two in ('{{', '}}'):
                    st['del'] = (two == '{{'); i += 2; continue
                if two in ('<<', '>>'):
                    st['sup'] = not st['sup']; i += 2; continue
                if ch == '[':
                    if st['rec']:
                        log.append('%s %s %s: [ while open -> treated as close' % (name, label, verse))
                        st['rec'] = False
                    else:
                        st['rec'] = True
                    i += 1; continue
                if ch == ']':
                    if not st['rec']:
                        rest = re.sub(r'\[\[|\]\]', '', t[i+1:] + after_seg)
                        nb = re.search(r'[\[\]]', rest)
                        if nb and nb.group(0) == ']':
                            log.append('%s %s %s: ] while closed -> treated as open' % (name, label, verse))
                            st['rec'] = True
                        else:
                            log.append('%s %s %s: ] while closed -> ignored' % (name, label, verse))
                    else:
                        st['rec'] = False
                    i += 1; continue
                if ch in '<>':
                    flush(); st['mg'] = not st['mg']; i += 1; continue
                if ch in '{}':
                    st['del'] = (ch == '{'); i += 1; continue
                if ch == '^':
                    st['car'] = not st['car']; i += 1; continue
                if ch in SEPS or ch == '-':
                    flush(); i += 1; continue
                if ch == '¤':
                    if cur and cur['letters']:
                        cur['letters'][-1]['unc'] = True
                    i += 1; continue
                if ch == '°':
                    if st['del']:
                        i += 1; continue
                    if cur is None: cur = newword(); cur['mg'] = st['mg']
                    cur['ill'] += 1; cur['raw'] += '°'; i += 1; continue
                if ch == '׳' or ch == "'":
                    if cur is not None:
                        cur['abbr'] = True; cur['raw'] += '׳'
                    i += 1; continue
                if ch in HEB:
                    if st['del']:
                        i += 1; continue
                    if cur is None or cur.get('mg') != st['mg']:
                        flush(); cur = newword(); cur['mg'] = st['mg']
                    cur['letters'].append({'c': ch, 'rec': st['rec'], 'unc': False, 'sup': st['sup'] or st['car']})
                    cur['raw'] += ('[%s]' % ch) if st['rec'] else ch
                    i += 1; continue
                log.append('%s %s: unknown char %r' % (name, label, ch))
                i += 1
        # end of row: do not flush across wrapped rows? words never span rows; flush
        flush()
    flush()
    log.append('%s: default_flip=%s rows_flipped=%d' % (name, default_flip, nflip))

# finalize
for w in words:
    w['cons'] = ''.join(L['c'] for L in w['letters'])
    w['n_rec'] = sum(1 for L in w['letters'] if L['rec'])
    w['n_unc'] = sum(1 for L in w['letters'] if L['unc'])
    tot = len(w['letters']) + w['ill']
    w['n_tot'] = tot
    w['mostly_rec'] = (w['n_rec'] + w['ill']) * 2 >= tot  # half or more missing/reconstructed
    w['witness'] = w['ms'] + ('mg' if w.get('mg') else '')
json.dump(words, open(outpath, 'w', encoding='utf-8'), ensure_ascii=False)
open(logpath, 'w', encoding='utf-8').write('\n'.join(log))
c = collections.Counter((w['witness'], w['mostly_rec']) for w in words)
for k in sorted(c): print(k, c[k])
print('log entries', len(log))
