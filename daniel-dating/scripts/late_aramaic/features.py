"""Count old/new Aramaic isoglosses in late Aramaic corpora.
Usage: python3 -I features.py TOKENS_TSV OUT_DIR
Reads tokens.tsv (corpus, ref, idx, vocalised, consonantal[finals normalised]).
Writes late_aramaic_features.csv, audit_hits.tsv, audit_examples.txt, samples for hand-checking.
"""
import sys, re, csv, os, random, unicodedata, collections

TSV, OUT = sys.argv[1], sys.argv[2]
CORPORA = ["Targum Onkelos", "Targum Jonathan (sample)", "Megillat Antiochus"]

# ---------------------------------------------------------------- load
verses = collections.OrderedDict()   # (corpus, ref) -> list of (voc, cons)
for line in open(TSV, encoding="utf-8"):
    corpus, ref, k, v, c = line.rstrip("\n").split("\t")
    verses.setdefault((corpus, ref), []).append((v, c))
words = collections.Counter(corpus for (corpus, ref), toks in verses.items() for _ in toks)
lexicon = set(c for toks in verses.values() for v, c in toks)

VNAMES = {'ְ': 'shva', 'ֱ': 'hat-seg', 'ֲ': 'hat-pat', 'ֳ': 'hat-qam', 'ִ': 'hireq',
          'ֵ': 'tsere', 'ֶ': 'segol', 'ַ': 'patah', 'ָ': 'qamats', 'ֹ': 'holam', 'ֻ': 'qubuts'}

def vowel_on_letter(voc, n):
    """vowel signs attached to the n-th letter (0-based) of the vocalised token"""
    v = unicodedata.normalize("NFD", voc)
    letters = [i for i, ch in enumerate(v) if 'א' <= ch <= 'ת']
    if n >= len(letters):
        return "none"
    i = letters[n]
    j = letters[n + 1] if n + 1 < len(letters) else len(v)
    m = "".join(VNAMES[ch] for ch in v[i + 1:j] if ch in VNAMES)
    return m or "none"

# ---------------------------------------------------------------- rule definitions
RULES = collections.OrderedDict()   # feature -> dict(desc, fn(corpus, ref, voc, cons, ctx) -> 'old'|'new'|None)

# 1. 3mp suffix ------------------------------------------------------------
PREP = r"(ל|ב|עמ|על|מנ|קדמ|בינ|אחרי|כל|כול|מינ|ית|לות)"
R3_PREP_OLD = re.compile(rf"^(ו|ד|וד|כ)?{PREP}(הומ|המ)$")
R3_PREP_NEW = re.compile(rf"^(ו|ד|וד|כ)?{PREP}(הונ)$")
R3_PL_OLD = re.compile(r"^(.{2,})(יהומ|יהמ)$")
R3_PL_NEW = re.compile(r"^(.{2,})(יהונ)$")
R3_EXCL = {"יהונ", "ויהונ", "דיהונ", "ודיהונ"}   # 'they will be' (impf of hwy), not a suffix (also <2-letter stems anyway)

def f_3mp(corpus, ref, voc, c, ctx):
    if c in R3_EXCL:
        return None
    if R3_PREP_OLD.match(c) or R3_PL_OLD.match(c):
        return "old"
    if R3_PREP_NEW.match(c) or R3_PL_NEW.match(c):
        return "new"
    return None
RULES["3mp suffix"] = dict(fn=f_3mp, desc=(
    "A) ^(ו|ד|וד|כ)?(ל|ב|עמ|על|מנ|קדמ|בינ|אחרי|כל|כול|מינ|ית|לות)(הומ|המ)$ = old, ...(הונ)$ = new; "
    "B) ^(.{2,})(יהומ|יהמ)$ = old, ^(.{2,})יהונ$ = new; excluded verb forms יהון/ויהון/דיהון/ודיהון ('they will be'). "
    "Defective -הן not counted (= 3fp in Targumic Aramaic, and בכן/לכן analogues show the defective spelling is not the 3mp suffix)."))

