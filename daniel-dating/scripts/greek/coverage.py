"""Per-textgroup coverage: files, Greek word tokens, author name, assigned date.
Usage: python3 -I coverage.py OUT.csv ROOT [ROOT...]"""
import csv, glob, os, re, sys
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dates import AUTHOR
CTS = "{http://chs.harvard.edu/xmlns/cts}"
W = re.compile(r"[Ͱ-Ͽἀ-῿]+")
out = sys.argv[1]
agg = {}
for root in sys.argv[2:]:
    corpus = root.rstrip('/').split('/')[-2]
    for f in glob.glob(os.path.join(root, "*", "*", "*.xml")):
        b = os.path.basename(f)
        if "grc" not in b or b.startswith("__"):
            continue
        aid = f.split(os.sep)[-3]
        try:
            t = etree.parse(f, etree.XMLParser(recover=True, huge_tree=True))
            body = t.getroot().find(".//{http://www.tei-c.org/ns/1.0}body")
            n = len(W.findall(" ".join(body.itertext()))) if body is not None else 0
        except Exception:
            n = 0
        a = agg.setdefault(aid, {"files": 0, "tokens": 0, "corpora": set(), "name": ""})
        a["files"] += 1; a["tokens"] += n; a["corpora"].add(corpus)
        if not a["name"]:
            try:
                g = etree.parse(os.path.join(os.path.dirname(os.path.dirname(f)), "__cts__.xml")).find(".//" + CTS + "groupname")
                a["name"] = (g.text or "").strip()
            except Exception:
                pass
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["author_id", "author", "files", "greek_tokens", "corpora", "approx_year_if_assigned"])
    for k, v in sorted(agg.items()):
        w.writerow([k, v["name"], v["files"], v["tokens"], "+".join(sorted(v["corpora"])), AUTHOR.get(k, ("", ""))[0]])
print(len(agg), sum(v["files"] for v in agg.values()), sum(v["tokens"] for v in agg.values()))
