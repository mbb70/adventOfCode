import sys
import re

max_dist = 0
rs = {}
T = 2503
for line in sys.stdin:
    m = re.search(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds', line)
    n = m.group(1)
    s, t, r = [int(m.group(i+2)) for i in range(3)]
    scs = [0]
    ct = 0
    while ct < T + 2:
        scs.extend([scs[-1] + s*i for i in range(t + 1)])
        scs.extend([scs[-1] for i in range(r - 1)])
        ct += t + r
    scs = scs[2:(T + 2)]
    rs[n] = scs
print("Further Distanced Reached:", max(r[-1] for r in rs.values()))

points = {}
for t in range(T):
    mxs = {}
    for n,d in rs.items():
        mxs[d[t]] = mxs.get(d[t], [])
        mxs[d[t]].append(n)
    for i,n in enumerate(max(mxs.items())[1]):
        points[n] = points.get(n, 0)
        points[n] += 1
print("Most Points Earned:", max(points.values()))

