# Earliest physical and external attestations of the Hebrew prophetic books: dating data

Compiled 2026-11-24. This file holds catalogue data only (manuscript dates, radiocarbon results, dated external texts). It makes no claims about the authors' intent. Row-level data, with URLs for every manuscript, are in `manuscript_dates.csv` (115 rows).

## Conventions and source key

| key | source | what it gives |
|---|---|---|
| **IAA** | Leon Levy DSS Digital Library (IAA), the `period` field of each record, read from the record page `deadseascrolls.org.il/explore-the-archive/manuscript/<ID>-1` | a coarse script period only (Early Hellenistic / Hasmonean / Herodian / Hellenistic-Roman / Roman), plus the DJD reference |
| **W** | B. Webster, "Chronological Index of the Texts from the Judaean Desert", DJD XXXIX (2002), as quoted in E. Tov, *Scribal Practices and Approaches* (2004), the author's PDF at emanueltov.info | the editors' (DJD) palaeographic date. In Tov's App. 1 these are recorded as **midpoints** of Webster's range ("b 37" = midpoint 37 BCE). Elsewhere Tov quotes the ranges themselves (Tables 27, 16; pp. 158, 207; n. 296) |
| **P25** | Popović, Dhali, Schomaker et al., "Dating ancient manuscripts using radiocarbon and AI-based writing style analysis", *PLOS ONE* 2025, doi:10.1371/journal.pone.0323185, with appendices S2 (Table S1), S4, S7 (Table S11) and S12 | new AMS dates (Groningen; IntCal20; samples cleaned of castor oil); earlier palaeographic dates quoted from DJD; the authors' own palaeographic ranges; "Enoch" AI estimates |
| **B92** | Bonani et al., *Radiocarbon* 34 (1992) 843–849, Table 1 | ETH Zürich AMS dates, 1σ calibration |
| **J95** | Jull et al., *Radiocarbon* 37 (1995) 11–19, Table 2 | Arizona AMS dates, 1σ and 2σ calibration |
| **R20** | my recalibration of the 1990s BP values against IntCal20 (Reimer et al. 2020), using a simple probability method with HPD ranges rounded to 5 years. It reproduces P25's published ranges to within ±5 years and about 1 percentage point | makes the 1990s and 2025 dates comparable |
| **WP** | Wikipedia, used **only as a fallback** where no primary or scholarly source was reachable; each such use is marked | |

Ranges are 2σ (95.4%) unless marked 1σ. A radiocarbon date dates the preparation of the skin or papyrus, not the act of copying. The palaeographic dates are relative typological estimates (P25 S1 discusses the lack of dated comparanda for 300 BCE–100 CE).

## 1. Summary: earliest dated copy and strongest external terminus, by book

| book | earliest dated copy | strongest external terminus (dated text that names or quotes the book) |
|---|---|---|
| **Isaiah** (all of 1–66) | **1QIsaᵃ**. Palaeographic date 150–100 BCE (Cross 125–100; J95 and Tov 150–125; P25 175–125). Two radiocarbon runs (ETH 2128±38 BP, AA 2141±32 BP); R20 combined, 2σ: **205–90 BCE (74%)**, 345–315 (13%), 80–50 (8%) | Ben Sira 48:20–25 names Isaiah, and 48:24–25 uses the wording of Isa 40:1 / 61:2–3 and 42:9 / 46:10 / 48:6. Composed about 196–175 BCE (Simon II anchor, §5). The Greek translation is dated 132 BCE to about 116 BCE. The Hebrew survives only in medieval MS B |
| **Jeremiah** | **4Q70 (4QJerᵃ)**. Radiocarbon 2226±17 BP: **320–200 BCE (79.2%)** or 375–345 BCE (16.3%). Palaeographic date 225–175 BCE (Tov, DJD XV 150) | Ben Sira 49:6–7 quotes Jer 1:5, 10. Eupolemus fr. 4 (Jeremiah under "Jonachim"); his chronology ends in 158/157 BCE |
| **Ezekiel** | **4Q73 (4QEzekᵃ)**. Webster 50–25 BCE; P25 palaeographers 100–50 BCE; no radiocarbon date. 4Q75 is labelled "Hasmonean" by the IAA but has no finer date | Ben Sira 49:8 (the chariot vision; about 196–175 BCE). **4Q391** papPseudo-Ezekielᵉ, a copy of a work that presupposes Ezekiel: Webster 150–100 BCE |
| **Twelve Prophets** | **4Q76 (4QXIIᵃ)**: "around 150 BCE" (Fuller 1996); P25 175–125 BCE. 4Q77 (4QXIIᵇ): around 150 BCE | Ben Sira 49:10, "the twelve prophets" (שנים עשר הנביאים), about 196–175 BCE. 8ḤevXIIgr (end of the 1st c. BCE) is a revision of an existing Greek Twelve |
| **Daniel** | **4Q114 (4QDanᶜ)**. Radiocarbon 2168±15 BP: **230–160 BCE (45.9%)** or 355–285 BCE (49.5%); the authors reject the older peak on typological grounds. Palaeographic date 125–100 BCE (Ulrich, DJD XVI 270, following Cross) | 1 Macc 1:54 uses OG Dan 11:31's phrase βδέλυγμα ἐρημώσεως, and 1 Macc 2:59–60 names Hananiah, Azariah, Mishael and Daniel. 1 Macc was composed after John Hyrcanus became high priest (16:23–24; 134 BCE). 4Q174 cites "the book of Daniel the prophet" (copy late 1st c. BCE). Daniel is **not** named in Ben Sira 44–50 |
| **Kings** | 5Q2 and 6Q4 (papyrus): IAA "Hasmonean"; no finer date found | Demetrius the Chronographer reckons the Sennacherib and Nebuchadnezzar captivities down to Ptolemy IV (221–204 BCE); Ben Sira 48:17–21 (Hezekiah, Sennacherib, Rabshakeh) |

