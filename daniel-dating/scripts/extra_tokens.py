"""Harmonise the ETCBC extrabiblical corpus with BHSA conventions:
- pronominal suffixes are separate 'prps' tokens attached to the preceding word (no space);
  fold them into the host word (has_suffix=True) and drop them;
- lexemes lack the BHSA '/', '[' markers; map each bare lexeme to the BHSA lexeme with the same bare form."""
import re
from collections import Counter, defaultdict

GROUPS = {
    "Arad": "EX Epigraphic Hebrew c. 700-587 BCE", "Lachish": "EX Epigraphic Hebrew c. 700-587 BCE",
    "Mesad_Hashavyahu": "EX Epigraphic Hebrew c. 700-587 BCE", "Ketef_Hinnom": "EX Epigraphic Hebrew c. 700-587 BCE",
    "Siloam": "EX Epigraphic Hebrew c. 700-587 BCE",
    "1QS": "EX 1QS (ETCBC encoding)", "1QM": "EX 1QM (ETCBC encoding)", "1QH": "EX 1QH (ETCBC encoding)",
    "Pirqe": "EX Mishnah: Pirqe Avot (c. 200-250 CE)", "Shirata": "EX Mekhilta: Shirata (3rd c. CE)",
}
bare = lambda l: re.sub(r"[/\[=]", "", l or "")

def bhsa_lex_map(F):
    cnt = defaultdict(Counter)
    for w in F.otype.s("word"):
        cnt[bare(F.lex.v(w))][F.lex.v(w)] += 1
    return {b: c.most_common(1)[0][0] for b, c in cnt.items()}

def extra_tokens(EA, lexmap):
    """yield (unit, book, dict(lex, vt, vs, ps, nu, gn, cons, has_suffix, prev_lex))"""
    F, L, T = EA.F, EA.L, EA.T
    out = defaultdict(list)
    for b in F.otype.s("book"):
        name = T.sectionFromNode(b)[0]
        unit = GROUPS.get(name)
        if not unit:
            continue
        ws = list(L.d(b, "word"))
        toks = []
        for i, w in enumerate(ws):
            attached = i > 0 and (F.g_suffix.v(ws[i - 1]) or "") == ""
            if F.sp.v(w) == "prps" and attached and toks:
                toks[-1]["has_suffix"] = True
                toks[-1]["sfx_lex"] = F.lex.v(w)
                continue
            vt = F.vt.v(w) if F.sp.v(w) == "verb" else None
            vt = vt if vt not in ("NA", "unknown", None, "") else None
            toks.append(dict(lex=lexmap.get(bare(F.lex.v(w)), F.lex.v(w)), vt=vt, vs=F.vs.v(w) if vt else None,
                             ps=F.ps.v(w), nu=F.nu.v(w), gn=F.gn.v(w), cons=F.g_cons_utf8.v(w) or "",
                             has_suffix=False, sp=F.sp.v(w)))
        for j, t in enumerate(toks):
            t["prev_lex"] = toks[j - 1]["lex"] if j else None
        out[unit].extend(toks)
    return out
