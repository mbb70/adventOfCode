import sys
import itertools

inp = sys.stdin.read().strip()
for i in range(50):
    if i == 40:
        print("Length after 40 iterations:", len(s))
    s = []
    for n,g in itertools.groupby(inp):
        s.extend([str(len(list(g))),n])
    inp = s
print("Length after 50 iterations:", len(s))

