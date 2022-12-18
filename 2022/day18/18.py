#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(",") for x in f.read().splitlines()]

cubes = set([tuple([int(i) for i in x]) for x in data])

def traverse(cube):
	out = []
	for mod in [-1, 1]:
		out.append((cube[0] + mod, cube[1], cube[2]))
		out.append((cube[0], cube[1] + mod, cube[2]))
		out.append((cube[0], cube[1], cube[2] + mod))

	return out

def flood(cube, outside, limit):
	outside.add(cube)

	for c in traverse(cube):
		if c not in cubes and c not in outside:
			in_range = [-1 <= cube[i] <= limit for i in [0, 1, 2]]
			if all(in_range): outside = flood(c, outside, limit)

	return outside

def check(cube, gold):
	score = 0
	for c in [x for x in traverse(cube) if x not in cubes]:
		if gold and c not in gold: continue
		score += 1

	return score

sys.setrecursionlimit(10000)
outside = flood((0, 0, 0), set(), max([max(x) for x in cubes]) + 1)

silver = sum([check(x, False) for x in cubes])
gold = sum([check(x, outside) for x in cubes])
print(f"Silver: {silver}\nGold: {gold}")
