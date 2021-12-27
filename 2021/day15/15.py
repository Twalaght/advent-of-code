#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	infile = f.read().splitlines()

def setup(gold):
	size = len(infile) * (5 if gold else 1)

	data, grid = [], []
	for i in range(size): grid.append([9999] * size)
	for i in range(size): data.append([0] * size)

	if gold:
		for x in range(size):
			for y in range(size):
				add = (x // (size // 5)) + (y // (size // 5))
				data[x][y] = int(infile[x % (size // 5)][y % (size // 5)]) + add
				if data[x][y] > 9: data[x][y] = data[x][y] % 10 + 1
	else:
		for i in range(size): data[i] = [int(char) for char in infile[i]]

	return data, grid, size

def update(x, y, cost, data, grid, updates, size):
	if data[x][y] + cost >= grid[x][y]: return
	grid[x][y] = data[x][y] + cost

	tmp = []
	if x + 1 < size and grid[x + 1][y] > data[x + 1][y] + grid[x][y]:
		tmp.append([x + 1, y, grid[x][y]])
	if y + 1 < size and grid[x][y + 1] > data[x][y + 1] + grid[x][y]:
		tmp.append([x, y + 1, grid[x][y]])
	if x - 1 >= 0 and grid[x - 1][y] > data[x - 1][y] + grid[x][y]:
		tmp.append([x - 1, y, grid[x][y]])
	if y - 1 >= 0 and grid[x][y - 1] > data[x][y - 1] + grid[x][y]:
		tmp.append([x, y - 1, grid[x][y]])

	for i in tmp:
		idx = (i[0], i[1])
		if idx not in updates or updates[idx] > i[2]: updates[idx] = i[2]


def solve(gold):
	updates = {}
	data, grid, size = setup(gold)
	update(size - 1, size - 1, 0, data, grid, updates, size)

	while updates:
		tmp = updates
		updates = {}
		for i in tmp: update(i[0], i[1], tmp[i], data, grid, updates, size)

	return grid[0][0] - data[0][0]

silver, gold = solve(False), solve(True)
print(f"Silver: {silver}\nGold: {gold}")
