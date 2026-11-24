"""Classify candidates for the 7 variables (rules + manual decisions) and write CSV + audit files."""
import json, re, collections, csv, os
W = json.load(open('out/corpus.json', encoding='utf-8'))
OUT = 'out/audit'; os.makedirs(OUT, exist_ok=True)
FIN = str.maketrans('ךםןףץ', 'כמנפצ')
CORPORA = ['B', 'A', 'M', 'C', 'D', 'E', 'F', '11QPsa', '2Q18', 'marginalia']
def ctx(i, n=5):
    w = W[i]; out = []
    for j in range(max(0, i - n), min(len(W), i + n + 1)):
        x = W[j]
        if x['witness'] != w['witness'] or x['file'] != w['file']: continue
        out.append('<<%s>>' % x['raw'] if j == i else (x['raw'] if x['countable'] else '{%s}' % x['raw']))
    return ' '.join(out)

audit = collections.defaultdict(list)   # var -> rows
def add(var, i, decision, note=''):
    w = W[i]
    audit[var].append({'idx': i, 'witness': w['witness'], 'corpus': w['corpus'], 'verse': w['verse'], 'file': w['file'], 'line': w['line'],
                       'form': w['raw'], 'cons': w['cons'], 'decision': decision, 'note': note,
                       'countable': w['countable'], 'dedup': w['dedup'], 'context': ctx(i)})

# ---------- 1. 1cs pronoun ----------
for i, w in enumerate(W):
    c = w['cons']
    if re.fullmatch(r'ו?(אנכי|אנוכי)', c): add('1cs pronoun', i, 'earlier')
    elif re.fullmatch(r'ו?אני', c): add('1cs pronoun', i, 'later')

# ---------- 2. kingdom ----------
for i, w in enumerate(W):
    c = w['cons']
    if 'ממלכ' in c: add("'kingdom'", i, 'earlier')
    elif re.fullmatch(r'(ו|ה|ב|ל|כ|מ|וב|ול|ומ|וה|ש)?מלכו(ת|תו|תה|תי|תך|תם|תן|תנו|יות)', c): add("'kingdom'", i, 'later')
    elif re.fullmatch(r'(ו|ה|ב|ל|כ|מ|וב|ול|ומ)?מלכת', c): add("'kingdom'", i, 'excluded', 'defective מלכת: queen/kingdom ambiguous')

# ---------- 3. 1cs wayyiqtol (manual decisions on all ו+א candidates) ----------
WAYY = {  # (witness, verse, cons) -> (decision, note)
 ('B', '51:8', 'ואזכרה'): ('later', 'wayyiqtol long; past narrative "and I remembered" (G aorist)'),
 ('B', '51:9', 'וארים'): ('earlier', 'wayyiqtol without -h (hiph. רום, unapocopated spelling); past (G aorist)'),
 ('B', '51:10', 'וארומם'): ('earlier', 'wayyiqtol without -h (polel רום); past (G aorist)'),
 ('B', '51:14', 'ואתפלל'): ('earlier', 'wayyiqtol short; past "I prayed in my youth"'),
 ('11QPsa', '51:18', 'ואשחקה'): ('later', 'wayyiqtol long after qatal זמותי; past narrative (Qumran-type)'),
 ('B', '51:12', 'ואהללה'): ('ambiguous', 'after qatal הודיתי: wayyiqtol-long (past) or cohortative; G has future -> not counted'),
 ('B', '51:12', 'ואברכה'): ('ambiguous', 'as ואהללה; not counted'),
 ('B', '51:19', 'ואביט'): ('ambiguous', 'after yiqtol אחרד/אחדר; past or iterative/future unclear; would be short type; not counted'),
 ('B', '51:7', 'ואפנה'): ('III-he', 'wayyiqtol of פנה: uninformative'),
 ('B', '51:7', 'ואצפה'): ('III-he', 'wayyiqtol of צפה: uninformative'),
 ('B', '51:11', 'ואזכרך'): ('not wayyiqtol', 'w+yiqtol with object suffix in vow series (G future)'),
 ('B', '42:15', 'ואספרה'): ('not wayyiqtol', 'cohortative "and I will recount" (G future)'),
 ('M', '42:15', 'ואשננה'): ('not wayyiqtol', 'cohortative "and I will repeat/recount"'),
 ('M-interlinear', '42:15', 'ואשננה'): ('not wayyiqtol', 'interlinear repetition; cohortative'),
 ('A', '4:19', 'ואסגירנו'): ('not wayyiqtol', 'w+yiqtol (future) with suffix'),
 ('B', '45:16', 'ואזכרה'): ('not verb', 'noun אזכרה "memorial portion"'),
 ('A', '5:6', 'ואמרת'): ('not 1cs', 'weqatal 2ms'), ('C', '5:6', 'ואמרת'): ('not 1cs', 'weqatal 2ms'),
 ('A', '8:2', 'ואבדת'): ('not 1cs', 'weqatal 2ms'), ('D', '8:2', 'ואבדת'): ('not 1cs', 'weqatal 2ms'),
 ('E', '33:32', 'ואבד'): ('not 1cs', 'qatal 3ms'),
 ('B', '31:16', 'ואכול'): ('not 1cs', 'imperative "and eat"'),
 ('B', '36:7', 'ואמץ'): ('not 1cs', 'imperative/noun'),
}
VERBLIKE = set(k[2] for k in WAYY)
for i, w in enumerate(W):
    c = w['cons']
    if re.fullmatch(r'וא[א-ת]{2,}', c):
        k = (w['witness'], w['verse'], c)
        if k in WAYY:
            add('1cs wayyiqtol', i, *WAYY[k])
        else:
            add('1cs wayyiqtol', i, 'not verb', 'noun/particle/other (screened)')

