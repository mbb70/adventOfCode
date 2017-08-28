import sys
import re

m = re.search(r'row (\d+), column (\d+)', sys.stdin.read())
row, col = [int(m.group(i+1)) for i in range(2)]
goal = sum(range(1, col + 1)) + sum(range(col, col + row - 1))
current = 20151125
for i in range(1, goal):
    current = current * 252533 % 33554393
print(current)

