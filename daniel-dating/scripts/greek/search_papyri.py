"""Search DDbDP / DCLP EpiDoc files for the target stems, attaching HGV/DCLP dates.
Usage: python3 -I search_papyri.py IDP_ROOT OUT.csv"""
import csv
import glob
import os
import re
import sys
import unicodedata

from lxml import etree

T = "{http://www.tei-c.org/ns/1.0}"
SKIP = {"note", "rdg", "sic", "orig", "del", "teiHeader", "certainty", "desc", "figure"}
GREEK = "Ͱ-Ͽἀ-῿̀-ͯ"
WORD_RE = re.compile(r"[%s]+" % GREEK)
PATTERNS = {
    "symphon": re.compile(r"^(συμ|ξυμ|συν|ξυν)φων"),
    "psalter": re.compile(r"^(ψαλτηρ|ψαλτερ|ψαλτιρ|ψαντηρ|ψαλτειρ)"),
    "kithar": re.compile(r"^κιθαρ"),
}


def norm(tok):
    t = unicodedata.normalize("NFD", tok)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace("ς", "σ").replace("ϲ", "σ")
    return re.sub(r"[^α-ω]", "", t)


def local(tag):
    return tag.split("}", 1)[-1] if isinstance(tag, str) else None


def collect(elem, out, line):
    name = local(elem.tag)
    if name is None:
        if elem.tail:
            out.append((elem.tail, line[0]))
        return
    if name in SKIP:
        if elem.tail:
            out.append((elem.tail, line[0]))
        return
    if name == "lb":
        line[0] = elem.get("n") or line[0]
        if elem.get("break") != "no":
            out.append((" ", line[0]))
    elif name in ("ab", "div", "p", "l", "cb", "pb"):
        out.append((" ", line[0]))
    if name == "gap":
        out.append((" … ", line[0]))
    if elem.text:
        out.append((elem.text, line[0]))
    for ch in elem:
        collect(ch, out, line)
    if elem.tail:
        out.append((elem.tail, line[0]))


def hgv_dates(root):
    """Map HGV id -> (notBefore, notAfter, text) from HGV_meta_EpiDoc."""
    m = {}
    for f in glob.glob(os.path.join(root, "HGV_meta_EpiDoc", "*", "*.xml")):
        try:
            t = etree.parse(f)
        except Exception:
            continue
        hid = os.path.splitext(os.path.basename(f))[0]
        od = t.find(".//" + T + "origDate")
        title = t.find(".//" + T + "title")
        if od is not None:
            nb = od.get("notBefore") or od.get("when") or ""
            na = od.get("notAfter") or od.get("when") or ""
            m[hid] = (nb, na, " ".join("".join(od.itertext()).split()), (title.text or "").strip() if title is not None else "")
    return m


def main():
    root, out = sys.argv[1], sys.argv[2]
    dates = hgv_dates(root)
    files = glob.glob(os.path.join(root, "DDbDP", "*", "*.xml")) + glob.glob(os.path.join(root, "DCLP", "*", "*.xml"))
    n_tok = 0
    rows = []
    for f in files:
        try:
            t = etree.parse(f)
        except Exception:
            continue
        r = t.getroot()
        title = r.find(".//" + T + "titleStmt/" + T + "title")
        title = " ".join("".join(title.itertext()).split()) if title is not None else ""
        hgv = [i.text for i in r.findall(".//" + T + "idno[@type='HGV']") if i.text]
        dl = "DCLP" in f
        nb = na = dtext = hgvtitle = ""
        if dl:
            od = r.find(".//" + T + "origDate")
            if od is not None:
                nb = od.get("notBefore") or od.get("when") or ""
                na = od.get("notAfter") or od.get("when") or ""
                dtext = " ".join("".join(od.itertext()).split())
        else:
            for h in (hgv[0].split() if hgv else []):
                if h in dates:
                    nb, na, dtext, hgvtitle = dates[h]
                    break
        segs = []
        for ed in r.iter(T + "div"):
            if ed.get("type") == "edition":
                collect(ed, segs, [""])
        text = ""
        offs = []
        lines = []
        for s, ln in segs:
            offs.append(len(text))
            lines.append(ln)
            text += s
        toks = [(m.start(), m.group()) for m in WORD_RE.finditer(text)]
        n_tok += len(toks)
        import bisect
        for i, (st, tok) in enumerate(toks):
            nt = norm(tok)
            for key, pat in PATTERNS.items():
                if pat.match(nt):
                    si = bisect.bisect_right(offs, st) - 1
                    lo, hi = max(0, i - 12), min(len(toks), i + 13)
                    ctx = re.sub(r"\s+", " ", text[toks[lo][0]: toks[hi - 1][0] + len(toks[hi - 1][1])])
                    rows.append({
                        "lemma_group": key, "form": tok, "norm": nt,
                        "collection": "DCLP" if dl else "DDbDP",
                        "file": os.path.relpath(f, root), "title": title, "hgv_title": hgvtitle,
                        "not_before": nb, "not_after": na, "date_text": dtext,
                        "line": lines[si] if si >= 0 else "", "context": ctx,
                    })
    def key(x):
        try:
            return int(x["not_before"][:5].replace("-", "-") if x["not_before"] else 9999)
        except ValueError:
            try:
                return int(x["not_before"].split("-")[0] or 0) * (-1 if x["not_before"].startswith("-") else 1)
            except ValueError:
                return 9999
    def year(s):
        if not s:
            return 9999
        m = re.match(r"^(-?)(\d+)", s)
        return int(m.group(2)) * (-1 if m.group(1) else 1) if m else 9999
    rows.sort(key=lambda x: (year(x["not_before"]), x["file"]))
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("files", len(files), "tokens", n_tok, "hits", len(rows), "hgv dates", len(dates))


if __name__ == "__main__":
    main()