# ---------- 4. object pronoun את+suffix ----------
OBJ = {
 ('A', '3:13', 'אותו'): 'object', ('A', '7:23', 'אותם'): 'object', ('C', '7:23', 'אותם'): 'object', ('D', '7:23', 'אותם'): 'object',
 ('B', '38:1', 'אתו'): 'object', ('Bmg', '38:1', 'אותו'): 'object', ('B', '39:31', 'אתם'): 'object', ('B', '45:25', 'אתכם'): 'object',
 ('B', '51:26', 'אתה'): 'object', ('E', '33:11', 'אותם'): 'object', ('F', '32:7', 'אותך'): 'object',
 ('Bmg', '32:7', 'אתך'): 'object?',
 ('A', '5:12', 'אתך'): 'prep "with"', ('C', '5:12', 'אתך'): 'prep "with"', ('A', '16:2', 'אתם'): 'prep "with"', ('B', '16:2', 'אתם'): 'prep "with"',
 ('B', '31:20', 'אתו'): 'prep "with"',
}
for i, w in enumerate(W):
    c = w['cons']
    if re.fullmatch(r'ו?(את|אות)(ו|ם|י|ך|נו|ה|כם|כן|הם|ן|ני|הו)', c):
        k = (w['witness'], w['verse'], c)
        d = OBJ.get(k)
        if d is None:
            d = 'pronoun "you"' if c.endswith('אתה') else ('verb "I will give"' if c == 'אתן' else 'unclassified')
        add('object pronoun', i, d)
# verbal object suffixes: only -הו and -ני forms classifiable from consonants
V_SUF = set('''הושעתני התקילני והאכילתהו והשיבהו ויאזרהו ויאמצהו ויאשרוהו ויאשריהו ויגישהו ויחזקהו ויכהו ויכוננהו ויכנהו ויכנוהו
וילבישהו וימלטני וימשחהו וימשילהו וינעריהו ויסרתיהו ויענהו ויעשהו ויפארהו ויפדני ויצוהו ויציבהו ויקיפהו ויקיפוהו וירממהו וישימהו
וישיתהו וישמיעהו וישעוהו וישרתהו וישתיהו ויתנהו ונטותיהו וקדמתהו ורוממתהו ושחריהו חשבהו יאשרוהו יהדפוהו יזכרני יעבדוהו עזרתני ענוהו
פציתני צפתהו קנהו תאשרהו תושיבהו תזכרהו תחרפהו תמשילהו תעזבהו תעמידהו תקמיעהו תקצרהו תראני תרפני תוגהו'''.split())
NONV_NI = set('בני לפני ולפני עני מפני בעיני ופני לבני אבני אני מבני עשתוני לעני העוני עיני אזני ותחנוני מתני פני מני וזמני ושני באבני סרני ובעיני כבני לשני בסיני זני בשני בבני אדני ובלשוני לעיני תחנוני אוזני בפני מלפני'.split())
for i, w in enumerate(W):
    c = w['cons']
    if c.endswith('הו') or (c.endswith('ני') and c not in NONV_NI):
        if c in V_SUF: add('verbal object suffix (-hw/-ny)', i, 'finite verb + suffix')
        elif c in ('עושהו', 'וקונהו', 'ומשחרהו', 'רואיהו') or (c == 'עשהו' and w['witness'] == 'M'): add('verbal object suffix (-hw/-ny)', i, 'participle (not finite)')
        else: add('verbal object suffix (-hw/-ny)', i, 'not verb', 'noun/name/preposition/III-he plural/fragment')

