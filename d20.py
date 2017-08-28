import sys

def factor(h, a):
    factors = set([h])
    min_ = h // 50 + 1
    for i in range(1, int(h**0.5) + 1):
        if h % i == 0:
            o = h // i
            if (a or i > min_): factors.add(i)
            if (a or o > min_): factors.add(o)
    return factors

inp = int(sys.stdin.read().strip())
def find_house(a):
    m, t, h = 0, 0, 0
    while t <= inp:
        h += 1
        t = sum((r*(10 + (not a)) for r in factor(h,a)))
    return h

print('Lowest number house with all elves visiting all houses:', find_house(True))
print('Lowest number house with elves visiting 50 houses:', find_house(False))
