import sys, json, re, collections, glob, os
d = sys.argv[1]
for fn in sorted(glob.glob(os.path.join(d, "*.json"))):
    if "test_" in fn or "idx_" in fn or os.path.basename(fn).startswith("v_"): continue
    j = json.load(open(fn))
    def walk(x):
        if isinstance(x, str): yield x
        elif isinstance(x, list):
            for y in x: yield from walk(y)
    s = "\n".join(walk(j["text"]))
    c = collections.Counter(ch for ch in s if not ('א' <= ch <= 'ת') and not ('֑' <= ch <= 'ׇ') and ch not in ' \n')
    tags = collections.Counter(re.findall(r"<[^>]+>", s))
    print(os.path.basename(fn)[:60], len(s), dict(c.most_common(25)), dict(tags.most_common(6)))
