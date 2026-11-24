"""Sequential probe with a persistent keep-alive session (requests).
usage: probe2.py IDFILE OUT.tsv [delay]"""
import sys, time, re, os, requests
BASE = "https://elephantine.smb.museum/xml/elephantine_erc_db_%06d.tei.xml"
UA = "Mozilla/5.0 (compatible; academic-corpus-count; non-commercial research)"
idfile, out = sys.argv[1], sys.argv[2]
delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
done = set()
if os.path.exists(out):
    for line in open(out, encoding="utf-8"):
        done.add(int(line.split("\t")[0]))
ids = [int(x) for x in open(idfile).read().split() if int(x) not in done]
s = requests.Session(); s.headers.update({"User-Agent": UA})
f = open(out, "a", encoding="utf-8")
for i in ids:
    status, size, lang, title = 0, "", "", ""
    for attempt in range(4):
        try:
            r = s.get(BASE % i, headers={"Range": "bytes=0-4095"}, timeout=30)
            status = r.status_code
            if status in (200, 206):
                cr = r.headers.get("Content-Range", "")
                size = cr.split("/")[-1] if cr else r.headers.get("Content-Length", "")
                body = r.content.decode("utf-8", "replace")
                m = re.search(r'mainLang="([^"]*)"', body); lang = m.group(1) if m else "?"
                m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S)
                title = re.sub(r"\s+", " ", m.group(1)).strip()[:120] if m else ""
                break
            if status in (404, 403, 416): break
            time.sleep(5 * (attempt + 1))
        except Exception as e:
            status = -1; title = repr(e)[:80]
            s = requests.Session(); s.headers.update({"User-Agent": UA})
            time.sleep(5 * (attempt + 1))
    f.write(f"{i}\t{status}\t{size}\t{lang}\t{title}\n"); f.flush()
    time.sleep(delay)
