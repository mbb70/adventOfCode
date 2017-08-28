import sys
import math
import itertools
import re

h = {}
starts = set()
for line in sys.stdin:
    m = re.search('(\w+) to (\w+) = (\d+)', line)
    s, e, d = [ m.group(i+1) for i in range(3) ]
    d = int(d)
    lh = h.get(s, {})
    lh[e] = d
    h[s] = lh

    lh = h.get(e, {})
    lh[s] = d
    h[e] = lh

    starts.update([s,e])

min_t = math.inf
max_t = 0
for path in itertools.permutations(starts):
    total = 0
    for s,e in zip(path, path[1:]):
        total += h[s][e]
    min_t = min([total, min_t])
    max_t = max([total, max_t])
print("Minimum path:", min_t)
print("Maximum path:", max_t)