# 2. 2mp suffix ------------------------------------------------------------
R2_PREP_OLD = re.compile(rf"^(ו|ד|וד|כ)?{PREP}(כומ|כמ)$")
R2_PREP_NEW = re.compile(rf"^(ו|ד|וד|כ)?{PREP}(כונ)$")
R2_PL_OLD = re.compile(r"^(.{2,})(יכומ|יכמ)$")
R2_PL_NEW = re.compile(r"^(.{2,})(יכונ)$")
R2_EXCL = {"יחיכונ"}   # Isa 13:21, 16:10, 34:14 'they will laugh/mock' (verb)

def f_2mp(corpus, ref, voc, c, ctx):
    if c in R2_EXCL:
        return None
    if R2_PREP_OLD.match(c) or R2_PL_OLD.match(c):
        return "old"
    if R2_PREP_NEW.match(c) or R2_PL_NEW.match(c):
        return "new"
    return None
RULES["2mp suffix"] = dict(fn=f_2mp, desc=(
    "A) ^(ו|ד|וד|כ)?(ל|ב|עמ|על|מנ|קדמ|בינ|אחרי|כל|כול|מינ|ית|לות)(כומ|כמ)$ = old, ...(כונ)$ = new; "
    "B) ^(.{2,})(יכומ|יכמ)$ = old, ^(.{2,})יכונ$ = new; excluded יחיכון (verb, Isa 13:21; 16:10; 34:14). "
    "Defective -כן not counted (בכן = 'then')."))

# 3. 3mp independent pronoun ----------------------------------------------
R_PRON_OLD = re.compile(r"^(ו|ד|וד)?(המו|המונ|המ)$")
R_PRON_NEW = re.compile(r"^(ו|ד|וד)?(אנונ|אינונ|אנינ|אינינ)$")
R_PRON_DEM = re.compile(r"^(ו|ד)?ה(אנונ|אינונ|אנינ|אינינ)$")
PRON_EXCL_TYPES = {"המונ"}   # all 10 hits (TJ Isa/1Sam) are Hebrew-loan 'multitude' (hand-checked)

def f_pron(corpus, ref, voc, c, ctx):
    if c in PRON_EXCL_TYPES:
        return None
    if R_PRON_OLD.match(c):
        return "old"
    if R_PRON_NEW.match(c):
        return "new"
    return None
RULES["3mp pronoun"] = dict(fn=f_pron, desc=(
    "^(ו|ד|וד)?(המו|המונ|המ)$ = old; ^(ו|ד|וד)?(אנונ|אינונ|אנינ|אינינ)$ = new. "
    "All המון hits (10, TJ) are 'multitude' and excluded by hand. ה-prefixed האנון/האינון ('those', demonstrative use) not counted, reported in notes."))

# 4. plural demonstrative ---------------------------------------------------
R_DEM = re.compile(r"^(ו|ד|וד|ה|וה|כ|ב|ל|מ|דה)?(אלה|אלכ|אילכ|אלינ|אילינ|אלנ|אילנ)$")
DEM_TREE_OK = {("Targum Jonathan (sample)", "Joshua 17:2"), ("Targum Jonathan (sample)", "Joshua 19:51"),
               ("Targum Onkelos", "Genesis 6:9")}   # bare אילן/אלן = 'these' here; elsewhere 'tree'
DEM_HART = {("Targum Jonathan (sample)", "I Kings 5:3"), ("Targum Jonathan (sample)", "Isaiah 35:6")}  # מאילין/כאילין 'harts'

def f_dem(corpus, ref, voc, c, ctx):
    m = R_DEM.match(c)
    if not m:
        return None
    pfx, stem = m.group(1) or "", m.group(2)
    if stem == "אלה":
        return None          # every hit hand-checked: 'God' (אלה קים, לאלה, אלה שמיא) or the name Elah
    if stem in ("אלכ", "אילכ"):
        return "old"
    if stem in ("אילנ", "אלנ") and "ה" not in pfx:
        return "new" if (corpus, ref) in DEM_TREE_OK else None   # otherwise 'tree'
    if stem == "אילינ" and (corpus, ref) in DEM_HART and pfx in ("מ", "כ"):
        return None
    return "new"
