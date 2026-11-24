import sys, time, urllib.request, urllib.parse, os, json
out = sys.argv[1]
jobs = []
for b in ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy"]:
    jobs.append((f"Onkelos {b}", "he", f"Onkelos {b}"))
for b in ["Joshua","Judges","I Samuel","II Samuel","I Kings","II Kings","Isaiah"]:
    jobs.append((f"Targum Jonathan on {b}", "he", "Mikraot Gedolot"))
jobs.append(("Megillat Antiochus", "he", "the Open Siddur Project - Aramaic"))
jobs.append(("Megillat Antiochus", "he", "the Open Siddur Project"))  # Hebrew version, for comparison only
for title, lang, vt in jobs:
    fn = os.path.join(out, f"{title} - {lang} - {vt}.json".replace("/", "_"))
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        print("skip", fn); continue
    url = "https://www.sefaria.org/download/version/" + urllib.parse.quote(f"{title} - {lang} - {vt}.json")
    req = urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    json.loads(data)  # validate
    open(fn, "wb").write(data)
    print(title, vt, len(data))
    time.sleep(1.5)