## 2. Judaean Desert manuscripts (sigla as in ETCBC/Abegg; contents from the ETCBC DSS 2.0.5 book/chapter features)

### Isaiah
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 1Qisaa | 1QIsaᵃ | Isa 1–66 | 125–100 BCE (W midpoint 112; Cross in B92); 150–125 (J95; Tov 2008); 175–125 (P25). Radiocarbon: see §3 | W, B92, J95, P25 |
| 1Q8 | 1QIsaᵇ | Isa 7–66 (mainly 38–66) | "first century BCE" (Tov 2008); IAA Herodian | Tov 2008, IAA |
| 4Q55 | 4QIsaᵃ | 1–2,4–6,11–13,17,19–23,33 | W midpoint 37 BCE (≈50–25 BCE); IAA Hasmonean | W, IAA |
| 4Q56 | 4QIsaᵇ | 1–66 scattered | third quarter of the 1st c. BCE (DJD XV, quoted by Tov 2004 p. 86); IAA Herodian | Tov 2004, IAA |
| 4Q57 | 4QIsaᶜ | 9–14,22–26,…,66 | W midpoint 50 CE; P25 1–50 CE; IAA Herodian | W, P25 |
| 4Q58 | 4QIsaᵈ | 45–49,52–54,57–58 | W midpoint 50 CE; P25 1–50 CE; IAA Herodian | W, P25 |
| 4Q59 | 4QIsaᵉ | 2,7–14,59 | IAA Herodian | IAA |
| 4Q60 | 4QIsaᶠ | 1–2,5–8,20–29 | IAA Hasmonean | IAA |
| 4Q61 | 4QIsaᵍ | 42–43 | W midpoint 25 BCE; IAA Herodian | W |
| 4Q62 | 4QIsaʰ | 42 | W midpoint 75 BCE; IAA Hasmonean | W |
| 4Q62a | 4QIsaⁱ | 56–57 | none found (no separate IAA record) | – |
| 4Q63–4Q68 | 4QIsaʲ⁻ᵒ | 1; 28–29; 7–8; 60–61; 58; 14–15 | IAA: j Herodian; k, l, m, n, o Hasmonean | IAA |
| 4Q69 | 4QpapIsaᵖ | 5 | IAA Hasmonean | IAA |
| 4Q69a, 4Q69b | 4QIsaᵠ, 4QIsaʳ | 54; 30 | none found (no IAA record) | – |
| 5Q3 | 5QIsa | 40 | IAA Herodian | IAA |
| Mur3 | MurIsa | 1 | 20–84 CE (W, Tov 2004 Table 27); IAA Roman | W |

### Jeremiah
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 2Q13 | 2QJer | 42–44,46–49 | IAA Herodian | IAA |
| 4Q70 | 4QJerᵃ | 6–15,17–22,26 | 225–175 BCE (Tov, DJD XV 150, quoting Yardeni and Cross); W midpoint 200 BCE; IAA "Early Hellenistic". Radiocarbon: §3 | P25 S12, W, IAA |
| 4Q71 | 4QJerᵇ | 9–10 | first half of the 2nd c. BCE (Tov 1999, citing DJD XV); IAA Hasmonean. Short, LXX-like text | Tov 1999 |
| 4Q72 | 4QJerᶜ | 4,8–10,19–33 | 30–1 BCE (W, Tov 2004 Table 27). The IAA record "4Q72-1" (labelled copy "d", "Early Hellenistic") contradicts this; treat the IAA label as unreliable | W |
| 4Q72a | 4QJerᵈ | 43 | W midpoint 175 BCE; first half of the 2nd c. BCE (Tov 1999) | W, Tov 1999 |
| 4Q72b | 4QJerᵉ | 50 | none found (formerly part of "4QJerᵇ") | – |

