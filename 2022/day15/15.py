#!/usr/bin/python3

import sys
from multiprocessing import Pool, cpu_count
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

def distance(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

scanners = []
full = set()
for line in data:
	tmp = line.replace(":", "").replace(",", "").split(" ")
	tmp = tuple([int(tmp[val][2:]) for val in [2, 3, 8, 9]])
	scanners.append(((tmp[0], tmp[1]), (tmp[2], tmp[3])))

def in_range(sensor, x, y):
	dist = abs(sensor[0][0] - x) + abs(sensor[0][1] - y)
	return dist <= distance(sensor[0], sensor[1])

def scan(scanners, y):
	ranges = []
	for s in scanners:
		dx = distance(s[0], s[1]) - abs(s[0][1] - y)
		ranges.append([s[0][0] - dx, s[0][0] + dx])

	silver = 0
	x = min([x[0] for x in ranges])
	for rng in sorted(ranges, key=lambda x: (x[0], x[1])):
		if rng[1] > x >= rng[0]:
			silver += (rng[1] - x)
			x = rng[1]

	return silver

def search(scanners, limit):
	gold = None
	for sc_a, sc_b in [(a, b) for i, a in enumerate(scanners) for b in scanners[i + 1:]]:
		mh_dist = distance(sc_b[0], sc_b[1]) + 1
		total = distance(sc_a[0], sc_a[1]) + 1 + mh_dist

		# Find two scanners who share a ring
		if distance(sc_a[0], sc_b[0]) != total: continue

		# Set initial coordinate and unit vector
		coord = [sc_b[0][0] + -mh_dist if sc_a[0][0] < sc_b[0][0] else mh_dist, sc_b[0][1]]
		vec = [1 if sc_a[0][0] < sc_b[0][0] else -1, -1 if sc_a[0][1] < sc_b[0][1] else 1]

		# Exit if out of bounds
		if coord[0] < 0 or coord[1] < 0 or coord[0] > limit or coord[1] > limit: continue

		while not gold:
			valid = True
			for s in scanners:
				# Get difference between point and nearest beacon to scanner
				diff = distance(s[0], s[1]) - distance(s[0], coord)
				if diff > 0:
					valid = False
					break

			if valid == True: return coord[0] * 4000000 + coord[1]

			# Jump forward depending on the distance
			multi = diff // 2 + 1 if diff > 0 else 1
			coord = [coord[0] + vec[0] * multi, coord[1] + vec[1] * multi]

silver, gold = scan(scanners, 2000000), search(scanners, 4000000)
print(f"Silver: {silver}\nGold: {gold}")
