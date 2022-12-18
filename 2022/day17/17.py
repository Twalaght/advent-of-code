#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()][0]

rocks = [[(2, 3), (3, 3), (4, 3), (5, 3)],        # Horizontal bar
		[(3, 3), (2, 2), (3, 2), (4, 2), (3, 1)], # Plus sign
		[(2, 3), (3, 3), (4, 3), (4, 2), (4, 1)], # Backwards L
		[(2, 3), (2, 2), (2, 1), (2, 0)],         # Vertial bar
		[(2, 3), (3, 3), (2, 2), (3, 2)]]         # Square

def move(d, rock, grid):
	dropped = [[x[0], x[1] + 1] for x in rock]
	for node in dropped:
		if grid[node[1]][node[0]] == 1:
			return False

	mod = 1 if d == ">" else -1
	moved = [[x[0] + mod, x[1]] for x in dropped]

	for node in moved:
		if node[0] > 6 or node[0] < 0: return dropped
		if grid[node[1]][node[0]] == 1: return dropped

	return moved

grid = [[1, 1, 1, 1, 1, 1, 1]]
for _ in range(8): grid.insert(0, [0, 0, 0, 0, 0, 0, 0])

height = []
for i in range(4000):
	if i == 2022: silver = len(grid) - 9

	# Get the current for every round of 5 blocks
	if i % 5 == 0: height.append(len(grid) - 9)

	rock = rocks[i % 5]
	while True:
		res = move(data[0], rock, grid)
		if not res:
			for x in rock: grid[x[1]][x[0]] = 1
			break

		rock = res
		data = data[1:] + data[0]

	for _ in range(sum([1 for x in grid[:8] if any(x)])):
		grid.insert(0, [0, 0, 0, 0, 0, 0, 0])

# Make heights relative and find a cycle
height = [height[i + 1] - height[i] for i in range(len(height) - 1)][::-1]
for i in range(1, 400):
	cycle = tuple(height[:i])
	if cycle == tuple(height[i:i * 2]):
		break

cycles, extra = divmod(int(2e11) - len(height), len(cycle))
gold = sum(height) + (cycles * sum(cycle)) + sum(cycle[::-1][:extra])
print(f"Silver: {silver}\nGold: {gold}")
