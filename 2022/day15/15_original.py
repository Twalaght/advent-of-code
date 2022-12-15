#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

scanners = []
items = set()
full = set()

for x in data:
	tmp = x.split(": ")

	sen = tmp[0].split("at ")[-1].split(", ")
	bec = tmp[1].split("at ")[-1].split(", ")

	sen = tuple([int(x[2:]) for x in sen])
	bec = tuple([int(x[2:]) for x in bec])

	full.add(sen)
	full.add(bec)

	manhattan = abs(sen[0] - bec[0]) + abs(sen[1] - bec[1])

	items.add(sen[0] - manhattan)
	items.add(sen[0] + manhattan)

	scanners.append((sen[0], sen[1], manhattan))

def in_range(sensor, x, y):
	manhattan = abs(sensor[0] - x) + abs(sensor[1] - y)
	if manhattan <= sensor[2]:
		return True
	else:
		return False

def bounds(scanners, y, max_x):
	tmp = []

	for s in scanners:
		dy = abs(s[1] - y)
		dx = s[2] - dy
		tmp.append([s[0] - dx, s[0] + dx])

	tmp = sorted(tmp, key=lambda x: (x[0],x[1]))

	x = 0
	for rng in tmp:
		if rng[0] <= x <= rng[1]:
			x = rng[1] + 1

	if x <= max_x:
		return x
	else:
		return None

scan_y = 2000000
search = 4000000
silver = 0
l = min(items)
r = max(items)
for i in range(l, r + 1):
	for s in scanners:
		if in_range(s, i, scan_y):
			tmp  = (i, scan_y)
			if tmp not in full: silver += 1
			break

for y in range(search + 1):
	res = bounds(scanners, y, search)
	if res:
		gold = res * 4000000 + y
		break

print(f"Silver: {silver}\nGold: {gold}")
