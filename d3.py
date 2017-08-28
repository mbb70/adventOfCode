import sys

def update_cord(d, cord, houses):
    if d is '>':
        cord[0] -= 1
    elif d is '<':
        cord[0] += 1
    elif d is '^':
        cord[1] += 1
    elif d is 'v':
        cord[1] -= 1
    houses.add(','.join([str(c) for c in cord]))

pair = set(['0,0'])
solo = set(['0,0'])
for line in sys.stdin:
    cord0, cord1, cord2 = [0,0], [0,0], [0,0]
    for d1, d2 in zip(*[iter(line)]*2):
        update_cord(d1, cord0, solo)
        update_cord(d2, cord0, solo)
        update_cord(d1, cord1, pair)
        update_cord(d2, cord2, pair)

print("Houses Visited Solo:", len(solo))
print("Houses Visited Pair:", len(pair))

