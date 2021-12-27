#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().split()[-2:]

x_rng = [int(x) for x in data[0][2:-1].split("..")]
y_rng = [int(y) for y in data[1][2:].split("..")]

valid_x, valid_y = {}, {}
for x_start in range(x_rng[1] + 1):
	dx = x_start
	x_pos = 0

	for t in range(500):
		x_pos += dx

		if x_rng[0] <= x_pos and x_pos <= x_rng[1]:
			if t not in valid_x: valid_x[t] = []
			valid_x[t].append(x_start)

		if dx > 0: dx -= 1

for y_start in range(y_rng[0], x_rng[1]):
	dy = y_start
	y_pos = 0

	for t in range(500):
		y_pos += dy

		if y_rng[0] <= y_pos and y_pos <= y_rng[1]:
			if t not in valid_y: valid_y[t] = []
			valid_y[t].append(y_start)

		dy -= 1

valid_starts = []
for t in [x for x in valid_x if x in valid_y]:
	valid_starts += [(x, y) for x in valid_x[t] for y in valid_y[t]]

high_y = max([i[1] for i in valid_starts])

silver = int((high_y * (high_y + 1)) / 2)
gold = len(set(valid_starts))
print(f"Silver: {silver}\nGold: {gold}")
