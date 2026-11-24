import sys
sys.path.insert(0, sys.argv[1])
from tf import read_tf
D = sys.argv[2]
m, scroll = read_tf(D + '/scroll.tf')
names = {}
for n, v in scroll.items():
    if 1605868 <= n <= 1606868:
        names.setdefault(v, []).append(n)
for k in sorted(names):
    if k.startswith('Mas') or k in ('2Q18', '11Q5'):
        print(k, names[k])