### Ezekiel
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 1Q9 | 1QEzek | 4–5 | IAA Hellenistic-Roman | IAA |
| 3Q1 | 3QEzek | 16 | IAA Herodian | IAA |
| 4Q73 | 4QEzekᵃ | 10–11,23,41 | 50–25 BCE (W, Table 27); P25 100–50 BCE (they "expect ca. 100 or 75 BCE"); IAA Hasmonean | W, P25 |
| 4Q74 | 4QEzekᵇ | 1 | IAA Herodian | IAA |
| 4Q75 | 4QEzekᶜ | 24 | IAA Hasmonean | IAA |
| 11Q4 | 11QEzek | 1,4–5,7 | IAA Herodian | IAA |
| Mas1d | MasEzek | 35–38 | 50–1 BCE (W, Table 27); Masada fell 73/74 CE | W |

### Twelve Prophets
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 4Q76 | 4QXIIᵃ | Zech 14; Mal 2–3; Jonah 1–3 | "around 150 BCE" (Fuller 1996, *Forming Prophetic Literature* 91–92, quoted by Guillaume, *JHS* 7.15, 2007); P25 175–125 BCE; Enoch 190–150 BCE; IAA Hasmonean | Fuller/Guillaume, P25 |
| 4Q77 | 4QXIIᵇ | Zeph 1–3; Hag 1–2 | around 150 BCE (Fuller 1996); IAA Hasmonean | Fuller/Guillaume |
| 4Q78 | 4QXIIᶜ | Hos, Joel, Amos, Zeph, Mal 3 | W midpoint 75 BCE; IAA Hasmonean | W |
| 4Q79 | 4QXIIᵈ | Hos 1–2 | IAA Hasmonean | IAA |
| 4Q80 | 4QXIIᵉ | Hag 2; Zech 1–12 | W midpoint 62 BCE; IAA Hasmonean | W |
| 4Q81 | 4QXIIᶠ | Jonah 1–2; Mic 5 | IAA Hasmonean | IAA |
| 4Q82 | 4QXIIᵍ | Hos through Zech | Herodian bookhand, last third of the 1st c. BCE (Lange, *Textus* 26, 2016, citing Fuller DJD XV); W midpoint 18 BCE | Lange, W |
| 5Q4 | 5QAmos | Amos 1 | IAA record has no period | – |
| Mur88 | MurXII | Joel through Zech 1 | c. 115 CE (W, Table 27); P25 25–75 CE. Radiocarbon attempted in 2025 and **rejected** (inconsistent runs) | W, P25 |
| 8Hev1 | 8ḤevXIIgr | Greek: Jonah, Mic, Nah, Hab, Zeph, Zech | end of the 1st c. BCE (Tov, DJD VIII; Tov 2004 App. 5); IAA Roman | Tov |

### Daniel
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 1Q71 / 1Q72 | 1QDanᵃ / 1QDanᵇ | 1–2 / 3 (Aramaic) | IAA Hellenistic-Roman (no finer date found) | IAA |
| 4Q112 | 4QDanᵃ | 1–5,7–8,10–11 | W midpoint 50 BCE; IAA Hasmonean | W |
| 4Q113 | 4QDanᵇ | 5–8 | IAA Herodian | IAA |
| **4Q114** | **4QDanᶜ** | 10:5–11:29 | 125–100 BCE, "no more than about a half century younger than the autograph" (Ulrich, DJD XVI 270, after Cross). Cross had varied between 125–100 BCE, c. 100–50 BCE and the late 2nd c. (P25 S4). IAA Hasmonean. Radiocarbon: §3 | P25 S12/S4 |
| 4Q115 | 4QDanᵈ | 3–4,7 | IAA Herodian | IAA |
| 4Q116 | 4QDanᵉ | 9 | IAA Hasmonean | IAA |
| 6Q7 | 6QpapDan | 8,10–11 | IAA Herodian | IAA |

