"""Write results/imperial/report_snippets.json: the Aramaic comparison table and text fragments for the report."""
import os, json, html
import pandas as pd
HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "results")
df = pd.read_csv(os.path.join(RES, "aramaic_timeline.csv"))
cols = [("Persian-era papyri", "Persian-era papyri<br>5th c. BCE"), ("Ezra", "Ezra"), ("Daniel (Masoretic)", "Daniel<br>Masoretic"),
        ("Daniel (Qumran copies)", "Daniel<br>Qumran copies"), ("Qumran Aramaic", "Qumran Aramaic<br>3rd–1st c. BCE"),
        ("Targums (Onkelos and Jonathan)", "Targums<br>2nd–3rd c. CE")]
lab = {"3mp suffix": "'their': -hm / -hwn", "2mp suffix": "'your' (pl.): -km / -kwn", "3mp pronoun": "'they': hmw(n) / ʾnwn",
       "plural demonstrative": "'these': ʾlh, ʾlk / ʾlyn", "causative prefix": "causative: h- / ʾ- (perfect-type forms)",
       "relative particle": "spelling 'which': zy / dy", "'this'": "spelling 'this': znh / dnh", "'earth'": "spelling 'earth': ʾrq / ʾrʿ",
       "reflexive prefix": "reflexive: ht- / ʾt- (not a time marker)"}
rows = []
for f in lab:
    cells = []
    for c, _ in cols:
        r = df[(df.feature == f) & (df.corpus == c)]
        if len(r) and (r.iloc[0].n_old + r.iloc[0].n_new) > 0:
            r = r.iloc[0]; n = r.n_old + r.n_new
            cells.append(f'<td class="num">{r.n_old} / {r.n_new}<br><small>{r.n_new/n:.0%}</small></td>')
        else:
            cells.append('<td class="num">–</td>')
    rows.append(f'<tr><td>{html.escape(lab[f])}</td>{"".join(cells)}</tr>')
head = "".join(f'<th class="num">{h}</th>' for _, h in cols)
table = ('<div class="tbl"><table><thead><tr><th>Feature (older / later form)</th>' + head + '</tr></thead><tbody>' + "".join(rows) +
         '</tbody></table></div><p class="caption">Counts of older / later forms, with the share of the later form. Papyri: Elephantine (Berlin ERC database, 799 documents, '
         '19,903 fully legible words) and ten Arshama letters (1,040 words); only fully legible words counted. Targums: Onkelos (Pentateuch, 82,706 words) and Jonathan '
         '(Joshua–Kings, Isaiah, 94,519 words) from Sefaria. Every hit is listed with its reference in the project files. Mt Gerizim inscriptions (3rd–2nd c. BCE): '
         'zy 32 / dy 9, znh 2 / dnh 5, causative h- 24 / ʾ- 0.</p>')
snip = {
 "imp_fig": '<div class="fig"><b>0 of 268</b><span>later grammatical forms ("their," "your," "they," "these") in the 5th-century Elephantine and Arshama papyri. Daniel: 53 of 66</span></div>',
 "imp_corpus": "about 21,000 fully legible words of dated Persian-era Aramaic: 799 Elephantine papyri and ostraca (Berlin ERC database, 5th century BCE) and ten Arshama letters, plus 4th-century ostraca from Idumea, 3rd–2nd-century inscriptions from Mt Gerizim, and about 177,000 words of the Targums (2nd–3rd centuries CE);",
 "imp_short": "the Persian-era papyri: 799 Elephantine documents (5th century BCE) and ten Arshama letters, about 21,000 fully legible words;",
 "imp_legend": '<span><i class="lg" style="background:var(--s-blue);border-radius:2px"></i>Persian-era papyri (5th c.)</span>',
 "imp_table": table,
 "imp_para": "",
 "imp_limit": "The Persian-era Aramaic is mostly letters, contracts and accounts from one Egyptian garrison. The Wadi Daliyeh, Bactrian and Persepolis Aramaic texts are not openly available, and the Comprehensive Aramaic Lexicon asks not to be scraped (it offers data dumps on request).",
}
json.dump(snip, open(os.path.join(RES, "imperial", "report_snippets.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
