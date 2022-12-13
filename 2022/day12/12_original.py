#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

h, w = len(data), len(data[0])
start, end = [0, 0], [0, 0]
height = []
for y in range(h):
	tmp = []
	for x in range(w):
		val = ord(data[y][x]) - 96
		if data[y][x] == "S":
			start = (y, x)
			val = 1
		if data[y][x] == "E":
			end = (y, x)
			val = 26

		tmp.append(val)

	height.append(tmp)

cost = []
for i in range(h):
	tmp = [int(1e7) for _ in range(w)]
	cost.append(tmp)

cost[end[0]][end[1]] = 0

# send notifs from y, x
def send(y, x):
	lcl_height = height[y][x]
	lcl_cost = cost[y][x]

	notif = []
	# Top
	if y - 1 >= 0:
		if lcl_height - height[y - 1][x] <= 1:
			notif.append([(y - 1, x), lcl_cost + 1])
	# Bottom
	if y + 1 < h:
		if lcl_height - height[y + 1][x] <= 1:
			notif.append([(y + 1, x), lcl_cost + 1])

	# Left
	if x - 1 >= 0:
		if lcl_height - height[y][x - 1] <= 1:
			notif.append([(y, x - 1), lcl_cost + 1])

	# Right
	if x + 1 < w:
		if lcl_height - height[y][x + 1] <= 1:
			notif.append([(y, x + 1), lcl_cost + 1])

	return notif

msgs = []
msgs += send(end[0], end[1])


def update(msg):
	y, x = msg[0]
	if cost[y][x] > msg[1]:
		cost[y][x] = msg[1]
		return send(y, x)

	return []

while msgs:
	msg = msgs.pop(0)
	msgs += update(msg)

silver = cost[start[0]][start[1]]
gold = int(1e7)
for y in range(h):
	for x in range(w):
		if height[y][x] == 1:
			if cost[y][x] < gold:
				gold = cost[y][x]

print(f"Silver: {silver}\nGold: {gold}")