### Kings
| siglum | name | contents | date | source |
|---|---|---|---|---|
| 4Q54 | 4QKgs | 1 Kgs 7–8 | IAA Herodian | IAA |
| 5Q2 | 5QKgs | 1 Kgs 1 | IAA Hasmonean | IAA |
| 6Q4 | 6QpapKgs | 1 Kgs 3,12,22; 2 Kgs 5–10 | IAA Hasmonean | IAA |

No finer date was found in accessible sources for the rows marked "IAA" only. The DJD editions (DJD I, III, XIV, XV, XVI, XXIII) contain them but are not openly accessible.

## 3. Radiocarbon determinations relevant to the prophets

| MS | lab no. | ¹⁴C age BP | published calibration | IntCal20 (P25 or R20) | palaeographic date at the time |
|---|---|---|---|---|---|
| 1QIsaᵃ | ETH-6651/6813 (B92) | 2128±38 | 1σ 335–327 BC (5%), 202–107 BC (95%) | R20: 350–290 (14.5%), 210–45 BCE (80.5%) | 125–100 BC |
| 1QIsaᵃ | AA-14984 (J95) | 2141±32 | 2σ 356–291 (24%), 250–103 BC (76%) | R20: 350–290 (20.4%), 210–50 BCE (74.8%) | 150–125 BC |
| 1QIsaᵃ combined | – | 2136±24 (χ²=0.07) | – | R20: 345–315 (13.3%), **205–90 (74.4%)**, 80–50 BCE (7.8%) | – |
| 4Q70 4QJerᵃ | GrM-11151/52, 11170/71 (P25) | 2226±17 | – | 375–345 (16.3%), **320–200 BCE (79.2%)** | 225–175 BCE |
| 4Q114 4QDanᶜ | GrA-69795 + GrM-13252..55, 7 runs (P25) | 2168±15 | 1σ 345–315, 205–175 BCE | 355–285 (49.5%), **230–160 BCE (45.9%)** ("accepted") | 125–100 BCE |
| 1QpHab | AA-13417 (J95) | 2054±22 | 2σ 153–143 (3%), 120–5 BC (97%) | R20: 150–130 (4%), **120 BCE–20 CE (91.5%)** | 30–1 BC (Cross) |
| 4Q161 4QpIsaᵃ | GrA-69810, GrM-10661/62 (P25) | 2028±18 | – | 90–80 (1.7%), **55 BCE–30 CE (92.1%)**, 45–60 CE (1.7%) | 30 BCE–20 CE (Yardeni) |
| 4Q266 4QDᵃ | AA-13415 (J95) | 1954±38 | 2σ 45 BC–AD 120 | R20: 40–10 BCE (8%), **1–170 CE (85%)** | 100–50 BC |
| 4Q267 4QDᵇ | AA-13422 (J95) | 2094±29 | 2σ 194–45 BC | 200–40 BCE (94.0%) (P25 S4) | 50–0 BC; DJD 30 BCE–20 CE |
| 4Q267 4QDᵇ | GrM-13393/94, 14226/27 (P25) | 2151±21 | – | 355–290 (28.6%), **210–95 (65.3%)**, 70–55 BCE (1.6%) | 30 BCE–20 CE |
| Mur88 MurXII | GrA-69806, GrM-10663/64, 18829/30 | – | rejected: the runs disagree | – | c. 115 CE |

Notes:
- P25's "accepted" ranges for bimodal results drop the older peak "based on comparative typological evidence". For 4Q114 the radiocarbon result alone puts roughly half its probability in 355–285 BCE. Either way the 2σ ceiling is 160 BCE.
- The 4Q70 sample was a fragment that had not been identified when sampled; it was later identified as 4Q70 (P25 S2 n. 1).
- 1QIsaᵃ and 1QpHab were assumed free of castor oil (not handled by the 1950s team; P25 S7.5).

## 4. Greek witnesses to the prophetic books (earliest)

