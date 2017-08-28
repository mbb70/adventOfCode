import sys
import math
import heapq

class Node:
    def __init__(self, youh, bossh, bossd, ymana, smana, effects, hmode):
        self.youh = youh
        self.bossh = bossh
        self.bossd = bossd
        self.ymana = ymana
        self.smana = smana
        self.effects = effects
        self.hmode = hmode

    def run_effects(self):
        for effect in self.effects:
            self.effects[effect] -= 1
            if effect is 'posion':
                self.bossh -= 3
            elif effect is 'recharge':
                self.ymana += 101
        self.effects = { e : v for e,v in self.effects.items() if v > 0 }

    def attack_options(self):
        effects = [e for e, v in self.effects.items() if v > 1]
        return set(['missile', 'drain', 'shield', 'posion', 'recharge']).difference(effects)

    def copy(self):
        return Node(self.youh, self.bossh, self.bossd, self.ymana, self.smana, self.effects.copy(), self.hmode)

    def spend_mana(self, m):
        self.ymana -= m
        self.smana += m

    def yattack(self, attack):
        if attack is 'shield':
            self.spend_mana(113)
            self.effects[attack] = 6
        elif attack is 'posion':
            self.spend_mana(173)
            self.effects[attack] = 6
        elif attack is 'recharge':
            self.spend_mana(229)
            self.effects[attack] = 5
        elif attack is 'missile':
            self.spend_mana(53)
            self.bossh -= 4
        elif attack is 'drain':
            self.spend_mana(73)
            self.bossh -= 2
            self.youh += 2

    def battack(self):
        self.youh -= max(1, self.bossd - (7 if 'shield' in self.effects else 0))

    def children(self):
        children = []
        for attack in self.attack_options():
            s = self.copy()

            if s.hmode:
                s.youh -= 1
                if s.youh == 0: continue
            s.run_effects()
            s.yattack(attack)

            s.run_effects()
            if s.bossh > 0:
                s.battack()

            if s.youh > 0 and s.ymana > 0:
                children.append(s)
        return children

    def __lt__(self, other):
        return self.smana < other.smana

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return "{} {} {} {}".format(self.youh, self.bossh, self.ymana, self.effects)

class PriorityQueue:
    def __init__(self, q):
        self.q = q
        self.in_q = set(q)

    def pop(self, index=0):
        item = self.q.pop(index)
        self.in_q.remove(item)
        return item

    def remove(self, item):
        self.q.remove(item)
        self.in_q.remove(item)

    def add(self, item):
        heapq.heappush(self.q, item)
        self.in_q.add(item)

    def get(self, item):
        return self.q[self.q.index(item)]

    def replace(self, item):
        self.remove(item)
        self.add(item)

    def __bool__(self):
        return len(self.q) != 0

    def __contains__(self, item):
        return item in self.in_q

def dijkstra(node):
    q = PriorityQueue([node])
    visited = set()
    lowest = math.inf
    while q:
        current = q.pop()
        if current.bossh <= 0 and current.smana < lowest:
            lowest = current.smana
        visited.add(current)
        for child in current.children():
            if child.smana > lowest: continue
            if child not in visited:
                if child not in q:
                    q.add(child)
                elif q.get(child).smana > child.smana:
                    q.replace(child)
    return lowest

def main():
    bossh, bossd = (int(s.split(':')[1].strip()) for s in sys.stdin.readlines())
    start = Node(50, bossh, bossd, 500, 0, {}, False)
    print('Easy Mode: ', dijkstra(start))
    start = Node(50, bossh, bossd, 500, 0, {}, True)
    print('Hard Mode: ', dijkstra(start))

if __name__ == '__main__':
    main()

