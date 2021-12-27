#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

data = data.split()[-2:]

x_rng = [int(x) for x in data[0][2:-1].split("..")]
y_rng = [int(y) for y in data[1][2:].split("..")]

valid_x = {}
for start in range(400):
	dx = start
	xpos = 0

	for t in range(1000):
		xpos += dx

		if xpos in range(x_rng[0], x_rng[1] + 1):
			if t not in valid_x:
				valid_x[t] = []

			valid_x[t].append(start)


		if dx > 0:
			dx -= 1

valid_y = {}
for start in range(-1000, 1000):
	dy = start
	ypos = 0

	for t in range(1000):
		ypos += dy


		if ypos in range(y_rng[0], y_rng[1] + 1):
			if t not in valid_y:
				valid_y[t] = []

			valid_y[t].append(start)

		dy -= 1

valid_starts = []
for i in valid_x:
	if i in valid_y:
		for x in valid_x[i]:
			for y in valid_y[i]:
				valid_starts.append((x, y))

highest_y = -9999
for i in valid_starts:
	if i[1] > highest_y:
		highest_y = i[1]

silver = int((highest_y * (highest_y + 1)) / 2)
gold = len(set(valid_starts))
print(f"Silver: {silver}\nGold: {gold}")
