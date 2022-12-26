#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	infile = f.read().splitlines()

data = []
grid = []
size = len(infile)

for i in range(size): grid.append([int(1e9)] * size)
for i in range(size): data.append([int(0)] * size)

for i in range(size):
	data[i] = [int(char) for char in infile[i]]

updates = []
def update(x, y, cost):
	prop_cost = data[x][y] + cost

	if prop_cost < grid[x][y]:
		grid[x][y] = prop_cost
	else:
		return

	if x + 1 < size:
		if grid[x + 1][y] > data[x + 1][y] + grid[x][y]:
			updates.append([x + 1, y, grid[x][y]])
	if y + 1 < size:
		if grid[x][y + 1] > data[x][y + 1] + grid[x][y]:
			updates.append([x, y + 1, grid[x][y]])
	if x - 1 >= 0:
		if grid[x - 1][y] > data[x - 1][y] + grid[x][y]:
			updates.append([x - 1, y, grid[x][y]])
	if y - 1 >= 0:
		if grid[x][y - 1] > data[x][y - 1] + grid[x][y]:
			updates.append([x, y - 1, grid[x][y]])

update(size - 1, size - 1, 0)

while updates:
	tmp = {}
	for i in updates:
		idx = (i[0], i[1])

		if idx not in tmp:
			tmp[idx] = i[2]
		else:
			if tmp[idx] > i[2]:
				tmp[idx] = i[2]

	updates = []

	for i in tmp:
		update(i[0], i[1], tmp[i])

print(f"Silver: {grid[0][0] - data[0][0]}")

data = []
grid = []
size = len(infile) * 5

for i in range(size): grid.append([int(1e9)] * size)
for i in range(size): data.append([int(0)] * size)

for i in range(size):
	for j in range(size):
		adder = (i // (size // 5)) + (j // (size // 5))
		data[i][j] = int(infile[i % (size // 5)][j % (size // 5)]) + adder
		if data[i][j] > 9:
			data[i][j] = data[i][j] % 10 + 1

updates = []
def update(x, y, cost):
	prop_cost = data[x][y] + cost

	if prop_cost < grid[x][y]:
		grid[x][y] = prop_cost
	else:
		return

	if x + 1 < size:
		if grid[x + 1][y] > data[x + 1][y] + grid[x][y]:
			updates.append([x + 1, y, grid[x][y]])
	if y + 1 < size:
		if grid[x][y + 1] > data[x][y + 1] + grid[x][y]:
			updates.append([x, y + 1, grid[x][y]])
	if x - 1 >= 0:
		if grid[x - 1][y] > data[x - 1][y] + grid[x][y]:
			updates.append([x - 1, y, grid[x][y]])
	if y - 1 >= 0:
		if grid[x][y - 1] > data[x][y - 1] + grid[x][y]:
			updates.append([x, y - 1, grid[x][y]])

update(size - 1, size - 1, 0)

while updates:
	tmp = {}
	for i in updates:
		idx = (i[0], i[1])

		if idx not in tmp:
			tmp[idx] = i[2]
		else:
			if tmp[idx] > i[2]:
				tmp[idx] = i[2]

	updates = []

	for i in tmp:
		update(i[0], i[1], tmp[i])

print(f"Gold: {grid[0][0] - data[0][0]}")
