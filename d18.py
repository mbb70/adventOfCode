import sys
import itertools

grid = [[False for _ in range(100)] for _ in range(100)]
igrid = [[False for _ in range(100)] for _ in range(100)]
for i,line in enumerate(sys.stdin):
    for j,c in enumerate(line.strip()):
        grid[i][j] = c == '#'
        igrid[i][j] = c == '#'

def nsur(x,y):
    tot = 0
    for xp in range(x-1, x+2):
        for yp in range(y-1,y+2):
            if xp == x and yp == y: continue
            if xp < 0 or yp < 0: continue
            try:
                tot += grid[xp][yp]
            except IndexError:
                pass
    return tot

def force_corners():
    for x,y in [(0,0),(-1,-1),(-1,0),(0,-1)]:
        grid[x][y] = True

def run_grid(con):
    for _ in range(100):
        if con: force_corners()
        to_tog = []
        for x, y in itertools.combinations(range(100), 2):
            #print(x,y)
            v = grid[x][y]
            n = nsur(x,y)
            if (v and n not in [2,3]) or (not v and n == 3):
                to_tog.append((x,y))
        for x,y in to_tog:
            grid[x][y] = not grid[x][y]
    if con: force_corners()
    return sum((sum(g) for g in grid))

print('Number of lights after 100 iterations:', run_grid(False))
grid = igrid
print('Number of lights after 100 iterations with corners always on:', run_grid(True))

