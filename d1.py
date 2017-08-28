import sys
for line in sys.stdin:
    up = line.count('(')
    down = line.count(')')
    print("Final Floor:", up - down)

    floor = 0
    for i,char in enumerate(line):
        floor += 1 if char is '(' else -1
        if floor == -1:
            print("First Time in Basement:" i+1)
            exit()

