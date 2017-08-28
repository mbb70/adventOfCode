import sys
import itertools
import re

def inc(st):
    if not st:
        st = [0]
    elif st[-1] != 25:
        st[-1] += 1
    else:
        st = inc(st[:-1])
        st.append(0)
    return st

def acceptable(pwd):
    no_iol = not iol.intersection(pwd)
    repeaters = [True for n,g in itertools.groupby(pwd) if len(list(g)) >= 2]
    seq = False
    for a,b,c in zip(pwd,pwd[1:],pwd[2:]):
        if c - b == 1 and b - a == 1:
            seq = True
    return seq and no_iol and len(repeaters) >= 2

m = {c: ord(c) - 97 for c in 'abcdefghijklmnopqrstuvwxyz'}
b = dict((v,k) for k,v in m.items())
iol = set([m[c] for c in 'iol'])

pwd = [ord(c) - 97 for c in sys.stdin.read().strip()]
while not acceptable(pwd): pwd = inc(pwd)
print("First acceptable password:", ''.join([b[c] for c in pwd]))

pwd = inc(pwd)
while not acceptable(pwd): pwd = inc(pwd)
print("Second acceptable password:", ''.join([b[c] for c in pwd]))

