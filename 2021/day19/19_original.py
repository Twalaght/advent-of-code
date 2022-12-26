#!/usr/bin/python3

import re
import math
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

data = re.split("--- scanner \d+ ---\n", data)[1:]
data = [[x for x in scan.splitlines() if x] for scan in data]

translator = {0:[(0, 1), (1, 1), (2, 1)]}
offset = {0:[0, 0, 0]}

def distance(start, end):
	start = [int(x) for x in start.split(",")]
	end = [int(x) for x in end.split(",")]
	rel = [start[0] - end[0], start[1] - end[1], start[2] - end[2]]
	d = (rel[0] ** 2) + (rel[1] ** 2) + (rel[2] ** 2)
	return int(math.sqrt(d))

full_dist = []
for scan in range(len(data)):
	scans = []
	for start in data[scan]:
		distances = []

		for end in data[scan]:
			if start == end: continue
			distances.append(distance(start, end))

		scans.append(distances)

	full_dist.append(scans)

def find_common(targ_1, targ_2):
	common = []
	for start in range(len(full_dist[targ_1])):
		test = full_dist[targ_1][start]

		for end in range(len(full_dist[targ_2])):
			tmp = [x for x in test if x in full_dist[targ_2][end]]
			if len(tmp) >= 11: common.append([data[targ_1][start], data[targ_2][end]])

	return common

overlap = []
for i in range(len(data)):
	for j in range(i + 1, len(data)):
		tmp = find_common(i, j)
		if len(tmp) >= 12: overlap.append([[i, j], tmp])

def offsetify(base, unk, inputs):
	base_data = [[int(x) for x in line[0].split(",")] for line in inputs]

	for i in range(len(base_data)):
		x = (base_data[i][translator[base][0][0]] * translator[base][0][1]) + offset[base][0]
		y = (base_data[i][translator[base][1][0]] * translator[base][1][1]) + offset[base][1]
		z = (base_data[i][translator[base][2][0]] * translator[base][2][1]) + offset[base][2]
		base_data[i] = [x, y, z]

	unk_data = [[int(x) for x in line[1].split(",")] for line in inputs]

	u_map = [None, None, None]
	for idx in range(3):
		for test in range(3):
			var = set()
			for i in range(len(base_data)):
				tmp = base_data[i][idx] - unk_data[i][test]
				var.add(tmp)

			if len(var) == 1:
				u_map[idx] = (test, 1)

		for test in range(3):
			var = set()
			for i in range(len(base_data)):
				tmp = base_data[i][idx] + unk_data[i][test]
				var.add(tmp)

			if len(var) == 1:
				u_map[idx] = (test, -1)

	os = [None, None, None]
	os[0] = base_data[0][0] - (unk_data[0][u_map[0][0]] * u_map[0][1])
	os[1] = base_data[0][1] - (unk_data[0][u_map[1][0]] * u_map[1][1])
	os[2] = base_data[0][2] - (unk_data[0][u_map[2][0]] * u_map[2][1])

	translator[unk] = u_map
	offset[unk] = os

while(overlap):
	union = overlap.pop(0)
	if union[0][0] in offset and union[0][1] in offset: continue
	if union[0][0] not in offset and union[0][1] not in offset:
		overlap.append(union)
		continue

	if union[0][0] in offset:
		offsetify(union[0][0], union[0][1], union[1])
	else:
		new_data = [[line[1], line[0]] for line in union[1]]
		offsetify(union[0][1], union[0][0], new_data)

beacons = set()
for scan in range(len(data)):
	for point in data[scan]:
		tmp = [int(x) for x in point.split(",")]

		x = (tmp[translator[scan][0][0]] * translator[scan][0][1]) + offset[scan][0]
		y = (tmp[translator[scan][1][0]] * translator[scan][1][1]) + offset[scan][1]
		z = (tmp[translator[scan][2][0]] * translator[scan][2][1]) + offset[scan][2]
		tmp = (x, y, z)

		beacons.add(tmp)

print(f"Silver: {len(beacons)}")

from itertools import combinations

gold = 0
combins = combinations(range(len(data)), 2)
for c in combins:
	left = offset[c[0]]
	right = offset[c[1]]

	x = abs(left[0] - right[0])
	y = abs(left[1] - right[1])
	z = abs(left[2] - right[2])

	manhattan = x + y + z

	if manhattan > gold: gold = manhattan

print(f"Gold: {gold}")
