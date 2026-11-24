"""Feature classification on normalised consonantal forms (final letters -> medial).
classify(form, raw) -> list of (feature, variant). Curated lists live in curation/*.tsv."""
import re, os, csv
HERE = os.path.dirname(os.path.abspath(__file__))
CUR = os.path.join(os.path.dirname(HERE), "curation")

def load(name):
    d = {}
    p = os.path.join(CUR, name)
    if os.path.exists(p):
        for row in csv.reader(open(p, encoding="utf-8"), delimiter="\t"):
            if row and not row[0].startswith("#") and len(row) >= 2:
                d[row[0]] = row[1]
    return d

CAUS = load("causative.tsv")      # form -> H / A / no
REFL = load("reflexive.tsv")      # form -> HT / AT / no
SFX_EXCL = load("suffix_exclude.tsv")  # form -> reason (not a pronominal suffix)
KH = load("sfx2ms_kh.tsv")        # form -> yes/no (ends in -כה: is it 2ms suffix?)

PRON3MP = {"המ": "המ", "והמ": "המ", "המו": "המו", "והמו": "המו", "המונ": "המונ", "והמונ": "המונ",
           "אנונ": "אנונ", "ואנונ": "אנונ", "אנינ": "אנינ", "ואנינ": "אנינ", "הומ": "הומ (pron.)", "הונ": "הונ (pron.)"}

def strip_w(f):
    return f[1:] if f.startswith("ו") and len(f) > 2 else f

def procl(f, allowed="בלכמ"):
    """yield stems after optional ו and optional one proclitic from allowed."""
    out = {f}
    g = strip_w(f)
    out.add(g)
    for h in list(out):
        if len(h) > 2 and h[0] in allowed:
            out.add(h[1:])
    return out

DEM_PL = {"אלה": "אלה", "אלכ": "אלכ/אלכי", "אלכי": "אלכ/אלכי", "אלכה": "אלכ/אלכי", "אלנ": "אלנ/אלינ", "אלינ": "אלנ/אלינ", "אל": "אל (ambiguous)"}
REL_Z = {"זי", "כזי", "בזי", "לזי", "מזי", "עדזי"}
REL_D = {"די", "כדי", "בדי", "לדי", "מדי", "עדדי"}
THIS_M = {"זנה": "זנה", "דנה": "דנה"}
THIS_F = {"זא": "זא", "דא": "דא", "דה": "דה", "זה": "זה (?)"}
THAT = {"זכ": "זכ", "זכה": "זכ", "זכי": "זכי (dem. or 'innocent')", "דכ": "דכ", "דכה": "דכ", "דכנ": "דכנ", "דכנה": "דכנ", "זכנ": "זכנ"}
PREP2MS_K = {"לכ", "בכ", "עמכ", "מנכ", "עליכ", "עלכ", "קדמיכ", "קדמכ", "יתכ", "לותכ", "תחתיכ"}
PREP2MS_KH = {w + "ה" for w in PREP2MS_K}
OBJ = {"ית": "ית", "יתה": "ית+sfx", "יתהמ": "ית+sfx", "יתהומ": "ית+sfx", "יתהונ": "ית+sfx", "יתי": "ית+sfx", "יתנ": "ית+sfx",
       "יתכ": "ית+sfx", "יתכמ": "ית+sfx", "יתכונ": "ית+sfx", "יות": "יות"}
PRON2MS = {"אנת": "אנת", "אנתה": "אנתה"}
PRON1CP = {"אנחנה": "אנחנה", "אנחנא": "אנחנא", "אנחנ": "אנחנ", "אנחננ": "אנחננ"}
BEHOLD = {"הלו": "הלו", "אלו": "אלו", "ארו": "ארו"}
NOW = {"כענ": "כענ", "כענת": "כענת", "כעת": "כעת"}
BE_IMPF = {"יהוה": "y-", "יהוא": "y-", "יהוונ": "y-", "יהוו": "y-", "תהוה": "t-", "תהוא": "t-", "תהוונ": "t-", "להוה": "l-", "להוא": "l-", "להוונ": "l-", "לתהוונ": "l-"}
NAMES_ZKR = {"זכריה", "זכור", "וזכריה", "לזכריה", "זכורי", "בזכריה", "זכריהו"}

