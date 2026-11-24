"""Verse-level claim database for the historical prophecies of Daniel 8 and 11 (+ 12:11-12),
each claim checked against the ancient record.

Status codes
  hit      the claim matches the event as recorded in ancient sources
  partial  matches in part, or the identification of the referent is uncertain
  miss     the record contradicts the claim (under the reading in which the passage
           continues to describe the same king, which is what the Hebrew syntax does)
  vague    too general or metaphorical to be checked against any record

Identification of referents for 8:3-25 and 11:2-39 follows the explicit labels the text itself
gives (8:20 Media-Persia, 8:21 Greece, 11:2 Persia/Greece) and the near-universal correlation
with Persian-Hellenistic history (accepted by conservative and critical readers alike).
11:40-45 is scored twice: (A) the same king (Antiochus IV) continues, as the grammar implies;
(B) the futurist reading, in which these verses are unfulfilled and therefore uncheckable.

Sources are ANCIENT texts (and coins/inscriptions); see results/primary_sources.md for quotations.
"""
import os, sys, json, math
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))

S = dict(  # short source keys
    Beh="Behistun inscription", Hdt="Herodotus", Diod="Diodorus Siculus", App="Appian, Syriaca", Pol="Polybius",
    Liv="Livy", Jos="Josephus, Antiquities", M1="1 Maccabees", M2="2 Maccabees", Just="Justin, Epitome",
    Canopus="Canopus decree (238 BCE, OGIS 56)", Adulis="Adulis inscription of Ptolemy III (OGIS 54)",
    Gurob="Gurob papyrus (FGrH 160)", Strabo="Strabo", Coins="Seleucid coinage", BKL="Babylonian king list BM 35603",
    ABC="Babylonian Chronicles",
)

