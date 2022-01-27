#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

axi_lines, ver_lines, grid = [], [], []
for i in range(1000): grid.append([0] * 1000)

for line in data:
	tmp = [[int(x) for x in line[0].split(",")], [int(x) for x in line[2].split(",")]]
	(axi_lines if tmp[0][0] == tmp[1][0] or tmp[0][1] == tmp[1][1] else ver_lines).append(tmp)

def draw(lines):
	for line in lines:
		uv = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
		length = max(abs(uv[0]), abs(uv[1])) + 1

		if uv[0] != 0: uv[0] //= abs(uv[0])
		if uv[1] != 0: uv[1] //= abs(uv[1])

		for i in range(length): grid[line[0][0] + (i * uv[0])][line[0][1] + (i * uv[1])] += 1

	return sum(x > 1 for x in [elem for row in grid for elem in row])

silver, gold = draw(axi_lines), draw(ver_lines)
print(f"Silver: {silver}\nGold: {gold}")