| MS | contents | date | source |
|---|---|---|---|
| 8ḤevXIIgr (Rahlfs 943) | Twelve (kaige revision) | end of the 1st c. BCE | Tov, DJD VIII; Tov 2004 |
| 7Q2 7QpapEpJer gr | Epistle of Jeremiah (not Jeremiah) | IAA Hasmonean; c. 100 BCE (Baillet, DJD III; not verified here) | IAA |
| P.Chester Beatty VIII (Ra 966) | Jer 4–5 | 2nd–3rd c. CE (Tov 2004); c. 200 (WP) | Tov 2004 |
| P.Chester Beatty IX–X + P.Scheide 3 + Köln + Madrid + Barcelona = **P967** | Ezekiel, **Old Greek Daniel** (Bel and Susanna come after ch. 12; chs. 7–8 precede 5–6), Esther | early 3rd c. CE (Tov 2004 App. 5); 3rd c. (WP) | Tov 2004, WP |
| P.Chester Beatty VII (Ra 965) | Isa 8–60 (Tov also lists Ezek 11–17) | 3rd c. CE | Tov 2004, WP |
| P.Fir. 8 / P.Berlin 17212 / Freer W | Isa 19 / Jer 2–3 / Twelve | 3rd c. CE | Tov 2004 |
| P.Alex. 203 (roll) | Isa 48 | 3rd–4th c. CE | Tov 2004 |
| P.Oslo 11, P.Genève 252, P.Grenfell 5, P.Antinoopolis 10 | Isa 42,52–53; Jer 5–6; Ezek 5–6; Ezek 33–34 | 4th c. CE | Tov 2004 |
| Codices B, S (4th c.), A (5th c.), Q Marchalianus (6th c., WP) | full prophets (Daniel in Theodotion) | – | WP |
| Codex Chisianus 88; Syro-Hexapla | Old Greek Daniel | 88: 10th or early 14th c. (WP); Syro-Hexapla translated 616/7 (WP) | WP |

## 5. External attestations

### 5a. Ben Sira 48:17–50:24: Hebrew of Genizah MS B, fols. XVIII–XX
Source: Abegg transcription, bensira.org (`transcriptions/B/B_XVIII_Recto.pdf`, `_Verso.pdf`, `B_XIX_Recto.pdf`, `B_XX_Recto.pdf`). Folio XVIII is Bodleian MS Heb. e.62. MS B is a medieval copy and the only Hebrew witness to these chapters; MasSir covers only 39:27–44:17. Square brackets mark restorations. Greek is Rahlfs (CenterBLC LXX).

| verse | MS B (fol./line) | Hebrew | Greek note |
|---|---|---|---|
| 48:20 | 18r 13–14 | [ויקר]או אל אל עליון ויפרשו אליו כפים / [וישמע] קול תפלתם **ויושיעם ביד ישעיהו** | ἐλυτρώσατο αὐτοὺς ἐν χειρὶ Ησαιου |
| 48:22 | 18r 16–17 | [יח]זקיהו את הטו[ב] ויחזק בדרכי דוד — the rest is lost | adds ἃς ἐνετείλατο **Ησαιας ὁ προφήτης** ὁ μέγας καὶ πιστὸς ἐν ὁράσει αὐτοῦ |
| 48:23 | 18r 18 | lost | the sun went back; life added to the king (= Isa 38 / 2 Kgs 20) |
| 48:24 | 18v 1 | ברוח גבורה **חזה אחרית** **וינחם אבלי ציון** (cf. Isa 61:2–3 לנחם כל אבלים … לאבלי ציון; 40:1) | πνεύματι μεγάλῳ εἶδεν τὰ ἔσχατα καὶ παρεκάλεσεν τοὺς πενθοῦντας ἐν Σιων |
| 48:25 | 18v 2 | עד עולם **הגיד נהיות ונסתרות לפני בואן** (cf. Isa 42:9; 46:10; 48:6) | ὑπέδειξεν τὰ ἐσόμενα καὶ τὰ ἀπόκρυφα |
| 49:6 | 18v 10 | ויציתו קרית קדש וישמו ארחתיה | |
| 49:7 | 18v 11–12 | **ביד ירמיהו** כי ענוהו והוא **מרחם נוצר נביא** / **לנתוש ולנתוץ ולהאביד להרס** וכן **לבנת לנטע** ולהשיב (= Jer 1:5, 1:10) | ἐν χειρὶ Ιερεμιου … ἐν μήτρᾳ ἡγιάσθη προφήτης |
| 49:8 | 18v 13 | **יחזקאל ראה מראה ויגד זני מרכבה** (Ezek 1, 10) | Ιεζεκιηλ ὃς εἶδεν ὅρασιν δόξης … ἐπὶ ἅρματος χερουβιν |
| 49:9 | 18v 14 | וגם הזכיר את איוב נ[ב]יא המכלכל כל ד[רכי צ]דק | the Greek reads איוב (Job) as אויב (enemy): τῶν ἐχθρῶν |
| 49:10 | 18v 15–16 | **וגם שנים עשר הנביאים** תהי עצמתם פר[חות מתח]תם / אשר החלימו את יעקב וישעוהו ב[…] (letters of הנביאים partly marked uncertain) | καὶ **τῶν δώδεκα προφητῶν** τὰ ὀστᾶ ἀναθάλοι |
| 50:1 | 19r 7–8 | גדול אחיו ותפארת עמו **שמעון בן יוחנן הכהן** / אשר בדורו נפקד הבית ובימיו חזק היכל | **Σιμων Ονιου υἱὸς** ἱερεὺς ὁ μέγας |
| 50:24 | 20r | יאמן **עם שמעון** חסדו ויקם לו ברית פינחס אשר לא יכרת לו ולזרעו כימי שמים | the Greek generalises it to "with us" (μεθ᾿ ἡμῶν) |

