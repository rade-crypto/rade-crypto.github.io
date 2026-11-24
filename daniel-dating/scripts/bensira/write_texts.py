import sys, json, collections, os
words = json.load(open(sys.argv[1], encoding='utf-8'))
outdir = sys.argv[2]
by = collections.defaultdict(list)
for w in words:
    by[w['witness']].append(w)
for wit, ws in by.items():
    with open(os.path.join(outdir, 'text_%s.txt' % wit), 'w', encoding='utf-8') as fh:
        cur = None; buf = []
        for w in ws:
            key = (w['verse'], w['file'])
            if key != cur:
                if buf: fh.write('%s\t%s\t%s\n' % (cur[0], cur[1], ' '.join(buf)))
                cur = key; buf = []
            form = w['raw']
            if w['mostly_rec']: form = '{' + form + '}'
            buf.append(form)
        if buf: fh.write('%s\t%s\t%s\n' % (cur[0], cur[1], ' '.join(buf)))
print('ok')
