"""Download full TEI for ids whose probe row says arc-*.
usage: fetch_full.py OUTDIR PROBE.tsv..."""
import sys, os, time, requests
BASE = "https://elephantine.smb.museum/xml/elephantine_erc_db_%06d.tei.xml"
UA = "Mozilla/5.0 (compatible; academic-corpus-count; non-commercial research)"
outdir = sys.argv[1]
ids = set()
for p in sys.argv[2:]:
    for line in open(p, encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 4 and f[1] in ("200", "206") and ("Armi" in f[3] or f[3].startswith("arc")):
            ids.add(int(f[0]))
s = requests.Session(); s.headers["User-Agent"] = UA
n = 0
for i in sorted(ids):
    fn = os.path.join(outdir, "elephantine_erc_db_%06d.tei.xml" % i)
    if os.path.exists(fn):
        continue
    for attempt in range(4):
        try:
            r = s.get(BASE % i, timeout=60)
            if r.status_code == 200:
                open(fn + ".tmp", "wb").write(r.content); os.replace(fn + ".tmp", fn); n += 1
                break
            if r.status_code == 404:
                break
        except Exception:
            s = requests.Session(); s.headers["User-Agent"] = UA
        time.sleep(3 * (attempt + 1))
    time.sleep(0.15)
print("fetched", n, "of", len(ids))
