"""Write the classified list of symphonia (noun) hits dated <=100 CE, plus fragments of
pre-100 CE authors transmitted in later texts. Category codes:
 a = musical instrument; b = harmony/concord/music in the abstract (incl. musical consonance and
 metaphorical concord); c = agreement/consistency/other; d = unclear / concrete performed music
 (band, ensemble or instrument - context does not decide)."""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
pre = [x for x in rows if x["class"] == "noun symphonia" and x["approx_year"] != "" and int(x["approx_year"]) <= 100]
C = set([19, 22, 24, 78, 80, 109, 110, 112, 117, 118, 126, 175])
A = {119: "listed among instruments (trumpet, pipe, kithara, sambyke, psalterion, symphonia) in OG Dan 3:5",
     120: "listed among instruments in OG Dan 3:15",
     237: "listed among instruments in Theodotion Dan 3:15 (Codex B; A,Q,Gamma add it also at 3:5, A,Q at 3:7 per Swete's apparatus)"}
D = {114: "Polybius 26.1a (Athenaeus 10.439a version): Antiochus IV joins young men's parties 'with horn and symphonia' - concrete music; instrument or band",
     115: "Polybius 26.1.4 (= Athenaeus 5.193e): 'came reveling with a keration (horn) and symphonia' - concrete music; instrument or band",
     116: "Polybius 30.22.11 (= Athenaeus 14.615d), L. Anicius' games 167 BCE: 'two dancers were brought in with a symphonia ... boxers with trumpeters and horn-players' - parallel with players suggests band/ensemble",
     188: "Luke 15:25 'he heard symphonia and dances' - performed music (band or instrument); Origen (Comm. Matt. 14.1; fr. in Luc. 74) glosses it as musical harmony"}
out = []
for i, x in enumerate(pre, 1):
    if i in A: cat, why = "a", A[i]
    elif i in D: cat, why = "d", D[i]
    elif i in C: cat, why = "c", "agreement / consistency (not musical)"
    else: cat, why = "b", "musical consonance or (metaphorical) harmony/concord"
    out.append({"n": i, "category": cat, "justification": why, "transmission": "direct",
                "original_author": x["author"], "approx_year": x["approx_year"], "date_label": x["date_label"],
                "source_text": x["author"] + ", " + x["work"], "edition_file": x["edition_file"],
                "citation": x["citation"], "form": x["form"], "context": x["context"]})
