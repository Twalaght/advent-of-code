#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
silver, gold = "", ""

x, y = 1, 1
for moves in data:
	for move in moves:
		if move == "U" and y > 0:
			y -= 1
		if move == "D" and y < 2:
			y += 1
		if move == "L" and x > 0:
			x -= 1
		if move == "R" and x < 2:
			x += 1

	silver += str(pad[y][x])

pad = [
	[0, 0, 1, 0, 0],
	[0, 2, 3, 4, 0],
	[5, 6, 7, 8, 9],
	[0, "A", "B", "C", 0],
	[0, 0, "D", 0, 0],
]

x, y = 0, 2
for moves in data:
	for move in moves:
		if move == "U" and y > 0:
			if pad[y - 1][x] != 0:
				y -= 1
		if move == "D" and y < 4:
			if pad[y + 1][x] != 0:
				y += 1
		if move == "L" and x > 0:
			if pad[y][x - 1] != 0:
				x -= 1
		if move == "R" and x < 4:
			if pad[y][x + 1] != 0:
				x += 1

	gold += str(pad[y][x])

print(f"Silver: {silver}\nGold: {gold}")
