"""Generate the inline-SVG charts for the report from the results/ CSVs.
Colors are CSS custom properties defined by the page, so the charts follow light/dark themes.
Each mark carries data-tip for the page's hover tooltip."""
import os, json, csv, math, html
from collections import defaultdict
import pandas as pd
import numpy as np

RES = os.path.join(os.path.dirname(__file__), "..", "results")
OUT = os.path.join(RES, "charts")
os.makedirs(OUT, exist_ok=True)
esc = lambda s: html.escape(str(s), quote=True)

def svg_open(w, h, label):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}" class="chart" '
            f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">')

# ------------------------------------------------------------------ chart 1: resolution + accuracy
def chart_timeline():
    seg = pd.read_csv(os.path.join(RES, "prophecy_segments.csv"))
    # words per decade of history, aggregated over all segments
    dec = defaultdict(float)
    for _, r in seg.iterrows():
        y0, y1 = [int(x) for x in r["span"].replace(" BCE", "").split("-")]
        years = y0 - y1 + 1
        for y in range(y1, y0 + 1):
            dec[(y - 1) // 5 * 5 + 1] += r["words"] / years   # 5-year bins 556-560 etc (BCE, counting down)
    W, H = 760, 430
    L, R = 58, 18
    x0, x1 = 560, 150      # BCE, left to right
    X = lambda y: L + (x0 - y) / (x0 - x1) * (W - L - R)
    # panel A
    aT, aB = 34, 190
    vmax = max(dec.values())
    ymaxA = math.ceil(vmax / 50) * 50
    YA = lambda v: aB - v / ymaxA * (aB - aT)
    s = [svg_open(W, H, "Words of prophecy per decade of history, and accuracy of claims by period")]
    s.append(f'<text x="{L}" y="18" class="ct">Words of prophecy spent on each five years of history (Dan 8, 11, 12:11-12)</text>')
    for v in range(0, ymaxA + 1, 50):
        s.append(f'<line x1="{L}" x2="{W-R}" y1="{YA(v):.1f}" y2="{YA(v):.1f}" class="grid"/>'
                 f'<text x="{L-8}" y="{YA(v)+4:.1f}" class="tick" text-anchor="end">{v}</text>')
    for d in sorted(dec):
        v = dec[d]
        if v <= 0:
            continue
        xa, xb = X(d + 4), X(d - 1)
        late = d <= 165
        h = aB - YA(v)
        s.append(f'<rect x="{xa+1:.1f}" y="{YA(v):.1f}" width="{max(1.5, xb-xa-2):.1f}" height="{max(h, 1.5):.1f}" rx="2" '
                 f'class="bar{" fut" if late else ""}" data-tip="{d+4}-{d} BCE: {v:.0f} words{" (predicted: the time of the end)" if late else ""}"/>')
    # annotations
    pers = sum(v for d, v in dec.items() if d >= 331)
    s.append(f'<text x="{X(520):.1f}" y="{aB-40}" class="ann">Persian era, 550-331 BCE:</text>'
             f'<text x="{X(520):.1f}" y="{aB-24}" class="ann">{pers:.0f} words in 220 years</text>')
    s.append(f'<text x="{X(470):.1f}" y="{aB-6}" class="ann muted">479-337: nothing at all</text>')
    a4 = sum(v for d, v in dec.items() if 166 <= d <= 175)
    s.append(f'<text x="{X(180):.1f}" y="{aT+8}" class="ann" text-anchor="end">Antiochus IV, 175-166 BCE: {a4:.0f} words</text>')
    s.append(f'<line x1="{L}" x2="{W-R}" y1="{aB}" y2="{aB}" class="axis"/>')
    # panel B: accuracy per segment
    bT, bB = 250, 390
    YB = lambda p: bB - p * (bB - bT)
    s.append(f'<text x="{L}" y="{bT-16}" class="ct">Share of checkable claims that match the ancient record</text>')
    for p in (0, 0.5, 1):
        s.append(f'<line x1="{L}" x2="{W-R}" y1="{YB(p):.1f}" y2="{YB(p):.1f}" class="grid"/>'
                 f'<text x="{L-8}" y="{YB(p)+4:.1f}" class="tick" text-anchor="end">{int(p*100)}%</text>')
    for _, r in seg.iterrows():
        if pd.isna(r["accuracy"]):
            continue
        y0, y1 = [int(x) for x in r["span"].replace(" BCE", "").split("-")]
        mid = (y0 + y1) / 2
        fut = str(r["future"]) == "True"
        cls = "dot fut" if fut else "dot"
        tip = (f'Dan {r["id"]} ({r["span"]}): {r["label"]}. {r["hits"]} match, {r["partial"]} partly, '
               f'{r["misses"]} no match, {r["vague"]} too vague; score {r["accuracy"]:.0%}')
        s.append(f'<line x1="{X(y0):.1f}" x2="{X(y1):.1f}" y1="{YB(r["accuracy"]):.1f}" y2="{YB(r["accuracy"]):.1f}" class="span{" fut" if fut else ""}"/>')
        s.append(f'<circle cx="{X(mid):.1f}" cy="{YB(r["accuracy"]):.1f}" r="5.5" class="{cls}" data-tip="{esc(tip)}"/>')
    s.append(f'<text x="{X(163)-12:.1f}" y="{YB(0.05)+4:.1f}" class="ann" text-anchor="end">11:40-45 and 12:11-12, the predicted end</text>')
    s.append(f'<line x1="{X(165.5):.1f}" x2="{X(165.5):.1f}" y1="{bT-4}" y2="{bB}" class="cp"/>'
             f'<text x="{X(165.5)-8:.1f}" y="{YB(0.3)+4:.1f}" class="ann" text-anchor="end">break ~165 BCE</text>')
    s.append(f'<line x1="{L}" x2="{W-R}" y1="{bB}" y2="{bB}" class="axis"/>')
    for y in range(550, 149, 50):
        s.append(f'<line x1="{X(y):.1f}" x2="{X(y):.1f}" y1="{bB}" y2="{bB+5}" class="axis"/>'
                 f'<text x="{X(y):.1f}" y="{bB+19}" class="tick" text-anchor="middle">{y}</text>')
    s.append(f'<text x="{W-R}" y="{H-6}" class="tick" text-anchor="end">years BCE</text>')
    s.append("</svg>")
    return "\n".join(s)

# ------------------------------------------------------------------ dot-plot helper
def dotplot(rows, series, title, xlabel, W=760, row_h=34, left=230):
    """rows: list of (label, sublabel, {series_key: (value 0..1, n, tip)})"""
    T = 26
    H = T + row_h * len(rows) + 46
    R = 22
    X = lambda p: left + p * (W - left - R)
    s = [svg_open(W, H, title)]
    for p in (0, .25, .5, .75, 1):
        s.append(f'<line x1="{X(p):.1f}" x2="{X(p):.1f}" y1="{T-6}" y2="{T+row_h*len(rows)}" class="grid"/>'
                 f'<text x="{X(p):.1f}" y="{T+row_h*len(rows)+16}" class="tick" text-anchor="middle">{int(p*100)}%</text>')
    s.append(f'<text x="{(left+W-R)/2:.1f}" y="{H-8}" class="tick" text-anchor="middle">{esc(xlabel)}</text>')
    for i, (lab, sub, vals) in enumerate(rows):
        y = T + row_h * i + row_h / 2
        s.append(f'<text x="{left-12}" y="{y-1:.1f}" class="rl" text-anchor="end">{esc(lab)}</text>')
        if sub:
            s.append(f'<text x="{left-12}" y="{y+12:.1f}" class="rs" text-anchor="end">{esc(sub)}</text>')
        s.append(f'<line x1="{X(0):.1f}" x2="{X(1):.1f}" y1="{y:.1f}" y2="{y:.1f}" class="rowline"/>')
        y0row = y
        nser = len(series)
        for si, (key, (shape, cls)) in enumerate(series.items()):
            if key not in vals or vals[key][0] is None:
                continue
            v, n, tip = vals[key]
            cx = X(v)
            y = T + row_h * i + row_h / 2 + (si - (nser - 1) / 2) * 4
            t = f'data-tip="{esc(tip)}"'
            if shape == "circle":
                s.append(f'<circle cx="{cx:.1f}" cy="{y:.1f}" r="6.5" class="{cls}" {t}/>')
            elif shape == "ring":
                s.append(f'<circle cx="{cx:.1f}" cy="{y:.1f}" r="6" class="{cls}" {t}/>')
            elif shape == "square":
                s.append(f'<rect x="{cx-5.5:.1f}" y="{y-5.5:.1f}" width="11" height="11" rx="2" class="{cls}" {t}/>')
            elif shape == "diamond":
                s.append(f'<path d="M{cx:.1f},{y-7:.1f} L{cx+7:.1f},{y:.1f} L{cx:.1f},{y+7:.1f} L{cx-7:.1f},{y:.1f}Z" class="{cls}" {t}/>')
            elif shape == "tri":
                s.append(f'<path d="M{cx:.1f},{y-7:.1f} L{cx+7:.1f},{y+5.5:.1f} L{cx-7:.1f},{y+5.5:.1f}Z" class="{cls}" {t}/>')
    s.append("</svg>")
    return "\n".join(s)

# ------------------------------------------------------------------ chart 2: Aramaic
def chart_aramaic():
    """Unified Aramaic comparison: Persian-era papyri, Ezra, Daniel (MT and Qumran copies), Qumran Aramaic."""
    df = pd.read_csv(os.path.join(RES, "aramaic_timeline.csv"))
    feats = [
        ("3mp suffix", "grammar", "'their': -hm vs -hwn"),
        ("2mp suffix", "grammar", "'your (pl.)': -km vs -kwn"),
        ("3mp pronoun", "grammar", "'they': hmw(n) vs ʾnwn"),
        ("plural demonstrative", "grammar", "'these': ʾlh/ʾlk vs ʾlyn"),
        ("causative prefix", "grammar", "causative: h- vs ʾ-"),
        ("relative particle", "spelling", "spelling: zy vs dy"),
        ("'this'", "spelling", "spelling: znh vs dnh"),
        ("'earth'", "spelling", "spelling: ʾrq vs ʾrʿ"),
    ]
    corp = {"Persian-era papyri": "pap", "Ezra": "ezra", "Daniel (Masoretic)": "dan", "Daniel (Qumran copies)": "danq", "Qumran Aramaic": "qum",
            "Targums (Onkelos and Jonathan)": "targ"}
    names = {"3mp suffix": "3rd pl. suffix", "2mp suffix": "2nd pl. suffix", "3mp pronoun": "3rd pl. pronoun",
             "plural demonstrative": "plural demonstrative", "causative prefix": "causative prefix",
             "relative particle": "relative particle", "'this'": "'this'", "'earth'": "'earth'"}
    rows = []
    for f, grp, sub in feats:
        vals = {}
        for c, k in corp.items():
            r = df[(df.feature == f) & (df.corpus == c)]
            if len(r):
                r = r.iloc[0]
                n = r.n_old + r.n_new
                if n:
                    vals[k] = (r.n_new / n, n, f"{c}: {r.n_new} of {n} later form = {r.n_new/n:.0%}")
        rows.append((names[f], sub, vals))
    series = {"pap": ("square", "m-c6"), "ezra": ("tri", "m-ezra"), "qum": ("diamond", "m-qum"), "targ": ("ring", "m-targ"), "danq": ("ring", "m-danq"), "dan": ("circle", "m-dan")}
    return dotplot(rows, series, "Aramaic: share of the later form from the 5th-century BCE papyri to the Targums", "share of the later form")

# ------------------------------------------------------------------ chart 3: Hebrew date model
def chart_hebrew_model():
    s_ = pd.read_csv(os.path.join(RES, "hebrew_chronolect_summary_function.csv"))
    a = s_[s_.role == "anchor"].dropna(subset=["loo_pred"])
    b, c = np.polyfit(a.loo_pred, a.anchor_date, 1)
    cal = lambda v: b * v + c
    groups = [
        ("Classical", ["MT Samuel", "MT Kings", "MT Judges"]),
        ("6th century", ["MT Jeremiah", "MT Ezekiel", "MT Haggai", "MT Zechariah 1-8", "MT Isaiah 40-55"]),
        ("Persian era", ["MT Ezra", "MT Nehemiah", "MT Chronicles", "MT Esther"]),
        ("Qumran, 2nd-1st c.", ["Q Jubilees Hebrew (4Q216-224)", "Q Temple Scroll (11Q19-20, 4Q524)", "Q MMT (4Q394-399)",
                                "Q Damascus Document (CD, 4Q266-273)", "Q Community Rule (1QS, 4QS)", "Q War Scroll (1QM, 4Q491-496)",
                                "Q Hodayot (1QHa, 4Q427-432)"]),
        ("Blind test", ["EX Epigraphic Hebrew c. 700-587 BCE"]),
        ("Daniel", ["MT Daniel 1", "MT Daniel 8", "MT Daniel 9", "MT Daniel 10", "MT Daniel 11", "MT Daniel 12", "MT Daniel (all Hebrew)"]),
    ]
    def short(u):
        if u.startswith("MT Daniel ("):
            return "Daniel, all Hebrew"
        if u.startswith("EX Epigraphic"):
            return "Inscriptions c. 700-587"
        for pre in ("MT ", "Q "):
            if u.startswith(pre):
                u = u[len(pre):]
        return u.split(" (")[0]
    rows = sum((len(m) for _, m in groups), 0) + len(groups)
    W, rh, T, left, R = 760, 19, 30, 200, 20
    H = T + rh * rows + 50
    x0, x1 = 800, 0
    X = lambda y: left + (x0 + y) / (x0 - x1) * (W - left - R)   # y negative BCE
    s = [svg_open(W, H, "Hebrew dating model: estimated date of each text, out-of-sample, calibrated")]
    for yr in range(800, -1, -100):
        s.append(f'<line x1="{X(-yr):.1f}" x2="{X(-yr):.1f}" y1="{T-8}" y2="{T+rh*rows}" class="grid"/>'
                 f'<text x="{X(-yr):.1f}" y="{T+rh*rows+16}" class="tick" text-anchor="middle">{yr}</text>')
    s.append(f'<text x="{(left+W-R)/2:.1f}" y="{H-10}" class="tick" text-anchor="middle">estimated date of the language, years BCE (each text scored blind)</text>')
    i = 0
    for gname, members in groups:
        y = T + rh * i + rh / 2 + 3
        s.append(f'<text x="8" y="{y:.1f}" class="gl">{esc(gname)}</text>')
        i += 1
        for u in members:
            r = s_[s_.unit == u]
            if not len(r):
                continue
            r = r.iloc[0]
            y = T + rh * i + rh / 2
            dan = u.startswith("MT Daniel")
            blind = u.startswith("EX ")
            est = cal(r.loo_pred if not (dan or blind) else r.pred_median)
            s.append(f'<text x="{left-10}" y="{y+4:.1f}" class="rl{" strong" if dan else ""}" text-anchor="end">{esc(short(u))}</text>')
            if blind:
                lo, hi = cal(r.boot_lo), cal(r.boot_hi)
                s.append(f'<rect x="{X(-700):.1f}" y="{y-7:.1f}" width="{X(-587)-X(-700):.1f}" height="14" rx="2" class="band"/>')
                s.append(f'<line x1="{X(lo):.1f}" x2="{X(hi):.1f}" y1="{y:.1f}" y2="{y:.1f}" class="ci blue"/>')
                s.append(f'<circle cx="{X(est):.1f}" cy="{y:.1f}" r="5.5" class="m-anchor" data-tip="Hebrew inscriptions (Lachish, Arad, Siloam, Mesad Hashavyahu, Ketef Hinnom), dated by archaeology to c. 700-587 BCE (shaded); never used in training. Model estimate c. {-est:.0f} BCE (bootstrap 90%: {-lo:.0f}-{-hi:.0f})"/>')
            elif dan:
                lo, hi = cal(r.boot_lo), cal(r.boot_hi)
                s.append(f'<line x1="{X(lo):.1f}" x2="{X(hi):.1f}" y1="{y:.1f}" y2="{y:.1f}" class="ci"/>')
                s.append(f'<circle cx="{X(est):.1f}" cy="{y:.1f}" r="5.5" class="m-dan" data-tip="{esc(short(u))}: estimated c. {-est:.0f} BCE (bootstrap 90%: {-lo:.0f}-{-hi:.0f} BCE)"/>')
            else:
                truth = r.anchor_date
                s.append(f'<line x1="{X(truth):.1f}" x2="{X(truth):.1f}" y1="{y-6:.1f}" y2="{y+6:.1f}" class="truth"/>')
                s.append(f'<circle cx="{X(est):.1f}" cy="{y:.1f}" r="4.5" class="m-anchor" data-tip="{esc(short(u))}: conventional date c. {-truth:.0f} BCE; model estimate without seeing it c. {-est:.0f} BCE"/>')
            i += 1
    s.append("</svg>")
    return "\n".join(s), b, c

# ------------------------------------------------------------------ chart 4: Hebrew variables
def chart_hebrew_vars():
    df = pd.read_csv(os.path.join(RES, "hebrew_variables.csv"))
    groups = {
        "c6": ["6th c.: Ezekiel", "6th c.: Jeremiah", "6th c.: Haggai + Zechariah 1-8"],
        "per": ["Persian LBH: Ezra-Nehemiah", "Persian LBH: Chronicles", "LBH: Esther"],
        "qum": ["Qumran non-biblical Hebrew (2nd-1st c. BCE)"],
        "dan": ["DANIEL Hebrew (1:1-2:4a, 8-12)"],
        "rab": ["Rabbinic Hebrew c. 200-250 CE (Pirqe Avot, Mekhilta Shirata)"],
        "bs": ["Ben Sira (c. 190 BCE; mostly medieval copies)"],
    }
    names = {"c6": "6th c. (Jer, Ezek, Hag, Zech 1-8)", "per": "Persian era (Ezra-Neh, Chr, Esth)", "qum": "Qumran Hebrew",
             "dan": "Daniel", "rab": "Rabbinic Hebrew (Mishnah, Mekhilta)", "bs": "Ben Sira (c. 190 BCE)"}
    vars_ = [("'kingdom'", "mamlākâ vs malkût"), ("1cs wayyiqtol", "'and I did': short vs long form"),
             ("1cs pronoun", "ʾānōkî vs ʾănî"), ("relative", "ʾăšer vs še- (Mishnaic)")]
    rows = []
    for v, sub in vars_:
        vals = {}
        for k, cs in groups.items():
            d = df[(df.variable == v) & (df.corpus.isin(cs))]
            nl, n = d.n_later.sum(), d.n_later.sum() + d.n_earlier.sum()
            if n:
                vals[k] = (nl / n, n, f"{names[k]}: {nl} of {n} = {nl/n:.0%} later form")
        rows.append((v.replace("1cs", "1st sg.").replace("'kingdom'", "word for 'kingdom'").replace("relative", "relative word"), sub, vals))
    series = {"c6": ("square", "m-c6"), "per": ("diamond", "m-per"), "qum": ("ring", "m-qum2"), "bs": ("square", "m-bs"), "rab": ("tri", "m-cla"), "dan": ("circle", "m-dan")}
    return dotplot(rows, series, "Hebrew: share of the later variant", "share of the later variant")

if __name__ == "__main__":
    charts = {"timeline": chart_timeline(), "aramaic": chart_aramaic(), "hebvars": chart_hebrew_vars()}
    hm, b, c = chart_hebrew_model()
    charts["hebmodel"] = hm
    json.dump(charts, open(os.path.join(OUT, "charts.json"), "w"))
    for k, v in charts.items():
        open(os.path.join(OUT, f"{k}.svg"), "w").write(v)
    print("calibration", b, c, {k: len(v) for k, v in charts.items()})
