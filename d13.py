import sys
import itertools
import re

def seat_guests(inp, with_you):
    c = {}
    peps = set()
    for line in inp:
        m = re.search(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)', line.strip())
        a,d,h,b = [m.group(i+1) for i in range(4)]
        h = int(h)
        if d == 'lose': h = -h
        c[a] = c.get(a, {})
        c[a][b] = h
        peps.update([a])

    if with_you:
        c['You'] = {s : 0 for s in peps}
        for p in peps:
            c[p]['You'] = 0
        peps.update(['You'])

    max_hap = 0
    for p in itertools.permutations(peps):
        hap = 0
        for i,o in enumerate(p):
            pre, nex = p[(i-1) % len(p)], p[(i+1) % len(p)]
            hap += c[o][pre] + c[o][nex]
        max_hap = max(hap, max_hap)
    return max_hap

inp = sys.stdin.readlines()
print("Maximum Happiness without you:", seat_guests(inp, with_you=False))
print("Maximum Happiness with you:", seat_guests(inp, with_you=True))

