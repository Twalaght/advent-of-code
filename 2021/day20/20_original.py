#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

light = {"#": "1", ".": "0"}
rule = [light[char] for char in data[0]]
grid = [[light[char] for char in line] for line in data[2:]]

def generate(grid, pad):
	extra = 5
	h = len(grid) + (extra * 2)
	w = len(grid[0]) + (extra * 2)

	for i in range(len(grid)):
		tmp = [pad] * extra
		grid[i] = tmp + grid[i] + tmp

	for i in range(extra):
		grid.insert(0, [pad] * w)
		grid.append([pad] * w)

	output = []
	for i in range(h - 2): output.append([pad] * (w - 2))

	for x in range(1, len(grid) - 1):
		for y in range(1, len(grid[x]) - 1):
			bstr = ""
			for i in range(-1, 2):
				for j in range(-1, 2):
					bstr += grid[x + i][y + j]

			output[x - 1][y - 1] = rule[int(bstr, 2)]

	return output

def count(grid):
	total = 0

	for line in grid:
		for char in line:
			if char == "1":
				total += 1

	return total

for rnd in range(50):
	pad = "0" if rnd % 2 == 0 else "1"
	grid = generate(grid, pad)

	if rnd == 1: print(f"Silver: {count(grid)}")
	if rnd == 49: print(f"Gold: {count(grid)}")