extra = [
 ("d", "Polybius 30.26.8 (Antiochus IV's Daphne banquet, 166 BCE): 'when the symphonia struck up/called him forth, he leapt up and danced' - band or instrument", "Polybius (2nd c. BCE), quoted by Athenaeus", "-150", "Athenaeus 5.195f (book=5|chapter=24)", "καὶ τῆς συμφωνίας προκαλουμένης ἀναπηδήσας γυμνὸς ὠρχεῖτο καὶ ὑπεκρίνετο μετὰ τῶν γελωτοποιῶν (grc4; grc3 lacks γυμνὸς). Not present in the Perseus Polybius text, whose 30.26 stops after the banquet couches."),
 ("d", "same Polybius passage, second Athenaean version", "Polybius (2nd c. BCE), quoted by Athenaeus", "-150", "Athenaeus 10.439d (book=10|chapter=53)", "καὶ ὑπὸ τῶν μίμων εἰσεφέρετο ὅλος συγκεκαλυμμένος καὶ ἐτίθετο εἰς τὴν γῆν ὡς εἷς ὢν τῶν μίμων καὶ τῆς συμφωνίας προκαλουμένης ὁ βασιλεὺς ἀναπηδήσας ὠρχεῖτο"),
 ("d", "Posidonius FGrHist 87 (Harpalus' funeral procession for Pythionike): 'with a great chorus of the most distinguished artists, all sorts of instruments and symphoniai' - symphoniai alongside instruments (ensembles/concerted music). TEXTUAL VARIANT: Perseus grc4 edition reads εὐφωνίαις instead.", "Posidonius of Apamea (c. 135-51 BCE), Histories bk 22, quoted by Athenaeus", "-80", "Athenaeus 13.594e (book=13|chapter=67)", "τεχνιτῶν τῶν ἐπισημοτάτων χορῷ μεγάλῳ καὶ παντοίοις ὀργάνοις καὶ συμφωνίαις [grc4: εὐφωνίαις] παρέπεμπε τὸ σῶμα"),
 ("b", "Semus of Delos, Delias bk 5, defining synaulia: 'a contest of symphonia, alternating between aulos and rhythm' - concerted music in abstract", "Semus of Delos (Hellenistic, c. 200 BCE?), quoted by Athenaeus", "-200", "Athenaeus 14.618a (book=14|chapter=9)", "ἀγνοουμένης δὲ παρὰ πολλοῖς τῆς συναυλίας, λεκτέον. ἦν τις ἀγὼν συμφωνίας ἀμοιβαῖος αὐλοῦ καὶ ῥυθμοῦ"),
 ("b", "Damoxenus, Syntrophoi (comic cook mixing dishes 'according to concord', with fourths, fifths, octaves) - musical-harmony metaphor", "Damoxenus (New Comedy, late 4th/early 3rd c. BCE), quoted by Athenaeus", "-300", "Athenaeus 3.103a (book=3|chapter=60)", "εἶτ’ οὐδὲν εἰκῇ παρατίθημι ... ἀλλὰ μείξας πάντα κατὰ συμφωνίαν. ... ἔστιν αὑτοῖς ἃ διὰ τεττάρων ἔχει κοινωνίαν, διὰ πέντε, διὰ πασῶν"),
 ("d", "Isigonus of Nicaea, Apista bk 2 (dancing reeds of Lake Tala in Lydia): 'when the beat (κτύπος) of a symphonia arises on the shore, all the reeds dance' - performed music; wording may be the epitomator's", "Isigonus of Nicaea (1st c. BCE/CE?), via Paradoxographus Florentinus (date uncertain)", "-50", "Paradoxographus Florentinus, Mirabilia de aquis 43", "ἐπειδὰν ἐπὶ τῆς ἠϊόνος κτύπος συμφωνίας γένηται· πάντες οἱ κάλαμοι χορεύουσι· ... ὡς ἱστορεῖ Ἰσίγονος ἐν δευτέρωι ἀπίστων"),
 ("b", "Philodemus (Herculaneum papyrus): 'as the musician brings one lyre into concord with the many'", "Philodemus (1st c. BCE), P.Herc. 1506 / 240 etc. (DCLP)", "-60", "DCLP P.Herc. 1506 col. ? l. 25; P.Herc. 240/421/431/436", "συλλύειν καὶ μὴ μαχομένας ποιεῖν, ὡς ὁ μουσικὸς τὴν μίαν λύραν εἰς συμφωνίαν ἄγει πρὸς τὰς πολλάς"),
 ("c", "Philodemus (Herculaneum papyrus): agreement with the phenomena", "Philodemus (1st c. BCE), P.Herc. 1050 (DCLP)", "-60", "DCLP P.Herc. 1050 l. 11", "τὰ δ' ἐκ τῆς τοῖς φαινομένοις συμφωνίας"),
 ("c", "Documentary papyri, 1st c. CE: συμφωνία = agreed sum / contract (tax-farming composition, wages)", "Documentary papyri (O.Bodl. 2.1056, 67 CE; P.Oxy. 34.2725, 71 CE; P.Aberd. 76, 79 CE; P.Oxy. 1.104, 96 CE; O.Leid. 81a, 96 CE)", "70", "DDbDP (see papyri_hits.csv)", "ἀπὸ τῆς συμφωνίας τοῦ ιγ ἔτους Νέρωνος ... ὑπὲρ διαλύσεως καὶ συμφωνίας περὶ τῶν ὀφειλομένων"),
]
for k, (cat, why, auth, yr, cit, ctx) in enumerate(extra, len(out) + 1):
    out.append({"n": k, "category": cat, "justification": why, "transmission": "indirect (fragment/quotation) or papyrus",
                "original_author": auth, "approx_year": yr, "date_label": "", "source_text": cit.split(" (")[0],
                "edition_file": "", "citation": cit, "form": "", "context": ctx})
with open(sys.argv[2], "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
import collections
print(collections.Counter(r["category"] for r in out[:len(pre)]), len(pre), len(out))