RULES["plural demonstrative"] = dict(fn=f_dem, desc=(
    "^(ו|ד|וד|ה|וה|כ|ב|ל|מ|דה)?(אלה|אלכ|אילכ)$ = old; ...(אלינ|אילינ|אלנ|אילנ)$ = new. "
    "All אלה/לאלה/ואלה hits hand-checked = 'God' or PN Elah -> excluded (so n_old counts only אלך/אילך). "
    "Bare אילן/אלן (no ה-) = 'tree' except Josh 17:2, 19:51, Gen 6:9; מאילין 1Kgs 5:3 and כאילין Isa 35:6 = 'harts', excluded. "
    "ה-prefixed האלין/האילן ('these', attributive) included."))

# 5. relative particle --------------------------------------------------------
R_REL_OLD = re.compile(r"^ו?זי$")
R_REL_NEW = re.compile(r"^ו?די$")
def f_rel(corpus, ref, voc, c, ctx):
    if R_REL_OLD.match(c):
        return "old"
    if R_REL_NEW.match(c):
        return "new"
    return None
RULES["relative particle"] = dict(fn=f_rel, desc=(
    "standalone ^ו?זי$ = old vs ^ו?די$ = new (counts in n_old/n_new). Proclitic ד- estimated separately (see notes)."))

# proclitic d- heuristic (reported in notes only)
ROOT_D = {  # d-initial lexemes whose remainder happens to be an attested word (hand list from frequency review)
    "דמא", "דמ", "דבר", "ודבר", "דברו", "ודברו", "דכי", "דכיא", "דכר", "ודכר", "דכרא", "דכרינ", "דכריא", "דכורא",
    "דרא", "דר", "דרי", "דנ", "ודנ", "דנא", "דננ", "דא", "ודא", "דינ", "ודינ", "דינא", "דיניא", "ודיניא", "דיני", "דינינ",
    "דלמא", "דילמא", "דהבא", "דהב", "ודהבא", "דבש", "ודבש", "דרתא", "דרומא", "דחיל", "ודחיל", "דחילו", "ודחילו", "דחילא",
    "דחלא", "דחלת", "דחלתא", "דחלתי", "דחלינ", "דשא", "דמות", "דמי", "דביר", "דבח", "דיר", "דפא", "דפינ", "דבורה",
    "דגונ", "דמשק", "דמשכ", "דוכ", "דוכא", "דרע", "דרעא", "דקר", "דמע", "דמעא", "דלק", "דליק", "דור", "דרכ", "דרכא",
    "דבק", "דביק", "דקיק", "דקיקא", "דשנ", "דשנא", "דלי", "דליא", "דגלא", "דגל", "דוגא", "דבבא", "דבביכונ", "דבביהונ",
    "דבבוהי", "דבבי", "דבבכ", "דבבנא", "דבבה", "דבבא", "דעת", "דימוס", "דביחא", "דכיר", "דכירינ", "דרגא",
}
R_PROC_D = re.compile(r"^(ו)?ד(.{2,})$")
def is_proclitic_d(c):
    if c in ("די", "ודי") or c in ROOT_D:
        return False
    m = R_PROC_D.match(c)
    return bool(m) and m.group(2) in lexicon

# 6. earth ------------------------------------------------------------------------
R_EARTH = re.compile(r"^(ו|ד|ב|ל|מ|כ|וב|ול|ומ|וכ|וד|דב|דל|דמ|דכ)?(ארע|ארק)(א|ה|יה|י|כ|יכ|כונ|הונ|נא|תא|תנא|תהונ)?$")
EARTH_EXCL = {("Targum Jonathan (sample)", "I Samuel 30:21")}   # וארע = 'and (David) met' (verb)
def f_earth(corpus, ref, voc, c, ctx):
    m = R_EARTH.match(c)
    if not m or ((corpus, ref) in EARTH_EXCL and c == "וארע"):
        return None
    return "old" if m.group(2) == "ארק" else "new"
