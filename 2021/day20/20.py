#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

rule = [{"#":"1", ".":"0"}[char] for char in data[0]]
grid = [[{"#":"1", ".":"0"}[char] for char in line] for line in data[2:]]

def generate(grid, pad):
	for i in range(len(grid)): grid[i] = [pad] * 2 + grid[i] + [pad] * 2
	grid = [[pad] * len(grid[0])] * 2 + grid + [[pad] * len(grid[0])] * 2

	output = []
	for i in range(len(grid) - 2): output.append([pad] * (len(grid[0]) - 2))

	for x in range(1, len(grid) - 1):
		for y in range(1, len(grid[x]) - 1):
			bstr = ""
			for i in range(-1, 2):
				for j in range(-1, 2):
					bstr += grid[x + i][y + j]

			output[x - 1][y - 1] = rule[int(bstr, 2)]

	return output

silver, gold = 0, 0
for rnd in range(50):
	grid = generate(grid, "0" if rnd % 2 == 0 else "1")
	if rnd == 1: silver = sum([sum([int(x) for x in line]) for line in grid])
	if rnd == 49: gold = sum([sum([int(x) for x in line]) for line in grid])

print(f"Silver: {silver}\nGold: {gold}")
