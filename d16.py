import sys
import re

data = { 'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }
for line in sys.stdin:
    name = line.split(':')[0]
    a = re.findall(r'(\w+): (\d+)', line)
    sue = { k : int(v) for k,v in a }
    p1_ruled_out = False
    p2_ruled_out = False
    for d in data:
        try:
            if ((d in ['cats', 'trees'] and sue[d] <= data[d]) or
                (d in ['pomeranians', 'goldfish'] and sue[d] >= data[d]) or
                (d not in ['cats', 'trees', 'pomeranians', 'goldfish'] and sue[d] != data[d])):
                p2_ruled_out = True
            if data[d] != sue[d]:
                p1_ruled_out = True
        except KeyError:
            pass
    if not p1_ruled_out:
        print("Gift giver if exact results:", name)
    if not p2_ruled_out:
        print("Gift giver if range results:", name)

