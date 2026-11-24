import pdfplumber, collections, sys
for f in sys.argv[1:]:
    pdf = pdfplumber.open(f)
    for pg in pdf.pages:
        chars = sorted(pg.chars, key=lambda c: (-c['matrix'][5], c['x0']))
        rows = []
        for c in chars:
            b = c['matrix'][5]
            if rows and abs(rows[-1][0] - b) <= 2.5: rows[-1][1].append(c)
            else: rows.append([b, [c]])
        for b, cs in rows:
            cs.sort(key=lambda c: c['x0'])
            s = ''; prev = None; pf = None
            for c in cs:
                fn = c['fontname'].split('+')[-1]
                tag = 'S' if 'SPTib' in fn else ('L' if 'Charis' in fn else ('T' if 'Times' in fn else 'o'))
                if prev and c['x0'] - prev['x1'] > 2: s += ' '
                if tag != pf: s += '‹%s›' % tag; pf = tag
                s += c['text']; prev = c
            print(round(b), s)
