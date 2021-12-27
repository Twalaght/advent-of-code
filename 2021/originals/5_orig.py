#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

lines = []
for entry in data:
	tmp = entry.split()
	tmp = [[int(i) for i in tmp[0].split(",")], [int(i) for i in tmp[2].split(",")]]

	lines.append(tmp)
	# if tmp[0][0] == tmp[1][0] or tmp[0][1] == tmp[1][1]: lines.append(tmp)

grid = []
for i in range(1000): grid.append([0] * 1000)

for line in lines:

	uv_x = line[1][0] - line[0][0]
	uv_y = line[1][1] - line[0][1]
	length = max(abs(uv_x), abs(uv_y)) + 1

	# print((uv_x, uv_y))

	if uv_x != 0: uv_x /= abs(uv_x)
	if uv_y != 0: uv_y /= abs(uv_y)

	# print((uv_x, uv_y))

	x_cord, y_cord = line[0]

	for i in range(length):
		grid[int(x_cord)][int(y_cord)] += 1
		x_cord += uv_x
		y_cord += uv_y

twos = 0
for i in range(1000):
	for j in range(1000):
		if grid[i][j] > 1: twos += 1

print(twos)
