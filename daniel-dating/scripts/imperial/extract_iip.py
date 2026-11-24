"""Extract Aramaic IIP (EpiDoc) inscriptions for given site prefixes.
usage: extract_iip.py OUT_tokens.tsv OUT_docs.tsv FILE..."""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xml.etree.ElementTree as ET
from extract_eleph import walk, tokens_from_items, Out, NS, ln

def main():
    ft = open(sys.argv[1], "w", encoding="utf-8"); fd = open(sys.argv[2], "w", encoding="utf-8")
    ft.write("doc\tside\tline\tidx\tform\tstatus\traw\n")
    fd.write("doc\ttitle\tmainLang\tnotBefore\tnotAfter\ttm\tn_tokens\tn_attested\n")
    for path in sys.argv[3:]:
        root = ET.parse(path).getroot()
        tl = root.find(f".//{NS}textLang")
        if tl is None or tl.get("mainLang") != "arc":
            continue
        doc = os.path.basename(path)[:-4]
        nb = na = ""
        for d in root.iter(NS + "date"):
            if d.get("notBefore") or d.get("notAfter"):
                nb, na = d.get("notBefore", ""), d.get("notAfter", ""); break
        out = Out()
        found = False
        for div in root.iter(NS + "div"):
            if div.get("type") == "edition" and div.get("subtype") == "transcription":
                found = True
                # line counter: IIP <lb/> often lacks n; number lines ourselves
                n = 1
                out.mark("LB", (str(n), None))
                for p in div:
                    if p.text: out.text(p.text, False)
                    for k in p:
                        if ln(k.tag) == "lb" and not k.get("n"):
                            n += 1; out.mark("LB", (str(n), k.get("break")))
                        else:
                            walk(k, False, out)
                        if k.tail: out.text(k.tail, False)
        if not found:
            continue
        rows = tokens_from_items(out.items, doc)
        for i, r in enumerate(rows):
            ft.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{i}\t{r[3]}\t{r[4]}\t{r[5]}\n")
        fd.write(f"{doc}\t\tarc\t{nb}\t{na}\t\t{len(rows)}\t{sum(1 for r in rows if r[4]=='A')}\n")

main()
