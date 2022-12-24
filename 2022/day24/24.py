#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

blizard = []
height, width = len(data), len(data[0])
cycle = (height - 2) * (width - 2) + 1
for t in range(cycle):
	state = set()
	for y in range(height):
		for x in range(width):
			if data[y][x] not in ">v<^": continue

			tmp = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}[data[y][x]]
			x_pos = x if tmp[0] == 0 else 1 + ((x - 1 + (tmp[0] * t)) % (width - 2))
			y_pos = y if tmp[1] == 0 else 1 + ((y - 1 + (tmp[1] * t)) % (height - 2))
			state.add((x_pos, y_pos))

	blizard.append(state)

silver, gold = 0, 0
mem = set()
queue = [(1, 0, 0, False, False)]
while queue:
	x, y, t, end, start = queue.pop(0)

	# If not in range, and not in a wall
	if not (0 <= y < height and 0 <= x < width and data[y][x] != "#"): continue

	if y == height - 1 and end and start:
		gold = t
		break

	if y == height - 1 and silver == 0: silver = t
	if y == height - 1: end = True
	if y == 0 and end: start = True

	if (x, y, t, end, start) in mem: continue
	mem.add((x, y, t, end, start))

	opts = [(x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
	opts = [x for x in opts if x not in blizard[(t + 1) % cycle]]
	for opt in opts: queue.append((*opt, t + 1, end, start))

print(f"Silver: {silver}\nGold: {gold}")