RULES["'earth'"] = dict(fn=f_earth, desc=(
    "^(ו|ד|ב|ל|מ|כ|וב|ול|ומ|וכ|וד|דב|דל|דמ|דכ)?(ארק|ארע)(א|ה|יה|י|כ|יכ|כונ|הונ|נא|תא|תנא|תהונ)?$ (all forms of the noun incl. suffixed/construct); "
    "ארק = old, ארע = new. Adjectives ארעי(ת)א/ארעאה/ארעית/ארעין 'lower' and verb וארעימו fall outside the suffix set; וארע 1Sam 30:21 (verb 'met') excluded."))

# 7. t-stem prefix ---------------------------------------------------------------
R_T_NEW = re.compile(r"^(ו|ד|וד|ל|ול|דל)?((?:את|אית)[א-ת]{3,}|(?:אשת|אסת|אזד|אצט|אצד)[א-ת]{2,})$")
R_T_OLD = re.compile(r"^(ו|ד|וד|ל|ול|דל)?((?:הת)[א-ת]{3,}|(?:השת|הסת|הזד|הצט)[א-ת]{2,})$")
T_EXCL_PREFIXES = ("אתת", "אתרגוש", "אתרגשות", "אתנסיבות", "אסתלקות", "אשתמודעות", "אצטלו", "אצטלא")
T_EXCL_TYPES = {"איתוהי", "איתיכונ", "איתואיכונ", "איתנא", "אשתיתי", "אשתיתא"}
T_OLD_INTERROG = {"התחבל", "התיזלי", "התקנ", "התקיפ", "התטר", "התצלח", "התמסרינונ", "התחתינני", "התעול",
                  "התיזל", "התיזיל"}   # interrogative ha- + imperfect (hand-checked)
MA_T_EXCL = {"אתיתי", "אתיביה", "איתיאו"}   # MA: 'I came', aphel 'answered him', aphel 'they brought'

def f_t(corpus, ref, voc, c, ctx):
    m = R_T_OLD.match(c)
    if m:
        stem = m.group(2)
        return None if stem in T_OLD_INTERROG else "old"
    m = R_T_NEW.match(c)
    if not m:
        return None
    pfx, stem = m.group(1) or "", m.group(2)
    if stem.startswith(T_EXCL_PREFIXES) or stem in T_EXCL_TYPES:
        return None
    if corpus == "Megillat Antiochus":
        return None if stem in MA_T_EXCL else "new"
    # vocalisation filter: prefix alef must carry hireq (perfect / imperative / infinitive of Ithpe'el/Ithpa'al/Ishtaph'al);
    # removes aphel of t-initial roots (patah), 'come/bring' forms (hateph-patah/qamats/patah), nouns אתר/אתונ (patah),
    # and 1cs imperfects (segol)
    if vowel_on_letter(voc, len(pfx)) != "hireq":
        return None
    return "new"
RULES["t-stem prefix"] = dict(fn=f_t, desc=(
    "Candidates: new ^(ו|ד|וד|ל|ול|דל)?((את|אית)[א-ת]{3,}|(אשת|אסת|אזד|אצט|אצד)[א-ת]{2,})$; old same with הת / השת|הסת|הזד|הצט. "
    "New candidates kept only if the prefix aleph is vocalised with hireq (Targums; MA classified by hand), and minus nouns/existentials "
    "(אתת- 'wife', אתרגוש- 'tumult', איתוהי/איתיכון 'he is/you are', אסתלקות, אצטלון 'robes', אשתיתי 'I drank'). "
    "Old candidates: all are interrogative ha- + imperfect except להתנבאה (Judg 5:7)."))

