import sys
from itertools import combinations
from operator import mul
from functools import reduce

weights = [int(l) for l in sys.stdin.readlines()]
def find_lowest(c):
    ds = sum(weights) / c
    for size in range(len(weights)):
        for comb in combinations(weights, size):
            if sum(comb) == ds:
                return reduce(mul, comb)

for c in [3, 4]:
    print(c, 'sections:', find_lowest(c))