The list in 44–50 runs Hezekiah, Isaiah, Josiah, Jeremiah, Ezekiel, Job, the Twelve, Zerubbabel, Jeshua, Nehemiah (49:11–13), then Enoch, Joseph, Shem, Seth, Enosh and Adam (49:14–16), then Simon (50:1). Daniel and Ezra are not named in either the Hebrew or the Greek.

**Factual anchors for Ben Sira's date**
| anchor | text |
|---|---|
| Simon the high priest | MS B 50:1 "Simon son of Yoḥanan the priest" = Greek "Simon son of Onias". Josephus *Ant.* 12.224–225: Onias (II) "left the high priesthood to his son Simon" (τὴν ἀρχιερωσύνην Σίμωνι τῷ παιδὶ καταλιπών), succeeded by Simon's son Onias (III). 3 Macc 2:1 places a high priest Simon at the visit of Ptolemy IV Philopator (after Raphia, 217 BCE). The conventional composition date of c. 196–175 BCE (Simon II's death c. 196 BCE; no allusion to Antiochus IV) is an inference (WP). bensira.org gives "c. 180 B.C.E." |
| Grandson's prologue (Rahlfs lines 27–28) | ἐν γὰρ τῷ ὀγδόῳ καὶ τριακοστῷ ἔτει ἐπὶ τοῦ Εὐεργέτου βασιλέως παραγενηθεὶς εἰς Αἴγυπτον καὶ συγχρονίσας: the 38th year of Ptolemy VIII Euergetes II, counted from 170 BCE, is 132 BCE. The translation was completed later, conventionally c. 117 BCE (WP) |
| Prologue on translated prophecies (lines 21–26) | οὐ γὰρ ἰσοδυναμεῖ αὐτὰ ἐν ἑαυτοῖς Εβραϊστὶ λεγόμενα καὶ ὅταν μεταχθῇ εἰς ἑτέραν γλῶσσαν· οὐ μόνον δὲ ταῦτα, ἀλλὰ καὶ αὐτὸς ὁ νόμος καὶ **αἱ προφητεῖαι** καὶ τὰ λοιπὰ τῶν βιβλίων οὐ μικρὰν ἔχει τὴν διαφορὰν ἐν ἑαυτοῖς λεγόμενα. Lines 1–2 and 8–10 name "the law, the prophets (τῶν προφητῶν) and the other books" |

### 5b. Other dated texts that name or quote the prophetic books
| text | date anchor | attestation |
|---|---|---|
| **Demetrius the Chronographer**, *On the Kings in Judaea* (Clement, *Strom.* 1.21.141.1–2, Greek checked) | his reckoning ends at **Ptolemy IV** (221–204 BCE) | counts from the Sennacherib captivity to Nebuchadnezzar's last (128 yr 6 mo); from the Samaria captivity to Ptolemy IV (573 yr 9 mo); from the Jerusalem captivity to Ptolemy IV (338 yr 3 mo). This attests the 2 Kings narrative; no prophetic book is named. The figures are internally inconsistent |
| **Eupolemus** (Clement, *Strom.* 1.21.141.4; Eusebius, *PE* 9.39.2–5 via Alexander Polyhistor) | his chronology runs "to the fifth year of the reign of Demetrius, Ptolemy being in his twelfth year" = **158/157 BCE**. The historian is conventionally identified with "Eupolemus son of John son of Accos", Judas's envoy to Rome (1 Macc 8:17; 2 Macc 4:11; Josephus *Ant.* 12.419; 161 BCE) | fr. 4: "in his [Jonachim's] time prophesied **Jeremiah the prophet**", Baal worship, Nebuchadnezzar with "Astibares king of the Medes" takes Jerusalem, and Jeremiah keeps the ark and tablets |
| **Tobit** (Greek GII = Sinaiticus; GI = B/A) | Qumran copies: 4Q196 c. 50 BCE (W); 4Q198 and 4Q199 IAA Hasmonean; 4Q197 Herodian; 4Q200 W midpoint 5 BCE | 2:6 "the word of the prophet **Amos** at Bethel" (Amos 8:10). 14:4: Jonah (GI) or **Nahum** (GII), and "all that the **prophets of Israel** spoke" (GII). **4Q198** frg 1 (Tob 14:2–6): "…מללו [נב]יא[י ישראל" (partly preserved). The Amos citation is not preserved at Qumran |
| **1 Maccabees** (Greek translation of a Hebrew original) | composed after John Hyrcanus became high priest (16:23–24, "the book of the days of his high priesthood"; 134–104 BCE) | 1:54 βδέλυγμα ἐρημώσεως (identical to OG Dan 11:31; Theodotion has βδέλυγμα ἠφανισμένον) for 15 Chislev 145 SE. 2:59–60: Hananiah, Azariah and Mishael saved from the flame; Daniel from the lions |
| **2 Maccabees**, prefixed letters | first letter dated 188 SE = 124 BCE (1:9); the second letter is undated | 2:1 "**Jeremiah the prophet**" in "the records"; 2:13 Nehemiah collected "the books about the kings and **prophets**"; 15:14 "Jeremiah the prophet of God" |
| **Letter of Aristeas** | – | concerns the translation of the Law only, so it is not evidence for the Prophets. The claim in Clement, *Strom.* 1.22, that "the law and the prophets" were translated under Ptolemy I/II is a late (c. 200 CE) report |