# 8. causative prefix --------------------------------------------------------------
APHEL_FORMS = {
    "נפק 'bring out'": ["אפיק", "אפיקו", "אפיקית"],
    "סלק 'bring up'": ["אסיק", "אסיקו", "אסיקית", "אסקו", "אסקית"],
    "עלל 'bring in'": ["אעיל", "אעילו", "אעילית"],
    "אתי 'bring'": ["אייתי", "אייתיו", "אייתיאו", "אייתית", "איתי", "איתיו", "איתיאו", "איתית", "איתיאת"],
    "ידע 'make known'": ["אודע", "אודעו", "אודעית"],
    "יסף 'add'": ["אוסיפ", "אוסיפו", "אוסיפית"],
    "קום 'raise'": ["אקימ", "אקימו", "אקימית"],
    "חזי 'show'": ["אחזי", "אחזיו", "אחזיאו"],
    "תוב 'return'": ["אתיב", "אתיבו", "אתיבית"],
    "שכח 'find'": ["אשכח", "אשכחו", "אשכחית"],
    "כרז 'proclaim'": ["אכריז", "אכריזו"],
    "עדי 'remove'": ["אעדי", "אעדיו", "אעדיאו", "אעדיאת"],
    "גלי 'exile/reveal'": ["אגלי", "אגליו", "אגליאו"],
    "שני 'change'": ["אשני", "אשניו", "אשניאו"],
    "יקד 'burn'": ["אוקיד", "אוקידו"],
    "גיח 'wage (war)'": ["אגיח", "אגיחו"],
    "יבל 'carry'": ["אוביל", "אובילו"],
}
HAPHEL_EXTRA = ["הנפק", "הנפיק", "הנפקו", "הנפיקו", "הנסק", "הנסיק", "הנעל", "הנעיל", "הנעלו", "הכרז", "הכרזו",
                "היבל", "היבלו", "השכחת"]
APHEL = set(f for fs in APHEL_FORMS.values() for f in fs)
HAPHEL = set("ה" + f[1:] for f in APHEL) | set(HAPHEL_EXTRA)
R_CAUS = re.compile(r"^(ו|ד|וד)?(.+)$")
def f_caus(corpus, ref, voc, c, ctx):
    m = R_CAUS.match(c)
    for pfx, stem in ((m.group(1) or "", m.group(2)), ("", c)):
        if stem in HAPHEL:
            return "old"
        if stem in APHEL:
            # drop peal/other 1cs imperfects: aleph with segol/tsere (e.g. אֶחֱזֵי 'I will see', אֶסַּק, וְאֵתֵיב 'I will sit')
            if vowel_on_letter(voc, len(pfx)) in ("segol", "tsere"):
                return None
            return "new"
    return None
RULES["causative prefix"] = dict(fn=f_caus, desc=(
    "Explicit list, optional proclitic ו/ד/וד. Aphel (new): " +
    "; ".join(f"{k}: {', '.join(v)}" for k, v in APHEL_FORMS.items()) +
    ". Haphel (old): the same forms with initial ה instead of א (הפיק, הסיק, העיל, היתי, הודע, הוסיף, הקים, החזי, התיב, השכח, ...) "
    "plus " + ", ".join(HAPHEL_EXTRA) + ". Aphel tokens whose aleph has segol/tsere (peal 1cs imperfects) dropped."))

# ---------------------------------------------------------------- run
hits = collections.defaultdict(list)    # (feature, corpus, side) -> list of (ref, voc, cons, context)
proc_d = collections.defaultdict(list)
dem_those = collections.Counter()
for (corpus, ref), toks in verses.items():
    for i, (voc, c) in enumerate(toks):
        ctx = " ".join(t[1] for t in toks[max(0, i - 4):i]) + " [" + c + "] " + " ".join(t[1] for t in toks[i + 1:i + 5])
        for feat, r in RULES.items():
            side = r["fn"](corpus, ref, voc, c, ctx)
            if side:
                hits[(feat, corpus, side)].append((ref, voc, c, ctx))
        if is_proclitic_d(c):
            proc_d[corpus].append((ref, voc, c, ctx))
        if R_PRON_DEM.match(c):
            dem_those[corpus] += 1

