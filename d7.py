import sys
import re

def exec_instr(instr):
    if instr.isnumeric():
        return int(instr)
    elif defs.get(instr):
        return defs[instr]
    elif instr.startswith('NOT'):
        return ~defs[instr.replace('NOT ', '')] % 65536
    else:
        m = re.match(r'([a-z0-9]+) (\w+) ([a-z0-9]+)', instr)
        f, a, s = [m.group(i+1) for i in range(3)]
        f = int(f) if f.isnumeric() else defs[f]
        s = int(s) if s.isnumeric() else defs[s]
        if a == 'AND':
            return f & s % 65536
        elif a == 'OR':
            return f | s % 65536
        elif a == 'LSHIFT':
            return f * 2**s % 65536
        elif a == 'RSHIFT':
            return int(f / 2**s) % 65536

def tsort(t):
    p = set()
    while t:
        r = []
        for i, d in t:
            if p.issuperset(d):
                yield i
                p.add(i)
            else:
                r.append((i,d))
        t = r

lines = sys.stdin.readlines()
t = [re.findall(r'[a-z][a-z]?', line) for line in lines]
t = list(tsort([ (x[-1], x[:-1]) for x in t ]))

l = { re.findall(r'[a-z][a-z]?', line)[-1] : line.strip() for line in lines }
sorted_lines = [ l[i] for i in t ]

defs = {}
for line in sorted_lines:
    instr, assign = line.split(' -> ')
    defs[assign] = exec_instr(instr)
print("Value of a:", defs['a'])

l['b'] = '{} -> b'.format(defs['a'])
defs = {}
sorted_lines = [ l[i] for i in t ]
for line in sorted_lines:
    instr, assign = line.split(' -> ')
    defs[assign] = exec_instr(instr)
print("Value of a after reseting value of b:", defs['a'])

