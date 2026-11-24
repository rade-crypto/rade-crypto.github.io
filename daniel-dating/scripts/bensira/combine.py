import sys, json, re
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20, 'XXI': 21}
g = json.load(open('out/genizah_words.json', encoding='utf-8'))
m = json.load(open('out/masada_words.json', encoding='utf-8'))
d = json.load(open('out/dss_words.json', encoding='utf-8'))
def gkey(w):
    p = w['file'].split('_')
    return (ROM[p[1]], 0 if p[2] == 'Recto' else 1)
for i, w in enumerate(g): w['_i'] = i
g.sort(key=lambda w: (w['ms'], gkey(w), w['_i']))
allw = []
for src in (g, m, d):
    for w in src:
        w.pop('_i', None)
        allw.append(w)
for i, w in enumerate(allw):
    w['idx'] = i
    w.pop('letters_detail', None)
json.dump(allw, open('out/all_words.json', 'w', encoding='utf-8'), ensure_ascii=False)
import collections
c = collections.Counter((w['witness'], 'excl' if w['mostly_rec'] else 'kept') for w in allw)
for k in sorted(c): print(k, c[k])
