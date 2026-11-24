import csv, json, collections, re
rows = {}
def load(name):
    return list(csv.DictReader(open('out/audit/' + name, encoding='utf-8'), delimiter='\t'))
A = {
 '1cs pronoun': load('audit_1cs_pronoun.tsv'),
 "'kingdom'": load('audit_kingdom.tsv'),
 '1cs wayyiqtol': load('audit_1cs_wayyiqtol.tsv'),
 'object pronoun': load('audit_object_pronoun.tsv'),
 'verbsuf': load('audit_verbal_object_suffix_hw_ny.tsv'),
 'relative': load('audit_relative.tsv'),
 "'arise/stand'": load('audit_arise_stand.tsv'),
 'paragogic nun (yiqtol 2/3mp)': load('audit_paragogic_nun_yiqtol_2_3mp.tsv'),
}
wc = json.load(open('out/wordcounts.json'))
CORP = [('A', 'MS A'), ('B', 'MS B'), ('C', 'MS C'), ('D', 'MS D'), ('E', 'MS E'), ('F', 'MS F'), ('M', 'Mas1h (Masada)'), ('2Q18', '2Q18'), ('11QPsa', '11QPsa (Sir 51:13-20,30)'),
        ('marginalia', 'Genizah marginal readings (Bmg/Amg/Dmg/Emg) + Mas1h interlinear (not in totals)'), ('DEDUP', 'deduplicated total (one witness per verse: B>A>Mas>C>D>E>F>11QPsa>2Q18)')]
def sel(rs, corpus, decs):
    out = []
    for r in rs:
        if r['decision'] not in decs or r['countable'] != 'True': continue
        if corpus == 'DEDUP':
            if r['in_dedup'] == 'True': out.append(r)
        elif r['corpus'] == corpus: out.append(r)
    return out
def ex(rs, k=6, show_ms=False):
    s = ['%s %s%s' % (r['verse'], r['form'], ' (%s)' % r['witness'] if show_ms or r['witness'] != r['corpus'] else '') for r in rs[:k]]
    return '; '.join(s) + (' ...' if len(rs) > k else '')
out = []
for var in ['1cs pronoun', "'kingdom'", '1cs wayyiqtol', 'object pronoun', 'relative', "'arise/stand'", 'paragogic nun (yiqtol 2/3mp)']:
    for key, label in CORP:
        nwords = wc['words_dedup'] if key == 'DEDUP' else wc['words'].get(key, 0)
        sm = key == 'DEDUP'
        if var == 'object pronoun':
            L = sel(A['object pronoun'], key, {'object', 'object?'})
            E = sel(A['verbsuf'], key, {'finite verb + suffix'})
            rate = 1000.0 * len(L) / nwords if nwords else 0
            note = ('n_later = object marker את/אות+suffix = %d (%.2f per 1,000 words; %d countable words)' % (len(L), rate, nwords))
            if L: note += ': ' + ex(L, 8, sm)
            note += ' | n_earlier = PARTIAL count: finite verbs (incl. imperatives) with -הו or -ני object suffixes only (other suffixes not separable from nouns without a parse) = %d' % len(E)
            if E: note += ': ' + ex(E, 4, sm)
            pw = sel(A['object pronoun'], key, {'prep "with"'})
            if pw: note += ' | excluded as preposition "with": ' + ex(pw, 5, sm)
            out.append([var, label, len(E), len(L), note]); continue
        E = sel(A[var], key, {'earlier'}); L = sel(A[var], key, {'later'})
        note = 'words=%d. ' % nwords
        if var == '1cs pronoun':
            note += 'earlier=אנכי; later=אני. ' + ('earlier: ' + ex(E, 6, sm) + '. ' if E else '') + ('later: ' + ex(L, 6, sm) if L else '')
        elif var == "'kingdom'":
            note += 'earlier=ממלכה/ממלכות family; later=מלכות family. ' + ('earlier: ' + ex(E, 6, sm) + '. ' if E else '') + ('later: ' + ex(L, 6, sm) if L else '')
        elif var == '1cs wayyiqtol':
            amb = sel(A[var], key, {'ambiguous'}); iii = sel(A[var], key, {'III-he'})
            note += 'earlier=short (no -h); later=long ואקטלה. ' + ('earlier: ' + ex(E, 6, sm) + '. ' if E else '') + ('later: ' + ex(L, 6, sm) + '. ' if L else '')
            if amb: note += 'ambiguous, not counted: ' + ex(amb, 6, sm) + '. '
            if iii: note += 'III-he (uninformative): ' + ex(iii, 6, sm) + '.'
        elif var == 'relative':
            bare = [r for r in E if r['note'] == 'bare']
            note += 'earlier=אשר (all tokens; bare/ו-אשר=%d, compounds כאשר/באשר etc.=%d); later=še- (incl. כש-, complementizer, šel-type). ' % (len(bare), len(E) - len(bare))
            if L: note += 'še-: ' + ex(L, 12, sm) + '. '
            if E: note += 'אשר e.g.: ' + ex(E, 4, sm)
            if key in ('B', 'DEDUP') and any(r['verse'] == '51:30' for r in L): note += ' | NB 51:30 שנקרא is in the scribal subscription'
        elif var == "'arise/stand'":
            note += 'earlier=קום verb forms (all stems); later=עמד verb forms (all stems); nouns (מקום, קומת, עמוד pillar, מעמד) excluded. ' + ('קום: ' + ex(E, 8, sm) + '. ' if E else '') + ('עמד: ' + ex(L, 8, sm) if L else '')
        elif var == 'paragogic nun (yiqtol 2/3mp)':
            vol = sel(A[var], key, {'volitive (not counted)'}); wy = sel(A[var], key, {'wayyiqtol (not counted)'})
            note += 'earlier=yiqtol 2/3mp in -ו (indicative/modal, no object suffix); later=-ון. ' + ('later: ' + ex(L, 6, sm) + '. ' if L else '') + ('earlier e.g.: ' + ex(E, 5, sm) + '. ' if E else '')
            if vol: note += 'jussive/volitive not counted: %d. ' % len(vol)
            if wy: note += 'wayyiqtol 3mp not counted: %d.' % len(wy)
        out.append([var, label, len(E), len(L), note.strip()])
with open('bensira_variables.csv', 'w', encoding='utf-8', newline='') as fh:
    cw = csv.writer(fh)
    cw.writerow(['variable', 'corpus', 'n_earlier', 'n_later', 'notes'])
    cw.writerows(out)
with open('bensira_wordcounts.csv', 'w', encoding='utf-8', newline='') as fh:
    cw = csv.writer(fh)
    cw.writerow(['corpus', 'countable_words', 'notes'])
    for key, label in CORP:
        n = wc['words_dedup'] if key == 'DEDUP' else wc['words'].get(key, 0)
        cw.writerow([label, n, ''])
for r in out: print(r[0], '|', r[1][:20], '|', r[2], r[3])
