#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

elves = []

for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] == "#":
			elves.append((x, y))

def propose(elf, n):
	x, y = elf

	all_elves = set(elves)

	grid = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
			(x - 1, y), (x + 1, y),
			(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

	# If no neighbours, do nothing
	if not all_elves.intersection(set(grid)): return None

	n = n % 4
	moves = [all_elves.intersection(set(grid[:3])),
			all_elves.intersection(set(grid[-3:])),
			all_elves.intersection(set([grid[0], grid[3], grid[5]])),
			all_elves.intersection(set([grid[2], grid[4], grid[7]]))]

	rets = [grid[1], grid[6], grid[3], grid[4]]

	for _ in range(n):
		moves.append(moves.pop(0))
		rets.append(rets.pop(0))

	for i in range(4):
		if not moves[i]: return rets[i]

	return None

def filter(props):
	res = {}
	dests = [x[1] for x in props]
	for prop in props:
		if dests.count(prop[1]) == 1:
			res[prop[0]] = prop[1]

	return res

def solve(elves):
	xs = [x[0] for x in elves]
	ys = [x[1] for x in elves]
	x = max(xs) - min(xs) + 1
	y = max(ys) - min(ys) + 1

	res = (x * y) - len(elves)
	return res

old_elves = set(elves)
silver, gold = 0, 0

rounds = 1000000
for n in range(rounds):
	props = []
	for x in elves:
		tmp = propose(x, n)
		if tmp: props.append([x, tmp])

	moves = filter(props)

	if not moves:
		gold = n + 1
		break

	for i in range(len(elves)):
		if elves[i] in moves:
			elves[i] = moves[elves[i]]

	if n == 10: silver = solve(elves)

print(f"Silver: {silver}\nGold: {gold}")
