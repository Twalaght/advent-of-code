#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

cmd = data.pop()
cmd = " R ".join(cmd.split("R"))
cmd = " L ".join(cmd.split("L"))
cmd = [int(x) if x.isnumeric() else x for x in cmd.split()]

max_len = max([len(x) for x in data])
data = [x.ljust(max_len) for x in data[:-1]]


pos = [len(data[0]) - len(data[0].lstrip()), 0, 0]

vecdef = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def rotate(cmd, direc):
	if cmd == "R":
		return (direc + 1) % 4
	else:
		return (direc - 1) % 4

def move(pos):
	vec = vecdef[pos[2]]
	new_pos = [pos[0], pos[1]]
	new_pos = [(new_pos[0] + vec[0]) % len(data[new_pos[1]]),
				(new_pos[1] + vec[1]) % len(data)]

	while data[new_pos[1]][new_pos[0]] == " ":
		new_pos = [(new_pos[0] + vec[0]) % len(data[new_pos[1]]),
					(new_pos[1] + vec[1]) % len(data)]

	if data[new_pos[1]][new_pos[0]] == ".":
		return new_pos + [pos[2]]

	if data[new_pos[1]][new_pos[0]] == "#":
		return pos

for c in cmd:
	if c in ["R", "L"]:
		pos[2] = rotate(c, pos[2])
	else:
		for _ in range(c):
			pos = move(pos)

silver = 4 * (pos[0] + 1) + (1000 * (pos[1] + 1)) + pos[2]

import math
s_len = int(math.sqrt(sum([len(x.strip()) for x in data]) / 6))

cube_ids = []

for row in range(len(data) // s_len):
	for col in range(len(data[0]) // s_len):
		tmp = data[row * s_len:row * s_len + s_len]
		tmp = [x[col * s_len:col * s_len + s_len] for x in tmp]

		if tmp[0].strip():
			cube_ids.append((col, row))

trans = {(1,0): {0: (2,0,0), 1: (1,1,1), 2: (0,2,0), 3: (0,3,0)},
		(1,1): {0: (2,0,3), 1: (1,2,1), 2: (0,2,1), 3: (1,0,3)},
		(1,2): {0: (2,0,2), 1: (0,3,2), 2: (0,2,2), 3: (1,1,3)},
		(2,0): {0: (1,2,2), 1: (1,1,2), 2: (1,0,2), 3: (0,3,3)},
		(0,2): {0: (1,2,0), 1: (0,3,1), 2: (1,0,0), 3: (1,1,0)},
		(0,3): {0: (1,2,3), 1: (2,0,1), 2: (1,0,1), 3: (0,2,3)}}

def reentry(goal, old):
	new_pos = [None, None]

	# If going to right
	if goal[2] == 0:
		new_pos[0] = goal[0] * s_len

		# Left to right
		if old[2] == 2:
			new_pos[1] = (goal[1]+1) * s_len - 1 - old[1]

		# Top to right
		if old[2] == 3:
			new_pos[1] = goal[1] * s_len + old[0]

	# Down to left
	if old[2] == 1 and goal[2] == 2:
		new_pos = [(goal[0]+1) * s_len - 1, goal[1] * s_len + old[0]]

	# Right to left
	if old[2] == 0 and goal[2] == 2:
		new_pos = [(goal[0]+1) * s_len - 1, (goal[1]+1) * s_len - 1 - old[1]]

	# Left to down
	if old[2] == 2 and goal[2] == 1:
		new_pos = [goal[0] * s_len + old[1], goal[1] * s_len]

	# Down to down
	if old[2] == 1 and goal[2] == 1:
		new_pos = [goal[0] * s_len + old[0], goal[1] * s_len]

	# Right to up
	if old[2] == 0 and goal[2] == 3:
		new_pos = [goal[0] * s_len + old[1], (goal[1]+1) * s_len - 1]

	# Up to up - 2,0 to 0,3
	if old[2] == 3 and goal[2] == 3:
		new_pos = [goal[0] * s_len + old[0], (goal[1]+1) * s_len - 1]

	return new_pos

def translate(pos):
	x = pos[0] // s_len
	y = pos[1] // s_len

	vec = vecdef[pos[2]]
	new_pos = [pos[0], pos[1]]
	new_pos = [(new_pos[0] + vec[0]) % len(data[new_pos[1]]),
				(new_pos[1] + vec[1]) % len(data)]

	new_d = pos[2]

	if data[new_pos[1]][new_pos[0]] == " ":
		tmp = trans[(x, y)][pos[2]]

		new_d = tmp[2]

		old = (pos[0] % s_len, pos[1] % s_len, pos[2])
		new_pos = reentry(tmp, old)

	if data[new_pos[1]][new_pos[0]] == ".":
		return new_pos + [new_d]

	if data[new_pos[1]][new_pos[0]] == "#":
		return pos

pos = [len(data[0]) - len(data[0].lstrip()), 0, 0]
for c in cmd:
	if c in ["R", "L"]:
		pos[2] = rotate(c, pos[2])
	else:
		for _ in range(c):
			pos = translate(pos)

gold = 4 * (pos[0] + 1) + (1000 * (pos[1] + 1)) + pos[2]

print(f"Silver: {silver}\nGold: {gold}")
