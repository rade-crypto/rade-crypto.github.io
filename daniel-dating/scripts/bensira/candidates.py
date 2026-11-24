import json, re, collections, sys
W = json.load(open('out/corpus.json', encoding='utf-8'))
def ctx(i, n=4):
    w = W[i]
    out = []
    for j in range(max(0, i - n), min(len(W), i + n + 1)):
        x = W[j]
        if x['witness'] != w['witness'] or x['file'] != w['file']: continue
        f = x['raw'] if x['countable'] else '{%s}' % x['raw']
        out.append('<<%s>>' % f if j == i else f)
    return ' '.join(out)
PFX = '(?:ו|וכ|ול|וב|ומ|וה|ה|ב|כ|ל|מ|ש|וש|כש|מש|לכ)?'
pats = {
 'pron': r'^ו?(אנכי|אנוכי|אני)$',
 'kingdom': r'ממלכ|^' + PFX + r'מלכו?ת',
 'wayy': r'^וא[א-ת]{2,}$',
 'obj': r'^ו?(את|אות)(ו|ם|י|ך|נו|ה|כם|כן|הם|ן|ני|הו)$',
 'asher': r'^' + PFX + r'אשר$',
 'qum': r'^' + PFX + r'(ק[ו]?מ|[יתאנ]ק[ו]?מ|הק[י]?מ|[יתאנ]ק[י]?מ|מק[י]?מ|תקומ|קמ|קומ|יקים|יקום)',
 'amad': r'עמ[ו]?ד|עומד|עמיד',
 'parag': r'^(?:ו|ש|כי)?[ית][א-ת]{2,}ון$',
}
which = sys.argv[1]
rx = re.compile(pats[which])
n = 0
for i, w in enumerate(W):
    if w['corpus'] not in ('A','B','C','D','E','F','M','11QPsa','2Q18','marginalia'): continue
    if rx.search(w['cons']):
        n += 1
        print('%d\t%s\t%s\t%s\t%s\t%s\t%s' % (i, w['witness'], w['verse'], w['cons'], 'C' if w['countable'] else 'x', 'D' if w['dedup'] else '-', ctx(i)))
print('N=', n, file=sys.stderr)
