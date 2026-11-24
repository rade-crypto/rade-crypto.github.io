"""Attach the hand-check verdicts (made by reading each line in context) to the sample files."""
import sys, os
d = sys.argv[1]
J = {
 "sample_tstem.tsv": ({39: "FP: 1cs impf 'I will meet'", 64: "FP: 1cs impf 'I will turn'", 99: "FP: 1cs impf 'let me avenge'",
                       103: "FP: 1cs impf 'I will reveal myself'", 168: "FP: 1cs impf 'I will avenge'"}, "OK t-stem perf/impv/inf"),
 "sample_procd.tsv": ({28: "FP: root dbr 'I took'", 124: "FP: darom 'south'"}, "OK proclitic d-"),
 "sample_caus.tsv": ({9: "1cs impf", 13: "1cs impf", 14: "imperative", 25: "1cs impf", 29: "1cs impf", 31: "1cs impf",
                      32: "1cs impf", 34: "1cs impf", 40: "1cs impf", 45: "1cs impf", 51: "1cs impf", 53: "1cs impf",
                      54: "imperative", 55: "1cs impf (prob.)", 61: "imperative", 69: "imperative", 72: "imperative"}, "perfect"),
}
for fn, (bad, ok) in J.items():
    p = os.path.join(d, fn)
    lines = [l.rstrip("\n").split("\t")[:4] for l in open(p, encoding="utf-8")]
    with open(p.replace(".tsv", "_judged.tsv"), "w", encoding="utf-8") as f:
        f.write("n\tref\tvocalised\tcontext\tverdict\n")
        for row in lines:
            f.write("\t".join(row + [bad.get(int(row[0]), ok)]) + "\n")
    print(fn, len(lines), "lines;", len(bad), "flagged")
