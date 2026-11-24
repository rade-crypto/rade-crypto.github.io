"""Curated database of testable predictions in the Latter Prophets (+ Daniel 9:24-27 and two passages
from the Isaiah/Kings narratives that are often cited).

Built from results/inventory_oracles.csv: every foreign name that is the subject/object of predictive
verses in >= 3 verses is covered by at least one claim, plus the predictions about Israel, Judah and
Jerusalem that concern datable events. References use HEBREW verse numbering (BHSA).

Each claim records only what the Hebrew says ("prediction") and which events it can be checked
against. Judgements (scores) live in score.py so that they are separate from the data.
"""

CLAIMS = [
# ---------------------------------------------------------------- Assyrian period (8th-7th c.)
dict(id="A01", refs="Isa 7:4-9; 7:16; 8:1-4", target="Damascus and Samaria",
     prediction="The attack of Rezin (Aram) and the son of Remaliah (Israel) on Judah will fail; before the child "
                "Maher-shalal-hash-baz can say 'my father, my mother', the wealth of Damascus and the spoil of Samaria "
                "will be carried off before the king of Assyria (8:4). Written on a tablet before witnesses (8:1-2).",
     event="Tiglath-pileser III takes Damascus (732) and strips Israel of Galilee/Gilead, Pekah overthrown (733-732)",
     event_date=-732),
dict(id="A02", refs="Isa 7:8", target="Ephraim (Israel)",
     prediction="Within 65 years Ephraim will be shattered so that it is no longer a people.",
     event="Samaria falls 722/720 (about 13 years later); Esarhaddon-era resettlement c. 670 is reported only in Ezra 4:2",
     event_date=-720),
dict(id="A03", refs="Isa 17:1-3", target="Damascus",
     prediction="Damascus will cease to be a city and become a heap of ruins; the fortress will disappear from Ephraim.",
     event="Damascus captured 732 and made an Assyrian province; the city itself continued to be inhabited",
     event_date=-732),
dict(id="A04", refs="Amos 1:3-5", target="Damascus / Aram",
     prediction="Fire on the house of Hazael, the bar of Damascus broken, the people of Aram exiled to Kir.",
     event="Tiglath-pileser III conquers Damascus and deports its population (732); 'Kir' is named only in 2 Kgs 16:9",
     event_date=-732),
dict(id="A05", refs="Amos 5:27; 6:14; 7:17; 9:4", target="Israel (northern kingdom)",
     prediction="Israel will go into exile 'beyond Damascus'; a (unnamed) nation will oppress Israel 'from Lebo-hamath "
                "to the brook of the Arabah' (6:14, the same borders 2 Kgs 14:25 credits to Jeroboam II).",
     event="Assyrian deportations of Israelites 733-720 (Tiglath-pileser III, Shalmaneser V, Sargon II)",
     event_date=-720),
dict(id="A06", refs="Amos 7:9; 7:11", target="House of Jeroboam II",
     prediction="God will rise against the house of Jeroboam with the sword (7:9); Amaziah reports Amos as saying "
                "'Jeroboam will die by the sword' (7:11).",
     event="Zechariah son of Jeroboam assassinated after 6 months (2 Kgs 15:10); Jeroboam himself died a natural death (2 Kgs 14:29)",
     event_date=-746),
dict(id="A07", refs="Hos 1:4-5", target="House of Jehu; kingdom of Israel",
     prediction="In a little while God will punish the house of Jehu and put an end to the kingdom of the house of Israel.",
     event="End of Jehu's dynasty (746, biblical record only) and end of the kingdom (722/720, Assyrian records)",
     event_date=-722),
dict(id="A08", refs="Hos 10:5-8; 11:5; 14:1", target="Samaria and its calf image",
     prediction="The calf of Beth-aven will be carried to Assyria as tribute to 'the great king'; Samaria's king cut off; "
                "Samaria will fall by the sword, Assyria will be Israel's king.",
     event="Fall of Samaria 722/720; Sargon II lists 'the gods in which they trusted' among the spoil",
     event_date=-720),
dict(id="A09", refs="Mic 1:6-7", target="Samaria",
     prediction="Samaria will become a heap in the field, a place for planting vineyards; her stones poured into the "
                "valley, her foundations laid bare, her images smashed.",
     event="722/720 Samaria captured but rebuilt as an Assyrian provincial capital; 108 BCE John Hyrcanus razes it",
     event_date=-720),
dict(id="A10", refs="Isa 20:1-6", target="Egypt and Cush",
     prediction="Dated to the year the Tartan came to Ashdod under Sargon: the king of Assyria will lead away the "
                "captives of Egypt and the exiles of Cush, young and old, naked and barefoot.",
     event="701 Eltekeh (Egyptian and Kushite chariot officers captured); 671 Esarhaddon takes Memphis and deports "
           "Taharqa's family; 667/663 Ashurbanipal (Thebes)",
     event_date=-671),
dict(id="A11", refs="Isa 10:24-34; 14:24-27; 30:31; 31:8", target="Assyria at Jerusalem",
     prediction="Assyria will be broken 'in my land, on my mountains'; Assyria will fall by a sword not of man.",
     event="701: Sennacherib withdraws without taking Jerusalem; no non-biblical record of his army being destroyed",
     event_date=-701),
dict(id="A12", refs="Isa 37:33-35", target="Sennacherib and Jerusalem",
     prediction="He will not enter this city, shoot an arrow there, or build a siege ramp against it; he will return "
                "the way he came.  (Inside a narrative that also reports Sennacherib's death in 681, 37:38.)",
     event="701: Sennacherib's annals claim a blockade of Jerusalem and tribute, not its capture",
     event_date=-701, narrative_includes_fulfilment=True),
dict(id="A13", refs="Isa 37:7", target="Sennacherib",
     prediction="He will hear a rumour, return to his land, and fall by the sword in his own land.  (Same narrative; "
                "the fulfilment is narrated in 37:38.)",
     event="681: Sennacherib killed by his son(s) in a rebellion", event_date=-681, narrative_includes_fulfilment=True),
dict(id="A14", refs="Isa 39:5-7", target="Hezekiah's house and Babylon",
     prediction="All the treasures of the palace will be carried to Babylon; some of Hezekiah's descendants will be "
                "eunuchs in the palace of the king of Babylon.  (Narrative; written after 681 at the earliest.)",
     event="597-586: Jehoiachin and his sons held in Babylon (ration tablets)", event_date=-597,
     narrative_includes_fulfilment=True),
dict(id="A15", refs="Mic 3:12", target="Jerusalem / Temple Mount",
     prediction="Zion will be ploughed as a field, Jerusalem will become heaps of ruins, the Temple Mount a wooded height. "
                "(Quoted word for word in Jer 26:18 as a prophecy from Hezekiah's reign that was NOT carried out then, 26:19.)",
     event="586 destruction by Babylon; c. 130 CE Aelia Capitolina founded with the Roman ploughing rite",
     event_date=-586),
dict(id="A16", refs="Nah 1:8; 1:14; 2:2-14; 3:1-19", target="Nineveh",
     prediction="Nineveh will be destroyed: river gates opened, palace melting, plunder of silver and gold, fire devours "
                "the gate bars, an overflowing flood makes an end of its place, 'no healing for your wound'.",
     event="612: Nineveh captured by the Medes and Babylonians after a three-month siege; burnt; never again a capital",
     event_date=-612),
dict(id="A17", refs="Zeph 2:13-15", target="Assyria / Nineveh",
     prediction="God will destroy Assyria and make Nineveh a desolation, dry like the desert; flocks and every wild "
                "animal will lie down in her; owl and hedgehog in her capitals.",
     event="612 destruction; in 401 BCE Xenophon passed a huge deserted city ('Mespila') on the site",
     event_date=-612),
dict(id="A18", refs="Isa 23:1-18", target="Tyre and Sidon",
     prediction="Tyre laid waste; forgotten 70 years 'like the days of one king', then she will return to her trade.",
     event="Assyrian campaigns (701 Luli flees; 677 Sidon destroyed; 663 Tyre submits); 70 years is a conventional span",
     event_date=-677),
dict(id="A19", refs="Zeph 2:4-7", target="Philistine cities",
     prediction="Gaza deserted, Ashkelon a desolation, Ashdod driven out at noon, Ekron uprooted; the coast will belong "
                "to the remnant of the house of Judah.",
     event="604 Babylon destroys Ashkelon and Ekron; Gaza survives; 147-96 BCE Hasmoneans take the coast",
     event_date=-604),
# ---------------------------------------------------------------- Babylonian period (late 7th-6th c.)
dict(id="B01", refs="Jer 20:4-6; 21:4-10; 25:9-11; 32:28-29; 34:2; 37:8-10; 38:17-18", target="Jerusalem and Judah",
     prediction="Jerusalem will be handed to the king of Babylon, who will burn it with fire; Judah taken to Babylon.",
     event="597 surrender; 587/586 Jerusalem burnt (destruction layers); deportations", event_date=-586),
dict(id="B02", refs="Jer 22:18-19; 36:30", target="Jehoiakim",
     prediction="Jehoiakim will be unlamented, buried 'with the burial of a donkey', dragged and thrown outside the gates; "
                "his corpse exposed; none of his line will sit on David's throne.",
     event="2 Kgs 24:6 says he 'slept with his fathers'; his son Jehoiachin reigned 3 months", event_date=-598),
dict(id="B03", refs="Jer 22:24-30", target="Coniah (Jehoiachin)",
     prediction="Coniah will be handed to Nebuchadnezzar, hurled with his mother into another land and die there; "
                "no descendant of his will sit on David's throne.",
     event="597 deported (Babylonian Chronicle); ration tablets in Babylon; grandson Zerubbabel a governor, not a king",
     event_date=-597),
dict(id="B04", refs="Jer 34:4-5", target="Zedekiah",
     prediction="Zedekiah will not die by the sword; he will die in peace, with spices burnt for him as for his fathers.",
     event="Blinded at Riblah and held in Babylon until his death (Jer 52:11; biblical record only)", event_date=-586),
dict(id="B05", refs="Ezek 12:12-13", target="'The prince' (Zedekiah)",
     prediction="He will be brought to Babylon, the land of the Chaldeans, yet he will not see it, and he will die there.",
     event="Blinded before being taken to Babylon (2 Kgs 25:7; biblical record only)", event_date=-586),
dict(id="B06", refs="Jer 25:1-14; 29:10", target="Babylon's dominion",
     prediction="These nations will serve [MT: the king of Babylon] 70 years; when 70 years are complete God will punish "
                "[MT: the king of Babylon and] that nation [MT: the land of the Chaldeans].",
     event="Babylonian hegemony 605/609-539; Babylon falls to Cyrus 539 (66-70 years)", event_date=-539),
dict(id="B07", refs="Jer 28:16-17", target="Hananiah",
     prediction="Hananiah will die this year.  (Narrative reports the fulfilment in the next verse.)",
     event="Biblical narrative only", event_date=-593, narrative_includes_fulfilment=True),
dict(id="B08", refs="Jer 44:26-30", target="Pharaoh Hophra (Apries); Judeans in Egypt",
     prediction="Sign: Pharaoh Hophra will be given into the hand of his enemies who seek his life, as Zedekiah was given "
                "to Nebuchadnezzar.  Main prediction: all the men of Judah in Egypt will perish, a few will return.",
     event="570 Apries overthrown by Amasis, killed c. 567; but Judean communities in Egypt flourished (Elephantine, 5th c.)",
     event_date=-567),
dict(id="B09", refs="Jer 43:8-13; 46:13-26; Ezek 29:17-20; 30:10-12", target="Egypt and Nebuchadnezzar",
     prediction="Nebuchadnezzar will strike Egypt, set his throne at Tahpanhes, burn the temples of Egypt's gods; Egypt "
                "will be his army's wages (Ezek 29:17-20, dated 571).",
     event="568/567 campaign against Amasis (fragmentary Babylonian tablet); Amasis kept his throne until 526",
     event_date=-568),
dict(id="B10", refs="Ezek 29:9-16; 30:13", target="Egypt's future",
     prediction="Egypt uninhabited 40 years, its people scattered, then restored as the lowliest kingdom, never again "
                "ruling nations; 'there will no longer be a prince from the land of Egypt'.",
     event="No 40-year desolation (Amasis' long, prosperous reign); native kingship ended 343 BCE; Ptolemaic Egypt ruled "
           "Judea and Cyprus 301-200 BCE", event_date=-343),
dict(id="B11", refs="Ezek 26:1-14; 26:19-21; 27:36; 28:19", target="Tyre",
     prediction="Many nations against Tyre like waves; Nebuchadnezzar will besiege and enter it; 'they will put your "
                "stones, your timber and your soil in the midst of the water' (26:12); Tyre a bare rock, a place to "
                "spread nets; 'you will never be rebuilt' (26:14).",
     event="Nebuchadnezzar's 13-year siege ends without capture (admitted in Ezek 29:18); 332 Alexander builds a mole "
           "with the stones of Old Tyre; Tyre rebuilt and inhabited ever since", event_date=-332),
dict(id="B12", refs="Jer 47:1-7", target="Philistines (Gaza, Ashkelon)",
     prediction="Waters from the north overflow the Philistines; Gaza shaved bald, Ashkelon silenced.",
     event="604 Nebuchadnezzar captures Ashkelon and turns it into a ruin mound (Babylonian Chronicle)", event_date=-604),
dict(id="B13", refs="Jer 49:28-33", target="Kedar and Hazor (Arabs)",
     prediction="Nebuchadnezzar will strike Kedar; Hazor an everlasting waste where no one lives.",
     event="599/598 Nebuchadnezzar plunders the Arabs in the desert (Babylonian Chronicle)", event_date=-599),
dict(id="B14", refs="Jer 48:1-47; 49:1-6; Ezek 25:1-11", target="Moab and Ammon",
     prediction="Moab and Ammon destroyed, Ammon 'not remembered among the nations' (Ezek 25:10); yet 'I will restore the "
                "fortunes' of Moab and of Ammon (Jer 48:47; 49:6).",
     event="582 campaign (Josephus); both peoples disappear as distinct nations by Hellenistic times; Rabbah = Amman",
     event_date=-582),
dict(id="B15", refs="Jer 49:7-22; Ezek 25:12-14; 35:1-15; Obad 1-21; Isa 34:5-17; Mal 1:2-5", target="Edom",
     prediction="Edom made desolate 'like Sodom', no one will live there (Jer 49:18; Ezek 35:9); 'no survivor of the "
                "house of Esau' (Obad 18).",
     event="552 Nabonidus' campaign; Nabataeans take Edom's land (Petra a capital in the 1st c. CE); Idumeans in S. Judah "
           "forcibly made Jews c. 112-108 BCE; Edomites vanish as a people after 70 CE", event_date=-552),
dict(id="B16a", refs="Isa 13:17-19; 21:2; 21:9; Jer 51:11; 51:27-28; 51:31", target="Babylon's capture",
     prediction="God stirs up the Medes (Isa 13:17; Jer 51:11, 28), with Elam (Isa 21:2), and Ararat, Minni and Ashkenaz "
                "(Jer 51:27) against Babylon; Babylon falls ('Fallen, fallen is Babylon', Isa 21:9); its gods' images shattered.",
     event="539: Cyrus (king of Anshan in Elam, ruler of Media since 550) takes Babylon 'without battle'; gods returned, "
           "not shattered", event_date=-539),
dict(id="B16b", refs="Isa 13:19-22; 14:22-23; Jer 50:13; 50:39-40; 51:26; 51:29; 51:37; 51:43; 51:62", target="Babylon's future",
     prediction="Babylon like Sodom and Gomorrah, never inhabited for all generations, no Arab will pitch a tent there, "
                "shepherds will not rest flocks there (Isa 13:19-20); 'no stone will be taken from you for a corner' "
                "(Jer 51:26); 'desolate forever' (51:62).",
     event="Babylon inhabited 539 BCE - 1st c. CE; deserted by the 2nd c. CE; its bricks were quarried for later towns",
     event_date=100),
dict(id="B17", refs="Isa 44:24-28; 45:1-7; 45:13; 46:1-2; 47:1-15; 48:14", target="Cyrus and Babylon",
     prediction="Cyrus (named) will subdue nations; doors opened before him so gates will not be shut (45:1); Bel and "
                "Nebo bow and go into captivity (46:1-2); Babylon's sudden ruin (47); Cyrus will say of Jerusalem 'she "
                "shall be built' and of the temple 'your foundation shall be laid' (44:28).",
     event="539 Babylon entered without battle; gods returned to their cities; return permitted (Ezra 1; 6:3-5)",
     event_date=-539),
dict(id="B18", refs="Hab 1:5-11", target="The Chaldeans",
     prediction="'I am raising up the Chaldeans' who will sweep across the earth to seize dwellings not their own.",
     event="Rise of the Neo-Babylonian empire 626-605", event_date=-605),
# ---------------------------------------------------------------- Persian / Hellenistic period
dict(id="C01", refs="Hag 2:20-23", target="Kingdoms of the nations; Zerubbabel",
     prediction="Dated 24.IX of Darius' 2nd year (520): God will overthrow the throne of kingdoms, chariots and riders; "
                "Zerubbabel will be God's signet ring.",
     event="No overthrow of the Persian empire; Zerubbabel disappears from the record", event_date=-515),
dict(id="C02", refs="Hag 2:6-9", target="The Second Temple",
     prediction="In a little while God will shake the nations; their treasures will come; the latter glory of this house "
                "will be greater than the former; 'in this place I will give peace'.",
     event="Herod's rebuilding (from 20/19 BCE); temple destroyed in war 70 CE", event_date=-19),
dict(id="C03", refs="Zech 4:9; 6:12-13", target="Zerubbabel and the temple",
     prediction="Zerubbabel's hands founded this house and his hands will finish it.",
     event="Temple completed 515 (Ezra 6:15; biblical record only)", event_date=-515),
dict(id="C04", refs="Zech 9:1-8", target="Syria, Phoenicia, Philistia",
     prediction="Hadrach, Damascus, Hamath, Tyre and Sidon; Tyre's rampart and heaped silver; she will be consumed by fire; "
                "Ashkelon, Gaza (its king perishes), Ekron, Ashdod; God encamps at his house so no oppressor passes.",
     event="332 Alexander's march: Tyre (7-month siege) and Gaza (commander Batis killed); Jerusalem not attacked",
     event_date=-332),
dict(id="C05", refs="Zech 9:13-16", target="Zion and Yavan (Greece)",
     prediction="'I will stir up your sons, O Zion, against your sons, O Yavan'; God will appear over them; they will win.",
     event="167-160 BCE Maccabean war against the Seleucid (Greek-Macedonian) kingdom; temple rededicated 164",
     event_date=-164),
dict(id="C06", refs="Obad 17-21", target="Edom, Philistia, Samaria, Gilead",
     prediction="The house of Jacob a fire, the house of Esau stubble, 'no survivor'; the Negev will possess Mount Esau, "
                "the Shephelah the Philistines; they will possess Ephraim and Samaria; Benjamin Gilead.",
     event="Hasmonean conquests: Gilead 163, coast 147-96, Idumea and Samaria c. 112-108, Transjordan under Jannaeus",
     event_date=-108),
dict(id="C07", refs="Isa 19:18-25", target="Egypt",
     prediction="Five cities in Egypt speaking 'the language of Canaan'; one called 'city of destruction/the sun'; an altar "
                "to YHWH in the midst of Egypt and a pillar at its border.",
     event="Elephantine temple (before 525); Onias IV's temple at Leontopolis (c. 160 BCE), whose founder cited this "
           "prophecy", event_date=-160),
dict(id="C08", refs="Joel 4:4-8", target="Tyre, Sidon, Philistia",
     prediction="They sold Judeans to the Greeks (Yevanim); God will sell their sons and daughters into the hand of the "
                "people of Judah, who will sell them to the Sabeans.",
     event="332 Alexander sells the population of Tyre and Gaza into slavery (Macedonians, not Judeans)", event_date=-332),
# ---------------------------------------------------------------- Roman period (texts provably older)
dict(id="D01", refs="Dan 9:24-27", target="Jerusalem and the sanctuary",
     prediction="70 sevens; after 7+62 an anointed one cut off; 'the people of the leader who is to come will destroy the "
                "city and the sanctuary', its end with a flood; for half a seven sacrifice and offering cease; an "
                "abomination that desolates.",
     event="167-164 BCE: sacrifice stopped, altar desecrated, city partly burnt  |  70 CE: city and temple destroyed by Rome",
     event_date=70),
dict(id="D02", refs="Hos 3:4-5", target="Israel",
     prediction="The Israelites will dwell many days without king or prince, without sacrifice or pillar, without ephod "
                "or teraphim; afterwards they will return and seek YHWH and 'David their king'.",
     event="No king or sacrifice after 70 CE; but also kingship and sacrifice existed 515 BCE-70 CE", event_date=70),
dict(id="D03", refs="Jer 30:11; 31:35-37; 46:28; Amos 9:8-9", target="Jacob/Israel among the nations",
     prediction="God will make a full end of the nations to which he scattered Israel, but not of Israel; Israel shaken "
                "among the nations as in a sieve, yet not a pebble falls.",
     event="Survival of Jewish identity in dispersion; Assyria and Babylonia ended as states (as did many others)",
     event_date=100),
dict(id="D04", refs="Isa 11:11-16; Jer 16:14-15; Ezek 36:24; 37:21-22; Amos 9:14-15", target="Return from dispersion",
     prediction="A second recovery of the remnant from Assyria, Egypt, Pathros, Cush, Elam, Shinar, Hamath and the "
                "coastlands; Ephraim and Judah reunited and plunder Philistia, Edom, Moab, Ammon; the Sea of Egypt dried; "
                "'they will never again be uprooted' (Amos 9:15).",
     event="538 BCE onward returns under Persia; uprooting 70/135 CE; modern immigration from 1882 and statehood 1948",
     event_date=1948),
]
