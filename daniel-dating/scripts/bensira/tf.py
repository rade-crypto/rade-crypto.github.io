import sys, os, re
def read_tf(path):
    """Return (meta, data) where data maps node->value (node features) or node->set (edges)."""
    meta = {}
    data = {}
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    i = 0
    while i < len(lines) and lines[i].startswith('@'):
        l = lines[i]
        if '=' in l:
            k, v = l[1:].split('=', 1); meta[k] = v
        else:
            meta[l[1:]] = True
        i += 1
    # blank line separates
    if i < len(lines) and lines[i] == '':
        i += 1
    isedge = meta.get('edge', False)
    node = 0
    for l in lines[i:]:
        if l == '' and False:
            continue
        if '\t' in l:
            parts = l.split('\t')
            spec = parts[0]
            val = '\t'.join(parts[1:]) if len(parts) > 1 else ''
            if spec == '':
                nodes = [node + 1]
            else:
                nodes = []
                for p in spec.split(','):
                    if '-' in p:
                        a, b = p.split('-'); nodes.extend(range(int(a), int(b) + 1))
                    else:
                        nodes.append(int(p))
        else:
            nodes = [node + 1]; val = l
        for n in nodes:
            data[n] = val
        node = nodes[-1]
    return meta, data
