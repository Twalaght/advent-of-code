#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

elves = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "#"]

def propose(elf, n):
	all_elves = set(elves)
	grid = [(elf[0] + x, elf[1] + y) for y in [-1, 0, 1] for x in [-1, 0, 1]]

	# If alone, do nothing
	if set(grid[:4] + grid[-4:]).isdisjoint(all_elves): return None

	chk = [grid[:3], grid[-3:], [grid[0], grid[3], grid[6]], [grid[2], grid[5], grid[8]]]
	rets = [grid[1], grid[7], grid[3], grid[5]]

	for i in range(4):
		i = (i + n) % 4
		if all_elves.isdisjoint(set(chk[i])): return rets[i]

def filter(props):
	dests = [x[1] for x in props]
	return {prop[0]:prop[1] for prop in props if dests.count(prop[1]) == 1}

silver, gold = 0, 0
for n in range(int(1e7)):
	props = []
	for x in elves:
		tmp = propose(x, n)
		if tmp: props.append([x, tmp])

	moves = filter(props)

	if not moves:
		gold = n + 1
		break

	for i in range(len(elves)):
		if elves[i] in moves: elves[i] = moves[elves[i]]

	if n == 10:
		x_rng, y_rng = [x[0] for x in elves], [x[1] for x in elves]
		x, y = max(x_rng) - min(x_rng) + 1, max(y_rng) - min(y_rng) + 1
		silver = x * y - len(elves)

print(f"Silver: {silver}\nGold: {gold}")
