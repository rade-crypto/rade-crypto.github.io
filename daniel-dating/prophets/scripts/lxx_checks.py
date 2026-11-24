"""Print the Old Greek (Rahlfs, CenterBLC) of verses where names or wording matter for dating."""
import os, glob
from tf.fabric import Fabric
LP = glob.glob(os.path.expanduser("~/text-fabric-data/github/CenterBLC/LXX/tf/*"))[0]
A = Fabric(locations=LP, silent="deep").load("book chapter verse word", silent="deep")
F, L, T = A.F, A.L, A.T
CHECK = [  # (label, lxx book, ch, v)
 ("Isa 20:1 (Sargon, Tartan)", "Isa", 20, 1),
 ("Isa 13:17 (Medes)", "Isa", 13, 17), ("Isa 21:2 (Elam, Media)", "Isa", 21, 2), ("Isa 21:9", "Isa", 21, 9),
 ("Isa 44:28 (Cyrus)", "Isa", 44, 28), ("Isa 45:1", "Isa", 45, 1), ("Isa 19:18 (city name)", "Isa", 19, 18),
 ("Jer 25:1 MT=LXX 25:1", "Jer", 25, 1), ("Jer 25:9", "Jer", 25, 9), ("Jer 25:11", "Jer", 25, 11), ("Jer 25:12", "Jer", 25, 12),
 ("Jer 29:10 MT = LXX 36:10", "Jer", 36, 10),
 ("Jer 51:11 MT = LXX 28:11", "Jer", 28, 11), ("Jer 51:27 MT = LXX 28:27", "Jer", 28, 27), ("Jer 51:28 MT = LXX 28:28", "Jer", 28, 28),
 ("Jer 44:30 MT = LXX 51:30 (Hophra)", "Jer", 51, 30), ("Jer 26:18 MT = LXX 33:18 (quotes Micah)", "Jer", 33, 18),
 ("Mic 3:12", "Mic", 3, 12), ("Ezek 26:12", "Ezek", 26, 12), ("Ezek 26:14", "Ezek", 26, 14), ("Ezek 29:18", "Ezek", 29, 18),
 ("Amos 3:9 (MT Ashdod)", "Amos", 3, 9), ("Hos 10:6", "Hos", 10, 6), ("Nah 2:7", "Nah", 2, 7), ("Zeph 2:13", "Zeph", 2, 13),
 ("Zech 9:13 (Yavan)", "Zech", 9, 13), ("Obad 18", "Obad", 1, 18), ("Obad 19", "Obad", 1, 19), ("Obad 20", "Obad", 1, 20),
 ("Dan 9:25 OG", "Dan", 9, 25), ("Dan 9:26 OG", "Dan", 9, 26), ("Dan 9:27 OG", "Dan", 9, 27),
 ("Dan 9:26 Theod.", "DanTh", 9, 26), ("Dan 11:30 OG (Kittim)", "Dan", 11, 30),
 ("Tobit 14:4 (B/A text)", "TobBA", 14, 4), ("Tobit 14:4 (Sinaiticus)", "TobS", 14, 4), ("Tobit 14:8 (Sinaiticus)", "TobS", 14, 8),
 ("Sirach 48:24", "Sir", 48, 24), ("Sirach 49:7", "Sir", 49, 7), ("Sirach 49:8", "Sir", 49, 8), ("Sirach 49:10", "Sir", 49, 10),
]
out = ["# Old Greek wording of verses relevant to dating (Rahlfs 1935, CenterBLC Text-Fabric)\n"]
for lab, b, c, v in CHECK:
    n = T.nodeFromSection((b, c, v))
    txt = " ".join(F.word.v(w) for w in L.d(n, "word")) if n else "(verse not in this edition)"
    out.append(f"- **{lab}**: {txt}")
open(os.path.join(os.path.dirname(__file__), "..", "results", "lxx_key_verses.md"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
