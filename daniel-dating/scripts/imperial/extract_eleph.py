"""Extract Aramaic edition text from Elephantine ERC TEI files into token TSV.
usage: extract_eleph.py OUT_tokens.tsv OUT_docs.tsv FILE...
Each token row: doc, side, line, idx, form(normalized, finals->medial), status(A=attested complete, R=contains restoration, F=fragmentary/illegible), raw"""
import sys, re, unicodedata
import xml.etree.ElementTree as ET

NS = "{http://www.tei-c.org/ns/1.0}"
FINALS = str.maketrans("ךםןףץ", "כמנפצ")
HEB = re.compile(r"[א-ת]")
SKIP = {"note", "surplus", "del", "certainty", "handShift", "space", "figure", "graphic", "foreign_note", "orig_skip"}

def ln(tag):
    return tag.split("}")[-1] if isinstance(tag, str) else ""

class Out:
    def __init__(self):
        self.items = []  # (kind, payload)
    def text(self, s, restored):
        if s:
            self.items.append(("T", s, restored))
    def mark(self, kind, val=None):
        self.items.append((kind, val, None))

def walk(el, restored, out):
    tag = ln(el.tag)
    if tag in SKIP:
        pass
    elif tag == "gap":
        out.text(" … " if el.get("reason") != "illegible" else "◦", restored)
    elif tag == "lb":
        out.mark("LB", (el.get("n"), el.get("break")))
    elif tag == "pb":
        out.mark("PB", el.get("n"))
    elif tag == "choice":
        kids = [k for k in el if ln(k.tag) not in ("note",)]
        pick = None
        for pref in ("corr", "reg", "expan"):
            for k in kids:
                if ln(k.tag) == pref:
                    pick = k; break
            if pick is not None: break
        if pick is None and kids:
            pick = kids[0]
        if pick is not None:
            walk(pick, restored, out)
            # tail of picked child must not be emitted twice; tails of choice children are whitespace
    else:
        r = restored or tag == "supplied"
        if el.text:
            out.text(el.text, r)
        for k in el:
            walk(k, r, out)
            if k.tail:
                out.text(k.tail, r)
        return
    # skipped elements: nothing; tail handled by parent

def walk_choice_safe(el, restored, out):
    walk(el, restored, out)

def edition_abs(root):
    for div in root.iter(NS + "div"):
        if div.get("type") == "edition":
            for ab in div:
                if ln(ab.tag) != "ab":
                    continue
                # skip TAD-variant blocks
                pbs = [p.get("n") or "" for p in ab.iter(NS + "pb")]
                first_pb = pbs[0] if pbs else ""
                if "variant" in first_pb.lower():
                    continue
                txt = "".join(ab.itertext())
                if re.match(r"\s*TAD\s*:", txt):
                    continue
                yield ab

def tokens_from_items(items, doc):
    """Convert item stream into tokens with line refs, applying inline Leiden conventions."""
    side, line = "", ""
    chars = []  # (char, restored, side, line)
    inline_restored = False
    angle = False
    for kind, val, r in items:
        if kind == "PB":
            side = val or side
            chars.append((" ", False, side, line))
        elif kind == "LB":
            n, brk = val
            if n: line = n
            if brk != "no":
                chars.append((" ", False, side, line))
        else:
            s = val
            # brace alternatives {a|b} -> a ; labels like {Recto Palimpsest} -> drop
            s = re.sub(r"\{([^{}|]*)\|[^{}]*\}", r"\1", s)
            s = re.sub(r"\{[^{}]*[A-Za-z][^{}]*\}", " ", s)
            s = s.replace("{", "").replace("}", "")
            s = re.sub(r"(\S)/(\S)", r"\1", s)
            s = s.replace("^", "")
            s = s.replace("...", "…").replace("..", "…")
            for ch in s:
                if ch == "[":
                    inline_restored = True; continue
                if ch == "]":
                    inline_restored = False; continue
                if ch == "<":
                    angle = True; continue
                if ch == ">":
                    angle = False; continue
                if ch in "⸢⸣⸤⸥()?!‏‎·":
                    continue
                if unicodedata.category(ch) == "Mn":
                    continue
                if ch == ".":
                    ch = "…"
                chars.append((ch, bool(r) or inline_restored or angle, side, line))
    # tokenise on whitespace
    toks = []
    cur = []
    def flush():
        if cur:
            toks.append(list(cur)); cur.clear()
    for c in chars:
        if c[0].isspace():
            flush()
        else:
            cur.append(c)
    flush()
    rows = []
    for t in toks:
        raw = "".join(c[0] for c in t)
        if not HEB.search(raw):
            continue
        letters = [c for c in t if HEB.match(c[0])]
        form = "".join(c[0] for c in letters).translate(FINALS)
        if any(c[0] in "…◦" for c in t) or re.search(r"[^א-ת…◦]", raw):
            # contains gap/illegible or foreign chars (digits/numerals inside) -> fragmentary
            status = "F" if any(c[0] in "…◦" for c in t) else ("R" if any(c[1] for c in letters) else "A")
        elif any(c[1] for c in letters):
            status = "R"
        else:
            status = "A"
        if any(c[0] in "…◦" for c in t):
            status = "F"
        side_, line_ = letters[0][2], letters[0][3]
        rows.append((doc, side_ or "", line_ or "", form, status, raw))
    return rows