# ---------- 5. relative ----------
SHE = {  # confirmed še- (witness, verse, cons) -> note
 ('A', '3:22', 'שהורשית'): 'relative', ('A', '13:5', 'שלך'): 'še+l- "what is yours" (šel-type)', ('A', '14:16', 'שיפה'): 'relative',
 ('A', '14:18', 'שזה'): 'relative', ('A', '16:3', 'שהיו'): 'relative', ('A', '16:15', 'שמעשיו'): 'complementizer "that"',
 ('B', '15:17', 'שיחפץ'): 'relative (A: אשר יחפץ)', ('B', '16:3', 'שיהיו'): 'relative', ('B', '30:12', 'שעודנו'): 'relative/temporal',
 ('B', '30:12', 'כשהוא'): 'k+še temporal "when"', ('B', '30:19', 'שיש'): 'relative', ('B', '31:10', 'שנדבק'): 'relative',
 ('B', '31:15', 'ששנאת'): 'relative', ('B', '31:16', 'שרעך'): 'complementizer "that"', ('B', '31:16', 'ששם'): 'relative',
 ('B', '31:27', 'שהוא'): 'relative', ('B', '37:3', 'שאמר'): 'relative', ('B', '51:30', 'שנקרא'): 'relative (subscription)',
 ('C', '25:8', 'שלא'): 'relative', ('E', '33:20', 'שלך'): 'še+l- "what is yours" (šel-type)', ('E', '33:26', 'שלא'): 'relative/final',
 ('E', '33:28', 'שלא'): 'relative/final', ('M', '44:9', 'שאין'): 'relative (B: אשר אין)',
}
for i, w in enumerate(W):
    c = w['cons']
    m = re.fullmatch(r'(ו|ב|כ|ל|מ|וכ|וב|ול|ומ|עד)?אשר', c)
    if m:
        add('relative', i, 'earlier', 'compound %s-' % m.group(1) if m.group(1) and m.group(1) not in ('ו',) else 'bare')
    elif (w['witness'], w['verse'], c) in SHE:
        add('relative', i, 'later', SHE[(w['witness'], w['verse'], c)])
# screened-out še- candidates are listed for audit
she_screen = open('out/she_candidates_raw.tsv', encoding='utf-8').read().splitlines()

# ---------- 6. qum vs amad ----------
QUM = {'וקם': 'qal', 'והקם': 'hiphil', 'הקים': 'hiphil', 'קם': 'qal', 'המקים': 'hiphil ptc', 'ויקם': 'hiphil wayyiqtol', 'קמי': 'qal ptc (subst. "my adversaries")',
       'תקומם': 'hitpolel/polel', 'ומהתקומם': 'hitpolel inf', 'וקים': 'adj/ptc קַיָּם'}
