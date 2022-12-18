#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()][0]

rocks = [[(2, 3), (3, 3), (4, 3), (5, 3)],        # Horizontal bar
		[(3, 3), (2, 2), (3, 2), (4, 2), (3, 1)], # Plus sign
		[(2, 3), (3, 3), (4, 3), (4, 2), (4, 1)], # Backwards L
		[(2, 3), (2, 2), (2, 1), (2, 0)],         # Vertial bar
		[(2, 3), (3, 3), (2, 2), (3, 2)]]         # Square

def drop(rock, grid):
	new = [[x[0], x[1] + 1] for x in rock]
	for node in new:
		if grid[node[1]][node[0]] == 1:
			return "DONE"

	return new

def move(d, rock, grid):
	mod = 1 if d == ">" else -1
	moved = [[x[0] + mod, x[1]] for x in rock]

	valid = True
	for node in moved:
		if node[0] > 6 or node[0] < 0:
			valid = False
			break

		if grid[node[1]][node[0]] == 1:
			valid = False
			break

	if valid:
		return moved
	else:
		return rock

grid = [[1, 1, 1, 1, 1, 1, 1]]
for _ in range(8): grid.insert(0, [0, 0, 0, 0, 0, 0, 0])

h = []
for i in range(4000):
	if i == 2022:
		silver = len(grid) - 9

	# Get change for every 5 blocks
	if i % 5 == 0: h.append(len(grid) - 9)

	rock = rocks[i % 5]

	while True:
		d = data[0]
		res = drop(rock, grid)

		if res == "DONE":
			for x in rock:
				grid[x[1]][x[0]] = 1

			break

		rock = move(d, res, grid)
		data = data[1:] + data[0]

	ctr = 0
	for g in range(len(grid)):
		if tuple(grid[g]) == (0, 0, 0, 0, 0, 0, 0):
			ctr += 1

	for _ in range(8 - ctr):
		grid.insert(0, [0, 0, 0, 0, 0, 0, 0])

# Make heights relative
h = [h[i + 1] - h[i] for i in range(len(h) - 1)][::-1]

# Find a cycle
cycle_len = -1
delta = -1
loop = []
for i in range(1, 400):
	p1 = tuple(h[:i])
	p2 = tuple(h[i:i*2])

	if p1 == p2:
		loop = p1
		cycle_len = len(p1)
		delta = sum(p1)
		break

# Interp everything in groups of 5
cycles = 1000000000000 // 5
cycles = (cycles - len(h)) // cycle_len

gold = sum(h) + (cycles * delta)
extra = (1000000000000 // 5 ) - (cycles * cycle_len + len(h))
gold += sum(loop[::-1][:extra])

print(f"Silver: {silver}\nGold: {gold}")
