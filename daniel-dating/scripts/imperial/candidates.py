"""Dump distinct candidate forms per feature regex for manual curation.
usage: candidates.py NAME=TOKENS.tsv ...   (prints table form, counts per corpus, statuses A/R)"""
import sys, re, collections
PATS = {
 "sfx_hm":  r"..+המ$",
 "sfx_hwm": r".+הומ$",
 "sfx_hwn": r".+הונ$",
 "sfx_km":  r".+כמ$",
 "sfx_kwn": r".+כונ$",
 "caus_h":  r"^(ו)?(ל|מ|ת|י|נ|א|כ|ב|ז|ד)?ה[^ת].{2,}$",
 "caus_a":  r"^(ו)?(ל|מ|כ|ב|ז|ד)?א[^ת].{2,}$",
 "refl_ht": r"^(ו)?(ל|מ|כ|ב|ז|ד)?הת..+$",
 "refl_at": r"^(ו)?(ל|מ|כ|ב|ז|ד)?את..+$",
 "pron3mp": r"^(ו)?(המ|המו|המונ|הומ|הונ|אנונ|אנינ|הנונ|הנינ)$",
 "demPl":   r"^(ו)?(כ|ב|ל|מ)?(אלה|אל|אלכ|אלנ|אלינ|אלו|אלכה|אלכי)$",
 "rel":     r"^(ו)?(כ|ב|ל|מ|מנ|ע|עד)?(זי|די|ד|ז)$",
 "zyl":     r"^(ו)?(זיל|דיל).*$",
 "earth":   r"^(ו)?(ב|ל|מ|כ|ד|ז)?(ארק|ארע).*$",
 "sfx_2ms_kh": r"..+כה$",
 "this":    r"^(ו)?(ב|ל|מ|כ|ע|עד)?(זנה|דנה|זנ|דנ|דא|זא|דה|זה|דנא|זנא)$",
 "that":    r"^(ו)?(ב|ל|מ|כ|ע|עד)?(זכ|זכי|זכה|דכ|דכי|דכה|דכנ|זכנ|דכנה|זכנה|אכ)$",
 "gold":    r"^(ו)?(ב|ל|מ|כ|ד|ז)?(זהב|דהב).*$",
 "remember": r"^(ו)?(ב|ל|מ|כ|ד|ז|י|ת|נ|א)?(זכר|דכר).*$",
 "sacrifice": r"^(ו)?(ב|ל|מ|כ|ד|ז|י|ת|נ)?(זבח|דבח|דבחי|זבחי).*$",
 "objmark": r"^(ו)?(ית|יות|את|אית|יתה|יתהמ|יתהומ|יתהונ|יתכ|יתי|יתנ|יתכמ|יתכונ)$",
 "pron2ms": r"^(ו)?(אנת|אנתה|את|אתה)$",
 "pron1cp": r"^(ו)?(אנחנ|אנחנה|אנחנא|אנחננ|אנחנו|נחנ|נחנה)$",
 "behold":  r"^(ו)?(הלו|אלו|ארו|הא|הנ)$",
 "now":     r"^(ו)?(כענ|כענת|כעת|כעננ)$",
 "be_impf": r"^(ו)?(יהוה|יהוא|להוה|להוא|יהוונ|להוונ|להונ|יהונ|תהוה|תהוא|תהוונ|לתהוונ|נהוה|אהוה)$",
}
corpora = [a.split("=", 1) for a in sys.argv[1:]]
data = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.Counter()))
for name, path in corpora:
    for i, line in enumerate(open(path, encoding="utf-8")):
        if i == 0: continue
        f = line.rstrip("\n").split("\t")
        form, st = f[4], f[5]
        if st == "F": continue
        for feat, pat in PATS.items():
            if re.search(pat, form):
                data[feat][form][(name, st)] += 1
names = [n for n, _ in corpora]
for feat in PATS:
    print(f"### {feat}")
    rows = sorted(data[feat].items(), key=lambda kv: -sum(kv[1].values()))
    for form, c in rows:
        cells = " ".join(f"{n}:{c[(n,'A')]}+{c[(n,'R')]}" for n in names if c[(n,'A')] or c[(n,'R')])
        print(f"{form}\t{cells}")