def main():
    out_tok, out_doc = sys.argv[1], sys.argv[2]
    ft = open(out_tok, "w", encoding="utf-8"); fd = open(out_doc, "w", encoding="utf-8")
    ft.write("doc\tside\tline\tidx\tform\tstatus\traw\n")
    fd.write("doc\ttitle\tmainLang\tnotBefore\tnotAfter\ttm|refs\tn_tokens\tn_attested\n")
    for path in sys.argv[3:]:
        try:
            txt = open(path, encoding="utf-8", errors="replace").read()
            txt = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", txt)
            txt = re.sub(r"<\?xml[^>]*\?>", "", txt, count=1)
            root = ET.fromstring(txt)
        except ET.ParseError as e:
            # fallback: rebuild a minimal document from header bits + the edition div
            m_ed = re.search(r'<div type="edition">.*?(?=<div type="translation"|</body>)', txt, re.S)
            m_tl = re.search(r'<textLang[^>]*/>', txt)
            m_ti = re.search(r'<titleStmt>\s*<title[^>]*>.*?</title>', txt, re.S)
            ed = m_ed.group(0) if m_ed else ""
            depth = ed.count("<div") - ed.count("</div>")
            ed += "</div>" * max(depth, 0)
            mini = ('<TEI xmlns="http://www.tei-c.org/ns/1.0"><teiHeader><fileDesc>' + (m_ti.group(0) + "</titleStmt>" if m_ti else "") +
                    '</fileDesc><profileDesc><langUsage>' + (m_tl.group(0) if m_tl else "") + '</langUsage></profileDesc></teiHeader><text><body>' + ed + '</body></text></TEI>')
            try:
                root = ET.fromstring(mini)
                print("PARSE FALLBACK", path, e, file=sys.stderr)
            except ET.ParseError as e2:
                print("PARSE ERROR", path, e, e2, file=sys.stderr); continue
        doc = re.search(r"(\d{6})", path.split("/")[-1]).group(1)
        tl = root.find(f".//{NS}textLang")
        lang = tl.get("mainLang") if tl is not None else ""
        if not (lang.startswith("arc") or "Armi" in lang):
            continue
        title_el = root.find(f".//{NS}titleStmt/{NS}title")
        title = re.sub(r"\s+", " ", "".join(title_el.itertext())).strip() if title_el is not None else ""
        nb = na = ""
        for od in root.iter(NS + "origDate"):
            for d in od.iter(NS + "date"):
                if d.get("notBefore") or d.get("notAfter") or d.get("when"):
                    nb = nb or d.get("notBefore") or d.get("when") or ""
                    na = na or d.get("notAfter") or d.get("when") or ""
            nb = nb or od.get("notBefore-custom", "") or od.get("notBefore", "")
            na = na or od.get("notAfter-custom", "") or od.get("notAfter", "")
        tm = ""
        raw_xml = open(path, encoding="utf-8").read()
        m = re.search(r"trismegistos\.org/tm/detail\.php\?quick=(\d+)", raw_xml)
        if m: tm = m.group(1)
        refs = []
        for key, lab in (("YN2W5LUE", "TAD"), ("4YJ2JLJ9", "TAD"), ("NLPFRPHR", "TAD"), ("HZ63VVKS", "TAD"), ("INFDS2WE", "CG"), ("NIJERM79", "Sachau")):
            for mm in re.finditer(r'<bibl corresp="elephantine_erc_db_literature\.tei\.xml#%s">\s*<biblScope>([^<]*)</biblScope>' % key, raw_xml):
                refs.append(f"{lab} {mm.group(1).strip()}")
        tm = tm + "|" + "; ".join(refs)
        out = Out()
        for ab in edition_abs(root):
            out.mark("PB", "")
            if ab.text: out.text(ab.text, False)
            for k in ab:
                walk(k, False, out)
                if k.tail: out.text(k.tail, False)
        rows = tokens_from_items(out.items, doc)
        for i, r in enumerate(rows):
            ft.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{i}\t{r[3]}\t{r[4]}\t{r[5]}\n")
        na_ = sum(1 for r in rows if r[4] == "A")
        fd.write(f"{doc}\t{title}\t{lang}\t{nb}\t{na}\t{tm}\t{len(rows)}\t{na_}\n")

if __name__ == "__main__":
    main()
