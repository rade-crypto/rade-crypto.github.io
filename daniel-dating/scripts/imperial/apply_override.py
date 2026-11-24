import csv, sys, os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ov = {}
for row in csv.reader(open(os.path.join(base, 'curation/eleph_dedupe_override.tsv'), encoding='utf-8'), delimiter='\t'):
    if row and not row[0].startswith('#'): ov[row[0]] = row[1]
p = os.path.join(base, 'corpus/eleph_keep.tsv')
lines = open(p, encoding='utf-8').read().splitlines()
out = [lines[0]]
for l in lines[1:]:
    f = l.split('\t')
    if f[0] in ov: f[1] = ov[f[0]]
    elif f[1] == '0': print('UNREVIEWED auto-drop', l[:150])
    out.append('\t'.join(f))
open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(sum(1 for l in out[1:] if l.split('\t')[1] == '0'), 'dropped')
