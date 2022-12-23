#!/usr/bin/python3

import sys
from math import sqrt
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

cmd = data.pop().replace("R", " R ").replace("L", " L ").split()
cmd = [int(x) if x.isnumeric() else x for x in cmd]
data = [x.ljust(max([len(i) for i in data])) for x in data[:-1]]

# Determine side length of each face of the cube
s_len = int(sqrt(sum([len(x.strip()) for x in data]) // 6))

# Calculate grid ID for each distinct face of the cube
cube_ids = []
for y in range(len(data) // s_len):
	for x in range(len(data[0]) // s_len):
		y, x = y * s_len, x * s_len
		tmp = [i[x:x + s_len] for i in data[y:y + s_len]]
		if any([i.strip() for i in tmp]): cube_ids.append((x, y))

# Hardcoded transition matrix :(
trans = {(1,0): {0: (2,0,0), 1: (1,1,1), 2: (0,2,0), 3: (0,3,0)},
		(1,1): {0: (2,0,3), 1: (1,2,1), 2: (0,2,1), 3: (1,0,3)},
		(1,2): {0: (2,0,2), 1: (0,3,2), 2: (0,2,2), 3: (1,1,3)},
		(2,0): {0: (1,2,2), 1: (1,1,2), 2: (1,0,2), 3: (0,3,3)},
		(0,2): {0: (1,2,0), 1: (0,3,1), 2: (1,0,0), 3: (1,1,0)},
		(0,3): {0: (1,2,3), 1: (2,0,1), 2: (1,0,1), 3: (0,2,3)}}

# Calculate a jump around the cube
def wrap(goal, entry):
	new_pos = [None, None]

	# Goal -> right, origin -> left or top
	if goal[2] == 0:
		new_pos[0] = goal[0] * s_len
		if entry[2] == 2: new_pos[1] = (goal[1] + 1) * s_len - 1 - entry[1]
		if entry[2] == 3: new_pos[1] = goal[1] * s_len + entry[0]

	# Goal -> left, origin -> down or right
	if goal[2] == 2:
		new_pos[0] = (goal[0] + 1) * s_len - 1
		if entry[2] == 1: new_pos[1] = goal[1] * s_len + entry[0]
		if entry[2] == 0: new_pos[1] = (goal[1] + 1) * s_len - 1 - entry[1]

	# Goal -> down, origin -> left or down
	if goal[2] == 1:
		new_pos[1] = goal[1] * s_len
		if entry[2] == 2: new_pos[0] = goal[0] * s_len + entry[1]
		if entry[2] == 1: new_pos[0] = goal[0] * s_len + entry[0]

	# Goal -> up, origin -> right or up
	if goal[2] == 3:
		new_pos[1] = (goal[1]+1) * s_len - 1
		if entry[2] == 0: new_pos[0] = goal[0] * s_len + entry[1]
		if entry[2] == 3: new_pos[0] = goal[0] * s_len + entry[0]

	return new_pos

def move(pos, gold):
	new_dir = pos[2]
	vec = [(1, 0), (0, 1), (-1, 0), (0, -1)][pos[2]]
	new_pos = [(pos[0] + vec[0]) % len(data[pos[1]]),
				(pos[1] + vec[1]) % len(data)]

	if gold and data[new_pos[1]][new_pos[0]] == " ":
			goal = trans[(pos[0] // s_len, pos[1] // s_len)][pos[2]]
			new_dir = goal[2]
			entry = (pos[0] % s_len, pos[1] % s_len, pos[2])
			new_pos = wrap(goal, entry)
	else:
		while data[new_pos[1]][new_pos[0]] == " ":
			new_pos = [(new_pos[0] + vec[0]) % len(data[new_pos[1]]),
						(new_pos[1] + vec[1]) % len(data)]

	if data[new_pos[1]][new_pos[0]] == ".": return new_pos + [new_dir]
	if data[new_pos[1]][new_pos[0]] == "#": return pos

silver, gold = [[len(data[0]) - len(data[0].lstrip()), 0, 0] for _ in range(2)]
for c in cmd:
	if isinstance(c, int):
		for _ in range(c): silver, gold = move(silver, False), move(gold, True)
	else:
		silver[2] = (silver[2] + 1 if c == "R" else silver[2] - 1) % 4
		gold[2] = (gold[2] + 1 if c == "R" else gold[2] - 1) % 4

silver = 4 * (silver[0] + 1) + (1000 * (silver[1] + 1)) + silver[2]
gold = 4 * (gold[0] + 1) + (1000 * (gold[1] + 1)) + gold[2]
print(f"Silver: {silver}\nGold: {gold}")
