"""Polite sequential probe of Elephantine ERC TEI records.
usage: probe.py IDFILE OUT.tsv [delay]
For each id: Range GET bytes 0-4095; record status, total size, mainLang, title."""
import sys, time, re, os, urllib.request, urllib.error
BASE = "https://elephantine.smb.museum/xml/elephantine_erc_db_%06d.tei.xml"
UA = "Mozilla/5.0 (compatible; academic-corpus-count; non-commercial research)"
idfile, out = sys.argv[1], sys.argv[2]
delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
done = set()
if os.path.exists(out):
    for line in open(out, encoding="utf-8"):
        done.add(int(line.split("\t")[0]))
ids = [int(x) for x in open(idfile).read().split() if int(x) not in done]
f = open(out, "a", encoding="utf-8")
for i in ids:
    req = urllib.request.Request(BASE % i, headers={"Range": "bytes=0-4095", "User-Agent": UA})
    status, size, lang, title = 0, "", "", ""
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                status = r.status
                cr = r.headers.get("Content-Range", "")
                size = cr.split("/")[-1] if cr else r.headers.get("Content-Length", "")
                body = r.read().decode("utf-8", "replace")
                m = re.search(r'mainLang="([^"]*)"', body); lang = m.group(1) if m else "?"
                m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S)
                title = re.sub(r"\s+", " ", m.group(1)).strip()[:120] if m else ""
            break
        except urllib.error.HTTPError as e:
            status = e.code
            if e.code in (404, 403, 416): break
            time.sleep(5 * (attempt + 1))
        except Exception as e:
            status = -1; title = repr(e)[:80]
            time.sleep(5 * (attempt + 1))
    f.write(f"{i}\t{status}\t{size}\t{lang}\t{title}\n"); f.flush()
    time.sleep(delay)