SEGMENTS = [
    # ---------------------------------------------------------------- Daniel 8
    dict(id="8:3-4", ch=8, v=(3, 4), label="Ram: Media-Persia expands", span=(550, 334), claims=[
        ("two-horned ram = kings of Media and Persia (8:20); the higher horn came up last", "hit", "ABC 7 (Nabonidus Chronicle ii 1-4): Cyrus takes Media 550"),
        ("it charges west, north and south and no beast can stand", "hit", "Hdt 1.76-84 (Lydia 546), ABC 7 iii (Babylon 539), Hdt 3.1-16 (Egypt 525)"),
        ("it does as it pleases and becomes great", "hit", "Beh §6 (list of 23 lands)"),
    ]),
    dict(id="8:5-8", ch=8, v=(5, 8), label="Goat: Alexander; four horns", span=(334, 301), claims=[
        ("a he-goat from the west (= king of Greece, 8:21) crosses the earth without touching the ground", "hit", "Arrian, Anabasis 1-3; Diod 17"),
        ("it shatters both horns of the ram, which has no power to stand", "hit", "Granicus 334, Issus 333, Gaugamela 331: Diod 17.19-61"),
        ("at the height of its strength the great horn is broken", "hit", "Alexander dies at 32 in 323: Diod 17.117"),
        ("four horns come up toward the four winds = four kingdoms, not with his power (8:22)", "hit", "Diod 20.53 (kings take the diadem 306-305); Ipsus 301"),
    ]),
    dict(id="8:9-12", ch=8, v=(9, 12), label="Little horn: Antiochus IV", span=(175, 167), claims=[
        ("a small horn grows out of one of the four", "hit", "Antiochus IV, Seleucid: App 45"),
        ("it grows toward the south", "hit", "Egyptian campaigns 170-168: Pol 28.18-21, 29.27"),
        ("toward the east", "partial", "eastern campaign only in 165: App 66, Pol 31.9 - after the other events"),
        ("toward the 'beautiful land'", "hit", "Judea 169-167: M1 1:20-64"),
        ("it casts some of the host and the stars to the ground and tramples them", "vague", "metaphor"),
        ("it magnifies itself up to the Prince of the host", "vague", "theological"),
        ("the regular (tamid) offering is taken away", "hit", "M1 1:45"),
        ("the place of the sanctuary is thrown down", "partial", "sanctuary desecrated, not demolished: M1 1:39, 4:38"),
        ("truth is cast to the ground", "hit", "Torah scrolls torn and burned: M1 1:56-57"),
    ]),
    dict(id="8:13-14", ch=8, v=(13, 14), label="2300 evening-mornings", span=(167, 164), claims=[
        ("after 2,300 evenings and mornings the sanctuary will be put right", "partial",
         "rededication 25 Kislev SE 148 (Dec 164) = 3 years after the first pagan sacrifice: M1 1:54-59, 4:52-54; 1,150 days ~ 3 yr 2 mo"),
    ]),
    dict(id="8:23-25", ch=8, v=(23, 25), label="Interpretation: the bold-faced king", span=(175, 164), claims=[
        ("at the latter end of their (the four kingdoms') rule a bold-faced king arises", "hit", "Antiochus IV 175: App 45"),
        ("he destroys mighty men and the people of the holy ones", "hit", "M1 1:24, 1:30, 1:60-64; M2 5:11-14"),
        ("by cunning he makes deceit succeed; 'without warning' he destroys many", "hit", "M1 1:29-30: spoke peaceable words deceitfully then fell on the city suddenly; M2 5:24-26"),
        ("he rises up against the Prince of princes", "vague", "theological"),
        ("he is broken, but not by (human) hand", "hit", "died of illness at Tabae: Pol 31.9; M1 6:8-16; M2 9"),
    ]),
    # ---------------------------------------------------------------- Daniel 11
    dict(id="11:2", ch=11, v=(2, 2), label="Persia: 3 kings + a 4th rich king vs Greece", span=(530, 480), claims=[
        ("three more kings will arise in Persia", "hit", "Cambyses, Bardiya, Darius I: Beh §10-13; Hdt 3"),
        ("a fourth will be far richer than all", "hit", "Xerxes: Hdt 7.27-29, 7.187"),
        ("he will stir up all against the kingdom of Greece (Yavan)", "hit", "Hdt 7.20-21 (480 BCE)"),
    ]),
    dict(id="(gap)", ch=11, v=None, label="Persia 479-337: nothing", span=(479, 337), claims=[]),
    dict(id="11:3-4", ch=11, v=(3, 4), label="Alexander and the partition", span=(336, 301), claims=[
        ("a mighty king arises, rules a great dominion, does as he pleases", "hit", "Alexander 336-323: Arrian; Diod 17"),
        ("as soon as he has arisen his kingdom is broken", "hit", "death 323: Diod 17.117"),
        ("divided toward the four winds of heaven", "hit", "Diod 20.53; Ipsus 301"),
        ("but not to his posterity", "hit", "Alexander IV killed 310, Heracles 309: Diod 19.105, 20.28"),
        ("nor with the dominion he had; it goes to others besides these", "hit", "Diod 18-20"),
    ]),
    dict(id="11:5", ch=11, v=(5, 5), label="Ptolemy I and Seleucus I", span=(316, 281), claims=[
        ("the king of the south (Ptolemy I) becomes strong", "hit", "Diod 18.14, 18.43"),
        ("one of his commanders becomes stronger, with a greater realm", "hit", "Seleucus served Ptolemy 316-312 then won Babylon and the east: Diod 19.55-58, 19.86-92; App 55"),
    ]),
    dict(id="11:6", ch=11, v=(6, 6), label="Berenice's marriage and murder", span=(252, 246), claims=[
        ("after some years the two make an alliance", "hit", "end of 2nd Syrian War c. 252: App 65"),
        ("the daughter of the king of the south comes to the king of the north to make an agreement", "hit", "Berenice daughter of Ptolemy II marries Antiochus II: App 65; Just 27.1"),
        ("she will not retain her strength", "hit", "App 65; Just 27.1"),
        ("he (Antiochus II) and his power will not last", "hit", "Antiochus II dies summer 246: App 65; BKL obv. 12-13 (Abu SE 66)"),
        ("she is given up, with those who brought her and her child/supporter", "hit", "Berenice, her infant son and attendants killed at Antioch: Just 27.1; Polyaenus 8.50"),
    ]),
    dict(id="11:7-9", ch=11, v=(7, 9), label="Ptolemy III's invasion (3rd Syrian War)", span=(246, 240), claims=[
        ("a shoot from her roots (her brother Ptolemy III) arises in his place", "hit", "accession 246"),
        ("he enters the fortress of the king of the north and prevails", "hit", "Gurob papyrus (Seleucia, Antioch); Adulis"),
        ("he carries their gods, images and precious vessels to Egypt", "hit", "Canopus decree; Adulis inscription"),
        ("for some years he refrains from the king of the north", "hit", "peace 241: Just 27.2"),
        ("the king of the north comes into the southern realm but returns to his own land", "hit", "failed counter-campaign of Seleucus II: Just 27.2"),
    ]),
    dict(id="11:10-12", ch=11, v=(10, 12), label="Antiochus III and Raphia", span=(221, 217), claims=[
        ("his sons (Seleucus III, Antiochus III) mobilise great forces", "hit", "Pol 5.40-41"),
        ("one sweeps on and overflows, carrying the war to the southern 'fortress'", "hit", "Pol 5.61-71, 5.80 (to Gaza/Raphia 219-217)"),
        ("the enraged king of the south fights him; the northern multitude is given into his hand", "hit", "Raphia 217: Pol 5.79-86"),
        ("he casts down tens of thousands", "hit", "Pol 5.86: c. 10,000 infantry, 300 horse killed, 4,000 captured"),
        ("but he will not prevail / press his advantage", "hit", "Pol 5.87 (quick peace)"),
    ]),
    dict(id="11:13-16", ch=11, v=(13, 16), label="5th Syrian War: Panium, Sidon, Judea", span=(202, 198), claims=[
        ("the king of the north returns with a larger army after some years", "hit", "after the eastern anabasis 212-205: Pol 11.34, 16.18"),
        ("many rise against the king of the south", "hit", "pact of Philip V and Antiochus III: Pol 15.20; Egyptian revolts"),
        ("violent men of your people rise up to fulfil a vision but fail", "vague", "no clear record"),
        ("he builds siege mounds and takes a fortified city", "hit", "siege of Gaza (Pol 16.18.2, 16.22a) and of the Ptolemaic garrison in Jerusalem's citadel (Jos 12.133-136)"),
        ("the southern forces, even picked troops, cannot stand", "hit", "Panium 200: Pol 16.18-19"),
        ("he stands in the 'beautiful land' with destruction in his hand", "hit", "Judea taken 200-198: Jos 12.133-144"),
    ]),
    dict(id="11:17", ch=11, v=(17, 17), label="Cleopatra I given to Ptolemy V", span=(197, 193), claims=[
        ("he makes an agreement with the king of the south", "hit", "Pol 18.51; Liv 33.40"),
        ("he gives him a daughter in marriage", "hit", "Cleopatra I married Ptolemy V 194/193: Liv 35.13; App 5; Jos 12.154"),
        ("to destroy it (the kingdom), but it will not succeed or be for him", "hit", "Cleopatra sided with Egypt: Liv 37.3 (embassy congratulating Rome)"),
    ]),
    dict(id="11:18-19", ch=11, v=(18, 19), label="Coastlands, Rome, death in Elymais", span=(197, 187), claims=[
        ("he turns to the coastlands and takes many", "hit", "Asia Minor coast and Thrace 197-196, Greece 192-191: Liv 33.19-20, 36"),
        ("a commander ends his insolence and turns it back on him", "hit", "L. Cornelius Scipio, Magnesia 190/189; Apamea 188: Pol 21.17, 21.42-43; Liv 37.38-44"),
        ("he turns back to the fortresses of his own land", "hit", "Pol 21.42-45"),
        ("he stumbles and falls and is not found", "hit", "killed plundering the temple of Bel in Elymais 187: Diod 28.3, 29.15; Strabo 16.1.18; Just 32.2"),
    ]),
    dict(id="11:20", ch=11, v=(20, 20), label="Seleucus IV and the tax-collector", span=(187, 175), claims=[
        ("his successor sends an exactor through the 'glory of the kingdom'", "hit", "Heliodorus and the temple treasury: M2 3"),
        ("within a few days he is broken", "partial", "reigned 12 years - not 'a few days'"),
        ("neither in anger nor in battle", "hit", "assassinated by Heliodorus: App 45"),
    ]),
    dict(id="11:21-24", ch=11, v=(21, 24), label="Antiochus IV's accession and conduct", span=(175, 170), claims=[
        ("a contemptible person, not given royal majesty", "hit", "the heir Demetrius was a hostage in Rome: App 45; Pol 31.2"),
        ("he comes in quietly and seizes the kingdom by intrigue", "hit", "installed with Pergamene help: App 45"),
        ("forces are swept away before him and broken", "partial", "referent uncertain"),
        ("the 'prince of the covenant' too", "partial", "high priest Onias III deposed 175, murdered 171: M2 4:7-10, 4:33-35"),
        ("he distributes plunder and wealth as his fathers never did", "hit", "M1 3:30 ('more lavishly than preceding kings'); Pol 26.1"),
        ("he devises plans against strongholds, for a time", "vague", ""),
    ]),
    dict(id="11:25-28", ch=11, v=(25, 28), label="First Egyptian campaign 170/169", span=(170, 169), claims=[
        ("he moves against the king of the south with a great army", "hit", "Pol 28.18-21; Diod 30.14-18; M1 1:16-19"),
        ("the king of the south, with a huge army, cannot stand", "hit", "Ptolemy VI defeated near Pelusium: Diod 30.14; M1 1:18"),
        ("plots against him: those who eat his food destroy him", "hit", "regents Eulaeus and Lenaeus: Diod 30.15-17; Pol 28.21"),
        ("the two kings speak lies at one table", "partial", "negotiations of Antiochus with Ptolemy VI at Memphis: Pol 28.23; Liv 44.19"),
        ("he returns with great wealth", "hit", "M1 1:19-20"),
        ("his heart is against the holy covenant; he acts, and returns to his land", "hit", "plunder of the Temple 169 (SE 143): M1 1:20-24; M2 5:11-21"),
    ]),
    dict(id="11:29-30a", ch=11, v=(29, 30), label="Second campaign 168: Day of Eleusis", span=(168, 168), claims=[
        ("at the appointed time he returns to the south", "hit", "Pol 29.27; Liv 45.11-12"),
        ("but it is not as before", "hit", "Pol 29.27"),
        ("ships of Kittim come against him and he is cowed and withdraws", "hit", "Roman envoy C. Popillius Laenas, the circle in the sand: Pol 29.27; Liv 45.12 (envoys came by sea from Delos)"),
    ]),
    dict(id="11:30b-31", ch=11, v=(31, 31), label="Persecution and the 'abomination'", span=(168, 167), claims=[
        ("enraged, he acts against the holy covenant", "hit", "M1 1:29-40; M2 5:23-26"),
        ("he favours those who forsake the covenant", "hit", "M1 1:11-15, 1:43, 1:52; M2 4:7-17"),
        ("his forces profane the sanctuary and the fortress", "hit", "Apollonius and the Akra: M1 1:29-36; M2 5:24-26"),
        ("they remove the regular offering", "hit", "M1 1:45"),
        ("they set up the 'abomination that makes desolate'", "hit", "M1 1:54 (15 Kislev SE 145 = Dec 167); M2 6:2 (Zeus Olympios)"),
    ]),
    dict(id="11:32-35", ch=11, v=(32, 35), label="Martyrs, the wise, 'a little help'", span=(167, 166), claims=[
        ("he seduces with flattery those who violate the covenant", "hit", "M1 2:18"),
        ("those who know their God stand firm and act", "hit", "M1 1:62-63, 2:27-28"),
        ("the wise fall by sword, flame, captivity and plunder", "hit", "M1 1:60-63, 2:29-38; M2 6:10-11, 7"),
        ("they receive 'a little help'", "partial", "start of the Maccabean revolt (166): M1 2-3"),
        ("many join them insincerely", "vague", ""),
    ]),
    dict(id="11:36-39", ch=11, v=(36, 39), label="The king's religious self-exaltation", span=(169, 165), claims=[
        ("he exalts and magnifies himself above every god", "partial", "coins: BASILEOS ANTIOCHOU THEOU EPIPHANOUS; M2 9:12"),
        ("he speaks astonishing things against the God of gods", "hit", "M1 1:24"),
        ("he prospers until the wrath is completed", "vague", ""),
        ("he disregards the gods of his fathers", "partial", "coin types shift from the dynastic Apollo to Zeus: Seleucid coinage"),
        ("nor the one beloved by women", "vague", ""),
        ("he honours a 'god of fortresses' his fathers did not know", "partial", "temple of Jupiter Capitolinus at Antioch: Liv 41.20.9; Zeus Olympios in Jerusalem: M2 6:2"),
        ("he garrisons strongholds with a foreign god's people and parcels out land", "partial", "Akra garrison; settlers given land: M1 1:33-34, 3:36"),
    ]),
    dict(id="11:40-45", ch=11, v=(40, 45), label="'Time of the end': predicted final war and death", span=(165, 164), future=True, claims=[
        ("the king of the south attacks him", "miss", "no Ptolemaic war after 168: Pol 29.27; Liv 45.12"),
        ("the king of the north storms against him with chariots, horsemen and many ships", "miss", "no third Egyptian campaign"),
        ("he invades countries, sweeping through", "miss", ""),
        ("he enters the 'beautiful land'; tens of thousands fall", "miss", "his generals fought in Judea (M1 3-4) but he never returned"),
        ("Edom, Moab and the Ammonites escape him", "miss", "no record of such a campaign"),
        ("Egypt does not escape; he takes its treasures", "miss", "Egypt remained Ptolemaic under Roman protection"),
        ("Libyans and Cushites follow in his train", "miss", ""),
        ("news from the east and north alarms him; he sets out in fury", "partial", "he did campaign in Armenia (north) and Persia (east) in 165: App 45, 66 - but before, not after, any conquest of Egypt"),
        ("he pitches his royal tents between the sea(s) and the holy mountain", "miss", "he died at Tabae in Persis: Pol 31.9; M1 6:1-16; M2 9:1-29"),
        ("he comes to his end, with none to help him", "partial", "he did die c. Nov/Dec 164 (BKL), but in Persia"),
    ]),
    dict(id="12:11-12", ch=12, v=(11, 12), label="1,290 and 1,335 days", span=(164, 163), future=True, claims=[
        ("1,290 days from the removal of the tamid to the end", "miss", "lands mid-163 BCE (see calendar.md): no corresponding event"),
        ("blessed is he who reaches 1,335 days", "miss", "lands late summer 163 BCE: no corresponding event"),
    ]),
]

