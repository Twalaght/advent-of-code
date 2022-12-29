#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

cmds = []
for line in data:
	split = line.split()
	start, end = [int(x) for x in split[-3].split(",")], [int(x) for x in split[-1].split(",")]
	cmds.append({"cmd": split[-4], "start": start, "end": end})

s_grid, g_grid = [], []
for i in range(1000):
	s_grid.append([0] * 1000)
	g_grid.append([0] * 1000)

for cmd in cmds:
	for x in range(cmd["start"][0], cmd["end"][0] + 1):
		for y in range(cmd["start"][1], cmd["end"][1] + 1):
			if cmd["cmd"] == "toggle":
				s_grid[x][y] = (s_grid[x][y] + 1) % 2
				g_grid[x][y] += 2

			if cmd["cmd"] == "on":
				s_grid[x][y] = 1
				g_grid[x][y] += 1

			if cmd["cmd"] == "off":
				s_grid[x][y] = 0
				if g_grid[x][y] > 0: g_grid[x][y] -= 1

silver = sum([sum(line) for line in s_grid])
gold = sum([sum(line) for line in g_grid])
print(f"Silver: {silver}\nGold: {gold}")