AMAD = {'תעמוד', 'יעמוד', 'העמידה', 'יעמד', 'תעמידהו', 'ויעמד', 'עמד', 'עומד', 'יעמידו', 'עמדה', 'ועמדתי', 'ועמד'}
for i, w in enumerate(W):
    c = w['cons']
    if c in QUM:
        add("'arise/stand'", i, 'earlier', 'קום ' + QUM[c])
    elif c in ('יקום',) and w['witness'] == 'Bmg':
        add("'arise/stand'", i, 'excluded', 'Bmg 43:13 obscure; not counted')
    elif c in ('מקום', 'ומקום', 'קומת'):
        pass
    elif c in AMAD:
        add("'arise/stand'", i, 'later', 'עמד')
    elif c == 'העמיד' and w['witness'] == 'C':
        add("'arise/stand'", i, 'excluded', 'C 36:29 corrupt line (B/D: ועמוד משען "pillar"); not counted')
    elif c in ('ועמוד', 'מעמד', 'עמודים'):
        add("'arise/stand'", i, 'excluded', 'noun (pillar/standing place)')

# ---------- 7. paragogic nun ----------
PARAG = {('B', '30:19', 'יאכלון'): 'later', ('B', '45:21', 'יאכלון'): 'later', ('B', '51:24', 'תחסרון'): 'later'}
for i, w in enumerate(W):
    c = w['cons']
    if re.fullmatch(r'(ו|ש|כי|וכ|ול|ל|ה)?[יתנ][א-ת]{2,}ון', c):
        k = (w['witness'], w['verse'], c)
        if k in PARAG: add('paragogic nun (yiqtol 2/3mp)', i, 'later', 'yiqtol 3mp/2mp + -ûn')
        else: add('paragogic nun (yiqtol 2/3mp)', i, 'not 2/3mp yiqtol', 'noun/name/3ms of hollow-nun root/ptc')
EARLIER_Y = {  # (witness, verse, cons)
 ('A','3:27','ירבו'),('A','3:30','יכבו'),('A','4:12','יפיקו'),('A','4:13','ימצאו'),('A','4:13','ויחנו'),('A','5:8','יועילו'),('A','6:6','יהיו'),
 ('A','11:30','ירבו'),('A','13:23','יגיעו'),('A','13:23','יאמרו'),('A','14:17','יגועו'),('A','14:19','ירקבו'),('A','15:19','יראו'),('A','16:16','יראו'),
 ('A','16:19','ירעשו'),('A','16:23','יבינו'),
 ('B','11:5','יעטו'),('B','16:3','שיהיו'),('B','32:16','יבינו'),('B','32:16','יוציאו'),('B','37:31','יגועו'),('B','39:24','יישרו'),('B','39:24','יסתוללו'),
 ('B','39:27','ייטיבו'),('B','39:28','יעתיקו'),('B','39:30','יפקדו'),('B','39:31','ישישו'),('B','39:31','ימרו'),('B','40:14','יגילו'),('B','40:18','ימתקו'),
 ('B','40:19','יעמידו'),('B','40:19','יפריחו'),('B','40:20','יעליצו'),('B','40:21','יעריבו'),('B','40:22','יחמידו'),('B','40:23','ינהגו'),('B','40:26','יגילו'),
 ('B','41:9','תולידו'),('B','41:9','תכשלו'),('B','41:9','תמותו'),('B','43:24','יספרו'),('B','43:30','תוכלו'),('B','43:30','תחליפו'),('B','50:16','יריעו'),
 ('B','51:21','יהמו'),('B','51:28','תקנו'),('B','51:29','תבושו'),
 ('C','6:6','יהיו'),('C','19:2','יפחיזו'),('E','32:16','יוציאו'),('F','32:16','יבינו'),('F','32:16','יוציאו'),
 ('M','39:28','תיקו'),('M','39:28','יניחו'),('M','40:18','ימתקו'),('M','41:9','תולידו'),('M','41:9','תמותו'),('11QPsa','51:15','ישמחו'),
 ('Bmg','37:18','יפריחו'),('Bmg','37:31','יגועו'),('Bmg','39:16','יספיקו'),('Bmg','41:9','תפרו'),
}
VOLITIVE = {('B','36:3','ויראו'),('B','36:5','וידעו'),('B','36:13','ויתנחלו'),('B','36:21','יאמינו'),('B','36:22','וידעו'),('B','43:30','תלאו'),('Bmg','36:22','ויראו'),('Bmg','43:30','תלאו')}
WAYY3 = {('B','44:9','וישבתו'),('B','45:18','ויחרו'),('B','45:18','ויקנאו'),('B','48:15','ויפצו'),('B','48:19','ויחילו'),('B','48:20','ויפרשו'),('B','49:4','ויעזבו'),
         ('B','49:6','ויציתו'),('B','49:6','וישמו'),('B','49:12','וירימו'),('B','50:16','ויריעו'),('B','50:16','וישמיעו'),('B','50:17','ויפלו'),('B','50:19','וירנו'),('B','50:21','וישנו')}
