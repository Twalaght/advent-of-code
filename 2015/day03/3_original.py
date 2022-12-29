#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read()

x, y = 0, 0
visited = {(x, y)}

for cmd in data:
	if cmd == "^":
		y += 1
	elif cmd == "v":
		y -= 1
	elif cmd == ">":
		x += 1
	elif cmd == "<":
		x -= 1

	visited.add((x, y))

print(f"Silver: {len(visited)}")

s_x, s_y = 0, 0
r_x, r_y = 0, 0
visited = {(s_x, s_y)}

for i in range(len(data)):
	cmd = data[i]

	if i % 2 == 0:
		if cmd == "^":
			s_y += 1
		elif cmd == "v":
			s_y -= 1
		elif cmd == ">":
			s_x += 1
		elif cmd == "<":
			s_x -= 1
	else:
		if cmd == "^":
			r_y += 1
		elif cmd == "v":
			r_y -= 1
		elif cmd == ">":
			r_x += 1
		elif cmd == "<":
			r_x -= 1

	visited.add((s_x, s_y))
	visited.add((r_x, r_y))

print(f"Gold: {len(visited)}")
