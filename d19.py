import sys
import random
import re

repls = list()
m = ''
for line in sys.stdin:
    line = line.strip()
    try:
        cs, repl = line.split(' => ')
        repls.append((cs,repl))
    except ValueError:
        if line: m = line
n = set()
for r in repls:
    for match in re.finditer(r[0], m):
        s,e = match.span()
        n.add(m[:s] + r[1] + m[e:])
print('Total number of possible molecules after 1 replacement:', len(n))

def replace(st, i):
    if st == 'e': return i
    for r in repls:
        match = re.search(r[1], st)
        if match:
            s,e = match.span()
            return replace(st[:s] + r[0] + st[e:], i + 1)

searching = True
while searching:
    i = replace(m, 0)
    if i:
        print('Minimum number of replacement required:', i)
        searching = False
    else:
        random.shuffle(repls)

