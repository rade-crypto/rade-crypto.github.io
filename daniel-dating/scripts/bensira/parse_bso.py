"""Parse bensira.org Abegg/Elizur transcription PDFs (Genizah MSS A-F) into logical-order lines.
Visual (RTL) char order -> logical by: reading right-to-left, mirroring bracket glyphs,
and reading bold Latin runs (line labels / verse markers) left-to-right."""
import sys, re, json, glob, os, unicodedata, pdfplumber

MIRROR = {'[': ']', ']': '[', '{': '}', '}': '{', '(': ')', ')': '('}
# angle brackets are NOT mirrored here: they behave as toggles anyway

def rows_of(pg):
    chars = list(pg.chars)
    chars.sort(key=lambda c: (-c['matrix'][5], -c['x0']))
    rows = []
    for c in chars:
        b = c['matrix'][5]
        if rows and abs(rows[-1]['b'] - b) <= 2.5:
            rows[-1]['c'].append(c)
        else:
            rows.append({'b': b, 'c': [c]})
    return rows

def isbold(c):
    return 'Bold' in c['fontname'] and 'Hebrew' not in c['fontname']

def drop_overlapping_spaces(cs):
    letters = [c for c in cs if c['text'].strip() and 'Hebrew' in c['fontname'] and c['x1'] - c['x0'] > 1]
    out = []
    for c in cs:
        if c['text'] == ' ' and 'Hebrew' in c['fontname']:
            w = c['x1'] - c['x0']
            ov = max([min(c['x1'], L['x1']) - max(c['x0'], L['x0']) for L in letters] + [0])
            if w < 0.5 or ov > 0.6 * w:
                DROPPED.append(1)
                continue
        out.append(c)
    return out
DROPPED = []

def row_to_logical(cs):
    cs = drop_overlapping_spaces(cs)
    cs = sorted(cs, key=lambda c: -(c['x0'] + c['x1']) / 2)
    out = []  # list of segments (kind, text)
    i = 0
    while i < len(cs):
        c = cs[i]
        if isbold(c) or (c['fontname'].split('+')[-1].startswith(('Cambria', 'Charis', 'Calibri', 'Arial')) ):
            j = i
            while j < len(cs) and (isbold(cs[j]) or cs[j]['fontname'].split('+')[-1].startswith(('Cambria', 'Charis', 'Calibri', 'Arial'))):
                j += 1
            run = ''.join(x['text'] for x in reversed(cs[i:j]))
            out.append(('L', run))
            i = j
        else:
            j = i
            while j < len(cs) and not (isbold(cs[j]) or cs[j]['fontname'].split('+')[-1].startswith(('Cambria', 'Charis', 'Calibri', 'Arial'))):
                j += 1
            seg = []
            for x in cs[i:j]:
                t = x['text']
                seg.append(MIRROR.get(t, t))
            out.append(('H', ''.join(seg)))
            i = j
    return out

def parse_pdf(path):
    pdf = pdfplumber.open(path)
    lines = []
    for pno, pg in enumerate(pdf.pages):
        for r in rows_of(pg):
            segs = row_to_logical(r['c'])
            lines.append({'page': pno, 'baseline': round(r['b'], 1), 'segs': segs})
    return lines

if __name__ == '__main__':
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(sys.argv[1], '*.pdf'))):
        name = os.path.basename(f)[:-4]
        if name.startswith(('Masada', 'Full_Masada', '2Q18')):
            continue
        lines = parse_pdf(f)
        json.dump(lines, open(os.path.join(outdir, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        with open(os.path.join(outdir, name + '.txt'), 'w', encoding='utf-8') as fh:
            for l in lines:
                fh.write(' ¦ '.join('%s:%s' % s for s in l['segs']) + '\n')
    print('done; dropped overlapping spaces:', len(DROPPED))
