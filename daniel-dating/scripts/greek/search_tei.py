"""Search Perseus / First1KGreek TEI XML files for Greek lemmata.

Usage: python3 -I search_tei.py OUT.csv ROOT [ROOT ...]
Writes one CSV row per hit with author, work, file, citation, form, context.
"""
import csv
import glob
import os
import re
import sys
import unicodedata

from lxml import etree

TEI = "{http://www.tei-c.org/ns/1.0}"
CTS = "{http://chs.harvard.edu/xmlns/cts}"

SKIP = {"teiHeader", "note", "bibl", "rdg", "sic", "orig", "del", "fw", "ref", "gap", "figure"}

# Word pattern: Greek letters + combining marks + elision marks
GREEK = "Ͱ-Ͽἀ-῿̀-ͯ"
WORD_RE = re.compile(r"[%s]+(?:[\-­]\s*[%s]+)?[’᾽'ʼ]?" % (GREEK, GREEK))

PATTERNS = {
    "symphon": re.compile(r"^(συμ|ξυμ|συν|ξυν)φων"),
    "psalter": re.compile(r"^(ψαλτηρ|ψαλτερ|ψαλτιρ|ψαντηρ|ψαλτειρ)"),
    "kithar": re.compile(r"^κιθαρ"),
}


def norm(tok):
    t = unicodedata.normalize("NFD", tok)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace("ς", "σ").replace("ϲ", "σ")
    t = re.sub(r"[^α-ω]", "", t)
    return t


def local(tag):
    if not isinstance(tag, str):
        return None
    return tag.split("}", 1)[-1]


def cts_names(path):
    """Return (author, work) from __cts__.xml files next to the text."""
    wdir = os.path.dirname(path)
    adir = os.path.dirname(wdir)
    author = work = ""
    try:
        t = etree.parse(os.path.join(adir, "__cts__.xml"))
        g = t.find(".//" + CTS + "groupname")
        if g is not None:
            author = (g.text or "").strip()
    except Exception:
        pass
    try:
        t = etree.parse(os.path.join(wdir, "__cts__.xml"))
        titles = t.findall(".//" + CTS + "title")
        if titles:
            work = (titles[0].text or "").strip()
    except Exception:
        pass
    return author, work


def walk(elem, state, segs):
    """Depth-first traversal emitting (text, citation) segments."""
    name = local(elem.tag)
    if name is None:  # comment / PI
        if elem.tail:
            segs.append((elem.tail, cite_str(state)))
        return
    if name in SKIP:
        if elem.tail:
            segs.append((elem.tail, cite_str(state)))
        return
    pushed = False
    if name == "div" or re.fullmatch(r"div\d", name or ""):
        typ = elem.get("type", "")
        n = elem.get("n")
        if typ not in ("edition", "translation", "commentary") and n is not None and not n.startswith("urn:"):
            label = elem.get("subtype") or typ or name
            state["divs"].append((label, n))
            pushed = True
            state["l"] = None
    elif name == "milestone":
        unit = elem.get("unit")
        n = elem.get("n")
        if unit and n:
            state["ms"][unit] = n
    elif name == "l" and elem.get("n"):
        state["l"] = elem.get("n")
    elif name == "lb" and elem.get("n"):
        state["l"] = elem.get("n")
    elif name in ("p", "ab", "lg", "sp") and elem.get("n"):
        state["ms"][name] = elem.get("n")
    if elem.text:
        segs.append((elem.text, cite_str(state)))
    for ch in elem:
        walk(ch, state, segs)
    if pushed:
        state["divs"].pop()
    if elem.tail:
        # block-level elements imply word separation
        segs.append((elem.tail, cite_str(state)))


def cite_str(state):
    parts = [f"{a}={b}" for a, b in state["divs"]]
    if state["l"]:
        parts.append(f"line={state['l']}")
    ms = state["ms"]
    extra = [f"{k}={v}" for k, v in ms.items() if k in (
        "casaubonpage", "stephpage", "section", "chapter", "para", "page", "bekker", "line", "tlnum", "card", "subsection",
        "reiskpage", "p", "verse")]
    if extra:
        parts.append("[" + ",".join(extra) + "]")
    return "|".join(parts)


BLOCK = {"p", "l", "div", "lb", "head", "sp", "speaker", "ab", "lg", "item", "cell", "row", "quote", "cit", "pb", "milestone"}


def process(path, writer, stats):
    try:
        tree = etree.parse(path, etree.XMLParser(recover=True, huge_tree=True))
    except Exception as e:
        stats["errors"].append((path, str(e)))
        return
    root = tree.getroot()
    body = root.find(".//" + TEI + "body")
    if body is None:
        body = root.find(".//body")
    if body is None:
        stats["errors"].append((path, "no body"))
        return
    state = {"divs": [], "ms": {}, "l": None}
    segs = []
    # insert separators for block elements by pre-adding a space to their tails
    for el in body.iter():
        nm = local(el.tag)
        if nm in BLOCK:
            el.tail = " " + (el.tail or "")
            if nm in ("lb", "pb", "milestone") and el.get("break") == "no":
                el.tail = el.tail[1:]
    walk(body, state, segs)
    text_parts = []
    offsets = []
    cites = []
    pos = 0
    for t, c in segs:
        text_parts.append(t)
        offsets.append(pos)
        cites.append(c)
        pos += len(t)
    text = "".join(text_parts)
    import bisect
    toks = [(m.start(), m.group()) for m in WORD_RE.finditer(text)]
    stats["tokens"] += len(toks)
    author, work = cts_names(path)
    normed = [norm(t) for _, t in toks]
    for i, nt in enumerate(normed):
        for key, pat in PATTERNS.items():
            if pat.match(nt):
                st = toks[i][0]
                si = bisect.bisect_right(offsets, st) - 1
                cite = cites[si] if si >= 0 else ""
                lo = max(0, i - 12)
                hi = min(len(toks), i + 13)
                ctx_start = toks[lo][0]
                ctx_end = toks[hi - 1][0] + len(toks[hi - 1][1])
                ctx = re.sub(r"\s+", " ", text[ctx_start:ctx_end])
                writer.writerow({
                    "lemma_group": key,
                    "form": toks[i][1],
                    "norm": nt,
                    "author": author,
                    "work": work,
                    "file": os.path.relpath(path, stats["base"]),
                    "citation": cite,
                    "context": ctx,
                })
                stats["hits"] += 1


def main():
    out = sys.argv[1]
    roots = sys.argv[2:]
    files = []
    for r in roots:
        files += [f for f in glob.glob(os.path.join(r, "**", "*.xml"), recursive=True)
                  if "grc" in os.path.basename(f) and not os.path.basename(f).startswith("__")]
    files.sort()
    stats = {"tokens": 0, "hits": 0, "errors": [], "base": os.path.commonpath(roots) if len(roots) > 1 else os.path.dirname(roots[0])}
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["lemma_group", "form", "norm", "author", "work", "file", "citation", "context"])
        w.writeheader()
        for k, f in enumerate(files):
            process(f, w, stats)
    print("files", len(files), "tokens", stats["tokens"], "hits", stats["hits"], "errors", len(stats["errors"]))
    for e in stats["errors"][:20]:
        print("ERR", e)


if __name__ == "__main__":
    main()
