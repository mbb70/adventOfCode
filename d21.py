import sys
import itertools

def battle(you, boss):
    while you and boss:
        you.hit(boss)
        if boss:
            boss.hit(you)
    return you.__bool__()

class Player:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def hit(self, op):
        op.health -= max(1, (self.damage - op.armor))

    def __bool__(self):
        return self.health > 0

weapons, armors, rings = [], [], []
weapons.append((    'Dagger',   8,  4,  0))
weapons.append(('Shortsword',  10,  5,  0))
weapons.append(( 'Warhammer',  25,  6,  0))
weapons.append(( 'Longsword',  40,  7,  0))
weapons.append((  'Greataxe',  74,  8,  0))
armors.append((   'No Armor',  0,   0,  0))
armors.append((    'Leather',  13,  0,  1))
armors.append((  'Chainmail',  31,  0,  2))
armors.append((  'Splitmail',  53,  0,  3))
armors.append(( 'Bandedmail',  75,  0,  4))
armors.append((  'Platemail', 102,  0,  5))
rings.append((   'No Ring 1',   0,  0,  0))
rings.append((   'No Ring 2',   0,  0,  0))
rings.append((   'Damage +1',  25,  1,  0))
rings.append((   'Damage +2',  50,  2,  0))
rings.append((   'Damage +3', 100,  3,  0))
rings.append((  'Defense +1',  20,  0,  1))
rings.append((  'Defense +2',  40,  0,  2))
rings.append((  'Defense +3',  80,  0,  3))

h = {}
health = 100
bhealth, bdamage, barmor = (int(s.split(':')[1].strip()) for s in sys.stdin.readlines())
for weapon in weapons:
    for armor in armors:
        for r1, r2 in itertools.combinations(rings, 2):
            cost = weapon[1] + armor[1] + r1[1] + r2[1]
            tdamage, tarmor = (sum(x) for x in zip(weapon[2:], armor[2:], r1[2:], r2[2:]))
            names = frozenset((weapon[0], armor[0], r1[0], r2[0]))
            boss = Player(bhealth, bdamage, barmor)
            you = Player(health, tdamage, tarmor)
            h[names] = (cost, battle(you, boss))

print('Lowest cost to win:', min((c for (c, o) in h.values() if o)))
print('Highest cost to lose:', max((c for (c, o) in h.values() if not o)))

