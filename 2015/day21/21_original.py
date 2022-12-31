#!/usr/bin/python3

import sys
from itertools import combinations
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

boss = [int(x.split()[-1]) for x in data]

weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armours = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

def fight(you, boss):
	for i in range(int(1e7)):
		# Player turn
		if i % 2 == 0:
			hit = max(you[1] - boss[2], 1)
			boss[0] -= hit
		else:
			hit = max(boss[1] - you[2], 1)
			you[0] -= hit

		if you[0] <= 0: return False
		if boss[0] <= 0: return True

# Add the options of nothing
armours += [[0, 0, 0]]
rings += [[0, 0, 0], [0, 0, 0]]

silver = int(1e7)
gold = 0
for w in weapons:
	for a in armours:
		for r in combinations(rings, 2):
			full = [w] + [a] + [r[0]] + [r[1]]
			you = [sum([x[i] for x in full]) for i in range(3)]
			cost = you[0]
			you[0] = 100

			if fight(you.copy(), boss.copy()):
				silver = min(cost, silver)
			else:
				gold = max(cost, gold)

print(f"Silver: {silver}\nGold: {gold}")
