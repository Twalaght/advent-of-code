#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(",") for x in f.read().splitlines()]

data = [tuple([int(y) for y in x]) for x in data]
cubes = set(data)

def check(cube):
	score = 0
	for mod in [-1, 1]:
		x = (cube[0] + mod, cube[1], cube[2])
		y = (cube[0], cube[1] + mod, cube[2])
		z = (cube[0], cube[1], cube[2] + mod)

		if x not in cubes: score += 1
		if y not in cubes: score += 1
		if z not in cubes: score += 1

	return score

silver = 0
for cube in cubes: silver += check(cube)

sys.setrecursionlimit(100000)
limit = max([max(x) for x in cubes]) + 2
outside = set()
def flood(cube):
	if cube in outside: return

	if cube[0] > limit or cube[0] < -2: return
	if cube[1] > limit or cube[1] < -2: return
	if cube[2] > limit or cube[2] < -2: return

	outside.add(cube)

	for mod in [-1, 1]:
		x = (cube[0] + mod, cube[1], cube[2])
		y = (cube[0], cube[1] + mod, cube[2])
		z = (cube[0], cube[1], cube[2] + mod)

		for c in [x, y, z]:
			if c not in cubes and c not in outside:
				flood(c)

def check_gold(cube):
	score = 0
	for mod in [-1, 1]:
		x = (cube[0] + mod, cube[1], cube[2])
		y = (cube[0], cube[1] + mod, cube[2])
		z = (cube[0], cube[1], cube[2] + mod)

		for c in [x, y, z]:
			if c not in cubes and c in outside:
				score += 1

	return score

flood((0, 0, 0))
gold = 0
for cube in cubes: gold += check_gold(cube)

print(f"Silver: {silver}\nGold: {gold}")