NOUNS = set('ידו יחדו ידיו יצרו תקותו ותורתו ותהלתו ימיו יומו יושביו יצועיו יצוריו יתריו תוחלתו תוכחתו תומכו תפארתו שיחו שימו'.split())
for i, w in enumerate(W):
    c = w['cons']
    if w['countable'] and re.fullmatch(r'(ו|ש|כי|ה|ול)?[ית][א-ת]+ו', c) and not c.endswith('הו'):
        k = (w['witness'], w['verse'], c)
        if k in EARLIER_Y: add('paragogic nun (yiqtol 2/3mp)', i, 'earlier', 'yiqtol 3mp/2mp in -û' + (' (fragment יע[ ]תיקו)' if c == 'תיקו' else ''))
        elif k in VOLITIVE: add('paragogic nun (yiqtol 2/3mp)', i, 'volitive (not counted)', 'jussive/neg. volitive 2/3mp')
        elif k in WAYY3: add('paragogic nun (yiqtol 2/3mp)', i, 'wayyiqtol (not counted)', 'wayyiqtol 3mp')
        elif c in NOUNS: add('paragogic nun (yiqtol 2/3mp)', i, 'not verb', 'noun+3ms suffix / imperative')
        else: add('paragogic nun (yiqtol 2/3mp)', i, 'not counted', 'yiqtol+object suffix, qatal 3cp of I-y root, imperative or unclear')

# ---------- tallies ----------
words = collections.Counter(); words_dedup = 0
for w in W:
    if w['countable']: words[w['corpus']] += 1
    if w['dedup']: words_dedup += 1
def tally(var, dec):
    t = collections.Counter(); td = 0
    for r in audit[var]:
        if r['decision'] == dec and r['countable']:
            t[r['corpus']] += 1
            if r['dedup']: td += 1
    return t, td
rows = []
VARS = ['1cs pronoun', "'kingdom'", '1cs wayyiqtol', 'object pronoun', 'relative', "'arise/stand'", 'paragogic nun (yiqtol 2/3mp)']
summary = {}
for var in VARS:
    if var == 'object pronoun':
        e, ed = tally('verbal object suffix (-hw/-ny)', 'finite verb + suffix')
        l, ld = tally('object pronoun', 'object'); l2, ld2 = tally('object pronoun', 'object?')
        l.update(l2); ld += ld2
    else:
        e, ed = tally(var, 'earlier'); l, ld = tally(var, 'later')
    summary[var] = (e, ed, l, ld)
json.dump({'words': dict(words), 'words_dedup': words_dedup}, open('out/wordcounts.json', 'w'), indent=1)
for var, rs in audit.items():
    fn = os.path.join(OUT, 'audit_' + re.sub(r'[^A-Za-z0-9]+', '_', var).strip('_') + '.tsv')
    with open(fn, 'w', encoding='utf-8', newline='') as fh:
        cw = csv.writer(fh, delimiter='\t')
        cw.writerow(['idx', 'witness', 'corpus', 'verse', 'source_file', 'line', 'form', 'consonantal', 'decision', 'note', 'countable', 'in_dedup', 'context'])
        for r in rs:
            cw.writerow([r['idx'], r['witness'], r['corpus'], r['verse'], r['file'], r['line'], r['form'], r['cons'], r['decision'], r['note'], r['countable'], r['dedup'], r['context']])
json.dump({k: [dict(v[0]), v[1], dict(v[2]), v[3]] for k, v in summary.items()}, open('out/summary.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for var in VARS:
    e, ed, l, ld = summary[var]
    print(var, '| dedup E=%d L=%d |' % (ed, ld), ' '.join('%s:%d/%d' % (c, e[c], l[c]) for c in CORPORA if e[c] or l[c]))
print(dict(words), words_dedup)
