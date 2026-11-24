"""Assemble daniel-dating/report/index.html from the template, the SVG charts and the claim database."""
import os, json, html, csv
from collections import OrderedDict
import pandas as pd
import numpy as np

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "results")
REP = os.path.join(HERE, "..", "report")
esc = lambda s: html.escape(str(s), quote=True)

charts = json.load(open(os.path.join(RES, "charts", "charts.json")))
tpl = open(os.path.join(REP, "template.html")).read()

# claims list
seg = pd.read_csv(os.path.join(RES, "prophecy_segments.csv"))
cl = pd.read_csv(os.path.join(RES, "prophecy_claims.csv"))
parts = []
for _, s in seg.iterrows():
    if s["n_claims"] == 0:
        continue
    rows = cl[cl.verses == s["id"]]
    stat = f'{s["hits"]} hit · {s["partial"]} partial · {s["misses"]} miss' + (f' · {s["vague"]} vague' if s["vague"] else "")
    lis = "".join(
        f'<li><span><span class="pill p-{esc(r.status)}">{esc(r.status)}</span></span>'
        f'<span>{esc(r.claim)}<small>{esc(r["ancient evidence"]) if isinstance(r["ancient evidence"], str) and r["ancient evidence"] else "no specific record"}</small></span></li>'
        for _, r in rows.iterrows())
    parts.append(f'<details class="seg"><summary><span class="sref">Dan {esc(s["id"])}</span>'
                 f'<span class="slab">{esc(s["label"])} <span class="sstat">({esc(s["span"])})</span></span>'
                 f'<span class="sstat">{stat}</span></summary><ul class="claims">{lis}</ul></details>')
claims_html = "".join(parts)

# era word counts
yr = {}
for _, r in seg.iterrows():
    y0, y1 = [int(x) for x in r["span"].replace(" BCE", "").split("-")]
    n = y0 - y1 + 1
    for y in range(y1, y0 + 1):
        yr[y] = yr.get(y, 0) + r["words"] / n
pers = round(sum(v for y, v in yr.items() if 331 <= y <= 550))
a4 = round(sum(v for y, v in yr.items() if 166 <= y <= 175))

# hebrew model calibrated MAE
s_ = pd.read_csv(os.path.join(RES, "hebrew_chronolect_summary_function.csv"))
a = s_[s_.role == "anchor"].dropna(subset=["loo_pred"])
b, c = np.polyfit(a.loo_pred, a.anchor_date, 1)
mae = int(round((a.anchor_date - (b * a.loo_pred + c)).abs().mean(), -1))

imperial = ""
ip = os.path.join(RES, "imperial_aramaic_note.html")
if os.path.exists(ip):
    imperial = open(ip).read().strip()

out = (tpl.replace("{{timeline}}", charts["timeline"]).replace("{{hebmodel}}", charts["hebmodel"])
          .replace("{{hebvars}}", charts["hebvars"]).replace("{{aramaic}}", charts["aramaic"])
          .replace("{{claims}}", claims_html).replace("{{pers_words}}", str(pers)).replace("{{a4_words}}", str(a4))
          .replace("{{mae}}", f"about {mae}").replace("{{imperial}}", imperial))
assert "{{" not in out, [l for l in out.splitlines() if "{{" in l][:3]
open(os.path.join(REP, "index.html"), "w").write(out)
print("wrote", len(out), "bytes; pers", pers, "a4", a4, "mae", mae)
