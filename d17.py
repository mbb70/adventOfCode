import sys
from itertools import chain, combinations

jars = { i : int(j) for i,j in enumerate(sys.stdin.readlines()) }
h, few = set(), set()
fewest = len(jars)
for js in chain.from_iterable(combinations(jars, r) for r in range(len(jars))):
    if sum(jars[j] for j in js) == 150:
        h.add(frozenset(js))
        if len(js) < fewest:
            fewest = len(js)
            few = set()
        if len(js) == fewest:
            few.add(js)

print("Number of ways to fill:", len(h))
print("Number of ways to fill with fewest jars:", len(few))

