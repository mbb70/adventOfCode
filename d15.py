import sys
import re
from itertools import zip_longest

ings = {}
for line in sys.stdin:
    m = re.search(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)', line)
    n = m.group(1)
    c, d, f, t, cal = [int(m.group(i+2)) for i in range(5)]
    ings[n] = (c,d,f,t,cal)

combs = []
def left(l, rec):
    if len(rec) == len(ings) - 1:
        return combs.append(rec + [100 - sum(rec)])
    for i in range(1, l):
        left(l - i, rec + [i])
left(100, [])

tots = []
tots_500 = []
for opts in combs:
    t = []
    tot = 1
    for i,ing in enumerate(ings):
        t = [sum(l) for l in zip_longest(t, [opts[i]*v for v in ings[ing]], fillvalue=0)]
    for amt in t[:-1]:
        tot *= max(amt, 0)
    if t[-1] == 500:
        tots_500.append(tot)
    tots.append(tot)
print('Top Score:', max(tots))
print('Top Score with 500 calories:', max(tots_500))

