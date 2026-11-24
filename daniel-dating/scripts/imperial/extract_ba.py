"""Extract consonantal (ketiv) Biblical Aramaic tokens from OSHB morphhb XML.
usage: extract_ba.py OUT_tokens.tsv FILE..."""
import sys, re, unicodedata, os
import xml.etree.ElementTree as ET
NS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"
FINALS = str.maketrans("ךםןףץ", "כמנפצ")
def cons(s):
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.replace("/", "").replace("־", " ")
    return re.sub(r"[^א-ת ]", "", s)
out = open(sys.argv[1], "w", encoding="utf-8")
out.write("doc\tside\tline\tidx\tform\tstatus\traw\n")
for path in sys.argv[2:]:
    root = ET.parse(path).getroot()
    book = os.path.basename(path)[:-4]
    i = 0
    for v in root.iter(NS + "verse"):
        ref = v.get("osisID").split(".")
        for w in v:
            if w.tag != NS + "w":
                continue  # skip notes (qere rdg live inside <note>)
            if not (w.get("morph") or "").startswith("A"):
                continue
            raw = "".join(w.itertext())
            lem = (w.get("lemma") or "").replace(" ", "")
            mor = w.get("morph") or ""
            for part in cons(raw).split():
                out.write(f"{book}\t{ref[1]}\t{ref[2]}\t{i}\t{part.translate(FINALS)}\tA\t{part}|{lem}|{mor}\n"); i += 1
