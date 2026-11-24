"""Build normalised token tables from Sefaria JSON downloads.
Usage: python3 -I build_corpus.py DATA_DIR OUT_TSV
Output TSV columns: corpus, ref, tok_index, vocalised_token, consonantal_token(final letters normalised)
"""
import sys, json, re, os, unicodedata

DATA, OUT = sys.argv[1], sys.argv[2]

ONK = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy"]
TJ = ["Joshua", "Judges", "I Samuel", "II Samuel", "I Kings", "II Kings", "Isaiah"]
SOURCES = []
for b in ONK:
    SOURCES.append(("Targum Onkelos", f"Onkelos {b} - he - Onkelos {b}.json", b))
for b in TJ:
    SOURCES.append(("Targum Jonathan (sample)", f"Targum Jonathan on {b} - he - Mikraot Gedolot.json", b))
SOURCES.append(("Megillat Antiochus", "Megillat Antiochus - he - the Open Siddur Project - Aramaic.json", "MegAnt"))

FINALS = str.maketrans("ךםןףץ", "כמנפצ")
WORD_SEP_MARKS = "־׀׃׆"  # maqaf, paseq, sof pasuq, nun hafukha -> space

class Cleaner:
    """Removes HTML, (...) variants/additions and [...] supplements; parentheses/brackets may span verses."""
    def __init__(self):
        self.open = None   # None, ')' or ']'
    def __call__(self, s):
        s = unicodedata.normalize("NFD", s)
        s = re.sub(r"<[^>]+>", " ", s)
        s = re.sub(r"&[a-z]+;|&#\d+;", " ", s)
        # "[ת\"א]" = alternative targum appended to the verse (TJ Isa 49:24-25): drop it and what follows
        s = re.sub(r"\[ת[\"\u05F4\u05F3']+א\].*$", " ", s, flags=re.S)
        out = []
        for ch in s:
            if self.open:
                if ch == self.open:
                    self.open = None
                continue
            if ch == "(":
                self.open = ")"; continue
            if ch == "[":
                self.open = "]"; continue
            out.append(ch)
        s = "".join(out)
        for ch in WORD_SEP_MARKS:
            s = s.replace(ch, " ")
        return s

def consonantal(tok):
    t = re.sub(r"[֑-ׇ]", "", tok)       # strip niqqud/cantillation
    t = re.sub(r"[^א-ת]", "", t)        # keep letters only
    return t.translate(FINALS)

def walk(x, path=()):
    if isinstance(x, str):
        yield path, x
    elif isinstance(x, list):
        for i, y in enumerate(x, 1):
            yield from walk(y, path + (i,))

rows = []
stats = {}
for corpus, fn, book in SOURCES:
    j = json.load(open(os.path.join(DATA, fn)))
    clean = Cleaner()
    for path, seg in walk(j["text"]):
        if not seg.strip():
            continue
        ref = f"{book} {':'.join(map(str, path))}" if book != "MegAnt" else f"Meg. Ant. {path[0]}"
        # Megillat Antiochus para 79 is a Hebrew colophon; already fully parenthesised, so removed by clean()
        s = clean(seg)
        # split on whitespace and any non-letter non-mark char
        raw_toks = re.split(r"[^א-ת֑-ׇ]+", s)
        k = 0
        for rt in raw_toks:
            c = consonantal(rt)
            if not c or c in ("ססס", "פפפ"):   # empty or parasha (setuma/petuha) markers
                continue
            rows.append((corpus, ref, k, rt, c))
            k += 1
with open(OUT, "w") as f:
    for r in rows:
        f.write("\t".join(map(str, r)) + "\n")
from collections import Counter
cnt = Counter(r[0] for r in rows)
for k, v in cnt.items():
    print(k, v)
