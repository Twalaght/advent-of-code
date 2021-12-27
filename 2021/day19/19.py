#!/usr/bin/python3

import re
import sys
from itertools import combinations
from math import sqrt
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

data = re.split("--- scanner \d+ ---\n", data)[1:]
data = [[x for x in scan.splitlines() if x] for scan in data]

cmap = {0:[(0, 1), (1, 1), (2, 1)]}
offset = {0:[0, 0, 0]}

def distance(start, end):
	start = [int(x) for x in start.split(",")]
	end = [int(x) for x in end.split(",")]
	dist = sum([(start[i] - end[i]) ** 2 for i in range(3)])
	return int(sqrt(dist))

def generate(data):
	return [[[distance(p1, p2) for p2 in scan if p1 != p2] for p1 in scan] for scan in data]

def find_common(left, right, dists):
	common = []
	for p1 in range(len(dists[left])):
		for p2 in range(len(dists[right])):
			share = [x for x in dists[left][p1] if x in dists[right][p2]]
			if len(share) >= 11: common.append([data[left][p1], data[right][p2]])

	return common

def calc_offset(base, new, inputs):
	data = [[int(x) for x in line[0].split(",")] for line in inputs]
	for i in range(len(data)):
		data[i] = [data[i][cmap[base][x][0]] * cmap[base][x][1] + offset[base][x] for x in range(3)]

	u_data = [[int(x) for x in line[1].split(",")] for line in inputs]

	u_map = [None, None, None]
	for idx in range(3):
		for test in range(6):
			bit = 1 if test < 3 else -1
			valid = set([data[i][idx] - bit * u_data[i][test % 3] for i in range(len(data))])
			if len(valid) == 1: u_map[idx] = (test % 3, bit)

	cmap[new] = u_map
	offset[new] = [data[0][i] - (u_data[0][u_map[i][0]] * u_map[i][1]) for i in range(3)]

def calc_overlap(dists):
	overlap = []
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			tmp = find_common(i, j, dists)
			if len(tmp) >= 12: overlap.append([[i, j], tmp])

	return overlap

def solve(data):
	dists = generate(data)
	overlap = calc_overlap(dists)

	while(overlap):
		union = overlap.pop(0)
		if union[0][0] in offset and union[0][1] in offset: continue
		if union[0][0] not in offset and union[0][1] not in offset:
			overlap.append(union)
			continue

		if union[0][0] in offset: calc_offset(union[0][0], union[0][1], union[1])
		else: calc_offset(union[0][1], union[0][0], [[line[1], line[0]] for line in union[1]])

solve(data)
silver = set()
for scan in range(len(data)):
	for point in data[scan]:
		tmp = [int(x) for x in point.split(",")]
		beacon = [tmp[cmap[scan][i][0]] * cmap[scan][i][1] + offset[scan][i] for i in range(3)]
		silver.add(tuple(beacon))

gold = 0
for c in combinations(range(len(data)), 2):
	manhattan = sum([abs(offset[c[0]][i] - offset[c[1]][i]) for i in range(3)])
	if manhattan > gold: gold = manhattan

print(f"Silver: {len(silver)}\nGold: {gold}")