SCORE = {"hit": 1.0, "partial": 0.5, "miss": 0.0}

def word_counts():
    from corpora import load_bhsa
    A = load_bhsa("book chapter verse lex")
    F, L, T = A.F, A.L, A.T
    out = {}
    for seg in SEGMENTS:
        if not seg["v"]:
            out[seg["id"]] = 0
            continue
        n = 0
        for vv in range(seg["v"][0], seg["v"][1] + 1):
            node = T.nodeFromSection(("Daniel", seg["ch"], vv))
            # graphical words: count words that are followed by a space (maqaf/prefix-joined count once)
            n += sum(1 for w in L.d(node, "word") if (T.text([w], fmt="text-orig-full").endswith(" ")
                                                    or T.text([w], fmt="text-orig-full").endswith("׃ ")))
        out[seg["id"]] = n
    return out

def changepoint(claims_timeline):
    """Bayesian single change-point for a Bernoulli success rate along the claims ordered by referent date.
    p(before), p(after) ~ Beta(1,1); uniform prior over break positions. Returns posterior over the break date."""
    x = np.array([s for _, s in claims_timeline])
    t = np.array([d for d, _ in claims_timeline])
    from scipy.special import betaln
    n = len(x)
    logp = []
    for k in range(1, n):   # break after k-th claim
        a, b = x[:k], x[k:]
        lp = betaln(1 + a.sum(), 1 + len(a) - a.sum()) + betaln(1 + b.sum(), 1 + len(b) - b.sum())
        logp.append(lp)
    logp = np.array(logp); p = np.exp(logp - logp.max()); p /= p.sum()
    # break date = midpoint between the referent dates of claims k-1 and k
    dates = [(t[k - 1] + t[k]) / 2 for k in range(1, n)]
    return list(zip(dates, p)), x, t

