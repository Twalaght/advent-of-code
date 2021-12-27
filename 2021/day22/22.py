#!/usr/bin/python3

import re
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

x_full, y_full, z_full = set(), set(), set()

cmds = []
for i in range(len(data)):
	cmd = data[i].split()[0] == "on"
	tmp = data[i].split()[1].split(",")

	full = [int(x) for x in re.findall("-?\d+", data[i].split()[1])]
	full = [full[i] + (i % 2) for i in range(len(full))]

	x_full.update(full[0:2])
	y_full.update(full[2:4])
	z_full.update(full[4:6])
	cmds.append(full + [cmd])

def transform(input_set):
	full = sorted(input_set)

	segment, length = {}, {}
	for i in range(len(full)):
		segment[full[i]] = i
		length[i] = full[i + 1] - full[i] if i + 1 < len(full) else 0

	return segment, length

for c_set in [x_full, y_full, z_full]:
	for x in [-50, 50]: c_set.add(x)

x_full, x_len = transform(x_full)
y_full, y_len = transform(y_full)
z_full, z_len = transform(z_full)

def solve(gold):
	cubes = set()
	for cmd in cmds:
		if not gold:
			for i in range(6):
				cmd[i] = max(cmd[i], -50) if i % 2 == 0 else min(cmd[i], 50)

		for x in range(x_full[cmd[0]], x_full[cmd[1]]):
			for y in range(y_full[cmd[2]], y_full[cmd[3]]):
				for z in range(z_full[cmd[4]], z_full[cmd[5]]):
					if cmd[6]:
						cubes.add((x, y, z))
					else:
						cubes.discard((x, y, z))

	res = 0
	for cube in cubes:
		x = x_len[cube[0]]
		y = y_len[cube[1]]
		z = z_len[cube[2]]
		res += x * y * z

	return res

gold = solve(True)
silver = solve(False)
print(f"Silver: {silver}\nGold: {gold}")
