import sys, pdfplumber
pdf = pdfplumber.open(sys.argv[1])
for pg in pdf.pages:
    chars = pg.chars
    # group by line (top rounded)
    lines = {}
    for c in chars:
        key = round(c['top']/3)
        lines.setdefault(key, []).append(c)
    for k in sorted(lines)[:int(sys.argv[2]) if len(sys.argv)>2 else 999]:
        cs = sorted(lines[k], key=lambda c: -c['x0'])
        s = ''
        prev = None
        for c in cs:
            if prev is not None and prev['x0'] - c['x1'] > 1.5:
                s += ' '
            s += c['text']
            prev = c
        print(k, repr(s))