if __name__ == "__main__":
    RES = os.path.join(os.path.dirname(__file__), "..", "results")
    wc = word_counts()
    rows, timeline_A = [], []
    for seg in SEGMENTS:
        sc = [SCORE[s] for _, s, _ in seg["claims"] if s in SCORE]
        y0, y1 = seg["span"]
        years = max(1, y0 - y1 + 1)
        r = dict(id=seg["id"], label=seg["label"], span=f"{y0}-{y1} BCE", years=years, words=wc[seg["id"]],
                 words_per_decade=round(10 * wc[seg["id"]] / years, 1), n_claims=len(seg["claims"]),
                 checkable=len(sc), hits=sum(1 for _, s, _ in seg["claims"] if s == "hit"),
                 partial=sum(1 for _, s, _ in seg["claims"] if s == "partial"),
                 misses=sum(1 for _, s, _ in seg["claims"] if s == "miss"),
                 vague=sum(1 for _, s, _ in seg["claims"] if s == "vague"),
                 accuracy=round(sum(sc) / len(sc), 2) if sc else None,
                 claims_per_decade=round(10 * len(seg["claims"]) / years, 2), future=seg.get("future", False))
        rows.append(r)
        mid = (y0 + y1) / 2
        for c, s, src in seg["claims"]:
            if s in SCORE:
                timeline_A.append((mid, 1.0 if s == "hit" else (0.5 if s == "partial" else 0.0)))
    import csv
    with open(os.path.join(RES, "prophecy_segments.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    with open(os.path.join(RES, "prophecy_claims.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["segment", "verses", "claim", "status", "ancient evidence"])
        for seg in SEGMENTS:
            for c, s, src in seg["claims"]:
                w.writerow([seg["label"], seg["id"], c, s, src])
    for r in rows:
        print(f"{r['id']:10s} {r['span']:14s} words={r['words']:4d} w/decade={r['words_per_decade']:6.1f} "
              f"claims={r['n_claims']:2d} hit={r['hits']} part={r['partial']} miss={r['misses']} vague={r['vague']} acc={r['accuracy']}")
    # change-point: order claims by referent date (descending BCE = forward in time); partial counted as 0.5 -> binarise >=0.5 as success
    tl = sorted(timeline_A, key=lambda x: -x[0])
    tl_bin = [(d, 1 if s >= 0.5 else 0) for d, s in tl]
    post, x, t = changepoint(tl_bin)
    best = max(post, key=lambda z: z[1])
    cum = 0; lo = hi = None
    for d, p in sorted(post, key=lambda z: -z[0]):
        cum += p
        if lo is None and cum >= 0.025: lo = d
        if hi is None and cum >= 0.975: hi = d
    print(f"\nChange-point (scenario A): most probable break at ~{best[0]:.0f} BCE (p={best[1]:.2f}); 95% interval {lo:.0f}-{hi:.0f} BCE")
    # strict version: partial counted as failure
    tl_strict = [(d, 1 if s == 1.0 else 0) for d, s in tl]
    post2, _, _ = changepoint(tl_strict)
    best2 = max(post2, key=lambda z: z[1])
    print(f"Change-point (partial = failure): most probable break at ~{best2[0]:.0f} BCE (p={best2[1]:.2f})")
    # aggregate accuracy before/after
    pre = [s for d, s in tl if d > 166]; post_ = [s for d, s in tl if d <= 165]
    print(f"Accuracy of checkable claims about events before 166 BCE: {np.mean(pre):.2f} (n={len(pre)}); about 165-163 BCE: {np.mean(post_):.2f} (n={len(post_)})")
    json.dump(dict(best_break=best[0], p=best[1], ci=[lo, hi], best_break_strict=best2[0],
                   acc_pre=float(np.mean(pre)), n_pre=len(pre), acc_post=float(np.mean(post_)), n_post=len(post_),
                   posterior=[(float(d), float(p)) for d, p in post]),
              open(os.path.join(RES, "prophecy_changepoint.json"), "w"), indent=1)