### 5c. Non-biblical Qumran scrolls that quote or comment on the prophets
Quoted words were checked against the ETCBC/Abegg DSS text. "Preserved" means visible on the fragment, as opposed to restored.

| MS | copy date | key facts |
|---|---|---|
| 1QpHab | 30–1 BCE (Cross); 1–50 CE (W); radiocarbon 120 BCE–20 CE (91.5%, R20) | pesher on Hab 1–2 |
| 4Q169 pNah | 50–25 BCE (W); IAA Herodian | 3–4 i 2–3: "[Deme]trius king of Yavan who sought to enter Jerusalem" (טרוס מלך יון preserved) and "from **Antiochus** until the rise of the rulers of the Kittim" (preserved) |
| 4Q161–165 pIsaᵃ⁻ᵉ | 4Q163 (papyrus) c. 85 BCE (W; P25 125–75); 4Q161 and 4Q162 50–25 BCE; 4Q165 30–1 BCE; 4Q164 IAA Hasmonean | 4Q161 radiocarbon 55 BCE–30 CE (92.1%) |
| 4Q166–167 pHos; 1Q14, 4Q168 pMic; 1Q15, 4Q170 pZeph; 3Q4 pIsa | 4Q166 W midpoint 20 CE (P25 50–1 BCE); 4Q168 30 BCE–68 CE; others IAA Herodian or Hellenistic-Roman | – |
| 4Q174 Florilegium | W midpoint 15 BCE; IAA Herodian | formulas: "written in the book of **Isaiah the prophet**" (Isa 8:11), "in the book of **Ezekiel the prophet**", Amos 9:11, "as it is written in the book of **Daniel the prophet**" with Dan 12:10 / 11:32 wording (ויצטרפו ועם יודעי אלוה יחזיקו preserved) |
| 4Q177 Catena A | W midpoint 15 BCE | "book of Ezekiel the pro[phet]"; Zech 3:9 |
| 11Q13 Melchizedek | P25 50–1 BCE; IAA Hasmonean | II 15–16: Isa 52:7 ("[Isa]iah the prophet", largely preserved). II 18: "as Dan[iel] said": only דנ is partly legible, and the Dan 9:25 words (עד משיח נגיד שבועים שבעה) are **entirely restored** |
| CD-A / CD-B (Cairo Genizah) | 10th c. CE / 11th–12th c. CE (Schechter; WP) | A: Isa 24:17 ("by Isaiah the prophet son of Amoz"), Isa 54:16, Isa 7:17, **Amos 5:26–27** ("Damascus", VII 14–15), **Amos 9:11** (VII 16), Hos 4:16, Hos 5:10, Mic 2:6, Mal 1:10, Ezek 44:15. B: **Zech 13:7** ("by Zechariah the prophet", XIX 7–9), Ezek 9:4 |
| 4Q266–273 (4QDᵃ⁻ʰ) | 4Q266 c. 75 BCE (W; 100–50 BCE) but radiocarbon 1–170 CE (85%, R20); 4Q267 30 BCE–20 CE but radiocarbon 210–95 BCE (65%, P25); 4Q268 W midpoint 15 CE; 4Q269 and 4Q273 W midpoint 15 BCE; 4Q271 40 BCE; 4Q272 P25 75–25 BCE; 4Q270 IAA Herodian | Of the CD VII prophetic block, only 4Q266 3 iii 17–20 preserves words: "המה ספר[י] הנביא[ים]" ("they are the books of the prophets"), "[ד]משק … כתוב דרך". The **Amos 5:26–27 quotation itself and Zech 13:7 are not preserved in any Qumran copy** (searched 4Q266–273, 5Q12, 6Q15) |
| 4Q383–391 (Apocryphon of Jeremiah C / Pseudo-Ezekiel) | **4Q391 papPsEzekᵉ 150–100 BCE** (W; P25 125–75); 4Q384 W midpoint 35 CE; 4Q390 P25 75–25 BCE; the rest IAA Herodian | the IAA records 4Q385/4Q388 bundle the psEzek and apocrJer sigla on shared plates |
| 4Q243–245 Pseudo-Daniel | IAA Herodian | – |

