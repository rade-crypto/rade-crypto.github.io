"""Parse Reymond's Masada (Mas1h) transcription PDFs from bensira.org (SPTiberian visual-order encoding)."""
import sys, re, json, glob, os, pdfplumber
SP = {')': 'א', 'b': 'ב', 'g': 'ג', 'd': 'ד', 'h': 'ה', 'w': 'ו', 'z': 'ז', 'x': 'ח', '+': 'ט', 'y': 'י',
      'k': 'כ', 'K': 'ך', 'l': 'ל', 'm': 'מ', 'M': 'ם', 'n': 'נ', 'N': 'ן', 's': 'ס', '(': 'ע', 'p': 'פ',
      'P': 'ף', 'c': 'צ', 'C': 'ץ', 'q': 'ק', 'r': 'ר', '#': 'ש', '$': 'ש', '&': 'ש', 't': 'ת'}
MARKS = set('SX')
MIRROR = {'[': ']', ']': '['}
ORDER = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
words = []; log = []; rawlines = []
verse = None
for col in ORDER:
    f = 'Masada_%s.pdf' % col
    pdf = pdfplumber.open(os.path.join(sys.argv[1], f))
    for pg in pdf.pages:
        chars = sorted(pg.chars, key=lambda c: (-c['matrix'][5], c['x0']))
        rows = []
        for c in chars:
            b = c['matrix'][5]
            if rows and abs(rows[-1][0] - b) <= 5.5: rows[-1][1].append(c)
            else: rows.append([b, [c]])
        for b, cs in rows:
            if b > 680: continue  # page title
            cs.sort(key=lambda c: c['x0'])
            issp = lambda c: 'SPTiberian' in c['fontname']
            lab_r = ''.join(c['text'] for c in cs if not issp(c) and c['x0'] >= 495)
            lab_l = ''.join(c['text'] for c in cs if not issp(c) and c['x0'] < 160 and c['text'] not in '[].')
            text_chars = [c for c in cs if issp(c) or (c['text'] in '[].' and 140 <= c['x0'] < 495)]
            m = re.search(r'([IVX]+):(-?[\d.]+)', lab_r)
            line = m.group(0) if m else None
            mv = re.search(r'(\d+):(\d+)', lab_l)
            if mv:
                verse = '%s:%s' % (mv.group(1), mv.group(2))
            if not any(issp(c) and c['text'] in SP for c in text_chars):
                continue
            # visual string with gap-based spaces
            vis = []
            prev = None
            for c in text_chars:
                if prev is not None and c['x0'] - prev['x1'] > 2.0 and c['text'] != ' ' and (not vis or vis[-1] != ' '):
                    vis.append(' ')
                vis.append(c['text'])
                prev = c
            visual = ''.join(vis)
            visual = re.sub(r'(^|\s)-d(\s|$)', ' ', visual).replace('@', '')
            vis = list(visual)
            logical = ''.join(MIRROR.get(ch, ch) for ch in reversed(vis))
            status = 'main'
            if line is None or line.endswith('.5') or line.split(':')[1].startswith('-') or line.split(':')[1] == '0':
                status = 'interlinear/margin'
            rawlines.append({'col': col, 'line': line, 'verse': verse, 'visual': visual, 'logical_sp': logical, 'status': status})
            # tokenize logical
            rec = False
            cur = None
            def flush():
                global cur
                if cur and (cur['letters'] or cur['ill']):
                    words.append(cur)
                cur = None
            pend_unc = False
            i = 0
            L = logical
            while i < len(L):
                ch = L[i]
                if ch == ' ':
                    flush(); i += 1; continue
                if ch == '[':
                    if L[i:i+2] == '[]':
                        if cur is None: cur = {'ms': 'M', 'file': f, 'line': line, 'verse': verse, 'letters': [], 'ill': 0, 'raw': '', 'abbr': False, 'status': status}
                        cur['ill'] += 1; cur['raw'] += '[]'; i += 2; continue
                    if rec: log.append('%s %s: [ while open' % (col, line))
                    rec = True; i += 1; continue
                if ch == ']':
                    if not rec: log.append('%s %s: ] while closed' % (col, line))
                    rec = False; i += 1; continue
                if ch in MARKS:
                    pend_unc = True; i += 1; continue
                if ch == '.':
                    if cur is None: cur = {'ms': 'M', 'file': f, 'line': line, 'verse': verse, 'letters': [], 'ill': 0, 'raw': '', 'abbr': False, 'status': status}
                    cur['ill'] += 1; cur['raw'] += '°'; i += 1; continue
                if ch in SP:
                    if cur is None: cur = {'ms': 'M', 'file': f, 'line': line, 'verse': verse, 'letters': [], 'ill': 0, 'raw': '', 'abbr': False, 'status': status}
                    cur['letters'].append({'c': SP[ch], 'rec': rec, 'unc': pend_unc, 'sup': False})
                    cur['raw'] += ('[%s]' % SP[ch]) if rec else SP[ch]
                    pend_unc = False
                    i += 1; continue
                log.append('%s %s: unknown %r' % (col, line, ch)); i += 1
            flush()
            if rec: log.append('%s %s: rec open at end of line' % (col, line))
for w in words:
    w['cons'] = ''.join(L['c'] for L in w['letters'])
    w['n_rec'] = sum(1 for L in w['letters'] if L['rec'])
    w['n_unc'] = sum(1 for L in w['letters'] if L['unc'])
    w['n_tot'] = len(w['letters']) + w['ill']
    w['mostly_rec'] = (w['n_rec'] + w['ill']) * 2 >= w['n_tot']
    w['witness'] = 'M' if w['status'] == 'main' else 'M-interlinear'
json.dump(words, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(rawlines, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('\n'.join(log))
import collections
print(collections.Counter((w['witness'], w['mostly_rec']) for w in words))