def classify(form, raw=""):
    res = []
    f = form
    w = strip_w(f)
    # F4 independent 3mp pronoun
    if f in PRON3MP:
        res.append(("F4_pron3mp", PRON3MP[f]))
    # F1 3mp / 2mp suffix
    elif SFX_EXCL.get(f) == "verb":
        for suf in ("הומ", "הונ", "המ", "כונ", "כמ"):
            if f.endswith(suf):
                res.append(("F1c_verbal_obj_sfx", "-" + suf)); break
    elif f not in SFX_EXCL:
        if f.endswith("הומ") and len(f) > 3:
            res.append(("F1a_sfx3mp", "-הומ"))
        elif f.endswith("הונ") and len(f) > 3:
            res.append(("F1a_sfx3mp", "-הונ"))
        elif f.endswith("המ") and len(f) > 2:
            res.append(("F1a_sfx3mp", "-המ"))
        if f.endswith("כונ") and len(f) > 3:
            res.append(("F1b_sfx2mp", "-כונ"))
        elif f.endswith("כמ") and len(f) > 2:
            res.append(("F1b_sfx2mp", "-כמ"))
    # F2 causative (curated)
    c = CAUS.get(f)
    if c in ("H", "A"):
        res.append(("F2_causative", {"H": "h- (haphel)", "A": "ʾ- (aphel)"}[c]))
    r = REFL.get(f)
    if r in ("HT", "AT"):
        res.append(("F3_reflexive", {"HT": "ht- (hitpe/aal)", "AT": "ʾt- (itpe/aal)"}[r]))
    # F5 plural demonstrative
    for s in procl(f, "כבלמ"):
        if s in DEM_PL:
            res.append(("F5_demPl", DEM_PL[s])); break
    # F6 relative
    if w in REL_Z:
        res.append(("F6_rel", "זי"))
    elif w in REL_D:
        res.append(("F6_rel", "די"))
    if re.match(r"^ו?(ב|ל|כ)?זיל", f):
        res.append(("F6b_possessive", "זיל-"))
    elif re.match(r"^ו?(ב|ל|כ)?דיל", f):
        res.append(("F6b_possessive", "דיל-"))
    # F7 earth
    for s in procl(f, "בלמכ"):
        m = re.match(r"^(ארק|ארע)(א|ה|נ|תא|ת|י|כ|הומ|הונ|המ|הא)?$", s)
        if m:
            res.append(("F7_earth", m.group(1))); break
    # F8 2ms suffix on prepositions
    if w in PREP2MS_K:
        res.append(("F8_sfx2ms_prep", "-כ"))
    elif w in PREP2MS_KH:
        res.append(("F8_sfx2ms_prep", "-כה"))
    elif f.endswith("כה") and KH.get(f) == "yes":
        res.append(("F8b_sfx2ms_other_kh", "-כה (noun/verb)"))
    # F9 *ḏ words
    for s in procl(f, "בלכמ"):
        if s in THIS_M:
            res.append(("F9a_this_m", THIS_M[s])); break
    for s in procl(f, "בלכמ"):
        if s in THIS_F:
            res.append(("F9b_this_f", THIS_F[s])); break
    for s in procl(f, "בלכמ"):
        if s in THAT:
            res.append(("F9c_that", THAT[s])); break
    for s in procl(f, "בלכמ"):
        m = re.match(r"^(זהב|דהב)(א|ה)?$", s)
        if m:
            res.append(("F9d_gold", m.group(1))); break
    if f not in NAMES_ZKR:
        for s in procl(f, "בלכמ"):
            m = re.match(r"^(י|ת|נ|א|ה|מ)?(זכר|דכר)", s)
            if m and not re.match(r"^ו?(זכרי|זכור)", s):
                res.append(("F9e_zkr_dkr", m.group(2))); break
    for s in procl(f, "בלכ"):
        m = re.match(r"^(מ)(זבח|דבח)", s)
        if m:
            res.append(("F9g_altar", "מ" + m.group(2))); break
        m = re.match(r"^(י|ת|נ|מ)?(זבח|דבח)", s)
        if m:
            res.append(("F9f_zbh_dbh", m.group(2))); break
    # F10 object marker
    if w in OBJ:
        res.append(("F10_objmark", OBJ[w]))
    # F11 extras
    if w in PRON2MS: res.append(("F11a_pron2ms", PRON2MS[w]))
    if w in PRON1CP: res.append(("F11b_pron1cp", PRON1CP[w]))
    if w in BEHOLD: res.append(("F11c_behold", BEHOLD[w]))
    if w in NOW: res.append(("F11d_now", NOW[w]))
    if w in BE_IMPF: res.append(("F11e_impf_hwy_prefix", BE_IMPF[w]))
    return res