## 6. Old Greek translations: the concrete dating evidence

| book | terminus ante quem (evidence) | earliest MS | other evidence used in the literature (inferences, flagged) |
|---|---|---|---|
| all Prophets | The grandson's prologue (in Egypt from 132 BCE) says αἱ προφητεῖαι already exist in translation and differ from the Hebrew. It does not say which books | – | – |
| Isaiah | Prologue (132 BCE to about 116 BCE) | P.Chester Beatty VII (Ra 965), 3rd c. CE | Seeligmann (1948) dated it to 170–150 BCE from allusions, e.g. Isa 19:18 πόλις ασεδεκ read as alluding to the Leontopolis temple. Inference only |
| Jeremiah | Prologue | P.Chester Beatty VIII (Ra 966), 2nd–3rd c. CE | The Hebrew short text type of LXX-Jer is attested in 4QJerᵇ,ᵈ (first half of the 2nd c. BCE), which dates the Vorlage type, not the translation. Tov (1976) argues the same translation/revision runs through Jer 29–52 and Bar 1:1–3:8. 7Q2 (Greek EpJer, Hasmonean) shows Greek Jeremiah literature in Judaea |
| Ezekiel | Prologue | P967, early 3rd c. CE | – |
| Twelve | **8ḤevXIIgr** (end of the 1st c. BCE) is a Hebraizing revision of an existing Greek text (Barthélemy 1963; Tov DJD VIII), so the OG Twelve predates it. Also the prologue | 8ḤevXIIgr (revision); Freer W 3rd c. CE (OG) | – |
| Daniel | 1 Macc 1:54 (Greek) = OG Dan 11:31 βδέλυγμα ἐρημώσεως. This holds only if the Greek 1 Macc borrowed from OG Daniel, and the date of the Greek 1 Macc is itself unknown (Josephus used it in *Ant.* 12–13, c. 93/94 CE). Commonly put at c. 100 BCE (Montgomery; Collins) | P967, early 3rd c. CE; Chisianus 88; Syro-Hexapla 616/7 | The OG has 1,290 days at 12:11 like MT. Theodotion-type wording appears in the NT (e.g. Heb 11:33, cf. Th Dan 6:23), so the "Theodotion" text is pre-Christian in origin |

## 7. Access log
- Not attempted, per the brief: PHI, web.archive.org, achemenet, Trismegistos/LDAB.
- Refused or blocked; no workaround attempted: **papyri.info** (Anubis bot challenge), **repository.arizona.edu** (PDF bitstreams returned 1 byte, so the Cambridge Core open-access PDFs linked by Semantic Scholar were used instead), **Google Books API** (quota exceeded), **scholarsarchive.byu.edu** (403), **Israel Museum DSS site** (no response), the uni-koeln P967 page (404), and Wikipedia's API (temporary rate limit, so it was used sparingly).
- Checked and **rejected**: dssenglishbible.com. Its dates look like generic period conversions; for example it gives 4QJerᶜ as 250–150 BCE against Webster's 30–1 BCE.
- Not openly accessible: the DJD volumes and Tov's *Revised Lists* (2010). Webster's dates were taken from Tov 2004, which quotes them only for texts that appear in Tov's tables. That is why some fragments have only the coarse IAA period.
- Downloads (untrusted, one folder each) are in `/tmp/claude-0/-home-user-rade-crypto-github-io/df594cd1-7a3e-58a6-91bb-dd1c66d9c1a6/scratchpad/prophets_mss/`. The scripts (calibration, ETCBC/LXX text checks, CSV writer) are in `/tmp/claude-0/-home-user-rade-crypto-github-io/df594cd1-7a3e-58a6-91bb-dd1c66d9c1a6/scratchpad/prophets_scripts/`.
