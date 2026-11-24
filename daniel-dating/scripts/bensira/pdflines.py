"""Extract visual lines from bensira.org Abegg/Elizur transcription PDFs.
Output per line: list of runs in right-to-left visual order; Latin runs are reversed to read LTR."""
import sys, re, json, unicodedata, pdfplumber

LAT = re.compile(r'[0-9A-Za-z:()\t\xa0\.,\-]')

def is_latin_char(c):
    t = c['text']
    fn = c['fontname']
    if 'Hebrew' in fn:
        return False
    return True

def page_lines(path):
    pdf = pdfplumber.open(path)
    out = []
    for pno, pg in enumerate(pdf.pages):
        chars = [c for c in pg.chars]
        # baseline clustering
        chars.sort(key=lambda c: (-c['matrix'][5], -c['x0']))
        rows = []
        for c in chars:
            b = c['matrix'][5]
            if rows and abs(rows[-1]['b'] - b) <= 2.5:
                rows[-1]['c'].append(c)
            else:
                rows.append({'b': b, 'c': [c]})
        for r in rows:
            cs = sorted(r['c'], key=lambda c: -(c['x0'] + c['x1']) / 2)
            runs = []
            for c in cs:
                lat = is_latin_char(c)
                if runs and runs[-1][0] == lat:
                    runs[-1][1].append(c)
                else:
                    runs.append([lat, [c]])
            seq = []
            for lat, rc in runs:
                if lat:
                    txt = ''.join(c['text'] for c in reversed(rc))
                else:
                    txt = ''.join(c['text'] for c in rc)
                seq.append(('L' if lat else 'H', txt, round(rc[0]['x1'], 1), round(rc[-1]['x0'], 1)))
            out.append({'page': pno, 'baseline': round(r['b'], 1), 'runs': seq})
    return out

if __name__ == '__main__':
    for l in page_lines(sys.argv[1]):
        print(l['baseline'], ' | '.join('%s:%s' % (k, t) for k, t, a, b in l['runs']))
