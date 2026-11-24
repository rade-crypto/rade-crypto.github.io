"""Score each claim. These are JUDGEMENTS, kept separate from the data (claims.py, evidence.py, sources/).
P  proof the passage existed before the event (0-3): 3 passage in a manuscript/quotation older than the event;
   2 the book is attested before the event (e.g. Ben Sira 49:10) but not the passage; 1 internal evidence only
   (dated heading, political horizon, unrevised misses); 0 the same narrative reports the fulfilment.
E  event recorded outside the Bible (0-3): 3 contemporary documents/archaeology; 2 later non-biblical writers;
   1 biblical record only; 0 no record.
S  specificity (0-3): one point each for a named agent, a time limit, a distinctive detail beyond 'conquered'.
M  plain reading matches (0-3): 3 all stated elements; 2 main element, some details not; 1 only with a different
   agent/time than the text states; 0 no match.
U  unexpected when written (0-2): 2 contrary to the situation; 1 uncertain; 0 already under way.
I  independent of the text (0-1): 1 actors and recorders unaware of / unmoved by the prophecy.
"""
import os, pandas as pd
R = [  # id, P, E, S, M, U, I, note
("A01",1,3,3,3,1,1,"Tiglath-pileser III: Damascus besieged, 591 cities, 13,520 Israelites deported, Pekah killed, Hoshea installed (733-732); time limit ~1-2 yrs met"),
("A02",1,3,1,1,1,1,"Israel ended as a kingdom after ~13 yrs, not 65; 65 has no clear referent"),
("A03",1,3,0,1,1,1,"Damascus taken 732 but never ceased to be a city"),
("A04",1,3,1,2,2,1,"Damascus taken and deported 732; 'Kir' only in 2 Kgs 16:9; written when Assyria was weak (if heading accepted)"),
("A05",1,3,1,3,2,1,"Deportations 733-720 confirmed; Amos never names Assyria; 6:14 assumes Jeroboam II's borders"),
("A06",1,1,1,2,1,1,"Jeroboam's son killed (biblical only); Jeroboam himself not"),
("A07",1,3,1,3,1,1,"Kingdom ended 722/720 (Babylonian Chronicle 'ravaged Samaria'; Sargon)"),
("A08",1,3,2,3,1,1,"Sargon lists Samaria's gods as spoil; Assyria named"),
("A09",1,2,1,1,1,0,"720: Samaria rebuilt by Sargon; razed only c.108 BCE by a Jewish ruler"),
("A10",1,3,2,3,1,1,"Esarhaddon 671 deports Taharqa's wife, crown prince, children; 701 Egyptian/Kushite charioteers captured"),
("A11",1,3,1,2,1,1,"Sennacherib withdrew without taking Jerusalem; no record of his army destroyed"),
("A12",0,3,3,3,1,1,"No Sennacherib text claims entry, capture or ramp at Jerusalem; but narrative written after 681"),
("A13",0,3,3,3,1,1,"'Killed by his son' (Babylonian Chronicle); narrative reports it"),
("A14",0,3,3,3,2,1,"Jehoiachin and sons in Babylon ration lists; narrative written later"),
("A15",1,3,0,2,1,1,"586 destruction; Jer 26:19 says it was not carried out in Hezekiah's day"),
("A16",1,3,1,3,1,1,"612 siege, plunder, 'ruin-hills' (Babylonian Chronicle); no attacker or date in Nahum; no flood in the record"),
("A17",1,3,1,3,1,1,"612 destruction; later small town (Tacitus 49 CE)"),
("A18",1,3,1,1,1,1,"70 years is a stock span (Esarhaddon: 70 reversed to 11)"),
("A19",1,3,0,2,1,0,"Ashkelon/Ekron 604 yes; Gaza never deserted; coast taken by Hasmoneans"),
("B01",1,3,2,3,1,1,"597 Chronicle; 586 destruction layers; announced from 605 (Jer 25:9) though some oracles date to the siege itself"),
("B02",1,1,1,0,1,1,"2 Kgs 24:6: 'slept with his fathers'; his son reigned"),
("B03",1,3,2,3,1,1,"Ration tablets: Ya'ukin king of Judah and sons in Babylon; no descendant became king"),
("B04",1,1,1,0,1,1,"Blinded, died in prison (Jer 52:11)"),
("B05",1,1,2,3,1,1,"Blinded before reaching Babylon - biblical record only"),
("B06",1,3,3,2,1,1,"605-539 = 66 yrs, 609-539 = 70; '70 years' is a stock span"),
("B07",0,1,2,3,1,1,"Narrative reports it"),
("B08",1,2,3,2,1,1,"Apries handed over and strangled (Herodotus) - but Judeans in Egypt did not perish (Elephantine)"),
("B09",1,3,2,1,1,1,"568/567 campaign (BM 33041, outcome lost); Amasis kept throne"),
("B10",1,2,1,0,1,1,"No 40-yr desolation; Egypt most prosperous under Amasis (Herodotus)"),
("B11",1,2,3,1,2,1,"Nebuchadnezzar failed (Ezek 29:18); Alexander used Old Tyre's stones (Curtius); Tyre rebuilt"),
("B12",1,3,1,3,0,1,"Ashkelon captured and made a ruin mound 604 (Chronicle)"),
("B13",1,3,2,2,0,1,"599/598 raid on Arabs (Chronicle); Hazor unlocated"),
("B14",1,2,0,2,1,1,"Peoples vanished; lands and Rabbah (Amman) stayed inhabited"),
("B15",1,2,0,1,1,1,"Edomites vanished as a people; land not uninhabited (Petra)"),
("B16a",1,3,2,2,1,1,"539 taken by Cyrus (ruler of Media), 'without battle'; gods returned not shattered"),
("B16b",3,2,1,1,1,1,"1QIsa-a (205-90 BCE) older than abandonment; desolation came ~600 yrs after the conquest the text names; bricks quarried (Jer 51:26)"),
("B17",1,3,3,2,0,1,"Gates opened without battle; Bel and Nebo not taken captive; text speaks to Cyrus's own time"),
("B18",1,3,1,3,0,1,"Babylon's rise"),
("C01",1,2,1,0,1,1,"Persian empire not overthrown; Zerubbabel vanishes"),
("C02",2,2,1,1,1,0,"Herod's temple grander; 'peace in this place' did not follow"),
("C03",1,1,2,2,0,1,"Biblical record only"),
("C04",1,2,2,2,1,1,"Alexander 332 at Tyre and Gaza; Zech 9-14 undated"),
("C05",2,2,1,2,1,0,"Ben Sira's 'twelve prophets' predates 167; Maccabean war vs Seleucids; no scroll of Zech 9"),
("C06",2,2,2,2,1,0,"Ben Sira predates; Hasmonean conquests followed a deliberate 'ancestral land' programme"),
("C07",2,2,2,2,1,0,"Onias cited this very prophecy when founding his temple"),
("C08",1,2,1,1,1,1,"Alexander, not Judah, sold Tyrians and Gazans"),
("D01",2,3,2,1,1,1,"Book attested before 70 CE (4Q174; 1 Macc), but 9:24-27 not in any scroll; timeline does not reach 70 CE without a gap"),
("D02",3,3,1,1,1,1,"In 4QXII; but kings and sacrifice existed 515 BCE-70 CE"),
("D03",3,2,0,2,1,1,"Generic"),
("D04",3,3,1,1,1,0,"Modern movement drew on the texts; same passages: plunder Philistia/Edom/Moab, dry the sea of Egypt"),
]
df = pd.DataFrame(R, columns=["id","P","E","S","M","U","I","note"])
df["total"] = df[["P","E","S","M","U","I"]].sum(axis=1)
here = os.path.dirname(__file__)
import sys; sys.path.insert(0, here); from claims import CLAIMS
meta = {c["id"]: (c["refs"], c["target"]) for c in CLAIMS}
df.insert(1, "refs", df.id.map(lambda i: meta[i][0])); df.insert(2, "target", df.id.map(lambda i: meta[i][1]))
df = df.sort_values(["total","M","P"], ascending=False)
df.to_csv(os.path.join(here, "..", "results", "ranking.csv"), index=False)
pd.set_option("display.width", 220); pd.set_option("display.max_colwidth", 60)
print(df[["id","refs","P","E","S","M","U","I","total"]].head(15).to_string(index=False))
print("\nclaims with P=3 (provably older):\n", df[df.P==3][["id","target","M","total"]].to_string(index=False))