# ---------------------------------------------------------------- notes per cell
def abbrev(ref):
    return (ref.replace("Genesis", "Gen").replace("Exodus", "Exod").replace("Leviticus", "Lev").replace("Numbers", "Num")
            .replace("Deuteronomy", "Deut").replace("Joshua", "Josh").replace("Judges", "Judg").replace("II Samuel", "2Sam")
            .replace("I Samuel", "1Sam").replace("II Kings", "2Kgs").replace("I Kings", "1Kgs").replace("Isaiah", "Isa"))

def examples(lst, n=8):
    # spread examples through the corpus
    if not lst:
        return "none"
    step = max(1, len(lst) // n)
    sel = lst[::step][:n]
    return "; ".join(f"{abbrev(r)} {c}" for r, v, c, x in sel)

def types_summary(lst, n=6):
    cnt = collections.Counter(c for r, v, c, x in lst)
    return ", ".join(f"{k} {v}" for k, v in cnt.most_common(n))

extra = collections.defaultdict(str)
verses_by_corpus = collections.defaultdict(list)
for (corpus, ref), toks in verses.items():
    verses_by_corpus[corpus].append([c for v, c in toks])
for corpus in CORPORA:
    nd = len(proc_d[corpus])
    extra[("relative particle", corpus)] = (
        f"Proclitic ד- (heuristic: ^(ו)?ד(.{{2,}})$ whose remainder is an attested word in the combined corpora, minus a stop-list of ד-initial lexemes): "
        f"~{nd} tokens; proclitic ז- not attested. ")
    n_yt3 = sum(1 for x in hits[("3mp suffix", corpus, "new")] if re.match(r"^(ו|ד|וד)?יתהונ$", x[2]))
    n_yt2 = sum(1 for x in hits[("2mp suffix", corpus, "new")] if re.match(r"^(ו|ד|וד)?יתכונ$", x[2]))
    n_pl3 = sum(1 for x in hits[("3mp suffix", corpus, "new")] if not R3_PREP_NEW.match(x[2]))
    n_pl2 = sum(1 for x in hits[("2mp suffix", corpus, "new")] if not R2_PREP_NEW.match(x[2]))
    extra[("3mp suffix", corpus)] = f"Of n_new: object marker יתהון {n_yt3}; via rule B (-יהון not in prep list) {n_pl3}. -הם/-הום anywhere in the three corpora: only names (אברהם, כמהם, הוהם), תהום, וינהום. "
    extra[("2mp suffix", corpus)] = f"Of n_new: object marker יתכון {n_yt2}; via rule B (-יכון not in prep list) {n_pl2}. No -כם/-כום suffix anywhere (only שכם, סכום, חכם etc.). "
    extra[("3mp pronoun", corpus)] = f"ה-prefixed האנון/האינון ('those') not counted: {dem_those[corpus]} tokens. "
    n_dinit = sum(1 for toks in verses_by_corpus[corpus] for c in toks if re.match(r"^ו?ד", c) and c not in ("די", "ודי"))
    extra[("relative particle", corpus)] += (
        f"Upper bound (all ו?ד-initial tokens except די/ודי): {n_dinit}. "
        + ("Hand-check (Onk+TJ pooled): 148/150 sampled heuristic hits are proclitic (FP ודברית, דרום); "
           "21/100 sampled untagged ד-initial tokens are in fact proclitic, so the heuristic undercounts by roughly 10%. "
           if corpus != "Megillat Antiochus" else "MA not hand-sampled. "))
    if corpus != "Megillat Antiochus":
        extra[("t-stem prefix", corpus)] = (
            "Hand-check of 200 random new hits (Onk+TJ pooled): 195 are Ithpe'el/Ithpa'al/Ishtaph'al perfect/imperative/infinitive; "
            "5 are 1cs imperfects vocalised with hireq (Gen 18:21, 24:49, Num 23:15, Judg 16:28, Isa 49:25). Recall loss from the hireq filter small (some 20 perfects with odd vocalisation). ")
        extra[("causative prefix", corpus)] = (
            "Hand-check of 80 random new hits (Onk+TJ pooled): 63 perfects, 17 imperatives or 1cs imperfects (consonantally identical aphel forms; "
            "haphel 1cs impf would be אה-, not counted on old side). ")
    else:
        extra[("t-stem prefix", corpus)] = "All MA candidates classified by hand (vocalisation partial): excluded אתיתי x2 'I came', אתיביה (aphel), איתיאו x2 (aphel), ואתתיה 'his wife'. "
        extra[("causative prefix", corpus)] = ("Old = הנפיק (MA 21). Other ה-causatives in MA outside the verb list: הועל (17, hophal), מהחצפא (33, haphel ptc.), "
                                              "להודעא x2 (72, haphel inf.); other א-causatives outside the list: ואצדי (2), ואלבשינך/וארכבינך (19), אתיביה (20), לאדלקא x2 (69, 72), ואדליקו (70). "
                                              "ואגיח MA 60 is a 1cs impf. ")

rows = []
for feat, r in RULES.items():
    for corpus in CORPORA:
        o = hits[(feat, corpus, "old")]
        nw = hits[(feat, corpus, "new")]
        note = (extra[(feat, corpus)] +
                f"old types: {types_summary(o) or 'none'}; new types: {types_summary(nw) or 'none'}. "
                f"ex old: {examples(o)} | ex new: {examples(nw)}")
        rows.append(dict(feature=feat, corpus=corpus, n_old=len(o), n_new=len(nw), words=words[corpus], notes=note))

with open(os.path.join(OUT, "late_aramaic_features.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["feature", "corpus", "n_old", "n_new", "words", "notes"])
    w.writeheader()
    for row in rows:
        w.writerow(row)

with open(os.path.join(OUT, "audit_hits.tsv"), "w", encoding="utf-8") as f:
    f.write("feature\tcorpus\tside\tref\tvocalised\tconsonantal\tcontext\n")
    for (feat, corpus, side), lst in hits.items():
        for ref, voc, c, ctx in lst:
            f.write(f"{feat}\t{corpus}\t{side}\t{ref}\t{voc}\t{c}\t{ctx}\n")
    for corpus, lst in proc_d.items():
        for ref, voc, c, ctx in lst:
            f.write(f"relative particle (proclitic d- heuristic)\t{corpus}\tnew\t{ref}\t{voc}\t{c}\t{ctx}\n")

with open(os.path.join(OUT, "matching_rules.txt"), "w", encoding="utf-8") as f:
    f.write("Normalisation: NFD; strip HTML tags; delete (...) variant/additions and [...] editorial supplements (stateful across verses); "
            "maqaf/paseq/sof-pasuq -> space; delete U+0591-U+05C7 marks; keep only U+05D0-U+05EA; final letters ךםןףץ -> כמנפצ.\n\n")
    for feat, r in RULES.items():
        f.write(f"{feat}: {r['desc']}\n\n")

# hand-check samples
random.seed(20261124)
for name, pool in (("sample_tstem.tsv", [x for corpus in CORPORA[:2] for x in hits[("t-stem prefix", corpus, "new")]]),
                   ("sample_procd.tsv", [x for corpus in CORPORA[:2] for x in proc_d[corpus]]),
                   ("sample_caus.tsv", [x for corpus in CORPORA[:2] for x in hits[("causative prefix", corpus, "new")]])):
    k = {"sample_tstem.tsv": 200, "sample_procd.tsv": 150, "sample_caus.tsv": 80}[name]
    smp = random.sample(pool, min(k, len(pool)))
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        for i, (ref, voc, c, ctx) in enumerate(smp, 1):
            f.write(f"{i}\t{ref}\t{voc}\t{ctx}\n")

for row in rows:
    print(row["feature"], "|", row["corpus"], "|", row["n_old"], row["n_new"], row["words"])
print({c: len(v) for c, v in proc_d.items()})
