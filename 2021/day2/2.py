#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

horiz, s_vert, g_vert, aim = 0, 0, 0, 0
for line in data:
	cmd, dist = line[0], int(line[1])

	if cmd == "forward":
		horiz += dist
		g_vert += dist * aim
	elif cmd == "up" or cmd == "down":
		aim += dist * (-1 if cmd == "up" else 1)
		s_vert += dist * (-1 if cmd == "up" else 1)

print(f"Silver: {horiz * s_vert}\nGold: {horiz * g_vert}")
