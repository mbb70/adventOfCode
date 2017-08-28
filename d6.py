import sys
import itertools
import re

instructions = sys.stdin.readlines()
def exec_instructions(part1):
    default = False if part1 else 0
    grid = [[default for j in range(1000)] for i in range(1000)]
    for line in instructions:
        m = re.search(r'(\w+) (\d+),(\d+) through (\d+),(\d+)', line)
        a = m.group(1)
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if a == 'on':
                    grid[x][y] = True if part1 else grid[x][y] + 1
                elif a == 'off':
                    grid[x][y] = False if part1 else max(grid[x][y] - 1, 0)
                elif a == 'toggle':
                    grid[x][y] = not grid[x][y] if part1 else grid[x][y] + 2
    return grid

print("Total number on:", sum(list(itertools.chain.from_iterable(exec_instructions(True))))))
print("Total brightness:", sum(list(itertools.chain.from_iterable(exec_instructions(False)))))

